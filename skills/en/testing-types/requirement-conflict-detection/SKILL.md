---
name: requirement-conflict-detection
description: Use this skill when multiple requirement, policy, contract, or acceptance sources may contain mutually exclusive rules or constraints; triggers include requirement conflict detection, conflicting requirements, and mutually exclusive requirements.
---

# Requirement Conflict Detection

Identify mutually exclusive rules and constraints across supplied requirements, policies, contracts, designs, or acceptance artifacts within the same applicability scope. Preserve both sources, conditions, and evidence, and leave business decisions to a Human rather than choosing final precedence.

## When to Use

- Different artifacts allow and prohibit the same behavior.
- Role, state, permission, quantity, timing, or interface constraints are mutually exclusive in the same scope.
- You need to determine whether a difference is a real conflict or a boundary caused by version, platform, tenant, region, or applicability.

Do not use it for an ordinary one-source requirement review without mutually exclusive statements, to accept business risk, to choose precedence, or to invent an unapproved compromise rule.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

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

## Reference Files

- Always read `prompts/requirement-conflict-detection.md` before producing an analysis.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; structural gates do not prove conflict semantics were runtime-tested.
- To check discovery behavior, run `scripts/run_skill_trace_eval.py` with `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`, not a trigger pass.
- This is a repository-root development check; a standalone Skill package does not include the repository runner and does not depend on it at runtime.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

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
