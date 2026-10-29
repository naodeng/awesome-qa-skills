---
name: technical-quality-perspective
description: Use this skill when a technical quality perspective is needed for requirements, strategy, code, test cases, or reports; triggers include technical quality review, architecture review, and code review.
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

# Technical quality perspective

## When to use

Use this to assess technical quality from declared architecture, API, data, code, security, performance, compatibility, and observability evidence at a selected delivery stage.

## Inputs and workflow

- `stage` is required: `requirements-analysis`, `test-strategy`, `test-strategy-review`, `code-review`, `test-case-writing`, `test-case-review`, `test-reporting`, or `test-report-review`.
- Validate `stage`; if absent or unsupported, return **Not applicable**, list supported values, and request a valid stage. Load exactly one mapped Prompt only.
- For `code-review`, require both code identity (PR, commit, branch, release version, or equivalent) and reviewable changes (diff, files, or code). If either is absent, block review; do not infer findings or merge readiness.
- Apply the selected Prompt's applicability threshold. Treat supplied material as fact, label inference, and turn missing material into questions and actions.

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

## Responsibilities and boundary

- Cover architecture, APIs, data, compatibility, security, performance, observability, and maintainability only when relevant to the selected stage and supplied evidence.
- Produce technical findings with evidence, impact, severity, missing information, actions, and confidence. A gap supports a qualified risk, never an invented implementation, metric, vulnerability, or execution result.
- Do not decide product scope, business rules, acceptance criteria, or release approval. Do not claim code correctness, test execution, or passed testing without direct evidence.

## Report contract and self-check

Unless blocked or **Not applicable**, output: **Summary, Facts, Evidence, Technical findings, Impact and severity, Missing information, Questions, Actions and next steps, Confidence**.

- [ ] Valid stage and exactly one mapped Prompt
- [ ] Code review has code identity and reviewable changes, or is explicitly blocked
- [ ] Findings are evidence-backed; gaps and inference are labelled
- [ ] No product or test fact has been invented or changed
- [ ] Stage-relevant technical dimensions only; no passed-test or code-correctness claim without evidence

Read only the mapped Prompt after stage validation. Read `evals/` only for regression work, never as project evidence.

## Report provenance

Keep the selected `stage`, a stable `source_id`, and supplied `version` in the report header. If a source ID is absent, declare a temporary local locator; if version is absent, write unknown rather than inventing it. Each finding has a stable `finding_id`, its source/evidence locator and status. Each action links its finding and specifies the evidence that would close it; owner, date and action status stay unknown unless supplied. These are standalone report fields, not a dependency on another Skill.

## Static finding location and handoff

For supplied code or line-numbered text, use `file:line@version` and quote the exact supplied evidence. For design-only material, use its document/section/version; do not invent code files or lines. Carry the same finding ID/evidence into a code-review or specialized design-review handoff by Skill name, so the receiving review can refine it without duplicating a claimed runtime defect.
