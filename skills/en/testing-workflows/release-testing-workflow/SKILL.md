---
name: release-testing-workflow
description: Use this skill when you need release-phase QA workflow from T-14 planning to go/no-go and post-release monitoring; triggers include release testing workflow and go/no-go QA.
---

# Release Testing Workflow

**中文版：** See the corresponding Chinese skill.

## When to Use

- Need a release-window cadence: T-N planning → specialties → RC → Go/No-Go → post-release watch.
- Need release gates and a ship evidence pack, with specialty execution handed to type skills.

## Workflow

1. Read and follow `prompts/release-testing-workflow.md` (timeline, gates, Go/No-Go, handoffs).
2. Add release date, scope, freeze rules, candidate build, and known defects that change decisions.
3. After locating the T window, hand off by skill name per `reference.md`; invoke specialty type skills by name only.
4. If input is incomplete, still draft a gate board and mark assumptions—**never invent pass results**.

## Core Constraints

- Own release timeline and ship decision; hand specialty reports to `performance-testing` / `security-testing` / etc.
- Timelines may compress; gate criteria may not be deleted.
- Go/No-Go requires evidence; conditional Go must be verifiable.
- No relative-path links to other skill files.

## Progressive Disclosure

- Before producing output, read and follow `prompts/release-testing-workflow.md`.
- For step ↔ handoff mapping: read `reference.md`.
- For stage/specialty deep-dives: invoke the matching type skill; do not expand full specialty reports here.
- Templates: `output-templates/`.

## Pre-delivery Checklist

- [ ] Followed the main prompt’s output structure
- [ ] Includes scope/exclusions, T window, gate board, evidence gaps, next skill
- [ ] At decision point: Go / No-Go / conditional with rationale
- [ ] Did not invent pass results or unknown defect states
- [ ] Assumptions and open questions are marked

## Common Pitfalls

- Do not delete gates just to compress the calendar.
- Do not declare RC done before freeze.
- Do not write full specialty long-reports inside this skill.
- Do not replace conditional-Go terms with vague “keep watching”.
