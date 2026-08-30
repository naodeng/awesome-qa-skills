---
name: performance-bottleneck-analysis
description: Use this skill when you need to form evidence-based performance bottleneck hypotheses and validation steps; triggers include performance bottleneck analysis.
---

# Performance Bottleneck Analysis

## When to Use

- Use this skill when you need to combine load, metrics, and traces to locate resources or code paths limiting throughput or latency.
- Use it to review an existing plan, result, or evidence set and produce actionable improvements.
- Use it when context is incomplete but a bounded first pass is still valuable.

## Output Format Options

- Default to Markdown for review, execution, and incremental refinement.
- When the user requests tables, CSV, JSON, or ticket fields, preserve risk, evidence, priority, and boundary information.
- For machine-consumed output, confirm the schema, enums, and required fields first.

## How to Use

1. Read and follow `prompts/performance-bottleneck-analysis.md`, including its input contract, execution rules, minimum coverage, and output order.
2. Add only context that changes the decision: scope, environment, version, constraints, evidence, and success criteria.
3. Audit the input, then separate confirmed facts, working assumptions, and open questions.
4. Rank by risk and evidence strength, and produce an artifact that can be executed or reviewed directly.
5. If information is missing, deliver a bounded first pass and state which conclusions remain unsupported.

## Reference Files

- Always read `prompts/performance-bottleneck-analysis.md`; it is the complete execution specification for this skill.
- For evaluation or regression, read `evals/eval.yaml` and the relevant cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Core Constraints

- validate the workload model first
- require multiple signals for bottleneck claims
- do not equate high utilization with root cause
- Never invent system behavior, fields, data, metrics, or root causes absent from the evidence.
- Link important conclusions to evidence; mark unsupported conclusions as hypotheses with a verification method.
- Explain priority using business impact, likelihood, or detectability.

## Delivery Checklist

- [ ] Covered: throughput knee, queuing, CPU, memory and GC, I/O, lock contention, connection pools, downstream dependencies.
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
