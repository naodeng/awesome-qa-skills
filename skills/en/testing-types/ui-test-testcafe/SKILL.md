---
name: ui-test-testcafe
description: Use this skill when you need to design TestCafe UI automation with fixtures, selectors, roles, browser matrix execution, and reports; triggers include TestCafe UI testing, UI automation testing, and ui-test-testcafe.
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

# TestCafe UI Testing (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need outputs that should land in a TestCafe UI testing workflow.
- The project already uses TestCafe or wants TestCafe-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/ui-test-testcafe.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- `prompts/ui-test-testcafe.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Domain Execution Essentials

1. Confirm TestCafe/Node/browser, native automation mode, CI, and reporter versions. Produce fixtures/tests/config compatible with the existing runner; missing config is open, not an implicit upgrade.
2. Initialize isolated sessions with Roles or independent identities and isolate accounts/business keys too. Await asynchronous t actions and use supported Selector/assertion waits rather than fixed sleeps.
3. Verify paid state, amount, and principal. Boundary stubs must not bypass the real UI; a normal title is no success. Negative controls must fail business assertions.
4. CLI nonzero or programmatic failedCount>0 must fail CI. Reporters cannot swallow failures; retain screenshots/console/test IDs and cleanup. Parseable config is distinct from actual execution.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.

- To verify generated business assertions, failure propagation or isolation, read [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md) and its local good/bug/timeout controls; execute only when a run is requested.
