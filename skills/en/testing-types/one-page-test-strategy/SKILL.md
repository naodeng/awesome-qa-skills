---
name: one-page-test-strategy
description: Use this skill when a team needs a concise visual test strategy tied to project goals and risks; triggers include 一页纸测试策略、测试策略图 and one-page test strategy.
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

# One-Page Test Strategy

**中文版：** See the corresponding Chinese skill.

## When to Use

- A team needs a visual test strategy that is easy to discuss, share, and update.
- Business goals, quality risks, and test approaches need to fit on one page.
- The strategy should show early testing, built-in quality, and relevant post-release feedback.

If the user needs a full execution plan, detailed staffing, or test cases, use the existing full test-strategy capability; do not force those details onto this page.

## Workflow

1. Read and follow `prompts/one-page-test-strategy.md` for input review, output structure, and quality criteria.
2. Extract goals, current phase, key risks, system characteristics, team capability, and constraints; separate facts, assumptions, and gaps.
3. Follow the prompt's required modules: guiding principle and goal, functionality/performance/security scope, test enablers and constraints (environment/data/tools/team), seven lifecycle stages, shift-left/right, test quadrants, lean test layers, and iteration/release feedback.
4. If context is incomplete, provide a discussable draft with assumptions and open questions; do not invent gates, facts, or owners.

## Core Constraints

- Treat the strategy as a goal-driven team discussion artifact that evolves with project phases and risks, not as a full test plan or execution record.
- Show shared team ownership of quality; name individual owners only when input supports them.
- Always retain functionality, performance, and security scope columns with project-relevant risks or an Open status; do not require all three to be in scope.
- Always include a compact module for test environments/infrastructure, test data and access limits, automation/manual approach and tools, and relevant team roles/capability; distinguish known facts, recommendations, and Open items.
- Always cover requirements analysis, before development, development, development complete, testing, before release, and released; show early shift-left feedback and post-release shift-right feedback.
- Always show Q1–Q4 quadrants and the unit/API-integration/exploratory layers; orient business-facing/technology-facing vertically and supports-the-team/evaluates-the-product horizontally. Fill them from project definitions and evidence, and mark gaps Open. Automation/manual and tools are activity attributes, not quadrant axes.
- Quadrants and layers are selection frameworks, not fixed checklists, execution order, or ratios; choose investment based on goals, risks, architecture, and capability.
- Always show the iteration 1 → iteration 2 → … → iteration n → release/production cadence and explain how feedback enters the next iteration; mark unknown cadence and production mechanisms Open.
- Entry/exit gates, numeric thresholds, test ratios, and schedules must come from project evidence; do not claim production monitoring or user feedback exists without evidence.

## Progressive Disclosure

- Read `prompts/one-page-test-strategy.md` for every strategy generation.
- Read `examples/one-page-sample.md` when the user wants a layout reference; its project facts illustrate the format only.
- When the user requests an image, slide, or other medium, preserve the seven lifecycle stages, four quadrants, three test layers, shift-left/right, and iteration feedback modules while following that format.

## Pre-delivery Checklist

- [ ] The page includes shared team quality ownership, the goal, and risk/status across functionality, performance, and security.
- [ ] The page includes environment/infrastructure, test data/access limits, tools/approach, and team capability/roles, distinguishing known facts from Open items.
- [ ] All seven lifecycle stages appear and show shift-left/right feedback.
- [ ] Q1–Q4 quadrants use the stated axis orientation; unit/API-integration/exploratory layers and the iteration/release feedback loop each have a visible module.
- [ ] Selected test types, quadrants, and layers fit known context; unsupported items remain recommendations or Open.
- [ ] Assumptions, unknown gates, and open decisions are visible.
- [ ] No fixed test ratios, numeric gates, or day-by-day schedules are invented; the page has not expanded into test cases or execution claims.

## Common Mistakes

- Do not apply the same generic template unchanged to every project.
- Do not list every test type or layer to fill the page.
- Do not draw test quadrants as a fixed execution sequence or assume every architecture uses a testing pyramid.
- Do not use unconfirmed numeric thresholds to imply release agreement.
