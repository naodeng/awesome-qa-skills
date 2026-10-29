---
name: agent-failure-recovery-testing
description: Use this skill when you need evidence-bounded failure classification, retry/fallback/escalation, state consistency, user notice, and recovery evidence; triggers include Agent 故障恢复 and Agent failure recovery.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Agent 故障恢复测试（中文版）

## 何时使用

- 需要围绕故障分类、重试/回退/升级、状态一致性、用户通知与恢复证据开展有证据的分析、设计或验证准备。
- 需要评审 Agent、RAG 或 LLM 方案、结果或证据，并形成可执行改进项。
- 输入不完整，但仍需交付带假设、信息缺口和人工决策边界的受限初版。

## 输出格式选项

- 默认输出 Markdown，按领域风险、证据状态、优先级和边界组织。
- 用户要求表格、CSV、JSON 或工单格式时，保留相同的发现字段、证据和决策边界。
- 输出进入自动化流程前，先确认 schema、枚举值、必填项和证据来源。

## 如何使用

1. 先阅读并遵循 `prompts/agent-failure-recovery-testing.md`，包括输入审计、领域覆盖和输出顺序。
2. 提取范围、环境、版本、时间窗口、约束、成功标准和可用证据，重点检查故障分类、重试与回退、升级路径、状态一致性、用户通知。
3. 先区分已确认事实、证据支持的推断、候选建议和 Human 决策，再按风险与证据强度排序。
4. 把高风险项转成前置条件、步骤、预期结果或判断标准、所需证据和验证方法。
5. 信息不足时交付受限初版，明确哪些结论不能成立，不把静态材料写成执行结果。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/agent-failure-recovery-testing.md`；它是本 Skill 的完整执行规范。
- 需要评测时读取 `evals/eval.yaml` 和 `evals/cases/` 下的匹配用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 按项目协议建立 故障 | 写入是否确认 | 可重试性 | 重试/补偿/升级 | 恢复后状态 | 所需证据 表；暂时错误、永久错误和结果不确定分开。
2. 超时不能推出未执行：先以 operation_id/幂等键查已提交副作用，再决定读回结果或安全重试；同键不得产生第二次业务写入。
3. 部分成功按已完成步骤和剩余步骤核对；补偿仅在协议和授权允许时执行，逐步记录补偿结果，失败进入升级。
4. 永久错误停止原样重试并通知责任人。核对恢复前后业务状态、重试次数、用户可见结果与资源；缺日志时恢复仍待验证。
## 核心约束

- 只分析故障分类、重试/回退/升级、状态一致性、用户通知与恢复证据，不替代业务负责人或 Human 的风险接受、例外批准和安全决定。
- 不编造系统行为、字段、模型输出、数据、阈值、根因、执行记录或通过结论。
- 静态设计、计划、文件存在或 dry-run 只能保留原证据状态，不能升级为真实执行证明。
- 证据不足时使用待确认、blocked、unassessed 或 NOT_SCORED，并给出最小验证方法。
- 涉及用户数据、生产或安全时采用最小权限、脱敏数据、mock、dry-run 或隔离环境。

## 交付前自检

- [ ] 已覆盖故障分类、重试与回退、升级路径、状态一致性、用户通知，并为每项记录来源、证据状态和验证方法。
- [ ] 已分开事实、推断、候选建议、信息缺口和 Human 决策。
- [ ] 高风险项有 P0/P1/P2/P3 或等价优先级、责任角色和关闭条件。
- [ ] 未把计划、静态检查或 dry-run 写成测试执行、全部通过或安全批准。
- [ ] 已说明剩余风险、停止/升级条件和下一步。

## 常见误区

- 只列检查点，不说明触发条件、预期关注点、责任角色、关闭条件和证据。
- 把相邻领域的测试或模型工具名当成Agent 故障恢复的完整判断。
- 用未经说明的数字制造伪精确，或把相关性写成因果关系。
- 输入不完整时直接拒绝，或反过来假装结论已经确定。

## 最佳实践

- 从最可能造成用户伤害、业务损失或决策阻塞的路径开始。
- 使用最小可验证实验缩小不确定性，并记录条件、版本、来源和证据。
- 让另一位工程师能够独立安装、执行和复核本 Skill 的产出。
