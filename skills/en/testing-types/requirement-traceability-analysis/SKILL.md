---
name: requirement-traceability-analysis
description: Use this skill when requirements, acceptance criteria, design, code, tests, defects, or evidence must be mapped bidirectionally and coverage gaps made explicit; triggers include requirement traceability, traceability analysis, and traceability matrix.
---

# Requirement Traceability Analysis

Build a bidirectional, auditable mapping from requirements or controls to acceptance criteria, design, code, tests, defects, and validation evidence. Keep relationship types separate from coverage statuses; never turn names, static presence, or report wording into execution results.

## When to Use

- You need to check whether requirements have acceptance, design, implementation, test, and defect coverage.
- You need to find orphan requirements, orphan tests, broken links, stale artifacts, or missing evidence.
- You need an auditable traceability matrix for release, change review, compliance, or risk governance.

Do not use it only to write test cases, execute tests, or decide business priority; this Skill analyzes the mappings and evidence supplied by the user.

## Workflow

1. Read and follow `prompts/requirement-traceability-analysis.md`; audit target, version, scope, time window, and input boundary first.
2. Map requirements, acceptance, design, code, tests, defects, and evidence using stable identifiers, preserving source, version, and applicability.
3. Keep relationship types `direct`, `derived`, `indirect`, `contradictory`, and `missing` separate from coverage statuses `complete`, `partial`, `unverified`, `stale`, `unexecuted`, and `unassessed`; never use one group as the other.
4. When the task requests `coverage_analysis` or `test-coverage-analysis`, preserve bidirectional `RT-##` traceability and add a `TC-##` coverage view with test assets, coverage state, execution identity/time/environment, evidence quality, and orphan signals.
5. Preserve orphan items, broken links, duplicate mappings, missing execution records, and name-only links with a gap, owner, next action, and validation method.
6. Keep conclusions bounded by supplied material; execution, defect closure, and release claims require corresponding evidence.

## Core Constraints

- Use `RT-##` finding IDs; each row includes requirement/control, source, linked artifact, relationship type, coverage status, evidence, and gap action.
- Relationship types: `direct`, `derived`, `indirect`, `contradictory`, and `missing`.
- Coverage statuses: `complete`, `partial`, `unverified`, `stale`, `unexecuted`, and `unassessed`.
- In `coverage_analysis` mode, use `TC-##` for coverage views while preserving `RT-##` relationship findings; relationship types and coverage states remain separate.
- Check both directions: trace requirements downstream and trace tests/defects/evidence upstream; mark an item orphaned when no counterpart is found.
- Do not call a file, link, test name, report summary, or code presence executed, passed, fixed, or approved.
- When artifacts, stable IDs, versions, execution records, data, or environment are missing, mark `unassessed`/`unverified`/`unexecuted` and ask for evidence.
- Do not invent requirements, relationships, thresholds, owners, approvals, or runtime results; state the basis and close condition for recommendations.

## Progressive Disclosure

- Always read `prompts/requirement-traceability-analysis.md` before producing an analysis.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; configuration and static mappings do not prove real system execution.
- To check discovery behavior, run `scripts/run_skill_trace_eval.py` with `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`, not a trigger pass.
- To regress `test-coverage-analysis`, use the `coverage-*` Evals and a local trigger prompt containing “coverage analysis”; the target remains this physical Skill directory and no alias directory is created.

## Pre-delivery Checklist

- [ ] Input audit, scope, version, time window, and key assumptions are recorded
- [ ] Both requirement-to-artifact and artifact-to-requirement traceability are checked
- [ ] Every conclusion has source, evidence, relationship type, coverage status, and validation method
- [ ] Relationship types `direct`, `derived`, `indirect`, `contradictory`, and `missing` are separate from coverage statuses `complete`, `partial`, `unverified`, `stale`, `unexecuted`, and `unassessed`
- [ ] Static presence, report wording, and test names are not presented as execution results

## Common Pitfalls

- Claiming coverage because a test filename or ticket link exists.
- Building only a requirement-to-test matrix and missing orphan tests or unlinked defects.
- Treating missing evidence as no issue, or treating a report's “passed” as execution proof.
- Replacing stable IDs with similar titles and linking artifacts across versions or scopes.
