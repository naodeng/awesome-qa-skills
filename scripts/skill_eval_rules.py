"""Deterministic, local-only graders for Codex Skill eval traces.

The grader consumes a JSONL trace captured by ``codex exec --json`` and a small
JSON rule configuration. It never runs commands from the trace. Commands,
artifacts, and repository state are observed only after the run so the report
can distinguish a failed assertion from missing evidence.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import fnmatch
import hashlib
import json
import re
import shutil
from pathlib import Path
import subprocess
from typing import Any, Iterable


PASS = "PASS"
FAIL = "FAIL"
BLOCKED = "BLOCKED"
NOT_APPLICABLE = "N/A"
VALID_STATUSES = {PASS, FAIL, BLOCKED, NOT_APPLICABLE}
TRIGGER_MODES = frozenset({"explicit", "implicit", "contextual", "negative"})


@dataclass(frozen=True)
class RuleDefinition:
    rule_id: str
    category: str
    name: str
    description: str


RULES = (
    RuleDefinition("TRIGGER-001", "trigger", "explicit invocation", "An explicit skill request selects the expected Skill."),
    RuleDefinition("TRIGGER-002", "trigger", "implicit invocation", "A matching task description selects the expected Skill."),
    RuleDefinition("TRIGGER-003", "trigger", "contextual invocation", "A domain-context prompt still selects the expected Skill."),
    RuleDefinition("TRIGGER-004", "trigger", "negative control", "An adjacent task does not select the expected Skill."),
    RuleDefinition("TRACE-001", "trace", "trace audit", "The captured trace is non-empty and has no malformed JSONL lines."),
    RuleDefinition("TRACE-002", "trace", "JSONL contract", "Every captured line is a JSON object with an event type."),
    RuleDefinition("TRACE-003", "trace", "command lifecycle", "Command executions have both started and completed events."),
    RuleDefinition("PROCESS-001", "process", "required commands", "Every configured command appears in the trace."),
    RuleDefinition("PROCESS-002", "process", "command order", "Configured commands occur in the expected order."),
    RuleDefinition("PROCESS-003", "process", "command exit status", "Required commands complete successfully."),
    RuleDefinition("OUTCOME-001", "outcome", "definition of done", "Configured required artifacts exist and contain required markers."),
    RuleDefinition("OUTCOME-002", "outcome", "build check", "The configured build command completes successfully."),
    RuleDefinition("ARTIFACT-001", "artifact", "exact structure", "Expected and forbidden paths and content checks match the manifest."),
    RuleDefinition("ARTIFACT-002", "artifact", "persistence", "Configured artifact paths are persisted on disk."),
    RuleDefinition("ENV-001", "environment", "environment assumptions", "Captured working-directory and path assumptions hold."),
    RuleDefinition("ENV-002", "environment", "tool availability", "Configured local tools are available on PATH."),
    RuleDefinition("RUNTIME-001", "runtime", "runtime smoke", "The configured runtime smoke command completes successfully."),
    RuleDefinition("SAFETY-001", "safety", "cleanliness and efficiency", "Command count, repetition, token, and optional git cleanliness limits hold."),
    RuleDefinition("PERMISSION-001", "safety", "least privilege", "No configured forbidden command or unexpected permission escalation occurs."),
    RuleDefinition("REPRO-001", "reproducibility", "repeatability", "A comparison trace has the same normalized command behavior."),
)

RULE_IDS = tuple(rule.rule_id for rule in RULES)
RULE_ID_BY_NAME = {rule.name: rule.rule_id for rule in RULES}


@dataclass
class CommandRecord:
    command: str
    exit_code: int | None
    event_type: str
    event_index: int
    item_id: str | None = None
    cwd: str | None = None


@dataclass
class Trace:
    path: Path
    events: list[dict[str, Any]]
    errors: list[str] = field(default_factory=list)
    raw_line_count: int = 0

    @property
    def commands(self) -> list[CommandRecord]:
        return _command_records(self.events)

    @property
    def total_tokens(self) -> int:
        total = 0
        for event in self.events:
            usage = event.get("usage")
            if not isinstance(usage, dict):
                item = event.get("item")
                usage = item.get("usage") if isinstance(item, dict) else None
            if not isinstance(usage, dict):
                continue
            input_tokens = usage.get("input_tokens", 0)
            output_tokens = usage.get("output_tokens", 0)
            total_tokens = usage.get("total_tokens")
            if "input_tokens" in usage or "output_tokens" in usage:
                total += int(input_tokens or 0) + int(output_tokens or 0)
            elif isinstance(total_tokens, (int, float)):
                total += int(total_tokens)
        return total

    @property
    def selection_events(self) -> list[dict[str, Any]]:
        return _selection_events(self.events)

    @property
    def permission_escalations(self) -> list[dict[str, Any]]:
        return _permission_escalations(self.events)


@dataclass
class RuleResult:
    rule_id: str
    status: str
    message: str
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EvalReport:
    results: list[RuleResult]

    @property
    def has_failures(self) -> bool:
        return any(result.status == FAIL for result in self.results)

    @property
    def has_blocked(self) -> bool:
        return any(result.status == BLOCKED for result in self.results)

    @property
    def exit_code(self) -> int:
        if self.has_failures:
            return 1
        if self.has_blocked:
            return 2
        return 0

    def to_dict(self) -> dict[str, Any]:
        counts = {status: 0 for status in VALID_STATUSES}
        for result in self.results:
            counts[result.status] = counts.get(result.status, 0) + 1
        return {
            "exit_code": self.exit_code,
            "has_failures": self.has_failures,
            "has_blocked": self.has_blocked,
            "counts": counts,
            "results": [result.to_dict() for result in self.results],
        }


def validate_rule_catalog() -> list[str]:
    """Return catalog errors without reading or modifying the repository."""

    errors: list[str] = []
    if len(RULES) != 20:
        errors.append(f"expected 20 rules, found {len(RULES)}")
    if len(set(RULE_IDS)) != len(RULE_IDS):
        errors.append("rule IDs must be unique")
    if len({rule.name for rule in RULES}) != len(RULES):
        errors.append("rule names must be unique")
    for rule in RULES:
        if not re.fullmatch(r"[A-Z]+-\d{3}", rule.rule_id):
            errors.append(f"invalid rule ID: {rule.rule_id}")
        for field_name in ("category", "name", "description"):
            if not getattr(rule, field_name).strip():
                errors.append(f"{rule.rule_id} has empty {field_name}")
    return errors


def load_jsonl(path: Path) -> Trace:
    """Load JSONL without executing or interpreting commands from the trace."""

    events: list[dict[str, Any]] = []
    errors: list[str] = []
    raw_line_count = 0
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip():
            continue
        raw_line_count += 1
        try:
            value = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON ({exc.msg})")
            continue
        if not isinstance(value, dict):
            errors.append(f"line {line_number}: expected a JSON object")
            continue
        events.append(value)
    return Trace(path=path, events=events, errors=errors, raw_line_count=raw_line_count)


def evaluate_trace(trace: Trace, config: dict[str, Any], project_dir: Path) -> EvalReport:
    """Evaluate configured assertions and return explainable local evidence."""

    project_dir = project_dir.resolve()
    handler_factories = (
        lambda: _check_trigger(RULE_ID_BY_NAME["explicit invocation"], "explicit", trace, config),
        lambda: _check_trigger(RULE_ID_BY_NAME["implicit invocation"], "implicit", trace, config),
        lambda: _check_trigger(RULE_ID_BY_NAME["contextual invocation"], "contextual", trace, config),
        lambda: _check_trigger(RULE_ID_BY_NAME["negative control"], "negative", trace, config),
        lambda: _check_trace_audit(trace),
        lambda: _check_trace_contract(trace),
        lambda: _check_trace_lifecycle(trace, config),
        lambda: _check_required_commands(trace, config),
        lambda: _check_command_order(trace, config),
        lambda: _check_command_exit_status(trace, config),
        lambda: _check_required_artifacts(config, project_dir),
        lambda: _check_command_success(trace, config, "build_command", RULE_ID_BY_NAME["build check"]),
        lambda: _check_exact_artifacts(config, project_dir),
        lambda: _check_persisted_artifacts(config, project_dir),
        lambda: _check_environment(trace, config, project_dir),
        lambda: _check_tools(config),
        lambda: _check_command_success(trace, config, "smoke_command", RULE_ID_BY_NAME["runtime smoke"]),
        lambda: _check_safety(trace, config, project_dir),
        lambda: _check_permissions(trace, config),
        lambda: _check_reproducibility(trace, config, project_dir),
    )
    if len(handler_factories) != len(RULES):
        raise RuntimeError("rule handler count does not match the rule catalog")
    handlers = dict(zip(RULE_IDS, handler_factories))
    return EvalReport([handlers[rule.rule_id]() for rule in RULES])


def _result(rule_id: str, status: str, message: str, evidence: Iterable[str] = ()) -> RuleResult:
    if status not in VALID_STATUSES:
        raise ValueError(f"unknown rule status: {status}")
    return RuleResult(rule_id, status, message, list(evidence))


def _not_configured(rule_id: str, field_name: str) -> RuleResult:
    return _result(rule_id, NOT_APPLICABLE, f"not configured: {field_name}")


def _as_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1"}:
            return True
        if lowered in {"false", "no", "0"}:
            return False
    return None


def _normalize_command(command: str) -> str:
    return re.sub(r"\s+", " ", command.strip())


def _command_matches(expected: str, actual: str) -> bool:
    expected_normalized = _normalize_command(expected)
    actual_normalized = _normalize_command(actual)
    if not expected_normalized:
        return False
    return actual_normalized == expected_normalized or actual_normalized.startswith(f"{expected_normalized} ")


def _command_item(event: dict[str, Any]) -> dict[str, Any] | None:
    item = event.get("item")
    return item if isinstance(item, dict) else None


def _raw_command_events(events: list[dict[str, Any]]) -> list[tuple[str, dict[str, Any], int]]:
    raw: list[tuple[str, dict[str, Any], int]] = []
    for index, event in enumerate(events):
        event_type = str(event.get("type", ""))
        item = _command_item(event)
        if item is None or item.get("type") != "command_execution":
            continue
        command = item.get("command")
        if not isinstance(command, str) or not command.strip():
            continue
        raw.append((event_type, item, index))
    return raw


def _exit_code(item: dict[str, Any]) -> int | None:
    value = item.get("exit_code", item.get("exitCode"))
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _item_id(item: dict[str, Any]) -> str | None:
    for key in ("id", "command_id", "call_id"):
        value = item.get(key)
        if value is not None:
            return str(value)
    return None


def _command_records(events: list[dict[str, Any]]) -> list[CommandRecord]:
    records: list[CommandRecord] = []
    by_id: dict[str, int] = {}
    for event_type, item, event_index in _raw_command_events(events):
        command = str(item["command"])
        item_id = _item_id(item)
        record = CommandRecord(
            command=command,
            exit_code=_exit_code(item),
            event_type=event_type,
            event_index=event_index,
            item_id=item_id,
            cwd=item.get("cwd") if isinstance(item.get("cwd"), str) else None,
        )
        if item_id is not None and item_id in by_id:
            existing = records[by_id[item_id]]
            if record.exit_code is not None:
                existing.exit_code = record.exit_code
            if event_type.endswith("completed"):
                existing.event_type = event_type
                existing.event_index = event_index
            continue
        if item_id is None and event_type.endswith("completed"):
            previous = next(
                (
                    candidate
                    for candidate in reversed(records)
                    if candidate.item_id is None
                    and candidate.exit_code is None
                    and _command_matches(candidate.command, command)
                ),
                None,
            )
            if previous is not None:
                previous.exit_code = record.exit_code
                previous.event_type = event_type
                previous.event_index = event_index
                continue
        if item_id is not None:
            by_id[item_id] = len(records)
        records.append(record)
    return records


def _selection_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selections: list[dict[str, Any]] = []
    for event in events:
        if event.get("type") != "skill.selection":
            continue
        selected_value = event.get("selected", event.get("invoked", event.get("triggered")))
        selected = _as_bool(selected_value)
        selections.append(
            {
                "skill": event.get("skill", event.get("skill_name", event.get("name"))),
                "mode": event.get("mode", event.get("trigger_mode")),
                "selected": selected,
                "route": event.get("route"),
                "primary": event.get("primary"),
                "optional": event.get("optional"),
                "selected_skills": event.get("selected_skills"),
                "selection_fields": [
                    field
                    for field in ("route", "primary", "optional", "selected_skills")
                    if field in event
                ],
            }
        )
    return selections


def _permission_escalations(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    escalations: list[dict[str, Any]] = []
    for event in events:
        event_type = str(event.get("type", "")).lower()
        item = _command_item(event)
        source = item if item is not None and "permission" in str(item.get("type", "")).lower() else event
        if not any(token in event_type for token in ("permission", "approval", "escalat")):
            continue
        decision = source.get("granted", source.get("approved", source.get("allowed")))
        if decision is False or (isinstance(decision, str) and decision.strip().lower() in {"false", "no", "denied"}):
            continue
        escalations.append(source)
    return escalations


def _check_trigger(rule_id: str, mode: str, trace: Trace, config: dict[str, Any]) -> RuleResult:
    configured_mode = config.get("trigger_mode")
    if configured_mode is None:
        return _result(rule_id, BLOCKED, "trigger_mode is required to evaluate trigger evidence")
    if not isinstance(configured_mode, str) or configured_mode not in TRIGGER_MODES:
        return _result(rule_id, BLOCKED, "trigger_mode must be one of explicit, implicit, contextual, or negative")
    if configured_mode != mode:
        return _not_configured(rule_id, f"trigger_mode={mode}")
    skill = config.get("skill")
    expected = config.get("should_trigger", mode != "negative")
    expected_bool = _as_bool(expected)
    if expected_bool is None:
        return _result(rule_id, FAIL, "should_trigger must be boolean")
    candidates = [
        event
        for event in trace.selection_events
        if (skill is None or event.get("skill") == skill)
        and (event.get("mode") is None or event.get("mode") == mode)
    ]
    if not candidates:
        return _result(
            rule_id,
            BLOCKED,
            "no skill selection evidence; the trace adapter must emit a skill.selection event",
        )
    actual_value = candidates[-1]["selected"]
    if not isinstance(actual_value, bool):
        return _result(
            rule_id,
            BLOCKED,
            "skill selection evidence must include a boolean selected, invoked, or triggered field",
            [str(candidates[-1])],
        )
    actual = actual_value
    if actual != expected_bool:
        return _result(rule_id, FAIL, f"expected selected={expected_bool}, observed selected={actual}", [str(candidates[-1])])
    selection = candidates[-1]
    if "expected_selection" not in config:
        return _result(rule_id, PASS, f"observed selected={actual}", [str(selection)])

    expected_selection = config.get("expected_selection")
    required_fields = ("route", "primary", "optional")
    if not isinstance(expected_selection, dict) or any(
        field not in expected_selection for field in required_fields
    ):
        return _result(
            rule_id,
            BLOCKED,
            "structured selection evidence requires route, primary, and optional expectations",
            [str(selection)],
        )

    expected_route = expected_selection["route"]
    expected_primary = expected_selection["primary"]
    expected_optional = expected_selection["optional"]
    if (
        not isinstance(expected_route, str)
        or not isinstance(expected_primary, str)
        or (expected_optional is not None and not isinstance(expected_optional, str))
    ):
        return _result(
            rule_id,
            BLOCKED,
            "structured selection evidence has invalid expected route, primary, or optional values",
            [str(selection)],
        )

    missing_fields = [
        field for field in (*required_fields, "selected_skills") if field not in selection.get("selection_fields", [])
    ]
    if missing_fields:
        return _result(
            rule_id,
            BLOCKED,
            f"structured selection evidence is missing {', '.join(missing_fields)}",
            [str(selection)],
        )

    selected_skills = selection.get("selected_skills")
    if not isinstance(selected_skills, list) or not all(isinstance(skill_name, str) for skill_name in selected_skills):
        return _result(
            rule_id,
            BLOCKED,
            "structured selection evidence must provide selected_skills as a list of strings",
            [str(selection)],
        )

    expected_skills = [expected_primary]
    if expected_optional is not None:
        expected_skills.append(expected_optional)
    if selected_skills != expected_skills:
        return _result(
            rule_id,
            FAIL,
            f"selected_skills mismatch: expected {expected_skills}, observed {selected_skills}",
            [str(selection)],
        )

    observed_selection = {
        "route": selection.get("route"),
        "primary": selection.get("primary"),
        "optional": selection.get("optional"),
    }
    expected_values = {
        "route": expected_route,
        "primary": expected_primary,
        "optional": expected_optional,
    }
    if observed_selection != expected_values:
        return _result(
            rule_id,
            FAIL,
            f"expected selection={expected_values}, observed selection={observed_selection}",
            [str(selection)],
        )

    return _result(
        rule_id,
        PASS,
        f"route={expected_route}, primary={expected_primary}, optional={expected_optional}, selected_skills={selected_skills}",
        [str(selection)],
    )


def _check_trace_audit(trace: Trace) -> RuleResult:
    if not trace.events and not trace.errors:
        return _result("TRACE-001", FAIL, "trace contains no events")
    if trace.errors:
        return _result("TRACE-001", FAIL, "trace contains malformed lines", trace.errors)
    return _result("TRACE-001", PASS, f"parsed {len(trace.events)} JSONL events")


def _check_trace_contract(trace: Trace) -> RuleResult:
    if trace.errors:
        return _result("TRACE-002", FAIL, "stdout is not a pure JSONL object stream", trace.errors)
    missing_type = [str(index) for index, event in enumerate(trace.events, 1) if not isinstance(event.get("type"), str) or not event["type"].strip()]
    if missing_type:
        return _result("TRACE-002", FAIL, "events are missing a string type", [f"event {index}" for index in missing_type])
    if not trace.events:
        return _result("TRACE-002", FAIL, "stdout contains no JSON events")
    return _result("TRACE-002", PASS, "every event is a typed JSON object")


def _check_trace_lifecycle(trace: Trace, config: dict[str, Any]) -> RuleResult:
    if not config.get("require_command_lifecycle", False):
        return _not_configured("TRACE-003", "require_command_lifecycle")
    groups: dict[str, set[str]] = {}
    for event_type, item, _ in _raw_command_events(trace.events):
        key = _item_id(item) or _normalize_command(str(item["command"]))
        if event_type in {"item.started", "command_execution.started"}:
            lifecycle_state = "started"
        elif event_type in {"item.completed", "command_execution.completed"}:
            lifecycle_state = "completed"
        else:
            return _result(
                "TRACE-003",
                FAIL,
                "unknown command lifecycle event type",
                [event_type],
            )
        groups.setdefault(key, set()).add(lifecycle_state)
    if not groups:
        return _result("TRACE-003", FAIL, "lifecycle was required but no command_execution event exists")
    incomplete = [key for key, states in groups.items() if states != {"started", "completed"}]
    if incomplete:
        return _result("TRACE-003", FAIL, "command lifecycle is incomplete", incomplete)
    return _result("TRACE-003", PASS, f"verified lifecycle for {len(groups)} command execution(s)")


def _find_command(records: list[CommandRecord], expected: str) -> list[CommandRecord]:
    return [record for record in records if _command_matches(expected, record.command)]


def _check_required_commands(trace: Trace, config: dict[str, Any]) -> RuleResult:
    expected = config.get("required_commands")
    if not expected:
        return _not_configured("PROCESS-001", "required_commands")
    records = trace.commands
    missing = [command for command in expected if not _find_command(records, str(command))]
    if missing:
        return _result("PROCESS-001", FAIL, "required command(s) were not observed", missing)
    return _result("PROCESS-001", PASS, f"observed {len(expected)} required command(s)", [str(command) for command in expected])


def _check_command_order(trace: Trace, config: dict[str, Any]) -> RuleResult:
    expected = config.get("command_order")
    if not expected:
        return _not_configured("PROCESS-002", "command_order")
    records = trace.commands
    cursor = -1
    evidence: list[str] = []
    for command in expected:
        found = next((index for index, record in enumerate(records) if index > cursor and _command_matches(str(command), record.command)), None)
        if found is None:
            return _result("PROCESS-002", FAIL, "commands did not occur in the configured order", evidence + [str(command)])
        cursor = found
        evidence.append(f"{found + 1}: {records[found].command}")
    return _result("PROCESS-002", PASS, "commands occurred in the configured order", evidence)


def _check_command_exit_status(trace: Trace, config: dict[str, Any]) -> RuleResult:
    expected = config.get("required_commands")
    if not expected:
        return _not_configured("PROCESS-003", "required_commands")
    records = trace.commands
    blocked: list[str] = []
    failed: list[str] = []
    for command in expected:
        matches = _find_command(records, str(command))
        if not matches:
            failed.append(str(command))
            continue
        record = matches[-1]
        if record.exit_code is None:
            blocked.append(str(command))
        elif record.exit_code != 0:
            failed.append(f"{command} (exit={record.exit_code})")
    if failed:
        return _result("PROCESS-003", FAIL, "required command(s) failed", failed)
    if blocked:
        return _result("PROCESS-003", BLOCKED, "command completion did not include exit status", blocked)
    return _result("PROCESS-003", PASS, "all required commands exited with code 0")


def _safe_project_path(project_dir: Path, relative_path: str) -> Path | None:
    candidate = Path(relative_path)
    if candidate.is_absolute():
        return None
    resolved = (project_dir / candidate).resolve()
    try:
        resolved.relative_to(project_dir)
    except ValueError:
        return None
    return resolved


def _path_check(project_dir: Path, relative_path: str) -> tuple[Path | None, str | None]:
    target = _safe_project_path(project_dir, relative_path)
    if target is None:
        return None, f"unsafe path: {relative_path}"
    return target, None


def _read_marker(target: Path, marker: str) -> bool:
    if not target.is_file():
        return False
    try:
        return marker in target.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False


def _check_required_artifacts(config: dict[str, Any], project_dir: Path) -> RuleResult:
    required = config.get("required_artifacts")
    if not required:
        return _not_configured("OUTCOME-001", "required_artifacts")
    failures: list[str] = []
    for entry in required:
        if isinstance(entry, str):
            relative_path, marker = entry, None
        elif isinstance(entry, dict):
            relative_path, marker = entry.get("path"), entry.get("contains")
        else:
            failures.append(f"invalid artifact entry: {entry!r}")
            continue
        if not isinstance(relative_path, str):
            failures.append(f"invalid artifact path: {entry!r}")
            continue
        target, path_error = _path_check(project_dir, relative_path)
        if path_error:
            failures.append(path_error)
        elif target is None or not target.exists():
            failures.append(f"missing: {relative_path}")
        elif marker is not None and (not isinstance(marker, str) or not _read_marker(target, marker)):
            failures.append(f"marker missing: {relative_path}")
    if failures:
        return _result("OUTCOME-001", FAIL, "definition-of-done artifact check failed", failures)
    return _result("OUTCOME-001", PASS, f"verified {len(required)} required artifact(s)")


def _check_command_success(trace: Trace, config: dict[str, Any], field_name: str, rule_id: str) -> RuleResult:
    expected = config.get(field_name)
    if not expected:
        return _not_configured(rule_id, field_name)
    matches = _find_command(trace.commands, str(expected))
    if not matches:
        return _result(rule_id, FAIL, f"{field_name} was not observed", [str(expected)])
    record = matches[-1]
    if record.exit_code is None:
        return _result(rule_id, BLOCKED, f"{field_name} has no completed exit status")
    if record.exit_code != 0:
        return _result(rule_id, FAIL, f"{field_name} failed with exit code {record.exit_code}")
    return _result(rule_id, PASS, f"{field_name} completed successfully", [record.command])


def _check_exact_artifacts(config: dict[str, Any], project_dir: Path) -> RuleResult:
    expected = config.get("expected_files") or []
    forbidden = config.get("forbidden_files") or []
    content_checks = config.get("content_checks") or []
    if not expected and not forbidden and not content_checks:
        return _not_configured("ARTIFACT-001", "expected_files/content_checks/forbidden_files")
    failures: list[str] = []
    for relative_path in expected:
        target, path_error = _path_check(project_dir, str(relative_path))
        if path_error:
            failures.append(path_error)
        elif target is None or not target.is_file():
            failures.append(f"expected file missing: {relative_path}")
    for relative_path in forbidden:
        target, path_error = _path_check(project_dir, str(relative_path))
        if path_error:
            failures.append(path_error)
        elif target is not None and target.exists():
            failures.append(f"forbidden path exists: {relative_path}")
    for entry in content_checks:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str) or not isinstance(entry.get("contains"), str):
            failures.append(f"invalid content check: {entry!r}")
            continue
        target, path_error = _path_check(project_dir, entry["path"])
        if path_error:
            failures.append(path_error)
        elif target is None or not _read_marker(target, entry["contains"]):
            failures.append(f"content marker missing: {entry['path']}")
    if failures:
        return _result("ARTIFACT-001", FAIL, "exact artifact manifest check failed", failures)
    return _result("ARTIFACT-001", PASS, "artifact paths and content match the manifest")


def _check_persisted_artifacts(config: dict[str, Any], project_dir: Path) -> RuleResult:
    persisted = config.get("persisted_paths")
    if not persisted:
        return _not_configured("ARTIFACT-002", "persisted_paths")
    failures: list[str] = []
    for relative_path in persisted:
        target, path_error = _path_check(project_dir, str(relative_path))
        if path_error:
            failures.append(path_error)
        elif target is None or not target.exists():
            failures.append(f"not persisted: {relative_path}")
    if failures:
        return _result("ARTIFACT-002", FAIL, "persisted artifact check failed", failures)
    return _result("ARTIFACT-002", PASS, f"verified {len(persisted)} persisted path(s)")


def _environment_event(trace: Trace) -> dict[str, Any] | None:
    for event in trace.events:
        if event.get("type") == "eval.environment":
            return event
    return None


def _check_environment(trace: Trace, config: dict[str, Any], project_dir: Path) -> RuleResult:
    environment = config.get("environment")
    if not isinstance(environment, dict):
        return _not_configured("ENV-001", "environment")
    event = _environment_event(trace)
    failures: list[str] = []
    expected_cwd = environment.get("expected_cwd")
    if expected_cwd is not None:
        if event is None:
            return _result("ENV-001", BLOCKED, "expected_cwd requires an eval.environment event")
        observed_cwd = event.get("cwd")
        if observed_cwd != expected_cwd:
            failures.append(f"cwd expected {expected_cwd!r}, observed {observed_cwd!r}")
    if "initial_paths" in environment:
        if event is None:
            return _result("ENV-001", BLOCKED, "initial_paths requires an eval.environment event")
        observed = sorted(str(path) for path in event.get("paths", []))
        expected = sorted(str(path) for path in environment.get("initial_paths", []))
        if observed != expected:
            failures.append(f"initial paths expected {expected!r}, observed {observed!r}")
    for relative_path in environment.get("required_paths", []):
        target, path_error = _path_check(project_dir, str(relative_path))
        if path_error or target is None or not target.exists():
            failures.append(path_error or f"required environment path missing: {relative_path}")
    for relative_path in environment.get("forbidden_paths", []):
        target, path_error = _path_check(project_dir, str(relative_path))
        if path_error:
            failures.append(path_error)
        elif target is not None and target.exists():
            failures.append(f"forbidden environment path exists: {relative_path}")
    if failures:
        return _result("ENV-001", FAIL, "environment assumption check failed", failures)
    return _result("ENV-001", PASS, "configured environment assumptions hold")


def _check_tools(config: dict[str, Any]) -> RuleResult:
    required_tools = config.get("required_tools")
    if not required_tools:
        return _not_configured("ENV-002", "required_tools")
    missing = [str(tool) for tool in required_tools if shutil.which(str(tool)) is None]
    if missing:
        return _result("ENV-002", FAIL, "required local tool(s) are unavailable", missing)
    return _result("ENV-002", PASS, "all required tools are available", [str(tool) for tool in required_tools])


def _max_consecutive(commands: list[str]) -> int:
    maximum = 0
    previous = None
    current = 0
    for command in commands:
        normalized = _normalize_command(command)
        if normalized == previous:
            current += 1
        else:
            previous = normalized
            current = 1
        maximum = max(maximum, current)
    return maximum


def _git_changed_paths(project_dir: Path) -> list[str] | None:
    try:
        completed = subprocess.run(
            ["git", "-C", str(project_dir), "status", "--porcelain", "--untracked-files=all"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if completed.returncode != 0:
        return None
    paths: list[str] = []
    for line in completed.stdout.splitlines():
        if len(line) >= 4:
            paths.append(line[3:])
    return paths


def _is_allowed_path(path: str, allowed: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in allowed)


def _check_safety(trace: Trace, config: dict[str, Any], project_dir: Path) -> RuleResult:
    configured_fields = {"max_commands", "max_repeated_commands", "max_total_tokens", "clean_repo"}
    if not configured_fields.intersection(config):
        return _not_configured("SAFETY-001", "efficiency or clean_repo limits")
    failures: list[str] = []
    commands = trace.commands
    if "max_commands" in config and len(commands) > int(config["max_commands"]):
        failures.append(f"command count {len(commands)} > {config['max_commands']}")
    if "max_repeated_commands" in config:
        repeated = _max_consecutive([record.command for record in commands])
        if repeated > int(config["max_repeated_commands"]):
            failures.append(f"consecutive repetition {repeated} > {config['max_repeated_commands']}")
    if "max_total_tokens" in config and trace.total_tokens > int(config["max_total_tokens"]):
        failures.append(f"tokens {trace.total_tokens} > {config['max_total_tokens']}")
    if config.get("clean_repo"):
        changed = _git_changed_paths(project_dir)
        if changed is None:
            return _result("SAFETY-001", BLOCKED, "clean_repo requires a readable git worktree")
        allowed = [str(path) for path in config.get("allowed_changed_paths", [])]
        unexpected = [path for path in changed if not _is_allowed_path(path, allowed)]
        if unexpected:
            failures.append(f"unexpected git changes: {unexpected}")
    if failures:
        return _result("SAFETY-001", FAIL, "cleanliness or efficiency limit exceeded", failures)
    return _result("SAFETY-001", PASS, "configured cleanliness and efficiency limits hold")


def _check_permissions(trace: Trace, config: dict[str, Any]) -> RuleResult:
    permissions = config.get("permissions")
    forbidden = config.get("forbidden_commands")
    if not isinstance(permissions, dict) and not forbidden:
        return _not_configured("PERMISSION-001", "permissions/forbidden_commands")
    failures: list[str] = []
    if isinstance(permissions, dict):
        maximum = int(permissions.get("max_escalations", 0))
        observed = len(trace.permission_escalations)
        if observed > maximum:
            failures.append(f"permission escalations {observed} > {maximum}")
    if forbidden:
        for record in trace.commands:
            if any(_command_matches(str(pattern), record.command) for pattern in forbidden):
                failures.append(f"forbidden command: {record.command}")
    if failures:
        return _result("PERMISSION-001", FAIL, "least-privilege check failed", failures)
    return _result("PERMISSION-001", PASS, "no unexpected permission escalation or forbidden command observed")


def _file_digest(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError:
        return None
    return digest.hexdigest()


def _check_reproducibility(trace: Trace, config: dict[str, Any], project_dir: Path) -> RuleResult:
    comparison = config.get("compare_trace")
    if not comparison:
        return _not_configured("REPRO-001", "compare_trace")
    comparison_path = Path(str(comparison))
    if not comparison_path.is_file():
        return _result("REPRO-001", FAIL, "comparison trace does not exist", [str(comparison_path)])
    other = load_jsonl(comparison_path)
    if other.errors:
        return _result("REPRO-001", FAIL, "comparison trace is malformed", other.errors)
    current_behavior = [(_normalize_command(record.command), record.exit_code) for record in trace.commands]
    comparison_behavior = [(_normalize_command(record.command), record.exit_code) for record in other.commands]
    if any(exit_code is None for _, exit_code in current_behavior + comparison_behavior):
        return _result(
            "REPRO-001",
            BLOCKED,
            "both traces must include completed command exit statuses",
        )
    if current_behavior != comparison_behavior:
        return _result(
            "REPRO-001",
            FAIL,
            "normalized command behavior differs between runs",
            [f"current={current_behavior!r}", f"comparison={comparison_behavior!r}"],
        )
    current_paths = config.get("compare_paths") or []
    if current_paths:
        comparison_project = config.get("comparison_project_dir")
        if not comparison_project:
            return _result("REPRO-001", BLOCKED, "compare_paths requires comparison_project_dir")
        mismatches: list[str] = []
        for relative_path in current_paths:
            first = _safe_project_path(project_dir, str(relative_path))
            second = _safe_project_path(Path(str(comparison_project)).resolve(), str(relative_path))
            if first is None or second is None or _file_digest(first) != _file_digest(second):
                mismatches.append(str(relative_path))
        if mismatches:
            return _result("REPRO-001", FAIL, "comparison artifact digests differ", mismatches)
    return _result("REPRO-001", PASS, "normalized command and exit-code behavior is repeatable")
