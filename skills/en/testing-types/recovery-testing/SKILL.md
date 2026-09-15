---
name: recovery-testing
description: Use this skill when you need evidence-bounded recovery-testing analysis and validation preparation; triggers include 恢复测试 and recovery-testing.
---

# Recovery Testing

## When to Use

- Use this Skill when the work needs evidence-bounded analysis of recovery point, recovery time, recovery steps, validation evidence, and human takeover.
- Use it when the input is incomplete but a reviewable first draft with assumptions and gaps is still useful.
- Use it when static design evidence must remain separate from planned validation and completed execution.

## Output Format Options

- Default to Markdown organized by risk, evidence, and priority.
- If the user asks for a table, CSV, JSON, or ticket format, preserve the same finding fields and evidence states.
- Confirm the schema, enum values, and required fields before feeding the output to automation.

## How to Use

1. Read prompts/recovery-testing.md and follow its input audit, coverage checklist, and output order.
2. Extract scope, environment, version, dependencies, constraints, success criteria, and available evidence.
3. Model recovery point, recovery time, recovery steps, validation evidence, and human takeover with scenarios and decision criteria, prioritizing high-impact or hard-to-detect items.
4. Separate facts, evidence-backed inferences, candidate recommendations, and Human decisions.
5. When information is missing, deliver a bounded draft and the smallest evidence-gathering actions; do not write recommendations as execution results.

## Reference Files

- Read prompts/recovery-testing.md for every invocation; it is the complete execution contract.
- Read evals/eval.yaml and the matching evals/cases/ when evaluating the Skill.
- Read references/, examples/, scripts/, or output-formats.md only when the directory exists and the task needs it.

## Core Constraints

- Analyze only recovery point, recovery time, recovery steps, validation evidence, and human takeover; do not inject faults, access real dependencies, or call production systems.
- Do not invent thresholds, availability, recovery times, vulnerability states, or completed test runs.
- Mark unsupported claims as pending, blocked, or unassessed and provide a validation method.
- Leave risk acceptance, release approval, and Human takeover to a Human.

## Delivery Self-Check

- [ ] Complete the six-part input audit and mark evidence freshness.
- [ ] Cover the recovery objective, failure modes, expected concerns, and validation method.
- [ ] Separate facts, inferences, recommendations, gaps, and Human decisions.
- [ ] Do not turn static design or a dry-run into a claim of execution, passing, or release.

## Common Pitfalls

- Treating adjacent performance, incident, or API analysis as a complete substitute for Recovery Testing.
- Listing steps without triggers, expected results, owner roles, or close conditions.
- Refusing incomplete input, or filling critical facts with template assumptions.

## Best Practices

- Start with the paths most likely to cause business loss or recovery failure.
- Use the smallest isolated and reversible validation suggestion, with explicit stop conditions.
- Make every conclusion reviewable by another engineer from its evidence and boundary.
