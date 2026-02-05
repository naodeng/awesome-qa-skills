---
name: daily-testing-workflow
description: Guides QA engineers through daily testing activities—morning review, test case creation, automation, exploratory testing, bug reporting, and end-of-day wrap-up. Use when planning or executing day-to-day testing, daily test routines, or when the user asks about 日常测试工作流程 or daily testing workflow.
---

本文件为中文版。**英文版：** 见技能 `daily-testing-workflow-en`。

# 日常测试工作流程

为 QA 工程师提供每日测试活动的工作流指引。基于 [awesome-qa-prompt](https://github.com/awesome-qa-prompt) 工作流内容。

## 何时使用

- 用户提到「日常测试」「每日测试」「daily testing」「今日测试计划」
- 需要规划或执行一天的测试活动
- **触发示例：**「帮我安排今日测试」或「日常 QA 流程怎么走」

---

## 早晨例行（5–25 分钟）

1. **审查测试计划（5–10 分钟）**：需求分析 + 测试策略 → 审查当日用户故事、优先级、阻碍。
2. **设置测试环境（10–15 分钟）**：自动化测试 + 测试策略 → 验证环境、准备数据、更新本地自动化。

## 测试用例创建（30–60 分钟）

- **新功能**：测试用例编写 → 需求分析（边界值）→ 功能测试检查清单 → 记录到测试管理工具。
- **缺陷修复**：功能测试回归 → 验证修复用例 → 防回归用例。

## 测试自动化（1–2 小时）

- **新测试**：Selenium/Playwright 用自动化测试提示词，API 用 API 测试；生成 → 审查 → 本地运行 → 提交。
- **维护**：自动化测试维护策略 + AI 辅助测试；修不稳定用例、更新选择器、重构重复代码。

## 探索性测试（30–45 分钟）

手动测试探索性场景 + 章程；限时 60–90 分钟；记录发现与缺陷。章程含：任务、持续时间、区域、启发式（SFDPOT、FEW HICCUPS）。

## 缺陷上报（15–30 分钟）

缺陷上报模板 → 标题、重现步骤、预期 vs 实际、环境、截图/日志 → 记录到问题跟踪器。

## 可视化与 E2E（可选，30 分钟–2 小时）

- 可视化：可访问性测试 + 视觉回归（Percy/Applitools/BackstopJS）。
- E2E：功能测试端到端；关键旅程（登录→购买、注册→首次操作）。

## 下午审查（约 30 分钟）

CI/CD 结果、失败用例、报告；测试报告 + 测试策略 → 覆盖率、缺陷指标、质量仪表板；团队同步。

## 每日结束（约 15 分钟）

提交代码、更新文档、记录时间、更新任务、规划明日；可选分享与 wiki。

## 如何使用本技能中的提示词

执行某一步时：1）查 [reference.md](reference.md) 得到该步骤对应的提示词文件名；2）打开本目录 `prompts/` 下该文件；3）将提示词内容与用户当前上下文（需求、环境、待测项）结合后与 AI 协同执行。

## 常见误区

- ❌ 跳过早晨审查直接写用例 → ✅ 先明确当日故事与优先级，再写用例
- ❌ 探索性测试无章程、无时间盒 → ✅ 使用手动测试提示词写章程，限时 60–90 分钟
- ❌ 缺陷只口头描述不落单 → ✅ 用缺陷上报提示词生成标题、步骤、预期 vs 实际、环境

## 最佳实践

- 早晨先看 [reference.md](reference.md) 再选「审查」「环境」对应提示词
- 新功能先做需求分析/边界值，再写具体用例
- 自动化脚本生成后务必本地跑通再提交
- 下午审查用测试报告 + 测试策略做覆盖率与缺陷指标

## 问题应对

- 流水线失败：检查自动化/CI → 调试 → 修复重跑。
- 不稳定测试：维护策略 + 等待 + 重试。
- 被阻塞：记录阻碍、替代区域、测试策略重排优先级。

## 参考文件

- **[reference.md](reference.md)** — 步骤与提示词文件对照表
- **prompts/** — 本工作流所需中文提示词（每步打开对应 `.md` 与上下文结合使用）

**相关技能**：sprint-testing-workflow、release-testing-workflow。
