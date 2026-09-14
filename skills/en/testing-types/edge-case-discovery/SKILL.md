---
name: edge-case-discovery
description: Use this skill when you need to discover boundary, rare, limit, ordering, or combination scenarios from product and test evidence; triggers include edge case discovery.
---

# Edge Case Discovery

Discover boundary candidates across data domains, state models, time rules, resource limits, platform differences, and existing evidence. Produce `EC-##`. This is not a full requirement-quality review, full test-case authoring, threshold invention, or test execution.

## When to Use

- Use it to systematically consider value, length, null/type, time, state, capacity, concurrency, platform, and combination boundaries.
- Use it to find high-risk boundaries outside the happy path from defects, failures, or design constraints.
- Use it to prioritize boundary candidates and turn them into verifiable follow-up test intent.

Do not use it only to analyze requirement gaps, write a complete test case suite, review existing cases, or execute boundary tests.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read and follow `prompts/edge-case-discovery.md`, beginning with the six-part input audit.
2. Identify input, state/time/resource, and interaction dimensions and use only evidenced boundaries.
3. Record dimension, boundary/combination, trigger, concern, impact, evidence, and validation in `EC-##` entries.
4. Preserve assumptions and open questions for unknown thresholds, missing states, and conflicting rules.
5. Return discovery candidates rather than full cases; later test design and execution decide how to run them.

## Core Constraints

- Consider value/length, null/type, time/timezone, state transitions, capacity/resources, concurrency/order, platform/localization, and combinations when applicable.
- Do not invent thresholds, states, concurrency counts, error results, or product rules; mark unknowns `unassessed` or open.
- `EC-##` is a candidate discovery, not executed, passed, complete-coverage, or zero-risk evidence.
- Do not expand candidates into full test cases, execute tests, or modify the target system.

## Reference Files

- Always read `prompts/edge-case-discovery.md` before producing an analysis.
- For regression, read `evals/eval.yaml` and matching cases; configuration does not prove that boundaries were verified.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Pre-delivery Check

- [ ] Recorded known facts, missing information, conflicts, stale information, out-of-scope items, and assumptions.
- [ ] Each `EC-##` has a dimension, boundary/combination, trigger, source, evidence state, impact, and validation suggestion.
- [ ] Known thresholds, inferred candidates, and unknown open items remain separate.
- [ ] Reasons and residual risks are stated for unassessed dimensions.
- [ ] The discovery list is not presented as full cases, execution results, pass evidence, or release conclusions.

## Common Pitfalls

- Saying “test the boundary” without naming the dimension, trigger, and observable concern.
- Treating a common industry value as the current product threshold.
- Generating mechanical duplicate candidates for every field instead of prioritizing risk and evidence.
- Treating candidate count as proof of coverage quality.
