from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts/run_skill_eval_with_evidence.py"


class SkillUpRunEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.skill = self.root / "skills/en/testing-workflows/sample-skill"
        (self.skill / "evals/cases").mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("---\nname: sample-skill\n---\n", encoding="utf-8")
        (self.skill / "evals/eval.yaml").write_text(
            '{"schema_version":"v1alpha1","engine":{"name":"codex"}}\n',
            encoding="utf-8",
        )
        (self.skill / "evals/cases/smoke.yaml").write_text('{"id":"smoke"}\n', encoding="utf-8")
        self.fake_skill_up = self.root / "fake-skill-up"
        self.fake_skill_up.write_text(
            """#!/usr/bin/env python3
import json
import os
from pathlib import Path
import sys

if sys.argv[1:] == ["--version"]:
    print("fake-skill-up 1.0")
    raise SystemExit(0)

output = Path(sys.argv[sys.argv.index("--output-dir") + 1])
manifest = json.loads((output / "run-manifest.json").read_text(encoding="utf-8"))
assert manifest["status"] == "RUNNING"
assert len(manifest["input_fingerprint"]) == 64
if os.environ.get("WRE_MUTATE_SKILL_INPUTS") == "1":
    (Path.cwd() / "SKILL.md").write_text("---\\\\nname: sample-skill\\\\n---\\\\nchanged\\\\n", encoding="utf-8")
if os.environ.get("WRE_WRITE_REPORT", "1") == "1":
    reports = output / "iteration-1"
    reports.mkdir(parents=True)
    status = os.environ.get("WRE_CASE_STATUS", "PASS")
    (reports / "report.json").write_text(json.dumps({
        "case_results": [{"case_id": "smoke", "status": status}],
        "engine_name": "codex",
        "observed_configuration": {"version": "test-engine"},
    }), encoding="utf-8")
raise SystemExit(int(os.environ.get("WRE_EXIT_CODE", "0")))
""",
            encoding="utf-8",
        )
        self.fake_skill_up.chmod(self.fake_skill_up.stat().st_mode | stat.S_IXUSR)
        self.fake_codex = self.root / "codex"
        self.fake_codex.write_text("#!/usr/bin/env sh\nprintf 'codex-cli test-version\\n'\n", encoding="utf-8")
        self.fake_codex.chmod(self.fake_codex.stat().st_mode | stat.S_IXUSR)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def invoke(self, output: Path, **extra_env: str) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment.update(extra_env)
        environment["PATH"] = f"{self.root}:{environment['PATH']}"
        return subprocess.run(
            [
                sys.executable,
                str(RUNNER),
                "--skill-dir",
                str(self.skill),
                "--eval-file",
                "evals/eval.yaml",
                "--output-dir",
                str(output),
                "--skill-up-bin",
                str(self.fake_skill_up),
                "--",
                "--include-case-name",
                "smoke",
            ],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_captures_input_fingerprint_before_run_and_hashes_raw_report(self) -> None:
        self.assertTrue(RUNNER.is_file(), "start-time evidence runner has not been implemented")
        output = self.root / "run"

        result = self.invoke(output)

        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((output / "run-manifest.json").read_text(encoding="utf-8"))
        report = output / manifest["raw_report_path"]
        self.assertEqual(manifest["status"], "PASS")
        self.assertEqual(manifest["input_fingerprint"], manifest["input_fingerprint_after"])
        self.assertEqual(manifest["raw_report_sha256"], hashlib.sha256(report.read_bytes()).hexdigest())
        self.assertEqual(manifest["runner"]["version"], "fake-skill-up 1.0")
        self.assertEqual(manifest["engine_version"], "codex-cli test-version")
        self.assertEqual(manifest["cases"][0]["status"], "PASS")

    def test_marks_run_stale_when_skill_inputs_change_while_eval_runs(self) -> None:
        self.assertTrue(RUNNER.is_file(), "start-time evidence runner has not been implemented")
        output = self.root / "run"

        result = self.invoke(output, WRE_MUTATE_SKILL_INPUTS="1")

        self.assertEqual(result.returncode, 1, result.stderr)
        manifest = json.loads((output / "run-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "STALE")
        self.assertNotEqual(manifest["input_fingerprint"], manifest["input_fingerprint_after"])
        self.assertIn("changed during run", manifest["stale_reason"])

    def test_classifies_runner_error_without_a_report_as_error(self) -> None:
        self.assertTrue(RUNNER.is_file(), "start-time evidence runner has not been implemented")
        output = self.root / "run"

        result = self.invoke(output, WRE_WRITE_REPORT="0")

        self.assertEqual(result.returncode, 2, result.stderr)
        manifest = json.loads((output / "run-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "ERROR")
        self.assertIsNone(manifest["raw_report_sha256"])

    def test_refuses_to_reuse_an_existing_run_directory(self) -> None:
        self.assertTrue(RUNNER.is_file(), "start-time evidence runner has not been implemented")
        output = self.root / "run"
        output.mkdir()
        keep = output / "keep.txt"
        keep.write_text("preserve", encoding="utf-8")

        result = self.invoke(output)

        self.assertEqual(result.returncode, 2)
        self.assertEqual(keep.read_text(encoding="utf-8"), "preserve")


if __name__ == "__main__":
    unittest.main()
