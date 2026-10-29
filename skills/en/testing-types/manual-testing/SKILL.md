---
name: manual-testing
description: Use this skill when you need to plan manual or exploratory testing with charters, heuristics, and session records; triggers include manual testing and exploratory testing.
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

# Manual/Exploratory Testing

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need help with manual testing in a real project context.
- Need an output that can be used directly for execution, review, or follow-up.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Domain Execution Essentials

1. Give each time-box a charter: task/risk, environment/build, data, exploration scope, deadline, and evidence. Track scripted execution and exploration separately within authorization.
2. Record precondition→action→expected→actual→evidence ID→state. Not started is NOT_RUN, interrupted is INCOMPLETE, environment prevention is BLOCKED; a checklist is no execution log.
3. Prepare recoverable data/checkpoints and restore accounts/orders/config according to policy, checking residuals. Unauthorized deletion is not cleanup.
4. Under limited time complete the critical risk loop first, then preserve unfinished work, owners, and restart points. Conclusions cover observations only; missing oracles stay open.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Before producing output, read and follow `prompts/manual-testing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: scope, core journeys, setup and accounts, positive checks, negative checks, boundary checks, exploratory focus areas, evidence to collect, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
