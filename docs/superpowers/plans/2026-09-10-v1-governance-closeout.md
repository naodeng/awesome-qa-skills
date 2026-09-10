<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-10-v1-governance-closeout_EN.md">🇬🇧 English</a></div>

# v1.0 Governance Closeout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a reproducible, bilingual v1.0 source-governance record for every current Skill pair without presenting static evidence as execution or quality results.

**Architecture:** A deterministic repository script inventories paired package directories and their declared metadata/eval structure, then renders the Chinese and English records. The governance guide defines the controlled vocabulary and the Project Card; README, catalog, and graph remain stable discovery entry points.

**Tech Stack:** Python 3 standard library; Markdown; existing repository quality scripts.

**Spec:** User request in this task: audit all 79 bilingual Skill pairs and close v1.0 governance delivery.

## Global Constraints

- Inspect only repository source and declared package assets; do not execute Skill prompts, tests, tools, or live models.
- Mark semantic capability/effectiveness and any unavailable evidence as `UNASSESSED`.
- Do not calculate or imply a Quality Score.
- Preserve unrelated working-tree changes; do not push or publish.

---

### Task 1: Define the governance contract and Project Card

**Files:**
- Create: `docs/governance/SKILL_GOVERNANCE_V1.md`
- Create: `docs/governance/SKILL_GOVERNANCE_V1_EN.md`
- Modify: `scripts/check_docs_bilingual.py`

- [x] Define Virtual Domain, structural status, scope boundary, relation, Eval structure, and Capability Match evidence terms.
- [x] State static-only/UNASSESSED boundaries and project-card acceptance criteria in both languages.
- [x] Register the bilingual pair so broken switches and links fail the existing documentation validator.

### Task 2: Make the 79-pair inventory reproducible

**Files:**
- Create: `scripts/generate_skill_governance_inventory.py`
- Create: `docs/generated/skill-governance-inventory.md`
- Create: `docs/generated/skill-governance-inventory_EN.md`
- Modify: `scripts/check_skills_quality.sh`

- [x] Parse current paired package directories, frontmatter, agent metadata, and declared Eval case paths.
- [x] Render one record per logical Skill, including all required governance fields and source-path evidence.
- [x] Implement `--check` so stale generated records fail deterministically; invoke it from the complete quality gate.

### Task 3: Synchronize discovery entry points

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `docs/catalog/skills-index.md`
- Modify: `docs/catalog/skills-index_EN.md`
- Modify: `docs/catalog/skills-graph.md`
- Modify: `docs/catalog/skills-graph_EN.md`

- [x] Link the governance guide and generated inventory from both language entry points.
- [x] Label links as source-governance records, not runtime proof.

### Task 4: Regenerate and verify

**Files:** all files above.

- [x] Generate the two inventory artifacts.
- [x] Run `python3 scripts/generate_skill_governance_inventory.py --check`.
- [x] Run `bash scripts/check_skills_quality.sh`, inspect generated-file freshness, `git diff --check`, and `git status --short`.
