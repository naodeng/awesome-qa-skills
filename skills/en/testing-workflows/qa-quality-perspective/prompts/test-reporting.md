# QA quality perspective: test reporting

## Allowed inputs

- `stage: test-reporting`
- Test scope, execution records, results, defects, untested items, environment/data constraints, and run links; optional requirements and release context.

## Applicability and QA checks

`test-reporting` remains applicable whenever it is the valid stage. Even without execution records, results, or defect material, produce a complete QA quality report: set status to **not executed or insufficient evidence**, state release risk, gaps, needed evidence, and next actions; do not return **Not applicable**. Check scope, execution status, result traceability, defect impact, untested scope, environment variance, and evidence completeness.

## Evidence and risk

Only execution records, results, defects, and links are execution facts. High: critical scope untested, blocking defect, or missing evidence. Medium: partial coverage, environment variance, or defect awaiting verification. Low: known, controlled residual risk. Never present inference, recommendation, or verbal assurance as executed/passed.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. A test report must separately identify **facts, inference, missing evidence, and recommendations**; without execution evidence, make no pass, verified-quality, or release conclusion.
