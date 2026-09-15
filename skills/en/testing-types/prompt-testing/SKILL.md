---
name: prompt-testing
description: Use this skill when you need to test prompt behavior, regression risk, and output boundaries across versions; triggers include prompt testing and prompt-regression.
---

# Prompt Testing

## When to Use

- Use this skill when you need to verify prompts for correctness, consistency, and control across representative, boundary, adversarial, and version-change cases.
- Use the `prompt-regression` mode when comparing a baseline and candidate version with pinned dataset or test-prompt identity, observed differences, and evidence state.
- Use it to review an existing plan, result, or evidence set and produce actionable improvements.
- Use it when context is incomplete but a bounded first pass is still valuable.

## Output Format Options

- Default to Markdown for review, execution, and incremental refinement.
- When the user requests tables, CSV, JSON, or ticket fields, preserve risk, evidence, priority, and boundary information.
- For machine-consumed output, confirm the schema, enums, and required fields first.

## How to Use

1. Read and follow `prompts/prompt-testing.md`, including its input contract, execution rules, minimum coverage, and output order.
2. Select ordinary testing or `prompt-regression`; regression mode requires the baseline, candidate version, dataset or test-prompt identity, and comparability context.
3. Add only context that changes the decision: scope, environment, version, constraints, evidence, and success criteria.
4. Audit the input, then separate confirmed facts, working assumptions, and open questions.
5. Rank by risk and evidence strength, and produce an artifact that can be executed or reviewed directly.
6. If information is missing, deliver a bounded first pass and state which conclusions remain unsupported.

## Reference Files

- Always read `prompts/prompt-testing.md`; it is the complete execution specification for this skill.
- For evaluation or regression, read `evals/eval.yaml` and the relevant cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Core Constraints

- do not test one example only
- pin model and parameters
- use rubrics rather than brittle exact matches for semantic output
- Never invent system behavior, fields, data, metrics, or root causes absent from the evidence.
- Link important conclusions to evidence; mark unsupported conclusions as hypotheses with a verification method.
- Explain priority using business impact, likelihood, or detectability.
- In `prompt-regression`, use `PRT-##` finding IDs and distinguish baseline, candidate version, expected behavior, observed behavior, difference, and validation method.
- Treat version differences as evidence-bounded comparisons; static analysis must not become a claim that a model ran or regression passed.

## Delivery Checklist

- [ ] Covered: instruction following, format, factuality, boundary inputs, adversarial inputs, multilingual behavior, consistency, regression, cost.
- [ ] Separated facts, assumptions, gaps, and recommendations.
- [ ] Gave high-risk items a priority, evidence basis, owner or next action.
- [ ] Defined verifiable decision criteria instead of generic advice.
- [ ] For regression, preserved dataset or test-prompt identity, evidence state, differences, and the Human decision boundary.
- [ ] Performed no unauthorized production writes or destructive actions.

## Common Pitfalls

- Listing checks without preconditions, expected outcomes, or evidence.
- Marking everything high priority and avoiding tradeoffs.
- Substituting tool names or generic theory for domain reasoning.
- Refusing incomplete input, or pretending incomplete evidence supports certainty.
- Treating a surface difference between candidate and baseline as a regression defect without checking comparability or evidence state.

## Best Practices

- Start with paths most likely to cause business loss, safety issues, or release blockage.
- Reduce uncertainty through the smallest verifiable experiment and record reproduction conditions.
- Make the artifact executable and independently reviewable by another engineer.
