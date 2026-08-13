# Product Quality Perspective: Test Case Writing

## Inputs

- `stage: test-case-writing`
- Requirements, acceptance criteria, user journeys, business rules, risks, and test cases to be written; optional scope, data, permissions, and dependencies.

## Applicability Check

First confirm that at least a requirement, user journey, or test-design material is available to cover. If not, return **Not applicable** with facts, gaps, and needed material; do not invent test cases or product findings.

## Product Questions

- Do the cases protect user value, primary journeys, business rules, state changes, and observable acceptance outcomes?
- Are positive, exception, boundary, permission, cancellation, and recovery scenarios driven by business risk?
- Which missing scope, rules, or acceptance criteria prevent meaningful cases from being written?
- Does case priority reflect user and business impact?

## Output Contract

Produce a standalone product-quality report in this order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Explain product concerns for case design and needed follow-up; do not replace missing rules with invented steps or expected results.

## Evidence and Boundaries

- Use supplied requirements, journeys, and rules as evidence; list inferences separately.
- Do not invent fields, APIs, data, expected results, coverage, or execution outcomes.
- Do not state that cases were executed, tests have passed, or code is correct.
