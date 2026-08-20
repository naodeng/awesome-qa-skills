# Skill Governance Capabilities Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add three independently installable bilingual Skill Engineering Skills inspired by `deepseek-harness/.agents/skills`: prose contract review, change verification, and prose trimming.

**Architecture:** Add mirrored English/Chinese Skill directories under `skills/{zh,en}/skill-engineering/`. Each Skill owns its `SKILL.md`, copy-ready prompt, OpenAI metadata, and three minimum Eval cases. Keep the Skills generic and repository-independent; use current repository validators and indexes only for integration checks.

**Tech Stack:** Markdown, YAML, existing repository shell/Python quality scripts, skill-up validation.

---

### Task 1: Establish the new skill-engineering category and repository integration points

**Files:**
- Create: `skills/zh/skill-engineering/.gitkeep` only if the repository requires an explicit category marker; otherwise create the first Skill directory directly.
- Modify: `skills-index.md` if the index has a category table that requires the new category.
- Modify: `skills/zh/README.md` and `skills/en/README.md` only where the existing index structure requires the new category.
- Test: repository discovery and quality scripts.

- [ ] **Step 1: Inspect existing category/index conventions**

Run:

```bash
rg -n "testing-workflows|testing-types|category|skill-engineering" skills-index.md skills/zh/README.md skills/en/README.md README.md scripts
```

Expected: identify the smallest set of index files that must mention `skill-engineering`; do not add a new index section if the generators discover directories automatically.

- [ ] **Step 2: Add only required category integration**

Use the existing wording and ordering conventions. Do not add a second source tree under `.agents/skills/`.

- [ ] **Step 3: Run discovery-only validation**

Run:

```bash
python3 scripts/organize_project_dirs.py
```

Expected: exit 0 and no unrelated file movement.

### Task 2: Add bilingual `skill-prose-review`

**Files:**
- Create: `skills/zh/skill-engineering/skill-prose-review/SKILL.md`
- Create: `skills/zh/skill-engineering/skill-prose-review/prompts/skill-prose-review.md`
- Create: `skills/zh/skill-engineering/skill-prose-review/agents/openai.yaml`
- Create: `skills/zh/skill-engineering/skill-prose-review/evals/eval.yaml`
- Create: `skills/zh/skill-engineering/skill-prose-review/evals/cases/basic-success.yaml`
- Create: `skills/zh/skill-engineering/skill-prose-review/evals/cases/edge-incomplete-input.yaml`
- Create: `skills/zh/skill-engineering/skill-prose-review/evals/cases/edge-scope-risk.yaml`
- Create: matching files under `skills/en/skill-engineering/skill-prose-review/`

- [ ] **Step 1: Define the contract in the Chinese prompt**

The prompt must require: target scope, document role, contract chain, findings with severity/evidence/location, missing information, and a final claim boundary. It must not rewrite files unless explicitly requested.

- [ ] **Step 2: Mirror the contract in English**

Preserve semantics and output fields. Keep terminology aligned with the repository's existing bilingual conventions.

- [ ] **Step 3: Add frontmatter and metadata**

Use the same lowercase hyphenated key `skill-prose-review` in `SKILL.md` and `agents/openai.yaml`. The description must include both English and Chinese trigger phrases.

- [ ] **Step 4: Add three Evals per language**

Cover complete input, missing context, and unsafe scope/cross-Skill dependency. Assertions must check observable output behavior rather than prose similarity.

- [ ] **Step 5: Validate the new Skill structurally**

Run the repository's focused Skill integrity and Eval validation commands. Expected: no metadata, independence, or missing-eval findings for this Skill.

### Task 3: Add bilingual `skill-change-verification`

**Files:**
- Create: `skills/zh/skill-engineering/skill-change-verification/SKILL.md`
- Create: `skills/zh/skill-engineering/skill-change-verification/prompts/skill-change-verification.md`
- Create: `skills/zh/skill-engineering/skill-change-verification/agents/openai.yaml`
- Create: `skills/zh/skill-engineering/skill-change-verification/evals/eval.yaml`
- Create: three Eval case files under the Chinese directory
- Create: matching files under `skills/en/skill-engineering/skill-change-verification/`

- [ ] **Step 1: Define the verification evidence model**

The prompt must distinguish Static, Structural, Evaluation, Runtime, and Human review evidence. It must report executed commands, omitted checks with reasons, residual risks, and allowed claims.

- [ ] **Step 2: Define change-to-check routing**

Cover content-only, metadata/structure, script, Eval, and runtime-affecting changes. When commands cannot be discovered, require an explicit unknown/confirmation item instead of guessing.

- [ ] **Step 3: Add bilingual metadata and Evals**

Use key `skill-change-verification`. Cases must include a successful routing, incomplete environment, and a case where static validation must not be reported as runtime proof.

- [ ] **Step 4: Run focused validation**

Expected: both language directories pass integrity and Eval discovery checks.

### Task 4: Add bilingual `skill-prose-trim`

**Files:**
- Create: `skills/zh/skill-engineering/skill-prose-trim/SKILL.md`
- Create: `skills/zh/skill-engineering/skill-prose-trim/prompts/skill-prose-trim.md`
- Create: `skills/zh/skill-engineering/skill-prose-trim/agents/openai.yaml`
- Create: `skills/zh/skill-engineering/skill-prose-trim/evals/eval.yaml`
- Create: three Eval case files under the Chinese directory
- Create: matching files under `skills/en/skill-engineering/skill-prose-trim/`

- [ ] **Step 1: Define safe trimming rules**

Preserve contracts, negative guarantees, measured bounds, formal references, archived records, and fixture fidelity. Remove or restate unresolvable design-session and reviewer-addressed prose.

- [ ] **Step 2: Define no-overreach behavior**

The Skill must ask for or report a scope boundary when the target includes generated files, sealed archives, bilingual counterparts, or unrelated code.

- [ ] **Step 3: Add bilingual metadata and Evals**

Use key `skill-prose-trim`. Cases must cover a safe rewrite, missing scope, and preservation of a durable contract or archived record.

- [ ] **Step 4: Run focused validation**

Expected: both language directories pass integrity and Eval discovery checks.

### Task 5: Synchronize indexes and verify all three Skills

**Files:**
- Modify: only the repository indexes required by the discovery conventions identified in Task 1.
- Test: all three new Skill directories and the full repository quality gate.

- [ ] **Step 1: Verify bilingual pairing and independence**

Run:

```bash
python3 scripts/validate_agents_metadata.py
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
python3 scripts/validate_skills_integrity.py --fail-on-findings
```

Expected: exit 0 with no findings attributable to the new category.

- [ ] **Step 2: Validate Evals**

Run the repository's Eval validator and, if available, `skill-up validate` for all six language-specific Skill directories. Report static validation separately from runtime execution.

- [ ] **Step 3: Run the complete quality gate**

```bash
bash scripts/check_skills_quality.sh
git diff --check
rg -n 'TBD|TODO|<[^>]+>' skills/zh/skill-engineering skills/en/skill-engineering
```

Expected: all commands pass; the placeholder scan returns no unintended placeholders.

- [ ] **Step 4: Review scope and dirty-worktree safety**

Run `git status --short` and confirm only the design/plan files, the new `skill-engineering` files, and required indexes changed. Preserve all unrelated existing changes.
