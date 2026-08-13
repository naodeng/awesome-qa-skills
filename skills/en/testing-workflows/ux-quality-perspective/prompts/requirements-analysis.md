# UX Quality Perspective: Requirements Analysis

## Inputs

- `stage: requirements-analysis`
- Requirements, user stories, prototypes, screenshots, UI descriptions, design specifications, user flows, or acceptance criteria.

## Applicability Check

First confirm that a requirement or change exists to analyze. If not, return **Not applicable** with the reason, known facts, gaps, and needed material; do not generate findings. If a requirement exists but no prototype/UI evidence is supplied, this stage remains applicable: report only requirement facts, missing flow/screen/state/breakpoint/accessibility evidence, and questions; never assume a screen, control, copy, state, or device behavior.

## UX Questions

- Do the supplied information architecture, navigation, and content hierarchy support the target task and discoverability?
- Is evidence for interaction states, feedback, error/empty/loading states, and consistency sufficient?
- Can supplied breakpoint, device, or assistive-technology evidence support responsive and accessibility judgment?
- Which ambiguities could cause task failure, cognitive burden, exclusionary experience, or untestable risk?

## Output Contract

Produce a standalone report: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Findings must trace to supplied UX evidence; actions name priority and a product, design, engineering, or QA owner.

## Evidence and Boundaries

- Separate facts, evidence, and inferences; without a prototype, do not treat generic UX patterns as facts about this UI.
- Do not invent screens, components, copy, interaction states, responsive behavior, accessibility results, or test results.
- Do not determine implementation correctness, API reliability, security, passed tests, or release readiness.
