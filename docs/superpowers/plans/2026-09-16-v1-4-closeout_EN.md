<div align="right"><a href="./2026-09-16-v1-4-closeout.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.4 Governance and Release Closeout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete every v1.4 card in Project #4 in one delivery, including repository artifacts, evidence closeout, and Project state synchronization, without starting v1.5–v1.8 early.

**Architecture:** A JSON-compatible YAML contract records the v1.4 cards and their evidence. A Python standard-library generator renders bilingual Phase 0 closeout and v1.0/v1.4 Release DoD views. The existing Registry, Matrix, Inventory, README, Catalog, Lifecycle, Deprecation, Quality Gate, and installation documents remain evidence sources, with static, structural, Eval-execution, and release-approval states kept separate.

**Tech Stack:** Python 3 standard library, JSON-compatible YAML, Markdown, `unittest`, the existing repository quality gate, and the GitHub Project CLI.

**Spec:** `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`, `docs/governance/SKILL_GOVERNANCE_V1.md`, `docs/SKILL_MATCHING_GUIDE.md`, `docs/SKILL_LIFECYCLE.md`, `docs/SKILL_DEPRECATION_GUIDE.md`, `docs/SKILL_QUALITY_GATE.md`, `docs/governance/DOCUMENTATION_POLICY.md`, and the v1.4 cards in Project #4.

## Global Constraints

- v1.4 covers only the 35 Project #4 cards whose target version is `v1.4`; v1.5, v1.6, v1.7, and v1.8 are not moved or implemented early.
- Governance cards must not create duplicate physical Skills; `MATCH`, `MERGE`, `ENHANCE`, and `EXISTING` conclusions do not authorize creating, deleting, or renaming directories.
- Preserve `NOT_SCORED`, `NOT_RUN`, `UNASSESSED`, `BLOCKED`, and `N/A`; static checks are not runtime effectiveness, model Eval, business acceptance, or release approval.
- All current project governance documents keep Chinese/English mirrors; generated views are changed through their generator and source, not by hand.
- External Project changes move only v1.4 cards; do not create repository Issues, commit, push, or publish a Release.
- Preserve all prior v1.4 work in the current worktree; do not overwrite or revert unrelated files.

---

### Task 1: Establish the v1.4 closeout contract

**Files:**
- Create: `docs/governance/v1-4-closeout.yaml`
- Create: `scripts/generate_v14_closeout.py`
- Create: `scripts/tests/test_v14_closeout.py`
- Modify: `scripts/check_skills_quality.sh`

**Interfaces:**
- `load_contract(path: Path) -> CloseoutContract`
- `validate_contract(contract: CloseoutContract, root: Path) -> list[str]`
- `render_closeout(contract: CloseoutContract, locale: str, root: Path) -> str`
- `render_release_dod(contract: CloseoutContract, version: str, locale: str, root: Path) -> str`
- `--check` fails when any generated v1.4 view is stale or any evidence path is missing.

- [x] **Step 1: Write failing contract tests.** Assert exactly 35 unique v1.4 cards, all P0, 20 mapping cards, both already-Done cards, all remaining titles, and repository-existing evidence paths.
- [x] **Step 2: Run the focused tests and confirm that the new contract module is missing.**

```bash
python3 -m unittest scripts.tests.test_v14_closeout -v
```

- [x] **Step 3: Add the JSON-compatible YAML contract.** Record each card title, Project item id, kind, evidence paths, acceptance state, explicit static/runtime/model/release boundaries, exact counts, and the next-version rule.
- [x] **Step 4: Implement parsing, validation, deterministic bilingual rendering, and `--check`.** Reject duplicate titles/IDs, non-v1.4 cards, invalid kinds/states, missing evidence, missing language mirrors, and claims that promote `NOT_RUN` or `UNASSESSED` to pass.
- [x] **Step 5: Integrate the v1.4 generator check into `scripts/check_skills_quality.sh` and run focused tests.**

### Task 2: Complete lifecycle, deprecation, bilingual, Quality Score, and Eval contracts

