---
name: ui-test-webdriverio
description: Use this skill when you need to design WebdriverIO suites with config, services, runner behavior, Page Objects, capabilities, and reporters; triggers include WebdriverIO UI testing, UI automation testing, and ui-test-webdriverio.
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

# WebdriverIO UI Testing (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need outputs that should land in a WebdriverIO UI testing workflow.
- The project already uses WebdriverIO or wants WebdriverIO-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/ui-test-webdriverio.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- `prompts/ui-test-webdriverio.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Domain Execution Essentials

1. Fix WebdriverIO/Node, runner/framework, and browser/driver/service combinations. Check capabilities/services against installed packages, config, and remote support; names alone do not prove compatibility.
2. Generate version-compatible async specs/BDD steps and await every async command. Wait on observable business/element conditions; never catch command errors into a pass.
3. Isolate session, identity, and business keys per worker with setup/cleanup hooks. Cover supplied platform/browser matrix only; missing scope remains unknown.
4. Preserve test/worker/session/capability IDs, versions, URL, screenshot/logs, and original stack. Separate CONFIG_ERROR, business assertion failures, and environment errors, with diagnosis and CI propagation.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.

- To verify generated business assertions, failure propagation or isolation, read [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md) and its local good/bug/timeout controls; execute only when a run is requested.
