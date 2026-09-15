import csv
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
BATCH_2 = {
    "api-schema-validation": "ASV-",
    "api-negative-testing": "ANT-",
    "api-idempotency-testing": "AIT-",
    "api-pagination-testing": "APT-",
    "api-rate-limit-testing": "ARL-",
    "api-version-compatibility-testing": "AVC-",
    "api-error-contract-testing": "AEC-",
    "ui-test-strategy": "UTS-",
    "ui-test-selector-review": "USR-",
    "ui-test-wait-strategy-review": "UWR-",
    "visual-regression-testing": "VRT-",
    "cross-browser-testing": "CBT-",
    "test-code-review": "TCR-",
    "mutation-testing-analysis": "MTA-",
    "mock-quality-review": "MQR-",
    "test-suite-health-analysis": "TSH-",
}
CASES = (
    "basic-success.yaml",
    "edge-incomplete-input.yaml",
    "edge-scope-boundary.yaml",
)


class V20Batch2SkillContractsTest(unittest.TestCase):
    def test_every_bilingual_package_has_required_files(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                package = ROOT / "skills" / language / "testing-types" / slug
                with self.subTest(language=language, slug=slug):
                    for relative in (
                        "SKILL.md",
                        f"prompts/{slug}.md",
                        "agents/openai.yaml",
                        "evals/eval.yaml",
                        *[f"evals/cases/{case}" for case in CASES],
                        "evals/trigger-prompts.csv",
                        "evals/local-rules.json",
                    ):
                        self.assertTrue((package / relative).is_file(), relative)

    def test_metadata_and_prompt_names_are_physical_slugs(self):
        for language in LANGUAGES:
            for slug, prefix in BATCH_2.items():
                package = ROOT / "skills" / language / "testing-types" / slug
                with self.subTest(language=language, slug=slug):
                    if not (package / "SKILL.md").is_file():
                        continue
                    skill_text = (package / "SKILL.md").read_text()
                    self.assertRegex(skill_text, rf"(?m)^name:\s*{re.escape(slug)}\s*$")
                    self.assertIn(prefix, (package / f"prompts/{slug}.md").read_text())
                    metadata = (package / "agents/openai.yaml").read_text()
                    self.assertRegex(metadata, rf"(?m)^\s*key:\s*['\"]?{re.escape(slug)}['\"]?\s*$")
                    local_rules = json.loads((package / "evals/local-rules.json").read_text())
                    self.assertEqual(slug, local_rules["skill"])

    def test_trigger_data_covers_four_modes_and_positive_negative_controls(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                path = ROOT / "skills" / language / "testing-types" / slug / "evals/trigger-prompts.csv"
                with self.subTest(language=language, slug=slug):
                    if not path.is_file():
                        continue
                    with path.open(newline="") as handle:
                        rows = list(csv.DictReader(handle))
                    self.assertTrue(rows)
                    self.assertEqual(
                        {"explicit", "implicit", "contextual", "negative"},
                        {row["mode"] for row in rows},
                    )
                    self.assertIn("true", {row["should_trigger"].lower() for row in rows})
                    self.assertIn("false", {row["should_trigger"].lower() for row in rows})

    def test_eval_lists_all_three_cases(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                path = ROOT / "skills" / language / "testing-types" / slug / "evals/eval.yaml"
                with self.subTest(language=language, slug=slug):
                    if not path.is_file():
                        continue
                    text = path.read_text()
                    for case in CASES:
                        self.assertIn(f"evals/cases/{case}", text)


if __name__ == "__main__":
    unittest.main()
