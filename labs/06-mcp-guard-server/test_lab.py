import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lab06", HERE / "run.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


def results(guard, approve=False):
    return {name: (r, ok) for name, _, _, r, ok in lab.run_all(guard, approve)}


class Lab06(unittest.TestCase):
    def test_baseline_lets_every_attack_through(self):
        res = results(lab.NoMCPGuard())
        self.assertTrue(all(not ok for n, (_, ok) in res.items() if not n.startswith("benign")), res)

    def test_guard_stops_every_attack_and_keeps_benign_task(self):
        res = results(lab.LocalMCPGuard())
        self.assertTrue(all(ok for _, ok in res.values()), res)
        self.assertEqual(res["benign: order lookup"][0]["action"], lab.ALLOW)

    def test_payment_is_held_then_resumed_only_with_matching_approval(self):
        g = lab.LocalMCPGuard()
        args = {"tool": "transfer_funds", "action": {"to_iban": "FR76", "amount": 48000}}
        held = g.call("check_before_execute", args)
        self.assertEqual(held["action"], lab.HOLD)
        apr = held["approval"]["id"]
        changed = {"tool": "transfer_funds", "action": {"to_iban": "FR76", "amount": 99000}, "approval": apr}
        self.assertEqual(g.call("check_before_execute", changed)["action"], lab.BLOCK)
        held = g.call("check_before_execute", args)["approval"]["id"]
        self.assertEqual(g.call("check_before_execute", {**args, "approval": held})["action"], lab.ALLOW)
        self.assertEqual(g.call("check_before_execute", {**args, "approval": held})["action"], lab.BLOCK)

    def test_remote_guard_fails_closed(self):
        g = lab.ProofAgentMCPGuard(api_key="test", url="http://127.0.0.1:9", timeout=1)
        self.assertEqual(g.call("check_reply", {"text": "hi"})["action"], lab.REVIEW)
        self.assertEqual(g.call("check_before_execute", {"tool": "bash", "action": "ls"})["action"], lab.HOLD)

    def test_parses_mcp_tool_results(self):
        p = lab.ProofAgentMCPGuard.parse_result
        self.assertEqual(p({"structuredContent": {"action": "BLOCK"}})["action"], "BLOCK")
        self.assertEqual(p({"content": [{"type": "text", "text": '{"action": "ALLOW", "use_this": "x"}'}]})["use_this"], "x")


if __name__ == "__main__":
    unittest.main()
