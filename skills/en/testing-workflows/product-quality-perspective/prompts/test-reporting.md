# Product Quality Perspective: Test Reporting

## Inputs

- `stage: test-reporting`
- Test scope, execution records, results, defects, untested items, environment/data constraints, and release background; optional requirements and user impact.

## Applicability Check

First confirm that test status or report material exists to summarize. If not, return **Not applicable** with facts, gaps, and the needed records; do not invent quality status or release recommendations.

## Product Questions

- What do tested and untested scope mean for user value, core journeys, and business rules?
- Which defects, blockers, or limitations could change a user or business decision?
- Do metrics hide critical risk, sampling bias, or insufficient evidence?
- What facts or actions are still needed before the next decision?

## Output Contract

Produce a standalone product-quality report in this order: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Explain product impact from actual test status, but do not turn advice into approval.

## Evidence and Boundaries

- Use execution records, defects, and scope as evidence; absent records are unknown.
- Do not invent pass rates, defect impact, coverage, passed tests, or release conclusions.
- Do not replace release approval; state which product, engineering, and QA evidence is needed for a conclusion.
