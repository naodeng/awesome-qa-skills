from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/run_skill_eval.sh"


class SkillEvalShellWrapperTests(unittest.TestCase):
    def test_wrapper_uses_unique_evidence_runs_and_eval_engine_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake_bin = root / "bin"
            fake_bin.mkdir()
            executable = fake_bin / "skill-up"
            executable.write_text(
                """#!/usr/bin/env python3
import json
from pathlib import Path
import sys

if sys.argv[1:] == ["--version"]:
    print("fake-skill-up 1.0")
    raise SystemExit(0)

args = sys.argv[1:]
output = Path(args[args.index("--output-dir") + 1])
output.mkdir(parents=True, exist_ok=True)
(output / "args.json").write_text(json.dumps(args), encoding="utf-8")
report_dir = output / "iteration-1"
report_dir.mkdir()
(report_dir / "report.json").write_text(json.dumps({
    "case_results": [{"case_id": "smoke", "status": "PASS"}]
}), encoding="utf-8")
""",
                encoding="utf-8",
            )
            executable.chmod(0o755)
            environment = os.environ.copy()
            environment["PATH"] = f"{fake_bin}:{environment['PATH']}"
            environment["SKILL_UP_WORKSPACE_ROOT"] = str(root / "runs")
            result = subprocess.run(
                ["bash", str(SCRIPT), "skills/en/testing-workflows/pr-quality-review/evals/eval.yaml"],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            run_dirs = list((root / "runs" / "pr-quality-review" / "runs").iterdir())
            self.assertEqual(len(run_dirs), 1)
            manifest = json.loads((run_dirs[0] / "run-manifest.json").read_text(encoding="utf-8"))
            args = json.loads((run_dirs[0] / "args.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["status"], "PASS")
            self.assertNotIn("--engine", args)

    def test_wrapper_passes_explicit_engine_override(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake_bin = root / "bin"
            fake_bin.mkdir()
            executable = fake_bin / "skill-up"
            executable.write_text(
                """#!/usr/bin/env python3
import json
from pathlib import Path
import sys
if sys.argv[1:] == ["--version"]:
    print("fake-skill-up 1.0")
    raise SystemExit(0)
args = sys.argv[1:]
output = Path(args[args.index("--output-dir") + 1])
output.mkdir(parents=True, exist_ok=True)
(output / "args.json").write_text(json.dumps(args), encoding="utf-8")
report_dir = output / "iteration-1"
report_dir.mkdir()
(report_dir / "report.json").write_text(json.dumps({"case_results": [{"case_id": "smoke", "status": "PASS"}]}), encoding="utf-8")
""",
                encoding="utf-8",
            )
            executable.chmod(0o755)
            environment = os.environ.copy()
            environment["PATH"] = f"{fake_bin}:{environment['PATH']}"
            environment["SKILL_UP_WORKSPACE_ROOT"] = str(root / "runs")
            environment["SKILL_UP_ENGINE"] = "claude_code"
            result = subprocess.run(
                ["bash", str(SCRIPT), "skills/en/testing-workflows/pr-quality-review/evals/eval.yaml"],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            run_dir = next((root / "runs" / "pr-quality-review" / "runs").iterdir())
            args = json.loads((run_dir / "args.json").read_text(encoding="utf-8"))
            engine_index = args.index("--engine")
            self.assertEqual(args[engine_index + 1], "claude_code")

    def test_wrapper_finds_skill_root_for_nested_without_skill_config(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake_bin = root / "bin"
            fake_bin.mkdir()
            executable = fake_bin / "skill-up"
            executable.write_text(
                """#!/usr/bin/env python3
import json
from pathlib import Path
import sys
if sys.argv[1:] == ["--version"]:
    print("fake-skill-up 1.0")
    raise SystemExit(0)
args = sys.argv[1:]
output = Path(args[args.index("--output-dir") + 1])
output.mkdir(parents=True, exist_ok=True)
report_dir = output / "iteration-1"
report_dir.mkdir()
(report_dir / "report.json").write_text(json.dumps({"case_results": [{"case_id": "smoke", "status": "PASS"}]}), encoding="utf-8")
""",
                encoding="utf-8",
            )
            executable.chmod(0o755)
            environment = os.environ.copy()
            environment["PATH"] = f"{fake_bin}:{environment['PATH']}"
            environment["SKILL_UP_WORKSPACE_ROOT"] = str(root / "runs")
            result = subprocess.run(
                [
                    "bash",
                    str(SCRIPT),
                    "skills/en/testing-workflows/pr-quality-review/evals/without-skill/eval.yaml",
                ],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            run_dirs = list((root / "runs" / "pr-quality-review" / "runs").iterdir())
            self.assertEqual(len(run_dirs), 1)


if __name__ == "__main__":
    unittest.main()