**Files:**
- Modify: `docs/SKILL_DEPRECATION_GUIDE.md`, `docs/SKILL_DEPRECATION_GUIDE_EN.md`
- Modify: `docs/SKILL_LIFECYCLE.md`, `docs/SKILL_LIFECYCLE_EN.md`
- Modify: `docs/SKILL_QUALITY_GATE.md`, `docs/SKILL_QUALITY_GATE_EN.md`
- Modify: `docs/governance/DOCUMENTATION_POLICY.md`, `docs/governance/DOCUMENTATION_POLICY_EN.md`
- Create: `docs/governance/DEPRECATION_DECISION_CONTRACT.md`, `docs/governance/DEPRECATION_DECISION_CONTRACT_EN.md`
- Create: `docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md`, `docs/governance/BILINGUAL_CONSISTENCY_CONTRACT_EN.md`
- Create: `docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md`, `docs/governance/QUALITY_SCORE_EVAL_CONTRACT_EN.md`
- Modify: `scripts/check_docs_bilingual.py`
- Modify: `scripts/tests/test_v14_closeout.py`

- [x] **Step 1: Add tests for controlled vocabularies and evidence boundaries.** Cover deprecation states, replacement/retained-boundary/migration fields, the nine Quality Score dimensions, three minimum Eval case classes, and bilingual mirror requirements.
- [x] **Step 2: Document deprecation as a reversible, evidence-backed proposal.** Define `Deprecated` versus `Archived`, required replacement and migration fields, Matrix/Catalog/README/Workflow propagation, and the rule that deprecation cannot hide an unverified match.
- [x] **Step 3: Document the bilingual contract.** Define paired paths, top-level switches, maintained Skill files, catalog parity, generated-output exceptions, and the exact repository checks.
- [x] **Step 4: Document Quality Score and minimum Eval without inventing scores.** Keep the nine dimensions and thresholds, require three case classes for changed/new packages, and state `NOT_SCORED`/`NOT_RUN` when no real evaluation ran.
- [x] **Step 5: Register the new bilingual contracts in the documentation checker and pass focused tests.**

### Task 3: Synchronize README, Catalog, Graph, and Workflow/Eval installation guidance

**Files:**
- Modify: `README.md`, `README_EN.md`
- Modify: `docs/catalog/skills-index.md`, `docs/catalog/skills-index_EN.md`
- Modify: `docs/catalog/skills-graph.md`, `docs/catalog/skills-graph_EN.md`
- Modify: `scripts/INSTALL_SKILLS.md`
- Create: `docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md`, `docs/governance/WORKFLOW_EVAL_INSTALL_SYNC_EN.md`
- Modify: `scripts/check_docs_bilingual.py`
- Modify: `scripts/tests/test_v14_closeout.py`

- [x] **Step 1: Add tests for governance entrypoint links and ten workflow installation/Eval rows.** Verify both language documents point to the same physical workflow directories and commands.
- [x] **Step 2: Add v1.4 governance navigation to both READMEs, the full index, and the graph.** Label governance artifacts as source/structure evidence, not runtime-quality proof.
- [x] **Step 3: Add a bilingual Workflow/Eval installation synchronization checklist.** Cover all ten workflows, root installers, per-Skill installers, `npx skills`, dry-run behavior, language selection, and minimum Eval structure.
- [x] **Step 4: Update `scripts/INSTALL_SKILLS.md` with the checklist link and run link/parity tests.**

### Task 4: Publish the Enhancement Sprint, candidate 15-step template, and Shift Left milestone

**Files:**
- Create: `docs/governance/ENHANCEMENT_SPRINT.md`, `docs/governance/ENHANCEMENT_SPRINT_EN.md`
- Create: `docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE.md`, `docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE_EN.md`
- Create: `docs/governance/SHIFT_LEFT_MILESTONE.md`, `docs/governance/SHIFT_LEFT_MILESTONE_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`, `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`
- Modify: `docs/catalog/skills-graph.md`, `docs/catalog/skills-graph_EN.md`

