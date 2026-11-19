"""Run every lab's tests: python3 run_tests.py  (no dependencies, Python 3.9+)"""
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
suite = unittest.TestSuite()
for i, test_file in enumerate(sorted(ROOT.glob("labs/*/test_*.py")) + sorted(ROOT.glob("tests/test_*.py"))):
    spec = importlib.util.spec_from_file_location(f"t{i}_{test_file.parent.name.replace('-', '_')}", test_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(mod))
result = unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
