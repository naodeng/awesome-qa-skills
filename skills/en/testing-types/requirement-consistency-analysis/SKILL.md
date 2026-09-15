---
name: requirement-consistency-analysis
description: Use this skill when multiple requirement artifacts may disagree on terminology, identifiers, formats, states, rules, or behavior; triggers include requirement consistency, cross-document consistency, and consistency analysis.
---

# Requirement Consistency Analysis

Compare supplied requirements, contracts, designs, or rule artifacts to determine whether terminology, identifiers, formats, states, rules, and behavior agree within the same applicability scope. Preserve source and version boundaries; never silently merge mutually exclusive constraints.

## When to Use

- PRDs, stories, API contracts, prototypes, technical notes, or acceptance criteria use different names or states.
- You need to check whether multiple materials describe the same actor, field, flow, and outcome consistently.
- The same flow may differ by version, time, platform, or role and applicability must be established first.

Do not use it with one source when only general requirements analysis is needed, or to make a business decision for an explicit conflict.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read and follow `prompts/requirement-consistency-analysis.md`.
2. Inventory source, version, time, actor, platform, and applicability scope. State the limitation when a comparison artifact is missing.
3. Compare terminology, identifiers, formats, states, rules, and behavior using stable keys; preserve evidence and relationship per item.
4. Distinguish relation values `aligned`, `inconsistent`, and `conflict` from evidence statuses `assessed`, `missing`, `stale`, and `unassessed`; never silently merge mutually exclusive rules.
5. When the task requests `business-rule` mode, use stable rule keys and `BR-##` rule-level evidence for subject, trigger, applicability, precedence/override, action, outcome, and exception while retaining generic `RC-##` findings.
6. Provide impact, priority, owner role, open question, close condition, and validation method.

## Core Constraints

- Use `RC-##` finding IDs; each row includes source pair, comparison key, relation, status, evidence, scope/version, impact, and action. Relations are `aligned`, `inconsistent`, or `conflict`; statuses are `assessed`, `missing`, `stale`, or `unassessed`.
- In `business-rule` mode, add `BR-##` rule-level evidence for subject/object, trigger, applicability, precedence/override, action, outcome, and exception; never treat “stricter” as automatically higher precedence.
- Status values: `assessed`, `missing`, `stale`, and `unassessed` are evidence states, not relation values.
- Do not treat similar names as synonyms and do not call one source consistent merely because a second source is absent.
- Do not compare across versions or applicability scopes as if they were one fact. Use `stale`/`unassessed` when scope is unclear.
- Suggest `requirement-conflict-detection` for explicit mutually exclusive rules by Skill name only; do not link its internal files.
- Do not invent state transitions, field meaning, platform support, or a final specification.

## Reference Files

- Always read `prompts/requirement-consistency-analysis.md` before producing an analysis.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; structural gates do not prove cross-source semantic correctness.
- To check discovery behavior, run `scripts/run_skill_trace_eval.py` with `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`, not a trigger pass.
- This is a repository-root development check; a standalone Skill package does not include the repository runner and does not depend on it at runtime.
- To check `business-rule` mode, use the `business-rule-*` Evals and a local trigger prompt containing the business-rule phrase; the physical directory remains this Skill and no alias directory is created.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Pre-delivery Checklist

- [ ] Each comparison conclusion cites source, version/scope, and minimum evidence
- [ ] Relation values `aligned`, `inconsistent`, and `conflict` are separate from statuses `assessed`, `missing`, `stale`, and `unassessed`
- [ ] Explicit conflict is not silently merged or incorrectly downgraded
- [ ] P0/P1 issues have owner role, decision question, and validation method
- [ ] Names, document existence, and static tables are not presented as runtime results

## Common Pitfalls

- Treating similar terms as the same object without evidence.
- Ignoring document version, publication time, platform, tenant, or region.
- Filling one source's omissions with another source's unstated defaults.
- Rewriting conflicting statements into an unapproved compromise rule.
