<div align="right"><a href="./2026-08-29-project-structure-and-bilingual-docs.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Project Structure and Bilingual Documentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Organize project-level files without changing the `skills/` directory and ensure active project documentation has accurate, Chinese-first, switchable Chinese and English mirrors.

**Architecture:** Keep stable entry points at the root and classify project documentation into catalog, governance, generated, reviews, and archive areas. Protect path changes with link validation and a bilingual manifest while keeping historical records immutable.

**Tech Stack:** Markdown, Python 3 standard library, Bash, Git

**Spec:** `docs/superpowers/specs/2026-08-29-project-structure-and-bilingual-docs-design_EN.md`

## Global Constraints

- Do not move, rename, or remove any directory under `skills/`.
- Chinese is the default for active project documents; English uses `_EN.md` mirrors with two-way switching.
- Do not add language switches to internal Skill documents.
- Preserve unrelated uncommitted script changes.

---

### Task 1: Extend the Documentation Validation Contract

**Files:** `scripts/check_docs_bilingual.py`, `scripts/tests/test_check_docs_bilingual.py`

- [x] Add failing tests for moved project-document pairs and broken relative links.
- [x] Run the focused unit suite and confirm the new tests fail.
- [x] Update pair paths and implement relative Markdown link validation while ignoring URLs, anchors, email links, and fenced code.
- [x] Rerun the focused unit suite and confirm it passes.

### Task 2: Move Project Files and Repair References

**Files:** root catalog/report/draft files, governance documents, README/FAQ pairs, and `scripts/validate_agents_metadata.py`

- [x] Create the approved structure through tracked file moves.
- [x] Update active relative links and README documentation maps.
- [x] Change the metadata validator's default report to `docs/generated/skills-metadata-report.md` while preserving unrelated edits.
- [x] Scan old paths and distinguish active broken references from historical command records.

### Task 3: Review and Correct Bilingual Content

**Files:** contribution, FAQ, README, catalog, governance, and any missing active project-document mirror

- [x] Remove the duplicated full English body from the Chinese contribution guide and FAQ, keeping Chinese content and switch links.
- [x] Compare heading structure, tables, counts, and key conclusions across each pair and repair drift.
- [x] Verify every active project document has working two-way language switching.
- [x] Update the bilingual policy for the new structure and exclusion boundary.

### Task 4: Full Verification and Delivery

**Files:** this plan pair

- [x] Compare the baseline and current `skills/` directory sets.
- [x] Run `python3 -m unittest scripts.tests.test_check_docs_bilingual -v`.
- [x] Run `bash scripts/check_skills_quality.sh` and `git diff --check`.
- [x] Review staged content and exclude unrelated user changes.
- [x] Commit conventionally, push `explore`, and verify PR #4.
