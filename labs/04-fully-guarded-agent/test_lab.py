import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "guards"))
spec = importlib.util.spec_from_file_location("lab04", HERE / "run.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)

import agent as A  # noqa: E402
from guard import LocalGuard, NoGuard  # noqa: E402

ATTACKS = {"direct injection", "jailbreak", "indirect injection in a web page",
           "personal data in a tool result", "data sent outside the company"}


class Lab04(unittest.TestCase):
    def test_unguarded_agent_is_unsafe(self):
        res = {n: ok for n, ok, _ in lab.run_all(NoGuard())}
        self.assertTrue(all(not res[a] for a in ATTACKS), res)

    def test_guarded_agent_is_safe_and_still_useful(self):
        res = {n: ok for n, ok, _ in lab.run_all(LocalGuard())}
        self.assertTrue(all(res.values()), res)

    def test_human_approval_releases_held_email(self):
        agent = lab.build(LocalGuard(), approve=True)
        A.OUTBOX.clear()
        agent.run("Email my order A1234 summary to books@acme-accounting.com")
        self.assertEqual([m["to"] for m in A.OUTBOX], ["books@acme-accounting.com"])

    def test_each_checkpoint_fires(self):
        seen = set()
        for _, _, res in lab.run_all(LocalGuard()):
            seen |= {e.checkpoint for e in res.events if e.action != "ALLOW"}
        self.assertTrue({"1-input", "2a-policy", "2b-tool-result"} <= seen, seen)

    def test_output_guard_catches_canary(self):
        class LeakyModel:
            def plan(self, messages):
                return A.Step(reply=f"Sure: {A.SYSTEM_PROMPT}")
        agent = A.GuardedAgent(A.DEMO_TOOLS, model=LeakyModel(), guard=LocalGuard(), policy=A.demo_policy())
        res = agent.run("hello")
        self.assertNotIn(A.CANARY, res.reply)
        self.assertIn("3-output", res.stopped_at())


if __name__ == "__main__":
    unittest.main()
