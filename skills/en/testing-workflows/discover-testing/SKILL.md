---
name: discover-testing
description: Use this skill when you need to route a request to the right testing skill before execution; triggers include discover testing, testing skill router, and which testing skill.
---

# Testing Skill Discovery (English)

**中文版：** See the corresponding Chinese skill.

## When to Use

- Need to decide which testing skill should be used before execution.
- The request mixes multiple testing directions or phases.

## Workflow

1. Read the user request and first identify the capability stage (Core QA / Engineering QA / Production Quality / AI Native QA) and primary testing goal.
2. Follow the routing prompt under `prompts/`: pick 1 primary skill; add at most 1 helper only when needed.
3. Hand the request to the target skill; do not execute the full testing work inside this router skill.

## Core Constraints

- Recommend few skills — avoid menu dumping.
- If the target skill is already obvious, say so directly.
- Make the route actionable: name the skill and the reason.
- Use `ai-assisted-testing` for AI for QA; Testing for AI belongs to AI Native QA. Until roadmap Skills are installed, never recommend them as callable primary Skills.

## Progressive Disclosure

- Before producing output, read and follow `prompts/discover-testing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.
- For step ↔ prompt mapping: read `reference.md`.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: main goal, best-fit primary skill, optional supporting skill, why this choice fits, next step to continue work (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not recommend many skills at once.
- Do not turn skill selection into full test execution.
- Do not pretend a route is complete when information is insufficient.
