<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-10-16-ai-native-qa-development-landscape_EN.md">🇬🇧 English</a></div>

# GitHub 项目迭代方向与 AI Native QA 扩展空间

**调研日期：2026-10-16**

**范围：** 对照高关注度的 AI 开发工作流、Skill 目录、测试自动化与 LLM Eval 项目，并结合本仓库现有能力评估可行的扩展方向。

本报告记录截至 2026-10-16 的一次性调研，不构成长期规范。按当前双语文档策略，仍提供英文镜像；后续变化以更新日期更晚的评审记录为准。

## 结论摘要

本项目当前不缺 Skill 数量或 QA 生命周期覆盖面。README 记录每种语言 165 个 Skill、中英文合计 330 个目录，覆盖 Core QA、Engineering QA、Production Quality 和 AI Native QA；演进路线图中的 29 项扩展也已标记完成。[README](../../README.md#能力分层) [演进路线图](../governance/QA_SKILLS_EVOLUTION_ROADMAP.md)

下一阶段的主要缺口是把既有 Skill 从“可发现、可安装、可单独使用”推进到“能在一个真实研发任务中接力工作，并交付可复核的运行证据”。本仓库的 Composition 当前是导航元数据，不能视作强制执行链；路由治理记录也明确将自动目标执行和真实项目验证列为尚未完成的证据边界。[评测契约](../governance/SKILL_EVALUATION_CONTRACT.md#L60) [Skill 治理路线图](../governance/SKILL_GOVERNANCE_ROADMAP.md#L40-L42)

建议把项目定位为：**服务 AI 辅助软件交付的 AI Native Quality Engineering 工作流系统**。核心承诺是从需求、PR/Diff 或 AI 功能变更出发，形成测试决策、可选执行、证据包和风险结论。可以扩展到 AI Native Development，但应扩展“研发流程里的质量控制点”，而不是变成通用代码生成 Skill 集合。

## 调研方法与限制

- 选择了 GitHub 上星数较高的工程工作流、Skill 生态、测试与 LLM Eval 项目，以及一个直接 QA Skills 对照项目。
- 星数按 2026-10-16 的 GitHub 页面/API 快照取近似值并四舍五入；星数代表关注度，不代表质量、使用量或效果。
- 主要查看各项目 README、官方文档和近期提交方向；未运行或独立验证这些项目的功能。
- 这是一个代表性样本，不足以据此断言整个 QA Skills 市场的规模。

## 项目对照

| 项目 | 星数快照 | 可观察到的迭代方向 | 对本项目的启发 |
| --- | ---: | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | 约 300k | 把开发过程组织成明确阶段：构思、计划、分步实现、TDD、审查和收尾；近期迭代仍在改善核心流程、跨工具支持和可靠性。 | 大型 Skill 项目的价值不只在目录规模，更在流程能否约束任务如何前进。可借鉴阶段契约和交付物，避免扩成通用开发助手。 |
| [anthropics/skills](https://github.com/anthropics/skills) | 约 181k | 提供官方 Skill 示例、模板与开发材料；项目明确偏向示例和教育用途。 | 入口简单、示例易复制有助于生态传播；本项目的差异应继续放在 QA 领域深度、双语和证据治理。 |
| [github/spec-kit](https://github.com/github/spec-kit) | 约 141k | 将 Spec-Driven Development 做成可选流程，并提供扩展、预设和组合方式；近期持续完善评测契约、产物捕获与 Agent 命令集成。 | 提供按结果选择的工作流包，比只增加 Skill 清单更容易让研发团队开始使用。 |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 约 97.8k | 官方文档展示 Planner、Generator、Healer 等测试 Agent：探索应用、生成测试、实际验证选择器和断言、执行并处理失败。 | 让中间产物和执行结果可审查；自愈不能把跳过测试或“看起来通过”当成绿色结果。 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 约 40.1k | 社区贡献的 Skills、Agent、指令、Hooks 和插件，加上可搜索站点、学习入口与安装发现路径；近期提交主要维护社区目录。 | 发现、筛选和首次使用体验是独立的产品能力。可以按常见任务提供少量精选入口和演示，而不是只展示总数。 |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 约 25.5k | 用“构思—计划—构建—简化—审查—沉淀经验”的循环，让一次任务的学习服务于下一次任务；近期改进多模型协作与流程可靠性。 | 可以把复盘沉淀为可复用的测试资产、缺陷模式和 Eval 案例，但必须有证据来源和人工复核。 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 约 26k | 面向 LLM 应用的 Eval、红队测试、模型对比和 CI/CD 集成。 | 不需要在 Skill 仓库里重造通用评测执行器；可提供配置生成、用例设计、结果解释等可选适配。 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 约 18.9k | 提供 LLM Eval 框架，覆盖 Agent 轨迹、工具调用、检索和合成数据；配套 Skill 引导生成可重复运行的 pytest Eval 套件并分析 trace。 | Skill 可以帮助用户把一次性分析转成已提交、可回归的质量资产，这比只生成建议更有长期价值。 |
| [openqa-cn/codexqa](https://github.com/openqa-cn/codexqa) | 约 180 | 更贴近 QA Skills：项目 README 描述本地优先的 Router/Worker Skills、执行器、证据收集和报告产物；近期迭代强调可见的浏览器证据和减少误报。 | 这是值得观察的直接对照：聚焦少数实际执行路径可以形成“立即可用”的体验。本项目可保留更广的双语目录和治理优势，同时选择一个端到端场景做深。 |
| [naodeng/awesome-qa-skills](https://github.com/naodeng/awesome-qa-skills) | 约 260 | 双语、跨工具的 QA Skill 目录，README 记录每种语言 165 个 Skill，并覆盖需求到生产及 AI Native QA；治理强调独立安装、Eval 与证据边界。 | 规模和覆盖已形成基础差异化。下一阶段更该把少数现有能力连接成可验证的任务闭环，并用真实项目证据验证价值。 |

总体上，星数较高的相邻项目集中在**开发流程、工具生态、测试执行或模型评测**。专门定位为 QA Skills 的仓库在这组样本中规模较小；这说明本项目需要清晰连接到研发工作流，但不能据此推断 QA 需求本身较小。

## 本项目的优势与卡点

### 已有优势

- 覆盖需求、设计、测试、发布、生产和 AI 功能验证，且中英文维护、Skill 可独立安装。
- Skill 元数据、Eval 用例、仓库质量门禁与证据状态已经形成一套治理底座。
- 已有变更影响、回归范围、回归测试选择、Playwright、测试报告、发布工作流及 AI/LLM/Agent 测试相关能力，可以作为纵向工作流的现成积木。[README 能力目录](../../README.md#完整技能目录) [演进路线图](../governance/QA_SKILLS_EVOLUTION_ROADMAP.md)

### 主要卡点

- 能力地图和 Skill 目录的“库存”已相当丰富，继续加相似 Skill 的边际收益可能较低。
- 现有工作流组合更接近路由和导航，还没有普遍形成“输入 → 选择 → 执行 → 证据 → 结论”的可运行链路。
- 真实目标执行、跨模型/工具表现、真实项目回归和用户侧结果仍需要单独建立证据，不能从结构检查或 Eval 配置推断。[Skill 治理路线图](../governance/SKILL_GOVERNANCE_ROADMAP.md#L40-L42)
- 仓库文档有一处目录数快照差异：README 记录每种语言 165 个，演进路线图正文仍记录 164 个；后续更新路线图时应先核对生成器和当前目录。

这意味着停滞感更可能来自**从目录型项目转向工作流产品**的阶段切换，而不是需要再找一批 Skill 名称。

## 四类工作流的具体结构

这不是四个互不相干的新 Skill，而是四个入口复用同一条交付骨架：

```text
输入与版本确认 → 风险分析 → 可验收条件 → 测试设计/生成 → 实际执行 → 失败分流 → 证据包 → 结论与下一步
```

每一阶段都要输出结构化交接。下游不能只收到一段总结，还要知道它基于哪个需求/缺陷、哪个 commit、哪些假设和哪些证据。信息不足可以继续做不受影响的部分，但受影响的结论必须标为 `BLOCKED`、`NOT_RUN` 或 `INSUFFICIENT_EVIDENCE`，这些状态不能当成通过。

| 工作流入口 | 输入 | 阶段串接与现有 Skill | 完成条件与阻断规则 |
| --- | --- | --- | --- |
| **新功能交付** `new-feature-quality` | Issue/PRD、设计稿/API 契约、代码 PR、目标环境和现有测试 | `requirements-analysis` → `quality-risk-analysis` / `testability-analysis` → `acceptance-criteria-review` → `test-strategy` / `test-case-writing` → API/UI/功能测试 → `test-reporting` | 每条关键验收条件能映射到一个或多个测试及可观察证据。业务规则未确认时先交问题清单，不自行补规则；没有实现或环境时只交测试准备结果并标 `NOT_RUN`。 |
| **Bugfix 验证** `bugfix-verification`（建议新增组合路由） | 缺陷单、复现步骤、期望/实际、日志、修复 PR、基线与目标 commit | 复现审计 → `root-cause-analysis`（只形成假设）/`change-impact-analysis` → `acceptance-criteria-review` → `test-case-writing`（先固化复现用例）→ `regression-test-selection` → 相关测试执行 → `test-reporting` | 理想证据是复现用例在修复前失败、修复后通过，并且相关回归通过。无法在基线复现时不能声称“已验证修复”；需要区分修复缺陷、复现测试缺陷、环境问题和未复现。 |
| **AI 生成代码验证** `ai-code-verification`（建议新增组合路由） | 研发任务与验收条件、AI 生成的代码/测试 diff、目标 commit；若可用，附 Agent/模型/工具版本和执行 trace | `code-review` / `change-impact-analysis` → `acceptance-criteria-review` → 相关测试设计与生成 → `ai-generated-test-review` 检查断言是否能捕获真实缺陷 → 测试执行 → 结果报告 | 先验证生成的实现是否符合验收条件，再验证测试是否真的能保护该行为。仅有覆盖率或全绿结果不够；若测试会在关键实现被破坏后仍通过，应判为证据不足或测试失败。缺少生成来源信息可保留 `unknown`，不能猜。 |
| **发布准备** `release-readiness` | RC/tag、PR/commit 清单、CI/build、环境、已知缺陷、部署与回滚方案 | `release-testing-workflow` → 按变更做 `regression-test-selection` → 安全/性能/API/AI Eval 等专项执行 → `production-verification`（适用时）→ `test-reporting` | 产出带证据链接的门禁看板、未完成项、残余风险和 Go/No-Go 建议。关键门禁缺证据标 `BLOCKED`/`NOT_RUN`；正式放行仍由授权人员决定，Skill 只给有依据的建议。 |

这里有两个容易混淆的范围：仓库现有 `ai-feature-validation` 检验产品里的 AI 功能；`ai-code-verification` 检验编码 Agent 生成的代码和测试。前者不能替代后者。当前 Composition 已有 `new-feature-quality`、`change-regression`、`ai-feature-validation` 等导航路线，但路由本身不执行测试；发布也已有 [release-testing-workflow](../../skills/zh/testing-workflows/release-testing-workflow/SKILL.md)，需要连接执行和统一证据，而不是重写发布 Skill。

### 失败分流和最终证据

测试失败不能直接等同于产品缺陷。每个失败至少归到以下一类，并保留原始证据：

- **产品行为失败：** 可重复地违反已确认验收条件，状态 `FAIL`，关联具体用例、版本和实际/预期差异。
- **测试问题：** 测试断言、数据、隔离或清理有问题；修正后重跑，但保留首轮失败记录。
- **不稳定测试：** 限定重试次数，保留首次结果和重试结果；不能因某次重试通过就隐藏 flaky。
- **环境/权限/依赖问题：** 没有足够执行证据时是 `BLOCKED` 或 `NOT_RUN`，不能标绿。
- **需求或验收歧义：** 受影响的测试结论 `BLOCKED`；不受影响的测试仍可继续。

一次工作流的最小证据包可以包含：`run_id`、场景、输入工单/PR、基线与目标 SHA、验收条件 ID、选中的测试及选择理由、测试命令与环境、原始日志/报告路径、每个断言的证据状态、失败分类、未覆盖风险、建议结论和下一步负责人。报告要区分“测试断言通过”和“允许发布”，两者不是同一决定。

**Bugfix 例子：** 缺陷单声称“重复提交订单会重复扣库存”。工作流先确认这是已批准的库存契约，并固定一个可重复的复现输入；基线版本运行失败后，修复版本应运行同一用例并通过，再执行受影响库存/订单回归。若基线用例并未失败，结论是“复现未建立”；若修复版本测试因数据库服务未启动而未执行，状态为 `BLOCKED`；只有复现、修复与回归证据都齐全，才可说“本次验证的版本通过了这些断言”。

## 建议的扩展路线

### P0：先做一条旗舰级 QA 交付闭环

优先从已有资产出发，做 **PR/Diff → 变更风险分析 → 回归范围与测试集建议 → 可选测试执行 → 证据包与结论**。这是 QA 与研发最自然的交汇点，也复用了现有 `change-impact-analysis`、`regression-scope-analysis`、`regression-test-selection`、`ui-test-playwright` 和 `test-reporting` 等能力。

工作流至少应交付一个机器可读、可复核的 handoff/evidence manifest，例如包含：`workflow_id`、代码版本或 PR、阶段、选择的 Skills/测试、执行状态、证据路径、未覆盖风险、未决问题、下一步和退出条件。没有执行证据时，状态应为 `NOT_RUN`、`BLOCKED` 或其他明确状态，不能给出“回归通过”的结论。

第一版不必实现通用编排平台。可以先用一个可复制的工作流定义和可选 Runner/CI 适配，在示例仓库里完成闭环。至少用 `known-good`、`known-bad`、`known-ambiguous` 三类端到端样例，分别检查正常证据、真实缺陷和证据不足时是否会产生错误绿灯。

### P1：把 AI Native QA 从“测试设计”推进到“持续 Eval”

围绕真实 AI 功能形成可回归的 Eval 资产：数据集版本、Prompt/模型/Agent 版本、工具轨迹、指标与断言、人工复核项、红队用例、CI 质量门禁和版本对比。为 promptfoo、DeepEval 等成熟执行工具提供可选配置或工作流适配，Skill 负责设计输入、声明证据要求、解释结果和定位风险，不替代专用 Runner。

### P2：扩展到 AI Native Development 的质量控制点

面向研发同学补充或强化这些能力：需求和 Spec 的可测试性、编码 Agent 任务的验收条件、代码变更的测试影响、生成测试的质量审查、Bug 修复后的回归验证、PR/发布证据摘要。每个能力都应回答“怎样证明改动符合预期”，而不是泛化为“替用户写更多代码”。

### P3：优化首次使用和分发

围绕结果提供 3–5 个精选路径，例如“评审一个 PR”“上线一个 AI 功能”“排查不稳定测试”“准备发布”。每条路径附真实示例仓库、安装指引、预期产物和失败时的处理方式。按用户任务组织 Skill Bundles 和网站入口，降低从 330 个目录中自行挑选的成本。

## 如何判断迭代有效

建议以真实任务和版本回归为单位观察：

1. 缺陷发现率、误报率、漏报率，以及证据不足时能否正确阻断。
2. 从输入变更到形成可信质量判断所需时间，以及人工补充工作量。
3. 执行证据完整度、结果可复现性、跨 Agent/Runner 的可移植性。
4. Skill 更新前后的行为差异，以及真实用户能否完成首次任务。

星数、目录数、静态检查通过、一次 Eval 分数或一次本地运行都不能单独证明实际质量收益；应按对应证据类型报告结果。[Skill Eval 状态契约](../governance/SKILL_EVALUATION_CONTRACT.md#evidence-state)

## 近期决策建议

1. 暂缓扩大通用 Skill 数量，先选 **Bugfix 验证** 作为最小纵向切片：缺陷输入、基线复现、修复后验证和回归证据更容易形成可复核的闭环；稳定后再扩展到任意 PR/Diff 的变更回归。
2. 先定义工作流输入、交接数据、证据包和退出条件，再决定要不要写 Runner 或 CI 集成。
3. AI Native Development 以“开发过程中的质量保障”为边界，不扩成通用编码 Agent 或大型多 Agent 编排平台。
4. 用 3 类真实项目用例验证工作流，再根据失败和使用反馈决定下一轮投入。

## 主要来源

- [obra/superpowers](https://github.com/obra/superpowers)
- [anthropics/skills](https://github.com/anthropics/skills)
- [github/spec-kit](https://github.com/github/spec-kit)
- [Playwright Test Agents](https://github.com/microsoft/playwright/blob/main/docs/src/test-agents-js.md)
- [github/awesome-copilot](https://github.com/github/awesome-copilot)
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [promptfoo](https://github.com/promptfoo/promptfoo)
- [DeepEval Skill](https://github.com/confident-ai/deepeval/blob/main/skills/deepeval/SKILL.md)
- [openqa-cn/codexqa](https://github.com/openqa-cn/codexqa)
