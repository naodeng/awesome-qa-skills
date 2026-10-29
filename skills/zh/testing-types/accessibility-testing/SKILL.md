---
name: accessibility-testing
description: Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include 可访问性测试 and accessibility testing.
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

# 可访问性测试（中文版）

**英文版：** 见对应英文技能。

## 何时使用

- 需要在真实项目里处理 accessibility testing 相关任务。
- 需要一份可以直接用于执行、评审或跟进的结果。

## 执行流程

1. 阅读并遵循「按需加载」中的主提示词（覆盖清单、输出结构、质量要求）。
2. 只补充真正影响结果的项目上下文：范围、环境、限制、风险、依赖、期望产出。
3. 信息不全时先给可用初版，并显式标出假设与信息缺口。
4. 默认 Markdown；用户指定其他格式时再切换。

## 领域执行要点

1. 记录项目指定的 WCAG 版本/等级、范围和成功标准 ID；目标未指定时列为缺口，不能自行选等级或声称合规。
2. 建立 成功标准 ID | 用户任务/状态 | 输入方式/辅助技术/版本 | 检查步骤 | 证据类型 | 结果 表。自动扫描、键盘操作、读屏和人工视觉检查分别记录。
3. 键盘检查实际完成导航、打开、操作、关闭并检查焦点去向；读屏检查名称/角色/状态与动态更新。不可达的关键操作按用户任务影响优先。
4. 扫描零发现只能表示扫描范围内未发现；人工失败保留 FAIL，未执行项目保留 NOT_RUN。按准则汇总证据，不将局部扫描升级为整体合规。
## 核心约束

- 按风险/业务影响排优先级，不要平均摊铺。
- 把「已确认事实」和「当前假设」分开写。
- 不要编造用户未提供的接口、字段、环境或根因细节。
- 结果必须可执行：场景具体、有优先级、能指导下一步。

## 按需加载

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 产出前必须阅读并遵循 `prompts/accessibility-testing.md`（最低覆盖清单、输出结构、质量要求）。
- 需要 Excel/CSV/JSON/Word 等格式时：读 `output-formats.md`，并按用户格式要求输出。
- 需要套用现成模板时：读 `output-templates/` 中匹配的模板，不要自创冲突结构。
- 用户要示例或对标现有资产时：读 `examples/` 中相关样例。
- 需要框架规范、排障、报告 schema 等深资料时：只读 `references/` 里与当前问题相关的文件，不要整目录通读。
- 需要格式转换或辅助校验时：优先使用 `scripts/` 中已有脚本，而不是重写一遍。
- 需要评测/回归本 skill 时：使用 `evals/`，并用 skill-up 校验与运行。
- 用户只要最短上手路径时：读 `quick-start.md`。

## 交付前自检

- [ ] 已遵循主提示词的输出结构
- [ ] 最低覆盖关注：范围和目标用户、键盘可操作性、焦点顺序和焦点可见性、读屏语义和标签、标题和区域结构、表单错误和校验反馈、对比度和非颜色提示、图片图标和替代文本…（细节以主提示词为准）
- [ ] 已覆盖最低清单，或标明为何省略
- [ ] 高风险项有明确优先级
- [ ] 未编造用户未提供的细节
- [ ] 假设与信息缺口已标明

## 常见误区

- 范围和上下文都不清楚时，不要假装已经完整可用。
- 不要把所有项写成同等重要。
- 不要跳过假设与信息缺口。
- 不要输出大段与当前工具链无关的空泛理论。
