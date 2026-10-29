---
name: regression-optimization
description: Use this skill when you need evidence-bounded tradeoffs among regression selection, ordering, parallelism, caching, and risk preservation; triggers include 回归范围 and regression scope.
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

# Regression Optimization

## When to Use

- Use this skill when you need evidence-bounded analysis, design, or validation preparation for tradeoffs among regression selection, ordering, parallelism, caching, and risk preservation.
- Use it to review a plan, result, or metric and turn the review into executable improvements.
- Use it when input is incomplete but a bounded first pass with assumptions, gaps, and human-decision boundaries is still useful.

## Output Format Options

- Default to Markdown organized by domain risk, evidence state, priority, and boundary.
- When the user requests tables, CSV, JSON, or ticket fields, preserve the same finding fields, evidence, and decision boundaries.
- Before machine consumption, confirm the schema, enums, required fields, and evidence sources.

## How to Use

1. Read and follow `prompts/regression-optimization.md`, including its input audit, domain coverage, and output order.
2. Extract scope, environment, version, time window, constraints, success criteria, and available evidence, with attention to selection basis, ordering, parallelism, caching, risk preservation.
3. Separate confirmed facts, evidence-backed inferences, candidate recommendations, and Human decisions before ranking by risk and evidence strength.
4. Turn high-risk items into preconditions, steps, expected behavior or decision criteria, required evidence, and a validation method.
5. When input is incomplete, deliver a bounded first pass, state unsupported conclusions, and never present static material as execution evidence.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Always read `prompts/regression-optimization.md`; it is the complete execution specification for this skill.
- For evaluation, read `evals/eval.yaml` and the matching cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Domain Execution Essentials

1. Match before/after versions, environment, obligations, data and windows. Source selection/order/parallel/cache inclusions and exclusions; different test volumes cannot support timing comparisons.
2. Preserve critical risks, known escapes and mandatory gates. Reject removal of sole protection; unknown mappings require conservative checks or escalation.
3. Measure duration/resources, detection, misses/escapes and flakiness separately. The same controlled fault must still fail an effective assertion for the same obligation.
4. State benefit conditions, residual risk, implementation/rollback triggers and owners. Removing protection requires authorized acceptance, not an optimization proposal alone.

## Core Constraints

- Keep the analysis focused on tradeoffs among regression selection, ordering, parallelism, caching, and risk preservation; do not replace business owners or Human risk acceptance, exception approval, or release decisions.
- Never invent system behavior, fields, metrics, thresholds, data, root causes, execution records, or pass claims.
- Static design, plans, file presence, or a dry run retain their evidence state and cannot become proof of real execution.
- When evidence is insufficient, use pending confirmation, blocked, unassessed, or NOT_SCORED and give the smallest validation method.
- For production, privacy, or security work, use least privilege, masked data, mocks, dry runs, or isolation.

## Delivery Checklist

- [ ] Covered selection basis, ordering, parallelism, caching, risk preservation, with source, evidence state, and validation method for each.
- [ ] Separated facts, inferences, candidate recommendations, gaps, and Human decisions.
- [ ] Gave high-risk items P0/P1/P2/P3 or an equivalent priority, owner role, and close condition.
- [ ] Did not turn plans, static checks, or dry runs into test execution, all-passed, or release-approved claims.
- [ ] Stated residual risk, stop/escalation conditions, and next actions.

## Common Pitfalls

- Listing checks without triggers, expected concerns, owner roles, close conditions, and evidence.
- Treating adjacent metrics or tool names as a complete regression scope judgment.
- Using unexplained numbers for false precision or writing correlation as causation.
- Refusing incomplete input, or pretending that incomplete evidence is conclusive.

## Best Practices

- Start with paths most likely to cause business loss, quality regression, or decision blockage.
- Use the smallest verifiable experiment to reduce uncertainty and record conditions, versions, sources, and evidence.
- Make the Skill independently installable, executable, and reviewable by another engineer.
