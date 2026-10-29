---
name: requirement-gap-analysis
description: Use this skill when you need to find missing, conflicting, or untestable requirement information; triggers include 需求缺口分析 and requirement gap analysis.
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

# 需求缺口分析（中文版）

## 何时使用

- 需要发现需求中的歧义、遗漏、冲突、不可验证项和跨角色依赖缺口。
- 需要对现有方案、结果或证据做风险评审，并形成可执行改进项。
- 输入不完整，但仍需先给出带假设和信息缺口的可用初版。

## 输出格式选项

- 默认输出 Markdown，适合评审、执行和持续补充。
- 用户要求表格、CSV、JSON 或工单格式时，保留同样的风险、证据、优先级和边界字段。
- 若输出会进入自动化流程，先确认字段 schema、枚举值和必填项。

## 如何使用

1. 先阅读并遵循 `prompts/requirement-gap-analysis.md` 的输入、执行规则、最低覆盖清单和输出顺序。
2. 补充真正影响判断的范围、环境、版本、限制、证据和成功标准。
3. 先做输入审计，再区分已确认事实、合理假设和待确认问题。
4. 按风险和证据强度排序，产出可直接执行、评审或验证的结果。
5. 信息不足时不要停在提问：先交付受限初版，并说明哪些结论暂不能成立。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/requirement-gap-analysis.md`；它是本 Skill 的完整执行规范。
- 需要评测或回归本 Skill 时，读取 `evals/eval.yaml` 与匹配的 `evals/cases/` 用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 以范围/版本和适用角色、状态、规则、异常、关闭条件建立需求清单；每项注明来源与已提供材料覆盖，不把通常清单强套到不适用产品。
2. 分列MISSING_RULE（确认相关但规则未定义）、MISSING_MATERIAL（引用资料未提供）、CONFLICT（已提供规则冲突）、N/A（有范围理由不适用）与COMPLETE。
3. 缺口给原需求ID、缺失内容、影响场景、阻塞程度、责任人和最小澄清；空文档或未见字段不自动证明产品缺陷。
4. 关闭需权威补充规则/来源版本与可测试预期，并更新追踪；建议填法未经批准保持proposal，定义充分的正确对照不得报缺口。

## 核心约束

- 不要替干系人填业务决策
- 区分事实、推断和问题
- 优先提出会导致返工或事故的缺口
- 不编造输入中不存在的系统行为、字段、数据、指标或根因。
- 关键结论必须关联证据；证据不足时标记为假设并给出验证方法。
- 优先级必须说明业务影响、发生可能性或可探测性依据。

## 交付前自检

- [ ] 已覆盖：目标与范围、角色、规则、状态、异常、数据、权限、依赖、非功能、验收与回滚。
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
