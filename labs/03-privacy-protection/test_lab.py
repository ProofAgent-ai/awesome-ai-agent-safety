import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "guards"))
spec = importlib.util.spec_from_file_location("lab03", HERE / "run.py")
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)

from guard import LocalGuard, Vault  # noqa: E402

SECRETS = ["4111 1111 1111 1111", "jane.doe@example.com", "+44 20 7946 0958", "GB33 BUKB 2020 1555 5555 55",
           "AKIAIOSFODNN7EXAMPLE", "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789", "hunter2hunter2"]


class Lab03(unittest.TestCase):
    def test_baseline_leaks_everything(self):
        seen = " ".join(lab.run_once(t, protect=False)[1][0] for t in lab.SAMPLES.values())
        for s in SECRETS:
            self.assertIn(s, seen)

    def test_guarded_model_never_sees_values(self):
        seen = " ".join(lab.run_once(t, protect=True)[1][0] for t in lab.SAMPLES.values())
        for s in SECRETS:
            self.assertNotIn(s, seen)

    def test_user_gets_real_values_back(self):
        answer, _ = lab.run_once(lab.SAMPLES["support ticket"], protect=True)
        self.assertIn("jane.doe@example.com", answer)

    def test_clean_text_untouched(self):
        _, seen = lab.run_once(lab.SAMPLES["clean text"], protect=True)
        self.assertEqual(seen[0], lab.SAMPLES["clean text"])

    def test_invalid_card_number_not_masked(self):
        masked, _ = LocalGuard().mask("Ticket 1234 5678 9012 3456 is open", Vault())
        self.assertIn("1234 5678 9012 3456", masked)

    def test_same_value_same_placeholder(self):
        v = Vault()
        masked, _ = LocalGuard().mask("a@b.co and again a@b.co", v)
        self.assertEqual(masked, "[EMAIL_1] and again [EMAIL_1]")


if __name__ == "__main__":
    unittest.main()
