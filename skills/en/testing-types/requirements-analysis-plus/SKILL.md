---
name: requirements-analysis-plus
description: Use this skill when you need to parse Word/HTML/JSON/Markdown/Excel requirements and produce a structured analysis; triggers include requirements analysis plus and requirement document parsing.
---

# requirements-analysis-plus (EN)

**中文版：** See the corresponding Chinese skill.

## When to Use

- Need deeper requirement analysis across multiple source documents.
- Need stronger prioritization, conflict checks, and follow-up questions than the base version.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Direct requirement materials remain sufficient for standalone use. If the user supplies role reports with a declared `source_role`, treat them as optional composition inputs and never require installing a role Skill.
3. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
4. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
5. Default to Markdown; switch formats only when the user asks.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- When using a fact, view, risk, or question from a role report, preserve its source-role attribution item by item; never present a role view as a primary requirement fact or anonymous consensus.
- Consume only report content supplied by the user; do not read, link to, or depend on another role Skill's internal files.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- Before producing output, read and follow `prompts/requirements-analysis-plus.md` (minimum coverage, output structure, quality bar).
- When a ready-made template fits: use matching files under `output-templates/`.
- When the user wants examples or alignment with existing assets: read relevant `examples/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: source alignment, scope summary, conflicts and inconsistencies, missing rules, testability risks, dependency impacts, business impact, priority by risk, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked
- [ ] Findings, risks, and open questions that use role reports retain their source roles
- [ ] Optional role reports did not become prerequisites and no role Skill internal file was linked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
