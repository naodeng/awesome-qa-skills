from __future__ import annotations

import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts import run_skill_trace_eval as runner


class SkillTraceRunnerTest(unittest.TestCase):
    def write_prompts(self, path: Path, rows: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["id", "should_trigger", "prompt", "mode"])
            writer.writeheader()
            writer.writerows(rows)

    def test_load_prompt_cases_rejects_duplicate_or_unsafe_ids(self):
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "prompts.csv"
            self.write_prompts(
                path,
                [
                    {"id": "case-1", "should_trigger": "true", "prompt": "one", "mode": "explicit"},
                    {"id": "case-1", "should_trigger": "false", "prompt": "two", "mode": "negative"},
                ],
            )

            with self.assertRaisesRegex(ValueError, "duplicate case id"):
                runner.load_prompt_cases(path)

            self.write_prompts(
                path,
                [{"id": "../escape", "should_trigger": "true", "prompt": "one", "mode": "explicit"}],
            )
            with self.assertRaisesRegex(ValueError, "unsafe case id"):
                runner.load_prompt_cases(path)

            self.write_prompts(
                path,
                [{"id": "case-1", "should_trigger": "true", "prompt": "one", "mode": ""}],
            )
            with self.assertRaisesRegex(ValueError, "mode is required"):
                runner.load_prompt_cases(path)

            self.write_prompts(
                path,
                [{"id": "case-1", "should_trigger": "true", "prompt": "one", "mode": "unknown"}],
            )
            with self.assertRaisesRegex(ValueError, "invalid trigger mode"):
                runner.load_prompt_cases(path)

    def test_dry_run_prints_commands_without_creating_case_directories(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            prompts = root / "prompts.csv"
            config = root / "rules.json"
            project_root = root / "projects"
            output_root = root / "outputs"
            self.write_prompts(
                prompts,
                [{"id": "case-1", "should_trigger": "true", "prompt": "Create a demo", "mode": "explicit"}],
            )
            config.write_text(json.dumps({"skill": "demo-skill"}), encoding="utf-8")

            report = runner.run_cases(
                prompts_path=prompts,
                config_path=config,
                project_root=project_root,
                output_root=output_root,
                approve_for_me=True,
                dry_run=True,
            )

            self.assertEqual(report.exit_code, 0)
            self.assertEqual(report.to_dict()["summary"]["NOT_RUN"], 1)
            self.assertEqual(len(report.cases), 1)
            self.assertTrue(report.cases[0]["dry_run"])
            self.assertEqual(report.cases[0]["run_metadata"]["case_id"], "case-1")
            self.assertEqual(
                report.cases[0]["command"],
                [
                    "codex",
                    "exec",
                    "--json",
                    "--skip-git-repo-check",
                    "--approve-for-me",
                    "Create a demo",
                ],
            )
            self.assertFalse(project_root.exists())
            self.assertFalse(output_root.exists())

    def test_run_captures_trace_and_grades_each_isolated_case(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            prompts = root / "prompts.csv"
            config = root / "rules.json"
            project_root = root / "projects"
            output_root = root / "outputs"
            self.write_prompts(
                prompts,
                [{"id": "case-1", "should_trigger": "true", "prompt": "Create a demo", "mode": "explicit"}],
            )
            config.write_text(json.dumps({"skill": "demo-skill"}), encoding="utf-8")
            completed = runner.subprocess.CompletedProcess(
                args=["codex"],
                returncode=0,
                stdout='{"type":"skill.selection","skill":"demo-skill","mode":"explicit","selected":true}\n{"type":"turn.completed"}\n',
                stderr="progress\n",
            )

            with patch.object(runner.subprocess, "run", return_value=completed) as run:
                report = runner.run_cases(
                    prompts_path=prompts,
                    config_path=config,
                    project_root=project_root,
                    output_root=output_root,
                    approve_for_me=False,
                    dry_run=False,
                )

            self.assertEqual(report.exit_code, 0)
            codex_calls = [call for call in run.call_args_list if call.args[0][0] == "codex"]
            self.assertEqual(len(codex_calls), 1)
            called = codex_calls[0]
            self.assertEqual(
                called.args[0],
                ["codex", "exec", "--json", "--skip-git-repo-check", "Create a demo"],
            )
            self.assertEqual(called.kwargs["cwd"], str(project_root / "case-1"))
            self.assertTrue((output_root / "case-1.jsonl").is_file())
            self.assertTrue((output_root / "case-1.stderr.log").is_file())
            result = json.loads((output_root / "case-1.rules.json").read_text(encoding="utf-8"))
            self.assertEqual(result["case_id"], "case-1")
            self.assertEqual(result["runner_exit_code"], 0)
            self.assertEqual(result["exit_code"], 0)
            self.assertEqual(result["evidence_state"], "PASS")
            self.assertIn("run_id", result["run_metadata"])
            self.assertEqual(result["run_metadata"]["case_id"], "case-1")

    def test_malformed_trace_is_a_failure_not_an_infrastructure_block(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            prompts = root / "prompts.csv"
            config = root / "rules.json"
            project_root = root / "projects"
            output_root = root / "outputs"
            self.write_prompts(
                prompts,
                [{"id": "case-1", "should_trigger": "true", "prompt": "Create a demo", "mode": "explicit"}],
            )
            config.write_text(json.dumps({"skill": "demo-skill"}), encoding="utf-8")
            completed = runner.subprocess.CompletedProcess(
                args=["codex"],
                returncode=0,
                stdout="not-json\n",
                stderr="",
            )

            with patch.object(runner.subprocess, "run", return_value=completed):
                report = runner.run_cases(
                    prompts_path=prompts,
                    config_path=config,
                    project_root=project_root,
                    output_root=output_root,
                    dry_run=False,
                )

            result = report.cases[0]
            self.assertEqual(result["evidence_state"], "FAIL")
            self.assertEqual(result["failure_classification"], "UNKNOWN")
            self.assertEqual(result["trace_error_count"], 1)


if __name__ == "__main__":
    unittest.main()
