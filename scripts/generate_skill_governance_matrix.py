#!/usr/bin/env python3
"""Generate and validate the Phase 0 Skill governance matrix."""

from dataclasses import dataclass
import argparse
import json
from pathlib import Path


VALID_STATUSES = {
    "Existing", "Enhance", "Merge", "Match", "Planned-P0", "Planned-P1",
    "Planned-P2", "Experimental", "Deprecated", "Archived", "Candidate",
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


def render_matrix(registry: GovernanceRegistry, locale: str) -> str:
    english = locale == "en"
    switch = "中文" if english else "English"
    target = "SKILL_MATRIX.md" if english else "SKILL_MATRIX_EN.md"
    title = "Skill Governance Matrix" if english else "Skill 治理矩阵"
    intro = (
        "Generated from `docs/governance/skill-governance-registry.yaml`; structure and review states do not prove runtime effectiveness."
        if english else
        "由 `docs/governance/skill-governance-registry.yaml` 生成；结构和评审状态不证明运行效果。"
    )
    lines = [f'<div align="right"><a href="./{target}">{switch}</a></div>', "", f"# {title}", "", intro, "", "| Skill | Section | Virtual Domain | Status | Priority | Quality Score | Eval Execution | Evidence |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for skill in sorted(registry.skills, key=lambda item: str(item.get("slug", ""))):
        score = skill.get("quality_score", {}).get("state", "UNASSESSED")
        execution = skill.get("eval_execution", {}).get("state", "UNASSESSED")
        lines.append(f"| `{skill.get('slug', '')}` | {skill.get('section', 'UNASSESSED')} | {skill.get('virtual_domain', 'UNASSESSED')} | {skill.get('status', 'UNASSESSED')} | {skill.get('priority', 'UNASSESSED')} | `{score}` | `{execution}` | `{skill.get('governance_evidence', 'UNASSESSED')}` |")
    return "\n".join(lines) + "\n"


def render_matching_register(registry: GovernanceRegistry, locale: str) -> str:
    english = locale == "en"
    switch = "中文" if english else "English"
    target = "SKILL_MATCHING_REGISTER.md" if english else "SKILL_MATCHING_REGISTER_EN.md"
    title = "Skill Capability Match Register" if english else "Skill 能力匹配决策登记表"
    lines = [f'<div align="right"><a href="./{target}">{switch}</a></div>', "", f"# {title}", "", "| Candidate | Decision state | Proposed conclusion | Target | Evidence (six fields) | Next action |", "| --- | --- | --- | --- | --- | --- |"]
    for candidate in sorted(registry.candidates, key=lambda item: str(item.get("slug", ""))):
        evidence = candidate.get("evidence", {})
        evidence_text = "; ".join(f"{field}: {evidence.get(field, 'UNASSESSED')}" for field in MATCH_FIELDS)
        lines.append(f"| `{candidate.get('slug', '')}` | `{candidate.get('decision_state', 'UNASSESSED')}` | `{candidate.get('conclusion', 'UNASSESSED')}` | `{candidate.get('target', 'UNASSESSED')}` | {evidence_text} | {candidate.get('next_action', 'UNASSESSED')} |")
    if not registry.candidates:
        lines.append("| _No candidate decisions recorded yet_ | `UNASSESSED` | — | — | Six-field evidence pending | Record evidence before implementation |")
    return "\n".join(lines) + "\n"


def output_paths(root: Path, locale: str) -> tuple[Path, Path]:
    suffix = "" if locale == "zh" else "_EN"
    return root / f"docs/SKILL_MATRIX{suffix}.md", root / f"docs/SKILL_MATCHING_REGISTER{suffix}.md"


def check_outputs(root: Path, registry: GovernanceRegistry) -> int:
    stale = []
    for locale in ("zh", "en"):
        matrix_path, register_path = output_paths(root, locale)
        expected = (render_matrix(registry, locale), render_matching_register(registry, locale))
        for path, content in zip((matrix_path, register_path), expected):
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path.relative_to(root)))
    if stale:
        print("stale_governance_views=" + ",".join(stale))
        return 1
    print("governance_views=up-to-date")
    return 0


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    registry = load_registry(root / "docs/governance/skill-governance-registry.yaml")
    errors = validate_registry(registry, discover_physical_skills(root))
    if errors:
        for error in errors:
            print(error)
        return 1
    if args.check:
        return check_outputs(root, registry)
    for locale in ("zh", "en"):
        matrix_path, register_path = output_paths(root, locale)
        matrix_path.write_text(render_matrix(registry, locale), encoding="utf-8")
        register_path.write_text(render_matching_register(registry, locale), encoding="utf-8")
        print(f"generated={matrix_path.relative_to(root)}")
        print(f"generated={register_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
