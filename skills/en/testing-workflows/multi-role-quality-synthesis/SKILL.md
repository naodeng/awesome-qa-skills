---
name: multi-role-quality-synthesis
description: Use this skill when multiple role reports for one quality stage must be combined into a traceable synthesis; triggers include multi-role quality synthesis, role report consolidation, disagreement summary, 多角色质量汇总 and 角色报告合并.
---

# Multi-Role Quality Synthesis

## When to use

- One or more role reports exist for the same quality stage and must become a unified, traceable stage synthesis.
- Roles raised duplicate, complementary, or conflicting quality findings whose sources and disagreements must remain visible.
- Project-delivery constraints and quality facts appear together, and schedule or stakeholder requests must not override quality evidence.

## Input

Accept one or more role reports. Each report should contain `stage`, `source_role`, facts, evidence, findings, risks, gaps, questions, actions, and confidence, with a unique `source_id`. Record missing fields as input gaps; never fill them with invented content.

## Workflow

1. Read and follow `prompts/multi-role-quality-synthesis.md` in full; it is the standalone execution specification.
2. Verify that at least one report exists, each source is locatable, and all reports use the same `stage`. Do not combine different stages into one quality conclusion.
3. Build a source register and classify quality facts, findings, and project constraints before merging.
4. Merge only semantically equivalent findings and union all sources. Keep conflicting findings separate and include them under Disagreements.
5. Produce the traceable synthesis, then run source, disagreement, severity, project-boundary, and no-new-facts checks.

## Core constraints

- Every synthesized finding cites at least one input `source_id`; an equivalent finding retains every contributing source and role.
- Do not use voting or unexplained averaging. Preserve source severities when they conflict; explain any synthesized severity using the deterministic Prompt rule.
- Never hide, downgrade, or delete a minority P0/P1 view.
- Always include a Disagreements section, explicitly stating none when there are no disagreements.
- Keep schedules, capacity, dependencies, milestones, and stakeholder requests separate from quality facts. Project input cannot change defect, execution, evidence, or quality status.
- Create no fact, evidence, root cause, impact, status, or conclusion absent from all input reports.
- This Skill has no dependency on a specific role Skill. It processes only reports supplied by the caller and does not load or invoke another role Skill.

## Output contract

Output in this order: **Stage and Input Coverage, Quality Facts, Project Constraints, Synthesized Findings, Consensus, Disagreements, Blockers, Information Gaps, Open Questions, Actions, Confidence and Limitations, Source Register**. Preserve sources on findings, consensus, disagreements, blockers, and actions.

## Conditional loading

- Read `prompts/multi-role-quality-synthesis.md` for every execution; it contains the complete input validation, merge order, severity rules, and output template.
- Use `evals/` only for evaluation or regression. Eval scenarios are not project evidence and must not enter a real synthesis.

## Pre-delivery checks

- [ ] All inputs share one `stage`, or cross-stage synthesis is explicitly blocked
- [ ] Every synthesized finding cites one or more input sources
- [ ] Equivalent findings retain all contributors; conflicting findings were not silently merged
- [ ] Minority P0/P1 views remain visible; no severity was averaged without explanation
- [ ] Disagreements is always present and says none when no conflict exists
- [ ] Project constraints remain separate from quality facts; PM/delivery input did not override a quality fact
- [ ] No unsupported fact, evidence, root cause, impact, or conclusion was added

## Common mistakes

- Do not force together similarly worded findings with different targets, conditions, or impacts.
- Do not use majority agreement to remove a minority high-risk view.
- Do not treat deadlines, resource pressure, or status-change requests as quality evidence.
- Do not invent an optional role's perspective when it is absent; record a coverage gap and confidence limitation.
