---
name: ui-test-playwright
description: Use this skill when you need to design Playwright Test suites with fixtures, projects, traces, screenshots, API plus UI coverage, and CI reporting; triggers include Playwright UI testing, UI automation testing, and ui-test-playwright.
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

# Playwright UI 自动化测试

**English version:** see the matching English skill.

## 何时使用

- 需要输出面向 Playwright UI 自动化测试工作流的测试方案或自动化设计。
- 项目已经使用相关工具，或希望得到可直接落地的工具专项方案。

## 输出格式选项

默认使用 Markdown。除非请求明确要求其他格式，不额外扩展输出格式。

## 如何使用

1. 打开 `prompts/ui-test-playwright.md`，将其作为主提示词。
2. 补充真实项目上下文：范围、环境、约束、风险、依赖和期望交付物。
3. 如果输入不完整，先返回可用的第一版，并标出缺失信息和假设。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- `prompts/ui-test-playwright.md`：本技能主提示词。
- `references/framework-spec.md`：工具专项结构和覆盖说明。
- `references/setup-and-ci.md`：安装、执行和 CI 说明。
- `examples/sample-context.md`：示例请求上下文。
- `scripts/run-tests.sh`：轻量本地执行入口。

## 领域执行要点

1. 固定项目Playwright/Node/browser版本、projects/fixtures与配置；沿用真实入口，记录测试ID、commit、worker/project和环境，未兼容配置先诊断不擅自换框架。
2. 优先role/name/testid等稳定语义定位，执行后以auto-retrying assertion核对订单/账务/状态与主体；页面标题/URL只满足相应导航义务，不能替代付款成功。
3. 每worker独立browser context、storage state/账号与业务键，禁止共享会冲突的数据；同浏览器不同context仍须核对服务端账号隔离，teardown逆依赖清理。
4. 用错误业务状态和并行A/B对照验证断言敏感性；失败保留trace/screenshot/日志与非0 runner/CI，retry首失败仍可见。生成资产、实际browser运行与业务验收分别报告。

## 常见误区

- 不要在范围模糊且缺少上下文时直接给泛泛方案。
- 不要把所有模块和场景视为同等重要。
- 不要跳过假设和缺失信息说明。

## 最佳实践

- 从 prompt 文件开始，只补充真正影响结果的上下文。
- 输出保持风险驱动，并能直接用于执行或评审。
- 信息不完整时，先给可用版本，再标清缺口。

- 验证生成资产的业务断言、失败传播或隔离时，读取 [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md)，使用本地good/bug/timeout对照；仅在明确运行时执行。
