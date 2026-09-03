---
name: sprint-testing-workflow
description: Use this skill when you need a sprint-based QA workflow from planning through review and retrospective; triggers include sprint testing workflow and iteration QA workflow.
---

# Sprint Testing Workflow

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need a sprint cadence: planning → setup → execution → regression → stabilize → review.
- Need iteration gates and DoD with handoffs to type skills—not a one-off testing task.

## Workflow

1. Read and follow `prompts/sprint-testing-workflow.md` (stages, gates, DoD, handoffs).
2. Add sprint goal, story scope, capacity, and carryover defects that change the plan.
3. After locating the stage, hand off by skill name per `reference.md`; no relative-path links to other skill internals.
4. If input is incomplete, draft a usable sprint test plan and mark assumptions and gaps.

## Core Constraints

- Own iteration phases and exit evidence; hand full artifacts to type skills.
- Gates and DoD must be checkable.
- On scope change, re-rank and state gate impact.
- No relative-path links to other skill files.

## Progressive Disclosure

- Before producing output, read and follow `prompts/sprint-testing-workflow.md`.
- For step ↔ handoff mapping: read `reference.md`.
- For stage deep-dives: invoke the matching type skill; do not expand full artifacts here.
- Templates: `output-templates/`.

## Pre-delivery Checklist

- [ ] Followed the main prompt’s output structure
- [ ] Includes stage position, gate board, exit-criteria check, next skill
- [ ] High-risk items have priority and Owner
- [ ] Did not invent details the user did not provide
- [ ] Assumptions, tradeoffs, and carryover are marked

## Common Pitfalls

- Do not write a day diary with no gates.
- Do not dump full case bodies during planning.
- Do not claim regression passed while development is still open-ended.
- Do not replace exit evidence with “we tested a lot”.
