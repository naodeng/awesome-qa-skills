# QA quality perspective: test-case review

## Allowed inputs

- `stage: test-case-review`
- Test cases, requirements/acceptance criteria, risk, and scope; optional strategy, API contract, defect history, and data/environment notes.

## Applicability and QA checks

Require test cases to review; otherwise return **Not applicable**. Check executability, decidable expected results, requirement and risk traceability, boundary/exception/regression coverage, and data/environment clarity.

## Evidence and risk

Cases and supplied requirements are evidence, not execution. High: a critical risk has no case or expectation cannot be judged. Medium: boundary, exception, or data gap. Low: readability or duplication issue. Never present the existence of cases as passing tests.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. Link findings to a case/risk, state impact, and propose a revision action.
