---
name: ux-quality-perspective
description: Use this skill when a quality stage needs a UX perspective on information architecture, interaction states, consistency, responsive behavior, or accessibility; triggers include UX quality perspective, UX review..
---

# UX Quality Perspective (English)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- A quality stage needs a UX perspective on information architecture, interaction states, consistency, responsive behavior, or accessibility.
- Product, design, engineering, and QA need to turn UI, prototype, user-flow, or UI-test evidence into actionable experience risk decisions.

## Inputs

- `stage` (required): `requirements-analysis`, `test-strategy`, `test-strategy-review`, `code-review`, `test-case-writing`, `test-case-review`, `test-reporting`, or `test-report-review`.
- Supplied evidence such as prototypes, screenshots, UI descriptions, design specifications, user flows, change materials, test assets, or reports.
- Optional context: target users, devices/breakpoints, assistive technology, design system, release scope, and known constraints.

## Workflow

1. Validate `stage`. If missing or unsupported, return **Not applicable**, name the supported stages, and request a valid value; do not generate filler findings.
2. Load and follow exactly one prompt from the table for the valid `stage`; never combine prompts from multiple stages.
3. Decide applicability from the supplied material first. `test-strategy`, `test-strategy-review`, `code-review`, `test-case-writing`, and `test-reporting` are **conditional participation**: analyze only when traceable UI/UX impact or relevant experience evidence exists. Otherwise return **Not applicable** with the reason, known facts, gaps, and material required to reassess; do not write filler findings.
4. `requirements-analysis` remains applicable without a prototype: report only confirmed requirement facts, UX evidence gaps, questions, and needed prototype/flow/state material; never invent screens, states, copy, or cross-device behavior.
5. Produce a standalone UX quality report that separates facts, evidence, inferences, and unverified items.

| `stage` | Only prompt to load |
| --- | --- |
| `requirements-analysis` | `prompts/requirements-analysis.md` |
| `test-strategy` | `prompts/test-strategy.md` |
| `test-strategy-review` | `prompts/test-strategy-review.md` |
| `code-review` | `prompts/code-review.md` |
| `test-case-writing` | `prompts/test-case-writing.md` |
| `test-case-review` | `prompts/test-case-review.md` |
| `test-reporting` | `prompts/test-reporting.md` |
| `test-report-review` | `prompts/test-report-review.md` |

## UX Responsibilities and Boundaries

- Focus on information architecture, navigation, discoverability, interaction feedback and states, consistency, responsive behavior, and accessibility, using only supplied UX/UI evidence.
- When prototypes, flows, states, breakpoints, or assistive-technology evidence are absent, mark them unknown or needing confirmation; never invent screens, controls, copy, error states, device behavior, or test results.
- Do not replace frontend/backend implementation review, API reliability or security assessment, test execution, or release approval. Without their evidence, do not assert implementation correctness, API reliability, security, passed tests, or release readiness.

## Report Contract

Unless returning Not applicable, every report contains, in order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Prioritize findings, risks, and actions by impact; state each conclusion's evidence basis and accountable role.

## Pre-delivery Checklist

- [ ] The `stage` is valid and exactly one matching prompt was loaded
- [ ] Applicability was assessed first; non-applicable conditional stages contain no filler findings
- [ ] Requirements analysis without a prototype reports evidence gaps only and does not invent UI
- [ ] The report separates facts, evidence, inferences, and gaps and includes every contract field
- [ ] It does not exceed UX boundaries with implementation, API, security, test, or release claims

## Progressive Disclosure

- Only after validating `stage`, read the one corresponding file in `prompts/`.
- For evaluation or regression, use `evals/` and run skill-up validation; do not treat eval cases as project evidence.

## Common Pitfalls

- Do not present a generic UX checklist as a proven defect in this product.
- Do not compensate for an absent prototype by inventing screens, states, or mobile behavior.
- Do not turn UX review into unsupported implementation-correctness, API-reliability, or release conclusions.
