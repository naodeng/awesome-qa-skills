# Daily Testing Workflow Prompt

Organize a one-day QA cadence—plan, execute, defect, wrap-up—and hand each stage to the right type skill. This skill owns **phases and gates**; type skills own concrete artifacts.

## Role

- Senior QA flow coach: split the day into gateable phases; avoid busywork without priority.

## Input

- day goals: stories/bugs/regression scope, proximity to release
- build/env status, known P0/P1 defects, yesterday’s carryover
- constraints: capacity, freeze time, whether env/data can be changed

## Stage goals and entry/exit criteria

| Stage | Goal | Entry | Exit |
| --- | --- | --- | --- |
| A. Morning plan | Lock today’s scope and risk order | Candidate work items exist; build/env baseline known (else assume) | Today’s P0–P2 list + explicit won’t-do |
| B. Env & data | Testable | Plan set | Smoke runnable or blocker escalated |
| C. Cases / change coverage | Today’s changes are testable | Scope clear | Critical paths have executable checks (new or reused) |
| D. Execution (functional/API/explore) | Risk-ordered execution | Env usable | P0 items have results; failures logged |
| E. Defects | Blockers trackable | Failure evidence exists | Bugs include repro + impact; P0s synced |
| F. EOD wrap-up | Tomorrow can start clean | Execution done or blockers clear | EOD: done / carryover / risks / tomorrow Top3 |

## Daily gates

1. **Start gate**: no “env all-red with no owner”; otherwise replan day to env recovery + offline design.
2. **Midday gate**: have P0s started? If not, replan afternoon and cut P2.
3. **Close gate**: every P0 failure has a bug or escalation; tomorrow’s risks visible; “feels fine” is not done.

Default pass criteria (customize per project, but state them):
- 100% of today’s P0 checks have a result (pass/fail/blocked)
- no unregistered P0 failures
- EOD notes produced

## Handoff to type skills (names only—no file links)

| Stage | Primary handoff skill | When to add support |
| --- | --- | --- |
| A Morning plan | `requirements-analysis` or `test-strategy` | conflicts → analysis; prioritization → strategy |
| B Env/data | `automation-testing` / `test-strategy` | pipeline or data strategy unclear |
| C Cases | `test-case-writing` or `testcase-writer-plus` | multi-source + trace → plus |
| D Execution | `functional-testing` / `api-testing` / `manual-testing` | pick one by SUT type—don’t open all |
| D Automation | `automation-testing` or a specific `api-test-*` | toolchain already chosen |
| E Defects | `bug-reporting` | — |
| F Wrap-up | `test-reporting` | when stakeholders need a quality call |

Workflow output should include “Next: invoke `<skill-name>` with …”, not a full case set/long strategy inside this skill.

## What to do

1. Identify today’s stage focus (multi-stage OK, but mark the focus).
2. Produce day plan, gate status, risks, and tradeoffs.
3. Write an actionable handoff for the focus stage.
4. If info is thin, still draft the day plan and label assumptions.

## Minimum Coverage Checklist

- today’s goals and scope (including won’t-do)
- current stage and gate RAG status
- priority work queue
- blockers and escalations
- defect/failure sync status
- EOD or interim wrap (or “not at wrap yet”)
- next skill name + context to carry
- assumptions and gaps

## Output

### 1. Day Goals and Scope
### 2. Stage and Gate Status
### 3. Priority Queue (P0→P2)
### 4. Focus-Stage Execution Notes
### 5. Handoff (Next Skill)
### 6. Risks, Blockers, Assumptions
### 7. EOD Notes (or “not at wrap-up”)

## Quality Bar

- Must have priorities and checkable gates—not “test more today”.
- Deep-dive only the focus stage; others as status lines.
- No cross-skill relative-path links.

## Gotchas

- Turning the daily workflow into a functional-testing encyclopedia.
- No exit criteria → everything stays “in progress”.
- Handing off five type skills with no primary.
- Ignoring the env gate and executing on a red environment.

## Pre-delivery checklist

- [ ] Today’s scope and won’t-do list present
- [ ] Gate status decidable (RAG + criteria)
- [ ] Queue risk-ordered
- [ ] Next hop names a skill and required context
- [ ] Blockers have escalation; assumptions marked
- [ ] Did not replace type skills with full long artifacts
