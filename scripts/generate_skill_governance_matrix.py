#!/usr/bin/env python3
"""Generate and validate the Phase 0 Skill governance matrix."""

from dataclasses import dataclass
import argparse
import json
import re
from pathlib import Path

try:
    from .virtual_domains import catalog_skill_headings, load_required_catalog
except ImportError:  # pragma: no cover - direct script execution
    from virtual_domains import catalog_skill_headings, load_required_catalog


VALID_STATUSES = {
    "Existing", "Enhance", "Merge", "Match", "Planned-P0", "Planned-P1",
    "Planned-P2", "Experimental", "Deprecated", "Archived", "Candidate",
}
VALID_CONCLUSIONS = {"EXISTING", "MATCH", "ENHANCE", "MERGE", "NEW"}
VALID_DECISION_STATES = {"PROPOSED", "REVIEWED_WITH_LIMITATION", "REVIEWED"}
VALID_MATCH_REVIEW_CONCLUSIONS = {"EXISTING", "MATCH", "ENHANCE", "MERGE"}
VALID_MATCH_REVIEW_STATES = {"REVIEWED_WITH_LIMITATION"}
VALID_SCORE_STATES = {"NOT_SCORED", "PARTIALLY_SCORED", "SCORED"}
VALID_PROJECT_ACCEPTANCE_STATES = {"COMPLETE", "INCOMPLETE", "BLOCKED"}
MATCH_FIELDS = ("name", "purpose", "inputs", "outputs", "decision_logic", "workflow_role")
MATCH_REVIEW_FIELDS = ("candidate", "conclusion", "review_state", "target_skills", "evidence_paths", "next_action")
REQUIRED_MATCH_REVIEWS = {
    "requirement-change-impact-analysis": ("MATCH", ("change-impact-analysis",)),
    "test-impact-analysis": ("MERGE", ("change-impact-analysis", "pr-test-impact-analysis")),
    "code-change-risk-analysis": ("MERGE", ("pr-test-impact-analysis",)),
    "workload-modeling": ("MATCH", ("performance-workload-modeling",)),
    "capacity-planning": ("MATCH", ("capacity-planning-analysis",)),
    "performance-bottleneck-analysis": ("EXISTING", ("performance-bottleneck-analysis",)),
    "performance-result-analysis": ("EXISTING", ("performance-result-analysis",)),
    "performance-regression-analysis": ("EXISTING", ("performance-regression-analysis",)),
    "flaky-test-analysis": ("EXISTING", ("flaky-test-analysis",)),
    "production-verification": ("EXISTING", ("production-verification",)),
    "regression-scope-selection": ("MERGE", ("regression-scope-analysis", "regression-test-selection")),
    "ai-test-case-review": ("MATCH", ("ai-generated-test-review",)),
    "ai-log-analysis": ("ENHANCE", ("log-analysis",)),
    "ai-root-cause-analysis": ("ENHANCE", ("root-cause-analysis",)),
    "quality-risk-identification": ("MATCH", ("quality-risk-analysis",)),
    "ai-test-data-generation": ("ENHANCE", ("test-data-generation",)),
    "llm-output-quality-testing": ("ENHANCE", ("llm-testing",)),
    "llm-evaluation": ("MATCH", ("llm-evaluation-design",)),
    "prompt-testing": ("EXISTING", ("prompt-testing",)),
    "agent-tool-testing": ("EXISTING", ("agent-tool-testing",)),
}
REQUIRED_MATCH_REVIEW_CANDIDATES = tuple(REQUIRED_MATCH_REVIEWS)
PROJECT_EVIDENCE_FIELDS = (
    "project_number", "item_id", "title", "current_status", "verified_at", "verification",
    "transition_requirement", "transition_audit", "acceptance_state",
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
    match_reviews: tuple[dict[str, object], ...]
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
    match_reviews = data.get("match_reviews", [])
    candidates = data.get("candidates", [])
    if not isinstance(skills, list) or not isinstance(match_reviews, list) or not isinstance(candidates, list):
        raise ValueError("registry skills, match_reviews, and candidates must be lists")
    return GovernanceRegistry(tuple(skills), tuple(match_reviews), tuple(candidates))


def load_registry(path: Path) -> GovernanceRegistry:
    """Load JSON-compatible YAML without adding a YAML parser dependency."""
    return parse_registry(json.loads(path.read_text(encoding="utf-8")))


def validate_skill(skill: dict[str, object], domain_ids: set[str] | None = None) -> list[str]:
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
    if domain_ids is not None:
        virtual_domain = str(skill.get("virtual_domain", "")).strip()
        if virtual_domain and not virtual_domain.startswith("UNASSESSED") and virtual_domain not in domain_ids:
            errors.append("invalid virtual_domain")
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
            if project.get("acceptance_state") not in VALID_PROJECT_ACCEPTANCE_STATES:
                errors.append("project_evidence acceptance_state must be COMPLETE, INCOMPLETE, or BLOCKED")
            transition_audit = str(project.get("transition_audit", ""))
            if "UNASSESSED" in transition_audit and project.get("acceptance_state") == "COMPLETE":
                errors.append("project_evidence cannot be COMPLETE while transition history is UNASSESSED")
            if "UNASSESSED" in transition_audit and project.get("acceptance_state") not in {"INCOMPLETE", "BLOCKED"}:
                errors.append("project_evidence requires an incomplete or blocked acceptance state while transition history is UNASSESSED")
    return errors


def validate_match_review(
    review: dict[str, object],
    physical: set[str],
    candidates: dict[str, dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    for field in MATCH_REVIEW_FIELDS:
        value = review.get(field)
        if value is None or (isinstance(value, str) and not value.strip()) or value == []:
            errors.append(f"missing {field}")
    candidate = str(review.get("candidate", "")).strip()
    conclusion = review.get("conclusion")
    if conclusion not in VALID_MATCH_REVIEW_CONCLUSIONS:
        errors.append("invalid match review conclusion")
    if review.get("review_state") not in VALID_MATCH_REVIEW_STATES:
        errors.append("invalid match review state")
    targets = review.get("target_skills", [])
    if not isinstance(targets, list) or not targets:
        errors.append("target_skills must be a non-empty list")
        targets = []
    target_names = [str(target).strip() for target in targets]
    if len(target_names) != len(set(target_names)):
        errors.append("target_skills must not contain duplicates")
    errors.extend(f"unknown target Skill: {target}" for target in target_names if target not in physical)
    evidence_paths = review.get("evidence_paths", [])
    if not isinstance(evidence_paths, list) or not evidence_paths:
        errors.append("evidence_paths must be a non-empty list")
    if candidate in candidates:
        source = candidates[candidate]
        if source.get("conclusion") != conclusion:
            errors.append("match review conclusion differs from candidate record")
        source_targets = tuple(part.strip() for part in str(source.get("target", "")).split(",") if part.strip())
        if tuple(target_names) != source_targets:
            errors.append("match review targets differ from candidate record")
    elif candidate:
        if candidate not in physical:
            errors.append("non-candidate match review must reference a physical Skill")
        if conclusion != "EXISTING":
            errors.append("non-candidate match review must use EXISTING")
        if tuple(target_names) != (candidate,):
            errors.append("EXISTING self review must target the candidate Skill")
    return errors


def validate_repository_relative_files(root: Path, paths: object, field: str) -> list[str]:
    """Validate evidence entries as safe, repository-relative files."""
    if not isinstance(paths, list):
        return []
    errors: list[str] = []
    repository_root = root.resolve()
    for raw_path in paths:
        if not isinstance(raw_path, str) or not raw_path.strip():
            errors.append(f"{field} must contain non-empty repository-relative file paths")
            continue
        path = Path(raw_path)
        if path.is_absolute() or ".." in path.parts:
            errors.append(f"{field} must contain repository-relative file paths: {raw_path}")
            continue
        try:
            (root / path).resolve().relative_to(repository_root)
        except (OSError, ValueError):
            errors.append(f"{field} must stay within repository: {raw_path}")
        else:
            if not (root / path).is_file():
                errors.append(f"{field} must reference files: {raw_path}")
    return errors


def match_reviews_by_target(registry: GovernanceRegistry) -> dict[str, tuple[dict[str, object], ...]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for review in registry.match_reviews:
        for target in review.get("target_skills", []):
            grouped.setdefault(str(target), []).append(review)
    return {target: tuple(reviews) for target, reviews in grouped.items()}


def validate_registry(registry: GovernanceRegistry, physical: set[str], root: Path | None = None) -> list[str]:
    rows = {str(skill.get("slug")): skill for skill in registry.skills}
    candidate_rows = {str(candidate.get("slug")): candidate for candidate in registry.candidates}
    errors = [f"missing registry record for skill: {slug}" for slug in sorted(physical - set(rows))]
    errors.extend(f"registry record has no physical skill: {slug}" for slug in sorted(set(rows) - physical))
    domain_catalog = None
    catalog_headings: dict[str, str | None] = {}
    if root is not None:
        domain_path = root / "docs/governance/virtual-domains.yaml"
        catalog_path = root / "docs/catalog/skills-index.md"
        try:
            domain_catalog = load_required_catalog(root)
        except (OSError, ValueError) as error:
            errors.append(f"virtual-domain catalog error: {error}")
        if catalog_path.is_file() and domain_catalog is not None:
            catalog_headings = catalog_skill_headings(catalog_path)
        elif not catalog_path.is_file():
            errors.append(f"missing catalog index: {catalog_path.relative_to(root)}")
    for skill in registry.skills:
        errors.extend(
            f"{skill.get('slug')}: {error}"
            for error in validate_skill(skill, set(domain_catalog.domain_ids()) if domain_catalog else None)
        )
        if domain_catalog is not None:
            slug = str(skill.get("slug", ""))
            section = str(skill.get("section", ""))
            try:
                expected_domain = domain_catalog.classify(section, slug, catalog_headings.get(slug))
            except ValueError as error:
                errors.append(f"{slug}: {error}")
            else:
                actual_domain = str(skill.get("virtual_domain", ""))
                if actual_domain != expected_domain:
                    errors.append(
                        f"{slug}: virtual_domain is {actual_domain!r}; expected {expected_domain!r}"
                    )
        if root is not None:
            for path in skill.get("evidence_paths", []):
                if not (root / str(path)).exists():
                    errors.append(f"{skill.get('slug')}: missing evidence path: {path}")
            for language in LANGUAGES:
                path = root / str(skill.get(f"{language}_path", ""))
                if not path.is_dir():
                    errors.append(f"{skill.get('slug')}: missing {language} skill directory")
    seen_match_review_candidates: set[str] = set()
    for review in registry.match_reviews:
        candidate = str(review.get("candidate", ""))
        if candidate in seen_match_review_candidates:
            errors.append(f"duplicate match review: {candidate}")
        seen_match_review_candidates.add(candidate)
        errors.extend(
            f"{candidate}: {error}"
            for error in validate_match_review(review, physical, candidate_rows)
        )
        if root is not None:
            errors.extend(
                f"{candidate}: {error}"
                for error in validate_repository_relative_files(root, review.get("evidence_paths"), "evidence_paths")
            )
    if root is not None:
        actual_match_reviews = {
            str(review.get("candidate")): (
                str(review.get("conclusion")),
                tuple(str(target) for target in review.get("target_skills", [])),
            )
            for review in registry.match_reviews
        }
        if len(registry.match_reviews) != len(REQUIRED_MATCH_REVIEWS) or actual_match_reviews != REQUIRED_MATCH_REVIEWS:
            errors.append("match_reviews must contain the exact 20-row contract")
    for candidate in registry.candidates:
        errors.extend(f"{candidate.get('slug')}: {error}" for error in validate_candidate(candidate))
    if domain_catalog is not None:
        used_domains = {
            str(skill.get("virtual_domain"))
            for skill in registry.skills
            if str(skill.get("virtual_domain", "")).strip()
            and not str(skill.get("virtual_domain", "")).startswith("UNASSESSED")
        }
        missing_domains = sorted(set(domain_catalog.domain_ids()) - used_domains)
        if missing_domains:
            errors.append("registry does not use Virtual Domain IDs: " + ", ".join(missing_domains))
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


def review_action(conclusion: str, locale: str) -> str:
    actions = {
        "zh": {
            "EXISTING": "保留现有双语包；不创建重复目录；仅在有新的项目证据时复核。",
            "MATCH": "保留目标 Skill；不创建重复目录；后续变更前用项目证据复核语义等价。",
            "ENHANCE": "为目标 Skill 保留增强复核；范围、证据和 Eval 变更获批前不改动现有包。",
            "MERGE": "保留目标 Skill 包；项目上下文复核后再评估 mode、规则或子流程；不创建重复目录。",
        },
        "en": {
            "EXISTING": "Retain the existing bilingual package; create no duplicate directory; revisit only with new project evidence.",
            "MATCH": "Retain the target Skill; create no duplicate directory; reconfirm semantic equivalence with project evidence before future changes.",
            "ENHANCE": "Keep an enhancement review for the target Skill; do not change the current package until scope, evidence, and Eval changes are approved.",
            "MERGE": "Retain the target Skill packages; evaluate a mode, rule, or subflow after project-context review; create no duplicate directory.",
        },
    }
    return actions.get(locale, actions["en"]).get(conclusion, "UNASSESSED")


def render_review_relationship(review: dict[str, object], locale: str) -> str:
    candidate = str(review.get("candidate", "UNASSESSED"))
    targets = ", ".join(f"`{target}`" for target in review.get("target_skills", []))
    conclusion = str(review.get("conclusion", "UNASSESSED"))
    if locale == "zh":
        return f"{conclusion} 复核：`{candidate}` → {targets}；{review_action(conclusion, locale)}"
    return f"{conclusion} review: `{candidate}` -> {targets}; {review_action(conclusion, locale)}"


def render_matrix(registry: GovernanceRegistry, locale: str, root: Path | None = None) -> str:
    root = root or Path(__file__).resolve().parents[1]
    domain_catalog = load_required_catalog(root)
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
    reviews_by_target = match_reviews_by_target(registry)
    for skill in sorted(registry.skills, key=lambda item: str(item.get("slug", ""))):
        score = skill.get("quality_score", {}).get("state", "UNASSESSED")
        execution = skill.get("eval_execution", {}).get("state", "UNASSESSED")
        roles = ", ".join(skill.get("roles", [])) if isinstance(skill.get("roles"), list) else skill.get("roles", "UNASSESSED")
        related = skill.get("related", "UNASSESSED")
        if reviews := reviews_by_target.get(str(skill.get("slug", ""))):
            related = "<br>".join(render_review_relationship(review, locale) for review in reviews)
        workflow = skill.get("workflow", "UNASSESSED")
        scope = skill_description(root, skill, locale)
        evidence_paths = skill.get("evidence_paths", [skill.get("governance_evidence", "UNASSESSED")])
        evidence = "<br>".join(str(path) for path in evidence_paths)
        virtual_domain = str(skill.get("virtual_domain", "UNASSESSED"))
        domain_label = (
            domain_catalog.label(virtual_domain, locale)
            if domain_catalog is not None and virtual_domain in domain_catalog.domain_ids()
            else virtual_domain
        )
        lines.append(f"| `{skill.get('slug', '')}` | {skill.get('section', 'UNASSESSED')} | {domain_label} | {skill.get('sdlc_stage', 'UNASSESSED')} | {roles} | {skill.get('status', 'UNASSESSED')} | {skill.get('priority', 'UNASSESSED')} | {scope} | {skill.get('inputs', 'UNASSESSED')} | {skill.get('outputs', 'UNASSESSED')} | {related} / {workflow} | `{score}` | `{execution}` | {evidence} |")
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
                f"transition audit={project.get('transition_audit', 'UNASSESSED')}; "
                f"acceptance state=`{project.get('acceptance_state', 'UNASSESSED')}`"
            )
        lines.append(f"| `{candidate.get('slug', '')}` | `{candidate.get('decision_state', 'UNASSESSED')}` | `{candidate.get('conclusion', 'UNASSESSED')}` | `{candidate.get('target', 'UNASSESSED')}` | {source}<br>{targets} | {evidence_text} | {candidate.get('next_action', 'UNASSESSED')} |")
    if not registry.candidates:
        lines.append("| _No candidate decisions recorded yet_ | `UNASSESSED` | — | — | Six-field evidence pending | Record evidence before implementation |")
    return "\n".join(lines) + "\n"


def render_match_review(registry: GovernanceRegistry, locale: str) -> str:
    english = locale == "en"
    switch = "中文" if english else "English"
    target = "PHASE_0_MATCH_MERGE_REVIEW.md" if english else "PHASE_0_MATCH_MERGE_REVIEW_EN.md"
    title = "Phase 0 Typical Match / Merge Review" if english else "Phase 0 典型 Match / Merge 映射复核"
    intro = (
        "Generated from `docs/governance/skill-governance-registry.yaml`; this is a bounded source review, not semantic, runtime, model, or release evidence."
        if english else
        "由 `docs/governance/skill-governance-registry.yaml` 生成；这是有边界的来源复核，不是语义、运行时、模型或发布证据。"
    )
    reviews = sorted(registry.match_reviews, key=lambda item: str(item.get("candidate", "")))
    counts: dict[str, int] = {}
    for review in reviews:
        conclusion = str(review.get("conclusion", "UNASSESSED"))
        counts[conclusion] = counts.get(conclusion, 0) + 1
    if english:
        summary = (
            f"The review covers {len(reviews)} mappings: {counts.get('EXISTING', 0)} EXISTING, "
            f"{counts.get('MATCH', 0)} MATCH, {counts.get('ENHANCE', 0)} ENHANCE, and {counts.get('MERGE', 0)} MERGE."
        )
        scope = (
            "The 13 candidate mappings are cross-referenced to the generated Matching Register for six-field evidence. "
            "The 7 Existing self-reviews point to current bilingual package evidence."
        )
        boundaries = (
            "All rows remain `REVIEWED_WITH_LIMITATION`: the review records names, scope, inputs, outputs, decision logic, and Workflow role where candidate evidence exists, "
            "but does not authorize directory creation, modification, deletion, semantic-equivalence claims, runtime execution, model evaluation, or release approval."
        )
        evidence_label = "Matching Register / Matrix evidence"
        action_label = "Next action"
        candidate_label = "Candidate"
        conclusion_label = "Conclusion"
        state_label = "Review state"
        target_label = "Target Skills"
        paths_label = "Evidence paths"
        source_note = (
            "The Registry is authoritative; the [Matrix](../SKILL_MATRIX_EN.md), [Matching Register](../SKILL_MATCHING_REGISTER_EN.md), and this review are generated views. "
            "A physical Skill directory is not created by MATCH, MERGE, ENHANCE, or EXISTING alone."
        )
        follow_up = (
            "Next Phase 0 cards remain separate: Deprecation rules, bilingual consistency, and Quality Score/minimum Eval."
        )
    else:
        summary = (
            f"本次复核覆盖 {len(reviews)} 条映射：EXISTING {counts.get('EXISTING', 0)} 条、MATCH {counts.get('MATCH', 0)} 条、"
            f"ENHANCE {counts.get('ENHANCE', 0)} 条、MERGE {counts.get('MERGE', 0)} 条。"
        )
        scope = (
            "13 条候选映射关联生成的 Matching Register，复用六项证据；7 条 Existing 自映射指向当前双语 Skill 包证据。"
        )
        boundaries = (
            "所有行均保持 `REVIEWED_WITH_LIMITATION`：候选项有证据时记录名称、目的、输入、输出、决策逻辑和 Workflow 角色，"
            "但不授权创建、修改或删除目录，不证明语义等价、运行效果、模型评测或发布批准。"
        )
        evidence_label = "Matching Register / Matrix 证据"
        action_label = "后续动作"
        candidate_label = "Candidate"
        conclusion_label = "Conclusion"
        state_label = "Review state"
        target_label = "Target Skills"
        paths_label = "Evidence paths"
        source_note = (
            "Registry 是唯一事实源；[Matrix](../SKILL_MATRIX.md)、[Matching Register](../SKILL_MATCHING_REGISTER.md) 和本文均为生成视图。"
            "单独的 MATCH、MERGE、ENHANCE 或 EXISTING 结论不会创建物理 Skill 目录。"
        )
        follow_up = "后续 Phase 0 卡片保持独立：Deprecation 规则、中英文一致性、Quality Score 与最低 Eval。"
    lines = [
        f'<div align="right"><a href="./{target}">{switch}</a></div>',
        "",
        f"# {title}",
        "",
        intro,
        "",
        "## Scope" if english else "## 范围",
        "",
        summary,
        scope,
        "",
        "## Decision boundary" if english else "## 决策边界",
        "",
        boundaries,
        source_note,
        "",
        f"| {candidate_label} | {conclusion_label} | {state_label} | {target_label} | {paths_label} | {action_label} |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    candidate_slugs = {str(candidate.get("slug")) for candidate in registry.candidates}
    for review in reviews:
        candidate = str(review.get("candidate", ""))
        targets = "<br>".join(f"`{target}`" for target in review.get("target_skills", []))
        evidence = "<br>".join(str(path) for path in review.get("evidence_paths", []))
        if candidate in candidate_slugs:
            register = "../SKILL_MATCHING_REGISTER_EN.md" if english else "../SKILL_MATCHING_REGISTER.md"
            evidence = f"[Generated candidate evidence]({register})<br>{evidence}"
        else:
            matrix = "../SKILL_MATRIX_EN.md" if english else "../SKILL_MATRIX.md"
            evidence = f"[Target package evidence]({matrix})<br>{evidence}"
        lines.append(
            f"| `{candidate}` | `{review.get('conclusion', 'UNASSESSED')}` | "
            f"`{review.get('review_state', 'UNASSESSED')}` | {targets} | {evidence} | "
            f"{review_action(str(review.get('conclusion', 'UNASSESSED')), locale)} |"
        )
    if not reviews:
        lines.append("| _No focused mappings recorded_ | `UNASSESSED` | `UNASSESSED` | — | Record evidence before review | Record evidence before implementation |")
    lines.extend([
        "",
        "## Reproduction" if english else "## 复现",
        "",
        "- `python3 scripts/generate_skill_governance_matrix.py`",
        "- `python3 scripts/generate_skill_governance_matrix.py --check`",
        "- `python3 scripts/check_docs_bilingual.py --repo-root .`",
        "",
        follow_up,
    ])
    return "\n".join(lines) + "\n"


def output_paths(root: Path, locale: str) -> tuple[Path, Path]:
    suffix = "" if locale == "zh" else "_EN"
    return root / f"docs/SKILL_MATRIX{suffix}.md", root / f"docs/SKILL_MATCHING_REGISTER{suffix}.md"


def review_output_path(root: Path, locale: str) -> Path:
    suffix = "" if locale == "zh" else "_EN"
    return root / f"docs/governance/PHASE_0_MATCH_MERGE_REVIEW{suffix}.md"


def check_outputs(root: Path, registry: GovernanceRegistry) -> int:
    stale = []
    for locale in ("zh", "en"):
        matrix_path, register_path = output_paths(root, locale)
        review_path = review_output_path(root, locale)
        expected = (
            render_matrix(registry, locale, root),
            render_matching_register(registry, locale),
            render_match_review(registry, locale),
        )
        for path, content in zip((matrix_path, register_path, review_path), expected):
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
        review_path = review_output_path(root, locale)
        matrix_path.write_text(render_matrix(registry, locale, root), encoding="utf-8")
        register_path.write_text(render_matching_register(registry, locale), encoding="utf-8")
        review_path.write_text(render_match_review(registry, locale), encoding="utf-8")
        print(f"generated={matrix_path.relative_to(root)}")
        print(f"generated={register_path.relative_to(root)}")
        print(f"generated={review_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
