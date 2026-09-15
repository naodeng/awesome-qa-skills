from __future__ import annotations

import json
from pathlib import Path
import unittest

from scripts.tests.v11_contract_helpers import assert_trigger_contract


REPO_ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")

NEW_SLUGS = (
    "business-rule-extraction",
    "technical-design-quality-review",
    "api-design-quality-review",
    "database-design-quality-review",
    "observability-design-review",
    "error-handling-design-review",
    "test-scope-analysis",
)

REQUIREMENT_SLUGS = (
    "requirement-quality-review",
    "requirement-ambiguity-analysis",
    "requirement-consistency-analysis",
    "requirement-conflict-detection",
    "requirement-traceability-analysis",
)

TEST_DESIGN_SLUGS = (
    "test-gap-analysis",
    "risk-based-testing",
    "edge-case-discovery",
    "negative-scenario-discovery",
    "test-data-requirement-analysis",
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


class V11TenQualitySkillContractTest(unittest.TestCase):
    def test_new_packages_follow_the_repository_skill_and_prompt_skeleton(self):
        skill_headings = {
            "zh": ("## 何时使用", "## 输出格式选项", "## 如何使用", "## 参考文件", "## 常见误区", "## 最佳实践"),
            "en": ("## When to Use", "## Output Format Options", "## How to Use", "## Reference Files", "## Common Pitfalls", "## Best Practices"),
        }
        prompt_headings = {
            "zh": ("## 输入", "## 你要做的事", "## 执行规则", "## 最低覆盖清单", "## 输出", "## 质量要求"),
            "en": ("## Input", "## What to Do", "## Execution Rules", "## Minimum Coverage", "## Output", "## Quality Requirements"),
        }
        for language in LANGUAGES:
            for target_slug in (*REQUIREMENT_SLUGS, *NEW_SLUGS, *TEST_DESIGN_SLUGS):
                package = package_path(language, target_slug)
                skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                prompt_text = (package / "prompts" / f"{target_slug}.md").read_text(encoding="utf-8")
                for heading in skill_headings[language]:
                    self.assertIn(heading, skill_text, f"missing {heading}: {package / 'SKILL.md'}")
                for heading in prompt_headings[language]:
                    self.assertIn(heading, prompt_text, f"missing {heading}: {package / 'prompts' / f'{target_slug}.md'}")

    def test_new_skills_have_capability_match_records(self):
        registry = json.loads(
            (REPO_ROOT / "docs" / "governance" / "skill-governance-registry.yaml").read_text(encoding="utf-8")
        )
        candidates = {entry.get("slug"): entry for entry in registry.get("candidates", [])}
        for slug in NEW_SLUGS:
            self.assertIn(slug, candidates)
            self.assertEqual(candidates[slug].get("conclusion"), "NEW")
            self.assertTrue(candidates[slug].get("target_evidence_paths"), slug)

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

    def test_database_findings_include_the_specified_per_finding_fields(self):
        required_fields = (
            "Object",
            "Scope",
            "Source",
            "Evidence",
            "Design Rule",
            "Finding",
            "Impact",
            "Severity",
            "Constraint",
            "Index Risk",
            "Transaction",
            "Concurrency",
            "Migration",
            "Rollback",
            "Owner",
            "Validation",
        )
        for language in LANGUAGES:
            prompt = (
                package_path(language, "database-design-quality-review")
                / "prompts"
                / "database-design-quality-review.md"
            ).read_text(encoding="utf-8")
            for field in required_fields:
                self.assertIn(field, prompt, f"missing {field} in {language} database prompt")

    def test_specialized_findings_include_the_specified_fields(self):
        specialized_fields = {
            "observability-design-review": ("Covered Object", "Expected Semantics"),
            "error-handling-design-review": ("Caller-Visible Result", "Observable Evidence"),
        }
        for language in LANGUAGES:
            for slug, fields in specialized_fields.items():
                prompt = (package_path(language, slug) / "prompts" / f"{slug}.md").read_text(encoding="utf-8")
                for field in fields:
                    self.assertIn(field, prompt, f"missing {field} in {language} {slug} prompt")

            edge_prompt = (
                package_path(language, "edge-case-discovery")
                / "prompts"
                / "edge-case-discovery.md"
            ).read_text(encoding="utf-8")
            self.assertIn("Unresolved Questions", edge_prompt, f"missing per-finding questions in {language} edge-case prompt")

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
