# Tool-Specific Testing Skills Expansion Design

## Goal

Expand the repository with eight tool-specific testing-type skills, each available in Chinese and English, following the current lightweight skill standard and existing tool-specific patterns.

The new skills are:

- `api-test-postman`
- `ui-test-selenium`
- `ui-test-playwright`
- `ui-test-testcafe`
- `ui-test-cypress`
- `ui-test-puppeteer`
- `ui-test-webdriverio`
- `performance-test-jmeter`

## Scope

Create each skill as an independent testing-type skill under both language partitions:

- `skills/zh/testing-types/<skill-id>/`
- `skills/en/testing-types/<skill-id>/`

Each skill should be complete enough to copy and use independently, while keeping scripts lightweight and maintainable.

Out of scope:

- Building full runnable framework scaffolds for all eight tools.
- Reworking existing generic skills such as `api-testing`, `automation-testing`, or `performance-testing`.
- Refactoring unrelated skill directories or existing user changes.

## Recommended Approach

Use full tool-specific skill directories with lightweight execution scripts.

Each new skill should include:

```text
<skill-id>/
├── README.md
├── SKILL.md
├── agents/openai.yaml
├── examples/
├── output-templates/template-markdown.md
├── prompts/<skill-id>.md
├── references/framework-spec.md
├── references/setup-and-ci.md
└── scripts/run-tests.sh
```

This matches the current direction used by existing skills such as `api-test-bruno`, `api-test-supertest`, and `performance-test-k6`, while avoiding high-maintenance framework generators.

## Content Boundaries

### `api-test-postman`

Focus on Postman Collections, environments, variables, pre-request scripts, test scripts, Newman execution, CI integration, and API regression prioritization.

### `ui-test-selenium`

Focus on Selenium WebDriver usage across common languages, Page Object patterns, locator strategy, waits, browser/Grid execution, data-driven testing, and stability practices.

### `ui-test-playwright`

Focus on Playwright Test, fixtures, projects, trace/video/screenshot artifacts, API plus UI coverage, browser isolation, parallelism, and CI reporting.

### `ui-test-testcafe`

Focus on TestCafe fixture/test structure, selectors, roles, browser matrix execution, stable waiting behavior, and reporting.

### `ui-test-cypress`

Focus on Cypress e2e/component boundaries, custom commands, fixtures, network stubbing, browser constraints, CI execution, and reporting.

### `ui-test-puppeteer`

Focus on Puppeteer page automation, Chrome DevTools Protocol-oriented use cases, screenshots/PDFs, network interception, scraping-style checks, and clear boundaries where full E2E frameworks are a better fit.

### `ui-test-webdriverio`

Focus on WebdriverIO configuration, services, runner behavior, Page Object structure, capabilities, reporters, and Selenium/Appium integration boundaries.

### `performance-test-jmeter`

Focus on JMeter Test Plans, Thread Groups, HTTP Samplers, CSV Data Set Config, assertions, timers, listeners, non-GUI CLI execution, HTML reports, and CI execution.

## Language Strategy

Create aligned Chinese and English versions for every new skill.

The Chinese and English versions should share:

- directory names
- section structure
- frontmatter shape
- prompt skeleton
- reference-file purpose
- output-template structure

They do not need to be mechanical translations. Chinese content should fit Chinese QA team usage, while English content should be concise and reusable for English-language teams.

## Documentation Updates

Update the project entry points after adding the skills:

- `README.md`: change testing-type skill count from 25 to 33 and add the eight new Chinese entries.
- `README_EN.md`: change testing-type skill count from 25 to 33 and add the eight new English entries.
- `skills-index.md`: add the eight new skills to both Chinese and English Testing-Type Skills lists.
- `skills/zh/testing-workflows/discover-testing/reference.md`: add routing hints for Postman, UI automation tools, WebdriverIO, and JMeter.
- `skills/en/testing-workflows/discover-testing/reference.md`: add equivalent English routing hints.
- `installers/`: regenerate installer shortcuts through the existing script after the skills are in place.

## Validation Plan

Run these checks after implementation:

```bash
python3 scripts/organize_project_dirs.py
bash scripts/check_skills_quality.sh
bash scripts/generate-install-shortcuts.sh
```

If the quality check reports issues unrelated to this expansion, separate those existing issues from new-skill issues in the final report and avoid changing unrelated user work.

## Git Safety

The workspace currently contains unrelated modified and untracked files. Implementation should not revert, overwrite, stage, or commit those changes unless explicitly requested.

When committing this design, stage only this spec file.

## Acceptance Criteria

- All eight skills exist in both `skills/zh/testing-types` and `skills/en/testing-types`.
- Each skill follows the agreed complete directory layout.
- Each `SKILL.md` follows the current lightweight section standard.
- Each prompt follows the required prompt skeleton from `skills/SKILL_STYLE_GUIDE.md`.
- Tool-specific content stays focused and does not duplicate generic testing theory.
- Project README files, `skills-index.md`, discover-testing routing docs, and installer shortcuts are updated.
- Quality checks pass or any unrelated pre-existing findings are clearly separated.
