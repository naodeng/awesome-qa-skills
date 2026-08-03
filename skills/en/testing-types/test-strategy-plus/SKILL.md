---
name: test-strategy-plus
description: Use this skill when you need a structured test strategy from requirement, analysis, tech, and plan docs; triggers include test strategy plus and advanced test strategy.
---

# test-strategy-plus (EN)

**中文版：** See the corresponding Chinese skill.

## When to Use

- Need a fuller strategy with milestones, gates, ownership, and tradeoffs.
- Need a stronger planning artifact than the base strategy version.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- Before producing output, read and follow `prompts/test-strategy-plus.md` (minimum coverage, output structure, quality bar).
- When a ready-made template fits: use matching files under `output-templates/`.
- When the user wants examples or alignment with existing assets: read relevant `examples/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: objectives and scope, risk priorities, test methods and depth, resource and ownership plan, milestones, quality gates, entry or exit thinking, environment and data strategy, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
