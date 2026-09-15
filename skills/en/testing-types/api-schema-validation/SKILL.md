---
name: api-schema-validation
description: Use this skill when you need to compare API schemas with sourced request and response evidence; triggers include API schema validation.
---

# API Schema Validation

compare API schema constraints with sourced request, response, and version evidence. Produce ASV-## findings. This Skill organizes traceable API-quality candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need API schema validation candidates from OpenAPI, JSON Schema, GraphQL schemas, endpoint inventories, request-response samples, versions, and validation reports.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent contract or behavior, replace a complete strategy, or accept risk for a Human.

## How to Use

1. Read prompts/api-schema-validation.md and provide the objective, scope, material, environment, and evidence.
2. Complete the known, missing, conflicting, stale, out_of_scope, and assumptions input audit before findings.
3. Record ASV-## with the subject, preconditions, behavior of concern, source evidence, and validation, plus impact/priority, owner role, close condition, and evidence state.
4. Preserve conflicts, unknown constraints, and open questions when evidence is incomplete.

## Core Constraints

- Do not execute tests, assume missing rules, versions, thresholds, data, or responses, or treat candidate counts as coverage proof.
- File presence, names, design declarations, and Eval configuration are not runtime evidence.
- Mark unknowns unassessed, blocked, or pending clarification instead of filling them with convention.
- Do not edit requirements, code, test assets, or target systems.

## Pre-delivery Check

- [ ] Recorded the known, missing, conflicting, stale, out_of_scope, and assumptions input audit.
- [ ] Every ASV-## has source, evidence state, impact/priority, owner role, close condition, and validation.
- [ ] Facts, inferences, recommendations, unexecuted work, and Human decisions remain separate.
- [ ] Findings are not execution results, coverage proof, or release claims.

## Reference Files

- Read evals/eval.yaml and matching cases for regression; configuration does not prove project results.
- Use evals/trigger-prompts.csv and evals/local-rules.json for trigger checks; missing skill.selection evidence is BLOCKED.
