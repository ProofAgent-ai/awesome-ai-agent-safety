"""Deterministic checks for tool calls and MCP tool definitions.

Rules run before any model-based guard: they are instant, explainable and
cannot be talked out of a decision. A guard model then judges what they allow.
"""
from __future__ import annotations

import hashlib
import json
import re
from typing import Dict, List, Optional, Tuple

from guard import Decision, LocalGuard, normalise


def _type_ok(value, typ: str) -> bool:
    return {"string": isinstance(value, str), "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "boolean": isinstance(value, bool), "object": isinstance(value, dict),
            "array": isinstance(value, list)}.get(typ, True)


def validate_args(schema: Dict, args: Dict) -> List[str]:
    """A small JSON Schema subset: required, additionalProperties, type, pattern, enum, maxLength."""
    errors = []
    props = schema.get("properties", {})
    for req in schema.get("required", []):
        if req not in args:
            errors.append(f"missing required argument {req!r}")
    for k, v in args.items():
        if k not in props:
            if schema.get("additionalProperties", True) is False:
                errors.append(f"unexpected argument {k!r}")
            continue
        p = props[k]
        if "type" in p and not _type_ok(v, p["type"]):
            errors.append(f"{k!r} must be {p['type']}")
        if isinstance(v, str):
            if "pattern" in p and not re.search(p["pattern"], v):
                errors.append(f"{k!r} does not match {p['pattern']}")
            if "maxLength" in p and len(v) > p["maxLength"]:
                errors.append(f"{k!r} longer than {p['maxLength']}")
        if "enum" in p and v not in p["enum"]:
            errors.append(f"{k!r} must be one of {p['enum']}")
    return errors


class ToolPolicy:
    """Allowlist + schema + egress rules for tool calls.

    tools: {name: {"input_schema": {...}, "risk": {"side_effects": "none|internal|external",
            "destination_arg": "to", "requires_approval": "always|outside_allowlist|never"}}}
    """

    def __init__(self, tools: Dict[str, Dict], allowed_domains: Optional[List[str]] = None):
        self.tools = tools
        self.allowed_domains = [d.lower() for d in (allowed_domains or [])]

    def _domain_allowed(self, dest: str) -> bool:
        m = re.search(r"@([\w.-]+)$", dest) or re.search(r"https?://([\w.-]+)", dest)
        if not m:
            return False
        host = m.group(1).lower()
        return any(host == d or host.endswith("." + d) for d in self.allowed_domains)

    def check(self, name: str, args: Dict) -> Decision:
        spec = self.tools.get(name)
        if spec is None:
            return Decision("BLOCK", None, [f"unknown tool {name!r}"])
        errors = validate_args(spec.get("input_schema", {}), args)
        if errors:
            return Decision("BLOCK", None, errors)
        risk = spec.get("risk", {})
        rule = risk.get("requires_approval", "never")
        dest_arg = risk.get("destination_arg")
        if rule == "always":
            return Decision("REVIEW", json.dumps(args), [f"{name} always needs approval"])
        if rule == "outside_allowlist" and dest_arg:
            dest = str(args.get(dest_arg, ""))
            if re.fullmatch(r"\[[A-Z_]+_\d+\]", dest):
                return Decision("REVIEW", json.dumps(args), ["destination is masked personal data"])
            if not self._domain_allowed(dest):
                return Decision("REVIEW", json.dumps(args), [f"destination {dest!r} is outside the allowlist"])
        return Decision("ALLOW", json.dumps(args))


# --------------------------------------------------------------------------
# MCP tool definitions: poisoning and rug pulls
# --------------------------------------------------------------------------

def tool_fingerprint(tool: Dict) -> str:
    """Hash of everything the model reads about a tool. Pin it when the user approves the server."""
    canonical = json.dumps({k: tool.get(k) for k in ("name", "description", "inputSchema")}, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()


def scan_tool_definition(tool: Dict) -> List[str]:
    """Find instructions hidden in an MCP tool's description or schema (tool poisoning)."""
    text = json.dumps(tool, ensure_ascii=False)
    issues = [f"{f['id']}: {f.get('match', '')}".strip(": ") for f in LocalGuard().findings(text)]
    norm = normalise(text).lower()
    for phrase, why in [
        ("before using this tool", "pre-condition that asks the model to do something else first"),
        ("sidenote", "hidden side-channel argument"),
        ("instead of", "redirection of another tool's behaviour"),
        ("when this tool is available", "cross-tool shadowing"),
        ("all other tools", "cross-tool shadowing"),
    ]:
        if phrase in norm:
            issues.append(f"suspicious phrase {phrase!r}: {why}")
    for name in (tool.get("inputSchema") or {}).get("properties", {}):
        if re.search(r"(note|context|feedback|sidenote|extra|debug|content_of)", name, re.I):
            issues.append(f"suspicious parameter {name!r} that can carry exfiltrated data")
    return issues


class ToolRegistry:
    """Approve MCP tools once, then refuse any that change (rug pull) or carry instructions."""

    def __init__(self):
        self.pinned: Dict[str, str] = {}

    def approve(self, tools: List[Dict]) -> List[Tuple[str, List[str]]]:
        rejected = []
        for t in tools:
            issues = scan_tool_definition(t)
            if issues:
                rejected.append((t["name"], issues))
            else:
                self.pinned[t["name"]] = tool_fingerprint(t)
        return rejected

    def verify(self, tool: Dict) -> Decision:
        pin = self.pinned.get(tool["name"])
        if pin is None:
            return Decision("BLOCK", None, [f"tool {tool['name']!r} was never approved"])
        if pin != tool_fingerprint(tool):
            return Decision("BLOCK", None, [f"tool {tool['name']!r} changed since approval (possible rug pull)"])
        return Decision("ALLOW", tool["name"])
