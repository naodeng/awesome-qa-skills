# Awesome QA Skills 四阶段演进设计

## 决策摘要

仓库的产品叙事与路由模型调整为：

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

本次保持既有物理目录和 Skill 名称不变。能力阶段是逻辑导航层，而不是新的目录层；现有安装命令、单 Skill 复制路径和外部链接继续有效。

当前每种语言有 49 个 Skill（10 个 `testing-workflows`、36 个 `testing-types`、3 个 `skill-engineering`），中英双语共 98 个目录。旧文档中“每种语言 46 / 总计 92”的计数未包含 `skill-engineering`，本次统一修正。

## 目标与非目标

### 目标

- 让使用者按质量能力成熟度，而不只是按测试类型或工具找到 Skill。
- 保留现有的工作流、类型、工具专项和 Skill Engineering 治理结构。
- 以六个可验收迭代补齐质量工程、生产质量和 AI Native QA 的缺口。
- 在双语 README、索引、语言索引和 `discover-testing` 中使用同一套能力地图。

### 非目标

- 不移动、重命名或删除任何现有 Skill 目录。
- 不将相近主题机械拆成多个 Skill；每个新增 Skill 必须有独立输入、主要产物和路由触发条件。
- 不把 `ai-assisted-testing` 误称为 AI 产品测试；前者继续表示 AI for QA。

## 能力架构

| 能力阶段 | 面向的问题 | 现有锚点 | 重点新增方向 |
| --- | --- | --- | --- |
| Core QA Skills | 如何理解、设计、执行并报告基础测试？ | requirements、strategy、case、functional、API、security、reporting、日常/迭代工作流 | 仅校正导航与边界，不重复建设基础能力 |
| Engineering QA Skills | 如何把质量前移到需求和代码变更，并提高测试决策与诊断效率？ | requirements-analysis、code-review、automation-testing、performance-testing | Shift Left、变更影响、测试数据、契约、失稳与诊断、性能分析 |
| Production Quality Skills | 如何基于发布和生产证据做质量决策与闭环？ | release-testing-workflow、test-reporting | 发布就绪、生产验证、事故、Trace、指标异常 |
| AI Native QA Skills | 如何验证 AI 功能、LLM、Prompt、Agent 及其安全边界？ | ai-assisted-testing（跨层 AI for QA） | Testing for AI、Eval、Agent/Tool、Prompt 安全 |

`skill-engineering` 是横向治理层：它负责 Skill 的变更验证、文本质量与维护约束，不归入四个面向用户的能力阶段。

## 路由与文档设计

`discover-testing` 的路由顺序更新为：

1. 判定用户目标属于哪一能力阶段；不确定时以交付物和所处生命周期判断。
2. 在该阶段选一个唯一主 Skill，必要时最多附带一个互补 Skill。
3. 再判工作流、工具专项或 Plus 版本，而不是把它们当成成熟度阶段。
4. 明确区分 AI for QA（`ai-assisted-testing`）与 Testing for AI（AI Native QA）。

对外文档采用“双视图”：能力地图是首要导航；物理目录和按工具安装路径保留为实施导航。全量索引需同时列出实际路径、能力阶段和状态（现有 / 计划新增 / 扩展）。

## 跨仓库参考边界

`/Users/nao.deng/awsomeCode/awesome-qa-prompt` 是新增能力的 Prompt Baseline 参考源。该仓库已经提供与多数候选能力相近的主题，例如 `acceptance-criteria-reviewer`、`change-impact-analysis`、`flaky-test-analysis`、`distributed-trace-analysis`、`ai-feature-test-design`、`ai-evaluation-design`、`ai-agent-test-design` 与 `agent-tool-call-test-design`。

每个新增 Skill 开始前，必须先建立“Skill 名 → 参考 Prompt 模块 → 独立安装包边界”的映射。可适配其中的输入审计、禁止编造、信息不足降级、Human Task 边界、结构化输出与反硬编码 KPI 原则；不得复制 Prompt Baseline 的 `Standard-version/` 目录、框架变体或把跨仓库相对链接带入 Skill 包。Skill 的最终目录名仍以本仓库的命名、metadata、独立安装与 evals 规范为准。

## 六个迭代与新增规模

新增规模是 **29 个逻辑 Skill**，均需中英双语实现，合计 **58 个新目录**。完成后为每种语言 78 个、双语 156 个目录。该数字不包含对现有 Skill 的扩展。

