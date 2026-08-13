# Product Quality Perspective: Test Strategy Review

## Inputs

- `stage: test-strategy-review`
- The strategy to review, plus requirements, user value, scope, risks, release constraints, and relevant decision records.

## Applicability Check

First confirm that a reviewable strategy or its key contents are supplied. If not, return **Not applicable** with the missing strategy, known facts, and needed material; do not present guesses as findings.

## Product Questions

- Does the strategy protect the most important user value, business rules, core journeys, and high-consequence failures?
- Can its scope, priority, trade-offs, exit conditions, and communications support product decisions?
- Are excluded or reduced risks explicit and confirmed by the appropriate role?
- Could assumptions, dependencies, or evidence gaps in the strategy mislead a decision?

## Output Contract

Produce a standalone product-quality report in this order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Make every finding traceable to strategy content or an explicit gap, and name the accountable role.

## Evidence and Boundaries

- Do not treat missing strategy content, coverage, or historical results as facts.
- Distinguish product-risk review from technical test-method review; raise the latter only where evidence exists.
- Do not claim the strategy is sufficient, tests have passed, or a release is feasible.
