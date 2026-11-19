"""One guard interface for every lab.

    from guard import get_guard
    g = get_guard()                       # GUARD=local (default) | proofagent
    d = g.check(text, checkpoint="input") # input | tool_call | tool_result | output
    if d.blocked: ...
    if d.needs_review: ...
    use(d.text)                           # original, masked or cleaned text

Backends
--------
* ``local``      Offline, zero dependencies, CPU only. Transparent regex rules,
                 good for learning and for CI. NOT production grade: rules are
                 easy to evade (paraphrase, other languages, encodings).
* ``proofagent`` ProofAgent Nano over HTTP (free tier at app.proofagent.ai).
                 Set PROOFAGENT_NANO_API_KEY. Fails closed on any error.

Adding a backend (NeMo Guardrails, Guardrails AI, LLM Guard, Lakera, Llama
Prompt Guard ...) means writing one class with a ``check`` method. PRs welcome:
see CONTRIBUTING.md.
"""
from __future__ import annotations

import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Dict, List, Optional

CHECKPOINTS = ("input", "tool_call", "tool_result", "output")
ACTIONS = ("ALLOW", "MASK", "REVIEW", "BLOCK")


@dataclass
class Decision:
    action: str                                  # ALLOW | MASK | REVIEW | BLOCK
    text: Optional[str]                          # text to use next (None when blocked)
    reasons: List[str] = field(default_factory=list)
    raw: Dict = field(default_factory=dict)

    @property
    def blocked(self) -> bool:
        return self.action == "BLOCK"

    @property
    def needs_review(self) -> bool:
        return self.action == "REVIEW"


class Guard:
    name = "base"

    def check(self, text: str, checkpoint: str = "input") -> Decision:  # pragma: no cover
        raise NotImplementedError


class NoGuard(Guard):
    """The unprotected baseline: everything passes."""
    name = "none"

    def check(self, text: str, checkpoint: str = "input") -> Decision:
        return Decision("ALLOW", text)


# --------------------------------------------------------------------------
# Local rule-based guard
# --------------------------------------------------------------------------

# (pattern, risk id, owasp) - instructions that try to take control of the agent
INJECTION_RULES = [
    (r"\b(ignore|disregard|forget|override)\b.{0,40}\b(previous|prior|above|earlier|all|your|system)\b.{0,30}\b(instructions?|rules|prompts?|directions?|guidelines)",
     "prompt_injection", "LLM01"),
    (r"\b(you are now|from now on,? you are|act as|pretend to be)\b.{0,40}\b(DAN|developer mode|jailbroken|unfiltered|no (rules|restrictions|limits))",
     "jailbreak", "LLM01"),
    (r"\b(do anything now|developer mode enabled|no ethical (guidelines|restrictions))\b", "jailbreak", "LLM01"),
    (r"\b(reveal|print|show|repeat|output|leak)\b.{0,30}\b(system prompt|hidden instructions|initial instructions|your instructions)",
     "system_prompt_leak", "LLM07"),
    (r"\b(new|updated|important|urgent)\s+(instructions?|task|system (message|note))\s*[:!]", "prompt_injection", "LLM01"),
    (r"<\s*(important|system|instructions?|admin)\s*>", "prompt_injection", "LLM01"),
    (r"\b(ai|assistant|agent|llm|model|claude|gpt)\b\s*[:,]?\s*(please\s+)?(must|should|now)?\s*(ignore|email|send|forward|upload|exfiltrate|delete)\b",
     "prompt_injection", "LLM01"),
    (r"\bdo not (tell|inform|mention (this|it) to|notify) the user\b", "prompt_injection", "LLM01"),
    (r"\b(send|email|forward|upload|post|exfiltrate|transmit)\b.{0,60}\b(customer list|all (customers|users|records)|database|credentials|passwords?|api keys?|\.env|id_rsa|ssh key|secrets?)\b",
     "data_exfiltration", "LLM02"),
    (r"(~|\$HOME)?/?\.(ssh/id_[a-z0-9]+|aws/credentials|env\b|netrc|config/gcloud)", "sensitive_file_access", "LLM02"),
    (r"\bcurl\b.{0,80}(\|\s*(ba)?sh|-d\s*@|--data(-binary)?\s*@)", "data_exfiltration", "LLM02"),
    (r"!\[[^\]]*\]\(https?://[^)]*\?[^)]*(data|q|d|secret|token)=", "markdown_image_exfiltration", "LLM02"),
    (r"\brm\s+-rf\s+(/|~|\*)", "destructive_command", "LLM06"),
    (r"\b(drop\s+table|truncate\s+table|delete\s+from\s+\w+\s*;?\s*$)", "destructive_command", "LLM06"),
]

# Hidden carriers for instructions: HTML comments, zero-width and tag characters, bidi controls
HIDDEN_RULES = [
    (r"<!--.*?-->", "hidden_html_comment"),
    (r"[​-‏⁠-⁤﻿]", "zero_width_characters"),
    (r"[\U000e0000-\U000e007f]", "unicode_tag_characters"),
    (r"[‪-‮⁦-⁩]", "bidi_control_characters"),
]

