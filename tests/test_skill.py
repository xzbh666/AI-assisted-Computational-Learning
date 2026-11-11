"""Dependency-free smoke checks. Run: python -m unittest discover -s tests -v"""
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "code-to-understanding"


class SmokeTests(unittest.TestCase):
    def test_manifest(self):
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "code-to-understanding")
        self.assertEqual(manifest["version"], "0.1.0")
        ui = manifest["extensions"]["com.openai"]["interface"]
        self.assertLessEqual(len(ui["shortDescription"]), 30)

    def test_skill_files(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: code-to-understanding\n"))
        for ref in ("learning-playbook.md", "assessment-bank.md"):
            self.assertTrue((SKILL / "references" / ref).is_file())
            self.assertIn(ref, text)
        for mode in ("quick", "learn", "deep"):
            self.assertIn(mode, text)

    def test_example(self):
        path = SKILL / "scripts" / "newsvendor_demo.py"
        spec = importlib.util.spec_from_file_location("newsvendor_demo", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertAlmostEqual(module.critical_fractile(), 2 / 3)
        self.assertEqual(module.optimal_order(), 20)
        self.assertAlmostEqual(module.expected_profit(10), 60)
        self.assertAlmostEqual(module.expected_profit(20), 102)
        self.assertAlmostEqual(module.expected_profit(30), 99)


if __name__ == "__main__":
    unittest.main()
