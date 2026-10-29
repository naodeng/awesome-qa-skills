---
name: automation-testing
description: Use this skill when you need to design automation testing approaches using patterns like POM, data-driven testing, or BDD; triggers include automation testing and test automation strategy.
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

# Automation Testing (English)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need help with automation testing in a real project context.
- Need an output that can be used directly for execution, review, or follow-up.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Domain Execution Essentials

1. Select using candidate flow | protection obligation | repeat-frequency evidence | oracle/observability | isolation/cleanup | stability | maintenance constraint | adopt/defer rationale. Keep ROI cost scenarios separate; returns cannot remedy missing oracles or authority.
2. Reuse the existing framework. First require observable postconditions, independent data, and a CI entry that propagates failure. Defer unmet candidates with unblock conditions.
3. Specify unique identities/business keys, setup, actions, business postconditions, failure signal, and teardown. Failed assertions must fail runner/CI, not merely log.
4. Separate candidate selection, generated assets, real runs, and business acceptance. Rapidly changing prototypes or non-isolatable real payments may need Human/controlled verification, with evidence-based tradeoffs.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Before producing output, read and follow `prompts/automation-testing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: scope and objective, automation candidates, manual-only areas, priority by risk and ROI, framework alignment, data and environment needs, flaky-test risks, CI or execution strategy, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
