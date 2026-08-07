# Tool-Specific Testing Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add eight complete tool-specific testing skills in both Chinese and English, then update repository docs, routing, installers, and quality checks.

**Architecture:** Add each tool as an independent `testing-types` skill under `skills/zh` and `skills/en`, mirroring the current `api-test-bruno` and `performance-test-k6` pattern. Use focused templates and a local scaffolding helper to keep the 16 bilingual skill directories structurally aligned while allowing each tool's prompt, examples, and references to stay tool-specific.

**Tech Stack:** Markdown skill docs, YAML agent metadata, Bash run scripts, Python standard library for scaffolding, existing repository quality scripts.

---

## File Structure

Create these implementation helper and skill files:

- Create: `scripts/scaffold_tool_specific_skills.py`
- Create: `skills/zh/testing-types/api-test-postman/`
- Create: `skills/en/testing-types/api-test-postman/`
- Create: `skills/zh/testing-types/ui-test-selenium/`
- Create: `skills/en/testing-types/ui-test-selenium/`
- Create: `skills/zh/testing-types/ui-test-playwright/`
- Create: `skills/en/testing-types/ui-test-playwright/`
- Create: `skills/zh/testing-types/ui-test-testcafe/`
- Create: `skills/en/testing-types/ui-test-testcafe/`
- Create: `skills/zh/testing-types/ui-test-cypress/`
- Create: `skills/en/testing-types/ui-test-cypress/`
- Create: `skills/zh/testing-types/ui-test-puppeteer/`
- Create: `skills/en/testing-types/ui-test-puppeteer/`
- Create: `skills/zh/testing-types/ui-test-webdriverio/`
- Create: `skills/en/testing-types/ui-test-webdriverio/`
- Create: `skills/zh/testing-types/performance-test-jmeter/`
- Create: `skills/en/testing-types/performance-test-jmeter/`

Each skill directory must contain:

- `README.md`
- `SKILL.md`
- `agents/openai.yaml`
- `examples/sample-context.md`
- `output-templates/template-markdown.md`
- `prompts/<skill-id>.md`
- `references/framework-spec.md`
- `references/setup-and-ci.md`
- `scripts/run-tests.sh`

Modify these project entry points:

- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `skills-index.md`
- Modify: `skills/zh/testing-workflows/discover-testing/reference.md`
- Modify: `skills/en/testing-workflows/discover-testing/reference.md`
- Modify generated installer files under `installers/zh/<skill-id>/` and `installers/en/<skill-id>/`

Do not modify unrelated existing changes currently present in the worktree.

---

### Task 1: Add Scaffolding Helper

**Files:**
- Create: `scripts/scaffold_tool_specific_skills.py`

- [ ] **Step 1: Create the scaffolding script**

Use `apply_patch` to add `scripts/scaffold_tool_specific_skills.py` with this complete content:

