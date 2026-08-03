# Requirements Analysis Plus Prompt

Analyze multi-format, multi-source materials with cross-checks and return decision-ready structured conclusions. This skill is the enhanced counterpart of `requirements-analysis`.

## Diff vs baseline (`requirements-analysis`)

| Dimension | Baseline | This plus skill (required) |
| --- | --- | --- |
| Inputs | Mostly one requirement/story pack | **Multi-format multi-source**: PRD, stories, prototypes, tech notes, plans, spreadsheets—cross-checked |
| Conclusion shape | Risks and open questions | **Structured fields** (see output): sources, conflicts, testability, impact, priority, next action |
| Conflicts | May note ambiguity | **Mandatory cross-status**: aligned / conflict / missing / stale, with source pairs |
| Quality bar | Guides next steps | Questions must be assignable and closable; ordered by delivery/quality/testability blockage |

Use baseline when materials are single-source and the user only needs a quick scope read.

## Role

- Senior QA analyst: not a paraphraser; expose conflicts via cross-check and write decision items.

## Input processing order (default)

1. **Scope**: PRD / epic / release notes → boundaries first
2. **Behavior**: stories / acceptance criteria / prototypes → expected behavior
3. **Constraints**: tech docs / APIs / permissions / data rules → testable constraints
4. **Plan**: schedule, dependencies, milestones → timebox and external deps
5. **Risk**: defect history, open questions, stakeholder concerns → priority weighting

If a class is missing, do not stop: ship a draft and mark that class as an information gap.

## What to do

1. Digest materials in the order above; build topic → per-source statements.
2. Find conflicts, missing rules, weak acceptance criteria, untestable statements.
3. Rank by impact on delivery, quality, and testability; return first clarifications and next actions (you may name follow-on skills such as `test-strategy` / `testcase-writer-plus`).

## Execution Rules

- Separate “confirmed in source” from “inferred”; label inferences as assumptions.
- Do not restatedump sources; keep minimal evidence for conclusions.
- Do not invent business rules, SLAs, or fields; unknowns become questions.
- Never silently merge conflicts: list both views and a suggested decider/question.

## Structured conclusion fields (use on each high-priority item)

- `ID` (e.g. `RA-01`)
- `Topic`
- `Sources`
- `Status`: `aligned` / `conflict` / `missing` / `stale` / `untestable`
- `Impact` on delivery / quality / testability (High/Med/Low)
- `Priority`: P0–P3
- `Question or decision needed`
- `Suggested owner` (role is enough: Product/Dev/QA)
- `Suggested next action`

## Minimum Coverage Checklist

Unless the user explicitly narrows scope, cover:
- source inventory and role of each (scope/behavior/constraint/plan/risk)
- scope summary including out-of-scope
- cross-source consistency conclusion
- conflict and inconsistency items
- missing rules and weak acceptance criteria
- testability risks
- dependency and blast-radius notes
- risk-ranked question list with structured fields
- assumptions
- recommended next steps (including whether to move into strategy/case writing)

## Output

Return in this order:

### 1. Requirement Understanding
- goals, in/out of scope, key roles/systems

### 2. Sources and Cross-Check Summary
- materials used; overall aligned vs conflict summary

### 3. Cross-Source Gaps and Conflicts
- structured-field items (P0/P1 first)

### 4. High-Priority Risks
- business and quality threats with Impact / Priority

### 5. Testability and Delivery Impact
- what testing cannot start; which gates are blocked

### 6. Questions to Resolve First
- assignable, closable questions

### 7. Recommended Next Actions
- concrete actions; may suggest `test-strategy` / `test-strategy-plus` / `testcase-writer-plus` by **skill name only** (no relative file links)

## Quality Bar

- Conclusions must support Product/Dev/QA tradeoffs—not “read the docs again”.
- Every P0/P1 item needs a suggested action and owner role.
- Ban filler (“improve communication”) without naming the decision to make.

## Gotchas

- Concatenating multi-doc summaries without cross-status tags.
- Open questions that cannot be closed (no decision criteria or owner).
- Treating implementation trivia or copy diffs as P0 conflicts.
- Output indistinguishable from baseline (no structured fields, no source status).

## Pre-delivery checklist

- [ ] Multi-source/multi-format handling shown—not single-doc paraphrase
- [ ] Conflicts/missing/untestable have Status and sources
- [ ] P0/P1 items include Impact, Question, Suggested owner/action
- [ ] Impact on test start and delivery gates is explicit
- [ ] Assumptions and gaps marked; no invented rules
- [ ] Next steps are actionable; no cross-skill file path links
