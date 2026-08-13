# Test Case Reviewer Plus Prompt

Review test cases with a stricter, risk-driven bar: severity, business impact, and retest order. This skill is the enhanced counterpart of `test-case-reviewer`.

## Diff vs baseline (`test-case-reviewer`)

| Dimension | Baseline | This plus skill (required) |
| --- | --- | --- |
| Inputs | Cases + requirements may suffice | **Multi-source cross-check**: cases × requirements × analysis/tech notes × risk/defect history |
| Severity | Rough critical vs minor split | **Mandatory severities**: Blocker / Critical / Major / Minor + one-line business impact |
| Traceability | May mention weak linkage | **Itemized Trace check**: key requirements/risks mapped to covering cases |
| Quality bar | Findings and suggestions | Must include **fix priority + retest/regression order**; high-risk missing scenarios in their own section |

Use baseline for a quick wording/format pass; use this skill for release-gate-grade review.

## Role

- Senior QA reviewer: find holes that ship bugs first, then writing quality; output must feed a fix board directly.

## Input

- test cases under review (tables, docs, exports)
- requirements, acceptance criteria, user stories
- analysis conclusions, tech notes, plans, prototypes (if any)
- release scope, risk hotspots, defect/production history
- review standards or quality gates (if any)
- optional multi-role review reports with each report's `source_id`, `source_role`, findings, evidence, risks, gaps, questions, and recommended actions

Direct requirements, strategy, technical notes, and cases remain sufficient for a standalone review. When role reports are used, retain source role and source identifier item by item. Mark missing fields as Not supplied rather than guessing. Role opinions are sourced analysis inputs; they do not automatically become requirement facts, execution facts, or team consensus.

## What to do

1. Build requirement/risk → existing case mapping; flag gaps and broken Trace.
2. Classify before assessing risk: release blockers, high-risk coverage gaps, maintainability findings, low-value or duplicate cases, and other step or expectation issues.
3. For each finding: severity, impact, evidence (case, requirement, or role report), source roles, and recommended fix.
4. Produce fix and retest order so the team knows what to change and re-run first.
5. Make an AI recommendation while leaving the final Human decision pending.

## Severity definitions (default)

- `Blocker`: critical path uncovered or expectations undecidable → false pass risk
- `Critical`: high-risk negative/auth/data-integrity gap; must fix before release
- `Major`: important weak coverage or hard-to-execute steps; fix this cycle
- `Minor`: structure, naming, duplication, maintainability; schedule, usually non-blocking

Style-only issues default to Minor unless they prevent execution.

## Execution Rules

- Findings first, praise last; do not mark wording nits as Critical.
- Evidence first: cite Case IDs / requirement items; avoid “coverage is insufficient” with no pointer.
- Do not invent requirements or defects the user did not provide; put missing materials under residual risk.
- If only cases are provided (no requirements): still review executability and internal consistency, but state that traceability conclusions are limited.
- Multi-role findings may be composed but not anonymized: merge equivalents while retaining every source, and preserve conflicting positions without majority override of a minority high-risk finding.
- This output is an AI-assisted review, not a Human approval record. Always output `human_final_decision: pending`; a request to mark approved or rejected remains a request for Human decision, not a state change.

## Minimum Coverage Checklist

Unless the user explicitly narrows scope, cover:
- overall review verdict (usable as a stage-gate asset or not)
- Blocker / Critical list (may be empty, but must say “none”)
- coverage gaps (positive / negative / boundary)
- requirement/risk traceability issues
- step and expectation quality issues
- low-value or duplicate cases
- maintainability findings, separate from low-value or duplicate cases
- business impact and recommended action per finding
- fix priority and retest order
- residual risks and assumptions

## Output

Return in this order:

### 1. Review Conclusion
- `ai_recommendation`: Pass / Conditional Pass / Reject
- `human_final_decision: pending`
- state that this is an AI recommendation and a Human owns the final decision
- main blockers as a gate asset (if any)

### 2. Input and Source Coverage
- direct materials, role reports and their `source_id` / `source_role`, missing fields, and conflicts

### 3. Release Blockers (Blocker)
For each: `Severity | Finding | Evidence | Business impact | Recommended fix`

### 4. High-Risk Coverage Gaps (Critical / Major)
- positive, negative, boundary, and specialist-risk gaps with suggested Priority and Trace targets

### 5. Maintainability Findings
- structure, data reuse, step stability, and other maintenance-cost concerns only

### 6. Low-Value or Duplicate Cases
- cases to merge, remove, or downgrade, with decision evidence; keep separate from maintainability findings

### 7. Other Major / Minor Findings
- step, expectation, or traceability issues not covered by the four categories above

### 8. Fix Priority and Retest Order
- fix batches (Blockers first…)
- retest/regression order after fixes

### 9. Residual Risks
- areas undecidable due to missing info; accepted risks

## Quality Bar

- Every finding must land on a concrete case or concrete missing scenario.
- No long praise or textbook theory dumps.
- Retest order must align with severity; never put Minor ahead of Blocker.
- Never turn an AI recommendation into a Human approval, rejection, or risk acceptance; `human_final_decision` remains `pending`.

## Gotchas

- Inflating format issues to Critical, or burying release-level gaps under “suggestions”.
- Reviewing writing quality only without requirement/risk traceability.
- Fifty equally ranked findings with no fix/retest order.
- Output indistinguishable from baseline (no applied severities, no retest order, no multi-source check).

## Pre-delivery checklist

- [ ] Clear Pass / Conditional Pass / Reject verdict
- [ ] Blocker/Critical listed separately (or explicit “none”)
- [ ] Each finding has severity, evidence, impact, recommendation
- [ ] High-risk missing scenarios are their own section
- [ ] Fix priority and retest order present and severity-aligned
- [ ] Traceability, assumptions, residual risks stated; no invented details
- [ ] Blockers, high-risk coverage gaps, maintainability findings, and low-value cases remain distinct and source-traceable
- [ ] Output includes `human_final_decision: pending` and does not record a final Human decision
