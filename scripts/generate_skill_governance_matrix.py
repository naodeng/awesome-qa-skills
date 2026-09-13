#!/usr/bin/env python3
"""Generate and validate the Phase 0 Skill governance matrix."""

from dataclasses import dataclass
import json
from pathlib import Path


VALID_STATUSES = {
    "Existing", "Enhance", "Merge", "Match", "Planned-P0", "Planned-P1",
    "Planned-P2", "Experimental", "Deprecated", "Archived",
}
VALID_CONCLUSIONS = {"EXISTING", "MATCH", "ENHANCE", "MERGE", "NEW"}
VALID_SCORE_STATES = {"NOT_SCORED", "PARTIALLY_SCORED", "SCORED"}
MATCH_FIELDS = ("name", "purpose", "inputs", "outputs", "decision_logic", "workflow_role")
SECTIONS = ("testing-types", "testing-workflows", "skill-engineering")
LANGUAGES = ("zh", "en")
SCORE_DIMENSIONS = (
    "problem_value", "scope_clarity", "input_quality", "analysis_depth",
    "output_actionability", "evidence_quality", "reusability", "eval_coverage",
    "documentation",
)


@dataclass(frozen=True)
class GovernanceRegistry:
    skills: tuple[dict[str, object], ...]
    candidates: tuple[dict[str, object], ...]


def discover_physical_skills(root: Path) -> set[str]:
    """Return logical slugs from the union of both language trees."""
    return {
        directory.name
        for language in LANGUAGES
        for section in SECTIONS
        for directory in (root / "skills" / language / section).iterdir()
        if directory.is_dir()
    }


def parse_registry(data: dict[str, object]) -> GovernanceRegistry:
    skills = data.get("skills", [])
    candidates = data.get("candidates", [])
    if not isinstance(skills, list) or not isinstance(candidates, list):
        raise ValueError("registry skills and candidates must be lists")
    return GovernanceRegistry(tuple(skills), tuple(candidates))


def load_registry(path: Path) -> GovernanceRegistry:
    """Load JSON-compatible YAML without adding a YAML parser dependency."""
    return parse_registry(json.loads(path.read_text(encoding="utf-8")))


def validate_skill(skill: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if skill.get("status") not in VALID_STATUSES:
        errors.append("invalid status")
    for key in ("slug", "zh_path", "en_path"):
        if not str(skill.get(key, "")).strip():
            errors.append(f"missing {key}")
    score = skill.get("quality_score", {})
    if not isinstance(score, dict) or score.get("state") not in VALID_SCORE_STATES:
        errors.append("invalid quality_score state")
    elif score["state"] == "SCORED":
        dimensions = score.get("dimensions", {})
        if not isinstance(dimensions, dict) or set(dimensions) != set(SCORE_DIMENSIONS):
            errors.append("SCORED requires nine dimensions")
        if not str(score.get("evidence", "")).strip():
            errors.append("SCORED requires evidence")
    return errors


def validate_candidate(candidate: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if candidate.get("conclusion") not in VALID_CONCLUSIONS:
        errors.append("invalid conclusion")
    evidence = candidate.get("evidence", {})
    if not isinstance(evidence, dict):
        return [*errors, *MATCH_FIELDS]
    errors.extend(field for field in MATCH_FIELDS if not str(evidence.get(field, "")).strip())
    if candidate.get("conclusion") == "NEW":
        errors.extend(field for field in ("scope", "non_goals") if not str(candidate.get(field, "")).strip())
    return errors


def validate_registry(registry: GovernanceRegistry, physical: set[str]) -> list[str]:
    rows = {str(skill.get("slug")): skill for skill in registry.skills}
    errors = [f"missing registry record for skill: {slug}" for slug in sorted(physical - set(rows))]
    errors.extend(f"registry record has no physical skill: {slug}" for slug in sorted(set(rows) - physical))
    for skill in registry.skills:
        errors.extend(f"{skill.get('slug')}: {error}" for error in validate_skill(skill))
    for candidate in registry.candidates:
        errors.extend(f"{candidate.get('slug')}: {error}" for error in validate_candidate(candidate))
    return errors


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
