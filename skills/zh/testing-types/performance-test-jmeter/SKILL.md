---
name: performance-test-jmeter
description: Use this skill when you need to design JMeter test plans with Thread Groups, samplers, data sets, assertions, timers, CLI runs, and HTML reports; triggers include JMeter performance testing, performance testing, and performance-test-jmeter.
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

# JMeter 性能测试

**English version:** see the matching English skill.

## 何时使用

- 需要输出面向 JMeter 性能测试工作流的测试方案或自动化设计。
- 项目已经使用相关工具，或希望得到可直接落地的工具专项方案。

## 输出格式选项

默认使用 Markdown。除非请求明确要求其他格式，不额外扩展输出格式。

## 如何使用

1. 打开 `prompts/performance-test-jmeter.md`，将其作为主提示词。
2. 补充真实项目上下文：范围、环境、约束、风险、依赖和期望交付物。
3. 如果输入不完整，先返回可用的第一版，并标出缺失信息和假设。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- `prompts/performance-test-jmeter.md`：本技能主提示词。
- `references/framework-spec.md`：工具专项结构和覆盖说明。
- `references/setup-and-ci.md`：安装、执行和 CI 说明。
- `examples/sample-context.md`：示例请求上下文。
- `scripts/run-tests.sh`：轻量本地执行入口。

## 领域执行要点

1. 确认项目 JMeter/JDK/插件与 JMX版本，逐个核对 TestPlan/ThreadGroup/Sampler 与相邻 hashTree、变量和属性；XML可解析只证明结构，不等于JMeter可执行或SLO通过。
2. 标准ThreadGroup控制闭环线程数；目标RPS需明确think time/timer、吞吐控制器或已安装到达率插件，记录实际吞吐和请求数，不能从线程数直接推出RPS。
3. CSV Data Set记录文件路径、编码、列、共享模式、recycle/stopThread；按循环与线程复算数据消费，分布式每injector的数据、插件、网络和负载分担独立核对。
4. 在授权环境用non-GUI入口保存JTL与日志，分别检查业务断言、时延/错误门槛及exit/CI传播；门槛未给保持UNKNOWN，失败样本不能被HTML报告或进程0掩盖。

## 常见误区

- 不要在范围模糊且缺少上下文时直接给泛泛方案。
- 不要把所有模块和场景视为同等重要。
- 不要跳过假设和缺失信息说明。

## 最佳实践

- 从 prompt 文件开始，只补充真正影响结果的上下文。
- 输出保持风险驱动，并能直接用于执行或评审。
- 信息不完整时，先给可用版本，再标清缺口。

- 校验DSL/JMX资产与数据消费边界时，读取 [evals/fixtures/jmx/README.md](evals/fixtures/jmx/README.md)；示例仅本地校准，项目门槛未提供时不得宣布验收。
