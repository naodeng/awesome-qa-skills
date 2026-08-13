# QA quality perspective: requirements analysis

## Allowed inputs

- `stage: requirements-analysis`
- Requirements, user journeys, acceptance criteria, API/data constraints, dependencies, and known risks; optional historical defects and observability material.

## Applicability and QA checks

Require at least one requirement or behavior signal; otherwise return **Not applicable** with known facts and needed material. Check behavior, boundaries, failure handling, observable results, acceptance criteria, and whether data, environments, and dependencies make testing possible.

## Evidence and risk

Treat supplied requirements and constraints as evidence. High: core journeys, money/data, irreversible impact, or critical dependencies. Medium: important alternate paths or uncertain boundaries. Low: limited, recoverable impact. Never invent product intent, rules, or implementation.

## Output structure

Produce a standalone QA quality report: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. State testing impact and owner for every gap.
