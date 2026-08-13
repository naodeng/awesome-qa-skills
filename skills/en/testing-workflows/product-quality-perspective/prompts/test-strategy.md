# Product Quality Perspective: Test Strategy

## Inputs

- `stage: test-strategy`
- Product goals, requirement scope, risks, release plan, user impact, known test capability, and constraints; optional history and dependencies.

## Applicability Check

First confirm that a strategy is to be created or updated and that at least one product goal, scope, or risk signal is available. Otherwise return **Not applicable** with facts, gaps, and needed decision material; do not fill the report with strategy findings.

## Product Questions

- Which user journeys, business rules, and failure consequences most need protection?
- Do scope, priority, trade-offs, and quality thresholds match user and business impact?
- Which product risks remain under-covered because of time, data, environment, or dependency constraints?
- What evidence do decision makers need to accept the strategy trade-offs?

## Output Contract

Produce a standalone product-quality report in this order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Make actions prioritized items that product, QA, and engineering can jointly execute; do not replace the detailed test strategy.

## Evidence and Boundaries

- Use only supplied goals, scope, risks, and constraints as evidence; label inferences separately.
- Do not invent coverage, resources, environment capability, test results, or quality thresholds.
- Do not promise passed tests, code correctness, or release approval; strategy advice is not an execution conclusion.
