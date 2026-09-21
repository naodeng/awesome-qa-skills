from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "route": "api-delivery",
    "primary": "api-testing",
    "optional": "api-contract-testing",
}


class RouterSelectionJudgeTest(unittest.TestCase):
    def test_bilingual_router_judges_require_exact_structured_selection(self) -> None:
        for language in ("zh", "en"):
            script = (
                ROOT
                / "skills"
                / language
                / "testing-workflows"
                / "discover-testing"
                / "evals"
                / "fixtures"
                / "scripts"
                / "check_router_selection.sh"
            )
            with self.subTest(language=language):
                with tempfile.TemporaryDirectory() as temporary:
                    workdir = Path(temporary)
                    expected_path = workdir / "evals" / "fixtures" / "router-expected.json"
                    expected_path.parent.mkdir(parents=True)
                    expected_path.write_text(json.dumps(EXPECTED), encoding="utf-8")

                    valid = subprocess.run(
                        [str(script)],
                        cwd=workdir,
                        env={
                            **os.environ,
                            "EVAL_FINAL_MESSAGE": "```json\n"
                            + json.dumps(EXPECTED)
                            + "\n```",
                        },
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(valid.returncode, 0, valid.stderr or valid.stdout)

                    invalid_payload = {**EXPECTED, "additional_skill": "security-testing"}
                    invalid = subprocess.run(
                        [str(script)],
                        cwd=workdir,
                        env={
                            **os.environ,
                            "EVAL_FINAL_MESSAGE": "```json\n"
                            + json.dumps(invalid_payload)
                            + "\n```",
                        },
                        capture_output=True,
                        text=True,
                    )
                    self.assertNotEqual(invalid.returncode, 0, invalid.stdout)


if __name__ == "__main__":
    unittest.main()
