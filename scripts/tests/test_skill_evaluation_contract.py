from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from scripts import validate_skill_evaluation_contract as contract


ROOT = Path(__file__).resolve().parents[2]


class SkillEvaluationContractTest(unittest.TestCase):
    def test_repository_contract_is_complete(self) -> None:
        findings = contract.validate(ROOT)

        self.assertEqual(findings, [], "\n".join(findings))

    def test_missing_required_document_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for relative in contract.REQUIRED_DOCUMENTS:
                if relative.endswith("SKILL_EVALUATION_CONTRACT.md"):
                    continue
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("skill-up\n", encoding="utf-8")

            findings = contract.validate(root)

        self.assertTrue(any("SKILL_EVALUATION_CONTRACT.md" in item for item in findings))

    def test_required_statuses_and_pilots_are_part_of_the_contract(self) -> None:
        self.assertIn("INSUFFICIENT_EVIDENCE", contract.REQUIRED_STATUS_MARKERS)
        self.assertIn("requirements-analysis", contract.REQUIRED_PILOTS)
        self.assertIn("ui-test-playwright", contract.REQUIRED_PILOTS)

    def test_router_pilot_is_registered_in_both_languages_without_new_engine_or_score(self) -> None:
        required_markers = (
            "discover-testing",
            "route-new-feature-quality",
            "route-api-delivery",
            "route-change-regression",
            "route-performance-decision",
            "route-ai-feature",
            "skill.selection",
            "selected_skills",
            "NOT_RUN",
        )
        for relative in ("docs/governance/SKILL_EVALUATION_PILOTS.md", "docs/governance/SKILL_EVALUATION_PILOTS_EN.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            for marker in required_markers:
                self.assertIn(marker, text, f"{marker} missing from {relative}")
            if relative.endswith("_EN.md"):
                self.assertRegex(text, r"(?i)(no|not|does not).{0,60}(engine|score|quality score)")
            else:
                self.assertIn("不新增", text)
                self.assertTrue("Engine" in text or "Quality Score" in text)


if __name__ == "__main__":
    unittest.main()