- [x] **Step 1: Define Enhancement Sprint cadence.** Require one enhancement/merge/Eval sprint after every two or three New sprints and list prompt, scope, non-goal, Eval, bilingual, workflow, Matrix, README, and deprecation checks.
- [x] **Step 2: Define the exact 15-step candidate execution template.** Keep Match before New/Enhance/Merge, include human decisions and release/observation/re-evaluation boundaries, and provide a copyable checklist.
- [x] **Step 3: Define the v1.1–v1.4 Shift Left milestone.** Map requirements, impact, risk, regression, performance, production, AI, and governance evidence to current physical Skills/workflows without aliases.
- [x] **Step 4: Add reciprocal navigation and run bilingual/link checks.**

### Task 5: Generate Phase 0 review and v1.0/v1.4 Release DoD views

**Files:**
- Create: `docs/governance/PHASE_0_V1_4_CLOSEOUT.md`, `docs/governance/PHASE_0_V1_4_CLOSEOUT_EN.md`
- Create: `docs/governance/RELEASE_DOD_V1_0.md`, `docs/governance/RELEASE_DOD_V1_0_EN.md`
- Create: `docs/governance/RELEASE_DOD_V1_4.md`, `docs/governance/RELEASE_DOD_V1_4_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_V1.md`, `docs/governance/SKILL_GOVERNANCE_V1_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`, `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [x] **Step 1: Generate a 35-card closeout table from the contract.** Show Project id/title, evidence, acceptance state, and whether the item is governance, mapping, or DoD.
- [x] **Step 2: Generate separate v1.0 and v1.4 DoD views.** Mark repository/static gates as verified, real-model/real-target Eval as `NOT_RUN`, external release/push/approval as `N/A` or `NOT_RUN`, and list remaining risks.
- [x] **Step 3: Add current-state and follow-up links to governance baseline/roadmap docs.** State that v1.5–v1.8 remain scheduled and untouched.
- [x] **Step 4: Regenerate and test all v1.4 views.**

### Task 6: Close all 20 mapping cards against the Registry review ledger

**Files:**
- Modify: `docs/governance/skill-governance-registry.yaml`
- Modify: `scripts/generate_skill_governance_matrix.py`
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`
- Modify: generated Matrix/Register/review views as needed

- [x] **Step 1: Verify the exact 20-card mapping set against the 20 `match_reviews` records.** Require title-to-candidate mapping, target, conclusion, evidence paths, and action to agree.
- [x] **Step 2: Preserve the current evidence boundary.** Do not turn any mapping card into a physical Skill implementation, semantic-equivalence claim, runtime result, model Eval, or release approval.
- [x] **Step 3: Run mapping tests and generated-view freshness checks.**

### Task 7: Final verification and Project #4 batch transition

**Files:**
- Modify: `docs/superpowers/plans/2026-09-16-v1-4-closeout.md`
- External state: the 33 remaining v1.4 cards in Project #4.

- [x] **Step 1: Run focused tests, the full quality gate, generated-view checks, bilingual/link checks, and `git diff --check`.**
- [x] **Step 2: Confirm that no `skills/` directory was added, removed, renamed, or modified by this closeout; inspect exact working-tree scope.**
- [x] **Step 3: Resolve the Project #4 Status field/options live, re-read all v1.4 cards, then move only the 33 remaining `In Progress` cards to `Done`.**
- [x] **Step 4: Re-read Project #4 and verify exactly 35 `Done`, 0 `In Progress`, 0 `Todo` for v1.4; keep Draft markers unchanged and v1.5–v1.8 untouched.**
- [x] **Step 5: Run final checks after the plan update and report no commit/push/release unless separately requested.**

## Plan self-review

- The contract and generator make every Project transition traceable without relying on a hand-written “all done” statement.
- Existing source-governance evidence remains distinct from runtime, model, semantic, business, and release evidence.
- All new reader-facing documents have Chinese/English mirrors and are included in repository link/parity checks.
- The physical Skill tree is intentionally unchanged; this v1.4 closeout completes governance and cleanup cards, not future v1.5–v1.8 package creation.
