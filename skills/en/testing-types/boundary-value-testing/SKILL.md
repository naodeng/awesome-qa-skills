---
name: boundary-value-testing
description: Use this skill when you need to select boundary and near-boundary candidates from sourced value, length, time, and resource constraints; triggers include boundary value test design.
---

# Boundary Value Test Design

select boundary and near-boundary candidates from sourced value, length, time, and resource constraints. Produce BVT-## findings. This Skill organizes traceable test-design candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need Boundary Value Test Design candidates from field schemas, minimum/maximum rules, inclusivity, units, time rules, resource limits, and defect history.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent rules, replace a complete strategy, or accept risk for a Human.

## How to Use

1. Read prompts/boundary-value-testing.md and provide the objective, scope, material, environment, and evidence.
2. Complete known, missing, conflicting, stale, out_of_scope, and assumptions before findings.
3. Record BVT-## with input domain, boundary value, neighboring value, inclusivity, unit, source evidence, impact, priority, and validation method, source, evidence state, impact, owner, close condition, and validation.
4. Preserve conflicts, unknown constraints, and open questions.

## Core Constraints

- without a source, do not invent thresholds, units, or neighbors, and do not turn a candidate into a product rule or pass.
- File presence, names, design declarations, and Eval configuration are not runtime evidence.
- Mark unknowns unassessed, blocked, or pending clarification instead of filling them with convention.
- Do not edit requirements, code, test assets, or target systems.

## Pre-delivery Check

- [ ] Recorded the six-part input audit.
- [ ] Every BVT-## has source, minimum evidence, impact/priority, owner role, close condition, and validation.
- [ ] Facts, inferences, recommendations, unexecuted work, and Human decisions remain separate.
- [ ] Findings are not full cases, execution results, coverage proof, or release claims.

## Reference Files

- Read evals/eval.yaml and matching cases for regression; configuration does not prove project results.
- Use evals/trigger-prompts.csv and evals/local-rules.json for trigger checks; missing skill.selection evidence is BLOCKED.
