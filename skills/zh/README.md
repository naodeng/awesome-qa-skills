# 中文 Skills

语言根目录：`skills/zh`

本目录与 `skills/en` **同名对齐**：工作流 10 个 + 测试类型 44 个 + Skill Engineering 3 个。安装、约定与评测见仓库根 [README.md](../../README.md)、[AGENTS.md](../../AGENTS.md)、[skills/SKILL_AUTHORING.md](../SKILL_AUTHORING.md)。

## 能力导航

目录类别保持不变；以下阶段用于按质量目标查找 Skill：

| 阶段 | 可先选择的现有 Skill | 状态 |
| --- | --- | --- |
| Core QA Skills | `requirements-analysis`、`test-strategy`、`test-case-writing`、`functional-testing`、`test-reporting` | 已提供 |
| Engineering QA Skills | `code-review`、`automation-testing`、`performance-testing` | 已有基础，Shift Left、变更与诊断能力按路线图补齐 |
| Production Quality Skills | `release-testing-workflow`、`test-reporting` | 已有发布基础，生产能力按路线图补齐 |
| AI Native QA Skills | 暂无可安装的 Testing for AI 专项包 | 规划中；`ai-assisted-testing` 属于 AI for QA |

查看 [中文演进路线图](../../docs/QA_SKILLS_EVOLUTION_ROADMAP.md)；安装仍使用本页列出的实际目录。

## testing-workflows（工作流）

| 目录名 | 中文名称 | 说明 |
| --- | --- | --- |
| `daily-testing-workflow` | 日常测试工作流程 | 日常冒烟、缺陷跟进、当日计划 |
| `sprint-testing-workflow` | 迭代测试工作流程 | Sprint 规划、增量验收、迭代风险 |
| `release-testing-workflow` | 发布测试工作流程 | 发布门禁、回归范围、上线检查 |
| `discover-testing` | 测试技能路由 | 按目标推荐应调用的 skill |
| `product-quality-perspective` | 产品质量视角 | 分析用户价值、业务规则、范围、验收与发布风险 |
| `qa-quality-perspective` | QA 质量视角 | 评估可测试性、风险驱动覆盖、缺陷风险与证据边界 |
| `ux-quality-perspective` | UX 质量视角 | 识别信息架构、交互状态、一致性、响应式与无障碍风险 |
| `technical-quality-perspective` | 技术质量视角 | 基于架构、代码、安全、性能与可观测性证据分析技术质量 |
| `project-delivery-perspective` | 项目交付视角 | 记录带来源的交付约束和行动，不改变质量事实 |
| `multi-role-quality-synthesis` | 多角色质量汇总 | 汇总同阶段角色报告并保留来源、分歧和质量边界 |

## testing-types（测试类型）

### 核心执行

| 目录名 | 中文名称 |
| --- | --- |
| `functional-testing` | 功能测试 |
| `api-testing` | API 测试 |
| `automation-testing` | 自动化测试 |
| `manual-testing` | 手动/探索性测试 |
| `performance-testing` | 性能测试 |
| `security-testing` | 安全测试 |
| `mobile-testing` | 移动端测试 |
| `accessibility-testing` | 可访问性测试 |

### 过程与产出物

| 目录名 | 中文名称 |
| --- | --- |
| `requirements-analysis` | 需求分析 |
| `test-strategy` | 测试策略 |
| `test-strategy-review` | 测试策略评审 |
| `test-case-writing` | 测试用例编写 |
| `test-case-reviewer` | 测试用例评审 |
| `code-review` | 代码审查 |
| `bug-reporting` | 缺陷上报 |
| `test-reporting` | 测试报告 |
| `test-report-review` | 测试报告评审 |
| `ai-assisted-testing` | AI 辅助测试 |

### 工具专项

| 目录名 | 中文名称 |
| --- | --- |
| `api-test-bruno` | API 测试（Bruno） |
| `api-test-postman` | API 测试（Postman） |
| `api-test-pytest` | API 测试（Pytest） |
| `api-test-restassure` | API 测试（Rest Assured） |
| `api-test-supertest` | API 测试（Supertest） |
| `ui-test-selenium` | UI 自动化测试（Selenium） |
| `ui-test-playwright` | UI 自动化测试（Playwright） |
| `ui-test-testcafe` | UI 自动化测试（TestCafe） |
| `ui-test-cypress` | UI 自动化测试（Cypress） |
| `ui-test-puppeteer` | UI 自动化测试（Puppeteer） |
| `ui-test-webdriverio` | UI 自动化测试（WebdriverIO） |
| `performance-test-k6` | 性能测试（k6） |
| `performance-test-gatling` | 性能测试（Gatling） |
| `performance-test-jmeter` | 性能测试（JMeter） |

### 增强版（Plus）

| 目录名 | 中文名称 |
| --- | --- |
| `requirements-analysis-plus` | 需求分析增强版 |
| `test-strategy-plus` | 测试策略增强版 |
| `testcase-writer-plus` | 测试用例编写增强版 |
| `test-case-reviewer-plus` | 测试用例评审增强版 |

## skill-engineering（治理支撑）

| 目录名 | 中文名称 |
| --- | --- |
| `skill-change-verification` | Skill 变更验证 |
| `skill-prose-review` | Skill 文案评审 |
| `skill-prose-trim` | Skill 文案精简 |

这些 Skill 服务所有能力阶段，不构成第五阶段。

英文对照：[skills/en/README.md](../en/README.md) · 全量索引：[skills-index.md](../../skills-index.md)
