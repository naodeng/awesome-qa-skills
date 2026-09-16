from dataclasses import replace
import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest

from scripts import generate_skill_governance_matrix as matrix
from scripts.tests.v3_v4_skill_contracts import CARD_IDS as V34_CANDIDATE_SLUGS

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_LOGICAL_SKILL_COUNT = 162
EXPECTED_CANDIDATE_COUNT = 100
V20_CANDIDATE_SLUGS = {
    "decision-table-testing",
    "state-transition-testing",
    "boundary-value-testing",
    "equivalence-partitioning",
    "pairwise-testing",
    "combinatorial-testing",
    "model-based-testing",
    "property-based-testing",
    "metamorphic-testing",
    "api-schema-validation",
    "api-negative-testing",
    "api-idempotency-testing",
    "api-pagination-testing",
    "api-rate-limit-testing",
    "api-version-compatibility-testing",
    "api-error-contract-testing",
    "ui-test-strategy",
    "ui-test-selector-review",
    "ui-test-wait-strategy-review",
    "visual-regression-testing",
    "cross-browser-testing",
    "test-code-review",
    "mutation-testing-analysis",
    "mock-quality-review",
    "test-suite-health-analysis",
}
V11_REVIEWED_CANDIDATE_SLUGS = {
    "test-gap-analysis",
    "risk-based-testing",
    "edge-case-discovery",
    "negative-scenario-discovery",
    "test-data-requirement-analysis",
}
def complete_skill(**overrides):
    skill = {
        "slug": "sample",
        "zh_path": "skills/zh/testing-types/sample",
        "en_path": "skills/en/testing-types/sample",
        "virtual_domain": "UNASSESSED",
        "sdlc_stage": "UNASSESSED",
        "roles": ["UNASSESSED"],
        "status": "Existing",
        "priority": "UNASSESSED",
        "inputs": "UNASSESSED",
        "outputs": "UNASSESSED",
        "related": "UNASSESSED",
        "workflow": "UNASSESSED",
        "governance_evidence": "skills/zh/testing-types/sample/SKILL.md",
        "evidence_paths": ["skills/zh/testing-types/sample/SKILL.md"],
        "quality_score": {"state": "NOT_SCORED"},
        "eval_execution": {"state": "NOT_RUN"},
    }
    skill.update(overrides)
    return skill


def write_minimal_domain_catalog(root: Path) -> None:
    (root / "docs/governance").mkdir(parents=True, exist_ok=True)
    domains = [
        {
            "id": f"D{index:02d}",
            "name_zh": f"D{index:02d}",
            "name_en": f"D{index:02d}",
            "description_zh": f"D{index:02d}",
            "description_en": f"D{index:02d}",
        }
        for index in range(1, 17)
    ]
    (root / "docs/governance/virtual-domains.yaml").write_text(
        json.dumps(
            {
                "domains": domains,
                "section_defaults": {"testing-types": "D04"},
                "catalog_heading_defaults": {},
                "ambiguous_catalog_headings": [],
                "slug_overrides": {},
            }
        ),
        encoding="utf-8",
    )


