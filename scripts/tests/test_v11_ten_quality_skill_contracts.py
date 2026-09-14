from __future__ import annotations

import csv
import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
TRIGGER_MODES = {"explicit", "implicit", "contextual", "negative"}

NEW_SLUGS = (
    "business-rule-extraction",
    "technical-design-quality-review",
    "api-design-quality-review",
    "database-design-quality-review",
    "observability-design-review",
    "error-handling-design-review",
    "test-scope-analysis",
)

ENHANCEMENTS = {
    "business-rule-consistency-review": {
        "target": "requirement-consistency-analysis",
        "mode_markers": ("business-rule", "business_rule"),
        "artifact_markers": ("BR-",),
        "case_names": (
            "business-rule-success.yaml",
            "business-rule-incomplete-input.yaml",
            "business-rule-scope-boundary.yaml",
        ),
        "aliases": ("business-rule-consistency-review", "business rule", "业务规则"),
        "preserved_markers": ("RC-",),
    },
    "architecture-testability-review": {
        "target": "testability-analysis",
        "mode_markers": ("architecture",),
        "artifact_markers": ("seam", "substitute", "fault injection", "替身"),
        "case_names": (
            "architecture-success.yaml",
            "architecture-incomplete-input.yaml",
            "architecture-unsafe-seam-boundary.yaml",
        ),
        "aliases": ("architecture-testability-review", "architecture", "架构"),
        "preserved_markers": (
            ("observability", "可观察", "可观测"),
            ("controllability", "可控制"),
            ("isolation", "隔离"),
        ),
    },
    "test-coverage-analysis": {
        "target": "requirement-traceability-analysis",
        "mode_markers": ("coverage_analysis",),
        "artifact_markers": ("TC-",),
        "case_names": (
            "coverage-success.yaml",
            "coverage-incomplete-input.yaml",
            "coverage-scope-boundary.yaml",
        ),
        "aliases": ("test-coverage-analysis", "coverage analysis", "coverage_analysis", "覆盖分析"),
        "preserved_markers": (("RT-",), ("complete", "完整"), ("unexecuted", "未执行"), ("unassessed", "未评估")),
    },
}


def package_path(language: str, slug: str) -> Path:
    return REPO_ROOT / "skills" / language / "testing-types" / slug


def read_trigger_rows(package: Path) -> list[dict[str, str]]:
    path = package / "evals" / "trigger-prompts.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def assert_trigger_contract(test: unittest.TestCase, package: Path) -> list[dict[str, str]]:
    rows = read_trigger_rows(package)
    test.assertEqual({row.get("mode") for row in rows}, TRIGGER_MODES, package)
    test.assertEqual({row.get("should_trigger") for row in rows}, {"true", "false"}, package)
    test.assertEqual(len(rows), len({row.get("id") for row in rows}), package)
    test.assertTrue(all((row.get("prompt") or "").strip() for row in rows), package)
    return rows


class V11TenQualitySkillContractTest(unittest.TestCase):
    def test_new_packages_have_required_bilingual_contract(self):
        required_files = (
            "SKILL.md",
            "agents/openai.yaml",
            "evals/eval.yaml",
        )
        required_cases = (
            "basic-success.yaml",
            "edge-incomplete-input.yaml",
            "edge-scope-boundary.yaml",
        )

        for language in LANGUAGES:
            for slug in NEW_SLUGS:
                package = package_path(language, slug)
                for relative_path in required_files:
                    self.assertTrue((package / relative_path).is_file(), package / relative_path)
                self.assertTrue(
                    (package / "prompts" / f"{slug}.md").is_file(),
                    package / "prompts" / f"{slug}.md",
                )
                for case_name in required_cases:
                    self.assertTrue((package / "evals" / "cases" / case_name).is_file(), package / case_name)

                rows = assert_trigger_contract(self, package)
                self.assertTrue(any(row["should_trigger"] == "true" for row in rows), package)
                self.assertTrue(any(row["should_trigger"] == "false" for row in rows), package)

                rules = json.loads((package / "evals" / "local-rules.json").read_text(encoding="utf-8"))
                self.assertEqual(rules.get("skill"), slug, package)

    def test_enhancements_use_strong_mode_contracts_without_alias_directories(self):
        for candidate, contract in ENHANCEMENTS.items():
            target_slug = contract["target"]
            for language in LANGUAGES:
                target = package_path(language, target_slug)
                self.assertFalse(package_path(language, candidate).exists(), f"duplicate alias: {candidate}")

                skill_text = (target / "SKILL.md").read_text(encoding="utf-8")
                prompt_text = (
                    target / "prompts" / f"{target_slug}.md"
                ).read_text(encoding="utf-8")
                combined = f"{skill_text}\n{prompt_text}"
                normalized = combined.casefold()

                self.assertTrue(
                    any(marker.casefold() in normalized for marker in contract["mode_markers"]),
                    f"missing mode marker for {candidate} in {target}",
                )
                self.assertTrue(
                    any(marker.casefold() in normalized for marker in contract["artifact_markers"]),
                    f"missing artifact marker for {candidate} in {target}",
                )
                for marker in contract["preserved_markers"]:
                    alternatives = marker if isinstance(marker, tuple) else (marker,)
                    self.assertTrue(
                        any(alternative.casefold() in normalized for alternative in alternatives),
                        f"missing preserved marker {alternatives} in {target}",
                    )

                cases_dir = target / "evals" / "cases"
                for case_name in contract["case_names"]:
                    self.assertTrue((cases_dir / case_name).is_file(), cases_dir / case_name)

                rows = assert_trigger_contract(self, target)
                prompt_texts = "\n".join((row.get("prompt") or "").casefold() for row in rows)
                self.assertTrue(
                    any(alias.casefold() in prompt_texts for alias in contract["aliases"]),
                    f"missing candidate alias in trigger prompts for {candidate}",
                )

                rules = json.loads((target / "evals" / "local-rules.json").read_text(encoding="utf-8"))
                self.assertEqual(rules.get("skill"), target_slug, target)


if __name__ == "__main__":
    unittest.main()
