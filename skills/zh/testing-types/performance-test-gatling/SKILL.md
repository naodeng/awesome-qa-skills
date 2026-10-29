---
name: performance-test-gatling
description: Use this skill when you need Gatling performance scope, simulations, or runnable entry points; triggers include Gatling、Gatling 性能测试 and Gatling simulation.
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

# 性能测试（Gatling）（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要把性能测试结果落到 Gatling 结构里。
- 项目已经在用 Gatling，或希望输出直接适配 Gatling。

## 执行流程

1. 阅读并遵循「按需加载」中的主提示词（覆盖清单、输出结构、质量要求）。
2. 只补充真正影响结果的项目上下文：范围、环境、限制、风险、依赖、期望产出。
3. 信息不全时先给可用初版，并显式标出假设与信息缺口。
4. 默认 Markdown；用户指定其他格式时再切换。

## 领域执行要点

1. 先读取项目 Gatling/插件/JDK 与 Java/Scala/Kotlin DSL 版本，沿用已有布局；选定同一 DSL 的 injection 与 assertion API，不能混用。生成资产先用项目构建的离线 test-compile 验证，依赖未缓存则标 BLOCKED 而非编译通过。
2. 开放模型控制用户到达率，只有每用户单请求且无额外循环/重试时才与目标 RPS 一一对应；封闭模型控制并发，RPS 要从实际请求数/时窗核对。
3. feeder 的总消费数按每用户/每循环 feed 次数复算；queue 耗尽须可见失败，circular 只在项目允许重复数据时使用，身份/业务键不冲突。
4. 门槛来自项目并使用版本支持的 assertion API，缺门槛输出未配置骨架而不放入自定500ms/1%数值；编译、负载达成和SLO通过分别记证据。

## 核心约束

- 按风险/业务影响排优先级，不要平均摊铺。
- 把「已确认事实」和「当前假设」分开写；无 SLA/无流量时所有数字标「假设」并给待确认清单。
- 不要编造用户未提供的接口、字段、环境或根因细节；密钥只用占位符 / 环境变量，禁止真实 token。
- 结果必须可执行：场景具体、有优先级、能指导下一步。
- 默认只选最关键的 1～2 类性能场景，不要默认基线/负载/压力/尖峰/稳定性全做。

## 按需加载

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 产出前必须阅读并遵循 `prompts/performance-test-gatling.md`（最低覆盖清单、输出结构、质量要求）。
- 需要套用现成模板时：读 `output-templates/` 中匹配的模板，不要自创冲突结构。
- 用户要示例或对标现有资产时：读 `examples/` 中相关样例。
- 需要框架规范、排障、报告 schema 等深资料时：只读 `references/` 里与当前问题相关的文件，不要整目录通读。
- 需要格式转换或辅助校验时：优先使用 `scripts/` 中已有脚本，而不是重写一遍。
- 需要评测/回归本 skill 时：使用 `evals/`，并用 skill-up 校验与运行。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 最低覆盖关注：目标场景、负载模型、数据或 feeder 需求、爬坡方式、阈值、环境和监控、重点瓶颈、结果汇报需求…（细节以主提示词为准）
- [ ] 已覆盖最低清单，或标明为何省略
- [ ] 高风险项有明确优先级
- [ ] 未编造用户未提供的细节
- [ ] 假设与信息缺口已标明

## 常见误区

- 范围和上下文都不清楚时，不要假装已经完整可用。
- 不要把所有项写成同等重要。
- 不要跳过假设与信息缺口。
- 不要输出大段与当前工具链无关的空泛理论。

- 校验DSL/JMX资产与数据消费边界时，读取 [evals/fixtures/java-dsl/README.md](evals/fixtures/java-dsl/README.md)；示例仅本地校准，项目门槛未提供时不得宣布验收。
