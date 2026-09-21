from __future__ import annotations

import json
import shutil
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts import grade_skill_trace
from scripts import skill_eval_rules as rules


EXPECTED_RULE_IDS = {
    "TRIGGER-001",
    "TRIGGER-002",
    "TRIGGER-003",
    "TRIGGER-004",
    "TRACE-001",
    "TRACE-002",
    "TRACE-003",
    "PROCESS-001",
    "PROCESS-002",
    "PROCESS-003",
    "OUTCOME-001",
    "OUTCOME-002",
    "ARTIFACT-001",
    "ARTIFACT-002",
    "ENV-001",
    "ENV-002",
    "RUNTIME-001",
    "SAFETY-001",
    "PERMISSION-001",
    "REPRO-001",
}


def event_lines(project_dir: Path) -> list[dict]:
    cwd = str(project_dir)
    return [
        {
            "type": "skill.selection",
            "skill": "demo-skill",
            "mode": "explicit",
            "selected": True,
        },
        {"type": "eval.environment", "cwd": cwd, "paths": []},
        {
            "type": "item.started",
            "item": {
                "id": "build",
                "type": "command_execution",
                "command": "python build.py",
                "cwd": cwd,
            },
        },
        {
            "type": "item.completed",
            "item": {
                "id": "build",
                "type": "command_execution",
                "command": "python build.py",
                "exit_code": 0,
                "cwd": cwd,
            },
        },
        {
            "type": "item.started",
            "item": {
                "id": "smoke",
                "type": "command_execution",
                "command": "python smoke.py",
                "cwd": cwd,
            },
        },
        {
            "type": "item.completed",
            "item": {
                "id": "smoke",
                "type": "command_execution",
                "command": "python smoke.py",
                "exit_code": 0,
                "cwd": cwd,
            },
        },
        {
            "type": "turn.completed",
            "usage": {"input_tokens": 10, "output_tokens": 20},
        },
    ]


def write_trace(path: Path, events: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(event) + "\n" for event in events),
        encoding="utf-8",
    )


def happy_config(project_dir: Path, comparison_trace: Path) -> dict:
    return {
        "skill": "demo-skill",
        "trigger_mode": "explicit",
        "required_commands": ["python build.py", "python smoke.py"],
        "command_order": ["python build.py", "python smoke.py"],
        "required_artifacts": [{"path": "package.json", "contains": "demo"}],
        "build_command": "python build.py",
        "smoke_command": "python smoke.py",
        "expected_files": ["package.json", "src/main.py"],
        "content_checks": [{"path": "src/main.py", "contains": "main"}],
        "persisted_paths": ["package.json", "src/main.py"],
        "required_tools": ["python3"],
        "environment": {
            "expected_cwd": str(project_dir),
            "required_paths": ["package.json"],
            "forbidden_paths": ["unexpected.txt"],
        },
        "max_commands": 2,
        "max_repeated_commands": 1,
        "max_total_tokens": 100,
        "forbidden_commands": ["rm -rf"],
        "permissions": {"max_escalations": 0},
        "require_command_lifecycle": True,
        "compare_trace": str(comparison_trace),
    }


