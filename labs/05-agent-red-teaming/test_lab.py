import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "guards"))
spec = importlib.util.spec_from_file_location("lab05", HERE / "run.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)

from guard import LocalGuard, NoGuard  # noqa: E402


class Lab05(unittest.TestCase):
    def test_baseline_fails_every_scenario(self):
        findings = lab.campaign(NoGuard())
        self.assertTrue(all(f["succeeded"] for f in findings), [f["id"] for f in findings if not f["succeeded"]])

    def test_guarded_defends_every_scenario(self):
        findings = lab.campaign(LocalGuard())
        self.assertFalse(any(f["succeeded"] for f in findings), [f["id"] for f in findings if f["succeeded"]])

    def test_paraphrase_is_caught_late_by_output_canary(self):
        f = {x["id"]: x for x in lab.campaign(LocalGuard())}["RT-02"]
        self.assertIn("3-output", f["stopped_by"])

    def test_report_has_rate_and_rows(self):
        md = lab.report_md("none", lab.campaign(NoGuard()))
        self.assertIn("Attack success rate: **100%**", md)
        self.assertIn("RT-07", md)


if __name__ == "__main__":
    unittest.main()
