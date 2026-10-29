---
name: performance-test-gatling
description: Use this skill when you need Gatling performance scope, simulations, or runnable entry points; triggers include Gatling, Gatling simulations, and Gatling performance testing.
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

# performance-test-gatling (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need performance outputs that should land in Gatling structure.
- The project already uses Gatling or wants Gatling-ready scenarios.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Domain Execution Essentials

1. Read project Gatling/plugin/JDK and Java/Scala/Kotlin DSL versions, retaining its layout. Use compatible injection/assertion APIs in one DSL. Offline test-compile generated assets with the project build; uncached dependencies mean BLOCKED, not a passed compile.
2. Open models control user arrivals; arrivals equal request RPS only for one request per user without additional loops/retries. Closed models control concurrency; verify RPS from actual request counts/windows.
3. Calculate feeder consumption per user/loop. Queue exhaustion must visibly fail; circular reuse requires policy permission and non-conflicting identities/business keys.
4. Use project thresholds and version-supported assertions. Missing gates yield an unconfigured skeleton, not invented 500ms/1% values. Compile, achieved load, and SLO results are distinct evidence.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions; with no SLA/traffic, label every number as Assumption and list Open Questions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide; secrets are placeholders / env vars only — never real tokens.
- Keep output executable: concrete scenarios, clear priority, clear next steps.
- Default to only the most critical 1–2 scenario types — do not run baseline/load/stress/spike/soak all by default.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Before producing output, read and follow `prompts/performance-test-gatling.md` (minimum coverage, output structure, quality bar).
- When a ready-made template fits: use matching files under `output-templates/`.
- When the user wants examples or alignment with existing assets: read relevant `examples/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: target scenarios, load model, test data or feeder needs, ramp profile, thresholds, environment and monitoring, priority bottlenecks, reporting needs, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.

- To check DSL/JMX assets and data-consumption boundaries, read [evals/fixtures/java-dsl/README.md](evals/fixtures/java-dsl/README.md); local examples calibrate assets and cannot establish acceptance without project gates.
