import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRADER = ROOT / "skills/en/testing-workflows/release-testing-workflow/evals/graders/review-repair-regression.py"
grade = runpy.run_path(str(GRADER))["grade"]


class ReviewRepairRegressionGraderTests(unittest.TestCase):
    def test_decision_rows_ignore_other_tables_with_the_same_ids(self) -> None:
        response = """| Case | Scope | Quality | Operations | Decision evidence |
|---|---|---|---|---|
| R1 | UNKNOWN | P0 regression PASS | UNKNOWN | UNKNOWN |
| R2 | PASS | PASS | PASS | PASS |

R1 | NO_GO | Required security is NOT_RUN; no approval record.
R2 | READY | Required tests and operations readiness are reported; approval is cited.
"""
        grade(response, 0)

    def test_duplicate_decision_rows_are_rejected(self) -> None:
        response = "R1 | NO_GO | evidence\nR1 | NO_GO | duplicate\nR2 | READY | evidence\n"
        with self.assertRaisesRegex(ValueError, "R1"):
            grade(response, 0)

    def test_missing_decision_rows_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "R1"):
            grade("R2 | READY | evidence\n", 0)


if __name__ == "__main__":
    unittest.main()
