<div align="right"><a href="./2026-09-10-v1-governance-closeout.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.0 Governance Closeout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a reproducible, bilingual v1.0 source-governance record for every current Skill pair without presenting static evidence as execution or quality results.

**Architecture:** A deterministic repository script inventories paired package directories and their declared metadata/eval structure, then renders Chinese and English records. The governance guide defines the controlled vocabulary and Project Card; README, catalog, and graph remain discovery entry points.

**Tech Stack:** Python 3 standard library; Markdown; existing repository quality scripts.

**Spec:** User request in this task: audit all 79 bilingual Skill pairs and close v1.0 governance delivery.

## Global Constraints

- Inspect only repository source and declared package assets; do not execute Skill prompts, tests, tools, or live models.
- Mark semantic capability/effectiveness and unavailable evidence as `UNASSESSED`.
- Do not calculate or imply a Quality Score.
- Preserve unrelated working-tree changes; do not push or publish.

---

### Task 1: Define the governance contract and Project Card

**Files:** `docs/governance/SKILL_GOVERNANCE_V1.md`, `docs/governance/SKILL_GOVERNANCE_V1_EN.md`, and `scripts/check_docs_bilingual.py`.

- [x] Define Virtual Domain, structural status, scope boundary, relation, Eval structure, and Capability Match evidence terms.
- [x] State static-only/UNASSESSED boundaries and Project Card acceptance criteria in both languages.
- [x] Register the bilingual pair so broken switches and links fail the documentation validator.

### Task 2: Make the 79-pair inventory reproducible

**Files:** `scripts/generate_skill_governance_inventory.py`, generated Chinese/English inventories, and `scripts/check_skills_quality.sh`.

- [x] Parse paired package directories, frontmatter, Agent metadata, and both block-list and inline Eval case declarations.
- [x] Render one record per logical Skill, including all required governance fields and source-path evidence; report missing sides/files as `UNASSESSED (structural gap)`.
- [x] Implement `--check` for deterministic freshness and invoke it from the full quality gate.

### Task 3: Synchronize discovery entry points

**Files:** bilingual root README, catalog index, and graph.

- [x] Link the governance guide and generated inventory from both-language entry points.
- [x] Label the links as source-governance records, not runtime proof.

### Task 4: Regenerate and verify

- [x] Generate both inventories.
- [x] Run `python3 scripts/generate_skill_governance_inventory.py --check`.
- [x] Run unit tests, `bash scripts/check_skills_quality.sh`, `git diff --check`, and inspect `git status --short`.
