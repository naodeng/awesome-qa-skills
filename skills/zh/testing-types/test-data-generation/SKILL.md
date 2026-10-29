---
name: test-data-generation
description: Use this skill when you need to design safe, representative test data from stated constraints; triggers include 测试数据生成 and test data generation.
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

# 测试数据生成（中文版）

## 何时使用

- 需要设计覆盖业务规则、边界、组合和隐私约束的可复用测试数据集。
- 需要对现有方案、结果或证据做风险评审，并形成可执行改进项。
- 输入不完整，但仍需先给出带假设和信息缺口的可用初版。

## 输出格式选项

- 默认输出 Markdown，适合评审、执行和持续补充。
- 用户要求表格、CSV、JSON 或工单格式时，保留同样的风险、证据、优先级和边界字段。
- 若输出会进入自动化流程，先确认字段 schema、枚举值和必填项。

## 如何使用

1. 先阅读并遵循 `prompts/test-data-generation.md` 的输入、执行规则、最低覆盖清单和输出顺序。
2. 补充真正影响判断的范围、环境、版本、限制、证据和成功标准。
3. 先做输入审计，再区分已确认事实、合理假设和待确认问题。
4. 按风险和证据强度排序，产出可直接执行、评审或验证的结果。
5. 信息不足时不要停在提问：先交付受限初版，并说明哪些结论暂不能成立。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/test-data-generation.md`；它是本 Skill 的完整执行规范。
- 需要评测或回归本 Skill 时，读取 `evals/eval.yaml` 与匹配的 `evals/cases/` 用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 从已提供schema、实体外键、唯一约束、状态关系与场景预期派生数据组；固定种子/生成器版本，缺规则保留UNKNOWN，不自动发明字段或真实用户。
2. 分开有效happy/boundary数据与定向无效数据，每组注明改变的约束、预期拒绝/允许和不受影响的关系；无效数据不能悄悄进入正常流程组。
3. 实际交付脱敏样本及验证：唯一性、外键存在、字段类型/范围、状态关联、可重复输出；重跑相同seed应得到相同数据身份而非只写可复现建议。
4. 使用隔离ID/命名空间，保留来源许可、个人数据限制和清理逆依赖顺序；缺授权不抓真实个人资料，不把生成样本当真实业务代表性证明。

## 核心约束

- 不得使用真实个人敏感数据
- 区分合成、脱敏和生产镜像
- 生成数据必须可重复并可清理
- 不编造输入中不存在的系统行为、字段、数据、指标或根因。
- 关键结论必须关联证据；证据不足时标记为假设并给出验证方法。
- 优先级必须说明业务影响、发生可能性或可探测性依据。

## 交付前自检

- [ ] 已覆盖：有效与无效、边界、等价类、组合、关联完整性、状态、角色、本地化、隐私、清理。
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
