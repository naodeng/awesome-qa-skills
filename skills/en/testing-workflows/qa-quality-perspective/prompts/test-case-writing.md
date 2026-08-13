# QA quality perspective: test-case writing

## Allowed inputs

- `stage: test-case-writing`
- Requirements/acceptance criteria, scope, risk, API or UI contracts, and data/environment constraints; optional historical defects and strategy.

## Applicability and QA checks

Require testable behavior or a risk signal; otherwise return **Not applicable**. Check preconditions, inputs, steps, observable expected results, positive/negative/boundary/exception paths, data isolation, and traceability.

## Evidence and risk

Use only supplied rules and contracts to define expectations; missing expectations are clarification items. Prioritize high-risk cases for core journeys, authorization, money/data, and irreversible actions; medium for important boundaries; low for local recoverable behavior. Never invent business rules.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**, plus case recommendations with priority, preconditions, steps, expected results, and evidence needs.
