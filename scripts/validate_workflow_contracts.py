#!/usr/bin/env python3
"""Validate JSON-compatible YAML workflow, evidence, and run-state contracts."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import re
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0.0"
SCHEMA_ROOT = Path("resources/workflows/schemas")
SCHEMAS = ("workflow.schema.json", "evidence.schema.json", "run-state.schema.json")
EVIDENCE_STATES = {"PASS", "FAIL", "BLOCKED", "UNKNOWN"}
RUN_STATES = {"NOT_STARTED", "RUNNING", "COMPLETED", "FAILED", "BLOCKED", "STALE"}
STAGE_STATES = RUN_STATES | {"SKIPPED"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ID_RE = re.compile(r"^[a-z][a-z0-9_-]*$")
VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?$")
SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")
COMMIT_RE = re.compile(r"^(?:[a-fA-F0-9]{40}|[a-fA-F0-9]{64})$")
PERMISSIONS = {"read_only", "suggest_only", "write"}
APPROVAL_ACTIONS = {"execute_command", "write_repo", "external_write", "publish", "delete", "release_approval"}
EXECUTION_TYPES = {"static_analysis", "unit_test", "integration_test", "e2e_test", "manual_test", "model_eval", "install_check", "build", "other"}
EXECUTION_SCOPES = {"static_structure", "static_analysis", "test_execution", "model_behavior", "install_compatibility", "other"}
TEST_EXECUTION_TYPES = {"unit_test", "integration_test", "e2e_test", "manual_test"}


def _is_object(value: Any) -> bool:
    return isinstance(value, dict)


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def _check_localized(value: Any, path: str, errors: list[str]) -> None:
    if not _is_object(value):
        errors.append(f"{path}: must be an object with zh and en text")
        return
    for language in ("zh", "en"):
        if not _nonempty_string(value.get(language)):
            errors.append(f"{path}.{language}: must be a non-empty string")


def _check_unique_ids(items: Any, path: str, errors: list[str]) -> set[str]:
    if not isinstance(items, list) or not items:
        errors.append(f"{path}: must be a non-empty array")
        return set()
    ids: set[str] = set()
    for index, item in enumerate(items):
        location = f"{path}[{index}]"
        if not _is_object(item):
            errors.append(f"{location}: must be an object")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not ID_RE.fullmatch(item_id):
            errors.append(f"{location}.id: must be a lowercase identifier")
        elif item_id in ids:
            errors.append(f"{location}.id: duplicate identifier {item_id!r}")
        else:
            ids.add(item_id)
    return ids


def validate_workflow(
    workflow: Any,
    package_dir: Path | None = None,
    available_skill_ids: set[str] | None = None,
) -> list[str]:
    """Return actionable workflow-contract violations."""
    errors: list[str] = []
    if not _is_object(workflow):
        return ["workflow: root must be an object"]

    required = (
        "schema_version", "id", "version", "kind", "title", "summary", "lifecycle_state",
        "inputs", "outputs", "steps", "failure_policy", "permission_policy",
        "checkpoint_policy", "handoff", "evidence_contract_version",
    )
    for field in required:
        if field not in workflow:
            errors.append(f"workflow.{field}: is required")

    if workflow.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"workflow.schema_version: must be {SCHEMA_VERSION}")
    if not isinstance(workflow.get("id"), str) or not SLUG_RE.fullmatch(workflow.get("id", "")):
        errors.append("workflow.id: must be a canonical lowercase slug")
    if not isinstance(workflow.get("version"), str) or not VERSION_RE.fullmatch(workflow.get("version", "")):
        errors.append("workflow.version: must be a semantic version")
    if workflow.get("kind") not in {"sequence", "router", "task_set", "single_task"}:
        errors.append("workflow.kind: must be sequence, router, task_set, or single_task")
    if workflow.get("lifecycle_state") not in {"UNASSESSED", "EXPERIMENTAL", "STABLE", "MAINTENANCE", "DEPRECATED"}:
        errors.append("workflow.lifecycle_state: is not a supported lifecycle state")
    if workflow.get("evidence_contract_version") != SCHEMA_VERSION:
        errors.append(f"workflow.evidence_contract_version: must be {SCHEMA_VERSION}")
    _check_localized(workflow.get("title"), "workflow.title", errors)
    _check_localized(workflow.get("summary"), "workflow.summary", errors)

    for field in ("inputs", "outputs"):
        items = workflow.get(field)
        ids = _check_unique_ids(items, f"workflow.{field}", errors)
        for index, item in enumerate(items if isinstance(items, list) else []):
            if not _is_object(item):
                continue
            location = f"workflow.{field}[{index}]"
            if not _nonempty_string(item.get("description")):
                errors.append(f"{location}.description: must be a non-empty string")
            if field == "inputs" and not isinstance(item.get("required"), bool):
                errors.append(f"{location}.required: must be a boolean")
            if field == "outputs" and item.get("evidence_kind") not in {"fact", "inference", "plan", "execution"}:
                errors.append(f"{location}.evidence_kind: is not a supported evidence kind")
    steps = workflow.get("steps")
    step_ids = _check_unique_ids(steps, "workflow.steps", errors)
    for index, step in enumerate(steps if isinstance(steps, list) else []):
        if not _is_object(step):
            continue
        location = f"workflow.steps[{index}]"
        if not _nonempty_string(step.get("description")):
            errors.append(f"{location}.description: must be a non-empty string")
        skill_ids = step.get("skill_ids")
        if not isinstance(skill_ids, list) or any(not isinstance(skill_id, str) or not SLUG_RE.fullmatch(skill_id) for skill_id in skill_ids):
            errors.append(f"{location}.skill_ids: must be an array of canonical Skill IDs")
        elif available_skill_ids is not None:
            for skill_id in skill_ids:
                if skill_id not in available_skill_ids:
                    errors.append(f"{location}.skill_ids: unknown canonical Skill ID {skill_id!r}")
        dependencies = step.get("depends_on")
        if not isinstance(dependencies, list) or any(not isinstance(value, str) for value in dependencies):
            errors.append(f"{location}.depends_on: must be an array of step IDs")
        else:
            for dependency in dependencies:
                if dependency not in step_ids and dependency != step.get("id"):
                    errors.append(f"{location}.depends_on: unknown dependency step {dependency!r}")
                elif dependency == step.get("id"):
                    errors.append(f"{location}.depends_on: a step cannot depend on itself")
        if step.get("on_failure") not in {"stop", "continue_with_gap", "handoff"}:
            errors.append(f"{location}.on_failure: must be stop, continue_with_gap, or handoff")
        if step.get("permission") not in PERMISSIONS:
            errors.append(f"{location}.permission: is not a supported permission level")
        if not isinstance(step.get("approval_required"), bool):
            errors.append(f"{location}.approval_required: must be a boolean")
        skip_when = step.get("skip_when")
        if skip_when is not None:
            if not isinstance(skip_when, list):
                errors.append(f"{location}.skip_when: must be an array of explicit conditions")
            else:
                for condition_index, condition in enumerate(skip_when):
                    condition_location = f"{location}.skip_when[{condition_index}]"
                    if not _is_object(condition):
                        errors.append(f"{condition_location}: must include condition and reason")
                    else:
                        for field in ("condition", "reason"):
                            if not _nonempty_string(condition.get(field)):
                                errors.append(f"{condition_location}.{field}: must be a non-empty string")
        prompt = step.get("prompt")
        if prompt is not None:
            if not _nonempty_string(prompt):
                errors.append(f"{location}.prompt: must be a package-relative path")
            else:
                candidate = Path(prompt)
                if candidate.is_absolute() or ".." in candidate.parts:
                    errors.append(f"{location}.prompt: must stay inside the Skill package")
                elif package_dir is not None and not (package_dir / candidate).is_file():
                    errors.append(f"{location}.prompt: package resource does not exist: {prompt}")

    dependency_map: dict[str, set[str]] = {}
    for step in steps if isinstance(steps, list) else []:
        if not _is_object(step) or not isinstance(step.get("id"), str) or step.get("id") not in step_ids:
            continue
        dependencies = step.get("depends_on")
        if isinstance(dependencies, list):
            dependency_map.setdefault(step["id"], set()).update(
                dependency
                for dependency in dependencies
                if isinstance(dependency, str) and dependency in step_ids
            )
    resolved_steps: set[str] = set()
    while True:
        ready_steps = {
            step_id
            for step_id, dependencies in dependency_map.items()
            if step_id not in resolved_steps and dependencies.issubset(resolved_steps)
        }
        if not ready_steps:
            break
        resolved_steps.update(ready_steps)
    if len(resolved_steps) != len(dependency_map):
        cyclic_or_blocked = sorted(set(dependency_map) - resolved_steps)
        errors.append(
            "workflow.steps.depends_on: dependency cycle detected among "
            + ", ".join(cyclic_or_blocked)
        )

    failure = workflow.get("failure_policy")
    if not _is_object(failure):
        errors.append("workflow.failure_policy: must be an object")
    else:
        if failure.get("on_missing_dependency") not in {"fail_closed", "continue_with_limitations", "ask_user"}:
            errors.append("workflow.failure_policy.on_missing_dependency: is not supported")
        if failure.get("on_blocked") not in {"stop", "continue_with_gap", "handoff"}:
            errors.append("workflow.failure_policy.on_blocked: is not supported")

    permissions = workflow.get("permission_policy")
    if not _is_object(permissions):
        errors.append("workflow.permission_policy: must be an object")
    else:
        if permissions.get("default") not in PERMISSIONS:
            errors.append("workflow.permission_policy.default: is not supported")
        actions = permissions.get("approval_required_for")
        if not isinstance(actions, list) or any(action not in APPROVAL_ACTIONS for action in actions):
            errors.append("workflow.permission_policy.approval_required_for: contains an unsupported action")

    checkpoint = workflow.get("checkpoint_policy")
    if not _is_object(checkpoint):
        errors.append("workflow.checkpoint_policy: must be an object")
    else:
        if not isinstance(checkpoint.get("host_runtime_required"), bool) or checkpoint.get("host_runtime_required") is not True:
            errors.append("workflow.checkpoint_policy.host_runtime_required: must be true; Workflow stage execution requires a host Runtime")
        for field in ("fingerprint_fields", "invalidate_on_change"):
            values = checkpoint.get(field)
            if not isinstance(values, list) or not values or any(not _nonempty_string(value) for value in values):
                errors.append(f"workflow.checkpoint_policy.{field}: must be a non-empty string array")
        if checkpoint.get("automatic_replay") not in {"none", "side_effect_free_only"}:
            errors.append("workflow.checkpoint_policy.automatic_replay: must be none or side_effect_free_only")
        if isinstance(checkpoint.get("invalidate_on_change"), list) and not {"inputs", "commit_sha"}.issubset(set(checkpoint["invalidate_on_change"])):
            errors.append("workflow.checkpoint_policy.invalidate_on_change: must include inputs and commit_sha")

    handoff = workflow.get("handoff")
    if not _is_object(handoff) or not isinstance(handoff.get("required_fields"), list) or not handoff["required_fields"] or any(not _nonempty_string(value) for value in handoff["required_fields"]):
        errors.append("workflow.handoff.required_fields: must be a non-empty string array")
    return errors


def validate_evidence(
    document: Any,
    *,
    expected_input_fingerprint: str | None = None,
    expected_commit_sha: str | None = None,
    now: datetime | None = None,
) -> list[str]:
    """Validate evidence shape and reject runtime claims without runtime evidence."""
    errors: list[str] = []
    if not _is_object(document):
        return ["evidence: root must be an object"]
    required = ("schema_version", "workflow_id", "workflow_version", "run_id", "input_fingerprint", "commit_sha", "generated_at", "status", "evidence")
    for field in required:
        if field not in document:
            errors.append(f"evidence.{field}: is required")
    if document.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"evidence.schema_version: must be {SCHEMA_VERSION}")
    if not isinstance(document.get("workflow_id"), str) or not SLUG_RE.fullmatch(document.get("workflow_id", "")):
        errors.append("evidence.workflow_id: must be a canonical lowercase slug")
    if not isinstance(document.get("input_fingerprint"), str) or not SHA256_RE.fullmatch(document.get("input_fingerprint", "")):
        errors.append("evidence.input_fingerprint: must be a SHA-256 fingerprint")
    if not isinstance(document.get("commit_sha"), str) or not COMMIT_RE.fullmatch(document.get("commit_sha", "")):
        errors.append("evidence.commit_sha: must be a 40- or 64-character commit SHA")
    if not isinstance(document.get("status"), str) or document.get("status") not in EVIDENCE_STATES:
        errors.append("evidence.status: must be PASS, FAIL, BLOCKED, or UNKNOWN")
    if not _parse_datetime(document.get("generated_at")):
        errors.append("evidence.generated_at: must be an ISO-8601 timestamp with a timezone")
    records = document.get("evidence")
    if not isinstance(records, list):
        errors.append("evidence.evidence: must be an array")
        records = []
    if document.get("status") == "PASS" and not records:
        errors.append("evidence.evidence: PASS requires at least one evidence record")
    item_statuses: set[str] = set()
    for record in records:
        if not _is_object(record):
            continue
        status = record.get("status")
        item_statuses.add(status if isinstance(status, str) and status in EVIDENCE_STATES else "UNKNOWN")
    if "FAIL" in item_statuses:
        derived_status = "FAIL"
    elif "BLOCKED" in item_statuses:
        derived_status = "BLOCKED"
    elif not item_statuses or "UNKNOWN" in item_statuses:
        derived_status = "UNKNOWN"
    else:
        derived_status = "PASS"
    if isinstance(document.get("status"), str) and document.get("status") in EVIDENCE_STATES and document.get("status") != derived_status:
        errors.append(
            f"evidence.status: does not reconcile with evidence records; expected {derived_status} "
            "using FAIL > BLOCKED > UNKNOWN > PASS"
        )
    if expected_input_fingerprint and document.get("input_fingerprint") != expected_input_fingerprint:
        errors.append("evidence.input_fingerprint changed; evidence is STALE")
    if expected_commit_sha and document.get("commit_sha") != expected_commit_sha:
        errors.append("evidence.commit_sha changed; evidence is STALE")

    seen: set[str] = set()
    for index, record in enumerate(records):
        location = f"evidence.evidence[{index}]"
        if not _is_object(record):
            errors.append(f"{location}: must be an object")
            continue
        for field in ("id", "kind", "claim", "status", "source", "producer", "observed_at"):
            if field not in record:
                errors.append(f"{location}.{field}: is required")
        record_id = record.get("id")
        if not _nonempty_string(record_id):
            errors.append(f"{location}.id: must be a non-empty string")
        elif record_id in seen:
            errors.append(f"{location}.id: duplicate evidence id {record_id!r}")
        else:
            seen.add(record_id)
        if record.get("kind") not in {"fact", "inference", "plan", "execution"}:
            errors.append(f"{location}.kind: must be fact, inference, plan, or execution")
        if not _nonempty_string(record.get("claim")):
            errors.append(f"{location}.claim: must be a non-empty string")
        if not isinstance(record.get("status"), str) or record.get("status") not in EVIDENCE_STATES:
            errors.append(f"{location}.status: must be PASS, FAIL, BLOCKED, or UNKNOWN")
        source = record.get("source")
        if not _is_object(source) or source.get("type") not in {"file", "command", "artifact", "user_statement", "ci_run", "model_eval", "manual_observation"} or not _nonempty_string(source.get("reference")):
            errors.append(f"{location}.source: must include source type and reference")
        producer = record.get("producer")
        if not _is_object(producer) or not _nonempty_string(producer.get("skill_id")) or not _nonempty_string(producer.get("version")):
            errors.append(f"{location}.producer: must include skill_id and version")
        if not _parse_datetime(record.get("observed_at")):
            errors.append(f"{location}.observed_at: must be an ISO-8601 timestamp with a timezone")
        if "confidence" in record and (not isinstance(record["confidence"], (int, float)) or not 0 <= record["confidence"] <= 1):
            errors.append(f"{location}.confidence: must be between 0 and 1")
        valid_until = record.get("valid_until")
        if valid_until is not None:
            expiry = _parse_datetime(valid_until)
            if expiry is None:
                errors.append(f"{location}.valid_until: must be an ISO-8601 timestamp with a timezone")
            elif expiry <= (now or datetime.now(timezone.utc)) and record.get("status") == "PASS":
                errors.append(f"{location}: expired evidence cannot remain PASS; downgrade it to UNKNOWN or collect fresh evidence")
        if record.get("kind") == "inference" and (not isinstance(record.get("basis"), list) or not record.get("basis")):
            errors.append(f"{location}.basis: inference evidence requires a non-empty basis list")
        if record.get("kind") == "execution":
            execution = record.get("execution")
            if not _is_object(execution):
                errors.append(f"{location}: execution evidence requires execution details")
                continue
            if execution.get("type") not in EXECUTION_TYPES:
                errors.append(f"{location}.execution.type: is not supported")
            if execution.get("scope") not in EXECUTION_SCOPES:
                errors.append(f"{location}.execution.scope: is not supported")
            for field in ("environment", "started_at", "finished_at"):
                if not _nonempty_string(execution.get(field)):
                    errors.append(f"{location}.execution.{field}: is required")
            if execution.get("scope") == "test_execution" and execution.get("type") not in TEST_EXECUTION_TYPES:
                errors.append(f"{location}.execution: {execution.get('type')} cannot substantiate test_execution")
            if (
                execution.get("scope") == "test_execution"
                and record.get("status") in ("PASS", "FAIL")
                and not isinstance(execution.get("exit_code"), int)
            ):
                errors.append(f"{location}.execution.exit_code: test_execution requires an integer exit code")
            for field in ("started_at", "finished_at"):
                if not _parse_datetime(execution.get(field)):
                    errors.append(f"{location}.execution.{field}: must be an ISO-8601 timestamp with a timezone")
            if _parse_datetime(execution.get("started_at")) and _parse_datetime(execution.get("finished_at")) and _parse_datetime(execution["finished_at"]) < _parse_datetime(execution["started_at"]):
                errors.append(f"{location}.execution: finished_at cannot be earlier than started_at")
    return errors


def validate_run_state(document: Any, *, expected_input_fingerprint: str | None = None, expected_commit_sha: str | None = None) -> list[str]:
    """Validate resumable run state and require explicit stale invalidation."""
    errors: list[str] = []
    if not _is_object(document):
        return ["run_state: root must be an object"]
    required = ("schema_version", "run_id", "workflow_id", "workflow_version", "status", "input_fingerprint", "workflow_source_sha256", "commit_sha", "created_at", "updated_at", "stages", "artifacts", "idempotency_keys")
    for field in required:
        if field not in document:
            errors.append(f"run_state.{field}: is required")
    if document.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"run_state.schema_version: must be {SCHEMA_VERSION}")
    if document.get("status") not in RUN_STATES:
        errors.append("run_state.status: is not supported")
    if not isinstance(document.get("input_fingerprint"), str) or not SHA256_RE.fullmatch(document.get("input_fingerprint", "")):
        errors.append("run_state.input_fingerprint: must be a SHA-256 fingerprint")
    if not isinstance(document.get("workflow_source_sha256"), str) or not SHA256_RE.fullmatch(document.get("workflow_source_sha256", "")):
        errors.append("run_state.workflow_source_sha256: must fingerprint the Workflow package at run creation")
    if not isinstance(document.get("commit_sha"), str) or not COMMIT_RE.fullmatch(document.get("commit_sha", "")):
        errors.append("run_state.commit_sha: must be a 40- or 64-character commit SHA")
    if document.get("status") == "STALE" and not _nonempty_string(document.get("stale_reason")):
        errors.append("run_state.stale_reason: is required when status is STALE")
    created_at = _parse_datetime(document.get("created_at"))
    updated_at = _parse_datetime(document.get("updated_at"))
    if not created_at:
        errors.append("run_state.created_at: must be an ISO-8601 timestamp with a timezone")
    if not updated_at:
        errors.append("run_state.updated_at: must be an ISO-8601 timestamp with a timezone")
    if created_at and updated_at and updated_at < created_at:
        errors.append("run_state.updated_at cannot be earlier than created_at")
    if expected_input_fingerprint and document.get("input_fingerprint") != expected_input_fingerprint:
        errors.append("run_state input changed; mark this checkpoint STALE before resuming")
    if expected_commit_sha and document.get("commit_sha") != expected_commit_sha:
        errors.append("run_state commit SHA changed; mark this checkpoint STALE before resuming")

    stages = document.get("stages")
    if not isinstance(stages, list):
        errors.append("run_state.stages: must be an array")
        stages = []
    seen: set[str] = set()
    for index, stage in enumerate(stages):
        location = f"run_state.stages[{index}]"
        if not _is_object(stage):
            errors.append(f"{location}: must be an object")
            continue
        stage_id = stage.get("id")
        if not _nonempty_string(stage_id):
            errors.append(f"{location}.id: must be a non-empty string")
        elif stage_id in seen:
            errors.append(f"{location}.id: duplicate stage id {stage_id!r}")
        else:
            seen.add(stage_id)
        if stage.get("status") not in STAGE_STATES:
            errors.append(f"{location}.status: is not supported")
        if not isinstance(stage.get("attempt"), int) or stage.get("attempt", -1) < 0:
            errors.append(f"{location}.attempt: must be a non-negative integer")
        if not isinstance(stage.get("evidence_refs"), list):
            errors.append(f"{location}.evidence_refs: must be an array")
        approval = stage.get("approval")
        if approval is not None:
            if not _is_object(approval):
                errors.append(f"{location}.approval: must be an approval record")
            else:
                allowed_approval_fields = {"status", "approved_by", "approved_at", "scope"}
                unknown_fields = sorted(set(approval) - allowed_approval_fields)
                if unknown_fields:
                    errors.append(f"{location}.approval: unsupported fields {', '.join(unknown_fields)}")
                if approval.get("status") != "APPROVED":
                    errors.append(f"{location}.approval.status: must be APPROVED")
                if not _nonempty_string(approval.get("approved_by")):
                    errors.append(f"{location}.approval.approved_by: must be a non-empty human identifier")
                if not _parse_datetime(approval.get("approved_at")):
                    errors.append(f"{location}.approval.approved_at: must be an ISO-8601 timestamp with a timezone")
                if not _nonempty_string(approval.get("scope")):
                    errors.append(f"{location}.approval.scope: must identify the authorized action")
    if document.get("status") == "COMPLETED" and any(_is_object(stage) and stage.get("status") not in {"COMPLETED", "SKIPPED"} for stage in stages):
        errors.append("run_state.status COMPLETED requires terminal stage states")
    if not isinstance(document.get("artifacts"), list):
        errors.append("run_state.artifacts: must be an array")
    keys = document.get("idempotency_keys")
    if not isinstance(keys, list) or any(not _nonempty_string(key) for key in keys) or len(set(keys)) != len(keys):
        errors.append("run_state.idempotency_keys: must be a unique string array")
    return errors


def _read_json_yaml(path: Path) -> Any:
    """Read the contract's JSON-compatible YAML subset without a YAML dependency."""
    return json.loads(path.read_text(encoding="utf-8"))


