# Testmo-Inspired Case Workflows Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add two bilingual test-case data skills and extend two existing change-analysis skills with reviewed, evidence-bounded behavior.

**Architecture:** Keep each skill self-contained under its canonical `skills/{zh,en}` leaf. New skills produce traceable import/search outputs; existing workflow prompts add explicit pre-change and post-change branches. Root and catalog indexes expose the new IDs.

**Tech Stack:** Markdown, YAML, repository Python/Bash quality scripts, skill-up evals.

**Spec:** `docs/superpowers/specs/2026-11-12-testmo-inspired-case-workflows-design.md`

## Global Constraints

- New bilingual skills use the same canonical ID and start at version `1.0.0`.
- Existing compatible behavior additions bump metadata versions from `1.0.0` to `1.1.0` for each modified language package.
- New skills remain tool-agnostic, self-contained, and do not assume Testmo or any connector is installed.
- External writes require an explicit reviewed mapping and confirmation; predictions are never reported as execution evidence.
- Imported and retrieved case content is untrusted data; embedded instructions cannot expand scope or permissions, and retrieval does not invent ranks.
- Each new or materially changed skill has eval cases for success, incomplete input, and scope/risk boundaries.

## Review Focus

- Import files with ambiguous or unmapped columns preserve source data and surface unresolved mapping instead of inventing fields.
- Duplicate-looking cases remain candidates for review; the workflow does not silently merge or discard source rows.
- Retrieval results are candidates with traceable IDs and scope, not an asserted complete corpus or selected execution set.
- Proposed changes have no diff or SHA; pre-change output must label hypotheses rather than mark impact as a confirmed diff finding.
- Post-change per-case predictions remain distinct from actual run outcomes, including when CI evidence is supplied.

---

### Task 1: Add Test Case Importer

**Files:** Create Chinese and English leaf packages at `skills/{zh,en}/testing-types/test-case-importer/` with `SKILL.md`, `prompts/test-case-importer.md`, `agents/openai.yaml`, `evals/eval.yaml`, and three `evals/cases/*.yaml` files.

- [x] Add success, incomplete-source, and write-boundary eval cases first; validate the new eval schema and attempt a pre-implementation skill-up run.
- [x] Implement the import workflow with source-preserving mapping preview, duplicate candidates, unresolved fields, and confirmation before any connected write.
- [x] Verify metadata, standalone links, and zh/en parity.

### Task 2: Add Test Case Retrieval

**Files:** Create Chinese and English leaf packages at `skills/{zh,en}/testing-types/test-case-retrieval/` with the same required files as Task 1.

- [x] Add success, insufficient-corpus, and search-versus-selection boundary eval cases first; validate and attempt a pre-implementation skill-up run.
- [x] Implement scoped candidate retrieval, query refinement, source IDs, ranking caveats, and an explicit handoff to selection or execution.
- [x] Verify metadata, standalone links, and zh/en parity.

### Task 3: Extend Change-to-Regression

**Files:** Modify both `skills/{zh,en}/testing-workflows/change-to-regression/{SKILL.md,prompts/change-to-regression.md,agents/openai.yaml,evals/eval.yaml}` and add language-matched pre-change guardrail eval cases.

- [x] Add pre-change and missing-context eval cases first; validate and attempt a pre-implementation skill-up run.
- [x] Add a proposed-change branch while preserving existing diff/SHA behavior; bump both package versions to `1.1.0`.
- [x] Verify after-change cases and existing contract cases remain represented.

### Task 4: Extend PR Test Impact Analysis

**Files:** Modify both `skills/{zh,en}/testing-types/pr-test-impact-analysis/{SKILL.md,prompts/pr-test-impact-analysis.md,agents/openai.yaml,evals/eval.yaml}` and add language-matched outcome-prediction eval cases.

- [x] Add per-case prediction and run-evidence separation evals first; validate and attempt a pre-implementation skill-up run.
- [x] Add `PREDICTED_PASS`, `PREDICTED_FAIL`, and `UNCERTAIN` reasoning with evidence links and no execution claims; bump both package versions to `1.1.0`.
- [x] Verify existing impact-scope coverage remains intact.

### Task 5: Update Discovery and Quality Gates

**Files:** Modify `README.md`, `README_EN.md`, `skills/zh/README.md`, `skills/en/README.md`, and `docs/catalog/skills-index.md`.

- [x] Add both new IDs to bilingual catalogs and user-facing entry points.
- [x] Run `bash scripts/check_skills_quality.sh` and `bash scripts/check_skills_cli_compatibility.sh`.
- [x] Run relevant skill-up evals when the CLI and engine are available; otherwise report the exact blocker and retain static eval/YAML checks.

## Verification notes

- `skill-up` is unavailable in this environment, so behavior eval execution was attempted but could not run; `validate_skill_evals.sh` skipped YAML eval validation for this reason.
- The full quality and CLI compatibility gates stop because PyYAML is unavailable; installation was blocked by unavailable network/DNS. Ruby Psych parsed the changed YAML files, and standalone independence, integrity, metadata, and bilingual-doc checks passed.