```python
#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


@dataclass(frozen=True)
class SkillSpec:
    skill_id: str
    display_en: str
    display_zh: str
    short_en: str
    short_zh: str
    category_en: str
    category_zh: str
    focus_en: list[str]
    focus_zh: list[str]
    inputs_en: list[str]
    inputs_zh: list[str]
    outputs_en: list[str]
    outputs_zh: list[str]
    run_hint: str


SKILLS = [
    SkillSpec(
        skill_id="api-test-postman",
        display_en="API Test Postman",
        display_zh="API 测试 Postman",
        short_en="Design Postman collections, environments, scripts, and Newman-ready API regression plans.",
        short_zh="设计 Postman 集合、环境、脚本和可用 Newman 执行的 API 回归方案。",
        category_en="API testing",
        category_zh="API 测试",
        focus_en=["collection structure", "environment and variable strategy", "pre-request and test scripts", "Newman and CI execution", "API regression risk coverage"],
        focus_zh=["集合结构", "环境与变量策略", "pre-request 与 test scripts", "Newman 与 CI 执行", "API 回归风险覆盖"],
        inputs_en=["OpenAPI, curl, Postman collection, endpoint notes, or auth docs", "environment, release scope, and regression priorities", "current Newman or CI constraints"],
        inputs_zh=["OpenAPI、curl、Postman collection、接口说明或鉴权文档", "环境、发布范围和回归优先级", "现有 Newman 或 CI 约束"],
        outputs_en=["Postman collection plan", "environment and variable design", "assertion and script checklist", "Newman execution notes"],
        outputs_zh=["Postman 集合规划", "环境与变量设计", "断言与脚本清单", "Newman 执行说明"],
        run_hint='newman run "${COLLECTION:-collection.json}" -e "${ENVIRONMENT:-environment.json}" --reporters cli,json --reporter-json-export "$REPORT_JSON"',
    ),
    SkillSpec(
        skill_id="ui-test-selenium",
        display_en="UI Test Selenium",
        display_zh="UI 自动化测试 Selenium",
        short_en="Design Selenium WebDriver UI automation plans with stable locators, waits, Page Objects, Grid, and CI execution.",
        short_zh="设计 Selenium WebDriver UI 自动化方案，覆盖稳定定位、等待、Page Object、Grid 和 CI 执行。",
        category_en="UI automation testing",
        category_zh="UI 自动化测试",
        focus_en=["Page Object model", "locator strategy", "explicit waits", "browser and Grid execution", "flakiness control"],
        focus_zh=["Page Object 模式", "定位器策略", "显式等待", "浏览器与 Grid 执行", "不稳定用例治理"],
        inputs_en=["critical user flows and supported browsers", "language or framework preference", "test data and environment constraints"],
        inputs_zh=["关键用户流程和支持浏览器", "语言或框架偏好", "测试数据和环境约束"],
        outputs_en=["Selenium automation scope", "Page Object structure", "locator and wait rules", "Grid and CI notes"],
        outputs_zh=["Selenium 自动化范围", "Page Object 结构", "定位与等待规则", "Grid 与 CI 说明"],
        run_hint='echo "Run your Selenium suite with the project command, for example: mvn test, pytest, gradle test, or npm test"',
    ),
    SkillSpec(
        skill_id="ui-test-playwright",
        display_en="UI Test Playwright",
        display_zh="UI 自动化测试 Playwright",
        short_en="Design Playwright Test suites with fixtures, projects, traces, screenshots, API plus UI coverage, and CI reporting.",
        short_zh="设计 Playwright Test 套件，覆盖 fixtures、projects、trace、截图、API+UI 组合和 CI 报告。",
        category_en="UI automation testing",
        category_zh="UI 自动化测试",
        focus_en=["test fixtures", "browser projects", "trace, video, and screenshot artifacts", "API plus UI flows", "parallel CI execution"],
        focus_zh=["测试 fixtures", "浏览器 projects", "trace、video 与 screenshot 产物", "API+UI 流程", "并行 CI 执行"],
        inputs_en=["user flows, browser matrix, and auth setup", "existing Playwright config if available", "artifact and reporting needs"],
        inputs_zh=["用户流程、浏览器矩阵和登录设置", "已有 Playwright 配置", "产物和报告需求"],
        outputs_en=["Playwright suite plan", "fixture and project strategy", "trace and artifact rules", "CI execution notes"],
        outputs_zh=["Playwright 套件规划", "fixture 与 project 策略", "trace 与产物规则", "CI 执行说明"],
        run_hint='npx playwright test --reporter=list,html',
    ),
    SkillSpec(
        skill_id="ui-test-testcafe",
        display_en="UI Test TestCafe",
        display_zh="UI 自动化测试 TestCafe",
        short_en="Design TestCafe UI automation with fixtures, selectors, roles, browser matrix execution, and reports.",
        short_zh="设计 TestCafe UI 自动化方案，覆盖 fixture、selector、role、浏览器矩阵和报告。",
        category_en="UI automation testing",
        category_zh="UI 自动化测试",
        focus_en=["fixture and test organization", "selectors", "roles", "browser matrix", "reporting"],
        focus_zh=["fixture 与 test 组织", "selector", "role", "浏览器矩阵", "报告输出"],
        inputs_en=["target flows and supported browsers", "auth and role requirements", "current TestCafe configuration"],
        inputs_zh=["目标流程和支持浏览器", "鉴权与角色要求", "现有 TestCafe 配置"],
        outputs_en=["TestCafe suite plan", "selector and role rules", "browser execution matrix", "reporting notes"],
        outputs_zh=["TestCafe 套件规划", "selector 与 role 规则", "浏览器执行矩阵", "报告说明"],
        run_hint='npx testcafe "${BROWSERS:-chrome}" "${TEST_PATH:-tests/**/*.test.js}"',
    ),
    SkillSpec(
        skill_id="ui-test-cypress",
        display_en="UI Test Cypress",
        display_zh="UI 自动化测试 Cypress",
        short_en="Design Cypress e2e and component testing plans with commands, fixtures, network stubbing, and CI reporting.",
        short_zh="设计 Cypress e2e 与组件测试方案，覆盖 commands、fixtures、网络桩和 CI 报告。",
        category_en="UI automation testing",
        category_zh="UI 自动化测试",
        focus_en=["e2e versus component boundary", "custom commands", "fixtures", "network stubbing", "CI reporting"],
        focus_zh=["e2e 与组件测试边界", "custom commands", "fixtures", "网络桩", "CI 报告"],
        inputs_en=["critical browser flows", "API stubbing needs", "component or e2e scope", "current Cypress config"],
        inputs_zh=["关键浏览器流程", "API 桩需求", "组件或 e2e 范围", "现有 Cypress 配置"],
        outputs_en=["Cypress coverage plan", "command and fixture strategy", "network control notes", "CI run plan"],
        outputs_zh=["Cypress 覆盖规划", "command 与 fixture 策略", "网络控制说明", "CI 运行方案"],
        run_hint='npx cypress run --browser "${BROWSER:-chrome}"',
    ),
    SkillSpec(
        skill_id="ui-test-puppeteer",
        display_en="UI Test Puppeteer",
        display_zh="UI 自动化测试 Puppeteer",
        short_en="Design Puppeteer automation for Chromium-driven checks, screenshots, PDFs, network interception, and CDP use cases.",
        short_zh="设计 Puppeteer 自动化方案，覆盖 Chromium 检查、截图、PDF、网络拦截和 CDP 场景。",
        category_en="UI automation testing",
        category_zh="UI 自动化测试",
        focus_en=["page automation", "Chrome DevTools Protocol use cases", "screenshots and PDFs", "network interception", "E2E framework fit boundaries"],
        focus_zh=["页面自动化", "Chrome DevTools Protocol 场景", "截图与 PDF", "网络拦截", "与完整 E2E 框架的边界"],
        inputs_en=["Chromium automation goal", "target pages and artifacts", "network or scraping constraints"],
        inputs_zh=["Chromium 自动化目标", "目标页面和产物", "网络或抓取约束"],
        outputs_en=["Puppeteer automation plan", "artifact strategy", "network interception notes", "framework fit warning"],
        outputs_zh=["Puppeteer 自动化规划", "产物策略", "网络拦截说明", "框架适配提醒"],
        run_hint='node "${TEST_FILE:-scripts/puppeteer-check.js}"',
    ),
    SkillSpec(
        skill_id="ui-test-webdriverio",
        display_en="UI Test WebdriverIO",
        display_zh="UI 自动化测试 WebdriverIO",
        short_en="Design WebdriverIO suites with config, services, runner behavior, Page Objects, capabilities, and reporters.",
        short_zh="设计 WebdriverIO 套件，覆盖配置、services、runner、Page Object、capabilities 和 reporters。",
        category_en="UI automation testing",
        category_zh="UI 自动化测试",
        focus_en=["wdio configuration", "services", "runner behavior", "Page Object structure", "capabilities and reporters"],
        focus_zh=["wdio 配置", "services", "runner 行为", "Page Object 结构", "capabilities 与 reporters"],
        inputs_en=["browser or device matrix", "service integrations", "reporting needs", "existing wdio config"],
        inputs_zh=["浏览器或设备矩阵", "service 集成", "报告需求", "现有 wdio 配置"],
        outputs_en=["WebdriverIO suite plan", "configuration notes", "service and capability plan", "reporting and CI notes"],
        outputs_zh=["WebdriverIO 套件规划", "配置说明", "service 与 capability 方案", "报告与 CI 说明"],
        run_hint='npx wdio run "${CONFIG:-wdio.conf.js}"',
    ),
    SkillSpec(
        skill_id="performance-test-jmeter",
        display_en="Performance Test JMeter",
        display_zh="性能测试 JMeter",
        short_en="Design JMeter test plans with Thread Groups, samplers, data sets, assertions, timers, CLI runs, and HTML reports.",
        short_zh="设计 JMeter 测试计划，覆盖 Thread Group、Sampler、数据集、断言、Timer、CLI 执行和 HTML 报告。",
        category_en="performance testing",
        category_zh="性能测试",
        focus_en=["Test Plan structure", "Thread Groups", "HTTP Samplers", "CSV Data Set Config", "non-GUI execution and HTML reports"],
        focus_zh=["Test Plan 结构", "Thread Group", "HTTP Sampler", "CSV Data Set Config", "非 GUI 执行和 HTML 报告"],
        inputs_en=["target services and traffic model", "performance thresholds", "test data and environment limits"],
        inputs_zh=["目标服务和流量模型", "性能阈值", "测试数据和环境限制"],
        outputs_en=["JMeter test plan outline", "load model", "assertion and timer strategy", "CLI and report notes"],
        outputs_zh=["JMeter 测试计划大纲", "负载模型", "断言与 timer 策略", "CLI 与报告说明"],
        run_hint='jmeter -n -t "${TEST_PLAN:-test-plan.jmx}" -l "$REPORT_DIR/results.jtl" -e -o "$REPORT_DIR/html"',
    ),
]


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def skill_md(spec: SkillSpec, lang: str) -> str:
    if lang == "en":
        return f"""---
name: {spec.skill_id}
description: Use this skill when you need {spec.short_en[0].lower() + spec.short_en[1:]}; triggers include {spec.display_en}, {spec.category_en}, and {spec.skill_id}.
---

# {spec.display_en} (EN)

**中文版：** 见对应中文技能。

## When to Use

- Need outputs that should land in a {spec.display_en}-oriented workflow.
- The project already uses {spec.display_en.split()[-1]} or wants {spec.display_en.split()[-1]}-ready planning.

## Output Format Options

Markdown by default unless the request explicitly asks for another format.

## How to Use

1. Open `prompts/{spec.skill_id}.md` and use it as the main prompt.
2. Add the real project context: scope, environment, constraints, risks, dependencies, and expected deliverable.
3. If the input is incomplete, return a usable first version and mark missing information and assumptions.

## Reference Files

- `prompts/{spec.skill_id}.md`: main prompt for this skill.
- `references/framework-spec.md`: tool-specific structure and coverage notes.
- `references/setup-and-ci.md`: setup, execution, and CI notes.
- `examples/sample-context.md`: sample request context.
- `scripts/run-tests.sh`: lightweight local execution entry point.

## Common Pitfalls

- Do not use it with vague scope and no context.
- Do not treat every area as equally important.
- Do not skip assumptions and missing information.

## Best Practices

- Start from the prompt file, then add only the context that matters.
- Keep the output risk-driven and executable.
- If the request is incomplete, return a usable first version and mark gaps.
"""
    return f"""---
name: {spec.skill_id}
description: Use this skill when you need {spec.short_en[0].lower() + spec.short_en[1:]}; triggers include {spec.display_en}, {spec.category_en}, and {spec.skill_id}.
---

# {spec.display_zh}

**English version:** see the matching English skill.

## 何时使用

- 需要输出面向 {spec.display_zh} 工作流的测试方案或自动化设计。
- 项目已经使用相关工具，或希望得到可直接落地的工具专项方案。

## 输出格式选项

默认使用 Markdown。除非请求明确要求其他格式，不额外扩展输出格式。

## 如何使用

1. 打开 `prompts/{spec.skill_id}.md`，将其作为主提示词。
2. 补充真实项目上下文：范围、环境、约束、风险、依赖和期望交付物。
3. 如果输入不完整，先返回可用的第一版，并标出缺失信息和假设。

## 参考文件

- `prompts/{spec.skill_id}.md`：本技能主提示词。
- `references/framework-spec.md`：工具专项结构和覆盖说明。
- `references/setup-and-ci.md`：安装、执行和 CI 说明。
- `examples/sample-context.md`：示例请求上下文。
- `scripts/run-tests.sh`：轻量本地执行入口。

## 常见误区

- 不要在范围模糊且缺少上下文时直接给泛泛方案。
- 不要把所有模块和场景视为同等重要。
- 不要跳过假设和缺失信息说明。

## 最佳实践

- 从 prompt 文件开始，只补充真正影响结果的上下文。
- 输出保持风险驱动，并能直接用于执行或评审。
- 信息不完整时，先给可用版本，再标清缺口。
"""


def prompt_md(spec: SkillSpec, lang: str) -> str:
    if lang == "en":
        return f"""# {spec.display_en} Prompt

Design {spec.display_en}-ready testing assets or a {spec.display_en}-ready plan that the team can implement directly.

## Role

- Act as a senior QA automation expert who structures outputs for practical {spec.display_en} usage and maintainability.

## Input

{bullet(spec.inputs_en)}

## What to do

1. Understand the target scope and highest-risk flows first.
2. Organize the result around real {spec.display_en} usage, not generic testing theory.
3. Keep assumptions visible when project details are incomplete.

## Execution Rules

- Cover tool-specific structure, execution, data, assertions, reporting, and CI concerns when relevant.
- Prefer maintainable test organization over large one-off scripts.
- If information is incomplete, give a usable first version and mark assumptions.

## Minimum Coverage Checklist

Unless the user explicitly narrows the scope, make sure the result addresses these items:
{bullet(spec.focus_en)}
- test data or environment needs
- reporting needs
- missing information and assumptions

## Output

Return the result in this order:

### 1. Task Understanding
### 2. {spec.display_en} Scope
### 3. Test Structure and Coverage
### 4. Data, Environment, and Assertions
### 5. Execution and CI Notes
### 6. Open Questions

## Quality Bar

- Keep the result {spec.display_en}-oriented.
- Do not output unrelated framework advice.
- Avoid long code unless the user asks for runnable files.
"""
    return f"""# {spec.display_zh}提示词

设计可直接落地的 {spec.display_zh} 测试资产或测试方案。

## 角色定位

- 你是资深 QA 自动化专家，擅长把输出组织成可维护、可执行的 {spec.display_zh} 方案。

## 输入

{bullet(spec.inputs_zh)}

## 你要做的事

1. 先理解目标范围和最高风险流程。
2. 围绕真实 {spec.display_zh} 使用方式组织输出，不写泛泛测试理论。
3. 当项目信息不完整时，明确标出假设和缺失信息。

## 执行规则

- 按需覆盖工具专项结构、执行方式、数据、断言、报告和 CI。
- 优先给可维护的测试组织方式，不输出一次性大脚本。
- 信息不完整时，先给可用第一版，并标清假设。

## 最低覆盖清单

除非用户明确缩小范围，输出至少覆盖：
{bullet(spec.focus_zh)}
- 测试数据或环境需求
- 报告需求
- 缺失信息和假设

## 输出

按以下顺序输出：

### 1. 任务理解
### 2. {spec.display_zh} 范围
### 3. 测试结构与覆盖
### 4. 数据、环境与断言
### 5. 执行与 CI 说明
### 6. 待确认问题

## 质量要求

- 输出必须围绕 {spec.display_zh}。
- 不输出无关框架建议。
- 除非用户要求可运行文件，否则避免长代码。
"""


def readme_md(spec: SkillSpec, lang: str) -> str:
    title = f"{spec.skill_id} ({'EN' if lang == 'en' else 'ZH'})"
    overview = spec.short_en if lang == "en" else spec.short_zh
    install_lang = "en" if lang == "en" else "zh"
    return f"""# {title}

## Skill Overview

{overview}

## How to Use

1. Open `SKILL.md` in this folder and confirm this skill fits your task.
2. In your AI tool, call `@skill {spec.skill_id}`, then add your real project context and goal.
3. If you need a specific output shape, include it directly in your request.

## One-Click Install Script

Run from the repository root:

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang {install_lang} --skill {spec.skill_id}
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\\scripts\\install-skills-windows.ps1 -Tool codex -Lang {install_lang} -Skill {spec.skill_id}
```
"""


def agent_yaml(spec: SkillSpec, lang: str) -> str:
    return f"""version: 1
