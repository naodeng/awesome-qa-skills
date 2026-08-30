<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-08-30-all-testing-skills-audit_EN.md">🇬🇧 English</a></div>

# 全部测试类型 Skill 审计报告

**日期：** 2026-08-30

**审计范围：** `skills/{zh,en}/testing-types/` 下全部 130 个 Skill 包（65 个主题，中英文各一份）

**审计方法：** `skill-review` 九阶段审计、仓库结构与独立性校验、评测 YAML 校验，以及对 k6、Selenium、Appium 等带可执行示例的官方文档核验。

## 执行摘要

**结果：** 通过，但建议在下一次内容维护时处理 1 项 Medium 和 1 项 Low。

| 严重性 | 数量 | 结论 |
| --- | ---: | --- |
| Critical | 0 | 无安全泄露、破坏性执行或无法使用的 Skill 包。 |
| High | 0 | 无阻断安装、调用或核心交付的问题。 |
| Medium | 1 | 一条 k6 速查命令不是当前 CLI 支持的运行方式。 |
| Low | 1 | 一个 Selenium 示例锁定在明显过期的依赖版本。 |

## 已验证通过的项目

- 中英文测试类型目录完全配对：65 个主题、130 个包；目录名、入口、主 Prompt、`agents/openai.yaml` 与 `evals/` 均存在。
- 元数据、独立安装、跨 Skill 链接、完整性与外部快照卫生检查均为 0 findings。
- `skill-up` 静态评测 YAML 校验：156 passed、0 failed（包含本轮范围的 130 个测试类型包）。
- 评测用例覆盖完整输入、信息不完整和风险/边界场景；没有发现 TODO/FIXME 占位符留在用户可执行的入口或主 Prompt 中。评测断言里的 `TODO`/`TBD` 是要求模型显式标记信息缺口，不是待修复内容。
- 抽样核验的 Playwright、Cypress、k6 模块导入与 Appium 的 `AppiumBy` 写法均与官方当前文档兼容。

## 发现

### Medium：k6 “运行特定场景”命令无效

**位置：** `skills/zh/testing-types/performance-testing/quick-start.md:260`

```bash
k6 run --scenario-name my_scenario script.js
```

**证据：** 当前 k6 文档通过脚本 `options.scenarios` 定义场景，并以 `k6 run scenario-example.js` 执行脚本；没有提供 `--scenario-name` 运行参数。若需按名称选择工作负载，应在脚本中用环境变量或配置逻辑显式启用所需场景，而不是把该参数交给 CLI。

**影响：** 读者直接复制该速查命令会失败，且该命令位于常用命令区，误导性较强。

**建议修复：** 移除该命令；替换为“在脚本 `options.scenarios` 中定义场景后执行 `k6 run script.js`”，必要时给出受控环境变量选择场景的脚本示例。

### Low：Selenium 示例的锁定依赖过期

**位置：** `skills/zh/testing-types/automation-testing/examples/selenium-pom-python/requirements.txt:1-6` 及同目录 `README.md:277-281`

**证据：** 示例将 `selenium` 固定为 `4.16.0`、`pytest` 固定为 `7.4.3`。Selenium 官方当前稳定版为 4.48.0，并已由内置 Selenium Manager 处理大多数浏览器驱动；该示例同时保留了较旧的 `webdriver-manager` 依赖。

**影响：** 示例仍可能运行，但会错过当前兼容性与维护改进；新用户也可能误以为必须额外安装第三方 driver manager。

**建议修复：** 在隔离环境实跑后更新到经验证的当前版本范围，并优先采用 Selenium Manager；若保留 `webdriver-manager`，说明其只用于特定受限环境。

## 复核边界与剩余风险

- 本轮对所有包运行了自动结构、元数据、独立性和 YAML 评测校验；对工具类示例做了高风险抽样和官方文档核验，未对每个示例实际启动完整测试环境。
- `examples/` 与 `references/` 是按需资料，不要求逐文件与另一语言逐字镜像；这符合仓库的“Skill 可独立安装”和内部文档不设语言切换的约定，不构成双语缺陷。
- `SKILL.md` frontmatter 的 `description: Use this skill when ...` 是本仓库面向工具发现的既定元数据契约；中文包正文、Prompt 与项目级中文入口仍以中文为主，因此不将其判定为英文泄漏。

## 结论

全部测试类型 Skill 已达到项目当前的结构、双语配对、独立性和静态评测质量门槛。修复上述两项内容维护问题后，可进一步提升新用户复制示例时的可靠性；本轮未直接修改 Skill 内容，以保留审计与修复之间清晰的评审边界。