class SkillEvalRulesTest(unittest.TestCase):
    def test_catalog_contains_the_twenty_local_rules(self):
        self.assertEqual(set(rules.RULE_IDS), EXPECTED_RULE_IDS)
        self.assertEqual(rules.validate_rule_catalog(), [])

    def test_jsonl_loader_reports_bad_lines_and_extracts_audit_data(self):
        with TemporaryDirectory() as temporary:
            trace_path = Path(temporary) / "trace.jsonl"
            trace_path.write_text(
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "id": "one",
                            "type": "command_execution",
                            "command": "python -m unittest",
                            "exit_code": 0,
                        },
                    }
                )
                + "\nnot-json\n"
                + json.dumps(
                    {
                        "type": "turn.completed",
                        "usage": {"input_tokens": 3, "output_tokens": 4},
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            trace = rules.load_jsonl(trace_path)

            self.assertEqual(len(trace.events), 2)
            self.assertEqual(len(trace.errors), 1)
            self.assertEqual([record.command for record in trace.commands], ["python -m unittest"])
            self.assertEqual(trace.total_tokens, 7)

    def test_happy_trace_passes_all_configured_rules(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "package.json").write_text('{"name":"demo"}\n', encoding="utf-8")
            (root / "src/main.py").write_text("def main(): pass\n", encoding="utf-8")
            trace_path = root / "trace.jsonl"
            comparison_trace = root / "comparison.jsonl"
            write_trace(trace_path, event_lines(root))
            shutil.copyfile(trace_path, comparison_trace)

            trace = rules.load_jsonl(trace_path)
            report = rules.evaluate_trace(trace, happy_config(root, comparison_trace), root)

            self.assertFalse(report.has_failures)
            statuses = {result.rule_id: result.status for result in report.results}
            self.assertEqual(statuses["TRIGGER-001"], "PASS")
            self.assertEqual(statuses["TRIGGER-002"], "N/A")
            self.assertEqual(statuses["TRIGGER-004"], "N/A")
            for rule_id in EXPECTED_RULE_IDS - {"TRIGGER-002", "TRIGGER-003", "TRIGGER-004"}:
                self.assertEqual(statuses[rule_id], "PASS", rule_id)

    def test_failed_trace_explains_process_and_outcome_regressions(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "package.json").write_text('{"name":"demo"}\n', encoding="utf-8")
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [
                    {
                        "type": "skill.selection",
                        "skill": "demo-skill",
                        "mode": "explicit",
                        "selected": False,
                    },
                    {
                        "type": "item.completed",
                        "item": {
                            "id": "build",
                            "type": "command_execution",
                            "command": "python build.py",
                            "exit_code": 1,
                        },
                    },
                ],
            )

            config = {
                "skill": "demo-skill",
                "trigger_mode": "explicit",
                "required_commands": ["python build.py", "python smoke.py"],
                "command_order": ["python smoke.py", "python build.py"],
                "required_artifacts": [{"path": "missing.json"}],
                "build_command": "python build.py",
                "smoke_command": "python smoke.py",
                "expected_files": ["missing.json"],
                "required_tools": ["python3"],
                "permissions": {"max_escalations": 0},
            }
            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            results = {result.rule_id: result for result in report.results}

            self.assertTrue(report.has_failures)
            self.assertEqual(results["TRIGGER-001"].status, "FAIL")
            self.assertEqual(results["PROCESS-001"].status, "FAIL")
            self.assertEqual(results["PROCESS-002"].status, "FAIL")
            self.assertEqual(results["PROCESS-003"].status, "FAIL")
            self.assertEqual(results["OUTCOME-001"].status, "FAIL")
            self.assertEqual(results["OUTCOME-002"].status, "FAIL")
            self.assertEqual(results["ARTIFACT-001"].status, "FAIL")

    def test_negative_control_needs_an_explicit_non_selection_event(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [{
                    "type": "skill.selection",
                    "skill": "demo-skill",
                    "mode": "negative",
                    "selected": False,
                }],
            )
            config = {
                "skill": "demo-skill",
                "trigger_mode": "negative",
                "required_tools": ["python3"],
            }

            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            result = next(item for item in report.results if item.rule_id == "TRIGGER-004")
            self.assertEqual(result.status, "PASS")

    def test_trigger_config_without_mode_is_blocked(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(trace_path, [{"type": "turn.completed"}])

            report = rules.evaluate_trace(
                rules.load_jsonl(trace_path),
                {"skill": "demo-skill"},
                root,
            )

            trigger_results = [result for result in report.results if result.rule_id.startswith("TRIGGER-")]
            self.assertTrue(trigger_results)
            self.assertTrue(all(result.status == "BLOCKED" for result in trigger_results))
            self.assertEqual(report.exit_code, 2)

    def test_negative_control_rejects_missing_or_invalid_selection_boolean(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [{
                    "type": "skill.selection",
                    "skill": "demo-skill",
                    "mode": "negative",
                    "selected": "unknown",
                }],
            )
            config = {"skill": "demo-skill", "trigger_mode": "negative"}

            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            result = next(item for item in report.results if item.rule_id == "TRIGGER-004")
            self.assertEqual(result.status, "BLOCKED")

    def test_trigger_evidence_requires_the_canonical_skill_selection_event(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [{
                    "type": "skill.invoked",
                    "skill": "demo-skill",
                    "mode": "explicit",
                    "selected": True,
                }],
            )

            report = rules.evaluate_trace(
                rules.load_jsonl(trace_path),
                {"skill": "demo-skill", "trigger_mode": "explicit"},
                root,
            )
            result = next(item for item in report.results if item.rule_id == "TRIGGER-001")
            self.assertEqual(result.status, "BLOCKED")

    def test_router_selection_contract_matches_route_and_exact_skill_set(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [
                    {
                        "type": "skill.selection",
                        "skill": "discover-testing",
                        "mode": "explicit",
                        "selected": True,
                        "route": "api-delivery",
                        "primary": "api-testing",
                        "optional": "api-contract-testing",
                        "selected_skills": ["api-testing", "api-contract-testing"],
                    }
                ],
            )
            config = {
                "skill": "discover-testing",
                "trigger_mode": "explicit",
                "expected_selection": {
                    "route": "api-delivery",
                    "primary": "api-testing",
                    "optional": "api-contract-testing",
                },
            }

            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            result = next(item for item in report.results if item.rule_id == "TRIGGER-001")

            self.assertEqual(result.status, "PASS")
            self.assertIn("route=api-delivery", result.message)

    def test_router_selection_contract_blocks_when_structured_fields_are_missing(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [
                    {
                        "type": "skill.selection",
                        "skill": "discover-testing",
                        "mode": "explicit",
                        "selected": True,
                    }
                ],
            )
            config = {
                "skill": "discover-testing",
                "trigger_mode": "explicit",
                "expected_selection": {
                    "route": "api-delivery",
                    "primary": "api-testing",
                    "optional": "api-contract-testing",
                },
            }

            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            result = next(item for item in report.results if item.rule_id == "TRIGGER-001")

            self.assertEqual(result.status, "BLOCKED")
            self.assertIn("structured selection evidence", result.message)

    def test_router_selection_contract_fails_when_more_than_one_optional_is_observed(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [
                    {
                        "type": "skill.selection",
                        "skill": "discover-testing",
                        "mode": "explicit",
                        "selected": True,
                        "route": "api-delivery",
                        "primary": "api-testing",
                        "optional": "api-contract-testing",
                        "selected_skills": [
                            "api-testing",
                            "api-contract-testing",
                            "security-testing",
                        ],
                    }
                ],
            )
            config = {
                "skill": "discover-testing",
                "trigger_mode": "explicit",
                "expected_selection": {
                    "route": "api-delivery",
                    "primary": "api-testing",
                    "optional": "api-contract-testing",
                },
            }

            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            result = next(item for item in report.results if item.rule_id == "TRIGGER-001")

            self.assertEqual(result.status, "FAIL")
            self.assertIn("selected_skills", result.message)

    def test_command_matching_requires_a_token_boundary(self):
        self.assertTrue(rules._command_matches("npm test", "npm test -- --runInBand"))
        self.assertFalse(rules._command_matches("npm test", "npm test-extra"))

    def test_lifecycle_rejects_unknown_command_event_types(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            trace_path = root / "trace.jsonl"
            write_trace(
                trace_path,
                [
                    {
                        "type": "item.updated",
                        "item": {
                            "id": "build",
                            "type": "command_execution",
                            "command": "python build.py",
                        },
                    },
                    {
                        "type": "item.completed",
                        "item": {
                            "id": "build",
                            "type": "command_execution",
                            "command": "python build.py",
                            "exit_code": 0,
                        },
                    },
                ],
            )
            config = {"require_command_lifecycle": True}

            report = rules.evaluate_trace(rules.load_jsonl(trace_path), config, root)
            result = next(item for item in report.results if item.rule_id == "TRACE-003")
            self.assertEqual(result.status, "FAIL")

    def test_cli_writes_a_structured_report(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "package.json").write_text('{"name":"demo"}\n', encoding="utf-8")
            (root / "src/main.py").write_text("def main(): pass\n", encoding="utf-8")
            trace_path = root / "trace.jsonl"
            comparison_trace = root / "comparison.jsonl"
            config_path = root / "rules.json"
            report_path = root / "report.json"
            write_trace(trace_path, event_lines(root))
            shutil.copyfile(trace_path, comparison_trace)
            config_path.write_text(
                json.dumps(happy_config(root, comparison_trace)),
                encoding="utf-8",
            )

            stdout = StringIO()
            with redirect_stdout(stdout):
                exit_code = grade_skill_trace.main(
                    [
                        "--trace",
                        str(trace_path),
                        "--config",
                        str(config_path),
                        "--project-dir",
                        str(root),
                        "--report",
                        str(report_path),
                    ]
                )

            self.assertEqual(exit_code, 0)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["exit_code"], 0)
            self.assertEqual(len(report["results"]), 20)
            self.assertIn('"has_failures": false', stdout.getvalue())

    def test_reproducibility_compares_command_exit_codes(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            current_path = root / "current.jsonl"
            comparison_path = root / "comparison.jsonl"
            write_trace(
                current_path,
                [{
                    "type": "item.completed",
                    "item": {
                        "type": "command_execution",
                        "command": "npm test",
                        "exit_code": 1,
                    },
                }],
            )
            write_trace(
                comparison_path,
                [{
                    "type": "item.completed",
                    "item": {
                        "type": "command_execution",
                        "command": "npm test",
                        "exit_code": 0,
                    },
                }],
            )

            report = rules.evaluate_trace(
                rules.load_jsonl(current_path),
                {"compare_trace": str(comparison_path)},
                root,
            )
            result = next(item for item in report.results if item.rule_id == "REPRO-001")
            self.assertEqual(result.status, "FAIL")


if __name__ == "__main__":
    unittest.main()
