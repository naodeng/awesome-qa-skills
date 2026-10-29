---
name: quality-gate-design
description: Use this skill when you need evidence-bounded entry criteria, evidence requirements, owners, and exception paths for a delivery or release gate; triggers include 质量门禁 and quality gate.
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

# 质量门禁设计（中文版）

## 何时使用

- 需要围绕发布或交付入口的准入条件、证据要求、责任人与例外路径开展有证据的分析、设计或验证准备。
- 需要评审现有方案、结果或指标，并形成可执行的改进项。
- 输入不完整，但仍需交付带假设、信息缺口和人工决策边界的受限初版。

## 输出格式选项

- 默认输出 Markdown，按领域风险、证据状态、优先级和边界组织。
- 用户要求表格、CSV、JSON 或工单格式时，保留相同的发现字段、证据和决策边界。
- 输出进入自动化流程前，先确认 schema、枚举值、必填项和证据来源。

## 如何使用

1. 先阅读并遵循 `prompts/quality-gate-design.md`，包括输入审计、领域覆盖和输出顺序。
2. 提取范围、环境、版本、时间窗口、约束、成功标准和可用证据，重点检查门禁目标、准入条件、证据来源、责任角色、例外与回滚。
3. 先区分已确认事实、证据支持的推断、候选建议和 Human 决策，再按风险与证据强度排序。
4. 把高风险项转成前置条件、步骤、预期结果或判断标准、所需证据和验证方法。
5. 信息不足时交付受限初版，明确哪些结论不能成立，不把静态材料写成执行结果。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/quality-gate-design.md`；它是本 Skill 的完整执行规范。
- 需要评测时读取 `evals/eval.yaml` 和 `evals/cases/` 下的匹配用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 为每个门槛记录义务、输入/版本/时效、比较符、PASS/FAIL、不可执行BLOCKED、缺证据或无法判断UNKNOWN的真值表；没有记录不得视为PASS。
2. 聚合规则由项目指定：必要门槛FAIL优先，无法验证按fail-closed停止；UNKNOWN/BLOCKED保持原因而不是折算失败率。所有必要门槛有新鲜有效PASS才可推荐通过。
3. 例外单列义务范围、授权人、理由、批准证据、有效期、补偿控制与撤销条件；过期/越界/无授权不生效，不改写原始FAIL。
4. 明确门禁触发、负责人、重新验证和回滚/停止条件；设计、静态证据判定与实际流水线实施分别报告，缺规则提交待Human决策。

## 核心约束

- 只分析发布或交付入口的准入条件、证据要求、责任人与例外路径，不替代业务负责人或 Human 的风险接受、例外批准和发布决定。
- 不编造系统行为、字段、指标、阈值、数据、根因、执行记录或通过结论。
- 静态设计、计划、文件存在或 dry-run 只能保留原证据状态，不能升级为真实执行证明。
- 证据不足时使用待确认、blocked、unassessed 或 NOT_SCORED，并给出最小验证方法。
- 涉及生产、隐私或安全时采用最小权限、脱敏数据、mock、dry-run 或隔离环境。

## 交付前自检

- [ ] 已覆盖门禁目标、准入条件、证据来源、责任角色、例外与回滚，并为每项记录来源、证据状态和验证方法。
- [ ] 已分开事实、推断、候选建议、信息缺口和 Human 决策。
- [ ] 高风险项有 P0/P1/P2/P3 或等价优先级、责任角色和关闭条件。
- [ ] 未把计划、静态检查或 dry-run 写成测试执行、全部通过或发布批准。
- [ ] 已说明剩余风险、停止/升级条件和下一步。

## 常见误区

- 只列检查点，不说明触发条件、预期关注点、责任角色、关闭条件和证据。
- 把相邻领域的指标或工具名当成质量门禁的完整判断。
- 用未经说明的数字制造伪精确，或把相关性写成因果关系。
- 输入不完整时直接拒绝，或反过来假装结论已经确定。

## 最佳实践

- 从最可能造成业务损失、质量回退或决策阻塞的路径开始。
- 使用最小可验证实验缩小不确定性，并记录条件、版本、来源和证据。
- 让另一位工程师能够独立安装、执行和复核本 Skill 的产出。
