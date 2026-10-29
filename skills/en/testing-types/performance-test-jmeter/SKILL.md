---
name: performance-test-jmeter
description: Use this skill when you need to design JMeter test plans with Thread Groups, samplers, data sets, assertions, timers, CLI runs, and HTML reports; triggers include JMeter performance testing, performance testing, and performance-test-jmeter.
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

# JMeter Performance Testing (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need outputs that should land in a JMeter performance testing workflow.
- The project already uses JMeter or wants JMeter-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/performance-test-jmeter.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- `prompts/performance-test-jmeter.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Domain Execution Essentials

1. Confirm project JMeter/JDK/plugins and JMX version. Check TestPlan/ThreadGroup/Sampler and adjacent hashTree structure, variables, and properties. Parseable XML proves structure only, not execution or SLO success.
2. Standard ThreadGroup controls closed-loop threads. Target RPS needs declared think time/timers, throughput control, or an installed arrival-rate plugin; verify achieved throughput/counts rather than inferring RPS from threads.
3. Record CSV path, encoding, columns, sharing, recycle/stopThread settings and consumption per thread/loop. For distributed runs check each injector's data/plugins/network and load allocation.
4. Use non-GUI entry in authorized environments, preserving JTL/logs. Check business assertions, latency/error gates, and CI propagation separately. Missing thresholds are UNKNOWN; HTML reports or exit 0 cannot hide failed samples.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.

- To check DSL/JMX assets and data-consumption boundaries, read [evals/fixtures/jmx/README.md](evals/fixtures/jmx/README.md); local examples calibrate assets and cannot establish acceptance without project gates.
