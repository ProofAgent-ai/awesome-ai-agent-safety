"""Lab 03: keep personal data and secrets away from the model, locally, on CPU.

Mask before the model sees anything, keep a placeholder table (the vault) on
your side, and restore real values only where they are needed: in the tool call
that runs on your machine, or in the reply the user reads.

    python3 labs/03-privacy-protection/run.py
    python3 labs/03-privacy-protection/run.py --guard proofagent
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "guards"))
from guard import LocalGuard, Vault, get_guard  # noqa: E402

SAMPLES = {
    "support ticket": ("Hi, I'm Jane. My card 4111 1111 1111 1111 was charged twice. "
                       "Call me on +44 20 7946 0958 or email jane.doe@example.com."),
    "bank transfer": "Please refund to IBAN GB33 BUKB 2020 1555 5555 55, reference INV-2231.",
    "leaked config": ("DEBUG=true\nAWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE\n"
                      "GITHUB_TOKEN=ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789\npassword = hunter2hunter2"),
    "clean text": "What are your opening hours on Sunday?",
}


class FakeModel:
    """Stands in for a hosted LLM. Records everything it was sent."""

    def __init__(self):
        self.seen = []

    def reply(self, prompt: str) -> str:
        self.seen.append(prompt)
        return f"Thanks, I have noted the details: {prompt[:200]}"


def run_once(text: str, protect: bool, guard=None):
    model = FakeModel()
    if not protect:
        return model.reply(text), model.seen
    vault = Vault()
    guard = guard or LocalGuard()
    try:
        d = guard.check(text, "input", vault=vault)
    except TypeError:
        d = guard.check(text, "input")
    if d.blocked:
        return "[blocked]", model.seen
    answer = model.reply(d.text)
    return vault.restore(answer), model.seen   # the user sees real values, the model never did


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", default=None)
    guard = get_guard(ap.parse_args().guard)
    for name, text in SAMPLES.items():
        _, seen_raw = run_once(text, protect=False)
        answer, seen = run_once(text, protect=True, guard=guard)
        print(f"== {name}")
        print(f"  model sees (unprotected): {seen_raw[0]!r}")
        print(f"  model sees (guarded):     {seen[0]!r}" if seen else "  model sees (guarded): nothing (blocked)")
        print(f"  user reads (restored):    {answer[:140]!r}\n")


if __name__ == "__main__":
    main()
