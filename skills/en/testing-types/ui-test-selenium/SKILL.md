---
name: ui-test-selenium
description: Use this skill when you need to design Selenium WebDriver UI automation plans with stable locators, waits, Page Objects, Grid, and CI execution; triggers include Selenium UI testing, UI automation testing, and ui-test-selenium.
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

# Selenium UI Testing (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need outputs that should land in a Selenium UI testing workflow.
- The project already uses Selenium or wants Selenium-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/ui-test-selenium.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- `prompts/ui-test-selenium.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Domain Execution Essentials

1. Fix Selenium/binding/browser/driver/Grid versions, capabilities, and runner. Produce compatible config/POM; do not invent Grid topology and diagnose version conflicts first.
2. Explicitly wait on observable interactability, business state, window, or URL conditions. Presence/visibility is not business readiness; avoid mixed implicit/explicit waits and universal fixed sleeps.
3. After rerender/stale references re-find by stable locator and wait for fresh state. Bounded retries follow supplied policy; blind payment replay can duplicate effects.
4. Isolate accounts/business keys per parallel session. Use try/finally driver.quit with screenshots/logs/session/original failures. Rerender, business-failure, and exception controls verify cleanup and nonzero propagation.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.

- To verify generated business assertions, failure propagation or isolation, read [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md) and its local good/bug/timeout controls; execute only when a run is requested.