def validate_repo(repo_root: Path) -> dict[str, Any]:
    """Validate schemas, all workflow packages, and bilingual parity."""
    root = Path(repo_root).resolve()
    errors: list[str] = []
    workflow_files = 0
    package_sets: dict[str, dict[str, tuple[Path, Any]]] = {"zh": {}, "en": {}}
    available_skill_ids = {
        skill_file.parent.name
        for language in ("zh", "en")
        for skill_file in (root / "skills" / language).rglob("SKILL.md")
        if skill_file.is_file()
    }

    for schema_name in SCHEMAS:
        path = root / SCHEMA_ROOT / schema_name
        if not path.is_file():
            errors.append(f"missing schema: {SCHEMA_ROOT / schema_name}")
            continue
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"invalid schema JSON {path.relative_to(root)}: {exc}")
            continue
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema" or schema.get("type") != "object" or not schema.get("required"):
            errors.append(f"schema {path.relative_to(root)}: expected a Draft 2020-12 object schema with required fields")

    template_path = root / "resources" / "workflows" / "templates" / "workflow.template.json"
    if not template_path.is_file():
        errors.append(f"missing workflow template: {template_path.relative_to(root)}")
    else:
        try:
            template = json.loads(template_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"invalid workflow template JSON {template_path.relative_to(root)}: {exc}")
        else:
            for finding in validate_workflow(template):
                errors.append(f"{template_path.relative_to(root)}: {finding}")

    for language in ("zh", "en"):
        language_root = root / "skills" / language / "testing-workflows"
        if not language_root.is_dir():
            errors.append(f"missing workflow language root: skills/{language}/testing-workflows")
            continue
        for package in sorted(path for path in language_root.iterdir() if path.is_dir()):
            path = package / "workflow.yaml"
            if not path.is_file():
                errors.append(f"missing workflow.yaml: {path.relative_to(root)}")
                continue
            workflow_files += 1
            try:
                workflow = _read_json_yaml(path)
            except (json.JSONDecodeError, OSError) as exc:
                errors.append(f"invalid JSON-compatible YAML {path.relative_to(root)}: {exc}")
                continue
            for finding in validate_workflow(workflow, package, available_skill_ids):
                errors.append(f"{path.relative_to(root)}: {finding}")
            if workflow.get("id") != package.name:
                errors.append(f"{path.relative_to(root)}: id must match package directory {package.name!r}")
            package_sets[language][package.name] = (path, workflow)

    if package_sets["zh"].keys() != package_sets["en"].keys():
        missing_en = sorted(package_sets["zh"].keys() - package_sets["en"].keys())
        missing_zh = sorted(package_sets["en"].keys() - package_sets["zh"].keys())
        if missing_en:
            errors.append("workflow packages missing English mirror: " + ", ".join(missing_en))
        if missing_zh:
            errors.append("workflow packages missing Chinese mirror: " + ", ".join(missing_zh))
    for package_name in sorted(package_sets["zh"].keys() & package_sets["en"].keys()):
        zh_path, zh_workflow = package_sets["zh"][package_name]
        en_path, en_workflow = package_sets["en"][package_name]
        if zh_workflow != en_workflow:
            errors.append(f"bilingual contract mismatch for {package_name}: {zh_path.relative_to(root)} vs {en_path.relative_to(root)}")

    examples = root / "resources" / "workflows" / "examples"
    for name, validator in (("evidence.example.json", validate_evidence), ("run-state.example.json", validate_run_state)):
        path = examples / name
        if not path.is_file():
            errors.append(f"missing workflow example: {path.relative_to(root)}")
            continue
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"invalid workflow example {path.relative_to(root)}: {exc}")
            continue
        for finding in validator(document):
            errors.append(f"{path.relative_to(root)}: {finding}")

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "checked_workflow_files": workflow_files,
        "checked_workflow_packages": len(package_sets["zh"] | package_sets["en"]),
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--report", type=Path, help="Write a machine-readable JSON validation report")
    args = parser.parse_args(argv)
    report = validate_repo(args.repo_root)
    for error in report["errors"]:
        print(f"- {error}")
    print(
        "workflow_contracts: "
        f"status={report['status']} packages={report['checked_workflow_packages']} "
        f"workflow_files={report['checked_workflow_files']} errors={len(report['errors'])}"
    )
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
