---
name: llm-hallucination-testing
description: Use this skill when you need evidence-bounded claim-to-source relations, unsupported assertions, abstention, uncertainty, and evidence review; triggers include LLM 幻觉 and LLM hallucination.
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

# LLM Hallucination Testing

## When to Use

- Use this skill when you need evidence-bounded analysis, design, or validation preparation for claim-to-source relations, unsupported assertions, abstention, uncertainty, and evidence review.
- Use it to review an Agent, RAG, or LLM plan, result, or evidence set and produce actionable improvements.
- Use it when context is incomplete but a bounded first pass with assumptions, gaps, and human-decision boundaries is still useful.

## Output Format Options

- Default to Markdown organized by domain risk, evidence state, priority, and boundary.
- When the user requests tables, CSV, JSON, or ticket fields, preserve the same finding fields, evidence, and decision boundaries.
- Before machine consumption, confirm the schema, enums, required fields, and evidence sources.

## How to Use

1. Read and follow `prompts/llm-hallucination-testing.md`, including its input audit, domain coverage, and output order.
2. Extract scope, environment, version, time window, constraints, success criteria, and available evidence, with attention to claim-to-source relation, unsupported assertion, abstention, uncertainty, evidence review.
3. Separate confirmed facts, evidence-backed inferences, candidate recommendations, and Human decisions before ranking by risk and evidence strength.
4. Turn high-risk items into preconditions, steps, expected behavior or decision criteria, required evidence, and a validation method.
5. When input is incomplete, deliver a bounded first pass, state unsupported conclusions, and never present static material as execution evidence.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Always read `prompts/llm-hallucination-testing.md`; it is the complete execution specification for this skill.
- For evaluation, read `evals/eval.yaml` and the matching cases under `evals/cases/`.
- Load `references/`, `examples/`, `scripts/`, or `output-formats.md` only when those directories exist and the task needs them.

## Domain Execution Essentials

1. Split independently checkable claims including numbers/units, entities, conditions, dates, and citations. Assign IDs, retaining original answer text and evidence version/location.
2. SUPPORTED means evidence supports the same scope; CONTRADICTED means explicit opposing evidence; MISSING_SOURCE means no supplied support or direct contradiction; UNASSESSABLE means inaccessible, unclear-scope, or outdated evidence prevents comparison. Missing support alone does not prove fabrication.
3. Check citation existence, accessibility, relevance, and claim support separately. A real source with an opposing number is a contradiction; do not label an entire mixed paragraph at once.
4. Preserve claim denominators and separate supported rates from unknown proportions. Without ground truth or adequate sampling provide the check plan, not factual-accuracy proof.

## Core Constraints

- Keep the analysis focused on claim-to-source relations, unsupported assertions, abstention, uncertainty, and evidence review; do not replace business owners or Human risk acceptance, exception approval, or safety decisions.
- Never invent system behavior, fields, model outputs, data, thresholds, root causes, execution records, or pass claims.
- Static design, plans, file presence, or a dry run retain their evidence state and cannot become proof of real execution.
- When evidence is insufficient, use pending confirmation, blocked, unassessed, or NOT_SCORED and give the smallest validation method.
- For user data, production, or safety work, use least privilege, masked data, mocks, dry runs, or isolation.

## Delivery Checklist

- [ ] Covered claim-to-source relation, unsupported assertion, abstention, uncertainty, evidence review, with source, evidence state, and validation method for each.
- [ ] Separated facts, inferences, candidate recommendations, gaps, and Human decisions.
- [ ] Gave high-risk items P0/P1/P2/P3 or an equivalent priority, owner role, and close condition.
- [ ] Did not turn plans, static checks, or dry runs into test execution, all-passed, or safety-approved claims.
- [ ] Stated residual risk, stop/escalation conditions, and next actions.

## Common Pitfalls

- Listing checks without triggers, expected concerns, owner roles, close conditions, and evidence.
- Treating adjacent tests or model tools as a complete LLM hallucination judgment.
- Using unexplained numbers for false precision or writing correlation as causation.
- Refusing incomplete input, or pretending that incomplete evidence is conclusive.

## Best Practices

- Start with paths most likely to cause user harm, business loss, or decision blockage.
- Use the smallest verifiable experiment to reduce uncertainty and record conditions, versions, sources, and evidence.
- Make the Skill independently installable, executable, and reviewable by another engineer.
