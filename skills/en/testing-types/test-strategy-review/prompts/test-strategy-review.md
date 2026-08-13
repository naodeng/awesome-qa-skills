# Test Strategy Review

This Prompt forms a traceable AI-assisted recommendation for one proposed test strategy. It runs independently, reviews only supplied material, and does not make final Human approval.

## Input contract

Accept:

- **Required**: the proposed test strategy body or a locatable version;
- **When available**: role analysis, requirements and acceptance criteria, risk register, architecture/API/data constraints, environment capability, and project schedule/resource/dependency constraints;
- **Source information**: document identifiers, versions, roles, supplied owners, and timing gates.

Mark absent material as `not supplied`. Project constraints inform feasibility; they are not evidence that coverage is sufficient, risk is accepted, or quality is approved.

## Input validation and conflicts

1. If there is no strategy body or reviewable strategy conclusion, stop substantive review: list the blocking input gap, set the AI recommendation to `reject`, and request the material. Do not write a replacement strategy or pretend to complete the eight-dimension review.
2. Build a source inventory that distinguishes strategy claims, requirement/business facts, technical facts, role analysis, and project constraints.
3. Preserve every source for contradictory claims about scope, rules, gates, dependencies, exclusions, or ownership. If the unresolved conflict affects critical coverage or feasibility, record a blocker; do not choose a source without authority.
4. Reduce confidence and state gaps when sources are insufficient. Never infer unsupplied environment capability, data, test results, waiver, risk acceptance, or approval from general knowledge.

## Eight-dimension review

For every dimension, state evidence, assessment, and gaps. Sufficiency in one dimension does not replace another.

1. **Business coverage**: critical journeys, business rules, state/failure paths, unacceptable risks, requirement traceability, and scope boundaries.
2. **Test depth**: test levels and types fit risk; positive, negative, boundary, concurrency/state, regression, and applicable performance, security, compatibility, and accessibility depth.
3. **Feasibility**: methods, sequence, effort, capability, timing, observability, and evidence collection can be executed; planned work is not reported as completed.
4. **Environments**: required environments, versions/configuration, external simulation, fault injection, monitoring, and readiness are explicit; fallback does not overstate coverage.
5. **Data**: normal/boundary/error/private data, construction or masking, refresh/cleanup, ownership, and readiness evidence are explicit.
6. **Quality gates**: entry, pause/resume, and exit thresholds are measurable, verifiable, and tied to critical risks; never claim a gate is met without evidence.
7. **Dependencies**: system, team, vendor, tool, contract, and timing dependencies have ownership, readiness checks, and failure/delay handling.
8. **Explicit exclusions**: every exclusion has a source, rationale, risk impact, and required authorization/follow-up; schedule alone cannot rewrite approved scope.

## Finding classification

- **Blocker**: prevents reliable review, leaves a critical business/technical risk uncovered, makes critical testing infeasible, invalidates gates, or leaves a material scope/exclusion conflict unresolved. One blocker requires `reject`.
- **Non-blocking condition**: the strategy is reviewable and feasible overall, but this item must close before a named test phase, entry gate, or other observable milestone. With no blockers and one or more conditions, recommend `conditional_pass`.
- **Non-blocking improvement**: improves clarity, efficiency, or maintenance without changing the current recommendation. With only improvements, `pass` remains valid.

Do not vote by finding count. Positive evidence cannot cancel one critical blocker. Recommend `pass` only when there is no blocker or condition.

## Ownership and revision requests

Create a revision request for every blocker and condition with:

- `request_id` and related finding;
- the exact object to change or supply;
- an owner explicitly supplied by the input, or `unassigned` when absent—never guess a person;
- the closure time or gate; use an observable milestone when no date is supplied and do not invent a date;
- verifiable closure evidence such as an approved scope change, updated coverage matrix, environment probe, data validation result, or gate definition.

Create a request for an optional improvement only when useful, and label that it does not affect the current recommendation.

## Output format

Produce Markdown in this order:

1. **Review Status**
   - `review_type: AI-assisted recommendation`
   - `recommendation: pass | conditional_pass | reject`
   - `human_final_decision: pending`
   - confidence and limitations
   - concise rationale
2. **Inputs and Conflicts**: supplied/missing sources, versions, and ownership; for every conflict, list both sides, effect, and required authorized resolution. Say `No conflicts` when none exist.
3. **Dimension Review Matrix**: for all eight dimensions, provide `Evidence/Source`, `Assessment (sufficient/partial/insufficient/unknown/not applicable)`, and `Gap and Impact`.
4. **Blockers**: each has `finding_id`, dimension, evidence/source, impact, supplied owner, and closure condition. Say `No blockers` when empty.
5. **Non-Blocking Items**: label each `condition` or `improvement` and provide evidence, impact, owner, and closure gate. Say `No non-blocking items` when empty.
6. **Revision Requests**: follow the contract above. Keep the section and say `No revision requests` when empty.
7. **Exclusion Review**: exclusion, basis, requirement alignment, risk disposition, and authorization question. If none are explicit, state whether that is a gap.
8. **Recommendation Basis and Limitations**: explain how classification yields the recommendation and how evidence coverage limits confidence.
9. **Human Decision Questions**: list only questions for a Human or authorized role and restate that the AI recommendation is not approval.

## Mandatory pre-output check

- Did every dimension receive an assessment, without mixing facts, gaps, and project constraints?
- Are blockers and non-blockers separate, and conditions distinct from optional improvements?
- Does `reject`/`conditional_pass`/`pass` strictly follow the classification rules?
- Does every blocker and condition have an owner or `unassigned`, revision object, closure gate, and evidence?
- Are conflicting inputs, explicit exclusions, and sources preserved without an invented ruling or waiver?
- Did the output mistake plans for results or add a fact, person, date, risk acceptance, or approval? Delete it.
- Does it explicitly state `human_final_decision: pending` and avoid claiming final pass or approval?
