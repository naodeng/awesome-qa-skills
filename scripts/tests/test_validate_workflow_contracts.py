import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_workflow_contracts import (
    validate_evidence,
    validate_repo,
    validate_run_state,
    validate_workflow,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


def valid_workflow() -> dict:
    return {
        "schema_version": "1.0.0",
        "id": "sample-flow",
        "version": "1.0.0",
        "kind": "sequence",
        "lifecycle_state": "EXPERIMENTAL",
        "title": {"zh": "样例流程", "en": "Sample workflow"},
        "summary": {"zh": "样例说明", "en": "Sample summary"},
        "inputs": [{"id": "request", "required": True, "description": "User goal"}],
        "outputs": [{"id": "review", "description": "Review result", "evidence_kind": "fact"}],
        "steps": [
            {
                "id": "inspect",
                "description": "Inspect the supplied change",
                "skill_ids": ["code-review"],
                "prompt": "prompts/review.md",
                "depends_on": [],
                "on_failure": "stop",
                "permission": "read_only",
                "approval_required": False,
            }
        ],
        "failure_policy": {
            "on_missing_dependency": "continue_with_limitations",
            "on_blocked": "stop",
        },
        "permission_policy": {
            "default": "read_only",
            "approval_required_for": ["external_write", "delete"],
        },
        "checkpoint_policy": {
            "host_runtime_required": True,
            "fingerprint_fields": ["inputs", "commit_sha"],
            "invalidate_on_change": ["inputs", "commit_sha"],
            "automatic_replay": "side_effect_free_only",
        },
        "handoff": {"required_fields": ["workflow_id", "source", "status", "open_gaps"]},
        "evidence_contract_version": "1.0.0",
    }


def valid_evidence() -> dict:
    return {
        "schema_version": "1.0.0",
        "workflow_id": "sample-flow",
        "workflow_version": "1.0.0",
        "run_id": "run-123",
        "input_fingerprint": "a" * 64,
        "commit_sha": "b" * 40,
        "generated_at": "2026-10-30T08:00:00Z",
        "status": "PASS",
        "evidence": [
            {
                "id": "test-run",
                "kind": "execution",
                "claim": "The focused unit test command passed.",
                "status": "PASS",
                "source": {"type": "command", "reference": "pytest output"},
                "producer": {"skill_id": "sample-flow", "version": "1.0.0"},
                "observed_at": "2026-10-30T08:00:00Z",
                "execution": {
                    "type": "unit_test",
                    "scope": "test_execution",
                    "command": "pytest -q",
                    "exit_code": 0,
                    "environment": "local",
                    "started_at": "2026-10-30T07:59:00Z",
                    "finished_at": "2026-10-30T08:00:00Z",
                },
            }
        ],
    }


def valid_run_state() -> dict:
    return {
        "schema_version": "1.0.0",
        "run_id": "run-123",
        "workflow_id": "sample-flow",
        "workflow_version": "1.0.0",
        "status": "COMPLETED",
        "input_fingerprint": "a" * 64,
        "workflow_source_sha256": "c" * 64,
        "commit_sha": "b" * 40,
        "created_at": "2026-10-30T07:00:00Z",
        "updated_at": "2026-10-30T08:00:00Z",
        "stages": [
            {"id": "inspect", "status": "COMPLETED", "attempt": 1, "evidence_refs": ["test-run"]}
        ],
        "artifacts": [{"id": "test-run", "location": "evidence.json"}],
        "idempotency_keys": ["run-123:inspect:" + "a" * 64],
    }


class WorkflowContractTests(unittest.TestCase):
    def test_accepts_a_complete_workflow_contract(self) -> None:
        self.assertEqual(validate_workflow(valid_workflow()), [])

    def test_rejects_untagged_composite_workflow_result_deliverable(self) -> None:
        workflow = valid_workflow()
        workflow["outputs"] = [
            {
                "id": "workflow_result",
                "description": "Scoped result, evidence states, open gaps, and next handoff.",
                "evidence_kind": "fact",
            }
        ]

        errors = validate_workflow(workflow)

        self.assertTrue(any("not a typed deliverable" in error for error in errors), errors)

    def test_rejects_a_step_that_depends_on_an_unknown_step(self) -> None:
        workflow = valid_workflow()
        workflow["steps"][0]["depends_on"] = ["missing-step"]

        errors = validate_workflow(workflow)

        self.assertTrue(any("unknown dependency step" in error for error in errors), errors)

    def test_rejects_cyclic_step_dependencies(self) -> None:
        workflow = valid_workflow()
        workflow["steps"][0]["depends_on"] = ["verify"]
        workflow["steps"].append(
            {
                **workflow["steps"][0],
                "id": "verify",
                "depends_on": ["inspect"],
            }
        )

        errors = validate_workflow(workflow)

        self.assertTrue(any("dependency cycle" in error for error in errors), errors)

    def test_skip_conditions_require_both_condition_and_reason(self) -> None:
        workflow = valid_workflow()
        workflow["steps"][0]["skip_when"] = [{"condition": "input is absent"}]

        errors = validate_workflow(workflow)

        self.assertTrue(any("skip_when" in error for error in errors), errors)

    def test_rejects_escaping_prompt_paths(self) -> None:
        workflow = valid_workflow()
        workflow["steps"][0]["prompt"] = "../other-skill/prompt.md"

        errors = validate_workflow(workflow)

        self.assertTrue(any("must stay inside the Skill package" in error for error in errors), errors)

    def test_rejects_static_analysis_as_runtime_test_evidence(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0]["execution"]["type"] = "static_analysis"

        errors = validate_evidence(evidence)

        self.assertTrue(any("cannot substantiate test_execution" in error for error in errors), errors)

    def test_rejects_pass_test_execution_with_nonzero_exit_code(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0]["execution"]["exit_code"] = 1

        errors = validate_evidence(evidence)

        self.assertTrue(any("PASS" in error and "exit_code" in error for error in errors), errors)

    def test_rejects_boolean_test_execution_exit_code(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0]["execution"]["exit_code"] = True

        errors = validate_evidence(evidence)

        self.assertTrue(any("integer exit code" in error for error in errors), errors)

    def test_requires_execution_details_for_execution_evidence(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0].pop("execution")

        errors = validate_evidence(evidence)

        self.assertTrue(any("requires execution details" in error for error in errors), errors)

    def test_rejects_expired_pass_evidence(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0]["valid_until"] = "2026-10-29T23:59:00Z"

        errors = validate_evidence(evidence, now=datetime(2026, 10, 30, 0, 0, tzinfo=timezone.utc))

        self.assertTrue(any("expired evidence cannot remain PASS" in error for error in errors), errors)

    def test_rejects_evidence_summary_status_that_disagrees_with_records(self) -> None:
        mismatches = (
            ("PASS", "FAIL"),
            ("FAIL", "PASS"),
            ("BLOCKED", "UNKNOWN"),
            ("UNKNOWN", "BLOCKED"),
        )

        for summary_status, item_status in mismatches:
            with self.subTest(summary_status=summary_status, item_status=item_status):
                evidence = valid_evidence()
                evidence["status"] = summary_status
                evidence["evidence"][0]["status"] = item_status

                errors = validate_evidence(evidence)

                self.assertTrue(any("does not reconcile" in error for error in errors), errors)

    def test_accepts_evidence_summary_status_derived_from_records(self) -> None:
        matching = (
            ("PASS", ["PASS"]),
            ("FAIL", ["PASS", "FAIL"]),
            ("BLOCKED", ["PASS", "BLOCKED"]),
            ("UNKNOWN", ["PASS", "UNKNOWN"]),
            ("UNKNOWN", []),
        )

        for summary_status, item_statuses in matching:
            with self.subTest(summary_status=summary_status, item_statuses=item_statuses):
                evidence = valid_evidence()
                evidence["status"] = summary_status
                evidence["evidence"] = [
                    {**evidence["evidence"][0], "id": f"record-{index}", "status": status}
                    for index, status in enumerate(item_statuses)
                ]

                errors = validate_evidence(evidence)

                self.assertFalse(any("status does not reconcile" in error for error in errors), errors)

    def test_reports_malformed_evidence_status_without_crashing(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0]["status"] = ["PASS"]

        try:
            errors = validate_evidence(evidence)
        except Exception as exc:  # The validator must report malformed input as a finding.
            self.fail(f"validator raised instead of reporting malformed status: {exc!r}")

        self.assertTrue(any("evidence[0].status" in error for error in errors), errors)

    def test_reports_malformed_dependency_without_crashing(self) -> None:
        workflow = valid_workflow()
        workflow["steps"][0]["depends_on"] = [["inspect"]]

        try:
            errors = validate_workflow(workflow)
        except Exception as exc:  # Malformed contract data should produce findings, not abort validation.
            self.fail(f"validator raised instead of reporting malformed dependency: {exc!r}")

        self.assertTrue(any("depends_on" in error for error in errors), errors)

    def test_rejects_commit_mismatch_before_resume(self) -> None:
        state = valid_run_state()

        errors = validate_run_state(state, expected_commit_sha="c" * 40)

        self.assertTrue(any("STALE" in error for error in errors), errors)

    def test_rejects_confidence_outside_zero_to_one(self) -> None:
        evidence = valid_evidence()
        evidence["evidence"][0]["confidence"] = 1.2

        errors = validate_evidence(evidence)

        self.assertTrue(any("confidence" in error for error in errors), errors)

    def test_invalidates_checkpoint_when_input_fingerprint_changes(self) -> None:
        state = valid_run_state()

        errors = validate_run_state(state, expected_input_fingerprint="c" * 64)

        self.assertTrue(any("STALE" in error for error in errors), errors)

    def test_completed_run_cannot_contain_a_running_stage(self) -> None:
        state = valid_run_state()
        state["stages"][0]["status"] = "RUNNING"

        errors = validate_run_state(state)

        self.assertTrue(any("terminal stage states" in error for error in errors), errors)

    def test_requires_reason_for_stale_checkpoint(self) -> None:
        state = valid_run_state()
        state["status"] = "STALE"

        errors = validate_run_state(state)

        self.assertTrue(any("stale_reason" in error for error in errors), errors)

    def test_rejects_invalid_human_approval_record(self) -> None:
        state = valid_run_state()
        state["stages"][0]["approval"] = {
            "status": "PENDING",
            "approved_by": "",
            "approved_at": "not-a-timestamp",
            "scope": "write_repo",
        }

        errors = validate_run_state(state)

        self.assertTrue(any("approval.status" in error for error in errors), errors)
        self.assertTrue(any("approval.approved_by" in error for error in errors), errors)
        self.assertTrue(any("approval.approved_at" in error for error in errors), errors)

    def test_schema_files_are_valid_json_schema_documents(self) -> None:
        schema_root = REPO_ROOT / "resources" / "workflows" / "schemas"
        for name in ("workflow.schema.json", "evidence.schema.json", "run-state.schema.json"):
            with self.subTest(schema=name):
                data = json.loads((schema_root / name).read_text(encoding="utf-8"))
                self.assertEqual(data["$schema"], "https://json-schema.org/draft/2020-12/schema")
                self.assertEqual(data["type"], "object")
                self.assertIn("required", data)

    def test_workflow_schema_enforces_checkpoint_runtime_and_invalidation_fields(self) -> None:
        schema_path = REPO_ROOT / "resources/workflows/schemas/workflow.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        checkpoint = schema.get("properties", {}).get("checkpoint_policy")

        self.assertIsInstance(checkpoint, dict, "checkpoint_policy must be declared in the schema")
        self.assertIn("checkpoint_policy", schema["required"])
        self.assertIs(checkpoint["properties"]["host_runtime_required"].get("const"), True)
        invalidation = checkpoint["properties"]["invalidate_on_change"]
        required_values = {
            condition.get("contains", {}).get("const")
            for condition in invalidation.get("allOf", [])
        }
        self.assertTrue({"inputs", "commit_sha"}.issubset(required_values), invalidation)

    def test_evidence_schema_declares_all_aggregate_status_rules(self) -> None:
        schema_path = REPO_ROOT / "resources/workflows/schemas/evidence.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        rules = {
            rule.get("if", {}).get("properties", {}).get("status", {}).get("const"): rule.get("then", {})
            for rule in schema.get("allOf", [])
        }

        self.assertEqual(set(rules), {"PASS", "FAIL", "BLOCKED", "UNKNOWN"})
        pass_items = rules["PASS"].get("properties", {}).get("evidence", {})
        self.assertGreaterEqual(pass_items.get("minItems", 0), 1)
        self.assertEqual(pass_items.get("items", {}).get("properties", {}).get("status", {}).get("const"), "PASS")

    def test_evidence_schema_requires_successful_exit_for_passing_test_execution(self) -> None:
        schema_path = REPO_ROOT / "resources/workflows/schemas/evidence.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        rules = schema["$defs"]["evidenceItem"]["allOf"]

        def has_test_execution_scope(rule: dict) -> bool:
            return (
                rule.get("if", {})
                .get("properties", {})
                .get("execution", {})
                .get("properties", {})
                .get("scope", {})
                .get("const")
                == "test_execution"
            )

        requires_exit_code = any(
            has_test_execution_scope(rule)
            and set(rule.get("if", {}).get("properties", {}).get("status", {}).get("enum", [])) == {"PASS", "FAIL"}
            and "exit_code" in rule.get("then", {}).get("properties", {}).get("execution", {}).get("required", [])
            for rule in rules
        )
        passing_exit_code = any(
            has_test_execution_scope(rule)
            and rule.get("if", {}).get("properties", {}).get("status", {}).get("const") == "PASS"
            and rule.get("then", {}).get("properties", {}).get("execution", {}).get("properties", {}).get("exit_code", {}).get("const") == 0
            for rule in rules
        )

        self.assertTrue(requires_exit_code, "PASS/FAIL test_execution must require exit_code")
        self.assertTrue(passing_exit_code, "PASS test_execution must require exit_code 0")

    def test_repository_check_reports_bilingual_contract_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for lang in ("zh", "en"):
                package = root / "skills" / lang / "testing-workflows" / "sample-flow"
                (package / "prompts").mkdir(parents=True)
                (package / "prompts" / "review.md").write_text("Review", encoding="utf-8")
                (package / "workflow.yaml").write_text(json.dumps(valid_workflow()), encoding="utf-8")

            en_file = root / "skills" / "en" / "testing-workflows" / "sample-flow" / "workflow.yaml"
            en_workflow = json.loads(en_file.read_text(encoding="utf-8"))
            en_workflow["version"] = "1.0.1"
            en_file.write_text(json.dumps(en_workflow), encoding="utf-8")

            report = validate_repo(root)

            self.assertTrue(any("bilingual contract mismatch" in error for error in report["errors"]), report)

    def test_repository_check_rejects_unknown_skill_references(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            shutil.copytree(REPO_ROOT / "resources/workflows", root / "resources/workflows")
            for language in ("zh", "en"):
                package = root / "skills" / language / "testing-workflows" / "sample-flow"
                (package / "prompts").mkdir(parents=True)
                (package / "prompts/review.md").write_text("Review", encoding="utf-8")
                workflow = valid_workflow()
                workflow["steps"][0]["skill_ids"] = ["missing-skill"]
                (package / "workflow.yaml").write_text(json.dumps(workflow), encoding="utf-8")

            report = validate_repo(root)

            self.assertTrue(any("unknown canonical Skill ID 'missing-skill'" in error for error in report["errors"]), report)

    def test_pr_quality_review_output_does_not_label_mixed_analysis_as_fact(self) -> None:
        workflow_path = REPO_ROOT / "skills/zh/testing-workflows/pr-quality-review/workflow.yaml"
        workflow = json.loads(workflow_path.read_text(encoding="utf-8"))

        output_kinds = {output["id"]: output["evidence_kind"] for output in workflow["outputs"]}

        self.assertEqual(
            output_kinds,
            {"review_findings": "inference", "evidence_gaps": "fact", "next_actions": "plan"},
        )


if __name__ == "__main__":
    unittest.main()
