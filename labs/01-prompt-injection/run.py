"""Lab 01: detect direct and indirect prompt injection, and measure it.

    python3 labs/01-prompt-injection/run.py                  # local rules, offline
    python3 labs/01-prompt-injection/run.py --guard proofagent
    python3 labs/01-prompt-injection/run.py --guard none     # the unprotected baseline
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "guards"))
from guard import get_guard  # noqa: E402

CHECKPOINT = {"user": "input"}   # everything else arrives through a tool


def load_corpus():
    return [json.loads(line) for line in (HERE / "corpus.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]


def evaluate(guard, corpus):
    rows = []
    for item in corpus:
        cp = CHECKPOINT.get(item["source"], "tool_result")
        d = guard.check(item["text"], cp)
        # On tool results, "MASK" with instructions removed counts as a detection
        flagged = d.action in ("BLOCK", "REVIEW") or (cp == "tool_result" and d.action == "MASK"
                                                       and any("instruction" in r or "LLM01" in r or "LLM02" in r
                                                               for r in d.reasons))
        rows.append({**item, "checkpoint": cp, "action": d.action, "flagged": flagged, "reasons": d.reasons})
    return rows


def metrics(rows):
    core = [r for r in rows if not r.get("known_gap")]
    attacks = [r for r in core if r["label"] == "attack"]
    benign = [r for r in core if r["label"] == "benign"]
    gaps = [r for r in rows if r.get("known_gap")]
    return {
        "detection_rate": sum(r["flagged"] for r in attacks) / len(attacks),
        "false_positive_rate": sum(r["flagged"] for r in benign) / len(benign),
        "evasions_caught": f"{sum(r['flagged'] for r in gaps)}/{len(gaps)}",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", default=None, help="none | local | proofagent (default: $GUARD or local)")
    args = ap.parse_args()
    guard = get_guard(args.guard)
    rows = evaluate(guard, load_corpus())
    print(f"guard: {guard.name}\n")
    print(f"{'id':<6} {'source':<12} {'category':<22} {'label':<7} {'action':<7} result")
    for r in rows:
        ok = r["flagged"] == (r["label"] == "attack")
        mark = "ok" if ok else ("MISSED" if r["label"] == "attack" else "FALSE POSITIVE")
        if r.get("known_gap") and not r["flagged"]:
            mark = "missed (known gap for rules)"
        print(f"{r['id']:<6} {r['source']:<12} {r['category']:<22} {r['label']:<7} {r['action']:<7} {mark}")
    m = metrics(rows)
    print(f"\ndetection rate {m['detection_rate']:.0%} · false positive rate {m['false_positive_rate']:.0%} "
          f"· evasions caught {m['evasions_caught']}")


if __name__ == "__main__":
    main()
