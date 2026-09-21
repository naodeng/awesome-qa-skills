<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# Awesome QA Skills

按语言分区的 **AI 测试辅助技能库**（Agent Skills）。面向 Codex、Cursor、Claude Code、Kiro、OpenCode、Trae 等工具，提供可独立安装、可组合调用的测试工作流与测试类型技能。

[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-blue.svg)](./LICENSE)
[![Skills](https://img.shields.io/badge/skills-328%20(zh%2Ben)-0A7EA4)](./docs/catalog/skills-index.md)
[![Workflows](https://img.shields.io/badge/workflows-10-informational)](./skills/zh/testing-workflows/)
[![Testing types](https://img.shields.io/badge/testing%20types-149-informational)](./skills/zh/testing-types/)
[![Skill engineering](https://img.shields.io/badge/skill%20engineering-5-informational)](./skills/zh/skill-engineering/)
[![skills.sh](https://skills.sh/b/naodeng/awesome-qa-skills)](https://skills.sh/naodeng/awesome-qa-skills)

**在线目录：** [https://inaodeng.com/qaskills/](https://inaodeng.com/qaskills/)

**快速入口：** [完整技能索引](docs/catalog/skills-index.md) · [Composition 路由目录](docs/catalog/skills-composition.md) · [安装说明](scripts/INSTALL_SKILLS.md) · [Skills CLI 集成指南](docs/integrations/SKILLS_CLI_INTEGRATION.md) · [v1.4 治理收口](docs/governance/PHASE_0_V1_4_CLOSEOUT.md) · [贡献指南](CONTRIBUTING.md)

---

## 你可以用它做什么

这是一个面向 AI 测试协作的双语 Skill 集合。每个 Skill 都可以独立复制、安装和调用，也可以组合成从需求分析到发布验证的质量工作流。

| 场景 | 代表入口 | 适合解决的问题 |
| --- | --- | --- |
| 需求与测试设计 | `requirements-analysis`、`test-strategy`、`test-case-writing` | 从需求、风险和约束形成可追踪的测试方案与用例 |
| 功能、API 与 UI 测试 | `functional-testing`、`api-testing`、`ui-test-playwright` | 为业务流程、接口和浏览器场景设计可执行测试 |
| 回归、性能与质量工程 | `regression-test-selection`、`performance-testing`、`code-review` | 根据变更和风险选择回归范围，分析性能并前移质量 |
| 发布与生产质量 | `release-testing-workflow`、`production-verification`、`metrics-anomaly-analysis` | 支持发布决策、生产验证、事故和指标分析 |
| AI 功能与 Agent 安全 | `ai-feature-testing`、`llm-testing`、`ai-agent-testing`、`prompt-injection-testing` | 验证 AI 行为、评测、工具调用和安全边界 |
| Skill 工程与治理 | `skill-quality-review`、`skill-evaluation`、`skill-change-verification`、`skill-prose-review` | 检查 Skill 包质量、评测证据、变更契约和文案边界 |

每个 Skill 目录复制出去后应保持自洽：包含 `SKILL.md`、主提示词、工具元数据，以及按需提供的示例、模板、脚本和评测用例。

## 快速开始

### 1. 安装单个 Skill（推荐）

#### 英文 Skill（默认）

仓库级入口默认发现 English Skills，并按 canonical name 安装：

```bash
# 安装英文 functional-testing
npx skills add naodeng/awesome-qa-skills --skill functional-testing

# 可选：指定 Codex 目标
npx skills add naodeng/awesome-qa-skills --skill functional-testing -a codex

# 安装全部英文 Skills
npx skills add naodeng/awesome-qa-skills
```

#### 中文 Skill

中文 Skill 需要显式指定 `skills/zh` 源。EN/ZH 有意共享 canonical name，同一 target 默认只安装一种语言：

```bash
# 安装中文 functional-testing
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing

# 安装全部中文 Skills
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh
```

高级、CI 固定版本、中文集合、`list` / `use` / `update` / `remove` 以及 Tested / Ecosystem compatible 边界见 [Skills CLI 集成指南](docs/integrations/SKILLS_CLI_INTEGRATION.md)。

### 2. 使用一键安装脚本

```bash
# macOS / Linux：安装中文 Skill 到 Codex
bash ./install-skills-mac.sh --tool codex --lang zh

# macOS / Linux：全部工具 × 中英文
bash ./install-skills-mac.sh --tool all --lang all
```

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool codex -Lang zh
```

### 3. 克隆完整仓库

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git .skills/awesome-qa-skills
```

### 4. 作为 Git 子模块

```bash
git submodule add https://github.com/naodeng/awesome-qa-skills.git .skills/awesome-qa-skills
```

### 5. 手动复制

```bash
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/
```

单个 Skill 的快捷安装器、目标路径和完整参数见 [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)。

## 使用方式

如果你的 AI 工具支持 Agent Skills 的自动发现，可以直接用自然语言描述目标；需要显式调用时，指定 Skill 名称即可。

| 你可以这样说 | 推荐入口 |
| --- | --- |
| “帮我为用户登录功能生成测试用例” | `functional-testing` |
| “我要覆盖这个 REST API 的错误、幂等和分页场景” | `api-testing` |
| “这次发布前应该做哪些回归和 Go/No-Go 检查？” | `release-testing-workflow` |
| “请根据当前变更选择最小风险回归集” | `regression-test-selection` |
| “帮我评估这个 LLM 功能的行为和安全边界” | `llm-testing`、`prompt-injection-testing` |

不确定从哪里开始时，先调用路由 Skill：

```text
@skill discover-testing
我要做一次发布前回归，该选哪些 Skill？
```

如果需要查看五条结构化路线的主/辅 Skill 和边界，打开 [Composition 路由目录](docs/catalog/skills-composition.md)；单独复制 `discover-testing` 时使用其目录内的 `reference.md`。

## Skill 分类

先按研发 / 测试阶段选择分类，再从对应入口安装或调用。已经知道名称时，直接打开[完整技能索引](docs/catalog/skills-index.md)。

| 分类 | 包含内容 | 入口 |
| --- | --- | --- |
| 跨阶段工作流 | 路由、日常 / 迭代 / 发布、质量视角和多角色汇总 | [查看工作流](#跨阶段工作流) |
| Core QA Skills | 需求、策略、测试设计、执行、缺陷和报告 | [查看基础质量能力](#core-qa-skills--基础质量能力) |
| Engineering QA Skills | 质量左移、代码 / API / UI、回归、性能和持续改进 | [查看质量工程能力](#engineering-qa-skills--质量工程能力) |
| Production Quality Skills | 发布验证、生产验证、事故、Trace 和指标分析 | [查看生产质量能力](#production-quality-skills--生产质量能力) |
| AI Native QA Skills | AI 功能、LLM、Prompt、Agent 和安全测试 | [查看 AI 原生质量能力](#ai-native-qa-skills--ai-原生质量能力) |
| Skill Engineering | Skill 包质量审查、评测、变更验证、文案契约审查和过程性文案清理 | [查看 Skill Engineering](#skill-engineering横向治理) |

## 能力分层

仓库用稳定目录负责安装，用能力层帮助选择和演进：

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

`ai-assisted-testing` 是横向的 **AI for QA**，不等同于 AI Native QA 的 Testing for AI。六迭代路线与 Prompt Baseline 映射见[演进路线图](docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md)；长期 Existing / Enhance / Merge / Match / New 治理见 [Skill 治理路线图](docs/governance/SKILL_GOVERNANCE_ROADMAP.md)。v1.4 的治理证据、版本规划和剩余边界见 [Phase 0 收口](docs/governance/PHASE_0_V1_4_CLOSEOUT.md)。

---

## 完整技能目录

每种语言共 **164** 个 Skill：10 个工作流、149 个测试类型和 5 个 Skill Engineering；中英文合计 **328** 个目录。物理目录保持稳定，下面只提供逻辑导航。

### 跨阶段工作流

工作流负责串联研发测试阶段，不属于四个能力层中的第五层。

#### 需求发现与分析

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试技能路由 | [`discover-testing`](skills/zh/testing-workflows/discover-testing/) | 在执行前根据需求、阶段和风险选择合适的测试 Skill。 |
| 产品质量视角 | [`product-quality-perspective`](skills/zh/testing-workflows/product-quality-perspective/) | 从产品视角在需求、策略、评审、用例和报告阶段识别用户价值、业务规则、验收与风险。 |
| QA 质量视角 | [`qa-quality-perspective`](skills/zh/testing-workflows/qa-quality-perspective/) | 在质量各阶段基于证据评估可测试性、风险驱动覆盖、缺陷风险与质量结论边界。 |
| UX 质量视角 | [`ux-quality-perspective`](skills/zh/testing-workflows/ux-quality-perspective/) | 以 UX 视角在质量阶段识别信息架构、交互状态、一致性、响应式与无障碍风险。 |
| 技术质量视角 | [`technical-quality-perspective`](skills/zh/testing-workflows/technical-quality-perspective/) | 在指定交付阶段基于证据输出技术质量发现。 |

#### 开发与迭代

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 日常测试工作流程 | [`daily-testing-workflow`](skills/zh/testing-workflows/daily-testing-workflow/) | 按日常节奏完成计划、执行、缺陷跟踪和日终收口。 |
| 迭代测试工作流程 | [`sprint-testing-workflow`](skills/zh/testing-workflows/sprint-testing-workflow/) | 覆盖迭代计划、测试执行、评审和复盘的质量工作流。 |
| 项目交付视角 | [`project-delivery-perspective`](skills/zh/testing-workflows/project-delivery-perspective/) | 在支持的策略与报告评审阶段记录带来源的交付约束和行动，不改变质量事实。 |

#### 发布与综合

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 发布测试工作流程 | [`release-testing-workflow`](skills/zh/testing-workflows/release-testing-workflow/) | 从发布前计划到 Go/No-Go 决策和发布后监控的质量工作流。 |
| 多角色质量汇总 | [`multi-role-quality-synthesis`](skills/zh/testing-workflows/multi-role-quality-synthesis/) | 将同一阶段的多角色报告合并为保留来源、分歧和质量边界的可追溯汇总 |

### 四层能力体系与研发测试阶段

每个测试类型 Skill 只列一次；跨阶段协作由路由器和工作流补充。

#### Core QA Skills — 基础质量能力

##### 需求发现与分析

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 需求分析 <!-- data-skill:requirements-analysis --> | [`requirements-analysis`](skills/zh/testing-types/requirements-analysis/) | 在测试设计前识别需求测试点、边界、依赖和风险。 |
| 需求分析加强版 <!-- data-skill:requirements-analysis-plus --> | [`requirements-analysis-plus`](skills/zh/testing-types/requirements-analysis-plus/) | 解析多种需求文档并输出结构化的需求分析。 |

##### 方案设计与测试策略

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试策略 <!-- data-skill:test-strategy --> | [`test-strategy`](skills/zh/testing-types/test-strategy/) | 定义测试范围、方法、资源、风险和质量门禁。 |
| 测试策略加强版 <!-- data-skill:test-strategy-plus --> | [`test-strategy-plus`](skills/zh/testing-types/test-strategy-plus/) | 基于需求、分析、技术和计划文档形成结构化测试策略。 |
| 测试策略评审 <!-- data-skill:test-strategy-review --> | [`test-strategy-review`](skills/zh/testing-types/test-strategy-review/) | 基于证据评审测试策略，区分阻塞项与条件项并给出 Human 待决的 AI 建议 |

##### 测试设计与准备

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试用例编写 <!-- data-skill:test-case-writing --> | [`test-case-writing`](skills/zh/testing-types/test-case-writing/) | 编写覆盖正常、异常和边界场景的高质量测试用例。 |
| 测试用例编写加强版 <!-- data-skill:testcase-writer-plus --> | [`testcase-writer-plus`](skills/zh/testing-types/testcase-writer-plus/) | 根据需求与分析产物生成高质量测试用例。 |
| 测试用例评审 <!-- data-skill:test-case-reviewer --> | [`test-case-reviewer`](skills/zh/testing-types/test-case-reviewer/) | 评审测试用例的完整性、清晰度、可维护性和遗漏场景。 |
| 测试用例评审加强版 <!-- data-skill:test-case-reviewer-plus --> | [`test-case-reviewer-plus`](skills/zh/testing-types/test-case-reviewer-plus/) | 从需求、策略和用例文档中形成结构化评审发现。 |
| 决策表测试 <!-- data-skill:decision-table-testing --> | [`decision-table-testing`](skills/zh/testing-types/decision-table-testing/) | 将条件、规则、动作和结果整理为可审计的规则组合。 |
| 状态迁移测试 <!-- data-skill:state-transition-testing --> | [`state-transition-testing`](skills/zh/testing-types/state-transition-testing/) | 从状态、事件、迁移和非法路径设计可追溯测试。 |
| 边界值测试 <!-- data-skill:boundary-value-testing --> | [`boundary-value-testing`](skills/zh/testing-types/boundary-value-testing/) | 基于边界模型选择最小且高风险的边界测试集。 |
| 等价类划分 <!-- data-skill:equivalence-partitioning --> | [`equivalence-partitioning`](skills/zh/testing-types/equivalence-partitioning/) | 将输入空间划分为可解释、可覆盖的等价类。 |
| 成对组合测试 <!-- data-skill:pairwise-testing --> | [`pairwise-testing`](skills/zh/testing-types/pairwise-testing/) | 用成对交互覆盖控制多参数组合爆炸。 |
| 组合测试 <!-- data-skill:combinatorial-testing --> | [`combinatorial-testing`](skills/zh/testing-types/combinatorial-testing/) | 根据交互强度和风险选择组合覆盖策略。 |
| 基于模型测试 <!-- data-skill:model-based-testing --> | [`model-based-testing`](skills/zh/testing-types/model-based-testing/) | 从状态、流程或行为模型派生可追溯测试。 |
| 基于属性测试 <!-- data-skill:property-based-testing --> | [`property-based-testing`](skills/zh/testing-types/property-based-testing/) | 用不变量、生成策略和收缩规则验证属性。 |
| 变形测试 <!-- data-skill:metamorphic-testing --> | [`metamorphic-testing`](skills/zh/testing-types/metamorphic-testing/) | 在缺少可靠预言机时用输入变换和关系断言验证结果。 |

##### 测试执行与分析

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 功能测试 <!-- data-skill:functional-testing --> | [`functional-testing`](skills/zh/testing-types/functional-testing/) | 为业务流程、界面、数据和集成设计功能测试方案或用例。 |
| API 测试 <!-- data-skill:api-testing --> | [`api-testing`](skills/zh/testing-types/api-testing/) | 为 REST、GraphQL 或 gRPC 接口设计 API 测试方案或用例。 |
| 手动/探索性测试 <!-- data-skill:manual-testing --> | [`manual-testing`](skills/zh/testing-types/manual-testing/) | 使用章程、启发式方法和会话记录规划手动或探索性测试。 |
| 移动端测试 <!-- data-skill:mobile-testing --> | [`mobile-testing`](skills/zh/testing-types/mobile-testing/) | 覆盖功能、兼容性、性能、网络和安全的 iOS/Android 测试。 |
| 可访问性测试 <!-- data-skill:accessibility-testing --> | [`accessibility-testing`](skills/zh/testing-types/accessibility-testing/) | 按 WCAG、键盘导航和辅助技术场景设计可访问性测试。 |
| 安全测试 <!-- data-skill:security-testing --> | [`security-testing`](skills/zh/testing-types/security-testing/) | 围绕 OWASP 风险、漏洞扫描和渗透场景设计安全测试。 |

##### 发布、缺陷与报告

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 缺陷上报 <!-- data-skill:bug-reporting --> | [`bug-reporting`](skills/zh/testing-types/bug-reporting/) | 编写包含复现步骤、环境信息和证据的清晰缺陷报告。 |
| 测试报告 <!-- data-skill:test-reporting --> | [`test-reporting`](skills/zh/testing-types/test-reporting/) | 生成包含摘要、指标、缺陷分析和风险评估的测试报告。 |
| 测试报告评审 <!-- data-skill:test-report-review --> | [`test-report-review`](skills/zh/testing-types/test-report-review/) | 核对测试报告与执行、缺陷和范围证据，形成 Human 待决的 AI 建议 |

#### Engineering QA Skills — 质量工程能力

##### 需求与质量左移

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 验收标准评审 <!-- data-skill:acceptance-criteria-review --> | [`acceptance-criteria-review`](skills/zh/testing-types/acceptance-criteria-review/) | 评审验收标准的可验证性与缺口 |
| 需求缺口分析 <!-- data-skill:requirement-gap-analysis --> | [`requirement-gap-analysis`](skills/zh/testing-types/requirement-gap-analysis/) | 识别需求信息缺口、冲突与影响 |
| 质量风险分析 <!-- data-skill:quality-risk-analysis --> | [`quality-risk-analysis`](skills/zh/testing-types/quality-risk-analysis/) | 基于证据识别并排序质量风险 |
| 可测试性分析 <!-- data-skill:testability-analysis --> | [`testability-analysis`](skills/zh/testing-types/testability-analysis/) | 评估需求或设计的可测试性与阻碍 |
| 需求质量评审 <!-- data-skill:requirement-quality-review --> | [`requirement-quality-review`](skills/zh/testing-types/requirement-quality-review/) | 在测试设计前，从完整性、清晰度、可验证性、可行性、范围和证据质量评审需求 |
| 需求歧义分析 <!-- data-skill:requirement-ambiguity-analysis --> | [`requirement-ambiguity-analysis`](skills/zh/testing-types/requirement-ambiguity-analysis/) | 识别角色、对象、条件、数量、时间、状态和验收语句中的歧义 |
| 需求一致性分析 <!-- data-skill:requirement-consistency-analysis --> | [`requirement-consistency-analysis`](skills/zh/testing-types/requirement-consistency-analysis/) | 比较跨来源术语、标识、格式、状态、规则和行为的一致性 |
| 需求冲突检测 <!-- data-skill:requirement-conflict-detection --> | [`requirement-conflict-detection`](skills/zh/testing-types/requirement-conflict-detection/) | 识别同一适用范围内互斥的需求规则并保留 Human 决策边界 |
| 需求可追踪性分析 <!-- data-skill:requirement-traceability-analysis --> | [`requirement-traceability-analysis`](skills/zh/testing-types/requirement-traceability-analysis/) | 建立需求与验收、设计、代码、测试、缺陷和证据的双向追踪 |
| 业务规则提取 <!-- data-skill:business-rule-extraction --> | [`business-rule-extraction`](skills/zh/testing-types/business-rule-extraction/) | 从需求、政策和流程材料中提取有来源、有范围、有例外的业务规则 |
| 技术设计质量评审 <!-- data-skill:technical-design-quality-review --> | [`technical-design-quality-review`](skills/zh/testing-types/technical-design-quality-review/) | 从边界、失败、数据、安全、性能和可运维性评审技术设计 |
| API 设计质量评审 <!-- data-skill:api-design-quality-review --> | [`api-design-quality-review`](skills/zh/testing-types/api-design-quality-review/) | 评审 API 契约、错误、认证、幂等、分页、版本和消费者影响 |
| 数据库设计质量评审 <!-- data-skill:database-design-quality-review --> | [`database-design-quality-review`](skills/zh/testing-types/database-design-quality-review/) | 评审模型、约束、索引、生命周期、并发、迁移和恢复设计 |
| 可观测性设计评审 <!-- data-skill:observability-design-review --> | [`observability-design-review`](skills/zh/testing-types/observability-design-review/) | 评审信号、维度、语义、告警、隐私、基数、采样和保留策略 |
| 错误处理设计评审 <!-- data-skill:error-handling-design-review --> | [`error-handling-design-review`](skills/zh/testing-types/error-handling-design-review/) | 评审失败模式、重试、降级、传播、一致性和遥测设计 |
| 测试范围分析 <!-- data-skill:test-scope-analysis --> | [`test-scope-analysis`](skills/zh/testing-types/test-scope-analysis/) | 基于目标、风险、依赖和证据明确测试纳入、排除与深度 |
| 测试缺口分析 <!-- data-skill:test-gap-analysis --> | [`test-gap-analysis`](skills/zh/testing-types/test-gap-analysis/) | 从需求、风险、变更、缺陷和测试证据中发现未被充分保护的测试义务 |
| 基于风险的测试 <!-- data-skill:risk-based-testing --> | [`risk-based-testing`](skills/zh/testing-types/risk-based-testing/) | 将风险证据转换为测试优先级、方法、深度和范围取舍 |
| 边界场景发现 <!-- data-skill:edge-case-discovery --> | [`edge-case-discovery`](skills/zh/testing-types/edge-case-discovery/) | 从需求、状态、时间、资源和平台证据中发现边界候选 |
| 负向场景发现 <!-- data-skill:negative-scenario-discovery --> | [`negative-scenario-discovery`](skills/zh/testing-types/negative-scenario-discovery/) | 从产品证据中发现非法、拒绝、失败、降级和恢复候选 |

##### 可靠性与安全

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 可靠性测试 <!-- data-skill:reliability-testing --> | [`reliability-testing`](skills/zh/testing-types/reliability-testing/) | 围绕可靠性目标、故障模式和证据准备形成分析候选。 |
| 韧性测试 <!-- data-skill:resilience-testing --> | [`resilience-testing`](skills/zh/testing-types/resilience-testing/) | 分析降级、韧性和有限恢复证据。 |
| 混沌测试 <!-- data-skill:chaos-testing --> | [`chaos-testing`](skills/zh/testing-types/chaos-testing/) | 设计受控故障注入假设和安全边界。 |
| 故障切换测试 <!-- data-skill:failover-testing --> | [`failover-testing`](skills/zh/testing-types/failover-testing/) | 识别主备切换路径、触发条件和恢复证据。 |
| 恢复测试 <!-- data-skill:recovery-testing --> | [`recovery-testing`](skills/zh/testing-types/recovery-testing/) | 定义恢复目标、证据缺口和验证准备。 |
| 重试测试 <!-- data-skill:retry-testing --> | [`retry-testing`](skills/zh/testing-types/retry-testing/) | 分析重试安全、幂等、退避和耗尽行为。 |
| 超时测试 <!-- data-skill:timeout-testing --> | [`timeout-testing`](skills/zh/testing-types/timeout-testing/) | 分析超时预算、取消和下游边界。 |
| 熔断器测试 <!-- data-skill:circuit-breaker-testing --> | [`circuit-breaker-testing`](skills/zh/testing-types/circuit-breaker-testing/) | 分析熔断器状态、降级和恢复证据。 |
| 依赖故障测试 <!-- data-skill:dependency-failure-testing --> | [`dependency-failure-testing`](skills/zh/testing-types/dependency-failure-testing/) | 分类依赖故障并审查隔离与兜底证据。 |
| 灾备测试 <!-- data-skill:disaster-recovery-testing --> | [`disaster-recovery-testing`](skills/zh/testing-types/disaster-recovery-testing/) | 记录灾备目标、Runbook 和恢复验证准备。 |
| 身份认证测试 <!-- data-skill:authentication-testing --> | [`authentication-testing`](skills/zh/testing-types/authentication-testing/) | 审查身份凭证、生命周期和认证失败证据。 |
| 授权测试 <!-- data-skill:authorization-testing --> | [`authorization-testing`](skills/zh/testing-types/authorization-testing/) | 审查主体、资源、动作和权限边界决策。 |
| 会话安全测试 <!-- data-skill:session-security-testing --> | [`session-security-testing`](skills/zh/testing-types/session-security-testing/) | 审查会话生命周期、固定、过期和撤销风险。 |
| API 安全测试 <!-- data-skill:api-security-testing --> | [`api-security-testing`](skills/zh/testing-types/api-security-testing/) | 审查 API 攻击面和安全契约边界。 |
| 安全需求审查 <!-- data-skill:security-requirement-review --> | [`security-requirement-review`](skills/zh/testing-types/security-requirement-review/) | 审查安全需求的可追踪性和可测试性。 |
| 威胁建模 <!-- data-skill:threat-modeling --> | [`threat-modeling`](skills/zh/testing-types/threat-modeling/) | 建立资产、信任边界、威胁和缓解模型。 |
| 敏感信息暴露审查 <!-- data-skill:secrets-exposure-review --> | [`secrets-exposure-review`](skills/zh/testing-types/secrets-exposure-review/) | 审查敏感信息位置、生命周期和暴露证据。 |

##### 质量工程与效能

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 质量门禁设计 <!-- data-skill:quality-gate-design --> | [`quality-gate-design`](skills/zh/testing-types/quality-gate-design/) | 定义有证据的通过、阻塞、升级和例外规则 |
| 质量指标设计 <!-- data-skill:quality-metrics-design --> | [`quality-metrics-design`](skills/zh/testing-types/quality-metrics-design/) | 定义指标、分子分母、数据源、时效和解释边界 |
| 质量仪表盘设计 <!-- data-skill:quality-dashboard-design --> | [`quality-dashboard-design`](skills/zh/testing-types/quality-dashboard-design/) | 设计决策问题、面板、钻取、刷新和告警语义 |
| 质量债务分析 <!-- data-skill:quality-debt-analysis --> | [`quality-debt-analysis`](skills/zh/testing-types/quality-debt-analysis/) | 盘点质量债务来源、影响、年龄、所有人和偿还权衡 |
| 质量成熟度评估 <!-- data-skill:quality-maturity-assessment --> | [`quality-maturity-assessment`](skills/zh/testing-types/quality-maturity-assessment/) | 用证据锚点评估质量实践成熟度和改进缺口 |
| 测试有效性分析 <!-- data-skill:test-effectiveness-analysis --> | [`test-effectiveness-analysis`](skills/zh/testing-types/test-effectiveness-analysis/) | 分析测试信号、风险覆盖、漏检限制和验证计划 |
| 自动化投资回报分析 <!-- data-skill:automation-roi-analysis --> | [`automation-roi-analysis`](skills/zh/testing-types/automation-roi-analysis/) | 比较自动化建设、运行、维护成本与收益假设 |
| 测试瓶颈分析 <!-- data-skill:testing-bottleneck-analysis --> | [`testing-bottleneck-analysis`](skills/zh/testing-types/testing-bottleneck-analysis/) | 定位测试等待、依赖、容量、交接和约束证据 |
| 回归优化 <!-- data-skill:regression-optimization --> | [`regression-optimization`](skills/zh/testing-types/regression-optimization/) | 在风险、反馈时间、并行、缓存和维护之间优化回归范围 |
| CI 测试优化 <!-- data-skill:ci-test-optimization --> | [`ci-test-optimization`](skills/zh/testing-types/ci-test-optimization/) | 优化 CI 阶段、反馈、波动、资源、缓存和分片 |
| 测试运行时间优化 <!-- data-skill:test-runtime-optimization --> | [`test-runtime-optimization`](skills/zh/testing-types/test-runtime-optimization/) | 基于剖析和基线优化慢测试、初始化、清理、并行和隔离 |
| 测试维护成本分析 <!-- data-skill:test-maintenance-cost-analysis --> | [`test-maintenance-cost-analysis`](skills/zh/testing-types/test-maintenance-cost-analysis/) | 分析变更频率、修复工时、波动成本、所有权和可维护性 |
| 质量生产力指标 <!-- data-skill:quality-productivity-metrics --> | [`quality-productivity-metrics`](skills/zh/testing-types/quality-productivity-metrics/) | 定义质量与交付生产力指标并保留归因和操纵边界 |

##### 开发与持续集成

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 代码审查 <!-- data-skill:code-review --> | [`code-review`](skills/zh/testing-types/code-review/) | 对 PR 或 Diff 进行风险驱动的代码审查，输出 P0/P1/P2 问题与可执行修复建议。 |
| 变更影响分析 <!-- data-skill:change-impact-analysis --> | [`change-impact-analysis`](skills/zh/testing-types/change-impact-analysis/) | 分析变更的质量影响范围与风险 |
| PR 测试影响分析 <!-- data-skill:pr-test-impact-analysis --> | [`pr-test-impact-analysis`](skills/zh/testing-types/pr-test-impact-analysis/) | 从 PR 或 Diff 分析测试影响 |
| API 契约测试 <!-- data-skill:api-contract-testing --> | [`api-contract-testing`](skills/zh/testing-types/api-contract-testing/) | 验证 API 契约兼容性与变更风险 |
| 自动化测试 <!-- data-skill:automation-testing --> | [`automation-testing`](skills/zh/testing-types/automation-testing/) | 使用 POM、数据驱动或 BDD 等模式设计自动化测试方案。 |
| API Schema 校验 <!-- data-skill:api-schema-validation --> | [`api-schema-validation`](skills/zh/testing-types/api-schema-validation/) | 将 API Schema 与请求、响应和版本证据进行可追溯比对。 |
| API 负向测试 <!-- data-skill:api-negative-testing --> | [`api-negative-testing`](skills/zh/testing-types/api-negative-testing/) | 从契约和错误证据设计非法输入、拒绝与降级候选。 |
| API 幂等性测试 <!-- data-skill:api-idempotency-testing --> | [`api-idempotency-testing`](skills/zh/testing-types/api-idempotency-testing/) | 围绕重复请求、重试、幂等键和副作用设计验证候选。 |
| API 分页测试 <!-- data-skill:api-pagination-testing --> | [`api-pagination-testing`](skills/zh/testing-types/api-pagination-testing/) | 根据分页、排序和数据集证据识别边界、连续性和一致性风险。 |
| API 限流测试 <!-- data-skill:api-rate-limit-testing --> | [`api-rate-limit-testing`](skills/zh/testing-types/api-rate-limit-testing/) | 根据配额、窗口、突发和恢复证据设计限流候选。 |
| API 版本兼容性测试 <!-- data-skill:api-version-compatibility-testing --> | [`api-version-compatibility-testing`](skills/zh/testing-types/api-version-compatibility-testing/) | 从版本契约、旧客户端和弃用证据评估兼容性风险。 |
| API 错误契约测试 <!-- data-skill:api-error-contract-testing --> | [`api-error-contract-testing`](skills/zh/testing-types/api-error-contract-testing/) | 评审错误状态码、错误码、字段结构和脱敏行为的一致性。 |

##### 测试数据与自动化实现

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 测试数据需求分析 <!-- data-skill:test-data-requirement-analysis --> | [`test-data-requirement-analysis`](skills/zh/testing-types/test-data-requirement-analysis/) | 在测试设计或数据生成前分析实体、关系、隐私、生命周期、初始化、清理和阻塞项 |
| 测试数据生成 <!-- data-skill:test-data-generation --> | [`test-data-generation`](skills/zh/testing-types/test-data-generation/) | 设计安全且具代表性的测试数据 |
| Bruno 接口自动化 <!-- data-skill:api-test-bruno --> | [`api-test-bruno`](skills/zh/testing-types/api-test-bruno/) | 解析多格式 API 定义，生成可执行回归的 Bruno 集合。 |
| Postman API 测试 <!-- data-skill:api-test-postman --> | [`api-test-postman`](skills/zh/testing-types/api-test-postman/) | 设计 Postman 集合、环境、脚本和可用 Newman 执行的 API 回归方案。 |
| Pytest 接口自动化 <!-- data-skill:api-test-pytest --> | [`api-test-pytest`](skills/zh/testing-types/api-test-pytest/) | 解析多格式 API 定义并生成 Pytest 接口自动化方案。 |
| RestAssured 接口自动化 <!-- data-skill:api-test-restassure --> | [`api-test-restassure`](skills/zh/testing-types/api-test-restassure/) | 解析多格式 API 定义并生成 Rest Assured Java 测试类。 |
| Supertest 接口自动化 <!-- data-skill:api-test-supertest --> | [`api-test-supertest`](skills/zh/testing-types/api-test-supertest/) | 解析多格式 API 定义并生成可执行的 Supertest 脚本。 |
| Selenium UI 自动化测试 <!-- data-skill:ui-test-selenium --> | [`ui-test-selenium`](skills/zh/testing-types/ui-test-selenium/) | 设计 Selenium WebDriver UI 自动化方案，覆盖稳定定位、等待、Page Object、Grid 和 CI 执行。 |
| Playwright UI 自动化测试 <!-- data-skill:ui-test-playwright --> | [`ui-test-playwright`](skills/zh/testing-types/ui-test-playwright/) | 设计 Playwright Test 套件，覆盖 fixtures、projects、trace、截图、API+UI 组合和 CI 报告。 |
| TestCafe UI 自动化测试 <!-- data-skill:ui-test-testcafe --> | [`ui-test-testcafe`](skills/zh/testing-types/ui-test-testcafe/) | 设计 TestCafe UI 自动化方案，覆盖 fixture、selector、role、浏览器矩阵和报告。 |
| Cypress UI 自动化测试 <!-- data-skill:ui-test-cypress --> | [`ui-test-cypress`](skills/zh/testing-types/ui-test-cypress/) | 设计 Cypress e2e 与组件测试方案，覆盖 commands、fixtures、网络桩和 CI 报告。 |
| Puppeteer UI 自动化测试 <!-- data-skill:ui-test-puppeteer --> | [`ui-test-puppeteer`](skills/zh/testing-types/ui-test-puppeteer/) | 设计 Puppeteer 自动化方案，覆盖 Chromium 检查、截图、PDF、网络拦截和 CDP 场景。 |
| WebdriverIO UI 自动化测试 <!-- data-skill:ui-test-webdriverio --> | [`ui-test-webdriverio`](skills/zh/testing-types/ui-test-webdriverio/) | 设计 WebdriverIO 套件，覆盖配置、services、runner、Page Object、capabilities 和 reporters。 |
| UI 测试策略 <!-- data-skill:ui-test-strategy --> | [`ui-test-strategy`](skills/zh/testing-types/ui-test-strategy/) | 从用户旅程、界面状态、平台差异和风险证据形成 UI 测试策略。 |
| UI 测试选择器评审 <!-- data-skill:ui-test-selector-review --> | [`ui-test-selector-review`](skills/zh/testing-types/ui-test-selector-review/) | 基于 DOM、组件语义和测试代码评审选择器稳定性与可维护性。 |
| UI 测试等待策略评审 <!-- data-skill:ui-test-wait-strategy-review --> | [`ui-test-wait-strategy-review`](skills/zh/testing-types/ui-test-wait-strategy-review/) | 从异步状态和可观察条件评审等待、轮询与超时策略。 |
| 视觉回归测试 <!-- data-skill:visual-regression-testing --> | [`visual-regression-testing`](skills/zh/testing-types/visual-regression-testing/) | 围绕基线、视口、字体、数据和差异阈值设计视觉回归候选。 |
| 跨浏览器测试 <!-- data-skill:cross-browser-testing --> | [`cross-browser-testing`](skills/zh/testing-types/cross-browser-testing/) | 根据用户分布、引擎、版本、设备和缺陷证据选择兼容性覆盖。 |

##### 测试执行与回归智能

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 不稳定测试分析 <!-- data-skill:flaky-test-analysis --> | [`flaky-test-analysis`](skills/zh/testing-types/flaky-test-analysis/) | 从运行证据分析间歇性测试失败 |
| 回归范围分析 <!-- data-skill:regression-scope-analysis --> | [`regression-scope-analysis`](skills/zh/testing-types/regression-scope-analysis/) | 按风险定义回归范围和排除依据 |
| 回归测试选择 <!-- data-skill:regression-test-selection --> | [`regression-test-selection`](skills/zh/testing-types/regression-test-selection/) | 从测试资产选择最小风险覆盖回归集 |
| AI 辅助测试 <!-- data-skill:ai-assisted-testing --> | [`ai-assisted-testing`](skills/zh/testing-types/ai-assisted-testing/) | 使用 AI 辅助测试数据生成、根因分析和优先级判断等工作。 |
| AI 生成测试评审 <!-- data-skill:ai-generated-test-review --> | [`ai-generated-test-review`](skills/zh/testing-types/ai-generated-test-review/) | 审查 AI 生成测试是否具备真实回归保护，识别伪测试、弱断言和缺失业务结果。 |
| 测试代码评审 <!-- data-skill:test-code-review --> | [`test-code-review`](skills/zh/testing-types/test-code-review/) | 基于测试代码和运行证据识别断言、隔离、夹具、确定性和维护风险。 |
| 变异测试分析 <!-- data-skill:mutation-testing-analysis --> | [`mutation-testing-analysis`](skills/zh/testing-types/mutation-testing-analysis/) | 根据变异算子和存活结果分析测试敏感性，不虚构质量分数。 |
| Mock 质量评审 <!-- data-skill:mock-quality-review --> | [`mock-quality-review`](skills/zh/testing-types/mock-quality-review/) | 评审 mock 的契约一致性、逼真度、过度模拟和漂移风险。 |
| 测试套件健康度分析 <!-- data-skill:test-suite-health-analysis --> | [`test-suite-health-analysis`](skills/zh/testing-types/test-suite-health-analysis/) | 基于耗时、波动、重复、隔离和维护证据评估测试套件健康度。 |

##### 性能工程与容量决策

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| 性能测试 <!-- data-skill:performance-testing --> | [`performance-testing`](skills/zh/testing-types/performance-testing/) | 面向负载、压力、突发、耐久或容量目标设计性能测试。 |
| k6 性能测试 <!-- data-skill:performance-test-k6 --> | [`performance-test-k6`](skills/zh/testing-types/performance-test-k6/) | 规划 k6 的负载、压力、突发或浸泡测试范围、脚本与执行入口。 |
| Gatling 性能测试 <!-- data-skill:performance-test-gatling --> | [`performance-test-gatling`](skills/zh/testing-types/performance-test-gatling/) | 规划 Gatling 性能测试范围、模拟场景和可执行入口。 |
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
| RAG 质量测试 <!-- data-skill:rag-quality-testing --> | [`rag-quality-testing`](skills/zh/testing-types/rag-quality-testing/) | 测试 grounding、相关性、完整性、引用支持和拒答证据 |
| RAG 检索测试 <!-- data-skill:rag-retrieval-testing --> | [`rag-retrieval-testing`](skills/zh/testing-types/rag-retrieval-testing/) | 分析查询变体、分块、过滤、排序、新鲜度和检索证据 |
| LLM 幻觉测试 <!-- data-skill:llm-hallucination-testing --> | [`llm-hallucination-testing`](skills/zh/testing-types/llm-hallucination-testing/) | 按声明和来源证据识别无支持断言并评估拒答 |
| LLM 一致性测试 <!-- data-skill:llm-consistency-testing --> | [`llm-consistency-testing`](skills/zh/testing-types/llm-consistency-testing/) | 比较重复输入、版本因素、不变量和输出方差 |

> `prompt-regression-testing` 是 `prompt-testing` 内名为 `prompt-regression` 的增强模式，不创建别名目录。

##### Agent、工具与安全测试

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| AI Agent 测试 <!-- data-skill:ai-agent-testing --> | [`ai-agent-testing`](skills/zh/testing-types/ai-agent-testing/) | 测试 AI Agent 的目标、状态、恢复和安全边界 |
| Agent 工具调用测试 <!-- data-skill:agent-tool-testing --> | [`agent-tool-testing`](skills/zh/testing-types/agent-tool-testing/) | 验证 Agent 工具调用契约、授权和副作用边界 |
| Prompt Injection 测试 <!-- data-skill:prompt-injection-testing --> | [`prompt-injection-testing`](skills/zh/testing-types/prompt-injection-testing/) | 设计 AI 系统 Prompt 注入防护测试 |
| Agent 循环测试 <!-- data-skill:agent-loop-testing --> | [`agent-loop-testing`](skills/zh/testing-types/agent-loop-testing/) | 测试规划-动作-观察循环、停止条件、预算和重复行为 |
| Agent 记忆测试 <!-- data-skill:agent-memory-testing --> | [`agent-memory-testing`](skills/zh/testing-types/agent-memory-testing/) | 测试记忆读写、更新删除、保留、隔离、来源和遗忘 |
| Agent 权限测试 <!-- data-skill:agent-permission-testing --> | [`agent-permission-testing`](skills/zh/testing-types/agent-permission-testing/) | 验证身份、工具资源范围、批准拒绝和副作用边界 |
| Agent 故障恢复测试 <!-- data-skill:agent-failure-recovery-testing --> | [`agent-failure-recovery-testing`](skills/zh/testing-types/agent-failure-recovery-testing/) | 分析故障分类、重试回退、升级、状态一致性和用户通知 |
| 长运行 Agent 测试 <!-- data-skill:agent-long-running-testing --> | [`agent-long-running-testing`](skills/zh/testing-types/agent-long-running-testing/) | 测试检查点、心跳、恢复取消、重复提交、超时和资源生命周期 |
| 多 Agent 测试 <!-- data-skill:multi-agent-testing --> | [`multi-agent-testing`](skills/zh/testing-types/multi-agent-testing/) | 分析委派、协调、共享状态、冲突、所有权和终止 |
| AI 安全测试 <!-- data-skill:ai-safety-testing --> | [`ai-safety-testing`](skills/zh/testing-types/ai-safety-testing/) | 审查安全政策、滥用、拒答重定向、隐私和升级边界 |

### Skill Engineering（横向治理）

| 名称 | 目录 | 主要用途 |
| --- | --- | --- |
| Skill 变更验证 | [`skill-change-verification`](skills/zh/skill-engineering/skill-change-verification/) | 按变更范围选择验证证据，并区分静态、评测和运行时结论。 |
| Skill 质量审查 | [`skill-quality-review`](skills/zh/skill-engineering/skill-quality-review/) | 审查完整 Skill 包的工程契约、独立安装、双语一致性和 Eval 准备度。 |
| Skill 评测 | [`skill-evaluation`](skills/zh/skill-engineering/skill-evaluation/) | 设计、运行、解释和报告 evidence-bounded Skill 评测。 |
| Skill 文案契约审查 | [`skill-prose-review`](skills/zh/skill-engineering/skill-prose-review/) | 审查 Skill、Prompt 与文档的可执行契约、边界和证据要求。 |
| 过程性文案清理 | [`skill-prose-trim`](skills/zh/skill-engineering/skill-prose-trim/) | 清理文案中的审查和设计过程残留，同时保留当前状态契约。 |

Skill Engineering 服务所有能力层，不改变产品能力分类。英文 Skill 使用相同目录名；可从页面顶部切换语言。

## 支持的 AI 工具

这些工具有对应的一键安装器；也可以按[安装说明](scripts/INSTALL_SKILLS.md)使用 `npx skills` 或手动复制。

| 工具 | 默认安装目标 | 支持方式 |
| --- | --- | --- |
| Codex | `~/.codex/skills/` | 一键脚本、`npx skills`、手动复制 |
| Cursor | `~/.cursor/skills/` | 一键脚本、`npx skills`、手动复制 |
| Claude Code | `~/.claude/skills/` | 一键脚本、`npx skills`、手动复制 |
| Kiro | `~/.kiro/skills/` | 一键脚本、手动复制 |
| OpenCode | `~/.opencode/skills/` | 一键脚本、手动复制 |
| Trae | `~/.trae/skills/` | 一键脚本、手动复制 |

Skill 目录遵循 Agent Skills 约定。其他兼容工具可以参考其 Skill 目录要求，直接复制对应语言目录或单个 Skill。

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

需要对 `codex exec --json` 运行结果做本地确定性检测时，使用 [Skill 本地评测规则](docs/SKILL_EVAL_RULES.md)、`scripts/run_skill_trace_eval.py` 和 `scripts/grade_skill_trace.py`；它会把缺失证据标记为 `BLOCKED`，不会替代模型辅助的语义评分。

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
| [skills-composition.md](docs/catalog/skills-composition.md) | v1.5.2 五条结构化路由、主/辅 Skill 和导航关系 |
| [QA_SKILLS_EVOLUTION_ROADMAP.md](docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md) | 四层能力演进与研发测试阶段地图 |
| [DOCUMENTATION_POLICY.md](docs/governance/DOCUMENTATION_POLICY.md) | 中文优先的双语文档治理策略 |
| [SKILL_GOVERNANCE_V1.md](docs/governance/SKILL_GOVERNANCE_V1.md) | v1.0 源代码治理基线与当前 164 对静态记录入口（早期基线 79 对；不代表运行质量） |
| [PHASE_0_V1_4_CLOSEOUT.md](docs/governance/PHASE_0_V1_4_CLOSEOUT.md) | v1.4 35 张 Project 卡的证据收口与版本边界（不代表发布批准） |
| [BILINGUAL_CONSISTENCY_CONTRACT.md](docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md) | 中英文路径、入口、Catalog 与链接一致性契约 |
| [QUALITY_SCORE_EVAL_CONTRACT.md](docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md) | 九维评分与最低 Eval 工件标准 |
| [WORKFLOW_EVAL_INSTALL_SYNC.md](docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md) | 10 个 Workflow 的双语、Eval 与安装入口同步清单 |
| [PHASE_1_REQUIREMENTS_QUALITY.md](docs/governance/PHASE_1_REQUIREMENTS_QUALITY.md) | v1.1 Phase 1 前五个需求质量 Skill 的范围、卡片、证据和验收边界 |
| [SKILL_EVAL_RULES.md](docs/SKILL_EVAL_RULES.md) | `codex exec --json` trace 的 20 条本地确定性 Skill 评测规则 |
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
