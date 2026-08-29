# Awesome QA Skills 演进路线图

> 状态：已确认的规划。本文描述未来建设顺序，不代表表中新增 Skill 已经可安装。

## 演进方向

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

这是能力导航模型，不是目录迁移方案。现有及未来 Skill 继续放在稳定的物理目录：

```text
skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/
```

当前每种语言有 49 个 Skill（10 个工作流、36 个测试类型、3 个 Skill Engineering），中英双语共 98 个目录。完成全部路线图后，每种语言将有 78 个、双语共 156 个目录。

## 能力地图

| 阶段 | 要解决的问题 | 当前代表能力 | 后续重点 |
| --- | --- | --- | --- |
| Core QA Skills | 如何理解、设计、执行和报告基础测试？ | requirements、strategy、cases、functional、API、security、reporting | 保持基础完整性，避免重复造 Skill |
| Engineering QA Skills | 如何前移质量、评估变更并提高诊断和性能决策？ | requirements-analysis、code-review、automation-testing、performance-testing | Shift Left、变更智能、执行智能、性能工程 |
| Production Quality Skills | 如何用发布和生产证据做质量判断及闭环？ | release-testing-workflow、test-reporting | 生产验证、事故与可观测性 |
| AI Native QA Skills | 如何验证 AI 功能、LLM、Prompt、Agent 与安全边界？ | 当前尚无 Testing for AI 专项包 | Eval、Prompt、Agent/Tool、安全 |

`ai-assisted-testing` 是横向的 **AI for QA**：用 AI 辅助传统 QA 工作；它不是 AI Native QA 的 Testing for AI 替代品。`skill-engineering` 是横向治理层，不是第五个能力阶段。

## 迭代路线与参考基线

每个候选项先参考 `awesome-qa-prompt` 中的同类 Prompt Baseline，再适配为独立可安装 Skill。参考关系不形成运行时依赖；不得复制 `Standard-version/`、框架变体目录或跨仓库相对链接。

