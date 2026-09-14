from __future__ import annotations

import csv
import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SLUGS = (
    "requirement-quality-review",
    "requirement-ambiguity-analysis",
    "requirement-consistency-analysis",
    "requirement-conflict-detection",
    "requirement-traceability-analysis",
)
LANGUAGES = ("zh", "en")
TRIGGER_MODES = {"explicit", "implicit", "contextual", "negative"}


class V11RequirementQualityContractTest(unittest.TestCase):
    def test_each_package_has_a_local_trigger_dataset_and_rule_config(self):
        for slug in SLUGS:
            for language in LANGUAGES:
                package = REPO_ROOT / "skills" / language / "testing-types" / slug
                prompt_path = package / "evals" / "trigger-prompts.csv"
                rules_path = package / "evals" / "local-rules.json"

                self.assertTrue(prompt_path.is_file(), prompt_path)
                self.assertTrue(rules_path.is_file(), rules_path)

                with prompt_path.open(encoding="utf-8", newline="") as stream:
                    rows = list(csv.DictReader(stream))
                self.assertEqual(
                    {row.get("mode") for row in rows},
                    TRIGGER_MODES,
                    f"{language}/{slug} must cover all trigger modes",
                )
                self.assertEqual({row.get("should_trigger") for row in rows}, {"true", "false"})
                self.assertEqual(len(rows), len({row.get("id") for row in rows}))
                self.assertTrue(all((row.get("prompt") or "").strip() for row in rows))

                rules = json.loads(rules_path.read_text(encoding="utf-8"))
                self.assertEqual(rules.get("skill"), slug)

    def test_consistency_contract_separates_relation_and_status(self):
        for language in LANGUAGES:
            package = REPO_ROOT / "skills" / language / "testing-types" / "requirement-consistency-analysis"
            for path in (package / "SKILL.md", package / "prompts" / "requirement-consistency-analysis.md"):
                text = path.read_text(encoding="utf-8")
                self.assertIn("Status" if language == "en" else "状态", text, path)
                self.assertIn("aligned", text, path)
                self.assertIn("inconsistent", text, path)
                self.assertIn("unassessed", text, path)

            prompt = (package / "prompts" / "requirement-consistency-analysis.md").read_text(encoding="utf-8")
            self.assertRegex(prompt, r"\| `Status` \|" if language == "en" else r"\| `状态` \|")
            self.assertRegex(prompt, r"`assessed`[^\n]*`missing`[^\n]*`stale`[^\n]*`unassessed`")

    def test_traceability_contract_groups_relationship_and_coverage_states(self):
        relationship_states = ("direct", "derived", "indirect", "contradictory", "missing")
        coverage_states = ("complete", "partial", "unverified", "stale", "unexecuted", "unassessed")

        for language in LANGUAGES:
            package = REPO_ROOT / "skills" / language / "testing-types" / "requirement-traceability-analysis"
            skill = (package / "SKILL.md").read_text(encoding="utf-8")
            prompt = (package / "prompts" / "requirement-traceability-analysis.md").read_text(encoding="utf-8")

            relationship_heading = "Relationship types" if language == "en" else "关系类型"
            coverage_heading = "Coverage statuses" if language == "en" else "覆盖状态"
            self.assertIn(relationship_heading, prompt, package)
            self.assertIn(coverage_heading, prompt, package)
            self.assertIn(relationship_heading, skill, package)
            self.assertIn(coverage_heading, skill, package)
            for state in relationship_states + coverage_states:
                self.assertIn(state, prompt, f"missing {state} in {package}")
                self.assertIn(state, skill, f"missing {state} in {package}")

            self.assertRegex(
                prompt,
                rf"{re.escape(relationship_heading)}[^\n]*\n(?:\n|.)*{re.escape(coverage_heading)}",
            )

    def test_scope_boundary_cases_use_semantic_judges(self):
        for slug in SLUGS:
            for language in LANGUAGES:
                path = (
                    REPO_ROOT
                    / "skills"
                    / language
                    / "testing-types"
                    / slug
                    / "evals"
                    / "cases"
                    / "edge-scope-boundary.yaml"
                )
                text = path.read_text(encoding="utf-8")
                self.assertIn("type: agent_judge", text, path)
                self.assertIn("pass_threshold:", text, path)
                criteria = re.findall(r"^\s*- \".+\"$", text, re.MULTILINE)
                self.assertGreaterEqual(len(criteria), 3, path)


if __name__ == "__main__":
    unittest.main()
