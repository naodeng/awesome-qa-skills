---
name: business-rule-extraction
description: Use this skill when requirements, policies, contracts, or workflows need traceable business rules extracted before design or testing; triggers include business rule extraction, policy rule inventory, and atomic rule analysis.
---

# Business Rule Extraction

Extract traceable atomic business rules from requirements, policies, contracts, workflows, acceptance criteria, and supplied examples while retaining sources, applicability, exceptions, and unknowns. This is an inventory and analysis input, not business, compliance, or release approval.

## When to Use

- Use it when scattered prose must become comparable and verifiable `BR-##` entries.
- Use it when actors, objects, triggers, preconditions, actions, outcomes, invariants, or exceptions need to be explicit.
- Use it when sources are incomplete or conflicting and a bounded first-pass rule inventory is still useful.

Do not use it to invent rules from general knowledge, choose final precedence, execute system verification, or approve a policy for a business or compliance role.

## Workflow

1. Read and follow `prompts/business-rule-extraction.md`, auditing objective, version, time, and applicability first.
2. Classify inputs as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`; preserve each source and location.
3. Merge sentences only when the material supports the merge; otherwise create atomic rules with a stable `BR-##`, source, and minimum evidence.
4. Separate direct facts, evidence-backed inferences, recommendations, and Human decisions; list exceptions, unknowns, impact, and validation hints separately.
5. Deliver a bounded first pass when information is missing and ask assignable, closeable evidence questions instead of upgrading assumptions to facts.

## Core Constraints

- Do not invent thresholds, precedence, state transitions, permissions, default exceptions, or applicability.
- Do not turn examples, recommendations, document presence, or name matching into execution, pass, approval, or release evidence.
- Every `BR-##` should contain rule, source, actor/object, trigger, preconditions, action/outcome, constraint/invariant, exception, evidence, unknowns, impact, and validation method.
- Preserve both sides of a conflict; use `missing`, `stale`, or `unassessed` when the material cannot support a choice.

## On-Demand Loading

- Always read `prompts/business-rule-extraction.md` before producing an analysis.
- For regression, read `evals/eval.yaml` and the relevant `evals/cases/`; these files do not prove that business semantics ran.
- To inspect trigger behavior, use `evals/trigger-prompts.csv` and `evals/local-rules.json` with the repository trace runner; without `skill.selection` evidence report `BLOCKED`.
- This is a repository-root development check; a standalone Skill package does not include the repository runner and does not depend on it at runtime.

## Delivery Checklist

- [ ] Record the six input-audit categories and applicability scope.
- [ ] Trace every `BR-##` to minimum source evidence.
- [ ] Separate facts, inferences, recommendations, and Human decisions.
- [ ] Retain exceptions, conflicts, unknowns, and validation hints.
- [ ] Do not present static material or a rule inventory as runtime, approval, or release evidence.

## Common Pitfalls

- Merging similar sentences while losing version or regional scope.
- Filling “usually,” “timely,” or “reasonable” with an assumed threshold.
- Reporting rule prose without sources, exceptions, evidence, or open questions.
