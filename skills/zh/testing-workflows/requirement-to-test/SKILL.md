---
name: requirement-to-test
description: Use this skill when you need to turn requirements into testable, risk-driven, traceable test design; triggers include requirement-to-test and 需求到测试工作流.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-workflows"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# 需求到测试工作流

英文示例与 FAQ 位于同目录的 `README_EN.md`。

## 何时使用

将需求转成可测试、风险驱动且可追踪的测试设计时使用。

## 执行流程

执行前读取 `prompts/requirement-to-test.md`；按契约检查输入，逐阶段完成分析、保留来源、输出风险和交接。

## 核心约束

只组合已有专业 Skill，不复制分析规则；缺少 Host 安装证据时标 `UNKNOWN`。不把计划或静态分析写成已执行结果；默认只读，对外写入需授权。

## 按需加载

- 主流程：`prompts/requirement-to-test.md`
- 用法和 FAQ：`README.md`
- Eval：`evals/`

## 交付前自检

- [ ] 输入范围和假设明确
- [ ] 阶段交接保留来源、状态和缺口
- [ ] 执行证据与计划分开
- [ ] 下一步和授权边界明确

## 常见误区

不编造输入、不假设依赖已安装、不把建议当作实际执行或批准。
