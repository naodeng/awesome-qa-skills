---
name: test-scope-analysis
description: Use this skill when a test activity, iteration, release, or risk review needs explicit inclusion, exclusion, depth, and expansion boundaries before execution; triggers include test scope analysis, test boundary review, and release test scoping.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Test Scope Analysis

Analyze goals, product surface, changes/risks, constraints, existing assets, platforms, roles, data, and environments before testing. Produce `TS-##` inclusion/exclusion, depth, dependencies, stop conditions, expansion triggers, and residual risk. This is not a full test strategy, test selection, or test execution.

## When to Use

- Use it to define explainable boundaries for an iteration, release, change, or risk review.
- Use it to make core journeys, direct/transitive impact, non-functional scope, migration compatibility, and unassessed areas explicit.
- Use it when context is incomplete but a bounded scope draft and evidence questions are useful.

Do not use it to execute tests, generate a complete strategy, or claim full coverage/zero risk without evidence.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read `prompts/test-scope-analysis.md` and audit objective, version, scope, risk, and constraints.
2. Classify input as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`.
3. Record inclusion, exclusion, depth, dependencies, stop conditions, expansion triggers, evidence, and owner role in `TS-##` entries.
4. Separate scope facts, risk inferences, recommendations, and Human decisions; give a verifiable reason for every tradeoff.
5. Deliver a bounded scope and expansion criteria when context is missing; never upgrade a scope statement into coverage proof.

## Domain Execution Essentials

1. Build scope cells for version×layer×platform×data state from the delivery objective, linked to requirements, include/exclude evidence, owners, and observable acceptance. New-feature scope is broader than change-only regression.
2. Separate INCLUDE, EXCLUDE, and UNKNOWN. Exclusions need a sourced scope or independent-contract reason; unclear platform/data/boundary support cannot mean 'do not test'.
3. Record budget/environment/authority blockers and residual risk. Escalate unmet critical obligations rather than inventing product boundaries or accepting risk.
4. Changes in requirements, platforms, interfaces, or versions trigger reassessment. Selection/design, execution, and satisfaction remain separate; a checklist is not coverage proof.

## Core Constraints

- Do not generate a full test strategy, choose a concrete executable set, or execute tests.
- Do not use changed-file names, test names, scope tables, or static checks as coverage/pass evidence.
- Each `TS-##` includes goal/object, included, excluded, rationale, depth, platform/role/data/environment dependencies, stop conditions, expansion triggers, residual risk, source, and owner.
- Without risk, execution, or environment evidence, mark status `unassessed`, `unverified`, or `unexecuted`.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Always read `prompts/test-scope-analysis.md` before producing an analysis.
- For regression, read `evals/eval.yaml` and its cases; a scope draft does not prove testing ran.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Delivery Checklist

- [ ] Record objective, version, scope, and six-part input audit.
- [ ] Give every `TS-##` inclusion/exclusion, depth, dependencies, stop, and expansion conditions.
- [ ] Cover core/transitive impact, non-functional, migration compatibility, and unassessed areas.
- [ ] Give each tradeoff source, impact, and validation method.
- [ ] Do not present a bounded scope as coverage proof, execution evidence, or release conclusion.

## Common Pitfalls

- Treating “test only the core flow” as proof that non-core paths are safe.
- Replacing scope rationale and risk evidence with test or file counts.
- Having no expansion trigger when change or risk evidence evolves.
