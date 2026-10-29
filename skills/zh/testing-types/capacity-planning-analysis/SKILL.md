---
name: capacity-planning-analysis
description: Use this skill when you need to assess capacity demand, headroom, constraints, and planning assumptions; triggers include 容量规划分析 and capacity planning analysis.
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

# 容量规划分析（中文版）

## 何时使用

- 需要根据业务负载、资源利用率和增长假设估算容量需求与扩容触发条件。
- 需要对现有方案、结果或证据做风险评审，并形成可执行改进项。
- 输入不完整，但仍需先给出带假设和信息缺口的可用初版。

## 输出格式选项

- 默认输出 Markdown，适合评审、执行和持续补充。
- 用户要求表格、CSV、JSON 或工单格式时，保留同样的风险、证据、优先级和边界字段。
- 若输出会进入自动化流程，先确认字段 schema、枚举值和必填项。

## 如何使用

1. 先阅读并遵循 `prompts/capacity-planning-analysis.md` 的输入、执行规则、最低覆盖清单和输出顺序。
2. 补充真正影响判断的范围、环境、版本、限制、证据和成功标准。
3. 先做输入审计，再区分已确认事实、合理假设和待确认问题。
4. 按风险和证据强度排序，产出可直接执行、评审或验证的结果。
5. 信息不足时不要停在提问：先交付受限初版，并说明哪些结论暂不能成立。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/capacity-planning-analysis.md`；它是本 Skill 的完整执行规范。
- 需要评测或回归本 Skill 时，读取 `evals/eval.yaml` 与匹配的 `evals/cases/` 用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 对每个观测点记录环境/配置/实例数、负载 mix、到达/完成吞吐、延迟分位数、错误率、CPU/内存/队列和时窗；把测量→SLO→容量候选的来源链列出。
2. 仅使用已测 SLO 可接受区间估计；CPU 百分比不能线性换算吞吐，未测点为候选，受下游、饱和与伸缩时延限制。
3. 按项目假设复算扩容等待期积压 = max(0,到达率−已验证服务率)×等待秒数；仅在速率恒定/队列模型适用时使用，并检查积压时延与恢复。
4. 故障余量用失去项目指定实例/依赖后的实际测量或明确条件模型；无故障数据不能宣布容量足够。安全余量、增长、成本及接受条件来自项目。
## 核心约束

- 没有数据时给区间而非伪精确数字
- 明确平均值与峰值
- 容量结论必须关联 SLO 和验证方式
- 不编造输入中不存在的系统行为、字段、数据、指标或根因。
- 关键结论必须关联证据；证据不足时标记为假设并给出验证方法。
- 优先级必须说明业务影响、发生可能性或可探测性依据。

## 交付前自检

- [ ] 已覆盖：峰值与突发、并发和吞吐、资源瓶颈、安全余量、增长情景、故障降级、成本、扩容时效。
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
