<div align="right"><a href="./2026-08-29-four-stage-qa-skills-evolution.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Four-Stage QA Skills Evolution Implementation Plan

> Historical execution record. All six iterations are complete. The Chinese counterpart retains the full step-by-step record; this mirror preserves scope, sequence, boundaries, validation, and delivery decisions.

**Goal:** Evolve the catalog from Core QA through Engineering QA, Production Quality, and AI Native QA without changing existing Skill directories.

**Architecture:** Physical directories remain the installation contract. Every addition is a self-contained bilingual package with entry instructions, a primary prompt, OpenAI metadata, and three evaluation categories.

**Spec:** `docs/superpowers/specs/2026-08-29-four-stage-qa-skills-evolution-design_EN.md`

## Global Constraints

- Do not move or rename existing Skill directories.
- Use identical package names and equivalent boundaries in Chinese and English.
- Keep every package independently installable.
- Include success, incomplete-input, and risk-boundary evals.
- Adapt Prompt Baseline quality rules without importing external repository structure.

## Execution Sequence

### 1. Capability Navigation Foundation

Update root README files, the full index, language indexes, directory guidance, roadmaps, and `discover-testing`. Capability stages are navigation; physical paths remain the installation interface.

### 2. Shift Left

Add `acceptance-criteria-review`, `requirement-gap-analysis`, `quality-risk-analysis`, and `testability-analysis`, with distinct inputs and deliverables.

### 3. Change Intelligence

Add `change-impact-analysis`, `pr-test-impact-analysis`, `regression-scope-analysis`, and `regression-test-selection`. Their outputs form a traceable chain from change to executable regression set.

### 4. Execution Intelligence

Add `test-data-generation`, `api-contract-testing`, `flaky-test-analysis`, `root-cause-analysis`, and `log-analysis`. Separate confirmed evidence from hypotheses and never claim unsupported causes.

### 5. Performance Engineering

Add workload modeling, result analysis, bottleneck analysis, regression analysis, and capacity planning. State workload and environment assumptions and avoid invented thresholds.

### 6. Production Quality

Add production verification, incident analysis, distributed trace analysis, and metric anomaly analysis. Require least privilege, safe verification, stop conditions, rollback awareness, and Human Task boundaries.

### 7. AI Native QA

Add AI feature testing, LLM testing, evaluation design, prompt testing, agent testing, tool-call testing, and prompt-injection testing. Separate model quality, prompts, trajectories, tool contracts, evaluation, and adversarial safety.

## Validation

```bash
bash scripts/check_skills_quality.sh
git diff --check
```

Expected result:

- 156 Skills scanned
- 0 metadata, independence, integrity, or snapshot findings
- 156 valid skill-up YAML definitions
- complete bilingual package pairing

## Delivery

The work was delivered through scoped commits on `explore`, while unrelated working-tree changes remained excluded.
