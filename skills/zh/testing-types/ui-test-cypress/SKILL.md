---
name: ui-test-cypress
description: Use this skill when you need to design Cypress e2e and component testing plans with commands, fixtures, network stubbing, and CI reporting; triggers include Cypress UI testing, UI automation testing, and ui-test-cypress.
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

# Cypress UI 自动化测试

**English version:** see the matching English skill.

## 何时使用

- 需要输出面向 Cypress UI 自动化测试工作流的测试方案或自动化设计。
- 项目已经使用相关工具，或希望得到可直接落地的工具专项方案。

## 输出格式选项

默认使用 Markdown。除非请求明确要求其他格式，不额外扩展输出格式。

## 如何使用

1. 打开 `prompts/ui-test-cypress.md`，将其作为主提示词。
2. 补充真实项目上下文：范围、环境、约束、风险、依赖和期望交付物。
3. 如果输入不完整，先返回可用的第一版，并标出缺失信息和假设。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- `prompts/ui-test-cypress.md`：本技能主提示词。
- `references/framework-spec.md`：工具专项结构和覆盖说明。
- `references/setup-and-ci.md`：安装、执行和 CI 说明。
- `examples/sample-context.md`：示例请求上下文。
- `scripts/run-tests.sh`：轻量本地执行入口。

## 领域执行要点

1. 从项目lockfile/config确认Cypress、Node和浏览器版本及component/E2E边界；按该版本生成配置、custom command、spec与CI命令，不默认升级或混用旧配置。
2. 保留真实页面/组件与业务逻辑，cy.intercept只替换已确认外部边界；仅验证stub回包不足以证明真实后置条件。明确fixture数据与session隔离/注销。
3. 区分可重试query/assertion与执行一次的动作及整个test重试；等待以别名请求/可观察状态而不是sleep，重试不能掩盖首失败或重复副作用。
4. 最小应用正/负对照核对付款后订单状态/金额/主体；标题正常但业务错误必须断言失败且CI非0。记录截图/视频/原失败、teardown与真实运行证据，文件存在不等于通过。

## 常见误区

- 不要在范围模糊且缺少上下文时直接给泛泛方案。
- 不要把所有模块和场景视为同等重要。
- 不要跳过假设和缺失信息说明。

## 最佳实践

- 从 prompt 文件开始，只补充真正影响结果的上下文。
- 输出保持风险驱动，并能直接用于执行或评审。
- 信息不完整时，先给可用版本，再标清缺口。

- 验证生成资产的业务断言、失败传播或隔离时，读取 [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md)，使用本地good/bug/timeout对照；仅在明确运行时执行。
