from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "check_skills_cli_compatibility.sh"


FAKE_NPX = r'''#!/usr/bin/env python3
import os
from pathlib import Path
import re
import sys

arguments = sys.argv[1:]
if "--list" in arguments:
    print("requirements-analysis functional-testing api-testing performance-testing ai-agent-testing release-testing-workflow skill-change-verification")
    raise SystemExit(0)

package = Path(arguments[3])
source = package / "skills/en/testing-types/functional-testing/SKILL.md"
if os.environ.get("CLI_TEST_COPY_SOURCE") == "1" and source.is_file():
    content = source.read_text(encoding="utf-8")
else:
    content = """---
name: functional-testing
description: Installed from the remote main branch.
license: MIT
metadata:
  version: "0.9.0"
  compatibility: ""
  author: "Remote contributors"
  language: "en"
  category: "testing-types"
  source: "https://example.com/remote"
  license-url: "https://example.com/license"
---
\n# Functional Testing (English)
"""
if os.environ.get("CLI_TEST_MUTATE_VERSION") == "1":
    content = re.sub(r'(?m)^(\s+version: )"[^"]+"$', r'\g<1>"99.0.0"', content, count=1)
destination = Path.home() / ".agents/skills/functional-testing/SKILL.md"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(content, encoding="utf-8")
'''


class SkillsCliCompatibilityScriptTests(unittest.TestCase):
    def run_script(self, package: str, *, copy_source: bool = False, mutate_version: bool = False):
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            bin_dir = temp / "bin"
            bin_dir.mkdir()
            npx = bin_dir / "npx"
            npx.write_text(FAKE_NPX, encoding="utf-8")
            npx.chmod(0o755)
            environment = os.environ.copy()
            environment["PATH"] = f"{bin_dir}{os.pathsep}{Path(sys.executable).parent}{os.pathsep}{environment.get('PATH', '')}"
            environment["TMPDIR"] = temporary
            environment["SKILLS_CLI_PACKAGE"] = package
            environment["CLI_TEST_COPY_SOURCE"] = "1" if copy_source else "0"
            environment["CLI_TEST_MUTATE_VERSION"] = "1" if mutate_version else "0"
            return subprocess.run(
                ["bash", str(SCRIPT)],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_remote_default_does_not_compare_against_local_checkout_metadata(self):
        result = self.run_script("naodeng/awesome-qa-skills")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("metadata comparison skipped for remote package", result.stdout)

    def test_local_package_metadata_must_match_installed_skill(self):
        result = self.run_script(str(ROOT), copy_source=True, mutate_version=True)

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("did not preserve metadata.version", result.stderr)


if __name__ == "__main__":
    unittest.main()