class GovernanceMatrixTest(unittest.TestCase):
    def test_generator_entrypoint_exists(self):
        self.assertTrue((ROOT / "scripts/generate_skill_governance_matrix.py").is_file())

    def test_rejects_missing_and_extra_skill_records(self):
        registry = matrix.parse_registry(
            {
                "skills": [
                    complete_skill(
                        slug="only-one",
                        zh_path="skills/zh/testing-types/only-one",
                        en_path="skills/en/testing-types/only-one",
                    ),
                    complete_skill(
                        slug="extra",
                        zh_path="skills/zh/testing-types/extra",
                        en_path="skills/en/testing-types/extra",
                    ),
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
        physical = matrix.discover_physical_skills(ROOT)
        self.assertEqual(matrix.validate_registry(registry, physical), [])
        self.assertEqual(len(registry.skills), EXPECTED_LOGICAL_SKILL_COUNT)
        self.assertEqual(len(registry.skills), len(physical))
        self.assertEqual(len({skill["slug"] for skill in registry.skills}), len(registry.skills))

    def test_repository_match_reviews_cover_the_twenty_roadmap_mappings(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        actual = {
            review["candidate"]: (
                review["conclusion"],
                tuple(review["target_skills"]),
            )
            for review in registry.match_reviews
        }
        self.assertEqual(actual, matrix.REQUIRED_MATCH_REVIEWS)
        self.assertEqual(len(registry.match_reviews), 20)
        self.assertEqual(
            matrix.validate_registry(registry, matrix.discover_physical_skills(ROOT), ROOT),
            [],
        )

    def test_repository_match_review_validator_rejects_missing_row(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        missing = replace(registry, match_reviews=registry.match_reviews[:-1])

        errors = matrix.validate_registry(missing, matrix.discover_physical_skills(ROOT), ROOT)

        self.assertIn("match_reviews must contain the exact 20-row contract", errors)

    def test_match_reviews_surface_in_matrix_and_bilingual_review(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        matrix_zh = matrix.render_matrix(registry, "zh", ROOT)
        matrix_en = matrix.render_matrix(registry, "en", ROOT)
        review_zh = matrix.render_match_review(registry, "zh")
        review_en = matrix.render_match_review(registry, "en")

        for conclusion in ("MATCH", "MERGE", "ENHANCE", "EXISTING"):
            self.assertIn(f"{conclusion} 复核", matrix_zh)
            self.assertIn(f"{conclusion} review", matrix_en)
        zh_rows = [line for line in review_zh.splitlines() if line.startswith("| `")]
        en_rows = [line for line in review_en.splitlines() if line.startswith("| `")]
        self.assertEqual(len(zh_rows), 20)
        self.assertEqual(len(en_rows), 20)
        self.assertEqual(
            [line.split("|", 2)[1].strip() for line in zh_rows],
            [line.split("|", 2)[1].strip() for line in en_rows],
        )
        self.assertIn("20 条映射", review_zh)
        self.assertIn("20 mappings", review_en)

    def test_match_review_rejects_unknown_fields_and_candidate_drift(self):
        review = {
            "candidate": "candidate",
            "conclusion": "NEW",
            "review_state": "PROPOSED",
            "target_skills": ["missing"],
            "evidence_paths": [],
            "next_action": "review",
        }
        errors = matrix.validate_match_review(
            review,
            {"target"},
            {"candidate": {"conclusion": "MATCH", "target": "target"}},
        )
        self.assertIn("invalid match review state", errors)
        self.assertIn("invalid match review conclusion", errors)
        self.assertIn("unknown target Skill: missing", errors)
        self.assertIn("evidence_paths must be a non-empty list", errors)
        self.assertIn("match review conclusion differs from candidate record", errors)
        self.assertIn("match review targets differ from candidate record", errors)

    def test_candidates_reference_pinned_prompt_baselines(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        self.assertEqual(len(registry.candidates), EXPECTED_CANDIDATE_COUNT)
        self.assertEqual(len({candidate["slug"] for candidate in registry.candidates}), len(registry.candidates))
        candidate_slugs = {candidate["slug"] for candidate in registry.candidates}
        self.assertTrue(V20_CANDIDATE_SLUGS <= candidate_slugs)
        self.assertTrue((ROOT / "docs/governance/PHASE_0_PROMPT_BASELINE_SOURCES.md").is_file())
        self.assertTrue((ROOT / "docs/governance/PHASE_0_PROMPT_BASELINE_SOURCES_EN.md").is_file())
        proposed_v1_1 = {
            "requirement-quality-review": "NEW",
            "requirement-ambiguity-analysis": "NEW",
            "requirement-consistency-analysis": "NEW",
            "requirement-conflict-detection": "NEW",
            "requirement-traceability-analysis": "NEW",
            "business-rule-extraction": "NEW",
            "technical-design-quality-review": "NEW",
            "api-design-quality-review": "NEW",
            "database-design-quality-review": "NEW",
            "observability-design-review": "NEW",
            "error-handling-design-review": "NEW",
            "test-scope-analysis": "NEW",
            "business-rule-consistency-review": "ENHANCE",
            "architecture-testability-review": "ENHANCE",
            "test-coverage-analysis": "ENHANCE",
        }
        proposed_specs = {
            "requirement-quality-review": "docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design.md",
            "requirement-ambiguity-analysis": "docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design.md",
            "requirement-consistency-analysis": "docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design.md",
            "requirement-conflict-detection": "docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design.md",
            "requirement-traceability-analysis": "docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design.md",
            "business-rule-extraction": "docs/superpowers/specs/2026-09-14-v1-1-next-five-quality-skills-design.md",
            "technical-design-quality-review": "docs/superpowers/specs/2026-09-14-v1-1-next-five-quality-skills-design.md",
            "api-design-quality-review": "docs/superpowers/specs/2026-09-14-v1-1-next-five-quality-skills-design.md",
            "database-design-quality-review": "docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md",
            "observability-design-review": "docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md",
            "error-handling-design-review": "docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md",
            "test-scope-analysis": "docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md",
        }
        for candidate in registry.candidates:
            if candidate["decision_state"] == "PROPOSED":
                self.assertIn(candidate["slug"], proposed_v1_1)
                self.assertEqual(candidate["conclusion"], proposed_v1_1[candidate["slug"]])
                expected_spec = proposed_specs.get(
                    candidate["slug"],
                    "docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md",
                )
                self.assertIn(expected_spec, candidate["candidate_source"])
                target_paths = candidate["target_evidence_paths"]
                self.assertTrue(target_paths)
                self.assertTrue(all((ROOT / path).is_file() for path in target_paths))
                continue
            if candidate["decision_state"] == "REVIEWED":
                self.assertEqual(candidate["conclusion"], "NEW")
                self.assertTrue(candidate.get("scope"))
                self.assertTrue(candidate.get("non_goals"))
                if candidate["slug"] in V11_REVIEWED_CANDIDATE_SLUGS:
                    self.assertIn(
                        "docs/superpowers/specs/2026-09-14-v1-1-test-design-discovery-five-design.md",
                        candidate["candidate_source"],
                    )
                    self.assertIn(
                        "docs/superpowers/plans/2026-09-14-v1-1-test-design-discovery-five.md",
                        candidate["candidate_source"],
                    )
                else:
                    source_paths = re.findall(r"(?:docs|skills)/[A-Za-z0-9_./-]+", candidate["candidate_source"])
                    self.assertTrue(source_paths, candidate["slug"])
                    self.assertTrue(all((ROOT / path).is_file() for path in source_paths), candidate["slug"])
                target_paths = candidate["target_evidence_paths"]
                self.assertTrue(target_paths)
                self.assertTrue(all((ROOT / path).is_file() for path in target_paths))
                continue
            if candidate["slug"] in V34_CANDIDATE_SLUGS:
                self.assertEqual(candidate["decision_state"], "REVIEWED_WITH_LIMITATION")
                self.assertIn(
                    "docs/superpowers/specs/2026-09-15-v3-v4-two-batch-design.md",
                    candidate["candidate_source"],
                )
                self.assertTrue(candidate.get("scope"))
                self.assertTrue(candidate.get("non_goals"))
                self.assertTrue(candidate.get("capability_match"))
                self.assertTrue(candidate.get("project_evidence"))
                target_paths = candidate["target_evidence_paths"]
                self.assertTrue(target_paths)
                self.assertTrue(all((ROOT / path).is_file() for path in target_paths))
                continue
            self.assertEqual(candidate["decision_state"], "REVIEWED_WITH_LIMITATION")
            self.assertTrue(candidate["candidate_source"].startswith(
                "awesome-qa-prompt@554178fe9b93d851ec01388597ceb7996d22bd1c: "
            ))
            target_paths = candidate["target_evidence_paths"]
            self.assertTrue(target_paths)
            self.assertTrue(all((ROOT / path).is_file() for path in target_paths))
            for field in matrix.MATCH_FIELDS:
                self.assertNotIn("UNASSESSED", candidate["evidence"][field])
                self.assertIn("candidate_source", candidate["evidence"][field])
                self.assertIn("target:", candidate["evidence"][field])
            for value in [candidate["candidate_source"], *candidate["evidence"].values()]:
                self.assertNotIn("PHASE_0_PROMPT_BASELINE_SOURCES.md#", value)
                self.assertNotRegex(value, r"#[A-Za-z][A-Za-z0-9_-]*")

    def test_phase0_source_register_does_not_duplicate_candidate_decisions(self):
        for filename in (
            "docs/governance/PHASE_0_PROMPT_BASELINE_SOURCES.md",
            "docs/governance/PHASE_0_PROMPT_BASELINE_SOURCES_EN.md",
        ):
            text = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("| Candidate |", text)
            self.assertNotIn("| Target |", text)
            self.assertNotIn("| Conclusion |", text)
            self.assertTrue("single source" in text.lower() or "唯一事实源" in text)

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
            write_minimal_domain_catalog(root)
            registry = matrix.parse_registry({"skills": [], "candidates": []})
            (root / "docs/SKILL_MATRIX.md").write_text("stale\n", encoding="utf-8")
            self.assertEqual(matrix.check_outputs(root, registry), 1)

    def test_quality_gate_checks_generated_governance_views(self):
        quality_gate = (ROOT / "scripts/check_skills_quality.sh").read_text(encoding="utf-8")
        self.assertIn("python3 scripts/generate_skill_governance_matrix.py --check", quality_gate)
        self.assertIn("python3 -m unittest discover -s scripts/tests -v", quality_gate)

    def test_v20_candidates_have_explicit_capability_match_evidence(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        candidates = {entry["slug"]: entry for entry in registry.candidates}
        for slug in V20_CANDIDATE_SLUGS:
            with self.subTest(slug=slug):
                comparison = candidates[slug].get("capability_match")
                self.assertIsInstance(comparison, dict)
                self.assertTrue(comparison.get("existing_targets"))
                self.assertTrue(comparison.get("difference"))
                self.assertEqual(comparison.get("decision"), "NEW")
                self.assertTrue(all((ROOT / path).is_file() for path in comparison["existing_targets"]))

    def test_v20_candidates_have_exact_project_status_evidence(self):
        registry = matrix.load_registry(ROOT / "docs/governance/skill-governance-registry.yaml")
        candidates = {entry["slug"]: entry for entry in registry.candidates}
        for slug in V20_CANDIDATE_SLUGS:
            with self.subTest(slug=slug):
                project = candidates[slug].get("project_evidence")
                self.assertIsInstance(project, dict)
                self.assertEqual(project.get("project_number"), 4)
                self.assertRegex(project.get("item_id", ""), r"^PVTI_")
                self.assertEqual(project.get("title"), f"v2 P1｜候选 Skill｜{slug}")
                self.assertEqual(project.get("current_status"), "Done")
                self.assertTrue(project.get("verified_at"))
                self.assertIn("gh project item-list 4", project.get("verification", ""))
                self.assertEqual(project.get("transition_requirement"), "In Progress -> Done")
                self.assertIn("UNASSESSED", project.get("transition_audit", ""))
                self.assertEqual(project.get("acceptance_state"), "INCOMPLETE")
                self.assertNotEqual(project.get("acceptance_state"), "COMPLETE")

    def test_matrix_uses_skill_description_as_scope_evidence(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_minimal_domain_catalog(root)
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
            "decision_state": "PROPOSED",
            "conclusion": "NEW",
            "evidence": {field: "reviewed" for field in matrix.MATCH_FIELDS},
        }
        self.assertEqual(matrix.validate_candidate(candidate), ["scope", "non_goals"])

    def test_rejects_reviewed_v2_candidate_without_capability_match(self):
        candidate = {
            "slug": "v2-sample",
            "decision_state": "REVIEWED",
            "conclusion": "NEW",
            "scope": "bounded scope",
            "non_goals": "runtime execution",
            "candidate_source": "docs/superpowers/specs/2026-09-15-v2-test-engineering-two-batch-design.md",
            "evidence": {field: "reviewed" for field in matrix.MATCH_FIELDS},
        }
        self.assertIn("REVIEWED v2 candidate requires capability_match", matrix.validate_candidate(candidate))

    def test_rejects_reviewed_v2_candidate_without_project_evidence(self):
        candidate = {
            "slug": "v2-sample",
            "decision_state": "REVIEWED",
            "conclusion": "NEW",
            "scope": "bounded scope",
            "non_goals": "runtime execution",
            "candidate_source": "docs/superpowers/specs/2026-09-15-v2-test-engineering-two-batch-design.md",
            "evidence": {field: "reviewed" for field in matrix.MATCH_FIELDS},
            "capability_match": {
                "decision": "NEW",
                "existing_targets": ["skills/zh/testing-types/test-case-writing/SKILL.md"],
                "difference": "specialized bounded capability",
            },
        }
        self.assertIn("REVIEWED v2 candidate requires project_evidence", matrix.validate_candidate(candidate))

    def test_rejects_complete_v2_candidate_with_unassessed_transition_history(self):
        candidate = {
            "slug": "v2-sample",
            "decision_state": "REVIEWED",
            "conclusion": "NEW",
            "scope": "bounded scope",
            "non_goals": "runtime execution",
            "candidate_source": "docs/superpowers/specs/2026-09-15-v2-test-engineering-two-batch-design.md",
            "evidence": {field: "reviewed" for field in matrix.MATCH_FIELDS},
            "capability_match": {
                "decision": "NEW",
                "existing_targets": ["skills/zh/testing-types/test-case-writing/SKILL.md"],
                "difference": "specialized bounded capability",
            },
            "project_evidence": {
                field: "present"
                for field in matrix.PROJECT_EVIDENCE_FIELDS
            },
        }
        candidate["project_evidence"].update({
            "project_number": 4,
            "current_status": "Done",
            "acceptance_state": "COMPLETE",
            "transition_audit": "UNASSESSED: history unavailable",
        })
        errors = matrix.validate_candidate(candidate)
        self.assertIn("project_evidence cannot be COMPLETE while transition history is UNASSESSED", errors)

    def test_rejects_scored_entry_without_dimensions_and_evidence(self):
        skill = complete_skill(quality_score={"state": "SCORED", "dimensions": {}})
        self.assertEqual(matrix.validate_skill(skill), ["SCORED requires nine dimensions", "SCORED requires evidence"])

    def test_rejects_skill_without_required_governance_fields(self):
        skill = {
            "slug": "sample",
            "zh_path": "skills/zh/testing-types/sample",
            "en_path": "skills/en/testing-types/sample",
            "status": "Existing",
            "quality_score": {"state": "NOT_SCORED"},
            "eval_execution": {"state": "NOT_RUN"},
        }
        errors = matrix.validate_skill(skill)
        for field in ("virtual_domain", "sdlc_stage", "roles", "priority", "inputs", "outputs", "related", "workflow", "governance_evidence"):
            self.assertIn(f"missing {field}", errors)

    def test_rejects_mismatched_or_unpaired_paths(self):
        skill = {
            "slug": "sample",
            "zh_path": "skills/zh/testing-types/other",
            "en_path": "skills/en/testing-types/sample",
            "virtual_domain": "UNASSESSED",
            "sdlc_stage": "UNASSESSED",
            "roles": ["UNASSESSED"],
            "status": "Existing",
            "priority": "UNASSESSED",
            "inputs": "UNASSESSED",
            "outputs": "UNASSESSED",
            "related": "UNASSESSED",
            "workflow": "UNASSESSED",
            "governance_evidence": "skills/zh/testing-types/sample/SKILL.md",
            "evidence_paths": ["skills/zh/testing-types/sample/SKILL.md"],
            "quality_score": {"state": "NOT_SCORED"},
            "eval_execution": {"state": "NOT_RUN"},
        }
        self.assertIn("zh_path does not end in slug", matrix.validate_skill(skill))


if __name__ == "__main__":
    unittest.main()
