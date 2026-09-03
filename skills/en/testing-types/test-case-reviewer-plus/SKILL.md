---
name: test-case-reviewer-plus
description: Use this skill when you need structured test-case review findings from requirements, strategy, and case docs; triggers include test case reviewer plus and advanced test case review.
---

# test-case-reviewer-plus (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need a stricter review of existing test cases before test execution or release.
- Need issue severity, business impact, and retest order to be explicit.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Accept direct materials or user-supplied multi-role review reports; when role reports are used, retain `source_role` and source identifiers.
3. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
4. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
5. Default to Markdown; switch formats only when the user asks.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.
- Keep blockers, high-risk coverage gaps, maintainability findings, and low-value or duplicate cases in distinct sections rather than one generic issue list.
- Produce only AI findings and a recommendation; always output `human_final_decision: pending`, with the final pass, conditional-pass, or reject decision owned by a Human.

## Progressive Disclosure

- Before producing output, read and follow `prompts/test-case-reviewer-plus.md` (minimum coverage, output structure, quality bar).
- When a ready-made template fits: use matching files under `output-templates/`.
- When the user wants examples or alignment with existing assets: read relevant `examples/`.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: high-severity findings, coverage gaps, missing positive scenarios, missing negative scenarios, missing boundary scenarios, traceability, step and expectation quality, business impact, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked
- [ ] Multi-role inputs retain role sources and the four key finding categories remain distinct
- [ ] The AI recommendation does not impersonate a final Human approval or rejection record

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not turn an AI pass/reject recommendation into a final Human decision.
- Do not dump generic theory unrelated to the current toolchain.