| 迭代 | 阶段 | 新增 Skill | 优先级 | Prompt Baseline 参考 | 与现有 Skill 的边界 |
| --- | --- | --- | --- | --- | --- |
| 1 | Engineering QA / Shift Left | `acceptance-criteria-review` | P0 | `acceptance-criteria-reviewer` | 聚焦 AC 的可验收性，不代替全量需求分析 |
| 1 | Engineering QA / Shift Left | `requirement-gap-analysis` | P0 | `requirement-gap-analyzer` | 输出缺口与待澄清项，不代替策略 |
| 1 | Engineering QA / Shift Left | `quality-risk-analysis` | P0 | `quality-risk-analysis` | 输出质量风险排序和证据缺口 |
| 1 | Engineering QA / Shift Left | `testability-analysis` | P0 | `testability-analysis` | 输出可测性结论和改进建议 |
| 2 | Engineering QA / Change Intelligence | `change-impact-analysis` | P0 | `change-impact-analysis` | 变更到受影响区域的分析 |
| 2 | Engineering QA / Change Intelligence | `pr-test-impact-analysis` | P0 | `pr-risk-analysis` | 以 PR/Diff 为输入，输出测试影响 |
| 2 | Engineering QA / Change Intelligence | `regression-scope-analysis` | P0 | `regression-scope-analysis` | 定义回归范围，不直接选择执行集 |
| 2 | Engineering QA / Change Intelligence | `regression-test-selection` | P0 | `regression-test-selection` | 从已知测试资产选择回归集 |
| 3 | Engineering QA / Execution Intelligence | `test-data-generation` | P0 | `test-data-generation` | 生成可复核的测试数据方案，标注隐私与约束 |
| 3 | Engineering QA / Execution Intelligence | `api-contract-testing` | P0 | `api-contract-analysis` | 验证契约与兼容性，不代替通用 API 测试 |
| 3 | Engineering QA / Execution Intelligence | `flaky-test-analysis` | P0 | `flaky-test-analysis` | 定位不稳定测试模式和证据 |
| 3 | Engineering QA / Execution Intelligence | `root-cause-analysis` | P0 | `root-cause-analysis` | 基于证据形成假设，禁止宣称未证实根因 |
| 3 | Engineering QA / Execution Intelligence | `log-analysis` | P0 | `log-analysis` | 从日志提取时间线、症状和证据缺口 |
| 4 | Engineering QA / Performance | `performance-workload-modeling` | P0 | `workload-model-design` | 构造负载模型；无输入时标注假设 |
| 4 | Engineering QA / Performance | `performance-result-analysis` | P0 | `performance-result-analysis` | 解释结果，不编造阈值或结论 |
| 4 | Engineering QA / Performance | `performance-bottleneck-analysis` | P1 | `performance-bottleneck-analysis` | 产出可验证瓶颈假设 |
| 4 | Engineering QA / Performance | `performance-regression-analysis` | P1 | `performance-regression-analysis` | 对比版本证据，识别回归风险 |
| 4 | Engineering QA / Performance | `capacity-planning-analysis` | P1 | `capacity-planning-analysis` | 输出容量假设、缺口和待确认指标 |
| 5 | Production Quality | `production-verification` | P0 | `production-verification-generation` / `production-verification-review` | 基于生产证据验证，不代替人工放行 |
| 5 | Production Quality | `production-incident-analysis` | P1 | `production-incident-analysis` | 整理事故证据和后续分析 |
| 5 | Production Quality | `distributed-trace-analysis` | P1 | `distributed-trace-analysis` | 追踪调用链与关联证据 |
| 5 | Production Quality | `metrics-anomaly-analysis` | P1 | `metrics-anomaly-analysis` | 识别异常信号，不能编造监控数据 |
| 6 | AI Native QA | `ai-feature-testing` | P0 | `ai-feature-test-design` | 面向 AI 功能行为与风险，不是 AI 辅助测试 |
| 6 | AI Native QA | `llm-testing` | P0 | `llm-test-case-generation` | 验证模型行为、边界和失败模式 |
| 6 | AI Native QA | `llm-evaluation-design` | P0 | `ai-evaluation-design` / `llm-output-quality-evaluation` | 设计评测集、指标和人工复核 |
| 6 | AI Native QA | `prompt-testing` | P0 | `prompt-test-analysis` | 验证 Prompt 行为；包含回归测试模式 |
| 6 | AI Native QA | `ai-agent-testing` | P0 | `ai-agent-test-design` | 验证目标、状态、工具与失败恢复 |
| 6 | AI Native QA | `agent-tool-testing` | P0 | `agent-tool-call-test-design` | 验证 Agent 工具调用契约与副作用 |
| 6 | AI Native QA | `prompt-injection-testing` | P1 | `prompt-injection-test-design` | 验证注入攻击与防护边界 |

共计 29 个逻辑 Skill；中英文各实现一次，因此新增 58 个目录。

## 明确不单独新增的项

| 需求名称 | 归属 | 原因 |
| --- | --- | --- |
| `exploratory-testing` | `manual-testing` 的探索式测试模式 | 现有手工测试已覆盖会话式探索入口 |
| `release-readiness-assessment` | `release-testing-workflow` 的发布就绪评估模式 | 不把工作流中的门禁拆成重复包 |
| `prompt-regression-testing` | `prompt-testing` 的回归模式 | 与 Prompt 行为测试共享输入、断言和证据模型 |

## 每个迭代的完成定义

每个新增或扩展的 Skill 必须满足：

1. 中英同名、边界对等，并可独立复制安装。
2. 含 `SKILL.md`、主 `prompts/`、`agents/openai.yaml`、`evals/eval.yaml` 和成功/信息不足/风险边界三类用例。
3. 先进行输入审计，明确已知信息、缺失信息、假设和风险；禁止编造需求、指标、环境、执行事实或根因。
4. 信息不足时给最小可执行初版，或进入明确的阻塞/待确认状态；不以常识补造结论。
5. AI 只能整理证据、分析选项和提出建议，不能代替审批、发布、豁免、风险接受等 Human Task。
6. 同步更新能力地图、双语索引、路由和安装说明；执行 `bash scripts/check_skills_quality.sh`。

## 实施顺序

先完成本仓库的能力地图、路由、索引和贡献约定；随后按迭代 1 至 6 分批创建 Skill。每次创建前均复核本表的 Prompt Baseline，提取质量约束而非照搬文件结构。
