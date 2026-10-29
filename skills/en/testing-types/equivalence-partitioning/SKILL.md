---
name: equivalence-partitioning
description: Use this skill when you need to partition inputs into evidence-backed valid, invalid, and unknown classes based on constraints, rules, and response differences; triggers include 等价类划分 and equivalence partitioning test design.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Equivalence Partitioning Test Design

partition inputs into evidence-backed valid, invalid, and unknown classes based on constraints, rules, and response differences. Produce EP-## findings. This Skill organizes traceable test-design candidates only; it does not execute tests or turn a design inventory into coverage, pass, or release evidence.

## When to Use

- When you need Equivalence Partitioning Test Design candidates from input constraints, field types, business rules, role/state differences, error contracts, and existing cases.
- When you need selection rationale, applicability constraints, evidence gaps, and the smallest validation action.
- When inputs are incomplete but a bounded first pass can preserve blocked or unassessed boundaries.

Do not use it to execute tests, invent rules, replace a complete strategy, or accept risk for a Human.

## Output Format Options

- Use Markdown by default; use tables, JSON, or CSV only when explicitly requested or required by the delivery format.
- Separate static analysis, unexecuted work, evidence states, and Human decisions; keep items unassessed, blocked, or NOT_RUN when runtime evidence is absent.

## How to Use

1. Read prompts/equivalence-partitioning.md and provide the objective, scope, material, environment, and evidence.
2. Complete known, missing, conflicting, stale, out_of_scope, and assumptions before findings.
3. Record EP-## with equivalence class, partition rationale, representative value, valid/invalid state, source evidence, expected concern, and validation method, source, evidence state, impact, owner, close condition, and validation.
4. Preserve conflicts, unknown constraints, and open questions.

## Domain Execution Essentials

- Partition by sourced equivalent behavior/errors and constraints, not input shape alone; invalid classes with different responses must remain distinct.
- Deliver joint partitions, behavioral oracles and representatives, with disjointness/completeness scope and unknown classes; retain conditional validity.
- When deriving domain candidates, read and follow [prompts/equivalence-partitioning.md](prompts/equivalence-partitioning.md) for the domain procedure and oracle; retain valid controls, evidence gaps, and validation actions for each item.

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

## Common Pitfalls

- Do not turn a method name, file presence, or candidate count into test execution, coverage, pass, or release evidence when scope or evidence is incomplete.
- Do not fill in missing rules, thresholds, data, environments, or results from convention; preserve unassessed, blocked, and pending items.
- Do not expand this specialist design or review into a complete strategy, full test cases, runtime execution, or a release decision.

## Best Practices

- Complete the six-part input audit before selecting the smallest traceable and verifiable finding scope.
- Keep the source, evidence state, impact/priority, owner role, close condition, validation method, and residual risk for every finding.
- Write validation suggestions as next actions; do not upgrade package structure, candidate counts, or local Eval configuration into real quality conclusions.
