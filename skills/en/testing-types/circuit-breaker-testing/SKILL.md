---
name: circuit-breaker-testing
description: Use this skill when you need evidence-bounded circuit-breaker-testing analysis and validation preparation; triggers include 熔断器测试 and circuit-breaker-testing.
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

# Circuit-Breaker Testing

## When to Use

- Use this Skill when the work needs evidence-bounded analysis of closed, open, and half-open states, threshold evidence, recovery probes, and fallback.
- Use it when the input is incomplete but a reviewable first draft with assumptions and gaps is still useful.
- Use it when static design evidence must remain separate from planned validation and completed execution.

## Output Format Options

- Default to Markdown organized by risk, evidence, and priority.
- If the user asks for a table, CSV, JSON, or ticket format, preserve the same finding fields and evidence states.
- Confirm the schema, enum values, and required fields before feeding the output to automation.

## How to Use

1. Read prompts/circuit-breaker-testing.md and follow its input audit, coverage checklist, and output order.
2. Extract scope, environment, version, dependencies, constraints, success criteria, and available evidence.
3. Model closed, open, and half-open states, threshold evidence, recovery probes, and fallback with scenarios and decision criteria, prioritizing high-impact or hard-to-detect items.
4. Separate facts, evidence-backed inferences, candidate recommendations, and Human decisions.
5. When information is missing, deliver a bounded draft and the smallest evidence-gathering actions; do not write recommendations as execution results.

## Reference Files

- Read prompts/circuit-breaker-testing.md for every invocation; it is the complete execution contract.
- Read evals/eval.yaml and the matching evals/cases/ when evaluating the Skill.
- Read references/, examples/, scripts/, or output-formats.md only when the directory exists and the task needs it.

## Domain Execution Essentials

- Extract failure-count definitions, rolling/consecutive window, threshold, open duration, half-open probe/concurrency allowance, and success/failure transitions.
- Deliver pre-state/count/action/post-state/fallback per event, distinguishing probes from ordinary calls; state labels are not behavior evidence.
- When deriving domain candidates, read and follow [prompts/circuit-breaker-testing.md](prompts/circuit-breaker-testing.md) for the domain procedure and oracle; retain valid controls, evidence gaps, and validation actions for each item.

## Core Constraints

- Analyze only closed, open, and half-open states, threshold evidence, recovery probes, and fallback; do not inject faults, access real dependencies, or call production systems.
- Do not invent thresholds, availability, recovery times, vulnerability states, or completed test runs.
- Mark unsupported claims as pending, blocked, or unassessed and provide a validation method.
- Leave risk acceptance, release approval, and Human takeover to a Human.

## Delivery Self-Check

- [ ] Complete the six-part input audit and mark evidence freshness.
- [ ] Cover the circuit-breaker state, failure modes, expected concerns, and validation method.
- [ ] Separate facts, inferences, recommendations, gaps, and Human decisions.
- [ ] Do not turn static design or a dry-run into a claim of execution, passing, or release.

## Common Pitfalls

- Treating adjacent performance, incident, or API analysis as a complete substitute for Circuit-Breaker Testing.
- Listing steps without triggers, expected results, owner roles, or close conditions.
- Refusing incomplete input, or filling critical facts with template assumptions.

## Best Practices

- Start with the paths most likely to cause business loss or recovery failure.
- Use the smallest isolated and reversible validation suggestion, with explicit stop conditions.
- Make every conclusion reviewable by another engineer from its evidence and boundary.
