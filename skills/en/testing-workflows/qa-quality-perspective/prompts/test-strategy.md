# QA quality perspective: test strategy

## Allowed inputs

- `stage: test-strategy`
- Scope, requirements, risk, release goal, architecture/dependencies, and available test capabilities and constraints; optional historical defects, environment, and data material.

## Applicability and QA checks

Require at least one scope, goal, or risk signal; otherwise return **Not applicable**. Check coverage of critical behavior, boundaries, failure modes, dependencies, data, environment, observability, and exit evidence, with traceable trade-offs.

## Evidence and risk

Use supplied scope, risk, and capability constraints as evidence. Classify high, medium, or low using impact × likelihood × evidence uncertainty, then prioritize coverage. Do not invent coverage, staffing, executed tests, or pass results.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. For each coverage item, state risk, test level/method, required evidence, and reason for any exclusion.
