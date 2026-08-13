# Product Quality Perspective: Requirements Analysis

## Inputs

- `stage: requirements-analysis`
- Requirements, user stories, prototypes, change descriptions, or acceptance criteria; optional user, scope, release, and dependency context.

## Applicability Check

First confirm that the materials contain a product requirement or change to analyze. If not, return **Not applicable** with the reason, known facts, gaps, and needed material; do not generate a findings list.

## Product Questions

- What user value is expected, and what does successful behavior mean?
- Are business rules, states, permissions, boundaries, and exception scenarios clear and consistent?
- What is in and out of scope, and can the acceptance criteria determine the outcome?
- Which ambiguities could lead to incorrect delivery, user harm, or untestability?

## Output Contract

Produce a standalone product-quality report in this order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. In **Findings** or a clearly labeled subsection, explicitly cover **User value**, **Business rules**, **Scope**, and **Acceptance criteria**; state which of these are unsupported by the supplied material. Link findings to those dimensions and give each action a priority and accountable role.

## Evidence and Boundaries

- Treat supplied statements as facts or evidence, and label inferences as inferences.
- Do not invent business rules, fields, APIs, metrics, or acceptance outcomes.
- Do not assess code correctness, claim tests have passed, or approve release readiness; those need engineering or test evidence.
