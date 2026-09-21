from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class DiscoverTestingPromptContractTest(unittest.TestCase):
    def test_composition_reference_is_not_an_exhaustive_registry(self) -> None:
        expectations = {
            "zh": {
                "scoped_rule": "未命中时，按仓库现有 Skill 与路由规则选择",
                "global_rule": "只有当前仓库和本地 `reference.md` 中存在的 Skill 才可调用。",
            },
            "en": {
                "scoped_rule": "when no route matches, keep using the existing routing rules below",
                "global_rule": "Only Skills present in the repository and local `reference.md` are callable.",
            },
        }

        for language, expected in expectations.items():
            prompt = (
                ROOT
                / "skills"
                / language
                / "testing-workflows"
                / "discover-testing"
                / "prompts"
                / "discover-testing.md"
            ).read_text(encoding="utf-8")
            with self.subTest(language=language):
                self.assertIn(expected["scoped_rule"], prompt)
                self.assertNotIn(expected["global_rule"], prompt)

    def test_capability_stage_eval_does_not_require_roadmap_wording(self) -> None:
        paths = (
            ROOT / "skills/zh/testing-workflows/discover-testing/evals/cases/capability-stage-routing.yaml",
            ROOT / "skills/en/testing-workflows/discover-testing/evals/cases/capability-stage-routing.yaml",
        )

        for path in paths:
            content = path.read_text(encoding="utf-8")
            expect_section = content.split("expect:", 1)[1].split("judge:", 1)[0]
            judge_section = content.split("judge:", 1)[1]
            with self.subTest(path=path):
                self.assertIn("ai-feature-testing", expect_section)
                self.assertNotIn('"路线图"', expect_section)
                self.assertNotIn('"roadmap"', expect_section)
                self.assertNotIn('"路线图"', judge_section)
                self.assertNotIn('"roadmap"', judge_section)


if __name__ == "__main__":
    unittest.main()
