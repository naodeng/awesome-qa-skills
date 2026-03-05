---
name: requirements-analysis
description: Use this skill when you need to analyze requirements, identify test points, boundaries, dependencies, and risks before test design; triggers include 需求分析 and requirements analysis.
---

# 需求分析（中文版）

**英文版：** 见技能 `requirements-analysis-en`。

提示词见本目录 `prompts/requirements-analysis.md`。

## 何时使用

- 用户提到「需求分析」「requirements analysis」「测试点识别」
- 需要从需求文档中提取测试点
- **触发示例：**「分析这个需求的测试点」「识别需求中的边界条件」

## 输出格式选项

本技能**默认输出为 Markdown**。若需其他格式，请在需求**末尾**明确说明。

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

## 参考文件

- **[prompts/requirements-analysis.md](prompts/requirements-analysis.md)** — 需求分析提示词
- **[output-formats.md](output-formats.md)** — 格式说明

## 代码示例 | Code Examples

1. **需求分析模板（计划中）** - 需求分析示例和模板

## 常见误区 | Common Pitfalls

- ❌ **只看表面功能** → ✅ 深入分析隐含需求和边界条件
- ❌ **忽略非功能需求** → ✅ 关注性能、安全、可用性等
- ❌ **遗漏异常场景** → ✅ 识别所有可能的异常情况
- ❌ **缺少优先级** → ✅ 标记测试点的优先级

## 最佳实践 | Best Practices

### 1. 需求分析框架（5W1H）

```markdown
## What（是什么）
- 功能描述
- 业务目标
- 用户价值

## Who（谁使用）
- 目标用户
- 用户角色
- 权限要求

## When（何时）
- 触发条件
- 时间约束
- 频率要求

## Where（在哪里）
- 使用场景
- 环境要求
- 平台限制

## Why（为什么）
- 业务原因
- 问题解决
- 价值体现

## How（如何实现）
- 实现方式
- 技术方案
- 交互流程
```

### 2. 测试点识别

**测试点类型**：
- 功能测试点
- 界面测试点
- 数据测试点
- 性能测试点
- 安全测试点
- 兼容性测试点

### 3. 边界条件分析

- 输入边界
- 输出边界
- 时间边界
- 数量边界
- 权限边界

## 故障排除 | Troubleshooting

### 问题1：需求不清晰

**解决方案**：
1. 列出疑问点
2. 与产品经理沟通
3. 记录澄清结果
4. 更新需求文档

### 问题2：测试点遗漏

**解决方案**：
使用检查清单：
- [ ] 正常场景
- [ ] 异常场景
- [ ] 边界值
- [ ] 权限验证
- [ ] 数据验证
- [ ] 性能要求
- [ ] 安全要求

**相关技能：** test-case-writing、test-strategy、functional-testing。

## 目标受众

- 在真实项目中执行该测试域工作的 QA 与开发人员
- 需要结构化、可复用测试交付物的测试负责人
- 需要快速生成可落地测试产出的 AI 使用者

## 不适用场景

- 无测试范围上下文的纯线上应急处置
- 需要法律/合规最终裁定但缺少专家复核的决策
- 缺少最小输入（范围、环境、期望行为）的请求

## 关键成功因素

- 先明确范围、环境与验收标准，再生成测试内容
- 生成结果必须结合真实系统约束做二次校验
- 保持产物可追踪（需求 -> 测试点 -> 缺陷 -> 决策）

## 输出模板与解析脚本

- 模板目录：`output-templates/`
  - `template-word.md`（Word 友好结构）
  - `template-excel.tsv`（Excel 可直接粘贴）
  - `template-xmind.md`（XMind 结构化大纲）
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- 解析脚本目录：`scripts/`
  - 解析通用：`parse_output_formats.py`
  - 解析按格式：`parse_word.py`、`parse_excel.py`、`parse_xmind.py`、`parse_json.py`、`parse_csv.py`、`parse_markdown.py`
  - 转换通用：`convert_output_formats.py`
  - 转换按格式：`convert_to_word.py`、`convert_to_excel.py`、`convert_to_xmind.py`、`convert_to_json.py`、`convert_to_csv.py`、`convert_to_markdown.py`
  - 批量转换：`batch_convert_templates.py`（批量输出到 `artifacts/`）

示例：
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
