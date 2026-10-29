---
name: ui-test-puppeteer
description: Use this skill when you need to design Puppeteer automation for Chromium-driven checks, screenshots, PDFs, network interception, and CDP use cases; triggers include Puppeteer UI testing, UI automation testing, and ui-test-puppeteer.
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

# Puppeteer UI Testing (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need outputs that should land in a Puppeteer UI testing workflow.
- The project already uses Puppeteer or wants Puppeteer-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/ui-test-puppeteer.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- `prompts/ui-test-puppeteer.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Domain Execution Essentials

1. Read actual Puppeteer/Node/browser and launch config/support scope. Incompatibility is CONFIG_ERROR; successful launch does not prove every feature is compatible.
2. Identify new windows through target creation/opener association and wait for a usable page, verifying URI/authority. Navigation readiness and business readiness are separate; real state is the oracle, not a fixed sleep.
3. Close owned pages/browser in try/finally and preserve timeout/load errors. Report primary and cleanup failures separately; never swallow exceptions and return success.
4. Minimum fixtures include good payment, wrong state, popup, load failure, and timeout. Verify business state/principal plus screenshot/URL/log/version evidence; generated files and successful loads are no business pass.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.

- To verify generated business assertions, failure propagation or isolation, read [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md) and its local good/bug/timeout controls; execute only when a run is requested.
