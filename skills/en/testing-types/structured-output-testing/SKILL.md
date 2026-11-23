---
name: structured-output-testing
description: Use this skill when you need to verify JSON or other structured model outputs against schemas, required fields, enums, and semantic oracles; triggers include structured output testing, JSON Schema validation, and 结构化输出测试.
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

# Structured Output Testing

## When to Use

- Verify JSON, tool arguments, structured fields, or enums emitted by an LLM or agent.
- Separate JSON parsing, schema constraints, and domain-semantic failures.
- Trace output versions, run parameters, samples, and failure evidence without treating one sample as an overall quality result.

## Output Format Options

- Default to Markdown with structural checks, semantic checks, evidence, and conclusion boundaries.
- Before machine consumption, confirm the schema, required fields, types, enums, additional-field policy, and evidence-status field.

## How to Use

1. Read and follow `prompts/structured-output-testing.md` for the workflow, minimum coverage, and output contract.
2. Obtain the project schema, field meanings, required fields, enums, unknown-field policy, and semantic oracle; state gaps when they are unavailable.
3. Parse JSON, validate the schema, and then apply the domain oracle, recording each layer separately.
4. Pin and trace input, model, prompt, dataset, schema version, parameters, and repetition count.
5. When evidence is incomplete, deliver a bounded test design and set `evaluation_status` to `NOT_RUN`, `BLOCKED`, or `UNKNOWN`; never invent a pass result.

## Reference Files

- Read `prompts/structured-output-testing.md` for every task; it is the full execution specification.
- For this skill's regression cases, read `evals/eval.yaml` and the matching files under `evals/cases/`.
- Read `references/`, `examples/`, `scripts/`, or `output-formats.md` only when they exist and the task needs them.

## Core Constraints

- `parse_status`, `schema_status`, and `semantic_status` are independent results; parseable JSON does not prove field or business correctness.
- Every conclusion must trace to a sample, version, parameter, run record, or redacted output reference.
- Separate one observation from distribution-level conclusions; report repetitions, failure counts, and denominators.
- Do not invent field constraints, semantic expectations, or business acceptance thresholds.

## Evaluation Evidence Status

- Include `evaluation_status`: `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, or `UNKNOWN` for evaluation conclusions.
- `PASS` requires in-scope runtime records and evidence for every required assertion. Use `NOT_RUN` when no run results exist, `BLOCKED` when execution was prevented, and `UNKNOWN` when evidence is insufficient. A plan, static check, or file presence alone cannot prove `PASS`.
- Trace `trace_id`, sample and version identity, parameters, run/trial, parse, schema, semantic status, and evidence reference; decide those checks separately.

## Delivery Checklist

- [ ] Confirmed schema version, required fields, types, enums, and additional-field policy.
- [ ] Judged JSON parseability, structural conformance, and semantic correctness separately.
- [ ] Recorded input/run identity, parameters, repetitions, denominator, and evidence references.
- [ ] Did not report `PASS` when results are missing; stated the smallest next action.

## Common Pitfalls

- Treating valid JSON as schema-conformant or business-correct.
- Comparing permitted paraphrases only by exact string equality.
- Losing model, prompt, schema, or dataset versions and making regression comparisons invalid.
- Claiming stability from one passing sample or using pass when evidence is absent.
