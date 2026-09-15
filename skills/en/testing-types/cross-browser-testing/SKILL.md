---
name: cross-browser-testing
description: Use this skill when you need to select evidence-backed browser, engine, device, and version coverage; triggers include cross-browser testing.
---

# Cross-Browser Testing

select compatibility coverage from user distribution, browser engines, versions, devices, and known-defect evidence. Produce CBT-## findings. This Skill organizes traceable browser-compatibility quality candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need cross-browser testing candidates from browser and device support matrices, user distribution, engine versions, rendering differences, known defects, CI capacity, and environment limits.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent behavior conclusions, replace a complete strategy, or accept risk for a Human.

## Output Format Options

- Use Markdown by default; use tables, JSON, or CSV only when explicitly requested or required by the delivery format.
- Separate static analysis, unexecuted work, evidence states, and Human decisions; keep items unassessed, blocked, or NOT_RUN when runtime evidence is absent.

## How to Use

1. Read prompts/cross-browser-testing.md and provide the objective, scope, material, environment, and evidence.
2. Complete the known, missing, conflicting, stale, out_of_scope, and assumptions input audit before findings.
3. Record CBT-## with the subject, preconditions, concern, source evidence, and validation, plus impact/priority, owner role, close condition, and evidence state.
4. Preserve conflicts, unknown constraints, and open questions when evidence is incomplete.

## Core Constraints

- Do not execute tests, assume missing rules, versions, thresholds, data, or outcomes, or treat candidate counts as coverage proof.
- File presence, names, design declarations, and Eval configuration are not runtime evidence.
- Mark unknowns unassessed, blocked, or pending clarification instead of filling them with convention.
- Do not edit requirements, code, test assets, or target systems.

## Pre-delivery Check

- [ ] Recorded the known, missing, conflicting, stale, out_of_scope, and assumptions input audit.
- [ ] Every CBT-## has source, evidence state, impact/priority, owner role, close condition, and validation.
- [ ] Facts, inferences, recommendations, unexecuted work, and Human decisions remain separate.
- [ ] Findings are not execution results, coverage proof, or release claims.

## Reference Files

- Read evals/eval.yaml and matching cases for regression; configuration does not prove project results.
- Use evals/trigger-prompts.csv and evals/local-rules.json for trigger checks; missing skill.selection evidence is BLOCKED.

## Common Pitfalls

- Do not turn a method name, file presence, or candidate count into test execution, coverage, pass, or release evidence when scope or evidence is incomplete.
- Do not fill in missing rules, thresholds, data, environments, or results from convention; preserve unassessed, blocked, and pending items.
- Do not expand this specialist design or review into a complete strategy, full test cases, runtime execution, or a release decision.

## Best Practices

- Complete the six-part input audit before selecting the smallest traceable and verifiable finding scope.
- Keep the source, evidence state, impact/priority, owner role, close condition, validation method, and residual risk for every finding.
- Write validation suggestions as next actions; do not upgrade package structure, candidate counts, or local Eval configuration into real quality conclusions.
