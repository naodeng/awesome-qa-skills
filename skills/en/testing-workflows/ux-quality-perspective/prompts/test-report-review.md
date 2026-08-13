# UX Quality Perspective: Test-Report Review

## Inputs

- `stage: test-report-review`
- A test report, experience observations, defects, screenshots/video, and linked UI/UX requirements, prototypes, or flows.

## Applicability Check

First confirm that the report or linked material contains UI/UX evidence to review. If it does not, return **Not applicable** with the reason, facts, gaps, and needed experience-report or linked material; do not add filler findings.

## UX Questions

- Does each report conclusion have matching UI/flow/state, device, input-method, or assistive-technology evidence?
- Are observed issues' impact, scope, reproduction conditions, risks, and actions clear?
- Which untested states, devices, or accessibility paths are incorrectly implied to be covered?

## Output Contract

Produce: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Identify demonstrable insufficient evidence, scope ambiguity, or experience risk, with actions assigned to accountable roles.

## Evidence and Boundaries

- A single screenshot or conclusion supports only its visible scope; never extrapolate to mobile, keyboard, screen-reader, or every state.
- Do not replace backend/API, security, or test-execution assessment; do not assert correct implementation, passed tests, or release readiness.
