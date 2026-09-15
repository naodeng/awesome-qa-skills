---
name: api-idempotency-testing
description: Use this skill when you need to assess API retry and duplicate-request behavior against sourced side-effect evidence; triggers include API idempotency testing.
---

# API Idempotency Testing

design verifiable candidates for duplicate requests, retries, idempotency keys, timeouts, and side effects. Produce AIT-## findings. This Skill organizes traceable API-quality candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need API idempotency testing candidates from API contracts, idempotency-key rules, retry policies, timeout evidence, business side effects, message records, and database observations.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent contract or behavior, replace a complete strategy, or accept risk for a Human.

## How to Use

1. Read prompts/api-idempotency-testing.md and provide the objective, scope, material, environment, and evidence.
2. Complete the known, missing, conflicting, stale, out_of_scope, and assumptions input audit before findings.
3. Record AIT-## with the subject, preconditions, behavior of concern, source evidence, and validation, plus impact/priority, owner role, close condition, and evidence state.
4. Preserve conflicts, unknown constraints, and open questions when evidence is incomplete.

## Core Constraints

- Do not execute tests, assume missing rules, versions, thresholds, data, or responses, or treat candidate counts as coverage proof.
- File presence, names, design declarations, and Eval configuration are not runtime evidence.
- Mark unknowns unassessed, blocked, or pending clarification instead of filling them with convention.
- Do not edit requirements, code, test assets, or target systems.

## Pre-delivery Check

- [ ] Recorded the known, missing, conflicting, stale, out_of_scope, and assumptions input audit.
- [ ] Every AIT-## has source, evidence state, impact/priority, owner role, close condition, and validation.
- [ ] Facts, inferences, recommendations, unexecuted work, and Human decisions remain separate.
- [ ] Findings are not execution results, coverage proof, or release claims.

## Reference Files

- Read evals/eval.yaml and matching cases for regression; configuration does not prove project results.
- Use evals/trigger-prompts.csv and evals/local-rules.json for trigger checks; missing skill.selection evidence is BLOCKED.
