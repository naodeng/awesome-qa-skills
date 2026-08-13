# UX Quality Perspective: Code Review

## Inputs

- `stage: code-review`
- A PR/diff, change description, and linked UI/UX requirements, prototypes, design specifications, or UI-test evidence.

## Applicability Check

First confirm that change material shows traceable UI/UX impact. If the change is backend-only, infrastructure-only, or explicitly has no UI impact, return **Not applicable** with the reason, known facts, gaps, and screen/flow/component-impact evidence needed to reassess; do not generate UI-defect or accessibility findings.

## UX Questions

- Does visible change align with supplied information architecture, states, interaction feedback, consistency, responsive, or accessibility requirements?
- Which evidenced UX requirements lack supporting change or test evidence?
- What UI behavior, keyboard, assistive-technology, or multi-device evidence must design, engineering, or QA add?

## Output Contract

Produce: **Summary, Facts, Evidence, Findings, Risks, Information gaps, Questions, Actions, Confidence**. Limit findings to demonstrable deviations or risks between the change and UX evidence.

## Evidence and Boundaries

- Without traceable UI change, do not infer screens, components, states, or cross-device impact.
- This does not replace engineering review or backend/API reliability or security assessment; do not assert correct implementation, reliable APIs, passed tests, or release approval.
