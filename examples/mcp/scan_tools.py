#!/usr/bin/env python3
"""Scan and pin an MCP server's tools before your agent loads them.

    # save a server's tools/list response (e.g. from MCP Inspector) to tools.json, then:
    python3 examples/mcp/scan_tools.py tools.json                 # report issues
    python3 examples/mcp/scan_tools.py tools.json --pin pins.json # approve clean tools
    python3 examples/mcp/scan_tools.py tools.json --verify pins.json   # in CI: fail on changes

Accepts {"tools": [...]} or a bare list.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "guards"))
from tool_policy import scan_tool_definition, tool_fingerprint  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("tools")
ap.add_argument("--pin")
ap.add_argument("--verify")
a = ap.parse_args()
data = json.loads(Path(a.tools).read_text())
tools = data.get("tools", data) if isinstance(data, dict) else data

bad = 0
for t in tools:
    issues = scan_tool_definition(t)
    bad += bool(issues)
    print(f"{'REJECT' if issues else 'ok    '} {t['name']}")
    for i in issues:
        print(f"         - {i}")

if a.pin:
    pins = {t["name"]: tool_fingerprint(t) for t in tools if not scan_tool_definition(t)}
    Path(a.pin).write_text(json.dumps(pins, indent=2))
    print(f"pinned {len(pins)} tools to {a.pin}")
if a.verify:
    pins = json.loads(Path(a.verify).read_text())
    for t in tools:
        if pins.get(t["name"]) != tool_fingerprint(t):
            print(f"CHANGED {t['name']} (not pinned or modified since approval)")
            bad += 1
sys.exit(1 if bad else 0)
