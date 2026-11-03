<div align="right"><strong>🇨🇳 中文</strong> | <a href="./WORKFLOW_CONTRACT_EN.md">🇬🇧 English</a></div>

# QA Workflow Contract v1.0

新建 `workflow.yaml` 时从 [`workflow.template.json`](../../resources/workflows/templates/workflow.template.json) 复制。完整实例见中英文 `pr-quality-review/workflow.yaml`，其中定义阶段依赖、专业 Skill ID、失败规则和权限策略。

`workflow.yaml`、`evidence.json` 和 `run-state.json` 是可移交的数据契约，不是工作流执行引擎。仓库另提供可选的本地状态 CLI，用于持久化检查点、校验失效和记录人工确认；它不调度或执行 Skill，也不能验证 `--approved-by` 的身份。Schema 位于 [`resources/workflows/schemas/`](../../resources/workflows/schemas/)，示例位于相邻的 `examples/`。工作流叶子 Skill 只依赖自己目录中的 prompt/reference；运行时不需要 Schema 文件。

为让仓库质量门禁在无额外 Python 包时也能检查契约，`workflow.yaml` 使用 JSON 语法（JSON 是 YAML 的子集）。仓库校验器会检查字段、步骤引用、相对资源路径、中英文镜像和示例；消费者可使用标准 JSON Schema Draft 2020-12 validator 做更严格校验。

## `workflow.yaml`

每个 `skills/{zh,en}/testing-workflows/<slug>/workflow.yaml` 记录：

- `id`、语义版本、类型（顺序工作流、路由、独立任务集合、单步任务）和生命周期状态。
- 必需/可选输入、可交付输出、阶段顺序与 `depends_on`。
- 输出 `evidence_kind` 标注交付物的主要证据类型；复合报告应按类型拆分输出，并在 `evidence.json` 中为每条声明保留自己的类型。
- 阶段可声明 `skip_when` 条件；每项说明可判断的条件和跳过理由。未声明时默认执行，不允许静默跳过。
- 阶段需要的 canonical Skill ID、可选的包内 prompt 路径、失败/缺少依赖时的处理。
- 默认权限、必须显式审批的副作用、交接字段和证据契约版本。
- Checkpoint 记录 Workflow 包指纹、用户输入指纹、Commit SHA、阶段状态、证据/产物引用和幂等键。变化时使结果失效。可选本地 CLI 在 `resume` 时校验这些值，并将中断中的 `RUNNING` 阶段标为 `BLOCKED` 供检查；它不自动重放阶段。真实 Skill 调用和可信人工授权仍由宿主 Runtime 负责。

Skill ID 是能力导航，不是自动安装依赖。宿主没有提供安装清单时，可用状态保持 `UNKNOWN`；缺少 Skill 时不得假装执行，可按契约降级、阻断或请求最小补充。

## `evidence.json`

证据分为 `fact`、`inference`、`plan`、`execution`。每条记录都带声明、状态、来源、生产者版本和观察时间；推断还需列出依据。运行证据必须记录执行类型、范围、环境和起止时间；测试执行需提供命令与退出码。`static_analysis` 只能证明其静态检查范围，不能作为 `test_execution` 通过证据。

状态 `PASS`、`FAIL`、`BLOCKED`、`UNKNOWN` 只针对声明中写明的范围。工作流汇总状态按 `FAIL > BLOCKED > UNKNOWN > PASS` 从证据项推导；只有至少一条证据且所有证据均为 PASS 时，汇总状态才能为 PASS。没有证据时为 UNKNOWN。缺少来源、运行记录或版本时标 UNKNOWN；已过 `valid_until` 的 PASS 不可继续使用。局部工作流 PASS 不构成产品放行或风险接受。

## 使用建议

- 单一产出优先路由到现有专业 Skill；仅在用户明确要求跨阶段结果时启动完整 Workflow。
- 阶段交接时保留来源 ID、范围、输入指纹和未知项；不要把推断改写成事实或把计划改写成执行结果。
- 每个结论关联证据及其状态。`UNKNOWN`、`BLOCKED`、`STALE` 和缺失证据不能汇总为 PASS；证据过期或输入变化后重新评估。
- 将分析与外部副作用分开；写仓库、对外发布、删除和最终放行由宿主执行可信的人类审批。
- 先用仓库校验器检查契约，再用目标 Agent 和具体项目材料评测行为；两种结果分别记录。

可从 [完整 PR Quality Review 示例](../../skills/zh/testing-workflows/pr-quality-review/workflow.yaml) 查看阶段依赖和交接字段；中英文包各自独立安装，示例路径用于阅读，不是运行时依赖。

## `run-state.json` 与恢复

本地 CLI 可保存 `NOT_STARTED`、`RUNNING`、`COMPLETED`、`FAILED`、`BLOCKED` 或 `STALE`。Checkpoint 关联 Workflow 版本及包指纹、输入指纹、Commit SHA、阶段状态、证据/产物引用和幂等键。恢复前比较这些值；任一变化即转为 `STALE`，要求重新评估。重复启动同一阶段会被拒绝；中断阶段需人工检查后在新 Run 中处理，不自动重放。写仓库、对外写入、发布、删除和最终放行必须由宿主实施可信的显式授权。

状态迁移：

```text
NOT_STARTED → RUNNING → COMPLETED | FAILED | BLOCKED
中断恢复：RUNNING → BLOCKED（检查副作用后，不自动重放）
任何非终态 → STALE（输入指纹、Commit SHA 或 Workflow 包指纹变化）
```

Schema 校验只能证明记录形状满足契约，不证明宿主真的持久化、恢复或执行了阶段。

本地状态 CLI 的命令、恢复边界和审批记录示例见 [`WORKFLOW_STATE_RUNTIME.md`](./WORKFLOW_STATE_RUNTIME.md)。

## 校验

```bash
python3 scripts/validate_workflow_contracts.py --repo-root . --report /tmp/workflow-contract-report.json
python3 -m unittest scripts.tests.test_validate_workflow_contracts -v
```

报告中的 `PASS` 表示契约与示例校验通过。Skill-up 的 `validate`/`run` 是另一层：前者校验 Eval 配置，后者才运行模型案例。两种证据必须分开记录。
