# QA quality perspective: code review

## Allowed inputs

- `stage: code-review`
- PR/diff, code, API contract, requirement/acceptance criteria, test changes, and static or runtime evidence; optional architecture and defect material.

## Applicability and QA checks

Require a PR, diff, code, or API contract; otherwise return **Not applicable**. Check test entry points, observable results, error/boundary handling, regression impact, test assets, and risk traceability.

## Evidence and risk

Code and explicit contracts are implementation facts; requirements support traceability but do not prove correctness. High: core data, authorization, or transaction paths, or no regression evidence. Medium: unknown boundaries, exceptions, or dependency behavior. Low: contained maintainability gaps. Without runtime evidence, never claim tests passed.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. Label static findings as needing verification; QA must not certify code correctness.