metadata:
  key: "{spec.skill_id}"
  last_verified: "2026-08-07"
interface:
  display_name: "{spec.display_en if lang == 'en' else spec.display_zh}"
  short_description: "{spec.short_en if lang == 'en' else spec.short_zh}"
  default_prompt: "Use {spec.skill_id} to complete the task with local prompts, references, and examples in this skill folder."
policy:
  allow_implicit_invocation: true
"""


def framework_spec(spec: SkillSpec, lang: str) -> str:
    if lang == "en":
        return f"""# {spec.display_en} Framework Notes

## Primary Focus

{bullet(spec.focus_en)}

## Recommended Structure

- Start from business-critical flows or endpoints.
- Group tests by product capability and execution risk.
- Keep setup, data, assertions, and reporting visible in the plan.
- Prefer maintainable naming and reusable helpers over large scripts.

## Decision Rules

- Use this skill when {spec.display_en} is the chosen or likely tool.
- Use the generic parent testing skill when the tool is still undecided.
- Call out constraints that make another tool a better fit.
"""
    return f"""# {spec.display_zh}框架说明

## 主要关注点

{bullet(spec.focus_zh)}

## 推荐结构

- 从业务关键流程或接口开始。
- 按产品能力和执行风险组织测试。
- 在方案中明确 setup、数据、断言和报告。
- 优先使用可维护命名和可复用辅助结构，不输出大段一次性脚本。

