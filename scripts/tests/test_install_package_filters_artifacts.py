"""Installer regression tests for excluding generated local artifacts."""
from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INSTALLER = ROOT / "scripts" / "install-skills-mac.sh"
SKILL = ROOT / "skills" / "en" / "testing-workflows" / "discover-testing"


class InstallPackageArtifactFilterTests(unittest.TestCase):
    def test_install_omits_generated_artifacts_and_removes_old_install_residue(self) -> None:
        marker_dir = SKILL / "scripts" / "__pycache__" / f"wre-test-{uuid.uuid4().hex}"
        marker_dir.mkdir(parents=True)
        marker = marker_dir / "sentinel.pyc"
        marker.write_bytes(b"generated local artifact")
        try:
            with tempfile.TemporaryDirectory() as temporary:
                destination = Path(temporary) / "skills"
                installed = destination / "en" / "testing-workflows" / "discover-testing"
                stale_cache = installed / "scripts" / "__pycache__" / "stale.pyc"
                stale_cache.parent.mkdir(parents=True)
                stale_cache.write_bytes(b"stale")
                stale_file = installed / ".DS_Store"
                stale_file.write_bytes(b"stale")

                result = subprocess.run(
                    [
                        "bash", str(INSTALLER), "--tool", "cursor", "--lang", "en",
                        "--skill", "discover-testing", "--dest", str(destination),
                    ],
                    cwd=ROOT,
                    env={**os.environ, "HOME": temporary},
                    text=True,
                    capture_output=True,
                    check=False,
                )

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue((installed / "SKILL.md").is_file())
                self.assertFalse((installed / "scripts" / "__pycache__").exists())
                self.assertFalse((installed / ".DS_Store").exists())
                self.assertFalse((installed / "scripts" / "__pycache__" / marker_dir.name / marker.name).exists())
        finally:
            marker.unlink(missing_ok=True)
            marker_dir.rmdir()


if __name__ == "__main__":
    unittest.main()
