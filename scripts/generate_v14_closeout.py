#!/usr/bin/env python3
"""Validate and render the v1.4 governance and release closeout contract."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Any

try:
    from .generate_skill_governance_matrix import (
        REQUIRED_MATCH_REVIEW_CANDIDATES as REGISTRY_MATCH_REVIEW_CANDIDATES,
        load_registry,
    )
except ImportError:  # pragma: no cover - direct script execution
    from generate_skill_governance_matrix import (
        REQUIRED_MATCH_REVIEW_CANDIDATES as REGISTRY_MATCH_REVIEW_CANDIDATES,
        load_registry,
    )


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "docs/governance/v1-4-closeout.yaml"
ALLOWED_BOUNDARIES = {
    "static": {"VERIFIED"},
    "runtime": {"NOT_RUN"},
    "model_eval": {"NOT_RUN"},
    "release_approval": {"NOT_RUN"},
}
ALLOWED_KINDS = {
    "virtual-domain",
    "governance",
    "documentation",
    "retrospective",
    "release-prep",
    "mapping",
    "milestone",
    "release-dod",
}
ALLOWED_ACCEPTANCE_STATES = {"VERIFIED_STATIC", "VERIFIED_STATIC_WITH_RELEASE_NOT_RUN"}
EXPECTED_V14_PROJECT_ITEMS = (
    ("PVTI_lAHOAHP1as4BjBhVzg6SrHw", "v1.0｜治理｜16 个虚拟 Domain 分类"),
    ("PVTI_lAHOAHP1as4BjBhVzg6SrMU", "v1.0｜治理｜Deprecation 与替代路径规则"),
    ("PVTI_lAHOAHP1as4BjBhVzg6SrNg", "v1.0｜治理｜中英文一致性质量契约"),
    ("PVTI_lAHOAHP1as4BjBhVzg6SrPk", "v1.0｜治理｜Skill Quality Score 与最低 Eval 标准"),
    ("PVTI_lAHOAHP1as4BjBhVzg6SrYc", "v1.0｜文档｜README 与双语入口治理"),
    ("PVTI_lAHOAHP1as4BjBhVzg6SrZ4", "v1.0｜文档｜Skill Map Graph Catalog 治理"),
    ("PVTI_lAHOAHP1as4BjBhVzg6Srck", "v1.0｜文档｜Workflow Eval 安装文档同步清单"),
    ("PVTI_lAHOAHP1as4BjBhVzg6Srds", "v1.0｜复盘｜Phase 0 Governance Review"),
    ("PVTI_lAHOAHP1as4BjBhVzg6SrfA", "v1.0｜里程碑｜v1.0 Governance 发布准备"),
    ("PVTI_lAHOAHP1as4BjBhVzg6S3dk", "v1.0｜治理｜典型 Match Merge 映射复核"),
    ("PVTI_lAHOAHP1as4BjBhVzg6S30Y", "治理｜Enhancement Sprint 节奏"),
    ("PVTI_lAHOAHP1as4BjBhVzg6S32E", "治理｜候选 Skill 15 步执行模板"),
    ("PVTI_lAHOAHP1as4BjBhVzg6S38Q", "里程碑｜v1.1-v1.4 Shift Left"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TITI", "治理｜Match Enhance｜requirement-change-impact-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIVU", "治理｜Merge｜test-impact-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIWg", "治理｜Merge Enhance｜code-change-risk-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIYs", "治理｜Match｜workload-modeling"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIaM", "治理｜Match｜capacity-planning"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIcE", "治理｜Existing｜performance-bottleneck-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIeE", "治理｜Existing｜performance-result-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIf8", "治理｜Existing｜performance-regression-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIiA", "治理｜Existing｜flaky-test-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIjI", "治理｜Existing｜production-verification"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIlI", "治理｜Merge｜regression-scope-selection"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIno", "治理｜Match｜ai-test-case-review"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIpg", "治理｜Match Enhance｜ai-log-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIrY", "治理｜Match Enhance｜ai-root-cause-analysis"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIs8", "治理｜Match｜quality-risk-identification"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIvo", "治理｜Match Enhance｜ai-test-data-generation"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIw8", "治理｜Match Enhance｜llm-output-quality-testing"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TIyo", "治理｜Match｜llm-evaluation"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TI0E", "治理｜Existing｜prompt-testing"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TI2M", "治理｜Existing｜agent-tool-testing"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TaoM", "Release DoD｜v1.0"),
    ("PVTI_lAHOAHP1as4BjBhVzg6TarQ", "Release DoD｜v1.4"),
)
REQUIRED_MATCH_REVIEW_CANDIDATES = REGISTRY_MATCH_REVIEW_CANDIDATES
REQUIRED_BILINGUAL_PAIRS = (
    ("docs/governance/PHASE_0_V1_4_CLOSEOUT.md", "docs/governance/PHASE_0_V1_4_CLOSEOUT_EN.md"),
    ("docs/governance/RELEASE_DOD_V1_0.md", "docs/governance/RELEASE_DOD_V1_0_EN.md"),
    ("docs/governance/RELEASE_DOD_V1_4.md", "docs/governance/RELEASE_DOD_V1_4_EN.md"),
    ("docs/governance/DEPRECATION_DECISION_CONTRACT.md", "docs/governance/DEPRECATION_DECISION_CONTRACT_EN.md"),
    ("docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md", "docs/governance/BILINGUAL_CONSISTENCY_CONTRACT_EN.md"),
    ("docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md", "docs/governance/QUALITY_SCORE_EVAL_CONTRACT_EN.md"),
    ("docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md", "docs/governance/WORKFLOW_EVAL_INSTALL_SYNC_EN.md"),
    ("docs/governance/ENHANCEMENT_SPRINT.md", "docs/governance/ENHANCEMENT_SPRINT_EN.md"),
    ("docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE.md", "docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE_EN.md"),
    ("docs/governance/SHIFT_LEFT_MILESTONE.md", "docs/governance/SHIFT_LEFT_MILESTONE_EN.md"),
    ("docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md", "docs/governance/PHASE_0_MATCH_MERGE_REVIEW_EN.md"),
)


@dataclass(frozen=True)
class MatchReviewLink:
    project_item_id: str
    candidate: str
    conclusion: str
    review_state: str
    target_skills: tuple[str, ...]
    evidence_paths: tuple[str, ...]
    next_action: str


@dataclass(frozen=True)
class CloseoutCard:
    project_item_id: str
    title: str
    kind: str
    priority: str
    target_version: str
    project_status_before: str
    project_status_after: str
    acceptance_state: str
    evidence_paths: tuple[str, ...]
    match_review_candidate: str | None


@dataclass(frozen=True)
class CloseoutContract:
    target_version: str
    theme: str
    project_number: int
    project_title: str
    project_owner: str
    project_item_type: str
    project_status_verified_at: str
    final_project_counts: dict[str, dict[str, int]]
    boundaries: dict[str, str]
    boundary_text: str
    next_versions: tuple[dict[str, str], ...]
    quality_score_dimensions: tuple[str, ...]
    minimum_eval_case_types: tuple[str, ...]
    release_dod_scopes: dict[str, tuple[str, ...]]
    cards: tuple[CloseoutCard, ...]
    match_review_links: tuple[MatchReviewLink, ...]
    generated: dict[str, Any]


def _required_text(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"missing {key}")
    return value.strip()


def _required_text_list(data: dict[str, Any], key: str) -> tuple[str, ...]:
    value = data.get(key)
    if not isinstance(value, list) or not value or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise ValueError(f"{key} must be a non-empty list of non-empty strings")
    return tuple(item.strip() for item in value)


def load_contract(path: Path) -> CloseoutContract:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("closeout contract must be an object")
    raw_cards = data.get("cards")
    if not isinstance(raw_cards, list):
        raise ValueError("closeout cards must be a list")
    cards: list[CloseoutCard] = []
    for raw in raw_cards:
        if not isinstance(raw, dict):
            raise ValueError("each closeout card must be an object")
        evidence = raw.get("evidence_paths")
        if not isinstance(evidence, list):
            raise ValueError("card evidence_paths must be a list")
        match_review_candidate = raw.get("match_review_candidate")
        if match_review_candidate is not None and (
            not isinstance(match_review_candidate, str) or not match_review_candidate.strip()
        ):
            raise ValueError("card match_review_candidate must be a non-empty string or null")
        cards.append(
            CloseoutCard(
                project_item_id=_required_text(raw, "project_item_id"),
                title=_required_text(raw, "title"),
                kind=_required_text(raw, "kind"),
                priority=_required_text(raw, "priority"),
                target_version=_required_text(raw, "target_version"),
                project_status_before=_required_text(raw, "project_status_before"),
                project_status_after=_required_text(raw, "project_status_after"),
                acceptance_state=_required_text(raw, "acceptance_state"),
                evidence_paths=tuple(_required_text({"value": value}, "value") for value in evidence),
                match_review_candidate=(
                    match_review_candidate.strip() if isinstance(match_review_candidate, str) else None
                ),
            )
        )
    raw_match_review_links = data.get("match_review_links")
    if not isinstance(raw_match_review_links, list):
        raise ValueError("match_review_links must be a list")
    match_review_links: list[MatchReviewLink] = []
    for raw_link in raw_match_review_links:
        if not isinstance(raw_link, dict):
            raise ValueError("each match_review_link must be an object")
        match_review_links.append(
            MatchReviewLink(
                project_item_id=_required_text(raw_link, "project_item_id"),
                candidate=_required_text(raw_link, "candidate"),
                conclusion=_required_text(raw_link, "conclusion"),
                review_state=_required_text(raw_link, "review_state"),
                target_skills=_required_text_list(raw_link, "target_skills"),
                evidence_paths=_required_text_list(raw_link, "evidence_paths"),
                next_action=_required_text(raw_link, "next_action"),
            )
        )
    boundaries = data.get("boundaries")
    next_versions = data.get("next_versions")
    dimensions = data.get("quality_score_dimensions")
    eval_types = data.get("minimum_eval_case_types")
    raw_release_dod_scopes = data.get("release_dod_scopes")
    generated = data.get("generated")
    if not isinstance(boundaries, dict) or not isinstance(next_versions, list):
        raise ValueError("boundaries and next_versions must be present")
    if not isinstance(dimensions, list) or not isinstance(eval_types, list):
        raise ValueError("quality_score_dimensions and minimum_eval_case_types must be lists")
    if not isinstance(raw_release_dod_scopes, dict):
        raise ValueError("release_dod_scopes must be an object")
    release_dod_scopes: dict[str, tuple[str, ...]] = {}
    for version, raw_titles in raw_release_dod_scopes.items():
        if not isinstance(raw_titles, list) or any(
            not isinstance(title, str) or not title.strip() for title in raw_titles
        ):
            raise ValueError(f"release_dod_scopes[{version!r}] must be a list of non-empty titles")
        release_dod_scopes[str(version)] = tuple(title.strip() for title in raw_titles)
    if not isinstance(generated, dict):
        raise ValueError("generated outputs must be an object")
    return CloseoutContract(
        target_version=_required_text(data, "target_version"),
        theme=_required_text(data, "theme"),
        project_number=int(data.get("project_number", 0)),
        project_title=_required_text(data, "project_title"),
        project_owner=_required_text(data, "project_owner"),
        project_item_type=_required_text(data, "project_item_type"),
        project_status_verified_at=_required_text(data, "project_status_verified_at"),
        final_project_counts={
            str(version): {str(status): int(count) for status, count in counts.items()}
            for version, counts in data.get("final_project_counts", {}).items()
            if isinstance(counts, dict)
        },
        boundaries={str(key): str(value) for key, value in boundaries.items()},
        boundary_text=_required_text(data, "boundary_text"),
        next_versions=tuple(dict(item) for item in next_versions if isinstance(item, dict)),
        quality_score_dimensions=tuple(str(item) for item in dimensions),
        minimum_eval_case_types=tuple(str(item) for item in eval_types),
        release_dod_scopes=release_dod_scopes,
        cards=tuple(cards),
        match_review_links=tuple(match_review_links),
        generated=generated,
    )


def validate_contract(
    contract: CloseoutContract,
    root: Path,
    *,
    allow_generated: bool = False,
) -> list[str]:
    errors: list[str] = []
    if contract.target_version != "v1.4":
        errors.append("target_version must be v1.4")
    if contract.project_number != 4:
        errors.append("project_number must be 4")
    if contract.project_owner != "naodeng":
        errors.append("project_owner must be naodeng")
    if contract.project_item_type != "DraftIssue":
        errors.append("project_item_type must be DraftIssue")
    if contract.project_status_verified_at != "2026-09-16":
        errors.append("project_status_verified_at must be 2026-09-16")
    if contract.final_project_counts.get("v1.4") != {"Done": 35, "In Progress": 0, "Todo": 0}:
        errors.append("final v1.4 Project counts must be 35 Done, 0 In Progress, 0 Todo")
    if len(contract.cards) != 35:
        errors.append(f"expected 35 cards, got {len(contract.cards)}")
    titles = [card.title for card in contract.cards]
    ids = [card.project_item_id for card in contract.cards]
    if len(titles) != len(set(titles)):
        errors.append("duplicate card title")
    if len(ids) != len(set(ids)):
        errors.append("duplicate project item id")
    if {(card.project_item_id, card.title) for card in contract.cards} != set(EXPECTED_V14_PROJECT_ITEMS):
        errors.append("cards must match the canonical v1.4 Project item ID/title set")
    generated_paths = _generated_relative_paths(contract.generated)
    for primary_rel, english_rel in REQUIRED_BILINGUAL_PAIRS:
        for document_rel in (primary_rel, english_rel):
            if not (root / document_rel).is_file() and not (
                allow_generated and document_rel in generated_paths
            ):
                errors.append(f"missing required bilingual document: {document_rel}")
    for card in contract.cards:
        prefix = f"{card.title}:"
        if card.kind not in ALLOWED_KINDS:
            errors.append(f"{prefix} invalid kind {card.kind}")
        if card.priority != "P0":
            errors.append(f"{prefix} priority must be P0")
        if card.target_version != "v1.4":
            errors.append(f"{prefix} target version must be v1.4")
        if card.project_status_before not in {"Done", "In Progress"}:
            errors.append(f"{prefix} invalid project_status_before")
        if card.project_status_after != "Done":
            errors.append(f"{prefix} project_status_after must be Done")
        if card.acceptance_state not in ALLOWED_ACCEPTANCE_STATES:
            errors.append(f"{prefix} invalid acceptance_state")
        if not card.evidence_paths:
            errors.append(f"{prefix} evidence_paths must not be empty")
        for evidence_path in card.evidence_paths:
            path = root / evidence_path
            if not path.is_file() and not (allow_generated and evidence_path in generated_paths):
                errors.append(f"missing evidence path: {evidence_path}")
    mapping_error = "mapping card match_review_candidate set must match Registry"
    mapping_candidates = tuple(
        card.match_review_candidate for card in contract.cards if card.match_review_candidate
    )
    if len(mapping_candidates) != len(REQUIRED_MATCH_REVIEW_CANDIDATES) or set(mapping_candidates) != set(REQUIRED_MATCH_REVIEW_CANDIDATES):
        errors.append(mapping_error)
    if any(card.match_review_candidate and card.kind != "mapping" for card in contract.cards):
        errors.append("match_review_candidate is only allowed on mapping cards")
    mapping_cards_by_id = {
        card.project_item_id: card
        for card in contract.cards
        if card.kind == "mapping" and card.match_review_candidate
    }
    match_review_links_by_id = {
        link.project_item_id: link for link in contract.match_review_links
    }
    link_ids = [link.project_item_id for link in contract.match_review_links]
    if len(contract.match_review_links) != len(REQUIRED_MATCH_REVIEW_CANDIDATES):
        errors.append("match_review_links must contain the exact 20-row mapping contract")
    if len(link_ids) != len(set(link_ids)):
        errors.append("duplicate match_review link project item id")
    if set(match_review_links_by_id) != set(mapping_cards_by_id):
        errors.append("match_review_links must match mapping card Project item IDs")
    link_candidates = tuple(link.candidate for link in contract.match_review_links)
    if len(link_candidates) != len(REQUIRED_MATCH_REVIEW_CANDIDATES) or set(link_candidates) != set(REQUIRED_MATCH_REVIEW_CANDIDATES):
        errors.append("match_review link candidate set must match Registry")
    for card in contract.cards:
        link = match_review_links_by_id.get(card.project_item_id)
        if card.match_review_candidate:
            if link is None:
                errors.append(f"{card.title}: missing match_review link")
            elif link.candidate != card.match_review_candidate:
                errors.append(f"{card.title}: match_review link candidate must match card")
        elif link is not None:
            errors.append(f"{card.title}: match_review link is only allowed on mapping cards")
    registry_path = root / "docs/governance/skill-governance-registry.yaml"
    if not registry_path.is_file():
        errors.append("missing match review Registry: docs/governance/skill-governance-registry.yaml")
    else:
        try:
            registry = load_registry(registry_path)
        except (OSError, ValueError) as error:
            errors.append(f"invalid match review Registry: {error}")
        else:
            registry_candidates = tuple(str(review.get("candidate", "")) for review in registry.match_reviews)
            if set(mapping_candidates) != set(registry_candidates) and mapping_error not in errors:
                errors.append(mapping_error)
            registry_by_candidate = {
                str(review.get("candidate", "")): review for review in registry.match_reviews
            }
            for link in contract.match_review_links:
                registry_review = registry_by_candidate.get(link.candidate)
                if registry_review is None:
                    errors.append(f"{link.project_item_id}: match review candidate is not in Registry")
                    continue
                expected_fields = {
                    "candidate": str(registry_review.get("candidate", "")),
                    "conclusion": str(registry_review.get("conclusion", "")),
                    "review_state": str(registry_review.get("review_state", "")),
                    "target_skills": tuple(str(value) for value in registry_review.get("target_skills", [])),
                    "evidence_paths": tuple(str(value) for value in registry_review.get("evidence_paths", [])),
                    "next_action": str(registry_review.get("next_action", "")),
                }
                actual_fields = {
                    "candidate": link.candidate,
                    "conclusion": link.conclusion,
                    "review_state": link.review_state,
                    "target_skills": link.target_skills,
                    "evidence_paths": link.evidence_paths,
                    "next_action": link.next_action,
                }
                for field, expected in expected_fields.items():
                    if actual_fields[field] != expected:
                        errors.append(f"{link.project_item_id}: match review {field} must match Registry")
                for evidence_path in link.evidence_paths:
                    path = Path(evidence_path)
                    if path.is_absolute() or ".." in path.parts:
                        errors.append(
                            f"{link.candidate}: match review evidence path must be repository-relative file: {evidence_path}"
                        )
                    elif not (root / path).is_file():
                        errors.append(f"{link.candidate}: missing match review evidence path: {evidence_path}")
            for card in contract.cards:
                candidate = card.match_review_candidate
                if candidate and not card.title.endswith(f"｜{candidate}"):
                    errors.append(f"{card.title}: title must end with match review candidate {candidate}")
    if set(contract.boundaries) != set(ALLOWED_BOUNDARIES):
        errors.append("boundary keys must be static, runtime, model_eval, release_approval")
    for key, allowed in ALLOWED_BOUNDARIES.items():
        if contract.boundaries.get(key) not in allowed:
            errors.append(f"invalid {key} boundary")
    if "NOT_SCORED" not in contract.boundary_text:
        errors.append("boundary_text must preserve NOT_SCORED")
    if "UNASSESSED" not in contract.boundary_text:
        errors.append("boundary_text must preserve UNASSESSED")
    if set(contract.quality_score_dimensions) != {
        "problem_value", "scope_clarity", "input_quality", "analysis_depth",
        "output_actionability", "evidence_quality", "reusability", "eval_coverage", "documentation",
    } or len(contract.quality_score_dimensions) != 9:
        errors.append("quality_score_dimensions must contain the nine dimensions exactly once")
    if set(contract.minimum_eval_case_types) != {"success_path", "incomplete_information", "scope_or_risk_boundary"} or len(contract.minimum_eval_case_types) != 3:
        errors.append("minimum_eval_case_types must contain the three required case classes exactly once")
    if set(contract.release_dod_scopes) != {"v1.0"}:
        errors.append("release_dod_scopes must declare the v1.0 baseline scope")
    v10_scope = contract.release_dod_scopes.get("v1.0", ())
    if len(v10_scope) != 10:
        errors.append(f"v1.0 Release DoD scope must contain 10 records, got {len(v10_scope)}")
    if len(v10_scope) != len(set(v10_scope)):
        errors.append("v1.0 Release DoD scope contains duplicate titles")
    unknown_scope_titles = sorted(set(v10_scope) - set(titles))
    if unknown_scope_titles:
        errors.append("v1.0 Release DoD scope contains unknown card titles: " + ", ".join(unknown_scope_titles))
    expected_next = {"P1": "v1.5", "P2": "v1.6", "Backlog": "v1.7"}
    for priority, version in expected_next.items():
        if not any(item.get("priority") == priority and item.get("version") == version for item in contract.next_versions):
            errors.append(f"missing next-version mapping: {priority}->{version}")
    if not any(item.get("priority") == "Backlog" and item.get("version") == "v1.8" for item in contract.next_versions):
        errors.append("missing next-version mapping: Backlog->v1.8")
    return errors


def validate_project_snapshot(contract: CloseoutContract, payload: Any) -> list[str]:
    """Validate a live `gh project item-list --format json` response."""
    if not isinstance(payload, dict):
        return ["Project response must be an object"]
    items = payload.get("items")
    if not isinstance(items, list):
        return ["Project response items must be a list"]

    expected_by_id = {card.project_item_id: card for card in contract.cards}
    observed_by_id: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"Project item at index {index} must be an object")
            continue
        project_item_id = item.get("id")
        if not isinstance(project_item_id, str) or not project_item_id.strip():
            errors.append(f"Project item at index {index} is missing id")
            continue
        if project_item_id in observed_by_id:
            errors.append(f"duplicate live Project item id: {project_item_id}")
            continue
        observed_by_id[project_item_id] = item
        card = expected_by_id.get(project_item_id)
        if card is None:
            title = item.get("title")
            if isinstance(title, str) and title in {expected.title for expected in contract.cards}:
                errors.append(
                    f"unexpected {contract.target_version} Project item with canonical title: {project_item_id} ({title})"
                )
            elif (
                isinstance(title, str)
                and re.search(rf"(?<![A-Za-z0-9]){re.escape(contract.target_version)}(?![A-Za-z0-9])", title)
            ):
                errors.append(f"unexpected {contract.target_version} Project item: {project_item_id} ({title})")
            continue

        if item.get("title") != card.title:
            errors.append(
                f"{card.title}: live title must be {card.title!r}, got {item.get('title')!r}"
            )
        if item.get("status") != card.project_status_after:
            errors.append(
                f"{card.title}: live status must be {card.project_status_after!r}, got {item.get('status')!r}"
            )
        content = item.get("content")
        if not isinstance(content, dict):
            errors.append(f"{card.title}: live content must be an object")
            continue
        if content.get("type") != contract.project_item_type:
            errors.append(
                f"{card.title}: live content type must be {contract.project_item_type!r}, got {content.get('type')!r}"
            )
        if content.get("title") != card.title:
            errors.append(
                f"{card.title}: live content title must be {card.title!r}, got {content.get('title')!r}"
            )

    for card in contract.cards:
        if card.project_item_id not in observed_by_id:
            errors.append(f"missing live Project item: {card.project_item_id} ({card.title})")
    observed_target_items = [observed_by_id[card.project_item_id] for card in contract.cards if card.project_item_id in observed_by_id]
    expected_counts = contract.final_project_counts.get(contract.target_version, {})
    actual_counts = Counter(str(item.get("status")) for item in observed_target_items)
    normalized_actual_counts = {
        status: actual_counts.get(status, 0)
        for status in set(expected_counts) | set(actual_counts)
    }
    if expected_counts and normalized_actual_counts != expected_counts:
        errors.append(
            f"live {contract.target_version} Project status counts must be {expected_counts}, got {normalized_actual_counts}"
        )
    return errors


def fetch_project_snapshot(contract: CloseoutContract) -> dict[str, Any]:
    """Fetch the current Project items without mutating GitHub state."""
    command = [
        "gh",
        "project",
        "item-list",
        str(contract.project_number),
        "--owner",
        contract.project_owner,
        "--format",
        "json",
        "--limit",
        "200",
    ]
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
    except OSError as error:
        raise RuntimeError(f"unable to run {' '.join(command)}: {error}") from error
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown gh error"
        raise RuntimeError(f"{' '.join(command)} failed: {detail}")
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError("gh returned invalid Project JSON") from error
    if not isinstance(payload, dict):
        raise RuntimeError("gh Project response must be a JSON object")
    return payload


def cards_for_release_dod(contract: CloseoutContract, version: str) -> tuple[CloseoutCard, ...]:
    if version == "v1.4":
        return contract.cards
    scope_titles = contract.release_dod_scopes.get(version)
    if scope_titles is None:
        raise ValueError(f"Release DoD scope is not declared for {version}")
    cards_by_title = {card.title: card for card in contract.cards}
    try:
        return tuple(cards_by_title[title] for title in scope_titles)
    except KeyError as error:
        raise ValueError(f"Release DoD scope references unknown card {error.args[0]!r}") from error


def _generated_relative_paths(value: Any) -> set[str]:
    if isinstance(value, str):
        return {value}
    if isinstance(value, dict):
        paths: set[str] = set()
        for child in value.values():
            paths.update(_generated_relative_paths(child))
        return paths
    if isinstance(value, (list, tuple)):
        paths: set[str] = set()
        for child in value:
            paths.update(_generated_relative_paths(child))
        return paths
    return set()


def _relative_evidence(root: Path, output_path: Path, evidence_path: str) -> str:
    target = root / evidence_path
    relative = os.path.relpath(target, output_path.parent).replace(os.sep, "/")
    return f"[{evidence_path}]({relative})"


def _card_kind_label(kind: str, locale: str) -> str:
    labels = {
        "zh": {
            "virtual-domain": "虚拟 Domain",
            "governance": "治理",
            "documentation": "文档",
            "retrospective": "复盘",
            "release-prep": "发布准备",
            "mapping": "映射",
            "milestone": "里程碑",
            "release-dod": "Release DoD",
        },
        "en": {
            "virtual-domain": "Virtual Domain",
            "governance": "Governance",
            "documentation": "Documentation",
            "retrospective": "Retrospective",
            "release-prep": "Release preparation",
            "mapping": "Mapping",
            "milestone": "Milestone",
            "release-dod": "Release DoD",
        },
    }
    return labels[locale][kind]


def render_closeout(contract: CloseoutContract, locale: str, root: Path | None = None) -> str:
    root = root or ROOT
    english = locale == "en"
    output_rel = contract.generated["closeout"][locale]
    output_path = root / output_rel
    switch_target = "PHASE_0_V1_4_CLOSEOUT.md" if english else "PHASE_0_V1_4_CLOSEOUT_EN.md"
    title = "v1.4 Phase 0 Governance Closeout" if english else "v1.4 Phase 0 治理收口"
    intro = (
        "Generated from the v1.4 closeout contract. A Project card can be Done when its repository deliverable is verified; this does not mean the v1.4 release itself is approved."
        if english else
        "本文由 v1.4 收口契约生成。Project 卡片可以在仓库交付物验收后标记 Done；这不代表 v1.4 版本本身已获发布批准。"
    )
    static = "Repository/static evidence: `VERIFIED`; runtime: `NOT_RUN`; model Eval: `NOT_RUN`; release approval: `NOT_RUN`." if english else "仓库/静态证据：`VERIFIED`；运行时：`NOT_RUN`；模型 Eval：`NOT_RUN`；发布批准：`NOT_RUN`。"
    before_done = sum(card.project_status_before == "Done" for card in contract.cards)
    before_progress = sum(card.project_status_before == "In Progress" for card in contract.cards)
    final_counts = contract.final_project_counts["v1.4"]
    summary = (
        f"The contract covers {len(contract.cards)} P0 cards: {before_done} were already Done and {before_progress} were transitioned; Project verification on {contract.project_status_verified_at} reports v1.4 = {final_counts['Done']} Done, {final_counts['In Progress']} In Progress, {final_counts['Todo']} Todo."
        if english else
        f"契约覆盖 {len(contract.cards)} 张 P0 卡片：{before_done} 张原已 Done，{before_progress} 张完成本批转移；{contract.project_status_verified_at} 复核结果为 v1.4：Done {final_counts['Done']}、In Progress {final_counts['In Progress']}、Todo {final_counts['Todo']}。"
    )
    headers = (
        "| Project item ID | Project item | Kind | Before → after | Acceptance | Evidence |" if english
        else "| Project item ID | Project 卡片 | 类型 | 前置 → 目标 | 验收 | 证据 |"
    )
    lines = [
        f'<div align="right"><a href="./{switch_target}">{"中文" if english else "English"}</a></div>',
        "",
        f"# {title}",
        "",
        intro,
        "",
        f"**Theme:** `{contract.theme}`",
        f"**Project:** `#{contract.project_number}` — {contract.project_title}",
        "",
        summary,
        static,
        contract.boundary_text,
        "",
        headers,
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for card in contract.cards:
        evidence = "<br>".join(_relative_evidence(root, output_path, path) for path in card.evidence_paths)
        lines.append(
            f"| `{card.project_item_id}` | `{card.title}` | {_card_kind_label(card.kind, locale)} | "
            f"`{card.project_status_before}` → `{card.project_status_after}` | "
            f"`{card.acceptance_state}` | {evidence} |"
        )
    cards_by_id = {card.project_item_id: card for card in contract.cards}
    links_by_id = {link.project_item_id: link for link in contract.match_review_links}
    mapping_links = [
        links_by_id[card.project_item_id]
        for card in contract.cards
        if card.match_review_candidate and card.project_item_id in links_by_id
    ]
    if mapping_links:
        lines.extend([
            "",
            "## Match review linkage" if english else "## Match Review 关联",
            "",
            (
                "| Project item ID | Project item | Candidate | Conclusion | Review state | Target Skills | Next action | Evidence |"
                if english else
                "| Project item ID | Project 卡片 | Candidate | 结论 | 评审状态 | 目标 Skill | 后续动作 | 证据 |"
            ),
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for link in mapping_links:
            card = cards_by_id[link.project_item_id]
            targets = "<br>".join(f"`{target}`" for target in link.target_skills)
            evidence = "<br>".join(
                _relative_evidence(root, output_path, path) for path in link.evidence_paths
            )
            lines.append(
                f"| `{link.project_item_id}` | `{card.title}` | `{link.candidate}` | `{link.conclusion}` | "
                f"`{link.review_state}` | {targets} | {link.next_action} | {evidence} |"
            )
    lines.extend([
        "",
        "## Version plan" if english else "## 版本规划",
        "",
        "| Priority | Version | Scope |" if english else "| 优先级 | 版本 | 范围 |",
        "| --- | --- | --- |",
    ])
    for item in contract.next_versions:
        lines.append(f"| `{item.get('priority', 'UNASSESSED')}` | `{item.get('version', 'UNASSESSED')}` | {item.get('scope', 'UNASSESSED')} |")
    lines.extend([
        "",
        "## Evidence boundary" if english else "## 证据边界",
        "",
        "- `NOT_SCORED` remains the Quality Score state until nine-dimension scoring evidence exists." if english else "- 没有九维评分证据前，Quality Score 保持 `NOT_SCORED`。",
        "- `NOT_RUN` remains the Eval/runtime state when no real target, model, or external environment was executed." if english else "- 未执行真实目标、模型或外部环境时，Eval/运行状态保持 `NOT_RUN`。",
        "- `UNASSESSED` remains for semantic equivalence, business acceptance, risk acceptance, and external indexing/publication." if english else "- 语义等价、业务验收、风险接受和外部索引/发布状态保持 `UNASSESSED`。",
        "- No physical Skill directory is created, deleted, renamed, or treated as an alias by this v1.4 closeout." if english else "- 本次 v1.4 收口不创建、删除、重命名物理 Skill 目录，也不把目录当作别名。",
        "",
        "## Reproduce" if english else "## 复现",
        "",
        "```bash",
        "python3 scripts/generate_v14_closeout.py --verify-project",
        "python3 scripts/generate_v14_closeout.py --check",
        "python3 scripts/generate_skill_governance_matrix.py --check",
        "python3 scripts/check_docs_bilingual.py --repo-root .",
        "```",
        "",
        (
            "`--check` validates the checked-in contract and generated views offline; `--verify-project` compares the live Project items by id, title, status, and content type."
            if english else
            "`--check` 只离线校验仓库中的契约和生成视图；`--verify-project` 会按 ID、标题、状态和内容类型复核实时 Project 条目。"
        ),
    ])
    return "\n".join(lines) + "\n"


def render_release_dod(contract: CloseoutContract, version: str, locale: str, root: Path | None = None) -> str:
    root = root or ROOT
    if version not in {"v1.0", "v1.4"}:
        raise ValueError("Release DoD version must be v1.0 or v1.4")
    english = locale == "en"
    output_rel = contract.generated["release_dod"][version][locale]
    output_path = root / output_rel
    version_file = version.upper().replace(".", "_")
    switch_target = f"RELEASE_DOD_{version_file}.md" if english else f"RELEASE_DOD_{version_file}_EN.md"
    title = f"{version} Release DoD (governance closeout)" if english else f"{version} Release DoD（治理收口）"
    included = cards_for_release_dod(contract, version)
    contract_evidence = (
        f"{len(included)}-card {version} closeout contract and generated view"
        if english else
        f"{len(included)} 张 {version} 收口契约与生成视图"
    )
    package_evidence = (
        f"{version} governance closeout creates no package directories"
        if english else
        f"{version} 治理收口不创建 Skill 目录"
    )
    lines = [
        f'<div align="right"><a href="./{switch_target}">{"中文" if english else "English"}</a></div>',
        "",
        f"# {title}",
        "",
        (
            "This checklist evaluates repository governance delivery, not a published package or release approval."
            if english else
            "本清单验收仓库治理交付，不等同于已发布包或发布批准。"
        ),
        "",
        "| Gate | State | Evidence / boundary |" if english else "| 门禁 | 状态 | 证据 / 边界 |",
        "| --- | --- | --- |",
        (
            f"| Contract and card evidence | `VERIFIED` | {contract_evidence} |"
            if english else
            f"| 契约与卡片证据 | `VERIFIED` | {contract_evidence} |"
        ),
        (
            "| Repository quality gate | `VERIFIED` | `bash scripts/check_skills_quality.sh` |"
            if english else
            "| 仓库质量门禁 | `VERIFIED` | `bash scripts/check_skills_quality.sh` |"
        ),
        (
            "| Bilingual/link/freshness checks | `VERIFIED` | Matrix, inventory, and bilingual documentation checks |"
            if english else
            "| 双语/链接/freshness 检查 | `VERIFIED` | Matrix、Inventory 与双语文档检查 |"
        ),
        (
            f"| Physical Skill package changes | `N/A` | {package_evidence} |"
            if english else
            f"| 物理 Skill 包变更 | `N/A` | {package_evidence} |"
        ),
        (
            "| Runtime and external target execution | `NOT_RUN` | No real application, API, browser, or production target was executed |"
            if english else
            "| 运行时与外部目标执行 | `NOT_RUN` | 未执行真实应用、API、浏览器或生产目标 |"
        ),
        (
            "| Model-backed Eval and Quality Score | `NOT_RUN` / `NOT_SCORED` | Static structure does not prove model effectiveness or quality score |"
            if english else
            "| 模型 Eval 与 Quality Score | `NOT_RUN` / `NOT_SCORED` | 静态结构不证明模型效果或质量分数 |"
        ),
        (
            "| Human release approval, risk acceptance, push, and publication | `N/A` / `NOT_RUN` | Requires an explicit human decision and external delivery action |"
            if english else
            "| 人工发布批准、风险接受、推送与发布 | `N/A` / `NOT_RUN` | 需要明确人工决策和外部交付动作 |"
        ),
        "",
        (f"The `{version}` scope includes {len(included)} contract records; each Project card may be marked Done for its verified repository deliverable, while release approval remains `NOT_RUN`." if english else f"`{version}` 范围包含 {len(included)} 条契约记录；每张 Project 卡可因仓库交付物验收而标记 Done，但发布批准仍为 `NOT_RUN`。"),
        "",
        "## Card evidence" if english else "## 卡片证据",
        "",
        "| Card | Kind | Acceptance | Evidence |" if english else "| 卡片 | 类型 | 验收 | 证据 |",
        "| --- | --- | --- | --- |",
    ]
    for card in included:
        evidence = "<br>".join(_relative_evidence(root, output_path, path) for path in card.evidence_paths)
        lines.append(f"| `{card.title}` | {_card_kind_label(card.kind, locale)} | `{card.acceptance_state}` | {evidence} |")
    lines.extend([
        "",
        "## Reproduce" if english else "## 复现",
        "",
        "```bash",
        "python3 scripts/generate_v14_closeout.py --verify-project",
        "python3 scripts/generate_v14_closeout.py --check",
        "bash scripts/check_skills_quality.sh",
        "```",
        "",
        (
            "The live Project verification covers the full v1.4 card set; this DoD view intentionally shows only its declared version scope."
            if english else
            "实时 Project 校验覆盖完整 v1.4 卡片集；本 DoD 视图只展示契约中声明的对应版本范围。"
        ),
    ])
    return "\n".join(lines) + "\n"


def generated_paths(contract: CloseoutContract) -> tuple[Path, ...]:
    paths = [ROOT / value for value in contract.generated["closeout"].values()]
    for outputs in contract.generated["release_dod"].values():
        paths.extend(ROOT / value for value in outputs.values())
    return tuple(paths)


def check_outputs(contract: CloseoutContract, root: Path) -> int:
    expected: dict[Path, str] = {}
    for locale in ("zh", "en"):
        expected[root / contract.generated["closeout"][locale]] = render_closeout(contract, locale, root)
        for version in ("v1.0", "v1.4"):
            expected[root / contract.generated["release_dod"][version][locale]] = render_release_dod(contract, version, locale, root)
    stale = [str(path.relative_to(root)) for path, content in expected.items() if not path.is_file() or path.read_text(encoding="utf-8") != content]
    if stale:
        print("stale_v14_closeout_views=" + ",".join(stale))
        return 1
    print("v14_closeout_views=up-to-date")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated v1.4 views are stale")
    parser.add_argument(
        "--verify-project",
        action="store_true",
        help="verify the live GitHub Project card ids, titles, statuses, and content types",
    )
    args = parser.parse_args()
    contract = load_contract(CONTRACT_PATH)
    errors = validate_contract(contract, ROOT, allow_generated=True)
    if errors:
        for error in errors:
            print(error)
        return 1
    if args.verify_project:
        try:
            payload = fetch_project_snapshot(contract)
        except RuntimeError as error:
            print(f"project_verification_error={error}")
            return 1
        project_errors = validate_project_snapshot(contract, payload)
        if project_errors:
            for error in project_errors:
                print(error)
            return 1
        print(
            f"project_v14=verified cards={len(contract.cards)} "
            f"status=Done type={contract.project_item_type} total_project_items={len(payload['items'])}"
        )
    if args.check:
        return check_outputs(contract, ROOT)
    for locale in ("zh", "en"):
        closeout_path = ROOT / contract.generated["closeout"][locale]
        closeout_path.write_text(render_closeout(contract, locale, ROOT), encoding="utf-8")
        print(f"generated={closeout_path.relative_to(ROOT)}")
        for version in ("v1.0", "v1.4"):
            path = ROOT / contract.generated["release_dod"][version][locale]
            path.write_text(render_release_dod(contract, version, locale, ROOT), encoding="utf-8")
            print(f"generated={path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
