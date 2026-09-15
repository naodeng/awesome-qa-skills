#!/usr/bin/env python3
"""Generate and validate the Phase 0 Skill governance matrix."""

from dataclasses import dataclass
import argparse
import json
import re
from pathlib import Path


VALID_STATUSES = {
    "Existing", "Enhance", "Merge", "Match", "Planned-P0", "Planned-P1",
    "Planned-P2", "Experimental", "Deprecated", "Archived", "Candidate",
}
VALID_CONCLUSIONS = {"EXISTING", "MATCH", "ENHANCE", "MERGE", "NEW"}
VALID_DECISION_STATES = {"PROPOSED", "REVIEWED_WITH_LIMITATION", "REVIEWED"}
VALID_SCORE_STATES = {"NOT_SCORED", "PARTIALLY_SCORED", "SCORED"}
MATCH_FIELDS = ("name", "purpose", "inputs", "outputs", "decision_logic", "workflow_role")
PROJECT_EVIDENCE_FIELDS = (
    "project_number", "item_id", "title", "current_status", "verified_at", "verification",
    "transition_requirement", "transition_audit",
)
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
    for key in (
        "slug", "zh_path", "en_path", "virtual_domain", "sdlc_stage", "roles",
        "priority", "inputs", "outputs", "related", "workflow", "governance_evidence", "evidence_paths",
    ):
        value = skill.get(key)
        if value is None or (isinstance(value, str) and not value.strip()) or value == []:
            errors.append(f"missing {key}")
    if skill.get("status") not in VALID_STATUSES:
        errors.append("invalid status")
    slug = str(skill.get("slug", "")).strip()
    for language in LANGUAGES:
        path_key = f"{language}_path"
        path = str(skill.get(path_key, "")).rstrip("/")
        if path and not path.endswith(f"/{slug}"):
            errors.append(f"{path_key} does not end in slug")
        if path and not path.startswith(f"skills/{language}/"):
            errors.append(f"{path_key} is not in skills/{language}")
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
    if candidate.get("decision_state") not in VALID_DECISION_STATES:
        errors.append("invalid decision_state")
    evidence = candidate.get("evidence", {})
    if not isinstance(evidence, dict):
        return [*errors, *MATCH_FIELDS]
    errors.extend(field for field in MATCH_FIELDS if not str(evidence.get(field, "")).strip())
    if candidate.get("conclusion") == "NEW":
        errors.extend(field for field in ("scope", "non_goals") if not str(candidate.get(field, "")).strip())
    if (
        candidate.get("decision_state") == "REVIEWED"
        and "2026-09-15-v2-test-engineering-two-batch-design.md" in str(candidate.get("candidate_source", ""))
    ):
        comparison = candidate.get("capability_match")
        if not isinstance(comparison, dict):
            errors.append("REVIEWED v2 candidate requires capability_match")
        else:
            if comparison.get("decision") not in VALID_CONCLUSIONS:
                errors.append("capability_match requires a valid decision")
            if not comparison.get("existing_targets"):
                errors.append("capability_match requires existing_targets")
            if not str(comparison.get("difference", "")).strip():
                errors.append("capability_match requires difference")
        project = candidate.get("project_evidence")
        if not isinstance(project, dict):
            errors.append("REVIEWED v2 candidate requires project_evidence")
        else:
            errors.extend(
                f"project_evidence requires {field}"
                for field in PROJECT_EVIDENCE_FIELDS
                if project.get(field) in (None, "", [])
            )
            if project.get("project_number") != 4:
                errors.append("project_evidence must reference Project #4")
            if project.get("current_status") != "Done":
                errors.append("project_evidence current_status must be Done")
    return errors


def validate_registry(registry: GovernanceRegistry, physical: set[str], root: Path | None = None) -> list[str]:
    rows = {str(skill.get("slug")): skill for skill in registry.skills}
    errors = [f"missing registry record for skill: {slug}" for slug in sorted(physical - set(rows))]
    errors.extend(f"registry record has no physical skill: {slug}" for slug in sorted(set(rows) - physical))
    for skill in registry.skills:
        errors.extend(f"{skill.get('slug')}: {error}" for error in validate_skill(skill))
        if root is not None:
            for path in skill.get("evidence_paths", []):
                if not (root / str(path)).exists():
                    errors.append(f"{skill.get('slug')}: missing evidence path: {path}")
            for language in LANGUAGES:
                path = root / str(skill.get(f"{language}_path", ""))
                if not path.is_dir():
                    errors.append(f"{skill.get('slug')}: missing {language} skill directory")
    for candidate in registry.candidates:
        errors.extend(f"{candidate.get('slug')}: {error}" for error in validate_candidate(candidate))
    return errors


def skill_description(root: Path, skill: dict[str, object], locale: str) -> str:
    evidence = str(skill.get("governance_evidence", ""))
    if locale == "en" and evidence.startswith("skills/zh/"):
        evidence = evidence.replace("skills/zh/", "skills/en/", 1)
    path = root / evidence
    if not path.is_file():
        return "UNASSESSED"
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('"').replace("|", "\\|") if match else "UNASSESSED"


