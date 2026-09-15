---
name: agent-memory-testing
description: Use this skill when you need evidence-bounded memory write/read/update/delete, retention, contamination, isolation, provenance, and forgetting behavior; triggers include Agent 记忆 and Agent memory.
---

# Agent Memory Testing

## When to Use

- Use this skill when you need evidence-bounded analysis, design, or validation preparation for memory write/read/update/delete, retention, contamination, isolation, provenance, and forgetting behavior.
- Use it to review an Agent, RAG, or LLM plan, result, or evidence set and produce actionable improvements.
- Use it when context is incomplete but a bounded first pass with assumptions, gaps, and human-decision boundaries is still useful.

## Output Format Options

- Default to Markdown organized by domain risk, evidence state, priority, and boundary.
- When the user requests tables, CSV, JSON, or ticket fields, preserve the same finding fields, evidence, and decision boundaries.
- Before machine consumption, confirm the schema, enums, required fields, and evidence sources.

## How to Use

1. Read and follow `prompts/agent-memory-testing.md`, including its input audit, domain coverage, and output order.
2. Extract scope, environment, version, time window, constraints, success criteria, and available evidence, with attention to write/read, update/delete, retention, tenant isolation, provenance.
3. Separate confirmed facts, evidence-backed inferences, candidate recommendations, and Human decisions before ranking by risk and evidence strength.
4. Turn high-risk items into preconditions, steps, expected behavior or decision criteria, required evidence, and a validation method.
5. When input is incomplete, deliver a bounded first pass, state unsupported conclusions, and never present static material as execution evidence.

## Reference Files

- Always read `prompts/agent-memory-testing.md`; it is the complete execution specification for this skill.
- For evaluation, read `evals/eval.yaml` and the matching cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Core Constraints

- Keep the analysis focused on memory write/read/update/delete, retention, contamination, isolation, provenance, and forgetting behavior; do not replace business owners or Human risk acceptance, exception approval, or safety decisions.
- Never invent system behavior, fields, model outputs, data, thresholds, root causes, execution records, or pass claims.
- Static design, plans, file presence, or a dry run retain their evidence state and cannot become proof of real execution.
- When evidence is insufficient, use pending confirmation, blocked, unassessed, or NOT_SCORED and give the smallest validation method.
- For user data, production, or safety work, use least privilege, masked data, mocks, dry runs, or isolation.

## Delivery Checklist

- [ ] Covered write/read, update/delete, retention, tenant isolation, provenance, with source, evidence state, and validation method for each.
- [ ] Separated facts, inferences, candidate recommendations, gaps, and Human decisions.
- [ ] Gave high-risk items P0/P1/P2/P3 or an equivalent priority, owner role, and close condition.
- [ ] Did not turn plans, static checks, or dry runs into test execution, all-passed, or safety-approved claims.
- [ ] Stated residual risk, stop/escalation conditions, and next actions.

## Common Pitfalls

- Listing checks without triggers, expected concerns, owner roles, close conditions, and evidence.
- Treating adjacent tests or model tools as a complete Agent memory judgment.
- Using unexplained numbers for false precision or writing correlation as causation.
- Refusing incomplete input, or pretending that incomplete evidence is conclusive.

## Best Practices

- Start with paths most likely to cause user harm, business loss, or decision blockage.
- Use the smallest verifiable experiment to reduce uncertainty and record conditions, versions, sources, and evidence.
- Make the Skill independently installable, executable, and reviewable by another engineer.
