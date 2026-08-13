# UX Quality Perspective: Test-Case Writing

## Inputs

- `stage: test-case-writing`
- UI/UX requirements, prototypes, user flows, state definitions, design specifications, or existing-test context to turn into cases.

## Applicability Check

First confirm traceable UI/UX impact and a sufficiently described user task or state. If only backend scope exists, or there is no verifiable UI/flow/state evidence, return **Not applicable** with the reason, facts, gaps, and needed material; do not invent test steps, screens, controls, or expected results.

## UX Questions

- Which evidence-based cases follow from supplied tasks, navigation, hierarchy, states, feedback, consistency, responsive, or accessibility requirements?
- Which preconditions, devices/input methods, assistive technology, data, and observable outcomes are supported?
- Which gaps make an expected result unverifiable?

## Output Contract

Produce: **Summary, Facts, Evidence, Suggested cases/Findings, Risks, Information gaps, Questions, Actions, Confidence**. Cases contain only evidence-supported preconditions, steps, and expected outcomes; risks and actions have priority and owners.

## Evidence and Boundaries

- Do not invent screens, control names, copy, error states, breakpoints, screen-reader behavior, or results.
- Do not claim cases ran, implementation is correct, or experience is accepted.
