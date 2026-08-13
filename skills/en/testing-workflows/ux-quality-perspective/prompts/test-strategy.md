# UX Quality Perspective: Test Strategy

## Inputs

- `stage: test-strategy`
- A strategy draft plus traceable UI/UX requirements, prototypes, flows, design specifications, or historical experience risks.

## Applicability Check

First confirm that the strategy scope contains traceable UI/UX impact or experience evidence. If materials are backend-only, infrastructure-only, or contain no UI impact, return **Not applicable** with the reason, known facts, gaps, and UI/flow/state evidence needed to reassess; do not generate UX-coverage findings.

## UX Questions

- Does the strategy cover evidenced task flows, information architecture, key states, consistency, responsive behavior, and accessibility risks?
- Are devices, breakpoints, input methods, assistive technology, and visual states selected from evidence?
- Can entry/exit criteria, observable signals, ownership, and risk priority support an experience decision?

## Output Contract

Produce: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. List only evidence-supported experience risks as findings; list unsupplied coverage dimensions as gaps.

## Evidence and Boundaries

- Do not derive project breakpoints, screens, screen-reader behavior, or pass criteria from generic platform assumptions.
- Do not replace test execution or claim coverage is implemented, tests passed, or release is ready.
