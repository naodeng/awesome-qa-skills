---
name: decision-table-testing
description: Use this skill when you need to turn conditions, rules, actions, and outcomes into an auditable set of rule combinations; triggers include 决策表测试设计 and decision table test design.
---

# Decision Table Test Design

turn conditions, rules, actions, and outcomes into an auditable set of rule combinations. Produce DTT-## findings. This Skill organizes traceable test-design candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need Decision Table Test Design candidates from business rules, conditions, actions, exceptions, precedence, applicability, and existing test material.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent rules, replace a complete strategy, or accept risk for a Human.

## Output Format Options

- Use Markdown by default; use tables, JSON, or CSV only when explicitly requested or required by the delivery format.
- Separate static analysis, unexecuted work, evidence states, and Human decisions; keep items unassessed, blocked, or NOT_RUN when runtime evidence is absent.

## How to Use

1. Read prompts/decision-table-testing.md and provide the objective, scope, material, environment, and evidence.
2. Complete known, missing, conflicting, stale, out_of_scope, and assumptions before findings.
3. Record DTT-## with rule ID, condition combination, applicability, action/outcome, exception, source evidence, and validation method, source, evidence state, impact, owner, close condition, and validation.
4. Preserve conflicts, unknown constraints, and open questions.

## Core Constraints

- do not execute table rows, assume missing rules, or treat row counts as coverage proof.
- File presence, names, design declarations, and Eval configuration are not runtime evidence.
- Mark unknowns unassessed, blocked, or pending clarification instead of filling them with convention.
- Do not edit requirements, code, test assets, or target systems.

## Pre-delivery Check

- [ ] Recorded the six-part input audit.
- [ ] Every DTT-## has source, minimum evidence, impact/priority, owner role, close condition, and validation.
- [ ] Facts, inferences, recommendations, unexecuted work, and Human decisions remain separate.
- [ ] Findings are not full cases, execution results, coverage proof, or release claims.

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