def render_matrix(registry: GovernanceRegistry, locale: str, root: Path | None = None) -> str:
    root = root or Path(__file__).resolve().parents[1]
    english = locale == "en"
    switch = "中文" if english else "English"
    target = "SKILL_MATRIX.md" if english else "SKILL_MATRIX_EN.md"
    title = "Skill Governance Matrix" if english else "Skill 治理矩阵"
    intro = (
        "Generated from `docs/governance/skill-governance-registry.yaml`; structure and review states do not prove runtime effectiveness."
        if english else
        "由 `docs/governance/skill-governance-registry.yaml` 生成；结构和评审状态不证明运行效果。"
    )
    lines = [f'<div align="right"><a href="./{target}">{switch}</a></div>', "", f"# {title}", "", intro, "", "| Skill | Section | Virtual Domain | SDLC | Roles | Status | Priority | Scope evidence | Inputs | Outputs | Related / Workflow | Quality Score | Eval Execution | Evidence |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for skill in sorted(registry.skills, key=lambda item: str(item.get("slug", ""))):
        score = skill.get("quality_score", {}).get("state", "UNASSESSED")
        execution = skill.get("eval_execution", {}).get("state", "UNASSESSED")
        roles = ", ".join(skill.get("roles", [])) if isinstance(skill.get("roles"), list) else skill.get("roles", "UNASSESSED")
        related = skill.get("related", "UNASSESSED")
        workflow = skill.get("workflow", "UNASSESSED")
        scope = skill_description(root, skill, locale)
        evidence_paths = skill.get("evidence_paths", [skill.get("governance_evidence", "UNASSESSED")])
        evidence = "<br>".join(str(path) for path in evidence_paths)
        lines.append(f"| `{skill.get('slug', '')}` | {skill.get('section', 'UNASSESSED')} | {skill.get('virtual_domain', 'UNASSESSED')} | {skill.get('sdlc_stage', 'UNASSESSED')} | {roles} | {skill.get('status', 'UNASSESSED')} | {skill.get('priority', 'UNASSESSED')} | {scope} | {skill.get('inputs', 'UNASSESSED')} | {skill.get('outputs', 'UNASSESSED')} | {related} / {workflow} | `{score}` | `{execution}` | {evidence} |")
    return "\n".join(lines) + "\n"


def render_matching_register(registry: GovernanceRegistry, locale: str) -> str:
    english = locale == "en"
    switch = "中文" if english else "English"
    target = "SKILL_MATCHING_REGISTER.md" if english else "SKILL_MATCHING_REGISTER_EN.md"
    title = "Skill Capability Match Register" if english else "Skill 能力匹配决策登记表"
    lines = [f'<div align="right"><a href="./{target}">{switch}</a></div>', "", f"# {title}", "", "| Candidate | Decision state | Proposed conclusion | Target | Candidate source / target evidence | Evidence (six fields) | Next action |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for candidate in sorted(registry.candidates, key=lambda item: str(item.get("slug", ""))):
        evidence = candidate.get("evidence", {})
        evidence_text = "; ".join(f"{field}: {evidence.get(field, 'UNASSESSED')}" for field in MATCH_FIELDS)
        source = candidate.get("candidate_source", "UNASSESSED")
        targets = "<br>".join(str(path) for path in candidate.get("target_evidence_paths", []))
        comparison = candidate.get("capability_match")
        if isinstance(comparison, dict):
            comparison_targets = "<br>".join(str(path) for path in comparison.get("existing_targets", []))
            source = (
                f"{source}<br>Capability Match: decision={comparison.get('decision', 'UNASSESSED')}; "
                f"existing targets:<br>{comparison_targets}<br>difference: {comparison.get('difference', 'UNASSESSED')}"
            )
        project = candidate.get("project_evidence")
        if isinstance(project, dict):
            source = (
                f"{source}<br>Project #{project.get('project_number', 'UNASSESSED')} item "
                f"`{project.get('item_id', 'UNASSESSED')}` ({project.get('title', 'UNASSESSED')}) "
                f"current status=`{project.get('current_status', 'UNASSESSED')}`; "
                f"verified {project.get('verified_at', 'UNASSESSED')} via `{project.get('verification', 'UNASSESSED')}`; "
                f"required transition=`{project.get('transition_requirement', 'UNASSESSED')}`; "
                f"transition audit={project.get('transition_audit', 'UNASSESSED')}"
            )
        lines.append(f"| `{candidate.get('slug', '')}` | `{candidate.get('decision_state', 'UNASSESSED')}` | `{candidate.get('conclusion', 'UNASSESSED')}` | `{candidate.get('target', 'UNASSESSED')}` | {source}<br>{targets} | {evidence_text} | {candidate.get('next_action', 'UNASSESSED')} |")
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
        expected = (render_matrix(registry, locale, root), render_matching_register(registry, locale))
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
    errors = validate_registry(registry, discover_physical_skills(root), root)
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
