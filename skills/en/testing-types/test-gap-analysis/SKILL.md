---
name: test-gap-analysis
description: Use this skill when you need to identify missing or weak test obligations from requirements, risks, changes, defects, and test evidence; triggers include test gap analysis.
---

# Test Gap Analysis

Find test obligations that are not sufficiently protected by test intent or execution evidence across requirements, risks, changes, defects, and test assets. Produce actionable `TG-##` gaps. This is not a replacement for a traceability matrix, test-case review, or test execution.

## When to Use

- Use it to determine which requirements, risks, behaviors, or failure modes lack a test intent or evidence.
- Use it to find orphan tests, stale evidence, unverified execution, low-value duplicates, and high-risk uncovered obligations.
- Use it when inputs are incomplete but a bounded gap register and evidence questions are still useful.

Do not use it only to write test cases, build a complete `RT-##`/`TC-##` matrix, execute tests, or accept residual risk for a Human.

## Workflow

1. Read and follow `prompts/test-gap-analysis.md`, beginning with the six-part input audit.
2. Compare test obligations with test assets in both directions; never infer coverage from filenames or titles alone.
3. Use `TG-##` to distinguish missing mappings, orphan tests, unverified execution, stale evidence, uncovered risks, and low-value duplicates.
4. Preserve source, evidence state, impact/priority, proposed test intent, owner role, and close condition for every gap.
5. When evidence is missing, return a bounded result and mark `unassessed`, `unverified`, or `blocked` boundaries.

## Core Constraints

- `TG-##` records a gap and an action, not a coverage claim, pass, release, or risk-acceptance evidence.
- File presence, similar test names, report summaries, or static configuration cannot alone prove execution or coverage.
- Every material conclusion needs a source and minimum evidence; inferences must state assumptions and validation.
- Never invent requirements, priorities, test results, defect states, owners, or closure facts.
- Do not duplicate complete traceability analysis, test-case authoring, or executable-set selection here.

## Progressive Disclosure

- Always read `prompts/test-gap-analysis.md` before producing an analysis.
- For regression, read `evals/eval.yaml` and matching `evals/cases/`; Eval configuration does not prove project results.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`.

## Pre-delivery Check

- [ ] Recorded known facts, missing information, conflicts, stale information, out-of-scope items, and assumptions.
- [ ] Each `TG-##` has an obligation, source, gap type, evidence, impact/priority, and closure action.
- [ ] Static presence, inference, unverified execution, and actual execution evidence remain separate.
- [ ] High-risk gaps have an owner role, smallest evidence action, and validation method.
- [ ] The gap register is not presented as full coverage, pass, release, or Human risk acceptance.

## Common Pitfalls

- Treating a test file as proof that a requirement is covered.
- Saying “coverage is insufficient” without identifying the missing obligation and evidence.
- Marking every gap as highest priority or turning a suggested test into an execution result.
- Hiding the actual gap judgment inside a full traceability matrix or a test-case dump.
