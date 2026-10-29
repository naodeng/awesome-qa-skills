---
name: accessibility-testing
description: Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include accessibility testing and a11y testing.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Accessibility Testing (English)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need help with accessibility testing in a real project context.
- Need an output that can be used directly for execution, review, or follow-up.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Domain Execution Essentials

1. Record the project-supplied WCAG version/level, scope, and success criterion IDs. Missing targets stay open; never choose a level or claim conformance by default.
2. Build criterion ID | user task/state | input/assistive technology/version | steps | evidence type | outcome. Keep automated scan, keyboard, screen-reader, and manual visual evidence separate.
3. Exercise keyboard navigation, opening, operation, closing, and focus restoration. Check screen-reader name/role/state and dynamic announcements. Prioritize inaccessible critical actions by user impact.
4. A scan with zero findings establishes only the scanned result. Preserve manual FAIL and unexecuted NOT_RUN; aggregate evidence by criterion without promoting a partial scan to conformance.
## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Before producing output, read and follow `prompts/accessibility-testing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: scope and target users, keyboard access, focus order and visible focus, screen reader semantics and labels, headings and landmarks, form errors and validation feedback, color contrast and non-color cues, images, icons, and alternative text, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
