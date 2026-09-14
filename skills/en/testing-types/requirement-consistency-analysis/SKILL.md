---
name: requirement-consistency-analysis
description: Use when multiple requirement artifacts may disagree on terminology, identifiers, formats, states, rules, or behavior; triggers include requirement consistency, cross-document consistency, and consistency analysis.
---

# Requirement Consistency Analysis

Compare supplied requirements, contracts, designs, or rule artifacts to determine whether terminology, identifiers, formats, states, rules, and behavior agree within the same applicability scope. Preserve source and version boundaries; never silently merge mutually exclusive constraints.

## When to Use

- PRDs, stories, API contracts, prototypes, technical notes, or acceptance criteria use different names or states.
- You need to check whether multiple materials describe the same actor, field, flow, and outcome consistently.
- The same flow may differ by version, time, platform, or role and applicability must be established first.

Do not use it with one source when only general requirements analysis is needed, or to make a business decision for an explicit conflict.

## Workflow

1. Read and follow `prompts/requirement-consistency-analysis.md`.
2. Inventory source, version, time, actor, platform, and applicability scope. State the limitation when a comparison artifact is missing.
3. Compare terminology, identifiers, formats, states, rules, and behavior using stable keys; preserve evidence and relationship per item.
4. Distinguish `aligned`, `inconsistent`, `missing`, `stale`, and `unassessed`. Mark explicit mutual exclusion as `conflict` instead of silently merging it.
5. Provide impact, priority, owner role, open question, close condition, and validation method.

## Core Constraints

- Use `RC-##` finding IDs; each row includes source pair, comparison key, status, evidence, scope/version, impact, and action.
- Do not treat similar names as synonyms and do not call one source consistent merely because a second source is absent.
- Do not compare across versions or applicability scopes as if they were one fact. Use `stale`/`unassessed` when scope is unclear.
- Suggest `requirement-conflict-detection` for explicit mutually exclusive rules by Skill name only; do not link its internal files.
- Do not invent state transitions, field meaning, platform support, or a final specification.

## Progressive Disclosure

- Always read `prompts/requirement-consistency-analysis.md` before producing an analysis.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; structural gates do not prove cross-source semantic correctness.

## Pre-delivery Checklist

- [ ] Each comparison conclusion cites source, version/scope, and minimum evidence
- [ ] Aligned, inconsistent, missing, stale, and unassessed are distinguished
- [ ] Explicit conflict is not silently merged or incorrectly downgraded
- [ ] P0/P1 issues have owner role, decision question, and validation method
- [ ] Names, document existence, and static tables are not presented as runtime results

## Common Pitfalls

- Treating similar terms as the same object without evidence.
- Ignoring document version, publication time, platform, tenant, or region.
- Filling one source's omissions with another source's unstated defaults.
- Rewriting conflicting statements into an unapproved compromise rule.
