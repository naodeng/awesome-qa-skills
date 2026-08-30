<div align="right"><a href="./2026-08-29-bilingual-lifecycle-navigation.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Bilingual Lifecycle Navigation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Classify every Skill through the four-stage capability model and R&D/testing lifecycle without changing Skill directories, while enforcing maintainable Chinese-English documentation parity.

**Architecture:** Physical Skill directories remain the installation source of truth. README files, roadmaps, and indexes add only logical classification. A standard-library Python checker validates maintained document mirrors, language switches, and README classification completeness through the existing quality gate.

**Tech Stack:** Markdown, Python 3 standard library, Bash, and existing repository quality scripts.

**Spec:** `docs/superpowers/specs/2026-08-29-bilingual-lifecycle-navigation-design_EN.md`

## Global Constraints

- Do not move, rename, or delete any Skill directory under `skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/`.
- Chinese `README.md` remains the default entry and `README_EN.md` is its complete English mirror.
- Each testing-type Skill has one primary classification. Workflows and Skill Engineering remain orchestration and governance layers.
- Keep 78 Skills per language: 10 workflows, 65 testing types, and 3 Skill Engineering packages; 156 bilingual directories total.
- Exclude `legacy-prompts/`, `docs/archive/`, external snapshots, generated artifacts, third-party licenses, and evaluation outputs from file-by-file translation.
- Preserve unrelated worktree changes and stage only files explicitly owned by this plan.

---

### Task 1: Classification Manifest and Failing Validation

**Files:** Create `scripts/check_docs_bilingual.py` and `scripts/tests/test_check_docs_bilingual.py`; modify `scripts/check_skills_quality.sh`.

- [x] Add failing unit cases for a missing mirror, missing reverse link, duplicate classification, missing classification, and changed Skill directory snapshot.
- [x] Implement `check_docs_bilingual.py --repo-root PATH` with standard-library Python and non-zero exit on findings.
- [x] Check explicit project-document pairs and matched zh/en relative paths for maintained Skill documents.
- [x] Add the checker as step seven of the existing quality gate and run the unit tests.

### Task 2: Root README Lifecycle Navigation

**Files:** Modify `README.md` and `README_EN.md`.

- [x] Snapshot all Skill directory paths before edits.
- [x] Correct counts and remove stale roadmap language.
- [x] Keep workflow orchestration separate.
- [x] Place all 65 testing-type Skills exactly once under capability stage and applicable lifecycle phase using `data-skill` markers.
- [x] Mirror ordering, links, descriptions, and counts in English.

### Task 3: Indexes, Roadmaps, and Language Entry Points

**Files:** Modify `skills-index.md`, both language README files, and both roadmaps; create `skills-index_EN.md`.

- [x] Apply the same primary classification and lifecycle vocabulary everywhere.
- [x] Add complete two-way language switching.
- [x] Remove stale planned status for delivered Skills.
- [x] Run the parity checker for drift and broken paths.

### Task 4: Core Maintained Documentation Mirrors

**Files:** Add English mirrors and two-way links for the active 2026-08-29 review, four-stage design and plan, plus `skills/DIRECTORY_GUIDE.md`, `skills/EXTERNAL_SNAPSHOT_POLICY.md`, `skills/SKILL_AUTHORING.md`, and `skills/SKILL_STYLE_GUIDE.md`.

- [x] Translate headings and normative prose while preserving commands, paths, counts, and safety boundaries.
- [x] Add two-way relative language links.
- [x] Run parity and whitespace validation.

### Task 5: Maintained Skill-Document Mirrors

**Files:** Add English mirrors for 20 Chinese-only quick-start/tutorial files under the matching `skills/en/testing-types/` paths. Do not add per-file language switches inside Skill packages.

- [x] Translate 15 quick-start documents while preserving executable commands and placeholders.
- [x] Translate five tutorials while preserving code semantics and expected results.
- [x] Verify representative same-relative-path mirrors and run the parity checker.

### Task 6: Final Verification and Delivery

**Files:** Only repair files owned by Tasks 1–5 if validation finds defects.

- [x] Prove the sorted Skill directory snapshot is unchanged.
- [x] Run checker unit tests, the real-repository bilingual checker, `bash scripts/check_skills_quality.sh`, and `git diff --check`.
- [x] Stage only plan-owned paths, commit with `docs(readme): add lifecycle navigation and bilingual parity`, push `explore`, and verify PR #4.
