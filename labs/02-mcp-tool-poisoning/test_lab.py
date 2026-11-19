import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "guards"))
spec = importlib.util.spec_from_file_location("lab02", HERE / "run.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)

from guard import LocalGuard  # noqa: E402
from tool_policy import ToolPolicy, ToolRegistry, scan_tool_definition  # noqa: E402


class Lab02(unittest.TestCase):
    def test_baseline_loads_poisoned_tools(self):
        self.assertIn("add_numbers", lab.naive_client(lab.SERVER_TOOLS))

    def test_poisoned_descriptions_rejected_clean_one_kept(self):
        reg = ToolRegistry()
        loaded, rejected = lab.guarded_client(lab.SERVER_TOOLS, reg)
        self.assertEqual(loaded, ["get_weather"])
        self.assertEqual({n for n, _ in rejected}, {"add_numbers", "send_message"})

    def test_clean_tool_has_no_issues(self):
        self.assertEqual(scan_tool_definition(lab.SERVER_TOOLS[0]), [])

    def test_rug_pull_blocked(self):
        reg = ToolRegistry()
        reg.approve(lab.SERVER_TOOLS)
        self.assertEqual(reg.verify(lab.SERVER_TOOLS[0]).action, "ALLOW")
        self.assertEqual(reg.verify(lab.RUG_PULL).action, "BLOCK")

    def test_poisoned_result_cleaned(self):
        d = LocalGuard().check(lab.POISONED_RESULT, "tool_result")
        self.assertEqual(d.action, "MASK")
        self.assertIn("Paris", d.text)
        self.assertNotIn("evil.test", d.text)

    def test_schema_blocks_smuggled_argument(self):
        policy = ToolPolicy({"get_weather": {"input_schema": lab.SERVER_TOOLS[0]["inputSchema"]}})
        self.assertEqual(policy.check("get_weather", {"city": "Paris"}).action, "ALLOW")
        self.assertEqual(policy.check("get_weather", {"city": "Paris", "extra": "x"}).action, "BLOCK")
        self.assertEqual(policy.check("add_numbers", {"a": 1, "b": 2}).action, "BLOCK")


if __name__ == "__main__":
    unittest.main()
