from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts import add_skill_eval_regression_case as writer


class RegressionCaseWriterTest(unittest.TestCase):
    def test_writes_a_regression_case_without_touching_skill_files(self) -> None:
        with TemporaryDirectory() as temporary:
            skill_root = Path(temporary) / "skill"
            cases = skill_root / "evals" / "cases"
            cases.mkdir(parents=True)
            (skill_root / "evals" / "eval.yaml").write_text(
                "cases:\n"
                "  files:\n"
                "    - evals/cases/basic-success.yaml\n"
                "  defaults:\n"
                "    timeout_seconds: 180\n",
                encoding="utf-8",
            )
            skill_file = skill_root / "SKILL.md"
            skill_file.write_text("original\n", encoding="utf-8")

            output = writer.write_case(
                skill_root=skill_root,
                case_id="regression-missing-evidence",
                title="Missing evidence regression",
                description="Preserve the evidence boundary after a real failure.",
                prompt="Review this incomplete change and identify what is not proven.",
                must_contain=["evidence"],
                must_not_contain=["proven"],
            )

            self.assertEqual(output, (cases / "regression-missing-evidence.yaml").resolve())
            generated = output.read_text(encoding="utf-8")
            self.assertIn("category: REGRESSION", generated)
            self.assertIn("lifecycle: CANDIDATE", generated)
            self.assertIn("evidence_state: NOT_RUN", generated)
            self.assertIn(
                "    - evals/cases/regression-missing-evidence.yaml\n",
                (skill_root / "evals" / "eval.yaml").read_text(encoding="utf-8"),
            )
            self.assertEqual(skill_file.read_text(encoding="utf-8"), "original\n")

            with self.assertRaises(FileExistsError):
                writer.write_case(
                    skill_root=skill_root,
                    case_id="regression-missing-evidence",
                    title="Duplicate",
                    description="Duplicate case.",
                    prompt="Do not overwrite.",
                    must_contain=["evidence"],
                    must_not_contain=[],
                )

    def test_rejects_unsafe_case_id(self) -> None:
        with TemporaryDirectory() as temporary:
            skill_root = Path(temporary)
            with self.assertRaises(ValueError):
                writer.write_case(
                    skill_root=skill_root,
                    case_id="../escape",
                    title="Unsafe",
                    description="Unsafe.",
                    prompt="Unsafe.",
                    must_contain=["x"],
                    must_not_contain=[],
                )


if __name__ == "__main__":
    unittest.main()
