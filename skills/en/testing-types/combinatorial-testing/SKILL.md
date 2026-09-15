---
name: combinatorial-testing
description: Use this skill when you need to select high-risk multi-factor combinations after factors, values, and constraints are explicit; triggers include 组合测试 and combinatorial test design.
---

# Combinatorial Test Design

Select high-risk multi-factor combinations after factors, values, and constraints are explicit. Produce CT-## design candidates within the evidence boundary; do not execute tests or claim coverage or pass results.

## When to Use

- Analyze factors, values, combination constraints, interaction risk, and existing combinations.
- Preserve selection rationale, evidence gaps, priority, and validation actions.
- Inputs are incomplete but a bounded first pass can mark items unassessed or blocked.

## Output Format Options

- Use Markdown by default; use tables, JSON, or CSV only when explicitly requested or required by the delivery format.
- Separate static analysis, unexecuted work, evidence states, and Human decisions; keep items unassessed, blocked, or NOT_RUN when runtime evidence is absent.

## How to Use

1. Read `prompts/combinatorial-testing.md` and provide the objective, scope, material, environment, and evidence.
2. Start with separate known, missing, conflicting, stale, out_of_scope, and assumptions entries.
3. Produce CT-## findings with source, evidence state, applicability, impact/priority, owner, close condition, and validation.
4. Separate facts, evidence-backed inferences, recommendations, and Human decisions.
5. Recommend follow-up validation without claiming execution.

## Core Constraints

- Do not turn combination counts into coverage proof, ignore constraints, or invent values from experience.
- File presence, names, templates, and Eval configuration are not runtime evidence.
- Do not edit requirements, code, test assets, or target systems, or accept risk for a Human.

## Pre-delivery Check

- [ ] The six-part input audit is complete.
- [ ] Every CT-## has source, evidence state, applicability, concern, impact/priority, owner, close condition, and validation.
- [ ] Facts, inferences, recommendations, and Human decisions are separate.
- [ ] Unexecuted, unverified, unassessed, and pending-decision items are explicit.

## Reference Files

- Read evals/eval.yaml and matching cases for regression; configuration does not prove project results.
- Use evals/trigger-prompts.csv and evals/local-rules.json for trigger checks; missing skill.selection evidence is BLOCKED.

## Common Pitfalls

- Do not treat a method name, file presence, or candidate count as execution, coverage, pass, or release evidence.
- Do not fill missing rules, constraints, values, or results with convention; preserve unassessed, blocked, and pending items.
- Do not expand this specialist design into a complete strategy, full test cases, runtime execution, or a release decision.

## Best Practices

- Complete the six-part input audit before selecting the smallest traceable and verifiable finding scope.
- Keep the source, evidence state, impact/priority, owner role, close condition, validation method, and residual risk for every finding.
- Write validation suggestions as next actions; do not upgrade package structure, candidate counts, or local Eval configuration into real quality conclusions.
