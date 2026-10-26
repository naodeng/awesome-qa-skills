<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-10-25-github-qa-skills-iteration-research_EN.md">🇬🇧 English</a></div>

# GitHub 相邻项目与 QA Skills 迭代方向调研

> 调研日期：2026-10-25
> 范围：GitHub 上与 Agent Skills 目录、AI 辅助 QA 工作流、自动化测试执行、LLM/Agent Eval、QA 发现与分发有关的项目。
> 目的：提炼可迁移的产品和工程做法，评估适合小步试验的迭代方向；不是市场规模报告，也不是对这些项目的独立质量认证。

## 摘要

样本中的项目大致走向四类产品形态：

1. **目录和分发**：把 Skills 按任务组织，通过搜索、插件/套件和学习入口降低首次使用成本。
2. **任务工作流**：把 QA 任务拆成可交接阶段，并以结构化报告、状态和证据结束，而不是只留下对话文本。
3. **执行适配器**：调用 Playwright、CI、SAST 或专用工具完成真实动作，保留过程和产物。
4. **行为评测**：用版本化数据集、真实轨迹、盲测夹具和 CI 比较判断行为变化。

跨项目最值得借鉴的是：**围绕少数高频任务交付可检查的质量产物，再逐步加上执行与回归证据。** 这比追求目录继续变大更容易验证用户价值。具体选哪条工作流应由目标仓库的既有能力、真实用户任务和运行证据决定。

## 方法与证据限制

本次使用 GitHub 插件搜索仓库、文件和提交，并读取所选仓库的 README、技能文件、CI 文档、基准测试说明和限制说明。检索默认分支；最近提交日期按 GitHub 返回的 UTC 时间记录。

这些项目是按与本题的相关性挑选的代表样本，不是随机抽样。README 中的产品描述和项目方自报分数均按“项目方声明”处理；除明确读取的代码/契约外，没有克隆并运行这些项目，也没有独立复测其指标。因此，目录数、Stars、下载徽章或单次 Eval 数字都不作为效果证明。

## 对照当前仓库

本节用于避免把已有能力误列成新方向。现状来自仓库文件和带日期的归档记录；历史运行结果不代表本次重新运行。

| 领域 | 已有基础 | 仍需区分的缺口 |
| --- | --- | --- |
| Skill 覆盖与分发 | 当前树为中英文各 165 个 Skill，README/索引和固定 `skills@1.7.0` 分发兼容 gate 已存在。 | 截至本次调研日，README/索引写 165，但演进路线图正文仍有 164 的旧快照；此计数差异已于 2026-10-26 修正。全量发现/安装不是全 Agent、全语言的真实兼容矩阵。 |
| 路由与工作流 | `discover-testing` 已有五条 Composition 路线；`change-impact-analysis`、`regression-test-selection`、`root-cause-analysis`、`ui-test-playwright`、`test-reporting` 等可复用。 | Composition 是导航元数据，Router 一次选择主 Skill 和最多一个可选 Skill；不是多阶段自动调用链或执行器。 |
| 可执行 UI 测试 | `ui-test-playwright` 有本地合成 checkout fixture，覆盖 `good`、`bug`、`timeout`，并要求以业务状态而不是页面标题判定。 | fixture 存在不等于 Playwright/runtime 已运行；现有 Pilot 契约把浏览器/runtime 执行列为 `NOT_RUN`。 |
| Skill 行为评测 | 2026-10-03 Codex Pilot 的五个核心 Skill 中英文用例为 34/34 `PASS`；第二模型仅抽样 5/5；2026-10-05 将三个中文 Benchmark 延伸到每侧各三次。结果支持有限的文本行为和状态契约观察，不支持普遍质量增益或正式等级。[Pilot](../../evidence/skill-quality/2026-10-03-codex-pilot/README.md) · [重复采样](../../evidence/skill-quality/2026-10-05-codex-benchmark-repeat/README.md) |
| 更大范围的真实模型运行 | 2026-10-11 汇总的 530 个新增用例为 94 `PASS`、1 `FAIL`、4 `ERROR`、431 `NOT_RUN`；328 份评测配置校验与 230 个脚本测试当时通过。 | 这是有边界的当前源码运行，不是全库行为评测；未执行用例、失败和错误都要保留。无需为了“全绿”盲目重跑全部用例。[运行续评](./2026-10-08-review-runtime-continuation.md) |
| 真实业务与 Router 观测 | 已有业务验收清单、状态契约、benchmark 和证据模板。 | 真实项目业务验收仍为 `NOT_RUN`；Router 的 canonical `skill.selection` observed event 缺失，所以自然选择与业务路由效果仍是 `BLOCKED`/未证明。[业务验收清单](../../evidence/skill-quality/2026-10-03-codex-pilot/BUSINESS_ACCEPTANCE.md) · [Pilot 契约](../../docs/governance/SKILL_EVALUATION_PILOTS.md) |

