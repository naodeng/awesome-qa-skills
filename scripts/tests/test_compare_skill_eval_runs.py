from __future__ import annotations

import unittest

from scripts.compare_skill_eval_runs import compare_reports


def metadata(skill_version: str, run_id: str = "run-1") -> dict[str, str]:
    return {
        "run_id": run_id,
        "case_id": "unknown",
        "variant": "default",
        "skill_version": skill_version,
        "eval_version": "eval-1",
        "skill_up_version": "0.7.0",
        "engine": "codex",
        "provider": "openai",
        "requested_model": "model-a",
        "observed_model": "model-a",
        "judge_type": "rule_based",
        "judge_model": "unknown",
        "environment": "none",
        "timestamp": "2026-09-20T00:00:00Z",
    }


class CompareSkillEvalRunsTest(unittest.TestCase):
    def test_reports_a_comparable_pass_to_fail_observation(self) -> None:
        result = compare_reports(
            {"run_metadata": metadata("skill-a"), "cases": [{"case_id": "case-1", "evidence_state": "PASS"}]},
            {"run_metadata": metadata("skill-b", "run-2"), "cases": [{"case_id": "case-1", "evidence_state": "FAIL"}]},
        )

        self.assertTrue(result["comparable"])
        self.assertEqual(result["status"], "REGRESSION_OBSERVED")
        self.assertEqual(result["regressions"][0]["case_id"], "case-1")

    def test_unknown_or_changed_eval_metadata_blocks_comparison(self) -> None:
        current = metadata("skill-b", "run-2")
        current["eval_version"] = "eval-2"
        result = compare_reports(
            {"run_metadata": metadata("skill-a"), "cases": [{"case_id": "case-1", "evidence_state": "PASS"}]},
            {"run_metadata": current, "cases": [{"case_id": "case-1", "evidence_state": "FAIL"}]},
        )

        self.assertFalse(result["comparable"])
        self.assertEqual(result["status"], "INSUFFICIENT_EVIDENCE")
        self.assertTrue(result["comparability_errors"])


if __name__ == "__main__":
    unittest.main()
