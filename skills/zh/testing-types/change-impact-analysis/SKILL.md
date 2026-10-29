---
name: change-impact-analysis
description: Use this skill when you need to analyze how a code, configuration, or requirement change affects quality scope; triggers include 变更影响分析 and change impact analysis.
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

# 变更影响分析（中文版）

## 何时使用

- 需要从代码、配置、数据和依赖变更识别受影响能力、回归范围与发布风险。
- 需要对现有方案、结果或证据做风险评审，并形成可执行改进项。
- 输入不完整，但仍需先给出带假设和信息缺口的可用初版。

## 输出格式选项

- 默认输出 Markdown，适合评审、执行和持续补充。
- 用户要求表格、CSV、JSON 或工单格式时，保留同样的风险、证据、优先级和边界字段。
- 若输出会进入自动化流程，先确认字段 schema、枚举值和必填项。

## 如何使用

1. 先阅读并遵循 `prompts/change-impact-analysis.md` 的输入、执行规则、最低覆盖清单和输出顺序。
2. 补充真正影响判断的范围、环境、版本、限制、证据和成功标准。
3. 先做输入审计，再区分已确认事实、合理假设和待确认问题。
4. 按风险和证据强度排序，产出可直接执行、评审或验证的结果。
5. 信息不足时不要停在提问：先交付受限初版，并说明哪些结论暂不能成立。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/change-impact-analysis.md`；它是本 Skill 的完整执行规范。
- 需要评测或回归本 Skill 时，读取 `evals/eval.yaml` 与匹配的 `evals/cases/` 用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 固定变更版本及范围，输出 changed 文件/符号/配置→dependent→业务义务→test ID 的带类型证据图；每条边记录来源、版本与 confirmed/candidate/unknown。
2. 遍历直接和传递消费者，去重循环；只有契约隔离或已证明无消费者边才可停止，记录停止依据，不能以目录边界截断。
3. 动态注册、运行时配置或未追踪依赖保持 unknown；按风险增加消费者契约/集成验证候选，不把没有映射当无影响。
4. 输出纳入/排除理由、最小验证、残余风险及追加范围触发；本 Skill 可分析代码、数据、配置等变更，PR 专项另保留 base/head 与 diff 身份。

## 核心约束

- 区分已证实影响与推测影响
- 不要只按改动文件选测试
- 无法追踪的依赖要显式标为风险
- 不编造输入中不存在的系统行为、字段、数据、指标或根因。
- 关键结论必须关联证据；证据不足时标记为假设并给出验证方法。
- 优先级必须说明业务影响、发生可能性或可探测性依据。

## 交付前自检

- [ ] 已覆盖：直接影响、传递影响、数据兼容、接口契约、权限、运行时依赖、回滚、可观测性。
- [ ] 已区分事实、假设、缺口和建议。
- [ ] 高风险项有明确优先级、证据、负责人或下一步。
- [ ] 输出包含可验证的判断标准，而非泛泛而谈。
- [ ] 未执行未经授权的生产写操作或破坏性动作。

## 常见误区

- 只列检查点，不说明输入条件、预期结果或证据。
- 把所有事项都标为高优先级，失去取舍价值。
- 用工具名或通用理论替代领域判断。
- 输入不完整时直接拒绝，或反过来假装结论已经确定。

## 最佳实践

- 从最可能造成业务损失、安全问题或发布阻塞的路径开始。
- 用最小可验证实验缩小不确定性，并记录复现条件。
- 让输出能够被另一位工程师直接执行和复核。
