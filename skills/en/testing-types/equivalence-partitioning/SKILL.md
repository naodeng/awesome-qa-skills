---
name: equivalence-partitioning
description: Use this skill when you need to partition inputs into evidence-backed valid, invalid, and unknown classes based on constraints, rules, and response differences; triggers include equivalence partitioning test design.
---

# Equivalence Partitioning Test Design

partition inputs into evidence-backed valid, invalid, and unknown classes based on constraints, rules, and response differences. Produce EP-## findings. This Skill organizes traceable test-design candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need Equivalence Partitioning Test Design candidates from input constraints, field types, business rules, role/state differences, error contracts, and existing cases.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent rules, replace a complete strategy, or accept risk for a Human.

## How to Use

1. Read prompts/equivalence-partitioning.md and provide the objective, scope, material, environment, and evidence.
2. Complete known, missing, conflicting, stale, out_of_scope, and assumptions before findings.
3. Record EP-## with equivalence class, partition rationale, representative value, valid/invalid state, source evidence, expected concern, and validation method, source, evidence state, impact, owner, close condition, and validation.
4. Preserve conflicts, unknown constraints, and open questions.

## Core Constraints

- do not merge classes from similar field names, invent error codes or rules, or treat one representative per class as full coverage.
- File presence, names, design declarations, and Eval configuration are not runtime evidence.
- Mark unknowns unassessed, blocked, or pending clarification instead of filling them with convention.
- Do not edit requirements, code, test assets, or target systems.

## Pre-delivery Check

- [ ] Recorded the six-part input audit.
- [ ] Every EP-## has source, minimum evidence, impact/priority, owner role, close condition, and validation.
- [ ] Facts, inferences, recommendations, unexecuted work, and Human decisions remain separate.
- [ ] Findings are not full cases, execution results, coverage proof, or release claims.

## Reference Files

- Read evals/eval.yaml and matching cases for regression; configuration does not prove project results.
- Use evals/trigger-prompts.csv and evals/local-rules.json for trigger checks; missing skill.selection evidence is BLOCKED.
