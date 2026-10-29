---
name: ui-test-playwright
description: Use this skill when you need to design Playwright Test suites with fixtures, projects, traces, screenshots, API plus UI coverage, and CI reporting; triggers include Playwright UI testing, UI automation testing, and ui-test-playwright.
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

# Playwright UI Testing (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need outputs that should land in a Playwright UI testing workflow.
- The project already uses Playwright or wants Playwright-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/ui-test-playwright.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- `prompts/ui-test-playwright.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Domain Execution Essentials

1. Fix project Playwright/Node/browser versions, projects, fixtures, and config. Retain entry points with test ID, commit, worker/project, and environment; diagnose incompatible config without switching stacks.
2. Prefer stable role/name/testid locators and auto-retrying business assertions for order/ledger/state/principal. Title/URL checks protect navigation only, not payment success.
3. Give each worker independent browser context, storage state/account, and business keys. Context isolation still needs server-side account isolation; cleanup follows reverse dependencies.
4. Pair wrong-business-state and parallel A/B controls to test assertion sensitivity. Preserve traces/screenshots/logs and nonzero runner/CI status, including first retry failures. Separate generated assets, real browser runs, and acceptance.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.

- To verify generated business assertions, failure propagation or isolation, read [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md) and its local good/bug/timeout controls; execute only when a run is requested.
