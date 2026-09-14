from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts import generate_skill_governance_matrix as matrix

ROOT = Path(__file__).resolve().parents[2]


class GovernanceMatrixTest(unittest.TestCase):
    def test_generator_entrypoint_exists(self):
        self.assertTrue((ROOT / "scripts/generate_skill_governance_matrix.py").is_file())

    def test_rejects_missing_and_extra_skill_records(self):
        registry = matrix.parse_registry(
            {
                "skills": [
                    {
                        "slug": "only-one",
                        "zh_path": "skills/zh/testing-types/only-one",
                        "en_path": "skills/en/testing-types/only-one",
                        "status": "Existing",
                        "quality_score": {"state": "NOT_SCORED"},
                        "eval_execution": {"state": "NOT_RUN"},
                    },
                    {
                        "slug": "extra",
                        "zh_path": "skills/zh/testing-types/extra",
                        "en_path": "skills/en/testing-types/extra",
                        "status": "Existing",
                        "quality_score": {"state": "NOT_SCORED"},
                        "eval_execution": {"state": "NOT_RUN"},
                    },
                ],
                "candidates": [],
            }
        )
        self.assertEqual(
            matrix.validate_registry(registry, {"only-one", "missing"}),
            ["missing registry record for skill: missing", "registry record has no physical skill: extra"],
        )

    def test_discovers_union_of_language_skill_trees(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            for language, slug in (("zh", "zh-only"), ("en", "en-only")):
                (root / "skills" / language / "testing-types" / slug).mkdir(parents=True)
            for language in matrix.LANGUAGES:
                for section in matrix.SECTIONS:
                    (root / "skills" / language / section).mkdir(parents=True, exist_ok=True)
            self.assertEqual(matrix.discover_physical_skills(root), {"zh-only", "en-only"})

    def test_repository_registry_covers_every_logical_skill_once(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        self.assertEqual(matrix.validate_registry(registry, matrix.discover_physical_skills(ROOT)), [])
        self.assertEqual(len(registry.skills), 79)

    def test_matrix_render_contains_explicit_evidence_states(self):
        registry = matrix.parse_registry({"skills": [{
            "slug": "sample", "zh_path": "zh/sample", "en_path": "en/sample",
            "virtual_domain": "D01", "status": "Candidate",
            "quality_score": {"state": "NOT_SCORED"},
            "eval_execution": {"state": "NOT_RUN"},
        }], "candidates": []})
        rendered = matrix.render_matrix(registry, "zh")
        self.assertIn("NOT_SCORED", rendered)
        self.assertIn("NOT_RUN", rendered)
        self.assertIn("SDLC", rendered)
        self.assertIn("UNASSESSED", rendered)

    def test_check_outputs_detects_stale_matrix(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            registry = matrix.parse_registry({"skills": [], "candidates": []})
            (root / "docs/SKILL_MATRIX.md").write_text("stale\n", encoding="utf-8")
            self.assertEqual(matrix.check_outputs(root, registry), 1)

    def test_quality_gate_checks_generated_governance_views(self):
        quality_gate = (ROOT / "scripts/check_skills_quality.sh").read_text(encoding="utf-8")
        self.assertIn("python3 scripts/generate_skill_governance_matrix.py --check", quality_gate)

    def test_matrix_uses_skill_description_as_scope_evidence(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            evidence = root / "skills/zh/testing-types/sample/SKILL.md"
            evidence.parent.mkdir(parents=True)
            evidence.write_text("---\ndescription: Analyze requirement boundaries\n---\n", encoding="utf-8")
            registry = matrix.parse_registry({"skills": [{
                "slug": "sample", "section": "testing-types", "zh_path": "skills/zh/testing-types/sample",
                "en_path": "skills/en/testing-types/sample", "virtual_domain": "D01", "status": "Candidate",
                "quality_score": {"state": "NOT_SCORED"}, "eval_execution": {"state": "NOT_RUN"},
                "governance_evidence": "skills/zh/testing-types/sample/SKILL.md",
            }], "candidates": []})
            self.assertIn("Analyze requirement boundaries", matrix.render_matrix(registry, "zh", root))

    def test_rejects_new_candidate_without_boundaries(self):
        candidate = {
            "slug": "new-capability",
            "conclusion": "NEW",
            "evidence": {field: "reviewed" for field in matrix.MATCH_FIELDS},
        }
        self.assertEqual(matrix.validate_candidate(candidate), ["scope", "non_goals"])

    def test_rejects_scored_entry_without_dimensions_and_evidence(self):
        skill = {
            "slug": "sample",
            "zh_path": "skills/zh/testing-types/sample",
            "en_path": "skills/en/testing-types/sample",
            "status": "Existing",
            "quality_score": {"state": "SCORED", "dimensions": {}},
            "eval_execution": {"state": "NOT_RUN"},
        }
        self.assertEqual(matrix.validate_skill(skill), ["SCORED requires nine dimensions", "SCORED requires evidence"])


if __name__ == "__main__":
    unittest.main()
