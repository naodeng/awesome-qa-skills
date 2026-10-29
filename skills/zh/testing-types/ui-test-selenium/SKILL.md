---
name: ui-test-selenium
description: Use this skill when you need to design Selenium WebDriver UI automation plans with stable locators, waits, Page Objects, Grid, and CI execution; triggers include Selenium UI testing, UI automation testing, and ui-test-selenium.
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

# Selenium UI 自动化测试

**English version:** see the matching English skill.

## 何时使用

- 需要输出面向 Selenium UI 自动化测试工作流的测试方案或自动化设计。
- 项目已经使用相关工具，或希望得到可直接落地的工具专项方案。

## 输出格式选项

默认使用 Markdown。除非请求明确要求其他格式，不额外扩展输出格式。

## 如何使用

1. 打开 `prompts/ui-test-selenium.md`，将其作为主提示词。
2. 补充真实项目上下文：范围、环境、约束、风险、依赖和期望交付物。
3. 如果输入不完整，先返回可用的第一版，并标出缺失信息和假设。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- `prompts/ui-test-selenium.md`：本技能主提示词。
- `references/framework-spec.md`：工具专项结构和覆盖说明。
- `references/setup-and-ci.md`：安装、执行和 CI 说明。
- `examples/sample-context.md`：示例请求上下文。
- `scripts/run-tests.sh`：轻量本地执行入口。

## 领域执行要点

1. 固定项目Selenium/binding/browser/driver/Grid版本、capabilities和runner，生成兼容配置与POM；未提供Grid不自建拓扑，版本冲突先诊断。
2. 显式等待可观察条件（元素可交互、业务状态/窗口/URL达成），区分presence/visibility/业务ready；不混用implicit/explicit或以固定sleep修复所有时序。
3. rerender导致stale时依稳定locator重新查找并等待新状态，有限重试按项目策略；不能盲目重放付款动作引入重复效果。
4. 每并行session独立账号/业务键；try/finally driver.quit，失败留截图/日志/Grid session与原错误；重新渲染、业务失败、异常退出对照都需检查资源和失败传播。

## 常见误区

- 不要在范围模糊且缺少上下文时直接给泛泛方案。
- 不要把所有模块和场景视为同等重要。
- 不要跳过假设和缺失信息说明。

## 最佳实践

- 从 prompt 文件开始，只补充真正影响结果的上下文。
- 输出保持风险驱动，并能直接用于执行或评审。
- 信息不完整时，先给可用版本，再标清缺口。

- 验证生成资产的业务断言、失败传播或隔离时，读取 [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md)，使用本地good/bug/timeout对照；仅在明确运行时执行。