PII_RULES = [
    ("EMAIL", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    ("CARD", r"\b\d(?:[ -]?\d){12,18}\b"),
    ("IBAN", r"\b[A-Z]{2}\d{2}(?:[ ]?[A-Z0-9]{4}){3,7}(?:[ ]?[A-Z0-9]{1,3})?\b"),
    ("US_SSN", r"\b\d{3}-\d{2}-\d{4}\b"),
    ("IP_ADDRESS", r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    ("PHONE", r"(?<![\w+])(?:\+\d{1,3}|\(\d{2,4}\)|0\d)[\d ().-]{6,16}\d\b"),
]

SECRET_RULES = [
    ("AWS_ACCESS_KEY", r"\bAKIA[0-9A-Z]{16}\b"),
    ("GITHUB_TOKEN", r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    ("OPENAI_KEY", r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    ("ANTHROPIC_KEY", r"\bsk-ant-[A-Za-z0-9_-]{20,}\b"),
    ("SLACK_TOKEN", r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    ("STRIPE_KEY", r"\b[sr]k_live_[A-Za-z0-9]{20,}\b"),
    ("PRIVATE_KEY", r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    ("JWT", r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    ("PASSWORD_ASSIGNMENT", r"(?i)\b(password|passwd|pwd|secret|api[_-]?key|token)\s*[:=]\s*['\"]?[^\s'\"]{6,}"),
]


def _luhn_ok(digits: str) -> bool:
    d = [int(c) for c in digits if c.isdigit()]
    if not 13 <= len(d) <= 19:
        return False
    total = 0
    for i, n in enumerate(reversed(d)):
        if i % 2:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def normalise(text: str) -> str:
    """Fold look-alike characters and remove invisible ones before matching rules."""
    t = unicodedata.normalize("NFKC", text)
    t = re.sub(r"[​-‏⁠-⁤﻿‪-‮⁦-⁩]", "", t)
    # Unicode tag characters smuggle ASCII: decode them so the rules can read it
    t = "".join(chr(ord(c) - 0xE0000) if 0xE0020 <= ord(c) <= 0xE007E else c for c in t)
    return t


class LocalGuard(Guard):
    """Transparent, offline rules. Learn with it; do not ship it alone."""
    name = "local"

    def __init__(self, mask_pii: bool = True, mask_secrets: bool = True):
        self.mask_pii = mask_pii
        self.mask_secrets = mask_secrets

    def findings(self, text: str) -> List[Dict]:
        out: List[Dict] = []
        norm = normalise(text)
        for pat, rid, owasp in INJECTION_RULES:
            m = re.search(pat, norm, re.I | re.S)
            if m:
                out.append({"kind": "risk", "id": rid, "owasp": owasp, "match": m.group(0)[:120]})
        for pat, rid in HIDDEN_RULES:
            if re.search(pat, text, re.S):
                out.append({"kind": "hidden", "id": rid, "owasp": "LLM01"})
        return out

    def mask(self, text: str, vault: Optional["Vault"] = None) -> (str, List[Dict]):
        spans: List[Dict] = []
        rules = (SECRET_RULES if self.mask_secrets else []) + (PII_RULES if self.mask_pii else [])
        for kind, pat in rules:
            def sub(m, kind=kind):
                value = m.group(0)
                if kind == "CARD" and not _luhn_ok(value):
                    return value
                if kind == "PHONE" and sum(c.isdigit() for c in value) < 8:
                    return value
                token = vault.put(kind, value) if vault is not None else f"[{kind}]"
                spans.append({"kind": kind, "token": token})
                return token
            text = re.sub(pat, sub, text)
        return text, spans

    def check(self, text: str, checkpoint: str = "input", vault: Optional["Vault"] = None) -> Decision:
        if checkpoint not in CHECKPOINTS:
            raise ValueError(f"checkpoint must be one of {CHECKPOINTS}")
        found = self.findings(text)
        risks = [f for f in found if f["kind"] == "risk"]
        hidden = [f for f in found if f["kind"] == "hidden"]
        reasons = [f"{f['id']} ({f['owasp']})" for f in found]

        if checkpoint == "tool_result" and (risks or hidden):
            # Indirect injection: keep the data, drop the instructions.
            cleaned = sanitise(text)
            cleaned, spans = self.mask(cleaned, vault)
            return Decision("MASK", cleaned, ["instructions removed from tool result"] + reasons,
                            raw={"findings": found, "spans": spans})
        if risks:
            return Decision("BLOCK", None, reasons, raw={"findings": found})

        masked, spans = self.mask(text, vault)
        if checkpoint == "tool_call" and spans:
            # Personal data or secrets leaving through a tool: a human decides.
            return Decision("REVIEW", masked, [f"{s['kind']} in tool arguments" for s in spans],
                            raw={"spans": spans})
        if spans:
            return Decision("MASK", masked, [f"{s['kind']} masked" for s in spans], raw={"spans": spans})
        if hidden:
            return Decision("MASK", sanitise(text), reasons, raw={"findings": found})
        return Decision("ALLOW", text)


def sanitise(text: str) -> str:
    """Remove hidden carriers and sentences that read as instructions to the agent.

    JSON stays valid JSON: each string value is cleaned on its own.
    """
    try:
        data = json.loads(text)
    except (ValueError, TypeError):
        return _sanitise_prose(text)
    if not isinstance(data, (dict, list)):
        return _sanitise_prose(text)

    def walk(v):
        if isinstance(v, dict):
            return {k: walk(x) for k, x in v.items()}
        if isinstance(v, list):
            return [walk(x) for x in v]
        if isinstance(v, str):
            cleaned = _sanitise_prose(v)
            return cleaned if cleaned else "[removed by guardrail]"
        return v
    return json.dumps(walk(data), ensure_ascii=False)


def _sanitise_prose(text: str) -> str:
    t = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    t = re.sub(r"<\s*(important|system|instructions?|admin)\s*>.*?<\s*/\s*\1\s*>", "", t, flags=re.S | re.I)
    t = normalise(t)
    kept = []
    for sentence in re.split(r"(?<=[.!?\n])\s+", t):
        if any(re.search(p, sentence, re.I | re.S) for p, _, _ in INJECTION_RULES):
            continue
        kept.append(sentence)
    return " ".join(kept).strip()


class Vault:
    """Placeholder <-> real value table, kept on your side, never sent to the model."""

    def __init__(self):
        self._by_token: Dict[str, str] = {}
        self._by_value: Dict[str, str] = {}
        self._n: Dict[str, int] = {}

    def put(self, kind: str, value: str) -> str:
        if value in self._by_value:
            return self._by_value[value]
        self._n[kind] = self._n.get(kind, 0) + 1
        token = f"[{kind}_{self._n[kind]}]"
        self._by_token[token] = value
        self._by_value[value] = token
        return token

    def restore(self, text: str) -> str:
        for token, value in self._by_token.items():
            text = text.replace(token, value)
        return text

    def __len__(self):
        return len(self._by_token)


# --------------------------------------------------------------------------
# ProofAgent Nano over HTTP
# --------------------------------------------------------------------------

_NANO_DIRECTION = {"input": "input", "tool_call": "output", "tool_result": "tool", "output": "output"}
_NANO_ACTION = {"PASS": "ALLOW", "FLAG": "ALLOW", "MASK": "MASK", "SANITISE": "MASK",
                "REVIEW": "REVIEW", "GUARDIAN_ALERT": "REVIEW", "BLOCK": "BLOCK"}


def _load_dotenv():
    env = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env):
        for line in open(env, encoding="utf-8"):
            k, sep, v = line.strip().partition("=")
            if sep and not k.startswith("#"):
                os.environ.setdefault(k.strip(), v.strip().strip("\"'"))


class ProofAgentGuard(Guard):
    """ProofAgent Nano (https://nano.proofagent.ai). Fails closed on any error."""
    name = "proofagent"

    def __init__(self, api_key: Optional[str] = None, url: Optional[str] = None, timeout: float = 10):
        _load_dotenv()
        self.api_key = api_key or os.environ.get("PROOFAGENT_NANO_API_KEY")
        self.url = (url or os.environ.get("PROOFAGENT_NANO_URL", "https://nano.proofagent.ai")).rstrip("/")
        self.timeout = timeout
        if not self.api_key:
            raise RuntimeError("Set PROOFAGENT_NANO_API_KEY (free key at https://app.proofagent.ai) or use GUARD=local")

    def _post(self, body: Dict, retries: int = 3) -> Dict:
        req = urllib.request.Request(
            f"{self.url}/v1/scan", data=json.dumps(body).encode(), method="POST",
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"})
        for attempt in range(retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    return json.load(resp)
            except urllib.error.HTTPError as e:
                if e.code != 429 or attempt == retries:
                    raise
                time.sleep(min(float(e.headers.get("Retry-After") or 2 ** attempt), 20))
        return {}

    def check(self, text: str, checkpoint: str = "input", vault=None) -> Decision:
        body = {"text": text, "direction": _NANO_DIRECTION[checkpoint]}
        if checkpoint == "tool_call":
            body["destination"] = "external_tool"
        try:
            r = self._post(body)
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            return Decision("BLOCK", None, [f"guard unavailable, failing closed: {e}"])
        action = _NANO_ACTION.get((r.get("decision") or {}).get("action"), "BLOCK")
        masked = (r.get("text") or {}).get("masked") or text
        summary = (r.get("report") or {}).get("summary")
        return Decision(action, None if action == "BLOCK" else masked, [summary] if summary else [], raw=r)


def get_guard(name: Optional[str] = None) -> Guard:
    name = (name or os.environ.get("GUARD", "local")).lower()
    if name in ("none", "off"):
        return NoGuard()
    if name == "local":
        return LocalGuard()
    if name in ("proofagent", "nano"):
        return ProofAgentGuard()
    raise ValueError(f"unknown guard {name!r}: use none, local or proofagent")
