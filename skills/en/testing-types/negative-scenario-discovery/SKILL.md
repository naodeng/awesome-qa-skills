---
name: negative-scenario-discovery
description: Use this skill when you need to discover invalid, denied, failed, degraded, or unsafe-recovery scenarios from product evidence; triggers include negative scenario discovery.
---

# Negative Scenario Discovery

Discover failure, denial, degradation, and unsafe-recovery paths from goals, input constraints, permissions, dependency contracts, timeout/retry, idempotency/transaction, and recovery design. Produce `NS-##`. Do not write full test cases, run fault injection, invent error codes, or declare behavior correct.

## When to Use

- Use it to examine invalid input, unauthorized access, dependency failure, timeout, retry exhaustion, duplicate request, partial failure, and inconsistency.
- Use it to find failure stimuli and observable outcomes outside the happy path from designs or past failures.
- Use it when failure contracts are incomplete and evidence gaps, recovery choices, and Human decisions must be explicit.

Do not use it only to find boundary values, write full cases, run fault injection, conduct a real incident review, or choose final copy/SLA for a team.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read and follow `prompts/negative-scenario-discovery.md`, beginning with the six-part input audit.
2. Analyze failure mode, stimulus, preconditions, expected rejection/degradation/retry/handoff, and consistency impact.
3. Record source, evidence state, priority, caller-visible result, and validation in `NS-##` entries.
4. Separate explicit product contracts, evidence-based inference, open choices, and execution prerequisites.
5. Deliver bounded failure paths when information is missing; never present a recommendation as verified behavior.

## Core Constraints

- Distinguish invalid input, unauthorized access, dependency failure, timeout, retry exhaustion, duplicate request, partial failure, and unsafe recovery when applicable.
- Do not run fault injection, call real dependencies, or modify data or the target system.
- Do not invent error codes, retry counts, timeout thresholds, user copy, SLAs, or recovery approval.
- `NS-##` is a negative candidate and evidence need, not proof of execution, pass, recovery, or safety.
- Do not expand negative discovery into full test cases or an incident root-cause conclusion.

## Reference Files

- Always read `prompts/negative-scenario-discovery.md` before producing an analysis.
- For regression, read `evals/eval.yaml` and matching cases; configuration does not prove failure paths ran.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Pre-delivery Check

- [ ] Recorded known facts, missing information, conflicts, stale information, out-of-scope items, and assumptions.
- [ ] Each `NS-##` has failure mode, trigger, preconditions, expected handling, visible result, consistency impact, and evidence need.
- [ ] Retryable, non-retryable, Human-handoff, and safe-rejection paths are separate.
- [ ] No fault injection was run and no error code, threshold, or recovery result was invented.
- [ ] The candidate list is not presented as full cases, passed tests, incident conclusions, or release approval.

## Common Pitfalls

- Using one generic “return an error” path for every failure mode.
- Listing exception names without trigger, consistency impact, or visible result.
- Treating code presence or an example response as a complete error contract.
- Choosing retry, degradation, SLA, or Human-handoff policy merely to give a definite answer.