因此，下一步不是“从零补运行评测”，而是**把已有测试资产和有限运行证据接到一项真实、可验收的 QA 任务上**；同时只补最关键的已知证据缺口。成本和运行权限也要被视为产品约束：2026-10-03 Pilot 报告中的调用成本尚未完成可接受性评估，新的模型调用应按代表性样本和明确预算安排。

## GitHub 项目介绍、Topics 与 README 审查（2026-10-26）

我核对了 GitHub 当前 `main`、仓库 About 元数据、Topics，以及本地 `develop` 的双语 README。GitHub 文档说明 Topics 用于按项目目的和领域分类，最多 20 个；README 是访客判断项目用途和开始使用的主要入口。[仓库 Topics 说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) · [README 说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

| 项目区域 | 当前证据 | 判断 |
| --- | --- | --- |
| GitHub About 简介 | 更新前称项目为 “open-source AI-native Quality Engineering skill system”，并称其覆盖整个 SDLC 的 reasoning、design、execution、evaluation 和 improvement。 | **已更新。** 仓库使用 PolyForm Noncommercial 1.0.0；该许可证把许可目的限定为非商业用途，而 OSI 对 Open Source 的定义明确不允许许可证限制使用领域。因此 About 移除了 “open-source”，并明确项目是双语、可独立安装的 Agent Skills 集合。[PolyForm 许可证](https://polyformproject.org/licenses/noncommercial/1.0.0) · [OSI FAQ](https://opensource.org/faq) |
| Topics | 更新前有 10 个：`agent-skills`、`ai-qa`、`ai-skills`、`ai-testing`、`ai-tools`、`awesome-list`、`prompt-engineering`、`qa`、`qa-skills`、`skills`。 | **已精简并改为测试与宿主相关分类。** 移除 `ai-qa`、`ai-skills`、`ai-tools`、`awesome-list`、`skills`；保留相关核心标签并添加更具体的测试、质量工程与宿主标签。[fishzjp/qa-skills](https://github.com/fishzjp/qa-skills) · [PramodDutta/qaskills](https://github.com/PramodDutta/qaskills) |
| README 内容与状态 | GitHub `main` 当前 README 已是 330 个双语目录、每种语言 165 个 Skill，并列出 `one-page-test-strategy`；计数不用再改。GitHub `main` 与本地 `develop` 的双语 README 均包含 `social-preview.jpg` 引用。 | **不需要整体重写，适合做一轮入口整理。** 双语首页已经有快速安装、代表场景、完整目录、许可证说明和 Skills CLI 的验证边界，主体内容可用；较大的改进空间是让第一屏更快说明“这是可安装的 Skill 包，不是通用执行平台”，并减少开头的次要链接。仓库设置里的 GitHub 社交卡片是否另有配置，本次没有核验。 |

### 建议方案

**1. About description（优先级 P0，低成本，已完成）：** 用准确说明替换“open-source / system / execute”的表述。采用文案：

> Bilingual Agent Skills for software testing and QA workflows from requirements through release. Independently installable for Codex, Claude Code, Cursor, and compatible coding agents. Licensed under PolyForm Noncommercial 1.0.0.

这段突出交付形态、语言、用途、宿主范围和许可证；宿主兼容性的“已验证”范围仍以 README 中固定版本的 Skills CLI gate 为准，不应从简介推导所有平台都经过同等验证。

**2. Topics（优先级 P1，低成本，已完成）：** 用一组语义清晰的基础 Topics 替换宽泛/重复项：

```text
agent-skills, ai-testing, software-testing, test-automation,
quality-engineering, quality-assurance, qa-skills, qa,
claude-code, cursor, openai-codex, prompt-engineering
```

这是按当前产品实际范围和同类仓库的现有用法做的分类建议，不是搜索流量或新增 Stars 的预测。本次使用 12 个相关标签，没有为了凑满 GitHub 允许的 20 个上限而加标签；可在后续结合 GitHub 流量来源和用户搜索反馈再调整。

**3. README（优先级 P1，中低成本）：** 保留双语文件和现有详细目录，不重写 165 个 Skill 的说明；先收紧首屏：

- 把快速安装放到“我们是什么 / 适合谁”后最显眼的位置，并将快速链接缩成“安装、按任务浏览、完整目录、贡献”几项；治理和集成长文放到后续文档导航。
- 加一行简短边界：“This repository provides Agent Skills and reusable QA workflows; it does not provide a universal test runner.” 中文版同步说明“提供技能包和流程，不是通用测试执行平台”。
- 保留 PolyForm Noncommercial 徽章，并在首屏附近明确非商业许可，避免用户只在文末看到使用限制。
- 若要减少 README 长度，先将详细技能表交由现有 `docs/catalog/skills-index*.md` 承担，README 保留任务入口和代表 Skill；这是可选的信息架构调整，先检查对 GitHub 浏览与站点收录的影响，不必与 About/Topics 修正捆绑。
- README 的 `social-preview.jpg` 引用现已出现在 GitHub `main`；仍需单独核对 GitHub 仓库 Settings 的 Social preview，因为 README 内嵌图与仓库分享卡片是不同展示位置。

**验收方式：** GitHub About 不再声称 OSI 意义上的开源，描述和 README 对项目交付形态一致；Topics 仅保留与 Agent Skills、测试和实际支持宿主相关的标签；中英文首页首屏都能让新用户找到单个 Skill 安装方式、完整目录和许可证，目录计数与当前 Catalog 一致。不要用 Stars 变化作为单次文案修改的效果证明；可用 GitHub 流量来源和落地页点击、安装入口点击及首次安装反馈观察趋势。

**执行结果（2026-10-26）：** 用户确认后，已更新 GitHub About description 和 Topics。随后通过 GitHub REST API 与 `gh repo view` 两种方式回读核实，description 和 12 个标签均已生效。README 与仓库文件没有在这次 GitHub 元数据操作中改动。

## 相邻项目观察

### 1. QA Skills 与工作流目录

| 项目 | GitHub 可观察到的内容 | 对迭代的启发 | 边界 |
| --- | --- | --- | --- |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | 仓库把 Agents、Instructions、Skills、Hooks、Workflows、Plugins 分开维护；README 指向带全文搜索/筛选的站点、Learning Hub 和机器可读 `llms.txt`，并提供插件安装命令。2026-10-22 的提交继续接收社区 Skill。 | 目录可以围绕“用户要完成的事”提供精选路线、示例和套件，而不只是一个长列表；机器可读索引也能帮助 Agent 搜索。 | 它与 GitHub Copilot 的插件和市场入口紧密集成，不能由此推断同一分发方式适合所有 Agent。README 的资源量和使用入口不是实际采用率证据。 |
| [anthropics/skills](https://github.com/anthropics/skills) | 提供 Skill 示例、模板和规范目录；安装入口通过 Claude 插件市场。README 明确写明仓库用途是示例和教育，具体运行表现应自行验证。最近提交（2026-10-09）包含动态工作流和 quickstart 更新。 | 复杂 Skill 可带自包含资源与可跟随的 quickstart；明确“示例/规范/运行结果”不同层次，有助于避免过度承诺。 | 示例目录不是生产效果的 benchmark。它聚焦 Claude 实现，不能直接代表跨工具兼容。 |
| [fishzjp/qa-skills](https://github.com/fishzjp/qa-skills) | README 记录 12 个 Skill 与共享 `core/` 知识库，要求通过 `skills.sh` 全量安装；`examples/README.md` 展示同一任务的 Skill On/Off 产物对照，并说明四组为双臂 n=3、中位样本，同时指出完整方法和原始数据不随仓库分发。最近提交（2026-10-21）调整 npm、skills.sh 与 Git 分发方式。 | “安装前后看同一任务产物”比只展示 Skill 数量更能帮助评估；可挑少量代表案例，展示断言、输入承接和证据差异。 | 公开的示例能显示结果形态，但完整原始评测链不在仓库；其共享 `core/` 安装约束也提高了技能之间的耦合，不一定适合强调单 Skill 独立安装的项目。README 的历史数值不是本次独立复测。 |
| [PramodDutta/qaskills](https://github.com/PramodDutta/qaskills) | 提供目录站点、CLI、技能套件，以及一个 MCP Server；MCP 工具包含搜索、读元数据、读 Skill 内容、安装、列分类和排行榜。最近提交（2026-10-21）调整站点活动信息。 | 若现有目录已能找到并安装 Skill，可先加任务分类、精选套件和可视化示例；若 Agent 内发现明显困难，再评估 MCP 搜索/安装接口。 | README 中的质量分数和支持的 Agent 数是项目方展示，未在本次检查中找到足以独立核实其评分方法和所有宿主行为的证据。增加 MCP、CLI、排行榜也会带来 API、发布和维护成本。 |

**外部参考：** [Awesome Copilot README](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/README.md)、[技能目录](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/docs/README.skills.md)、[Anthropic Skills README](https://github.com/anthropics/skills/blob/main/README.md)、[FishZjp 输出对照](https://github.com/fishzjp/qa-skills/blob/main/examples/README.md)、[QASkills MCP README](https://github.com/PramodDutta/qaskills/blob/6fc32e4adb7449fd5136746efc7f085357fca6c8/packages/mcp/README.md)。

### 2. 通用开发工作流

[obra/superpowers](https://github.com/obra/superpowers) 把构思、设计、计划、TDD、分步实现、审查和收尾组织成可组合 Skill，并为多个编码 Agent 提供适配。README 的产品重点是让开发 Agent 按阶段推进并在关键点与用户确认；2026-10-21 的 v7.0.1 提交继续调整工作流和技能恢复能力。

**可迁移做法：** 把一个 QA 任务拆成“输入审计 → 风险/验收 → 设计或选择测试 → 执行 → 结果分类 → 证据交接”，规定每阶段产物和退出条件。将这些阶段先作为可复制的任务配方，不必一开始做通用编排引擎。

**边界：** 这是全软件开发方法论，不是 QA 专项评测；完整流程对简单任务可能过重，阶段数应由任务风险决定。[README](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/README.md) · [v7.0.1 提交](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b)。

#### github/spec-kit：有门禁的 Bugfix 工作流和可安装套件

[Spec Kit](https://github.com/github/spec-kit) 将 feature、bug fixing 和 idea assessment 做成独立入口；其 [bugfix bundle](https://github.com/github/spec-kit/blob/main/docs/reference/bundles.md) 组合 Bug 扩展与 `assess → human gate → fix → test` 工作流。Bundle 负责把有版本约束的组件打包安装，流程仍由显式步骤和 gate 构成。

**可迁移做法：** 可把现有 `change-regression` 等导航升级为少量 task recipe，并在变更前/发布前设人工确认点；recipe 可组合现有 Skill，配一份统一 handoff/evidence manifest。

**边界：** Spec Kit 是有 CLI、catalog、安装生命周期和 workflow runtime 的开发工具。本仓库应先采用“recipe + 自包含证据模板”的轻量层，只有验证出重复使用和安装组合需求后，再评估 CLI/Bundle；不要同时维护第二个包管理器或自动编排器。[Workflows 文档](https://github.github.io/spec-kit/reference/workflows.html) · [Bundles 文档](https://github.github.io/spec-kit/reference/bundles.html)。

### 3. 专项 QA 交付与证据工件

#### openqa-cn/codexqa：直接相关的质量验证 Skill 套件

[CodexQA](https://github.com/openqa-cn/codexqa) 把定位放在“代码写完后的测试和验证”，README 列出路由器与多个专用 Skill，包括变更影响、缺陷分析、测试用例、造数、根因和浏览器回放。可观察到的产物包括本地 HTML/Markdown/JSON 报告，以及带步骤截图的浏览器执行报告。

其 [inventory-service 示例](https://github.com/openqa-cn/codexqa/blob/783954281fc4898a9fac66a575363f419d4683e4/examples/inventory-service/README.md) 提供已知正确基线、包含 7 个缺陷和 4 个诱饵的变更分支、可执行答案键和盲测说明。README 报告了一次 Agent 运行 7/7 召回、7/7 精确率；文档同时明确它是同一项目自建夹具、单模型单次运行，**不是 benchmark**。近期代码变更还强调可见页面证据后才通过，并修复假通过和丢失用例问题：[要求可见证据](https://github.com/openqa-cn/codexqa/commit/7d81ca1d3baea84e8159352699731f01fc492476) · [修复 false pass](https://github.com/openqa-cn/codexqa/commit/238b1521b55848b9bfd6528e923293014157d4b5)。最近提交（2026-10-03）包括从符号图生成架构 Wiki。

有些能力的限制文档写明：符号图分析器使用仓库外单独发布的闭源 CLI，仓库 CI 不安装执行该 CLI，缺少公开宿主 Agent 运行和独立质量 benchmark；图覆盖也受解析器、动态调用和符号冲突影响。[Code Analyzer 限制](https://github.com/openqa-cn/codexqa/blob/783954281fc4898a9fac66a575363f419d4683e4/skills/codexqa-code-analyzer/KNOWN_LIMITATIONS.md) · [兼容和验证矩阵](https://github.com/openqa-cn/codexqa/blob/783954281fc4898a9fac66a575363f419d4683e4/docs/SUPPORT_MATRIX.md)。

**可迁移做法：** 输出可离线审查的报告文件；有针对性地创建已知正确、已知错误和诱饵代码夹具；把结构分析、模型判断和真实执行分开声明。

**边界：** 不要把 README 里的单次分数直接当成泛化能力证据，也不要仅凭示例报告认定分析器有效。外部闭源运行时会带来许可证、供应链、版本兼容和可复现性成本。

#### github/awesome-copilot 的 bug-receipt Skill：可验证的收尾契约

[bug-receipt](https://github.com/github/awesome-copilot/tree/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt) 要求 Bug/Incident 收尾包含 Problem、Baseline、Root cause、Change、Proof、Gaps 和证据来源。配套 [JSON Schema](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt/references/receipt.schema.json) 与 [Node 校验器](https://github.com/github/awesome-copilot/blob/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt/scripts/validate-receipt.mjs) 检查状态不变量：例如 VERIFIED 需要观察到基线、根因证据、改动和通过的验证；PARTIAL/BLOCKED 必须说明缺口。上游原作者声明 Skill 最初发布于另一个 MIT 项目。

**可迁移做法：** 借鉴机器可校验的完整性约束与“证据由谁提供/何时执行”字段，让工作流报告能由脚本检查，而不只依赖模型记得遵守格式。

**边界：** 这是单个 Skill 的契约，不是工作流编排器。若目标仓库已有状态模型，应迁移其不变量和字段语义，不应照抄状态名字造成并行词汇。

### 4. 自动化测试执行与修复

[microsoft/playwright 的 Test Agents](https://github.com/microsoft/playwright/blob/main/docs/src/test-agents-js.md) 提供三种角色：Planner 探索应用并写 Markdown 测试计划；Generator 按计划生成 Playwright 测试，并在生成期间检查 selector 和 assertion；Healer 执行测试并尝试修复失败的测试。文档要求使用 seed test 初始化测试环境，且支持 Codex、Claude、OpenCode 等 Agent loop。Playwright 仓库最近提交（2026-10-25）主要为 CI 文档更新。

**可迁移做法：** 让测试计划、生成代码和运行结果成为不同可审查阶段；针对已有 UI 自动化能力，优先复用 Playwright 原生工具和 fixture，不自建浏览器执行器。

**风险与控制：** Healer 可能通过调整测试而非修复产品来消除失败。若启用修复，应保留原始失败、修订差异、再次运行的结果，并由人审查 assertion 是否被削弱。该文档描述功能和用法，不提供普遍的缺陷检出率或自愈准确率证据。

若要验证生成测试是否真的能捕捉行为错误，可以在适用的项目中试用 [StrykerJS](https://github.com/stryker-mutator/stryker-js)：它可用 mutation testing 检查测试对代码变异的敏感度，并支持按变更增量运行。适合做某个 JavaScript/TypeScript 测试栈的可选适配；它不是跨语言通用质量分，也不能取代需求验收。

### 5. LLM/Agent Eval 与 CI

| 项目 | 可观察到的实现 | 对 QA Skills 的启发 | 成本与边界 |
| --- | --- | --- | --- |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | CLI/库做 LLM Eval、模型对比和红队；官方文档包含 GitHub Action，对 PR 中修改的 Prompt 做前后比较并把结果发到 PR；CI 文档列出 JSON/HTML/JUnit 输出和失败阈值。最近提交（2026-10-25）是依赖和 CI 变更。 | 为 AI 功能/Prompt/Agent 测试 Skill 生成或配置 promptfoo 项目文件、CI 示例和带 commit/run ID 的证据报告。用已有引擎跑，不另造 Runner。 | 真实运行通常需要 provider 凭据，会产生费用和模型方差；PR comment/共享结果也有数据隐私要求。工具支持 CI 不等于某个 Skill 的 Eval 设计正确。 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | README 和文档提供 Pytest 风格的 LLM Eval、数据集、单轮/多轮、端到端和组件级测试；Agent Eval 分析完整轨迹和单独工具调用/步骤，文档给出在 CI 运行 eval 的方式。最近提交（2026-10-23）继续维护 CLI/云端集成。 | 适合把真实失败转成可提交、可回归的数据集和测试；按失效原因选择 trace-level 或单组件断言，而不是只看最终答案。 | LLM-as-judge 需要校准，且可能有方差、时延、费用和 trace 敏感信息处理要求。README 描述框架能力，不等于某个目标系统达到相同质量。 |

**外部参考：** [Promptfoo README](https://github.com/promptfoo/promptfoo/blob/b4c2404a0dee93dcd4d53a323d6f32f87ee27558/README.md)、[Promptfoo GitHub Actions](https://github.com/promptfoo/promptfoo/blob/b4c2404a0dee93dcd4d53a323d6f32f87ee27558/site/docs/integrations/github-action.md)、[Promptfoo CI/CD](https://github.com/promptfoo/promptfoo/blob/b4c2404a0dee93dcd4d53a323d6f32f87ee27558/site/docs/integrations/ci-cd.md)、[DeepEval README](https://github.com/confident-ai/deepeval/blob/5410e3822dda5f889d5f35de3325a3738004aeb1/README.md)、[DeepEval CI Eval 文档](https://github.com/confident-ai/deepeval/blob/5410e3822dda5f889d5f35de3325a3738004aeb1/docs/content/docs/evaluation-unit-testing-in-ci-cd.mdx)、[DeepEval Agent Eval 文档](https://github.com/confident-ai/deepeval/blob/5410e3822dda5f889d5f35de3325a3738004aeb1/docs/content/guides/guides-ai-agent-evaluation.mdx)。

### 6. 更完整的运行时平台

[proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) 是一套 CLI/MCP 质量工程工具，为代码 Agent 配置多种客户端，提供测试生成、覆盖缺口分析、Flaky 行为诊断、发布质量评估和质量模式知识库。README 列出 Node.js 22、npm、SQLite 和可选原生依赖；最近提交（2026-10-25）仍在维护依赖。

[test-zeus-ai/testzeus-hercules](https://github.com/test-zeus-ai/testzeus-hercules) 提供面向浏览器的测试 Agent，以 Gherkin/自然语言为入口，接入 Playwright 和 Python sandbox 来执行自动化流程。

这些项目说明“Runtime/CLI/MCP + Agent + 状态/报告”可以形成更直接的执行产品，但同时需要安装、权限、数据、原生依赖、客户端适配、版本和现场故障支持。更稳妥的借鉴路径是先定义可复核的工作流产物与可选 Runner 接口，只有用户任务证明需要持续运行、状态保存或 CI 触发后，才考虑平台化。

## 可行迭代方向比较

以下收益与可行性是基于样本和常见工程依赖的定性判断，不是已测的商业回报。

| 方向 | 预期收益 | 可行性 | 主要工作 | 验收证据 | 主要风险 |
| --- | --- | --- | --- | --- | --- |
| **A. 任务型 QA 交付配方 + 证据收据** | 高 | 高 | 选 1–2 个高频任务（如 Bugfix 验证、PR 变更回归）；规定输入、阶段交接和退出条件；报告同时可读且可机读，并校验状态与证据约束。 | 基线、改动、验收条件、实际执行、失败归类和证据路径能关联；缺证据时不能输出完整通过结论；示例能独立复现。 | 过早做通用编排，或把猜测根因写成已证实事实。 |
| **B. 盲测夹具与效果报告** | 高 | 中 | 复用已有 checkout fixture 和 Codex Pilot；补充跨阶段/多任务的 known-good、known-bad、decoy、ambiguous/blocked，不复制另一套大评测集；按版本、Agent、模型、任务、重复次数和费用记录。 | 可公开运行脚本和答案键；报告误报、漏报、执行成功率、耗时/费用和限制；分清单次结果与可泛化结论。 | 自建夹具泄漏答案或过拟合；只用语义 Judge 而无校准；把结构门禁误报成效果。 |
| **C. 首次使用任务入口与示例库** | 中高 | 高 | 用少量“我现在要做什么”入口整理 Skill 配方和安装；提供同任务输入、输出样例和适用边界；复用现有目录网站/CLI 先验证搜索体验。 | 记录从选择入口到首次得到可用产物的完成率、耗时、常见误选和反馈；示例内容含事实与假设标注。 | 增加另一套 MCP/CLI/排行榜，造成重复分发和长期维护。 |
| **D. 复用外部 Eval/CI 工具的薄适配** | 中高（AI QA 场景） | 中 | 为 Promptfoo/DeepEval 提供可选配置生成、数据集结构、CI 示例和结果解释；统一运行元数据，保留工具原始报告。 | 同一数据集/配置可在开发和 CI 重跑；能按 commit/run ID 比较；失败不被摘要吞掉，成本和隐私边界明确。 | 把特定平台写成硬依赖；Judge 波动和 API 凭据导致 CI 噪声/费用；新维护自有 Runner。 |
| **E. 选择性执行器/宿主适配** | 中高 | 中低 | 从一种成熟工具（通常 Playwright）出发，定义执行接口、运行状态和报告引用；生成的测试仍回到用户项目，默认由用户决定是否执行或修复。 | 对同一有限场景能够实际执行；保留原失败、修改过的 assertion 和重跑结果；支持矩阵只写入实际验证过的宿主/版本。 | 多 Agent/浏览器运行带来权限、环境、selector 稳定性和变更测试掩盖缺陷的风险。 |
| **F. Router 选择事件与宿主观测适配** | 中高（路由质量验证） | 中低 | 为一种实际可观测的宿主记录最小 `skill.selection` 事件；不能从最终答案反推已调用 Skill。 | 可重放的 route/primary/optional/selected_skills 与 run metadata；无事件时仍明确 `BLOCKED`。 | 宿主可能不暴露调用事件；自建遥测会增加隐私与维护负担。 |
| **G. 完整 Agent QE 平台** | 潜在高 | 低 | 安装器、MCP server、状态存储、执行器、知识检索、CI 和跨 Agent 适配。 | 真实用户持续使用，并能量化较现有 Skill/CLI 的新增价值；支持与权限/升级策略清晰。 | 对纯 Skill 仓库而言投入大，可能复制现有执行工具而转移产品定位。建议延后到用户证明确有持续运行需求后再立项。 |

## 针对本仓库的推荐顺序

1. **P0：做一条可审查的 Bugfix/PR 验证配方。** 建议先选 Bugfix：缺陷、基线、修复、回归的前后对照容易定义；复用现有根因、变更影响、回归选择、Playwright 和报告能力。用专门的流程 Skill 或 recipe 串阶段，不把多步链塞进 Router 一次只选一个主 Skill/一个可选 Skill 的契约。
2. **P0：定义最小证据收据和退出状态。** 产物至少关联 issue/PR、baseline 与目标 commit、验收条件、选定测试、实际执行状态、原始报告路径、失败归类、未覆盖风险和人工决策。`bug-receipt` 的 Schema/validator 可作参考；本仓库已有状态模型，应沿用 `PASS/FAIL/BLOCKED/NOT_RUN` 等规范，不另造枚举。
3. **P1：先在现有 fixture 上补跨阶段红绿验证，再做一次获授权的真实项目试点。** 现有 `good/bug/timeout` 可覆盖局部断言敏感性；增加或复用一个基线缺陷、修复版本、decoy 和环境阻断场景。要求 `good` 正常通过、已知产品缺陷归为 `FAIL`、环境超时为 `BLOCKED/NOT_RUN`；三者都不能被报告成绿色。真实项目需要明确目标环境、权限、预算和验收责任人，缺一项就保持未验收。
4. **P1：整理已有评测债务，而不是执行全部未运行用例。** 先复核 1 个 `FAIL`、4 个 `ERROR` 的归因和处理，再按重要 Skill/风险选择一小组 `NOT_RUN` 代表案例；自然 Router selection 只有在宿主能产生 canonical 事件时才评。基线报告保留日期、源码哈希、目标模型/配置、费用和限制，不把 10 月的旧证据写成当前结果。
5. **P1：把配方做成任务型首次使用入口。** README、索引和网站展示 3–5 个任务入口，每个给输入例子、安装命令、可预期产物、未运行时状态和适用边界。先用人工反馈/小范围试用衡量首次完成，不先做排行榜或 MCP。
6. **P2：给 AI Native QA 做外部 Eval 工具薄适配。** 优先在一个真实 AI 功能上生成 Promptfoo 或 DeepEval 可运行配置，数据集和原始 trace 由工具保留，Skill 负责测试设计、结果解释和限制声明。没有明确目标、凭据或 CI 预算前，不承诺持续自动执行。
7. **延后：完整 Agent QE 平台、全宿主矩阵和自有 Eval Engine。** 只有当多个试点证明任务需要持久状态、团队级 CI 调度或当前工具无法提供的宿主事件时再评估。

对外调研倾向“recipe + receipt + task-first discovery”；本地证据把首轮从“补齐更多模型运行”调整为“用有限预算完成一条端到端业务验证，并解决最关键的 FAIL/ERROR/selection 观测缺口”。这个排序是基于现有资产和依赖的工程判断，不是已量化的商业收益结论。

## 不建议直接照搬的做法

- **只凭目录数、排行榜分数或下载徽章证明质量。** 它们可反映项目活动/展示方式，不能证明真实任务行为正确。
- **把自愈定义成“测试变绿”。** 必须保留原始失败并确认产品契约断言未被削弱。
- **自己重写 Promptfoo/DeepEval 的 Eval Engine。** 重点应放在领域用例、适配和证据解释。
- **过早引入完整 Runtime、数据库、向量检索和全宿主矩阵。** 相比先把一个 QA 结果交付物做可信，这些是更昂贵且证据要求更高的方向。
- **直接依赖竞品的闭源或特定宿主引擎。** 可借鉴输出/流程模式，不应把外部专有运行时作为跨工具 QA Skills 的隐含前提。

## 主要来源

- [github/spec-kit](https://github.com/github/spec-kit) · [Workflow 文档](https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md) · [Bundle 文档](https://github.com/github/spec-kit/blob/main/docs/reference/bundles.md)
- [github/awesome-copilot](https://github.com/github/awesome-copilot) · [Bug Receipt Skill](https://github.com/github/awesome-copilot/tree/d85f762d6e521abf5fe16703946e9b38adc42da7/skills/bug-receipt)
- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [microsoft/playwright Test Agents](https://github.com/microsoft/playwright/blob/main/docs/src/test-agents-js.md)
- [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js)
- [openqa-cn/codexqa](https://github.com/openqa-cn/codexqa) · [blind-eval fixture](https://github.com/openqa-cn/codexqa/tree/main/examples/inventory-service) · [known limitations](https://github.com/openqa-cn/codexqa/blob/main/skills/codexqa-code-analyzer/KNOWN_LIMITATIONS.md)
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · [GitHub Actions](https://github.com/promptfoo/promptfoo/blob/main/site/docs/integrations/github-action.md) · [CI/CD](https://github.com/promptfoo/promptfoo/blob/main/site/docs/integrations/ci-cd.md)
- [confident-ai/deepeval](https://github.com/confident-ai/deepeval) · [CI Eval docs](https://github.com/confident-ai/deepeval/blob/main/docs/content/docs/evaluation-unit-testing-in-ci-cd.mdx)
- [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe)
- [test-zeus-ai/testzeus-hercules](https://github.com/test-zeus-ai/testzeus-hercules)
- [fishzjp/qa-skills](https://github.com/fishzjp/qa-skills) · [output comparisons](https://github.com/fishzjp/qa-skills/tree/main/examples)
- [PramodDutta/qaskills](https://github.com/PramodDutta/qaskills) · [MCP server tools](https://github.com/PramodDutta/qaskills/tree/main/packages/mcp)
