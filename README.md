<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# Awesome QA Skills

按语言分区的 **AI 测试辅助技能库**（Agent Skills）。面向 Codex、Cursor、Claude Code、Kiro、OpenCode、Trae 等工具，提供可独立安装、可组合调用的测试工作流与测试类型技能。

[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-blue.svg)](./LICENSE)
[![Skills](https://img.shields.io/badge/skills-156%20(zh%2Ben)-0A7EA4)](./docs/catalog/skills-index.md)
[![Workflows](https://img.shields.io/badge/workflows-10-informational)](./skills/zh/testing-workflows/)
[![Testing types](https://img.shields.io/badge/testing%20types-65-informational)](./skills/zh/testing-types/)
[![Skill engineering](https://img.shields.io/badge/skill%20engineering-3-informational)](./skills/zh/skill-engineering/)
[![skills.sh](https://skills.sh/b/naodeng/awesome-qa-skills)](https://skills.sh/naodeng/awesome-qa-skills)

**在线站点：** [https://inaodeng.com/qaskills/](https://inaodeng.com/qaskills/)

---

## 为什么用这个仓库

| 能力 | 说明 |
| --- | --- |
| 双语对齐 | `skills/zh` 与 `skills/en` 同名目录、同结构，团队可按语言选用 |
| 覆盖完整测试链 | 从需求分析、策略、用例、执行到缺陷与报告 |
| 工作流 + 类型技能 | 日常 / 迭代 / 发布、角色质量视角与多角色汇总工作流，配合 65 类专项技能按需组合 |
| 开箱即装 | 支持一键安装与单 skill 安装脚本 |
| 可评测可演进 | 全量 skill 附带 `evals/`，可用 [skill-up](https://github.com/alibaba/skill-up) 校验与实跑 |

每个 skill 目录复制出去后应自洽：含 `SKILL.md`、主提示词、工具元数据，以及可选的示例、模板、脚本与评测用例。

## 能力演进地图

仓库以稳定目录提供安装，以能力阶段帮助选择和演进：

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

| 阶段 | 关注问题 | 现有入口 | 演进方向 |
| --- | --- | --- | --- |
| Core QA Skills | 需求、策略、用例、执行和报告如何形成基础质量闭环 | `requirements-analysis`、`test-strategy`、`functional-testing`、`test-reporting` | 保持基础完整，不重复拆包 |
| Engineering QA Skills | 如何前移质量、评估变更、诊断问题并做性能决策 | `code-review`、`automation-testing`、`performance-testing` | Shift Left、变更与执行智能、性能工程 |
| Production Quality Skills | 如何基于发布和生产证据进行质量决策 | `release-testing-workflow`、`test-reporting` | 生产验证、事故和可观测性 |
| AI Native QA Skills | 如何验证 AI 功能、LLM、Prompt、Agent 和安全边界 | AI 功能、LLM、Prompt、Agent 与安全专项能力已提供 | Testing for AI 专项 Skill |

`ai-assisted-testing` 是横向的 **AI for QA**，不等同于 AI Native QA 的 Testing for AI。完整的六迭代路线、29 个新增 Skill 和跨仓 Prompt Baseline 映射见 [演进路线图](docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md)。

## 支持的 AI 工具

| 工具 | 典型安装目标 |
| --- | --- |
| Codex | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| Claude Code | Claude skills 目录（见安装文档） |
| Kiro / OpenCode / Trae | 见 [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) |

也可手动 `cp -r` 单个 skill 目录到对应工具的 skills 路径。

## 5 分钟上手

### 1. 克隆仓库

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. 安装技能（任选其一）

```bash
# 一键：全部工具 × 中英文
bash ./install-skills-mac.sh --tool all --lang all

# 仅 Codex + 中文
bash ./install-skills-mac.sh --tool codex --lang zh

# 单个 skill（示例：功能测试 → Codex）
bash installers/zh/functional-testing/mac/codex.sh
```

也可以使用 `npx skills` 安装到支持的 AI 工具（需要 Node.js）：

```bash
# 安装全部中文 skills 到 Codex
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh -g -a codex -y

# 只安装一个 skill
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh/testing-types/functional-testing -g -a codex -y
```

英文 skills 将 URL 中的 `skills/zh` 替换为 `skills/en`。建议一次只安装一种语言，避免同名 skill 相互覆盖。

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

手动复制：

```bash
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/
```

完整参数与工具路径说明：[scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

### 3. 在工具中调用

```text
@skill functional-testing
帮我为用户登录功能生成测试用例
```

不确定用哪个 skill 时，先用路由技能：

```text
@skill discover-testing
我要做一次发布前回归，该选哪些技能？
```

---

## 技能目录

每种语言共 **78** 个 Skill：10 个工作流、65 个测试类型和 3 个 Skill Engineering；中英文合计 **156** 个目录。物理目录保持稳定，下面只提供逻辑导航。

### 跨阶段工作流

工作流负责串联研发测试阶段，不属于四个能力层中的第五层。

#### 需求发现与分析

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| Testing Skill Discovery | [`discover-testing`](skills/zh/testing-workflows/discover-testing/) | Use this skill when you need to route a request to the right testing skill before execution; triggers include 测试技能路由、discover testing and which testing skill. |
| 产品质量视角 | [`product-quality-perspective`](skills/zh/testing-workflows/product-quality-perspective/) | 从产品视角在需求、策略、评审、用例和报告阶段识别用户价值、业务规则、验收与风险。 |
| QA 质量视角 | [`qa-quality-perspective`](skills/zh/testing-workflows/qa-quality-perspective/) | 在质量各阶段基于证据评估可测试性、风险驱动覆盖、缺陷风险与质量结论边界。 |
| UX 质量视角 | [`ux-quality-perspective`](skills/zh/testing-workflows/ux-quality-perspective/) | 以 UX 视角在质量阶段识别信息架构、交互状态、一致性、响应式与无障碍风险。 |
| 技术质量视角 | [`technical-quality-perspective`](skills/zh/testing-workflows/technical-quality-perspective/) | 在指定交付阶段基于证据输出技术质量发现。 |

#### 开发与迭代

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 日常测试工作流程（中文版） | [`daily-testing-workflow`](skills/zh/testing-workflows/daily-testing-workflow/) | Use this skill when you need a day-by-day QA routine including planning, execution, bug reporting, and end-of-day wrap-up; triggers include 日常测试工作流程 and daily… |
| 迭代测试工作流程（中文版） | [`sprint-testing-workflow`](skills/zh/testing-workflows/sprint-testing-workflow/) | Use this skill when you need a sprint-based QA workflow from planning through review and retrospective; triggers include 迭代测试工作流程 and sprint testing workflow. |
| 项目交付视角 | [`project-delivery-perspective`](skills/zh/testing-workflows/project-delivery-perspective/) | 在支持的策略与报告评审阶段记录带来源的交付约束和行动，不改变质量事实。 |

#### 发布与综合

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 发布测试工作流程（中文版） | [`release-testing-workflow`](skills/zh/testing-workflows/release-testing-workflow/) | Use this skill when you need release-phase QA workflow from T-14 planning to go/no-go and post-release monitoring; triggers include 发布测试工作流程 and release testin… |
| 多角色质量汇总 | [`multi-role-quality-synthesis`](skills/zh/testing-workflows/multi-role-quality-synthesis/) | 将同一阶段的多角色报告合并为保留来源、分歧和质量边界的可追溯汇总 |

### 四层能力体系与研发测试阶段

每个测试类型 Skill 只列一次；跨阶段协作由路由器和工作流补充。

#### Core QA Skills — 基础质量能力

##### 需求发现与分析

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 需求分析（中文版） <!-- data-skill:requirements-analysis --> | [`requirements-analysis`](skills/zh/testing-types/requirements-analysis/) | Use this skill when you need to analyze requirements, identify test points, boundaries, dependencies, and risks before test design; triggers include 需求分析 and r… |
| 需求分析加强版 <!-- data-skill:requirements-analysis-plus --> | [`requirements-analysis-plus`](skills/zh/testing-types/requirements-analysis-plus/) | Use this skill when you need to parse Word/HTML/JSON/Markdown/Excel requirements and produce a structured analysis; triggers include 需求分析增强、requirements analys… |

##### 方案设计与测试策略

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试策略（中文版） <!-- data-skill:test-strategy --> | [`test-strategy`](skills/zh/testing-types/test-strategy/) | Use this skill when you need to define a test strategy covering scope, methods, resources, risks, and quality gates; triggers include 测试策略 and test strategy. |
| 测试策略加强版 <!-- data-skill:test-strategy-plus --> | [`test-strategy-plus`](skills/zh/testing-types/test-strategy-plus/) | Use this skill when you need a structured test strategy from requirement, analysis, tech, and plan docs; triggers include 测试策略增强、test strategy plus and advance… |
| 测试策略评审 <!-- data-skill:test-strategy-review --> | [`test-strategy-review`](skills/zh/testing-types/test-strategy-review/) | 基于证据评审测试策略，区分阻塞项与条件项并给出 Human 待决的 AI 建议 |

##### 测试设计与准备

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试用例编写（中文版） <!-- data-skill:test-case-writing --> | [`test-case-writing`](skills/zh/testing-types/test-case-writing/) | Use this skill when you need to create high-quality test cases with normal, exception, and boundary scenarios; triggers include 测试用例编写 and test case writing. |
| 测试用例编写加强版 <!-- data-skill:testcase-writer-plus --> | [`testcase-writer-plus`](skills/zh/testing-types/testcase-writer-plus/) | Use this skill when you need high-quality test cases from requirements and analysis artifacts; triggers include 测试用例编写增强、testcase writer plus and advanced test… |
| 测试用例评审（中文版） <!-- data-skill:test-case-reviewer --> | [`test-case-reviewer`](skills/zh/testing-types/test-case-reviewer/) | Use this skill when you need to review test cases for completeness, clarity, maintainability, and missing scenarios; triggers include 测试用例评审 and test case revi… |
| 测试用例评审加强版 <!-- data-skill:test-case-reviewer-plus --> | [`test-case-reviewer-plus`](skills/zh/testing-types/test-case-reviewer-plus/) | Use this skill when you need structured test-case review findings from requirements, strategy, and case docs; triggers include 用例评审增强、test case reviewer plus a… |

##### 测试执行与分析

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 功能测试（中文版） <!-- data-skill:functional-testing --> | [`functional-testing`](skills/zh/testing-types/functional-testing/) | Use this skill when you need to design functional test plans or cases for business flows, UI, data, and integrations; triggers include 功能测试 and functional test… |
| API 测试（中文版） <!-- data-skill:api-testing --> | [`api-testing`](skills/zh/testing-types/api-testing/) | Use this skill when you need to design API test plans or cases for REST, GraphQL, or gRPC interfaces; triggers include API 测试 and api testing. |
| 手动/探索性测试（中文版） <!-- data-skill:manual-testing --> | [`manual-testing`](skills/zh/testing-types/manual-testing/) | Use this skill when you need to plan manual or exploratory testing with charters, heuristics, and session records; triggers include 手动测试 and exploratory testin… |
| 移动端测试（中文版） <!-- data-skill:mobile-testing --> | [`mobile-testing`](skills/zh/testing-types/mobile-testing/) | Use this skill when you need to design mobile test plans for iOS or Android covering functionality, compatibility, performance, network, and security; triggers… |
| 可访问性测试（中文版） <!-- data-skill:accessibility-testing --> | [`accessibility-testing`](skills/zh/testing-types/accessibility-testing/) | Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include 可访问性测试 and… |
| 安全测试（中文版） <!-- data-skill:security-testing --> | [`security-testing`](skills/zh/testing-types/security-testing/) | Use this skill when you need to design security testing around OWASP risks, vulnerability scanning, and penetration scenarios; triggers include 安全测试 and securi… |

##### 发布、缺陷与报告

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 缺陷上报（中文版） <!-- data-skill:bug-reporting --> | [`bug-reporting`](skills/zh/testing-types/bug-reporting/) | Use this skill when you need to write clear, reproducible bug reports with steps, environment details, and evidence; triggers include 缺陷上报 and bug reporting. |
| 测试报告（中文版） <!-- data-skill:test-reporting --> | [`test-reporting`](skills/zh/testing-types/test-reporting/) | Use this skill when you need to generate test reports with summary, metrics, defect analysis, and risk assessment; triggers include 测试报告 and test reporting. |
| 测试报告评审 <!-- data-skill:test-report-review --> | [`test-report-review`](skills/zh/testing-types/test-report-review/) | 核对测试报告与执行、缺陷和范围证据，形成 Human 待决的 AI 建议 |

#### Engineering QA Skills — 质量工程能力

##### 需求与质量左移

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 验收标准评审 <!-- data-skill:acceptance-criteria-review --> | [`acceptance-criteria-review`](skills/zh/testing-types/acceptance-criteria-review/) | 评审验收标准的可验证性与缺口 |
| 需求缺口分析 <!-- data-skill:requirement-gap-analysis --> | [`requirement-gap-analysis`](skills/zh/testing-types/requirement-gap-analysis/) | 识别需求信息缺口、冲突与影响 |
| 质量风险分析 <!-- data-skill:quality-risk-analysis --> | [`quality-risk-analysis`](skills/zh/testing-types/quality-risk-analysis/) | 基于证据识别并排序质量风险 |
| 可测试性分析 <!-- data-skill:testability-analysis --> | [`testability-analysis`](skills/zh/testing-types/testability-analysis/) | 评估需求或设计的可测试性与阻碍 |

##### 开发与持续集成

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 代码审查（中文版） <!-- data-skill:code-review --> | [`code-review`](skills/zh/testing-types/code-review/) | Risk-driven PR/diff code review with P0/P1/P2 findings and actionable fixes; triggers include 代码审查 and code review. |
| 变更影响分析 <!-- data-skill:change-impact-analysis --> | [`change-impact-analysis`](skills/zh/testing-types/change-impact-analysis/) | 分析变更的质量影响范围与风险 |
| PR 测试影响分析 <!-- data-skill:pr-test-impact-analysis --> | [`pr-test-impact-analysis`](skills/zh/testing-types/pr-test-impact-analysis/) | 从 PR 或 Diff 分析测试影响 |
| API 契约测试 <!-- data-skill:api-contract-testing --> | [`api-contract-testing`](skills/zh/testing-types/api-contract-testing/) | 验证 API 契约兼容性与变更风险 |
| 自动化测试（中文版） <!-- data-skill:automation-testing --> | [`automation-testing`](skills/zh/testing-types/automation-testing/) | Use this skill when you need to design automation testing approaches using patterns like POM, data-driven testing, or BDD; triggers include 自动化测试 and automatio… |

##### 测试数据与自动化实现

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试数据生成 <!-- data-skill:test-data-generation --> | [`test-data-generation`](skills/zh/testing-types/test-data-generation/) | 设计安全且具代表性的测试数据 |
| Bruno 接口自动化 <!-- data-skill:api-test-bruno --> | [`api-test-bruno`](skills/zh/testing-types/api-test-bruno/) | Use this skill when you need to parse multi-format API definitions and generate Bruno collections for executable regression; triggers include Bruno、Bruno 集合 an… |
| Postman API 测试 <!-- data-skill:api-test-postman --> | [`api-test-postman`](skills/zh/testing-types/api-test-postman/) | 设计 Postman 集合、环境、脚本和可用 Newman 执行的 API 回归方案。 |
| Pytest 接口自动化 <!-- data-skill:api-test-pytest --> | [`api-test-pytest`](skills/zh/testing-types/api-test-pytest/) | Use this skill when you need to parse multi-format API definitions and generate Pytest API automation; triggers include Pytest 接口测试、pytest api and API automati… |
| RestAssured 接口自动化 <!-- data-skill:api-test-restassure --> | [`api-test-restassure`](skills/zh/testing-types/api-test-restassure/) | Use this skill when you need to parse multi-format API definitions and generate Rest Assured Java test classes; triggers include Rest Assured、RestAssured and J… |
| Supertest 接口自动化 <!-- data-skill:api-test-supertest --> | [`api-test-supertest`](skills/zh/testing-types/api-test-supertest/) | Use this skill when you need to parse multi-format API definitions and generate executable Supertest scripts; triggers include Supertest、Node.js API 测试 and Sup… |
| Selenium UI 自动化测试 <!-- data-skill:ui-test-selenium --> | [`ui-test-selenium`](skills/zh/testing-types/ui-test-selenium/) | 设计 Selenium WebDriver UI 自动化方案，覆盖稳定定位、等待、Page Object、Grid 和 CI 执行。 |
| Playwright UI 自动化测试 <!-- data-skill:ui-test-playwright --> | [`ui-test-playwright`](skills/zh/testing-types/ui-test-playwright/) | 设计 Playwright Test 套件，覆盖 fixtures、projects、trace、截图、API+UI 组合和 CI 报告。 |
| TestCafe UI 自动化测试 <!-- data-skill:ui-test-testcafe --> | [`ui-test-testcafe`](skills/zh/testing-types/ui-test-testcafe/) | 设计 TestCafe UI 自动化方案，覆盖 fixture、selector、role、浏览器矩阵和报告。 |
| Cypress UI 自动化测试 <!-- data-skill:ui-test-cypress --> | [`ui-test-cypress`](skills/zh/testing-types/ui-test-cypress/) | 设计 Cypress e2e 与组件测试方案，覆盖 commands、fixtures、网络桩和 CI 报告。 |
| Puppeteer UI 自动化测试 <!-- data-skill:ui-test-puppeteer --> | [`ui-test-puppeteer`](skills/zh/testing-types/ui-test-puppeteer/) | 设计 Puppeteer 自动化方案，覆盖 Chromium 检查、截图、PDF、网络拦截和 CDP 场景。 |
| WebdriverIO UI 自动化测试 <!-- data-skill:ui-test-webdriverio --> | [`ui-test-webdriverio`](skills/zh/testing-types/ui-test-webdriverio/) | 设计 WebdriverIO 套件，覆盖配置、services、runner、Page Object、capabilities 和 reporters。 |

##### 测试执行与回归智能

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 不稳定测试分析 <!-- data-skill:flaky-test-analysis --> | [`flaky-test-analysis`](skills/zh/testing-types/flaky-test-analysis/) | 从运行证据分析间歇性测试失败 |
| 回归范围分析 <!-- data-skill:regression-scope-analysis --> | [`regression-scope-analysis`](skills/zh/testing-types/regression-scope-analysis/) | 按风险定义回归范围和排除依据 |
| 回归测试选择 <!-- data-skill:regression-test-selection --> | [`regression-test-selection`](skills/zh/testing-types/regression-test-selection/) | 从测试资产选择最小风险覆盖回归集 |
| AI 辅助测试（中文版） <!-- data-skill:ai-assisted-testing --> | [`ai-assisted-testing`](skills/zh/testing-types/ai-assisted-testing/) | Use this skill when you need AI-assisted testing workflows such as test data generation, root-cause analysis, and prioritization; triggers include AI 辅助测试 and… |

##### 性能工程与容量决策

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 性能测试（中文版） <!-- data-skill:performance-testing --> | [`performance-testing`](skills/zh/testing-types/performance-testing/) | Use this skill when you need to design performance testing for load, stress, spike, endurance, or capacity objectives; triggers include 性能测试 and performance te… |
| k6 性能测试 <!-- data-skill:performance-test-k6 --> | [`performance-test-k6`](skills/zh/testing-types/performance-test-k6/) | Use this skill when you need k6 load/stress/spike/soak scope, scripts, or runnable entry points; triggers include k6、k6 性能测试 and k6 performance testing. |
| Gatling 性能测试 <!-- data-skill:performance-test-gatling --> | [`performance-test-gatling`](skills/zh/testing-types/performance-test-gatling/) | Use this skill when you need Gatling performance scope, simulations, or runnable entry points; triggers include Gatling、Gatling 性能测试 and Gatling simulation. |
| JMeter 性能测试 <!-- data-skill:performance-test-jmeter --> | [`performance-test-jmeter`](skills/zh/testing-types/performance-test-jmeter/) | 设计 JMeter 测试计划，覆盖 Thread Group、Sampler、数据集、断言、Timer、CLI 执行和 HTML 报告。 |
| 性能负载建模 <!-- data-skill:performance-workload-modeling --> | [`performance-workload-modeling`](skills/zh/testing-types/performance-workload-modeling/) | 建立基于证据的性能负载模型 |
| 性能结果分析 <!-- data-skill:performance-result-analysis --> | [`performance-result-analysis`](skills/zh/testing-types/performance-result-analysis/) | 解释性能结果、证据质量与风险 |
| 性能瓶颈分析 <!-- data-skill:performance-bottleneck-analysis --> | [`performance-bottleneck-analysis`](skills/zh/testing-types/performance-bottleneck-analysis/) | 形成可验证的性能瓶颈假设 |
| 性能回归分析 <!-- data-skill:performance-regression-analysis --> | [`performance-regression-analysis`](skills/zh/testing-types/performance-regression-analysis/) | 比较版本性能证据并评估回归风险 |
| 容量规划分析 <!-- data-skill:capacity-planning-analysis --> | [`capacity-planning-analysis`](skills/zh/testing-types/capacity-planning-analysis/) | 评估容量需求、余量和规划风险 |

##### 复盘与持续改进

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 根因分析 <!-- data-skill:root-cause-analysis --> | [`root-cause-analysis`](skills/zh/testing-types/root-cause-analysis/) | 形成并验证基于证据的根因假设 |
| 日志分析 <!-- data-skill:log-analysis --> | [`log-analysis`](skills/zh/testing-types/log-analysis/) | 从日志提取时间线、异常和证据 |

#### Production Quality Skills — 生产质量能力

##### 发布与生产验证

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 生产验证 <!-- data-skill:production-verification --> | [`production-verification`](skills/zh/testing-types/production-verification/) | 基于证据规划或评估生产验证 |

##### 生产运行与事故响应

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 生产事故分析 <!-- data-skill:production-incident-analysis --> | [`production-incident-analysis`](skills/zh/testing-types/production-incident-analysis/) | 分析生产事故证据、影响与后续动作 |
| 分布式 Trace 分析 <!-- data-skill:distributed-trace-analysis --> | [`distributed-trace-analysis`](skills/zh/testing-types/distributed-trace-analysis/) | 从分布式 Trace 关联调用链和证据 |
| 指标异常分析 <!-- data-skill:metrics-anomaly-analysis --> | [`metrics-anomaly-analysis`](skills/zh/testing-types/metrics-anomaly-analysis/) | 识别指标异常、基线与排查证据 |

#### AI Native QA Skills — AI 原生质量能力

##### AI 功能需求与风险

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| AI 功能测试 <!-- data-skill:ai-feature-testing --> | [`ai-feature-testing`](skills/zh/testing-types/ai-feature-testing/) | 设计 AI 功能行为、风险和边界测试 |

##### LLM 与 Prompt 评测设计

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| LLM Eval 设计 <!-- data-skill:llm-evaluation-design --> | [`llm-evaluation-design`](skills/zh/testing-types/llm-evaluation-design/) | 设计 LLM 评测集、判定与人工复核边界 |
| LLM 测试 <!-- data-skill:llm-testing --> | [`llm-testing`](skills/zh/testing-types/llm-testing/) | 验证 LLM 行为、失败模式和质量边界 |
| Prompt 测试 <!-- data-skill:prompt-testing --> | [`prompt-testing`](skills/zh/testing-types/prompt-testing/) | 测试 Prompt 行为、边界和版本回归 |

##### Agent、工具与安全测试

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| AI Agent 测试 <!-- data-skill:ai-agent-testing --> | [`ai-agent-testing`](skills/zh/testing-types/ai-agent-testing/) | 测试 AI Agent 的目标、状态、恢复和安全边界 |
| Agent 工具调用测试 <!-- data-skill:agent-tool-testing --> | [`agent-tool-testing`](skills/zh/testing-types/agent-tool-testing/) | 验证 Agent 工具调用契约、授权和副作用边界 |
| Prompt Injection 测试 <!-- data-skill:prompt-injection-testing --> | [`prompt-injection-testing`](skills/zh/testing-types/prompt-injection-testing/) | 设计 AI 系统 Prompt 注入防护测试 |

### Skill Engineering（横向治理）

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| Skill 变更验证 | [`skill-change-verification`](skills/zh/skill-engineering/skill-change-verification/) | 按变更范围选择验证证据，并区分静态、评测和运行时结论。 |
| Skill 文案契约审查 | [`skill-prose-review`](skills/zh/skill-engineering/skill-prose-review/) | 审查 Skill、Prompt 与文档的可执行契约、边界和证据要求。 |
| 过程性文案清理 | [`skill-prose-trim`](skills/zh/skill-engineering/skill-prose-trim/) | 清理文案中的审查和设计过程残留，同时保留当前状态契约。 |

Skill Engineering 服务所有能力层，不改变产品能力分类。英文 Skill 使用相同目录名；可从页面顶部切换语言。

## 仓库结构

```text
awesome-qa-skills/
├── skills/
│   ├── zh/                      # 中文技能
│   │   ├── testing-workflows/   # 工作流
│   │   ├── testing-types/       # 测试类型
│   │   └── skill-engineering/   # 技能工程
│   └── en/                      # 英文技能（结构同上）
├── scripts/                     # 安装、校验、评测辅助脚本
├── installers/                  # 按 skill / 工具生成的安装快捷脚本
├── resources/                   # 公共参考素材池（非 skill 安装源）
├── legacy-prompts/              # 旧版根级提示词（正式入口见各 skill 内 prompts/）
├── AGENTS.md                    # Coding Agent 操作约定
├── docs/catalog/                # 全量索引与关系图
├── README.md / README_EN.md
└── LICENSE                      # PolyForm Noncommercial 1.0.0
```

### 单个 Skill 约定结构

```text
skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/
├── SKILL.md                 # 入口 + YAML frontmatter（必需）
├── prompts/                 # 主提示词（必需）
├── agents/openai.yaml       # OpenAI / Codex 元数据（必需）
├── evals/                   # skill-up 评测用例（本仓库全量具备）
├── output-formats.md        # 可选：多格式输出说明
├── quick-start.md           # 可选：最短上手路径
├── references/ · examples/ · scripts/
└── ...
```

详细规范：[skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) · [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)

## 设计原则

- **语言分区，名称对齐**：中英文 skill 目录名一致，不再使用 `-en` 后缀；英文 prompt 文件名不带 `_EN`。
- **独立可安装**：禁止 skill A 硬链 skill B 内部文件；跨 skill 只做文案推荐。
- **渐进披露**：`SKILL.md` 保持精简；细节放在 `prompts/`、`references/`、`examples/`。
- **可执行产出**：默认 Markdown；需要 Excel/CSV/JSON/Word 时按 `output-formats.md` 切换。
- **安全默认**：示例与文档不硬编码真实 token、密码、私钥；使用环境变量或占位符。

## 质量与评测

提交前建议在仓库根目录运行：

```bash
bash scripts/check_skills_quality.sh
```

该门禁覆盖目录整理、agents 元数据、独立安装约束、完整性校验，以及 skill-up evals YAML 校验。

用 [skill-up](https://github.com/alibaba/skill-up) 校验 / 实跑（可选）：

```bash
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash
bash scripts/validate_skill_evals.sh
bash scripts/run_skill_eval.sh skills/zh/testing-types/functional-testing/evals/eval.yaml
```

推荐试点：`functional-testing`、`api-testing`、`api-test-bruno`、`bug-reporting`、`performance-test-k6`。说明见 [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)。

## 文档导航

| 文档 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Coding Agent 约定与质量检查 |
| [skills-index.md](docs/catalog/skills-index.md) | 全量技能索引 |
| [QA_SKILLS_EVOLUTION_ROADMAP.md](docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md) | 四层能力演进与研发测试阶段地图 |
| [DOCUMENTATION_POLICY.md](docs/governance/DOCUMENTATION_POLICY.md) | 中文优先的双语文档治理策略 |
| [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) | 目录与命名规范 |
| [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md) | 编写与 skill-up 评测约定 |
| [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) | 安装参数与工具路径 |
| [FAQ.md](FAQ.md) | 常见问题 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献流程 |
| [skills-graph.md](docs/catalog/skills-graph.md) | 技能关系图（参考） |

## 贡献

欢迎提交 Issue / PR：新增 skill、补齐双语、改进 prompt 与 evals、完善安装与文档。

1. 阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)
2. 中英文通常需同步更新（除非明确只要单语）
3. 本地跑通 `bash scripts/check_skills_quality.sh` 后再提 PR

## 许可证

本仓库采用 [PolyForm Noncommercial License 1.0.0](./LICENSE)。您可以自由使用、修改和分发本软件，但仅限非商业目的（如个人学习、研究、实验、慈善机构、教育机构、公共研究组织、政府机构等用途）。
