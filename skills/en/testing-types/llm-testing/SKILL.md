---
name: llm-testing
description: Use this skill when you need to test LLM behavior, failure modes, and evidence-based quality boundaries; triggers include llm testing.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.1.1"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# LLM Testing

## When to Use

- Use this skill when you need to test LLM applications for task quality, robustness, safety, factuality, and version regressions.
- Use it to review an existing plan, result, or evidence set and produce actionable improvements.
- Use it when context is incomplete but a bounded first pass is still valuable.

## Output Format Options

- Default to Markdown for review, execution, and incremental refinement.
- When the user requests tables, CSV, JSON, or ticket fields, preserve risk, evidence, priority, and boundary information.
- For machine-consumed output, confirm the schema, enums, and required fields first.

## How to Use

1. Read and follow `prompts/llm-testing.md`, including its input contract, execution rules, minimum coverage, and output order.
2. Add only context that changes the decision: scope, environment, version, constraints, evidence, and success criteria.
3. Audit the input, then separate confirmed facts, working assumptions, and open questions.
4. Rank by risk and evidence strength, and produce an artifact that can be executed or reviewed directly.
5. If information is missing, deliver a bounded first pass and state which conclusions remain unsupported.

## Reference Files

- Always read `prompts/llm-testing.md`; it is the complete execution specification for this skill.
- For evaluation or regression, read `evals/eval.yaml` and the relevant cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Core Constraints

- Keep boundaries with feature, Prompt, and Eval design explicit; stratify samples by risk and report repetition denominators, token/cost provenance, and latency metrics with sample counts.

- avoid exact-string assertions alone
- pin and record model settings
- evaluate stochastic outputs with repetitions and distributions
- Never invent system behavior, fields, data, metrics, or root causes absent from the evidence.
- Link important conclusions to evidence; mark unsupported conclusions as hypotheses with a verification method.
- Explain priority using business impact, likelihood, or detectability.

## Evaluation Evidence Status

- Include `evaluation_status`: `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, or `UNKNOWN` for evaluation conclusions.
- `PASS` requires in-scope runtime records and evidence for every required assertion. Use `NOT_RUN` when no run results exist, `BLOCKED` when execution was prevented, and `UNKNOWN` when evidence is insufficient. A plan, static check, or file presence alone cannot prove `PASS`.
- Trace `trace_id`, sample and version identity, parameters, run/trial, parse, schema, semantic status, and evidence reference; decide those checks separately.

## Delivery Checklist

- [ ] Covered: instruction following, factuality, robustness, safety, bias, context length, multilingual behavior, stochasticity, cost and latency.
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
