from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_docs_bilingual import (
    PROJECT_PAIRS,
    check_catalog,
    check_chinese_readme_metadata_leak,
    check_project_pairs,
    check_relative_links,
)


class DocsBilingualCheckTest(unittest.TestCase):
    def test_docs_and_language_skill_indexes_are_registered_as_bilingual_pairs(self):
        self.assertIn(("docs/README.md", "docs/README_EN.md"), PROJECT_PAIRS)
        self.assertIn(("skills/zh/README.md", "skills/en/README.md"), PROJECT_PAIRS)

    def test_current_review_reports_are_registered_as_bilingual_pairs(self):
        expected_pairs = (
            (
                "docs/reviews/2026-09-10-requirement-strategy-governance.md",
                "docs/reviews/2026-09-10-requirement-strategy-governance_EN.md",
            ),
            (
                "docs/reviews/2026-10-06-all-skills-review.md",
                "docs/reviews/2026-10-06-all-skills-review_EN.md",
            ),
            (
                "docs/reviews/2026-10-07-all-skills-repair-review.md",
                "docs/reviews/2026-10-07-all-skills-repair-review_EN.md",
            ),
            (
                "docs/reviews/2026-10-07-review-runtime-followup.md",
                "docs/reviews/2026-10-07-review-runtime-followup_EN.md",
            ),
            (
                "docs/reviews/2026-10-08-review-runtime-continuation.md",
                "docs/reviews/2026-10-08-review-runtime-continuation_EN.md",
            ),
            (
                "docs/reviews/2026-10-09-free-qa-skills-learning-review.md",
                "docs/reviews/2026-10-09-free-qa-skills-learning-review_EN.md",
            ),
            (
                "docs/reviews/2026-10-16-ai-native-qa-development-landscape.md",
                "docs/reviews/2026-10-16-ai-native-qa-development-landscape_EN.md",
            ),
            (
                "docs/reviews/2026-10-16-all-skills-review-update.md",
                "docs/reviews/2026-10-16-all-skills-review-update_EN.md",
            ),
            (
                "docs/reviews/2026-10-25-github-qa-skills-iteration-research.md",
                "docs/reviews/2026-10-25-github-qa-skills-iteration-research_EN.md",
            ),
        )

        for pair in expected_pairs:
            with self.subTest(pair=pair):
                self.assertIn(pair, PROJECT_PAIRS)

    def test_sqet_entrypoints_are_registered_as_bilingual_project_pairs(self):
        expected_pairs = (
            (
                "docs/skill-quality-engineering/README.md",
                "docs/skill-quality-engineering/README_EN.md",
            ),
            (
                "docs/skill-quality-engineering/SKILL_QUALITY_EVALUATION_MODEL.md",
                "docs/skill-quality-engineering/SKILL_QUALITY_EVALUATION_MODEL_EN.md",
            ),
            (
                "docs/skill-quality-engineering/SKILL_EVAL_CONTRACT.md",
                "docs/skill-quality-engineering/SKILL_EVAL_CONTRACT_EN.md",
            ),
            (
                "docs/skill-quality-engineering/SKILL_QUALITY_PILOT.md",
                "docs/skill-quality-engineering/SKILL_QUALITY_PILOT_EN.md",
            ),
            ("evals/README.md", "evals/README_EN.md"),
            (
                "evidence/skill-quality/README.md",
                "evidence/skill-quality/README_EN.md",
            ),
        )

        for pair in expected_pairs:
            with self.subTest(pair=pair):
                self.assertIn(pair, PROJECT_PAIRS)

    def test_composition_catalog_is_registered_as_a_bilingual_pair(self):
        self.assertIn(
            ("docs/catalog/skills-composition.md", "docs/catalog/skills-composition_EN.md"),
            PROJECT_PAIRS,
        )

    def test_reports_missing_english_mirror(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("README_EN.md", encoding="utf-8")
            findings = check_project_pairs(root)
            self.assertIn("missing English mirror: README_EN.md", findings)

    def test_reports_missing_reverse_switch(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("README_EN.md", encoding="utf-8")
            (root / "README_EN.md").write_text("English only", encoding="utf-8")
            findings = check_project_pairs(root)
            self.assertIn("missing Chinese switch link: README_EN.md", findings)

    def test_reports_broken_relative_markdown_link(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "docs").mkdir()
            (root / "docs/guide.md").write_text(
                "See [missing](./missing.md) and [web](https://example.com).\n",
                encoding="utf-8",
            )
            findings = check_relative_links(root, ("docs/guide.md",))
            self.assertEqual(
                findings,
                ["broken relative link in docs/guide.md: ./missing.md"],
            )

    def test_ignores_links_inside_fenced_code(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "guide.md").write_text(
                "```markdown\n[example](./not-a-real-file.md)\n```\n",
                encoding="utf-8",
            )
            self.assertEqual(check_relative_links(root, ("guide.md",)), [])

    def test_reports_english_metadata_leak_in_chinese_readme(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text(
                "Use this skill when you need an English catalog entry.\n",
                encoding="utf-8",
            )
            self.assertEqual(
                check_chinese_readme_metadata_leak(root),
                ["English Skill metadata leaked into README.md"],
            )

    def test_catalog_reports_duplicate_and_missing_markers(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for lang in ("zh", "en"):
                (root / f"skills/{lang}/testing-types/alpha").mkdir(parents=True)
                (root / f"skills/{lang}/testing-types/beta").mkdir(parents=True)
            body = "<!-- data-skill:alpha -->\n<!-- data-skill:alpha -->\n"
            (root / "README.md").write_text(body, encoding="utf-8")
            (root / "README_EN.md").write_text(body, encoding="utf-8")
            findings = check_catalog(root)
            self.assertTrue(any("duplicate Skill markers" in item for item in findings))
            self.assertTrue(any("missing Skill markers" in item for item in findings))

    def test_catalog_reports_language_directory_drift(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "skills/zh/testing-types/alpha").mkdir(parents=True)
            (root / "skills/en/testing-types/beta").mkdir(parents=True)
            (root / "README.md").write_text("", encoding="utf-8")
            (root / "README_EN.md").write_text("", encoding="utf-8")
            findings = check_catalog(root)
            self.assertIn("zh/en testing-type directory names differ", findings)


if __name__ == "__main__":
    unittest.main()