## 决策规则

- 当项目已选择或倾向使用 {spec.display_zh} 时使用本技能。
- 工具尚未确定时，先使用通用父级测试技能。
- 如果其他工具更适合，要明确说明约束和原因。
"""


def setup_ci(spec: SkillSpec, lang: str) -> str:
    if lang == "en":
        return f"""# {spec.display_en} Setup and CI Notes

## Local Setup

- Confirm the tool version and runtime before proposing commands.
- Keep secrets, tokens, and environment-specific values outside committed test files.
- Store generated reports under a reports or build-artifacts folder ignored by version control.

## Suggested Run Command

```bash
{spec.run_hint}
```

## CI Guidance

- Run smoke coverage on pull requests.
- Run broader regression on release branches or scheduled jobs.
- Preserve reports, logs, screenshots, traces, or result files as CI artifacts when the tool produces them.
- Fail the pipeline on clear assertion failures, not on missing optional artifacts.
"""
    return f"""# {spec.display_zh}安装与 CI 说明

## 本地设置

- 给出命令前先确认工具版本和运行时环境。
- 不要把密钥、token 或环境专属值写进已提交测试文件。
- 将生成报告放到 reports 或 build-artifacts 一类目录，并避免误提交。

## 建议执行命令

```bash
{spec.run_hint}
```

