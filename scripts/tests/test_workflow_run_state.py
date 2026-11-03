from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "scripts/workflow_run_state.py"
FINGERPRINT = "a" * 64
COMMIT = "b" * 40


def workflow_document() -> dict:
    return {
        "schema_version": "1.0.0",
        "id": "sample-flow",
        "version": "1.0.0",
        "kind": "sequence",
        "lifecycle_state": "EXPERIMENTAL",
        "title": {"zh": "样例流程", "en": "Sample flow"},
        "summary": {"zh": "用于状态恢复测试", "en": "State recovery fixture"},
        "inputs": [{"id": "request", "required": True, "description": "Request input."}],
        "outputs": [{"id": "result", "description": "Run result.", "evidence_kind": "execution"}],
        "steps": [
            {
                "id": "inspect",
                "description": "Read-only analysis",
                "skill_ids": ["code-review"],
                "depends_on": [],
                "on_failure": "stop",
                "permission": "read_only",
                "approval_required": False,
            },
            {
                "id": "publish",
                "description": "External write",
                "skill_ids": ["release-testing-workflow"],
                "depends_on": ["inspect"],
                "on_failure": "stop",
                "permission": "write",
                "approval_required": True,
            },
        ],
        "failure_policy": {"on_missing_dependency": "ask_user", "on_blocked": "stop"},
        "permission_policy": {"default": "read_only", "approval_required_for": ["external_write", "publish"]},
        "checkpoint_policy": {
            "host_runtime_required": True,
            "fingerprint_fields": ["inputs", "commit_sha"],
            "invalidate_on_change": ["inputs", "commit_sha"],
            "automatic_replay": "side_effect_free_only",
        },
        "handoff": {"required_fields": ["workflow_id", "source", "status", "open_gaps"]},
        "evidence_contract_version": "1.0.0",
    }


class WorkflowRunStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.skill = self.root / "skills/en/testing-workflows/sample-flow"
        self.skill.mkdir(parents=True)
        self.workflow = self.skill / "workflow.yaml"
        self.workflow.write_text(json.dumps(workflow_document()), encoding="utf-8")
        self.state_dir = self.root / "state"
        result = self.call(
            "create",
            "--workflow-file",
            str(self.workflow),
            "--state-dir",
            str(self.state_dir),
            "--input-fingerprint",
            FINGERPRINT,
            "--commit-sha",
            COMMIT,
            "--run-id",
            "run-1",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.state_file = Path(json.loads(result.stdout)["state_file"])

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def call(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def read_state(self) -> dict:
        return json.loads(self.state_file.read_text(encoding="utf-8"))

    def create_run_with_workflow(self, workflow: dict, run_id: str) -> None:
        self.workflow.write_text(json.dumps(workflow), encoding="utf-8")
        result = self.call(
            "create",
            "--workflow-file",
            str(self.workflow),
            "--state-dir",
            str(self.state_dir),
            "--input-fingerprint",
            FINGERPRINT,
            "--commit-sha",
            COMMIT,
            "--run-id",
            run_id,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.state_file = Path(json.loads(result.stdout)["state_file"])

    def start(self, stage_id: str, *extra: str) -> subprocess.CompletedProcess[str]:
        return self.call(
            "start-stage",
            "--state-file",
            str(self.state_file),
            "--workflow-file",
            str(self.workflow),
            "--stage-id",
            stage_id,
            "--expected-input-fingerprint",
            FINGERPRINT,
            "--expected-commit-sha",
            COMMIT,
            *extra,
        )

    def resume(self, fingerprint: str = FINGERPRINT, commit: str = COMMIT) -> subprocess.CompletedProcess[str]:
        return self.call(
            "resume",
            "--state-file",
            str(self.state_file),
            "--workflow-file",
            str(self.workflow),
            "--expected-input-fingerprint",
            fingerprint,
            "--expected-commit-sha",
            commit,
        )

    def test_requires_dependencies_before_starting_and_records_checkpoint(self) -> None:
        blocked = self.start("publish")
        self.assertEqual(blocked.returncode, 2)
        self.assertEqual(self.read_state()["stages"][1]["status"], "NOT_STARTED")

        started = self.start("inspect")
        self.assertEqual(started.returncode, 0, started.stderr)
        completed = self.call(
            "complete-stage",
            "--state-file",
            str(self.state_file),
            "--stage-id",
            "inspect",
            "--evidence-ref",
            "evidence:inspection-1",
            "--checkpoint-ref",
            "checkpoint:inspection-1",
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        state = self.read_state()
        self.assertEqual(state["stages"][0]["status"], "COMPLETED")
        self.assertEqual(state["stages"][0]["checkpoint_ref"], "checkpoint:inspection-1")

    def test_high_risk_stage_requires_recorded_human_approval(self) -> None:
        self.start("inspect")
        self.call(
            "complete-stage", "--state-file", str(self.state_file), "--stage-id", "inspect",
            "--evidence-ref", "evidence:inspection-1",
        )
        denied = self.start("publish")
        self.assertEqual(denied.returncode, 2)
        approved = self.start(
            "publish",
            "--confirm",
            "--approved-by",
            "release-owner",
        )
        self.assertEqual(approved.returncode, 0, approved.stderr)
        state = self.read_state()
        self.assertEqual(state["stages"][1]["approval"]["status"], "APPROVED")
        self.assertEqual(state["stages"][1]["approval"]["approved_by"], "release-owner")

    def test_duplicate_stage_start_is_rejected_without_replaying(self) -> None:
        first = self.start("inspect")
        second = self.start("inspect")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 2)
        self.assertEqual(self.read_state()["idempotency_keys"], [f"run-1:inspect:{FINGERPRINT}"])

    def test_continue_with_gap_failure_allows_an_independent_stage_and_keeps_gap(self) -> None:
        workflow = workflow_document()
        first_stage, next_stage = workflow["steps"]
        first_stage.update(id="code-review", on_failure="continue_with_gap")
        next_stage.update(
            id="requirements-analysis",
            depends_on=[],
            permission="read_only",
            approval_required=False,
            on_failure="continue_with_gap",
        )
        self.create_run_with_workflow(workflow, "run-continue-gap")

        self.assertEqual(self.start("code-review").returncode, 0)
        failed = self.call(
            "fail-stage",
            "--state-file",
            str(self.state_file),
            "--stage-id",
            "code-review",
            "--reason",
            "review evidence unavailable",
        )
        self.assertEqual(failed.returncode, 0, failed.stderr)

        next_stage = self.start("requirements-analysis")
        self.assertEqual(next_stage.returncode, 0, next_stage.stderr)
        completed = self.call(
            "complete-stage",
            "--state-file",
            str(self.state_file),
            "--stage-id",
            "requirements-analysis",
            "--evidence-ref",
            "evidence:requirements-1",
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        state = self.read_state()
        self.assertEqual(state["status"], "FAILED")
        self.assertEqual(
            {stage["id"]: stage["status"] for stage in state["stages"]},
            {"code-review": "FAILED", "requirements-analysis": "COMPLETED"},
        )

    def test_stop_failure_still_blocks_an_independent_stage(self) -> None:
        workflow = workflow_document()
        first_stage, next_stage = workflow["steps"]
        first_stage.update(id="code-review", on_failure="stop")
        next_stage.update(
            id="requirements-analysis",
            depends_on=[],
            permission="read_only",
            approval_required=False,
            on_failure="continue_with_gap",
        )
        self.create_run_with_workflow(workflow, "run-stop")

        self.assertEqual(self.start("code-review").returncode, 0)
        failed = self.call(
            "fail-stage",
            "--state-file",
            str(self.state_file),
            "--stage-id",
            "code-review",
            "--reason",
            "review failed",
        )
        self.assertEqual(failed.returncode, 0, failed.stderr)

        denied = self.start("requirements-analysis")
        self.assertEqual(denied.returncode, 2)
        self.assertIn("run status is FAILED", denied.stderr)

    def test_continue_with_gap_does_not_bypass_another_blocked_stage(self) -> None:
        workflow = workflow_document()
        failed_stage, blocked_stage = workflow["steps"]
        failed_stage.update(id="code-review", on_failure="continue_with_gap")
        blocked_stage.update(
            id="requirements-analysis",
            depends_on=[],
            permission="read_only",
            approval_required=False,
            on_failure="continue_with_gap",
        )
        workflow["steps"].append({**blocked_stage, "id": "test-case-review"})
        self.create_run_with_workflow(workflow, "run-blocked-gap")

        self.assertEqual(self.start("code-review").returncode, 0)
        self.assertEqual(self.start("requirements-analysis").returncode, 0)
        failed = self.call(
            "fail-stage",
            "--state-file",
            str(self.state_file),
            "--stage-id",
            "code-review",
            "--reason",
            "review evidence unavailable",
        )
        self.assertEqual(failed.returncode, 0, failed.stderr)
        blocked = self.call(
            "block-stage",
            "--state-file",
            str(self.state_file),
            "--stage-id",
            "requirements-analysis",
            "--reason",
            "human review required",
        )
        self.assertEqual(blocked.returncode, 0, blocked.stderr)
        self.assertEqual(self.read_state()["status"], "FAILED")

        denied = self.start("test-case-review")
        self.assertEqual(denied.returncode, 2)

    def test_input_or_commit_change_marks_saved_checkpoint_stale(self) -> None:
        resumed = self.resume(fingerprint="c" * 64)
        self.assertEqual(resumed.returncode, 1)
        state = self.read_state()
        self.assertEqual(state["status"], "STALE")
        self.assertIn("input fingerprint", state["stale_reason"])

    def test_commit_change_marks_checkpoint_stale(self) -> None:
        resumed = self.resume(commit="c" * 40)
        self.assertEqual(resumed.returncode, 1)
        state = self.read_state()
        self.assertEqual(state["status"], "STALE")
        self.assertIn("commit SHA changed", state["stale_reason"])

    def test_interrupted_running_stage_is_blocked_for_review_not_replayed(self) -> None:
        self.start("inspect")
        resumed = self.resume()
        self.assertEqual(resumed.returncode, 0, resumed.stderr)
        state = self.read_state()
        self.assertEqual(state["status"], "BLOCKED")
        self.assertEqual(state["stages"][0]["status"], "BLOCKED")
        self.assertIn("review before retry", state["stages"][0]["checkpoint_ref"])
        summary = json.loads(resumed.stdout)
        self.assertEqual(summary["ready_stages"], [])
        self.assertIs(summary["automatic_replay"], False)

    def test_refuses_state_file_symlinks(self) -> None:
        symlink = self.root / "state-link.json"
        symlink.symlink_to(self.state_file)

        result = self.call(
            "start-stage",
            "--state-file",
            str(symlink),
            "--workflow-file",
            str(self.workflow),
            "--stage-id",
            "inspect",
            "--expected-input-fingerprint",
            FINGERPRINT,
            "--expected-commit-sha",
            COMMIT,
        )

        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.read_state()["stages"][0]["status"], "NOT_STARTED")

    def test_workflow_package_change_marks_checkpoint_stale(self) -> None:
        changed = workflow_document()
        changed["steps"][0]["description"] = "Updated after run creation"
        self.workflow.write_text(json.dumps(changed), encoding="utf-8")

        resumed = self.resume()

        self.assertEqual(resumed.returncode, 1)
        state = self.read_state()
        self.assertEqual(state["status"], "STALE")
        self.assertIn("Workflow package changed", state["stale_reason"])


if __name__ == "__main__":
    unittest.main()
