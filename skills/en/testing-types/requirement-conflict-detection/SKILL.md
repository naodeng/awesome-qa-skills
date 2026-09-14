---
name: requirement-conflict-detection
description: Use when multiple requirement, policy, contract, or acceptance sources may contain mutually exclusive rules or constraints; triggers include requirement conflict detection, conflicting requirements, and mutually exclusive requirements.
---

# Requirement Conflict Detection

Identify mutually exclusive rules and constraints across supplied requirements, policies, contracts, designs, or acceptance artifacts within the same applicability scope. Preserve both sources, conditions, and evidence, and leave business decisions to a Human rather than choosing final precedence.

## When to Use

- Different artifacts allow and prohibit the same behavior.
- Role, state, permission, quantity, timing, or interface constraints are mutually exclusive in the same scope.
- You need to determine whether a difference is a real conflict or a boundary caused by version, platform, tenant, region, or applicability.

Do not use it for an ordinary one-source requirement review without mutually exclusive statements, to accept business risk, to choose precedence, or to invent an unapproved compromise rule.

## Workflow

1. Read and follow `prompts/requirement-conflict-detection.md`.
2. Audit source, version, time, actor, platform, region, tenant, and applicability conditions; state limitations when a boundary is missing.
3. Preserve mutually exclusive statements as a pair and verify whether they address the same object, action, and scope.
4. Distinguish `conflict`, `ambiguous`, `missing`, `stale`, and `unassessed`; do not promote missing evidence into a conflict.
5. Provide impact, priority, decision question, suggested owner, close condition, and validation method.

## Core Constraints

- Use `RF-##` finding IDs; each item includes both statements, sources, applicability, minimum evidence, impact, priority, and decision needed.
- Do not delete, rewrite, or compromise either source, and do not choose precedence, risk acceptance, or the final specification for a Human.
- When a rule differs by version, platform, tenant, region, or actor, report the boundary first instead of calling it a conflict.
- When version, scope, source, or context is missing, mark `missing`/`stale`/`unassessed` and ask for evidence.
- Do not present static document wording, an existing implementation, or a report table as runtime verification evidence.

## Progressive Disclosure

- Always read `prompts/requirement-conflict-detection.md` before producing an analysis.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; structural gates do not prove conflict semantics were runtime-tested.
- To check discovery behavior, run `scripts/run_skill_trace_eval.py` with `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`, not a trigger pass.

## Pre-delivery Checklist

- [ ] Every `RF-##` preserves both sources, versions/scopes, and minimum evidence
- [ ] `conflict`, `ambiguous`, `missing`, `stale`, and `unassessed` are distinct
- [ ] No source was silently merged, rewritten, or used to decide precedence
- [ ] P0/P1 conflicts have an owner role, decision question, close condition, and validation method
- [ ] Static artifacts, implementation presence, and report wording are not called execution evidence

## Common Pitfalls

- Choosing one statement because “must” sounds stronger than “should”.
- Ignoring version, platform, tenant, region, or actor boundaries and creating a cross-scope conflict.
- Inventing the other side when only one rule or one source is available.
- Hiding both original statements behind an unapproved compromise sentence.
