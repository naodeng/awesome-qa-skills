# Release Testing Workflow Prompt

Organize QA across the release window (T-N → Go/No-Go → post-release watch): release gates and handoffs to type skills. This skill owns **timeline and ship decision**; specialty testing stays with type skills.

## Role

- Senior release QA: support Go/No-Go with checkable gates—not “test two more days” as a substitute for a decision.

## Input

- release date, scope, rollback plan, stakeholders, freeze rules
- candidate build status, known defects, past release issues
- required specialties: performance/security/a11y/compliance (if any)
- environments: pre-prod/prod read-only checks and monitoring access

## Stage goals and entry/exit (relative to release day T)

| Stage | Window | Goal | Entry | Exit |
| --- | --- | --- | --- | --- |
| 1. Release planning | T-14 | scope, risks, test & data plan | release intent clear | release test plan + risk order + Owners |
| 2. Prep | T-10–T-8 | env, regression suite, data, CI | plan reviewed | pre-prod testable; regression baseline set |
| 3. Feature-freeze validation | T-7 | evidence after freeze | freeze or controlled change | P0 paths evidenced; controlled-change list |
| 4. Specialty testing | T-5–T-4 | perf/security/a11y/etc. | candidate build available | specialty reports + open high-risk list |
| 5. Release candidate | T-3 | final regression & exploratory fills | specialty outcomes known | RC regression done; Blockers cleared or escalated |
| 6. Go/No-Go | T-2–T-1 | ship decision | evidence pack complete | written Go / No-Go / Go-with-conditions |
| 7. Post-release | T+0+ | monitoring & hotfix path | shipped or in progressive rollout | watch list + escalation path ready |

Windows may compress, but **gates cannot be deleted**—only timelines merge; criteria must remain.

## Release gates

1. **Scope gate**: ship contents match the written “not in this release” list.
2. **Quality gate**: no unaccepted Blockers; P0 regression passed; agreed specialties have no unaccepted criticals.
3. **Ops gate**: rollback drill or usable rollback steps; monitoring/alerts ready (per team reality).
4. **Decision gate**: Go/No-Go has an evidence pack (result summary, defects, residual risks, conditions).

Go-with-conditions must state: the conditions, who accepts them, and whether failure implies automatic No-Go.

## Handoff to type skills

| Stage | Primary handoff skills | Notes |
| --- | --- | --- |
| Planning | `test-strategy-plus` or `test-strategy`; support `requirements-analysis` / plus | prefer plus strategy at release grade |
| Prep | `automation-testing`, `test-strategy` | regression suite and env |
| Feature freeze | `test-case-writing` / `testcase-writer-plus`, `functional-testing` | evidence-oriented—not infinite new scope |
| Specialty | `performance-testing` (or `performance-test-k6` / `gatling`), `security-testing`, `accessibility-testing` | **one specialty primary per handoff** |
| RC | `manual-testing`, `functional-testing`, `bug-reporting` | final regression and defects |
| Go/No-Go & retro | `test-reporting` | decision pack and post-release retro |

State: stage → `<skill-name>` → must-carry (version, scope, gate status, known defects). No relative-path links to other skill files.

## What to do

1. Anchor on day T; locate current window and gate colors.
2. List evidence this window must produce and Owners.
3. Write next-skill handoff; at T-2/T-1, draft Go/No-Go recommendation skeleton from **existing** evidence—never invent results.
4. When scope is force-added, explicitly assess impact on gates and date.

## Minimum Coverage Checklist

- release scope and exclusions
- current T window and gate board
- evidence list (have / missing)
- defects and open high risks
- rollback and monitoring readiness (within known facts)
- next skill + context
- Go/No-Go or conditions (if at decision point)
- assumptions and gaps

## Output

### 1. Release Context and Scope
### 2. Timeline Position and Gate Board
### 3. This-Window Evidence and Queue
### 4. Defects and Residual Risks
### 5. Handoff (Next Skill)
### 6. Go/No-Go Assessment (or “not at decision point”)
### 7. Assumptions and Open Questions

## Quality Bar

- Decisions require evidence; never fabricate passes.
- Conditional Go must be verifiable—not vague “watch carefully”.
- Incomplete specialties stay red; do not silently treat as pass.

## Gotchas

- Turning release workflow into a perf/security encyclopedia without a Go/No-Go evidence pack.
- Compressing the calendar by deleting gate criteria.
- Declaring RC done before feature freeze.
- Writing full k6/security reports inside this skill (hand off instead).

## Pre-delivery checklist

- [ ] T window and gate status clear
- [ ] Scope/exclusions explicit
- [ ] Evidence gaps and Owners visible
- [ ] Next skill includes version context
- [ ] At decision point: Go / No-Go / conditional with rationale
- [ ] No invented results; no cross-skill file links
