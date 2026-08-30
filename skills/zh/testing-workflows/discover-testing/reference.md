# 测试技能路由图（中文）

## 能力阶段优先级

- Core QA Skills：需求、策略、用例、执行、缺陷和报告；选择对应的已安装基础 Skill。
- Engineering QA Skills：需求质量、代码变更、诊断和性能决策；当前选择最近的已安装基础 Skill，并说明专项能力仍在路线图。
- Production Quality Skills：发布证据优先 `release-testing-workflow`；生产验证、事故和可观测性专项尚未安装时不得虚构目录。
- AI Native QA Skills：验证 AI 功能、LLM、Prompt、Agent 或注入防护；当前尚无可安装专项包，应明确说明路线图状态。
- AI for QA：使用 AI 协助常规测试时选 `ai-assisted-testing`；它不属于 AI Native QA。

不单独建路由目标：`manual-testing` 负责 `exploratory-testing` 模式；`release-testing-workflow` 负责 `release-readiness-assessment` 模式；未来 `prompt-testing` 负责 `prompt-regression-testing` 模式。

## 第一步：选择主技能（测试类型）

- 需求理解与测试点识别 -> `requirements-analysis` / `requirements-analysis`
- 功能行为验证 -> `functional-testing` / `functional-testing`
- API 接口与集成验证 -> `api-testing` / `api-testing`
- 自动化策略与脚本设计 -> `automation-testing` / `automation-testing`
- 手工 / 探索性测试 -> `manual-testing` / `manual-testing`
- 缺陷报告编写 -> `bug-reporting` / `bug-reporting`
- 测试用例编写 -> `test-case-writing` / `test-case-writing`
- 测试用例评审 -> `test-case-reviewer` / `test-case-reviewer`
- 代码 / PR 审查 -> `code-review` / `code-review`
- 指标与测试报告输出 -> `test-reporting` / `test-reporting`
- 测试策略与质量治理 -> `test-strategy` / `test-strategy`
- 性能测试范围 -> `performance-testing` / `performance-testing`
- 安全测试范围 -> `security-testing` / `security-testing`
- 可访问性测试范围 -> `accessibility-testing` / `accessibility-testing`
- 移动端测试范围 -> `mobile-testing` / `mobile-testing`
- AI 辅助测试工作 -> `ai-assisted-testing` / `ai-assisted-testing`

## 第二步：选择流程技能（按阶段）

- 日常执行节奏 -> `daily-testing-workflow` / `daily-testing-workflow`
- Sprint 迭代协同 -> `sprint-testing-workflow` / `sprint-testing-workflow`
- 发布就绪与 Go/No-Go -> `release-testing-workflow` / `release-testing-workflow`

## 第三步：补充辅助技能（可选）

- 需要报告输出 -> 加 `test-reporting` / `test-reporting`
- 需要范围与优先级强化 -> 加 `test-strategy` / `test-strategy`
- 需要缺陷产物质量提升 -> 加 `bug-reporting` / `bug-reporting`
- API 已确定使用 Postman -> 加 `api-test-postman` / `api-test-postman`
- UI 自动化已确定工具 -> 按工具加 `ui-test-selenium`、`ui-test-playwright`、`ui-test-testcafe`、`ui-test-cypress`、`ui-test-puppeteer` 或 `ui-test-webdriverio`
- 性能测试已确定使用 JMeter -> 加 `performance-test-jmeter` / `performance-test-jmeter`

---

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
