from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[2]
ARCHIVER = ROOT / "scripts/archive_skill_eval_run.py"


class ArchiveSkillEvalRunTests(unittest.TestCase):
    def test_archive_preserves_run_provenance_and_redacts_machine_paths(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo = root / "repo"
            skill = repo / "skills/en/testing-workflows/sample-skill"
            run = root / "runs/run-123/iteration-1"
            skill.mkdir(parents=True)
            run.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: sample-skill\n---\n", encoding="utf-8")
            report = {
                "skill_name": "sample-skill",
                "engine_name": "codex",
                "case_results": [
                    {
                        "case_id": "smoke",
                        "title": "Smoke test",
                        "status": "PASS",
                        "prompt": "Review sample",
                        "response": f"See {root}/tmp/skill-up-abc/.codex/skills/sample-skill/prompts/review.md",
                    }
                ],
            }
            report_path = run / "report.json"
            raw = json.dumps(report, ensure_ascii=False).encode("utf-8")
            report_path.write_bytes(raw)
            manifest = {
                "record_version": "skill-up-run-manifest/v1",
                "run_id": "run-123",
                "skill_id": "sample-skill",
                "status": "PASS",
                "started_at": "2026-11-02T10:00:00Z",
                "finished_at": "2026-11-02T10:01:00Z",
                "runner": {"name": "skill-up", "version": "skill-up version 0.12.0"},
                "engine": "codex",
                "engine_version": "codex-cli test-version",
                "commit_sha": "a" * 40,
                "dirty_path_count": 3,
                "input_fingerprint": "b" * 64,
                "input_fingerprint_after": "b" * 64,
                "skill_package_sha256": "c" * 64,
                "skill_file_count": 2,
                "raw_report_path": "iteration-1/report.json",
                "raw_report_sha256": hashlib.sha256(raw).hexdigest(),
                "process_exit_code": 0,
                "cases": [{"case_id": "smoke", "status": "PASS"}],
            }
            manifest_path = root / "runs/run-123/run-manifest.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            output = root / "archive.json"

            result = subprocess.run(
                [
                    sys.executable,
                    str(ARCHIVER),
                    "--manifest",
                    str(manifest_path),
                    "--skill-dir",
                    str(skill),
                    "--repo-root",
                    str(repo),
                    "--locale",
                    "en-US",
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            archived = json.loads(output.read_text(encoding="utf-8"))
            response = archived["cases"][0]["response"]
            self.assertEqual(archived["input_fingerprint"], "b" * 64)
            self.assertEqual(archived["raw_result_sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(archived["summary"]["overall_status"], "PASS")
            self.assertEqual(archived["engine"]["version"], "codex-cli test-version")
            self.assertIn("skills/en/testing-workflows/sample-skill/prompts/review.md", response)
            self.assertNotIn(str(root), response)


if __name__ == "__main__":
    unittest.main()