| 迭代 | 能力阶段 | 新增 Skill | 数量 | 现有 Skill 的扩展 |
| --- | --- | --- | ---: | --- |
| 1 | Engineering QA / Shift Left | `acceptance-criteria-review`、`requirement-gap-analysis`、`quality-risk-analysis`、`testability-analysis` | 4 | `requirements-analysis` 提供入口级交接 |
| 2 | Engineering QA / Change Intelligence | `change-impact-analysis`、`pr-test-impact-analysis`、`regression-scope-analysis`、`regression-test-selection` | 4 | `code-review`、`release-testing-workflow` 接入变更证据 |
| 3 | Engineering QA / Execution Intelligence | `test-data-generation`、`api-contract-testing`、`flaky-test-analysis`、`root-cause-analysis`、`log-analysis` | 5 | `manual-testing` 增补探索式测试模式；`ai-assisted-testing` 交接 AI 辅助数据生成 |
| 4 | Engineering QA / Performance | `performance-workload-modeling`、`performance-result-analysis`、`performance-bottleneck-analysis`、`performance-regression-analysis`、`capacity-planning-analysis` | 5 | `performance-testing` 保持总入口，工具 Skill 保持脚本实现 |
| 5 | Production Quality | `production-verification`、`production-incident-analysis`、`distributed-trace-analysis`、`metrics-anomaly-analysis` | 4 | `release-testing-workflow` 增补 release-readiness 评估模式，不新建重复 Skill |
| 6 | AI Native QA | `ai-feature-testing`、`llm-testing`、`llm-evaluation-design`、`prompt-testing`、`ai-agent-testing`、`agent-tool-testing`、`prompt-injection-testing` | 7 | `prompt-testing` 内含 prompt regression 模式；`ai-assisted-testing` 保持 AI for QA |

将 `exploratory-testing`、`release-readiness-assessment` 和 `prompt-regression-testing` 设计为既有或新增 Skill 的明确模式，而非独立目录。这避免与 `manual-testing`、`release-testing-workflow`、`prompt-testing` 重叠。

## 新增 Skill 的边界

- Shift Left 的四个 Skill 分别输出 AC 缺陷、需求缺口、质量风险排序和可测试性结论；不得再次泛化地代写需求分析。
- Change Intelligence 的四个 Skill 形成“变更 → 影响 → 回归范围 → 执行选择”的单向链，输入与输出可串联但各自可独立使用。
- 执行智能与性能 Skill 产出分析、模型或决策证据；工具专项仍负责具体框架与脚本。
- Production Quality 只基于生产/发布证据提出判断，禁止编造监控数据、事故原因或放行结果。
- AI Native QA 强制区分模型行为、评测集/指标、Prompt、Agent 工具调用和对抗安全；对不确定输出采用可复核证据与风险等级。

## 每迭代的 Definition of Done

每个新增或扩展的 Skill 必须具备：

1. 中英文同名目录与对等能力边界。
2. `SKILL.md`、`prompts/`、`agents/openai.yaml`、`evals/eval.yaml` 和至少三类 eval case（成功、信息不足、风险边界）。
3. 只依赖自身目录内文件，可独立安装；无跨 Skill 内部链接。
4. 能力地图、双语索引、路由规则和安装说明同步更新。
5. `bash scripts/check_skills_quality.sh` 通过，并对变更的 `discover-testing` 做路由场景验证。

## 本轮仓库调整范围

- 更新 `README.md` 与 `README_EN.md`：定位、能力地图、准确计数和路线图入口。
- 更新 `skills-index.md`、`skills/zh/README.md`、`skills/en/README.md`：按能力阶段呈现，同时保留真实路径与工具专项入口。
- 更新 `skills/DIRECTORY_GUIDE.md`：声明物理目录稳定、能力阶段为逻辑分类。
- 更新中英文 `discover-testing` 的 `SKILL.md`、主 Prompt 和参考路由图。
- 新增一份面向贡献者的中英路线图，记录迭代、候选目录、边界和验收标准。

## 验收标准

- 所有对外统计均一致地显示“49 per language / 98 bilingual directories”。
- 使用者可以从任一入口回答“我现在属于哪个能力阶段”和“应该调用哪个唯一主 Skill”。
- 现有目录、安装命令和 Skill 名没有破坏性变化。
- 路线图中的 29 个新增项均有明确边界、迭代、优先级和现有资产关系。
