import csv
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASES = (
    "prompt-regression-basic-success.yaml",
    "prompt-regression-missing-baseline.yaml",
    "prompt-regression-scope-boundary.yaml",
)
EXISTING_CASES = (
    "basic-success.yaml",
    "edge-incomplete-input.yaml",
    "edge-risk-priority.yaml",
)
LANGUAGES = ("zh", "en")
REQUIRED_TERMS = {
    "zh": (
        "基线",
        "候选版本",
        "数据集",
        "预期行为",
        "观察到的行为",
        "证据状态",
        "差异",
        "验证方法",
        "Human",
    ),
    "en": (
        "baseline",
        "candidate version",
        "dataset",
        "expected behavior",
        "observed behavior",
        "evidence state",
        "difference",
        "validation method",
        "Human",
    ),
}


class V34PromptRegressionContractTest(unittest.TestCase):
    def package(self, language):
        return ROOT / "skills" / language / "testing-types" / "prompt-testing"

    def test_enhancement_has_no_alias_skill_directory(self):
        for language in LANGUAGES:
            with self.subTest(language=language):
                self.assertFalse(
                    (ROOT / "skills" / language / "testing-types" / "prompt-regression-testing").exists()
                )

    def test_entrypoints_expose_prompt_regression_mode(self):
        for language in LANGUAGES:
            package = self.package(language)
            with self.subTest(language=language):
                skill = (package / "SKILL.md").read_text(encoding="utf-8")
                prompt = (package / "prompts/prompt-testing.md").read_text(encoding="utf-8")
                self.assertIn("prompt-regression", skill)
                self.assertIn("PRT-", skill)
                self.assertIn("prompt-regression", prompt)
                self.assertRegex(prompt, r"(?m)^### PRT-## ")
                for term in REQUIRED_TERMS[language]:
                    self.assertIn(term, prompt)
                if language == "en":
                    body = skill.split("---", 2)[2]
                    self.assertIsNone(re.search(r"[\u4e00-\u9fff]", body))

    def test_eval_keeps_existing_cases_and_adds_regression_cases(self):
        for language in LANGUAGES:
            path = self.package(language) / "evals/eval.yaml"
            text = path.read_text(encoding="utf-8")
            with self.subTest(language=language):
                for case in (*EXISTING_CASES, *CASES):
                    self.assertIn(f"evals/cases/{case}", text)

    def test_regression_cases_have_mode_prefix_and_boundary_contract(self):
        for language in LANGUAGES:
            cases_dir = self.package(language) / "evals/cases"
            combined = "\n".join(
                (cases_dir / case).read_text(encoding="utf-8") for case in CASES
            )
            with self.subTest(language=language):
                self.assertIn("prompt-regression", combined)
                self.assertIn("PRT-", combined)
                for case in CASES:
                    self.assertTrue((cases_dir / case).is_file(), case)
                boundary = (cases_dir / "prompt-regression-scope-boundary.yaml").read_text(
                    encoding="utf-8"
                )
                forbidden = (
                    ("测试已执行", "全部测试通过", "发布已批准")
                    if language == "zh"
                    else ("tests were executed", "all tests passed", "release approved")
                )
                for phrase in forbidden:
                    self.assertIn(phrase, boundary)

    def test_regression_trigger_rows_and_local_rules_are_explicit(self):
        for language in LANGUAGES:
            package = self.package(language)
            trigger_path = package / "evals/trigger-prompts.csv"
            rules_path = package / "evals/local-rules.json"
            with self.subTest(language=language):
                with trigger_path.open(newline="", encoding="utf-8") as handle:
                    rows = list(csv.DictReader(handle))
                regression_rows = [row for row in rows if row["mode"] == "prompt-regression"]
                self.assertTrue(regression_rows)
                self.assertIn("true", {row["should_trigger"].lower() for row in regression_rows})
                self.assertIn("false", {row["should_trigger"].lower() for row in regression_rows})
                self.assertEqual(
                    "prompt-testing",
                    json.loads(rules_path.read_text(encoding="utf-8"))["skill"],
                )
                self.assertIn(
                    "prompt-regression",
                    json.loads(rules_path.read_text(encoding="utf-8"))["modes"],
                )


if __name__ == "__main__":
    unittest.main()