## CI 建议

- Pull Request 阶段运行冒烟覆盖。
- 发布分支或定时任务运行更完整回归。
- 如果工具会产生日志、截图、trace 或结果文件，将它们保存为 CI artifact。
- Pipeline 应因明确断言失败而失败，不因可选产物缺失而失败。
"""


def output_template(lang: str) -> str:
    if lang == "en":
        return """# Output Template

## Summary
- Scope:
- Key Risks:

## Tool-Specific Plan
- Structure:
- Data:
- Assertions:
- Execution:

## Open Questions
- Question 1:
"""
    return """# 输出模板

## 摘要
- 范围：
- 关键风险：

## 工具专项方案
- 结构：
- 数据：
- 断言：
- 执行：

## 待确认问题
- 问题 1：
"""


def sample_context(spec: SkillSpec, lang: str) -> str:
    if lang == "en":
        return f"""# Sample Context

Use `@skill {spec.skill_id}` to design coverage for a release-critical login and checkout flow.

Project context:

- Tool: {spec.display_en}
- Environment: staging
- Priority: protect the release smoke path and the highest-risk regression cases
- Constraints: keep the first version maintainable and CI-friendly

Expected output:

{bullet(spec.outputs_en)}
"""
    return f"""# 示例上下文

使用 `@skill {spec.skill_id}` 为发布关键的登录和下单流程设计覆盖。

项目上下文：

- 工具：{spec.display_zh}
- 环境：staging
- 优先级：保护发布冒烟路径和最高风险回归场景
- 约束：第一版要可维护，并适合接入 CI

期望输出：

{bullet(spec.outputs_zh)}
"""


def run_script(spec: SkillSpec) -> str:
    return f"""#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPORT_DIR="$SCRIPT_DIR/../reports"
mkdir -p "$REPORT_DIR"
TS="$(date +%Y%m%d-%H%M%S)"
REPORT_JSON="$REPORT_DIR/{spec.skill_id}-$TS.json"

echo "Running {spec.skill_id} lightweight entry point"
echo "Report path: $REPORT_JSON"

