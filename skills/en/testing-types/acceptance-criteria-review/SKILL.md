---
name: acceptance-criteria-review
description: Use this skill when you need to review acceptance criteria for ambiguity, missing rules, and verifiability; triggers include acceptance criteria review.
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

# Acceptance Criteria Review

## When to Use

- Use this skill when you need to review existing acceptance criteria and separately propose verifiable rewrites or identify undefined rules.
- Use it to review an existing plan, result, or evidence set and produce actionable improvements.
- Use it when context is incomplete but a bounded first pass is still valuable.

## Output Format Options

- Default to Markdown for review, execution, and incremental refinement.
- When the user requests tables, CSV, JSON, or ticket fields, preserve risk, evidence, priority, and boundary information.
- For machine-consumed output, confirm the schema, enums, and required fields first.

## How to Use

1. Read and follow `prompts/acceptance-criteria-review.md`, including its input contract, execution rules, minimum coverage, and output order.
2. Add only context that changes the decision: scope, environment, version, constraints, evidence, and success criteria.
3. Audit the input, then separate confirmed facts, working assumptions, and open questions.
4. Rank by risk and evidence strength, and produce an artifact that can be executed or reviewed directly.
5. If information is missing, deliver a bounded first pass and state which conclusions remain unsupported.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Always read `prompts/acceptance-criteria-review.md`; it is the complete execution specification for this skill.
- For evaluation or regression, read `evals/eval.yaml` and the relevant cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Domain Execution Essentials

1. Select `review` (check existing criteria), `proposed-rewrite` (suggest a rewrite), or `missing-rule` (undefined policy). Retain each original AC ID, version, text, and source; a proposal never replaces the source rule.
2. Produce: AC ID | original criterion | mode | observable oracle | proposed wording | reason for change | product confirmation. Leave undefined rules open.
3. For each comparison, split below/equal/above inputs using the supplied operator. For repeated requests capture the business key, cumulative refund, refundable balance, and persisted state; a successful response does not prove correct accounting.
4. Proposed Given/When/Then wording includes observable data and error paths. Mark a sufficiently defined criterion testable instead of manufacturing ambiguity.
## Core Constraints

- do not decide missing business rules on behalf of product owners
- make every criterion observable
- escalate ambiguities that block implementation or testing
- Never invent system behavior, fields, data, metrics, or root causes absent from the evidence.
- Link important conclusions to evidence; mark unsupported conclusions as hypotheses with a verification method.
- Explain priority using business impact, likelihood, or detectability.

## Delivery Checklist

- [ ] Covered: testability and observable outcomes, happy, failure, and boundary paths, roles and permissions, data rules, state transitions, dependency failures, non-functional constraints, ambiguities.
- [ ] Separated facts, assumptions, gaps, and recommendations.
- [ ] Gave high-risk items a priority, evidence basis, owner or next action.
- [ ] Defined verifiable decision criteria instead of generic advice.
- [ ] Performed no unauthorized production writes or destructive actions.

## Common Pitfalls

- Listing checks without preconditions, expected outcomes, or evidence.
- Marking everything high priority and avoiding tradeoffs.
- Substituting tool names or generic theory for domain reasoning.
- Refusing incomplete input, or pretending incomplete evidence supports certainty.

## Best Practices

- Start with paths most likely to cause business loss, safety issues, or release blockage.
- Reduce uncertainty through the smallest verifiable experiment and record reproduction conditions.
- Make the artifact executable and independently reviewable by another engineer.
