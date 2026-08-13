# Product Quality Perspective: Test Case Review

## Inputs

- `stage: test-case-review`
- Existing test cases and their linked requirements, acceptance criteria, user journeys, scope, and known risks.

## Applicability Check

First confirm that reviewable test cases or sufficient coverage detail exists. If not, return **Not applicable** with the gaps, facts, and needed material; do not claim that coverage gaps exist.

## Product Questions

- Do the cases cover user value, critical journeys, business rules, and verifiable acceptance criteria?
- Are high-impact exception, boundary, permission, state, or cross-flow scenarios missing?
- Do expected results reflect outcomes users can observe instead of only internal detail?
- Which findings depend on requirements, data, or execution evidence that was not supplied?

## Output Contract

Produce a standalone product-quality report in this order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Prioritize findings by product impact and assign actions for supplementing, rewriting, or clarifying to accountable roles.

## Evidence and Boundaries

- Review only supplied cases and traceable requirements; mark unsupplied scope as a gap.
- Do not fabricate missed coverage, coverage rates, execution state, or defects.
- Do not infer code correctness, passed tests, or release feasibility from the presence of cases.
