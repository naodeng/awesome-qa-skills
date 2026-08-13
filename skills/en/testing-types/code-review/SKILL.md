---
name: code-review
description: Use this skill when you need a risk-driven code review of a PR/diff with severity-ranked findings and actionable fixes; triggers include code review, PR review, and 代码审查.
---

# Code Review

**中文版：** See the corresponding Chinese skill.

## When to Use

- Need to review a PR / diff / commit and catch logic, security, financial-loss, or maintainability risks before merge.
- Need a P0/P1/P2-ranked report with locations and actionable fix guidance.
- Need a QA / engineering-quality lens beyond author self-review.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Before reviewing, confirm both an identifiable code version and its reviewable changes; if either is missing, return a blocked result and request the exact material.
3. Add only project context that changes the result: change scope, business goal, stack, upstream/downstream deps, known risks, team norms.
4. Treat role reports as optional, source-identified context; use Product and UI/UX reports only when this change touches their concerns.
5. Default to Markdown; switch formats only when the user asks.

## Core Constraints

- Risk-driven: prioritize production failures, financial loss, security, and core maintainability — not naming/indent noise.
- Evidence-based: prefer file path, line, or snippet plus trigger path and impact for each finding.
- Two gates: require both identifiable code version (for example repository + PR / commit / branch / tag / revision) and reviewable change (for example diff/patch, changed-file contents, or an accessible base-to-head range). Code identity, change content, and role reports cannot substitute for one another.
- If either gate is missing, explicitly return `status: blocked` and distinguish `missing_code_identity` from `missing_reviewable_change`; do not claim review completion, recommend merge, or invent code findings.
- Role reports are optional. When using them, retain `source_role`. Product reports may add business-rule, state-flow, or acceptance context; UI/UX reports may add UI-state, feedback, responsive, or accessibility context only when relevant. Never present a role view as code fact.
- Strict severity: P0 blocks merge, P1 should fix this iteration, P2 can be tech debt.
- Separate confirmed facts from assumptions; do not invent endpoints, fields, environments, or root causes the user did not provide.
- Critique the code, not the author; respect the current stack — do not demand framework/architecture rewrites without authorization.
- Keep output executable: every finding needs a fix direction or before/after example.

## Progressive Disclosure

- Before producing output, read and follow `prompts/code-review.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For deeper review dimensions or severity rubrics: read `references/review-dimensions.md`.
- For examples or calibration: read matching files under `examples/`.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For the shortest path: read `quick-start.md`.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Confirmed both code-identity and reviewable-change gates; if blocked, did not issue a completed review or merge recommendation
- [ ] Minimum coverage focus: change summary, overall risk rating, P0/P1/P2 list, testability/observability, API/contract compatibility, fix order, residual risks and assumptions… (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit P0/P1 severity with rationale
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not treat a code snippet or role report as code identity, or a PR / commit identifier as the diff; block when either gate is missing.
- Do not activate Product or UI/UX concerns merely because a report exists; first establish relevance and retain its source.
- Do not treat every item as equally important, or dump low-value style nits.
- Do not skip assumptions and information gaps.
- Do not force refactors outside the change under review.
- Do not dump generic theory unrelated to this change.
