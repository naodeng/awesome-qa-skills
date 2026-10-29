---
name: ui-test-testcafe
description: Use this skill when you need to design TestCafe UI automation with fixtures, selectors, roles, browser matrix execution, and reports; triggers include TestCafe UI testing, UI automation testing, and ui-test-testcafe.
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

# TestCafe UI 自动化测试

**English version:** see the matching English skill.

## 何时使用

- 需要输出面向 TestCafe UI 自动化测试工作流的测试方案或自动化设计。
- 项目已经使用相关工具，或希望得到可直接落地的工具专项方案。

## 输出格式选项

默认使用 Markdown。除非请求明确要求其他格式，不额外扩展输出格式。

## 如何使用

1. 打开 `prompts/ui-test-testcafe.md`，将其作为主提示词。
2. 补充真实项目上下文：范围、环境、约束、风险、依赖和期望交付物。
3. 如果输入不完整，先返回可用的第一版，并标出缺失信息和假设。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- `prompts/ui-test-testcafe.md`：本技能主提示词。
- `references/framework-spec.md`：工具专项结构和覆盖说明。
- `references/setup-and-ci.md`：安装、执行和 CI 说明。
- `examples/sample-context.md`：示例请求上下文。
- `scripts/run-tests.sh`：轻量本地执行入口。

## 领域执行要点

1. 确认项目TestCafe/Node/browser、原生自动化模式与CI/reporter版本；生成fixture/test/config和现有runner兼容，缺配置保持待确认不推荐隐式升级。
2. 用Role或独立身份初始化隔离会话，账号/业务键同样隔离；异步t动作必须await，Selector/断言采用支持的智能等待而非固定sleep。
3. 核对付款后状态、金额和主体；stub外部边界不能绕过被测UI，正常标题不能代表成功，负对照应使业务断言失败。
4. CLI非0或programmatic runner返回failedCount>0必须使CI失败；reporter自定义不得吞失败，保留截图/控制台/测试ID与cleanup。配置静态可解析和真实执行分别记。

## 常见误区

- 不要在范围模糊且缺少上下文时直接给泛泛方案。
- 不要把所有模块和场景视为同等重要。
- 不要跳过假设和缺失信息说明。

## 最佳实践

- 从 prompt 文件开始，只补充真正影响结果的上下文。
- 输出保持风险驱动，并能直接用于执行或评审。
- 信息不完整时，先给可用版本，再标清缺口。

- 验证生成资产的业务断言、失败传播或隔离时，读取 [evals/fixtures/checkout-app/README.md](evals/fixtures/checkout-app/README.md)，使用本地good/bug/timeout对照；仅在明确运行时执行。
