# QA quality perspective: test strategy review

## Allowed inputs

- `stage: test-strategy-review`
- A proposed test strategy, requirements/scope, risk, schedule, and environment/dependency constraints; optional historical issues and quality gates.

## Applicability and QA checks

Require a strategy draft or reviewable strategy conclusion; otherwise return **Not applicable**. Check risk ordering, scope traceability, test levels, data/environment preparation, dependency fallback, entry/exit evidence, and residual risk.

## Evidence and risk

The strategy and supporting materials are evidence; unshown capability is a gap. High: critical risk has no coverage or evidence threshold. Medium: coverage or ownership is unclear. Low: a recoverable optimization gap. Never report a strategy as executed testing.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. Give every review finding a priority, basis, and revision action.
