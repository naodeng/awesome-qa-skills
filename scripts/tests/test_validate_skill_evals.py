from __future__ import annotations

import os
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest


class ValidateSkillEvalsTest(unittest.TestCase):
    def test_required_mode_fails_when_skill_up_is_missing(self) -> None:
        repo_root = Path(__file__).resolve().parents[2]
        with TemporaryDirectory() as temporary:
            env = os.environ.copy()
            env["PATH"] = f"{temporary}:/usr/bin:/bin"
            env["REQUIRE_SKILL_UP"] = "1"
            result = subprocess.run(
                ["bash", str(repo_root / "scripts" / "validate_skill_evals.sh")],
                cwd=repo_root,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("required", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()
