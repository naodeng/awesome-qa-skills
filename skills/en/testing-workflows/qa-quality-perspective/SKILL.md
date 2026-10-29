---
name: qa-quality-perspective
description: Use this skill when QA quality perspective is needed for requirements, strategy, review, test cases, or reports; triggers include QA quality perspective.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-workflows"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# QA quality perspective

## When to use

Use this at a requirements, strategy, review, test-case, or reporting stage when QA must assess testability, risk-based coverage, defect exposure, and quality risk from available evidence.

## Inputs

- `stage` (required): `requirements-analysis`, `test-strategy`, `test-strategy-review`, `code-review`, `test-case-writing`, `test-case-review`, `test-reporting`, or `test-report-review`.
- The declared stage inputs and any available requirement, code, test, defect, environment, or execution evidence.

## Workflow

1. Validate `stage`. If it is missing or unsupported, return **Not applicable**, list supported stages, and request a valid `stage`; do not generate filler conclusions.
2. Load and follow only the one Prompt mapped to that `stage`; never combine stage Prompts.
3. Apply that Prompt's input threshold. When materials are insufficient, state facts, gaps, and needed evidence rather than inventing tests, defects, or quality conclusions.
4. Produce a standalone QA quality report that separates facts, evidence, inference, missing evidence, and recommendations.

| `stage` | Only Prompt to load |
| --- | --- |
| `requirements-analysis` | `prompts/requirements-analysis.md` |
| `test-strategy` | `prompts/test-strategy.md` |
| `test-strategy-review` | `prompts/test-strategy-review.md` |
| `code-review` | `prompts/code-review.md` |
| `test-case-writing` | `prompts/test-case-writing.md` |
| `test-case-review` | `prompts/test-case-review.md` |
| `test-reporting` | `prompts/test-reporting.md` |
| `test-report-review` | `prompts/test-report-review.md` |

## QA responsibilities and boundary

- Focus on testability, risk-based coverage, observability, test evidence, defect risk, untested scope, and quality risk.
- Treat only supplied material as fact; label inference and missing evidence. Never invent product intent, acceptance rules, implementation behavior, execution records, defects, or metrics.
- QA does not decide product intent, certify code correctness, or approve release. Without execution evidence, it must never infer that testing ran, passed, or verified quality.

## Report contract

Unless returning **Not applicable**, include: **Summary, Facts, Evidence, Inference, Testability, Risk-based coverage, Defects and quality risks, Missing evidence, Recommendations and next steps, Confidence**. Tie every quality conclusion to evidence; classify risk as high, medium, or low with impact and uncertainty.

## Pre-delivery check

- [ ] The `stage` is valid and exactly one matching Prompt was loaded
- [ ] Facts, evidence, inference, missing evidence, and recommendations are distinct
- [ ] Testability and risk-based coverage are assessed, or the reason they cannot be assessed is explicit
- [ ] No missing product intent, implementation fact, or execution result is reported as fact
- [ ] Without execution evidence, the report does not imply or claim executed, passed, or verified testing

## On-demand loading and pitfalls

- Read only the mapped `prompts/` file after `stage` is valid. Read `evals/` for regression work, but never treat eval cases as project facts.
- Do not replace evidence with a generic risk checklist, or present test recommendations, static reading, or stakeholder opinion as a passing execution result.

## Report provenance

Keep the selected `stage`, a stable `source_id`, and supplied `version` in the report header. If a source ID is absent, declare a temporary local locator; if version is absent, write unknown rather than inventing it. Each finding has a stable `finding_id`, its source/evidence locator and status. Each action links its finding and specifies the evidence that would close it; owner, date and action status stay unknown unless supplied. These are standalone report fields, not a dependency on another Skill.

## Qualitative risk anchors

Use impact, observed likelihood signals, and uncertainty together; this is judgment, not arithmetic multiplication or a new score. Unknown likelihood stays unknown.

| Risk | Impact and likelihood evidence | Uncertainty/action |
| --- | --- | --- |
| High | Critical loss, blocking defect, or critical untested path; credible recurrence or unresolved exposure | Missing critical evidence prevents a confident low-risk claim; prioritize verification/escalation |
| Medium | Bounded impact or partial evidence with a plausible failure path | State the missing evidence and targeted follow-up |
| Low | Limited impact with supporting control evidence; no supplied critical exposure | State residual limits; do not equate low risk with release approval |
