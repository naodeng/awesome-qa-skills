---
name: ai-assisted-testing
description: Use this skill when you need AI-assisted testing workflows such as test data generation, root-cause analysis, and prioritization; triggers include AI-assisted testing and AI for QA.
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

# AI-Assisted Testing

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need help with ai assisted testing in a real project context.
- Need an output that can be used directly for execution, review, or follow-up.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Domain Execution Essentials

1. Record input classification, sanitization, and allowed use. Replace identities, tokens, and personal data with non-reversible placeholders while retaining schema/business constraints.
2. Trace input snapshot→model/prompt version→AI draft ID→Human review→adopted version ID→acceptance evidence. Drafts do not automatically become execution assets.
3. Name the reviewers of business oracles, assertions, privacy, and high-risk tradeoffs. Unreviewed work remains draft, unexecuted work NOT_RUN; AI does not accept on behalf of Human.
4. Compare equal tasks/complexity/windows: manual baseline versus AI generation+review+rework+acceptance time. Track defects/rework separately; generation time alone cannot prove productivity gains.
## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Before producing output, read and follow `prompts/ai-assisted-testing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: task scope, best AI-assisted opportunities, human verification points, high-risk areas that need manual judgment, draft artifacts to generate, review and approval steps, quality gates, time-saving opportunities, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