{spec.run_hint}
"""


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(0o755)


def main() -> int:
    for spec in SKILLS:
        for lang in ("zh", "en"):
            base = SKILLS_ROOT / lang / "testing-types" / spec.skill_id
            write(base / "README.md", readme_md(spec, lang))
            write(base / "SKILL.md", skill_md(spec, lang))
            write(base / "agents" / "openai.yaml", agent_yaml(spec, lang))
            write(base / "examples" / "sample-context.md", sample_context(spec, lang))
            write(base / "output-templates" / "template-markdown.md", output_template(lang))
            write(base / "prompts" / f"{spec.skill_id}.md", prompt_md(spec, lang))
            write(base / "references" / "framework-spec.md", framework_spec(spec, lang))
            write(base / "references" / "setup-and-ci.md", setup_ci(spec, lang))
            write(base / "scripts" / "run-tests.sh", run_script(spec), executable=True)
    print(f"scaffolded_skills={len(SKILLS) * 2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Run the scaffolding helper**

Run:

```bash
python3 scripts/scaffold_tool_specific_skills.py
```

Expected:

```text
scaffolded_skills=16
```

- [ ] **Step 3: Inspect generated file count**

Run:

```bash
find skills/zh/testing-types skills/en/testing-types -path '*api-test-postman*' -o -path '*ui-test-selenium*' -o -path '*ui-test-playwright*' -o -path '*ui-test-testcafe*' -o -path '*ui-test-cypress*' -o -path '*ui-test-puppeteer*' -o -path '*ui-test-webdriverio*' -o -path '*performance-test-jmeter*' | wc -l
```

Expected: output is greater than `140`, confirming files and directories were created.

- [ ] **Step 4: Commit the generated skill directories and helper**

Run:

```bash
git add scripts/scaffold_tool_specific_skills.py skills/zh/testing-types/api-test-postman skills/en/testing-types/api-test-postman skills/zh/testing-types/ui-test-selenium skills/en/testing-types/ui-test-selenium skills/zh/testing-types/ui-test-playwright skills/en/testing-types/ui-test-playwright skills/zh/testing-types/ui-test-testcafe skills/en/testing-types/ui-test-testcafe skills/zh/testing-types/ui-test-cypress skills/en/testing-types/ui-test-cypress skills/zh/testing-types/ui-test-puppeteer skills/en/testing-types/ui-test-puppeteer skills/zh/testing-types/ui-test-webdriverio skills/en/testing-types/ui-test-webdriverio skills/zh/testing-types/performance-test-jmeter skills/en/testing-types/performance-test-jmeter
git commit -m "feat: add tool-specific testing skills"
```

Expected: commit succeeds and pre-commit quality checks pass.

---

### Task 2: Tighten Generated Content Against Style Guide

**Files:**
- Modify: all new `SKILL.md`
- Modify: all new `prompts/<skill-id>.md`
- Modify: all new `references/framework-spec.md`
- Modify: all new `references/setup-and-ci.md`
- Modify: all new `examples/sample-context.md`

- [ ] **Step 1: Check frontmatter shape**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
skills = [
    "api-test-postman", "ui-test-selenium", "ui-test-playwright", "ui-test-testcafe",
    "ui-test-cypress", "ui-test-puppeteer", "ui-test-webdriverio", "performance-test-jmeter",
]
for lang in ("zh", "en"):
    for skill in skills:
        p = Path("skills") / lang / "testing-types" / skill / "SKILL.md"
        text = p.read_text()
        assert text.startswith("---\nname: "), p
        assert "\ndescription: Use this skill when " in text, p
        assert "\n---\n\n#" in text, p
print("frontmatter_ok=16")
PY
```

Expected:

```text
frontmatter_ok=16
```

- [ ] **Step 2: Check required `SKILL.md` sections**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
skills = [
    "api-test-postman", "ui-test-selenium", "ui-test-playwright", "ui-test-testcafe",
    "ui-test-cypress", "ui-test-puppeteer", "ui-test-webdriverio", "performance-test-jmeter",
]
required = {
    "en": ["## When to Use", "## Output Format Options", "## How to Use", "## Reference Files", "## Common Pitfalls", "## Best Practices"],
    "zh": ["## 何时使用", "## 输出格式选项", "## 如何使用", "## 参考文件", "## 常见误区", "## 最佳实践"],
}
for lang in ("zh", "en"):
    for skill in skills:
        p = Path("skills") / lang / "testing-types" / skill / "SKILL.md"
        text = p.read_text()
        missing = [section for section in required[lang] if section not in text]
        assert not missing, (p, missing)
print("skill_sections_ok=16")
PY
```

Expected:

```text
skill_sections_ok=16
```

- [ ] **Step 3: Check required prompt sections**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
skills = [
    "api-test-postman", "ui-test-selenium", "ui-test-playwright", "ui-test-testcafe",
    "ui-test-cypress", "ui-test-puppeteer", "ui-test-webdriverio", "performance-test-jmeter",
]
required = {
    "en": ["## Role", "## Input", "## What to do", "## Execution Rules", "## Minimum Coverage Checklist", "## Output", "## Quality Bar"],
    "zh": ["## 角色定位", "## 输入", "## 你要做的事", "## 执行规则", "## 最低覆盖清单", "## 输出", "## 质量要求"],
}
for lang in ("zh", "en"):
    for skill in skills:
        p = Path("skills") / lang / "testing-types" / skill / "prompts" / f"{skill}.md"
        text = p.read_text()
        missing = [section for section in required[lang] if section not in text]
        assert not missing, (p, missing)
print("prompt_sections_ok=16")
PY
```

Expected:

```text
prompt_sections_ok=16
```

- [ ] **Step 4: Manually review one generated skill per category**

Run:

```bash
sed -n '1,220p' skills/en/testing-types/api-test-postman/prompts/api-test-postman.md
sed -n '1,220p' skills/en/testing-types/ui-test-playwright/prompts/ui-test-playwright.md
sed -n '1,220p' skills/en/testing-types/performance-test-jmeter/prompts/performance-test-jmeter.md
sed -n '1,220p' skills/zh/testing-types/api-test-postman/prompts/api-test-postman.md
sed -n '1,220p' skills/zh/testing-types/ui-test-playwright/prompts/ui-test-playwright.md
sed -n '1,220p' skills/zh/testing-types/performance-test-jmeter/prompts/performance-test-jmeter.md
```

Expected: each file is tool-specific, concise, and contains no generic filler such as long persona backstory.

- [ ] **Step 5: Commit any tightening edits**

If Step 4 found text that needs tightening, edit those files with `apply_patch`, then run:

```bash
git add skills/zh/testing-types/api-test-postman skills/en/testing-types/api-test-postman skills/zh/testing-types/ui-test-selenium skills/en/testing-types/ui-test-selenium skills/zh/testing-types/ui-test-playwright skills/en/testing-types/ui-test-playwright skills/zh/testing-types/ui-test-testcafe skills/en/testing-types/ui-test-testcafe skills/zh/testing-types/ui-test-cypress skills/en/testing-types/ui-test-cypress skills/zh/testing-types/ui-test-puppeteer skills/en/testing-types/ui-test-puppeteer skills/zh/testing-types/ui-test-webdriverio skills/en/testing-types/ui-test-webdriverio skills/zh/testing-types/performance-test-jmeter skills/en/testing-types/performance-test-jmeter
git commit -m "docs: refine tool-specific skill content"
```

Expected: commit succeeds. If no edits were needed, skip this commit and note that the generated content passed review.

---

### Task 3: Update Project Entry Documents

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `skills-index.md`

- [ ] **Step 1: Update Chinese README skill count and table**

Edit `README.md`:

- Change `25 个测试类型技能` to `33 个测试类型技能`.
- Add these rows to the Testing-Type Skills table near related existing entries:

```markdown
| API 测试（Postman） | `skills/zh/testing-types/api-test-postman` |
| UI 自动化测试（Selenium） | `skills/zh/testing-types/ui-test-selenium` |
| UI 自动化测试（Playwright） | `skills/zh/testing-types/ui-test-playwright` |
| UI 自动化测试（TestCafe） | `skills/zh/testing-types/ui-test-testcafe` |
| UI 自动化测试（Cypress） | `skills/zh/testing-types/ui-test-cypress` |
| UI 自动化测试（Puppeteer） | `skills/zh/testing-types/ui-test-puppeteer` |
| UI 自动化测试（WebdriverIO） | `skills/zh/testing-types/ui-test-webdriverio` |
| 性能测试（JMeter） | `skills/zh/testing-types/performance-test-jmeter` |
```

- [ ] **Step 2: Update English README skill count and table**

Edit `README_EN.md`:

- Change `25 testing-type skills` to `33 testing-type skills`.
- Add these rows to the Testing-Type Skills table near related existing entries:

```markdown
| API Test (Postman) | `skills/en/testing-types/api-test-postman` |
| UI Test (Selenium) | `skills/en/testing-types/ui-test-selenium` |
| UI Test (Playwright) | `skills/en/testing-types/ui-test-playwright` |
| UI Test (TestCafe) | `skills/en/testing-types/ui-test-testcafe` |
| UI Test (Cypress) | `skills/en/testing-types/ui-test-cypress` |
| UI Test (Puppeteer) | `skills/en/testing-types/ui-test-puppeteer` |
| UI Test (WebdriverIO) | `skills/en/testing-types/ui-test-webdriverio` |
| Performance Test (JMeter) | `skills/en/testing-types/performance-test-jmeter` |
```

- [ ] **Step 3: Update skills index**

Edit `skills-index.md` and add these entries to both Chinese and English Testing-Type Skills lists:

```markdown
- [api-test-postman](skills/zh/testing-types/api-test-postman/)
- [ui-test-selenium](skills/zh/testing-types/ui-test-selenium/)
- [ui-test-playwright](skills/zh/testing-types/ui-test-playwright/)
- [ui-test-testcafe](skills/zh/testing-types/ui-test-testcafe/)
- [ui-test-cypress](skills/zh/testing-types/ui-test-cypress/)
- [ui-test-puppeteer](skills/zh/testing-types/ui-test-puppeteer/)
- [ui-test-webdriverio](skills/zh/testing-types/ui-test-webdriverio/)
- [performance-test-jmeter](skills/zh/testing-types/performance-test-jmeter/)
```

For the English list, use the same skill IDs with `skills/en/testing-types/...` paths.

- [ ] **Step 4: Verify README and index links exist**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
paths = [
    "skills/zh/testing-types/api-test-postman", "skills/en/testing-types/api-test-postman",
    "skills/zh/testing-types/ui-test-selenium", "skills/en/testing-types/ui-test-selenium",
    "skills/zh/testing-types/ui-test-playwright", "skills/en/testing-types/ui-test-playwright",
    "skills/zh/testing-types/ui-test-testcafe", "skills/en/testing-types/ui-test-testcafe",
    "skills/zh/testing-types/ui-test-cypress", "skills/en/testing-types/ui-test-cypress",
    "skills/zh/testing-types/ui-test-puppeteer", "skills/en/testing-types/ui-test-puppeteer",
    "skills/zh/testing-types/ui-test-webdriverio", "skills/en/testing-types/ui-test-webdriverio",
    "skills/zh/testing-types/performance-test-jmeter", "skills/en/testing-types/performance-test-jmeter",
]
for path in paths:
    assert Path(path).is_dir(), path
print("new_skill_paths_ok=16")
PY
```

Expected:

```text
new_skill_paths_ok=16
```

- [ ] **Step 5: Commit documentation entry updates**

Run:

```bash
git add README.md README_EN.md skills-index.md
git commit -m "docs: list tool-specific testing skills"
```

Expected: commit succeeds and does not stage unrelated files.

---

### Task 4: Update Discover Testing Routing

**Files:**
- Modify: `skills/zh/testing-workflows/discover-testing/reference.md`
- Modify: `skills/en/testing-workflows/discover-testing/reference.md`

- [ ] **Step 1: Add Chinese route hints**

Edit `skills/zh/testing-workflows/discover-testing/reference.md`. In the Chinese "第三步：补充辅助技能（可选）" section, add:

```markdown
- API 已确定使用 Postman -> 加 `api-test-postman` / `api-test-postman`
- UI 自动化已确定工具 -> 按工具加 `ui-test-selenium`、`ui-test-playwright`、`ui-test-testcafe`、`ui-test-cypress`、`ui-test-puppeteer` 或 `ui-test-webdriverio`
- 性能测试已确定使用 JMeter -> 加 `performance-test-jmeter` / `performance-test-jmeter`
```

- [ ] **Step 2: Add English route hints**

Edit `skills/en/testing-workflows/discover-testing/reference.md`. In the English "Step 3: Add Supporting Skill" section, add:

```markdown
- Postman is the chosen API tool -> add `api-test-postman` / `api-test-postman`
- UI automation tool is already chosen -> add `ui-test-selenium`, `ui-test-playwright`, `ui-test-testcafe`, `ui-test-cypress`, `ui-test-puppeteer`, or `ui-test-webdriverio`
- JMeter is the chosen performance tool -> add `performance-test-jmeter` / `performance-test-jmeter`
```

- [ ] **Step 3: Verify route files mention all new tool IDs**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
ids = ["api-test-postman", "ui-test-selenium", "ui-test-playwright", "ui-test-testcafe", "ui-test-cypress", "ui-test-puppeteer", "ui-test-webdriverio", "performance-test-jmeter"]
for path in [Path("skills/zh/testing-workflows/discover-testing/reference.md"), Path("skills/en/testing-workflows/discover-testing/reference.md")]:
    text = path.read_text()
    missing = [skill for skill in ids if skill not in text]
    assert not missing, (path, missing)
print("discover_routes_ok=2")
PY
```

Expected:

```text
discover_routes_ok=2
```

- [ ] **Step 4: Commit routing updates**

Run:

```bash
git add skills/zh/testing-workflows/discover-testing/reference.md skills/en/testing-workflows/discover-testing/reference.md
git commit -m "docs: route tool-specific testing skills"
```

Expected: commit succeeds.

---

### Task 5: Regenerate Installer Shortcuts

**Files:**
- Modify/Create: `installers/zh/<skill-id>/mac/*.sh`
- Modify/Create: `installers/zh/<skill-id>/windows/*.ps1`
- Modify/Create: `installers/en/<skill-id>/mac/*.sh`
- Modify/Create: `installers/en/<skill-id>/windows/*.ps1`
- Modify: `installers/README.md`

- [ ] **Step 1: Regenerate installer shortcuts**

Run:

```bash
bash scripts/generate-install-shortcuts.sh
```

Expected output contains:

```text
generated_skills=66
generated_scripts=792
```

This count assumes 33 testing-type skills plus 4 workflow skills in each language.

- [ ] **Step 2: Verify shortcut examples for one new skill**

Run:

```bash
ls installers/zh/api-test-postman/mac installers/en/ui-test-playwright/windows installers/zh/performance-test-jmeter/mac
```

Expected: each listed directory contains scripts for `claudecode`, `codex`, `cursor`, `kiro`, `opencode`, and `trae`.

- [ ] **Step 3: Commit installer updates**

Run:

```bash
git add installers
git commit -m "chore: regenerate skill installers"
```

Expected: commit succeeds.

---

### Task 6: Run Repository Validation

**Files:**
- No planned file changes unless validation identifies new-skill issues.

- [ ] **Step 1: Run directory validation**

Run:

```bash
python3 scripts/organize_project_dirs.py
```

Expected output contains:

```text
issues=0
```

- [ ] **Step 2: Run full quality checks**

Run:

```bash
bash scripts/check_skills_quality.sh
```

Expected output ends with:

```text
Skills quality checks passed.
```

- [ ] **Step 3: Check worktree scope**

Run:

```bash
git status --short
```

Expected: only pre-existing unrelated worktree changes remain, or no changes remain from this implementation. New-skill changes should already be committed by prior tasks.

- [ ] **Step 4: Final implementation report**

Report:

- Eight new skill IDs added.
- Chinese and English directories created.
- README, index, discover routing, and installers updated.
- Validation commands run and their results.
- Any pre-existing unrelated worktree changes that were intentionally left untouched.

No commit is required for this report step.

---

## Self-Review

Spec coverage:

- Eight independent skills: covered by Tasks 1 and 2.
- Chinese and English versions: covered by Task 1 generation and Task 2 checks.
- Complete directory layout: covered by Task 1 file creation.
- Lightweight scripts: covered by Task 1 `scripts/run-tests.sh`.
- README, index, routing, installers: covered by Tasks 3, 4, and 5.
- Validation: covered by Task 6.
- Git safety with existing unrelated changes: covered in file structure notes and Task 6.

Completion marker scan:

- This plan intentionally contains no deferred work markers, incomplete file names, or undefined task references.

Type consistency:

- Skill IDs are consistent across the spec, file paths, script constants, documentation snippets, and verification commands.
