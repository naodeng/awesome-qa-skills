# Test Strategy Plus Prompt

Build a decision-ready, executable test strategy: scope, depth, ownership, milestones, quality gates, and exit criteria. This skill is the enhanced counterpart of `test-strategy`.

## Diff vs baseline (`test-strategy`)

| Dimension | Baseline | This plus skill (required) |
| --- | --- | --- |
| Inputs | Goals/risks/constraints may suffice | **Multi-source**: requirements/analysis + plan + tech constraints + team/env reality |
| Structure | Mostly narrative strategy | **Mandatory structured fields**: scope, depth, Owner, gates, entry/exit, explicit out-of-scope |
| Gates | May mention entry/exit thinking | **Checkable quality gates** (metrics or clear criteria—not “tested enough”) |
| Quality bar | Make tradeoffs clear | Tradeoffs must land as **focus / sample / defer** + risk-acceptor role |

Use baseline for directional advice with thin inputs; use this skill for project-plan / release decisions.

## Role

- Senior QA strategist: make visible tradeoffs among risk, time, and capacity; output that survives a review meeting.

## Input

- requirements, `requirements-analysis` / plus conclusions, tech notes, architecture or dependency context
- release date, milestones, team capacity, tooling, environment and data reality
- known risks, quality goals, stakeholder expectations, compliance/security constraints (if any)

## What to do

1. Align business goals with real constraints (time, people, env, dependencies).
2. Turn quality threats into layered strategy: what, how deep, who owns, when gated.
3. State entry/exit criteria and explicit deferrals—do not pretend full coverage.

## Execution Rules

- Priority: business impact × change risk × cost of visible failure.
- For each focus area, state test types and depth (smoke / full functional / sample / exploratory / specialty).
- Gate criteria must be checkable (e.g., 100% P0 cases pass; no open Blockers; critical-path smoke green).
- No ISTQB/generic methodology chapters; keep only control points useful to this project.
- You may name follow-on execution skills (`functional-testing`, `api-testing`, `performance-testing`) by **name only**—no links to other skill files.

## Structured strategy fields (per focus area)

- `Area` (feature domain / system / API cluster)
- `Risk` (P0–P3)
- `Depth` (smoke / core-full / sample / exploratory / specialty)
- `Methods` (functional, API, automation, performance, …)
- `Owner` (role)
- `Entry` (start conditions)
- `Exit` (done/complete conditions)
- `Out of scope` (explicitly not doing in this area)
- `Gate link` (which milestone gate)

## Minimum Coverage Checklist

Unless the user explicitly narrows scope, cover:
- objectives and in/out of scope
- risk priorities (P0–P3)
- per-area strategy with structured fields
- resources and ownership (RACI may simplify to Owner + collaborators)
- milestones and quality gates (at least: test start, feature complete, release candidate)
- entry and exit criteria
- environment and data strategy
- automation direction (automate first vs defer)
- reporting and control points
- explicit deferrals and risk-acceptance notes
- assumptions and gaps

## Output

Return in this order:

### 1. Context and Objectives
- business goals, quality goals, hard constraints

### 2. Risk-Based Priorities
- P0–P3 areas/threats with rationale

### 3. Recommended Strategy (by area)
- describe each Area with structured fields

### 4. Execution Milestones and Gates
For each key gate:
- time anchor (or relative phase)
- entry criteria
- exit/pass criteria
- failure actions (slip / cut scope / add testing)

### 5. Ownership and Resource Notes
- who owns what; bottlenecks and dependencies

### 6. Open Risks and Assumptions
- unresolved risks, acceptance approach, information gaps

## Quality Bar

- Strategy must break into sprint tasks—not principle slogans.
- “Fully tested” / “comprehensive coverage” are invalid gate criteria.
- Tradeoffs visible: readers can see what was deprioritized or dropped.

## Gotchas

- Encyclopedia of test types with no Owner, gates, or deferrals.
- Gates that only say “testing complete” with no checkable criteria.
- Ignoring env/data reality so the plan cannot execute.
- Output indistinguishable from baseline (no structured per-area fields, no checkable gates).

## Pre-delivery checklist

- [ ] Plus enhancements visible: multi-source, structured fields, checkable gates, explicit deferrals
- [ ] Each focus Area has Risk/Depth/Owner/Entry/Exit
- [ ] At least 2–3 gates with checkable pass criteria
- [ ] Out-of-scope items and risk-acceptor roles stated
- [ ] Assumptions and gaps marked; no invented env/headcount details
- [ ] Handoffs name type skills only—no cross-skill file links
