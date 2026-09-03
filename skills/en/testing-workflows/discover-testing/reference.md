# Testing Skill Routing Map

## Capability stage first

- Core QA Skills: requirements, strategy, cases, execution, defects, and reporting; choose the matching installed foundation Skill.
- Engineering QA Skills: requirement quality, code change, diagnosis, and performance decisions; choose the nearest installed foundation Skill and state that the specialty remains on the roadmap.
- Production Quality Skills: use `release-testing-workflow` for release evidence; do not invent a directory when production verification, incidents, or observability specialties are not installed.
- AI Native QA Skills: testing AI features, LLMs, prompts, agents, or injection defenses; no specialized package is installable yet, so state the roadmap status.
- AI for QA: use `ai-assisted-testing` to assist conventional testing; it is not AI Native QA.

Do not add separate routing targets for `exploratory-testing` (`manual-testing` mode), `release-readiness-assessment` (`release-testing-workflow` mode), or `prompt-regression-testing` (future `prompt-testing` mode).

## Step 1: Choose Primary Skill Type

- Requirement understanding -> `requirements-analysis` / `requirements-analysis`
- Functional behavior validation -> `functional-testing` / `functional-testing`
- API contract and integration -> `api-testing` / `api-testing`
- Automation strategy or script design -> `automation-testing` / `automation-testing`
- Manual/exploratory sessions -> `manual-testing` / `manual-testing`
- Defect report authoring -> `bug-reporting` / `bug-reporting`
- Test case authoring -> `test-case-writing` / `test-case-writing`
- Test case quality review -> `test-case-reviewer` / `test-case-reviewer`
- Code / PR review -> `code-review` / `code-review`
- Metrics and report outputs -> `test-reporting` / `test-reporting`
- Strategy and governance -> `test-strategy` / `test-strategy`
- Performance scope -> `performance-testing` / `performance-testing`
- Security scope -> `security-testing` / `security-testing`
- Accessibility scope -> `accessibility-testing` / `accessibility-testing`
- Mobile scope -> `mobile-testing` / `mobile-testing`
- AI-assisted workflows -> `ai-assisted-testing` / `ai-assisted-testing`

## Step 2: Choose Workflow Skill (if phase-based planning is needed)

- Daily execution cadence -> `daily-testing-workflow` / `daily-testing-workflow`
- Sprint-cycle coordination -> `sprint-testing-workflow` / `sprint-testing-workflow`
- Release readiness and go/no-go -> `release-testing-workflow` / `release-testing-workflow`

## Step 3: Add Supporting Skill

- Need report output -> add `test-reporting` / `test-reporting`
- Need stronger scope definition -> add `test-strategy` / `test-strategy`
- Need defect artifact quality -> add `bug-reporting` / `bug-reporting`
- Postman is the chosen API tool -> add `api-test-postman` / `api-test-postman`
- UI automation tool is already chosen -> add `ui-test-selenium`, `ui-test-playwright`, `ui-test-testcafe`, `ui-test-cypress`, `ui-test-puppeteer`, or `ui-test-webdriverio`
- JMeter is the chosen performance tool -> add `performance-test-jmeter` / `performance-test-jmeter`
