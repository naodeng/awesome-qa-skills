# QA quality perspective: test report review

## Allowed inputs

- `stage: test-report-review`
- A test report, execution records, results, defects, scope, untested items, and environment/data evidence; optional release gates.

## Applicability and QA checks

Require a test report or auditable report material; otherwise return **Not applicable**. Check whether conclusions trace to execution evidence, whether scope, untested items, defects, and environment are complete, and whether risk classification matches evidence and impact.

## Evidence and risk

Treat raw records and links in the report as evidence; validate summary claims against them. High: an unsupported pass conclusion, critical untested scope, or blocking defect. Medium: unclear metric basis, environment, or retest. Low: wording and organization issues. Review opinion never substitutes for execution evidence.

## Output structure

Produce: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. Separately list **facts, inference, missing evidence, and recommendations**; without execution evidence, do not confirm passed testing or verified quality.
