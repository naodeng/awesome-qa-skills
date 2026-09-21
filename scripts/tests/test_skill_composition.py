from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from scripts import validate_skill_composition as composition


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "docs/governance/skill-composition.yaml"
EXPECTED_ROUTE_IDS = {
    "new-feature-quality",
    "api-delivery",
    "change-regression",
    "performance-decision",
    "ai-feature-validation",
}
ALLOWED_RELATION_TYPES = {
    "precedes",
    "recommended_with",
    "alternative_to",
    "conflicts_with",
}


class SkillCompositionContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = composition.load_manifest(MANIFEST_PATH)

    def errors_for(self, manifest):
        return composition.validate_manifest(manifest, ROOT)

    def test_current_manifest_has_five_unique_routes(self):
        routes = self.manifest["routes"]
        route_ids = [route["id"] for route in routes]
        self.assertEqual(set(route_ids), EXPECTED_ROUTE_IDS)
        self.assertEqual(len(route_ids), len(set(route_ids)))
        self.assertEqual(self.errors_for(self.manifest), [])

    def test_each_route_has_one_primary_and_at_most_one_optional(self):
        for route in self.manifest["routes"]:
            self.assertIsInstance(route["primary"], str)
            self.assertTrue(route["primary"])
            optional = route.get("optional")
            self.assertTrue(optional is None or isinstance(optional, str))

        invalid = copy.deepcopy(self.manifest)
        invalid["routes"][0]["optional"] = ["test-strategy", "api-testing"]
        errors = self.errors_for(invalid)
        self.assertTrue(any("new-feature-quality" in error and "optional" in error for error in errors))

    def test_all_route_targets_exist_in_both_languages(self):
        targets = composition.route_targets(self.manifest)
        self.assertEqual(
            targets,
            {
                "requirements-analysis",
                "test-strategy",
                "api-testing",
                "api-contract-testing",
                "change-impact-analysis",
                "regression-test-selection",
                "performance-workload-modeling",
                "performance-result-analysis",
                "ai-feature-testing",
                "llm-testing",
            },
        )
        for target in targets:
            self.assertTrue((ROOT / "skills/zh" / "testing-types" / target).is_dir())
            self.assertTrue((ROOT / "skills/en" / "testing-types" / target).is_dir())

    def test_relation_types_are_limited_to_navigation_contract(self):
        self.assertTrue(self.manifest["relations"])
        self.assertTrue(
            {relation["type"] for relation in self.manifest["relations"]}.issubset(ALLOWED_RELATION_TYPES)
        )

        invalid = copy.deepcopy(self.manifest)
        invalid["relations"][0]["type"] = "requires"
        errors = self.errors_for(invalid)
        self.assertTrue(any("relations[0].type" in error and "allowed" in error for error in errors))

    def test_relations_cannot_self_reference_or_duplicate_direction(self):
        invalid = copy.deepcopy(self.manifest)
        relation = invalid["relations"][0]
        invalid["relations"].append(copy.deepcopy(relation))
        invalid["relations"].append(
            {"from": relation["from"], "to": relation["from"], "type": "precedes"}
        )
        errors = self.errors_for(invalid)
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("self" in error for error in errors))

    def test_localized_copy_requires_exact_zh_and_en_fields(self):
        invalid = copy.deepcopy(self.manifest)
        invalid["routes"][0]["intent"]["fr"] = "unsupported language"
        errors = self.errors_for(invalid)
        self.assertTrue(any("new-feature-quality.intent" in error and "language" in error for error in errors))

        invalid = copy.deepcopy(self.manifest)
        del invalid["routes"][0]["handoff"]["en"]
        errors = self.errors_for(invalid)
        self.assertTrue(any("new-feature-quality.handoff.en" in error for error in errors))

    def test_unknown_target_is_reported_with_route_and_field(self):
        invalid = copy.deepcopy(self.manifest)
        invalid["routes"][0]["primary"] = "does-not-exist"
        errors = self.errors_for(invalid)
        self.assertTrue(any("new-feature-quality.primary" in error and "does-not-exist" in error for error in errors))

    def test_cross_skill_internal_paths_are_rejected(self):
        invalid = copy.deepcopy(self.manifest)
        invalid["routes"][0]["not_for"]["zh"].append("See ../../api-testing/SKILL.md for details")
        errors = self.errors_for(invalid)
        self.assertTrue(any("internal Skill path" in error for error in errors))

    def test_manifest_does_not_declare_install_dependencies(self):
        self.assertNotIn("dependencies", self.manifest)
        self.assertNotIn("install_requires", self.manifest)
        self.assertNotIn("requires", self.manifest)

        invalid = copy.deepcopy(self.manifest)
        invalid["dependencies"] = ["api-testing"]
        errors = self.errors_for(invalid)
        self.assertTrue(any("dependencies" in error and "install" in error for error in errors))

    def test_cli_prints_counts_and_returns_zero_for_current_manifest(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_skill_composition.py", "--repo-root", str(ROOT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["routes"], 5)
        self.assertGreaterEqual(summary["relations"], 1)
        self.assertEqual(summary["target_skills"], 10)


if __name__ == "__main__":
    unittest.main()
