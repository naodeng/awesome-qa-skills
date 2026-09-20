#!/usr/bin/env python3
"""Compare two existing Skill evaluation reports without rerunning an Eval."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Mapping


COMPARABILITY_FIELDS = (
    "eval_version",
    "variant",
    "skill_up_version",
    "engine",
    "provider",
    "requested_model",
    "observed_model",
    "judge_type",
    "judge_model",
    "environment",
)
VALID_STATES = {"PASS", "FAIL", "BLOCKED", "NOT_RUN", "NOT_SCORED", "UNASSESSED", "INSUFFICIENT_EVIDENCE"}
VALID_FAILURE_CLASSIFICATIONS = {"SKILL_DEFECT", "EVAL_DEFECT", "INFRASTRUCTURE_DEFECT", "UNKNOWN"}


def _metadata(report: Mapping[str, Any], label: str) -> tuple[dict[str, Any], list[str]]:
    value = report.get("run_metadata")
    if not isinstance(value, dict):
        return {}, [f"{label} report is missing run_metadata"]
    return value, []


def _cases(report: Mapping[str, Any], label: str) -> tuple[dict[str, Mapping[str, Any]], list[str]]:
    raw_cases = report.get("cases")
    if raw_cases is None and report.get("case_id"):
        raw_cases = [report]
    if not isinstance(raw_cases, list):
        return {}, [f"{label} report is missing cases"]

    cases: dict[str, Mapping[str, Any]] = {}
    errors: list[str] = []
    for index, raw_case in enumerate(raw_cases, 1):
        if not isinstance(raw_case, Mapping):
            errors.append(f"{label} case {index} is not an object")
            continue
        case_id = str(raw_case.get("case_id", "")).strip()
        if not case_id:
            errors.append(f"{label} case {index} is missing case_id")
            continue
        if case_id in cases:
            errors.append(f"{label} contains duplicate case_id: {case_id}")
            continue
        cases[case_id] = raw_case
    return cases, errors


def _parse_timestamp(metadata: Mapping[str, Any], label: str, errors: list[str]) -> datetime | None:
    raw = str(metadata.get("timestamp", "")).strip()
    if not raw or raw.lower() == "unknown":
        errors.append(f"{label} timestamp is unavailable")
        return None
    try:
        timestamp = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{label} timestamp is invalid: {raw}")
        return None
    if timestamp.tzinfo is None:
        errors.append(f"{label} timestamp must include a timezone: {raw}")
        return None
    return timestamp


def _case_failure_classification(case: Mapping[str, Any], label: str, case_id: str, errors: list[str]) -> str:
    raw = case.get("failure_classification")
    if raw is None or not str(raw).strip():
        return "UNKNOWN"
    classification = str(raw).strip().upper()
    if classification not in VALID_FAILURE_CLASSIFICATIONS:
        errors.append(f"{label} case {case_id} has invalid failure_classification: {classification}")
        return "UNKNOWN"
    return classification


def compare_reports(previous: Mapping[str, Any], current: Mapping[str, Any]) -> dict[str, Any]:
    previous_metadata, previous_errors = _metadata(previous, "previous")
    current_metadata, current_errors = _metadata(current, "current")
    previous_cases, previous_case_errors = _cases(previous, "previous")
    current_cases, current_case_errors = _cases(current, "current")
    errors = previous_errors + current_errors + previous_case_errors + current_case_errors
    previous_timestamp = _parse_timestamp(previous_metadata, "previous", errors)
    current_timestamp = _parse_timestamp(current_metadata, "current", errors)
    if previous_timestamp and current_timestamp and current_timestamp < previous_timestamp:
        errors.append("current timestamp precedes previous timestamp")

    previous_skill = str(previous_metadata.get("skill_version", "")).strip()
    current_skill = str(current_metadata.get("skill_version", "")).strip()
    if not previous_skill or previous_skill == "unknown":
        errors.append("previous skill_version is unavailable")
    if not current_skill or current_skill == "unknown":
        errors.append("current skill_version is unavailable")
    if previous_skill and current_skill and previous_skill == current_skill:
        errors.append("previous and current skill_version are identical")

    for field in COMPARABILITY_FIELDS:
        previous_value = str(previous_metadata.get(field, "unknown")).strip() or "unknown"
        current_value = str(current_metadata.get(field, "unknown")).strip() or "unknown"
        if previous_value != current_value:
            errors.append(f"{field} differs: previous={previous_value}, current={current_value}")
        elif previous_value == "unknown":
            judge_type = str(previous_metadata.get("judge_type", "unknown")).strip()
            if field != "judge_model" or judge_type not in {"rule_based", "script"}:
                errors.append(f"{field} is unknown in both reports")

    previous_ids = set(previous_cases)
    current_ids = set(current_cases)
    for case_id in sorted(previous_ids - current_ids):
        errors.append(f"case missing from current report: {case_id}")
    for case_id in sorted(current_ids - previous_ids):
        errors.append(f"case missing from previous report: {case_id}")

    case_results: list[dict[str, Any]] = []
    regressions: list[dict[str, Any]] = []
    inconclusive: list[dict[str, Any]] = []
    for case_id in sorted(previous_ids & current_ids):
        previous_state = str(previous_cases[case_id].get("evidence_state", "INSUFFICIENT_EVIDENCE")).upper()
        current_state = str(current_cases[case_id].get("evidence_state", "INSUFFICIENT_EVIDENCE")).upper()
        if previous_state not in VALID_STATES:
            errors.append(f"previous case {case_id} has invalid evidence_state: {previous_state}")
        if current_state not in VALID_STATES:
            errors.append(f"current case {case_id} has invalid evidence_state: {current_state}")
        current_failure_classification = _case_failure_classification(
            current_cases[case_id], "current", case_id, errors
        )
        result = {
            "case_id": case_id,
            "previous_state": previous_state,
            "current_state": current_state,
            "current_failure_classification": current_failure_classification,
            "regressed": (
                previous_state == "PASS"
                and current_state == "FAIL"
                and current_failure_classification == "SKILL_DEFECT"
            ),
        }
        case_results.append(result)
        if result["regressed"]:
            regressions.append(result)
        elif previous_state == "PASS" and current_state != "PASS":
            inconclusive.append(result)

    comparable = not errors
    if not comparable:
        status = "INSUFFICIENT_EVIDENCE"
    elif regressions:
        status = "REGRESSION_OBSERVED"
    elif inconclusive:
        status = "INCONCLUSIVE"
    else:
        status = "NO_REGRESSION_OBSERVED"

    return {
        "comparison": "VERSION_REGRESSION",
        "comparable": comparable,
        "status": status,
        "previous_run_id": previous_metadata.get("run_id", "unknown"),
        "current_run_id": current_metadata.get("run_id", "unknown"),
        "comparison_window": {
            "previous_timestamp": previous_metadata.get("timestamp", "unknown"),
            "current_timestamp": current_metadata.get("timestamp", "unknown"),
            "elapsed_seconds": (
                (current_timestamp - previous_timestamp).total_seconds()
                if previous_timestamp and current_timestamp
                else None
            ),
        },
        "comparability_errors": errors,
        "cases": case_results,
        "regressions": regressions,
        "inconclusive": inconclusive,
    }


def _load_report(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"report must be a JSON object: {path}")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("previous", type=Path, help="previous evaluation report JSON")
    parser.add_argument("current", type=Path, help="current evaluation report JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = compare_reports(_load_report(args.previous), _load_report(args.current))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
