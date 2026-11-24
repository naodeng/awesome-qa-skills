# 测试报告

## Skill 介绍

用于汇总测试范围、质量状态、风险、缺陷和下一步。如果报告包含 AI 效果或模型评测结论，还要记录模型、Prompt、数据集、judge、run、采样、token 成本、评估者和执行状态；缺模型版本或 run ID 时将 AI 效果标为 `UNKNOWN`。

## 如何使用

1. 打开当前目录下的 `SKILL.md`，先确认这个技能是否匹配你的任务。
2. 在 AI 工具里调用 `@skill test-reporting`，再补充你的真实业务背景和目标。
3. 如果你有格式要求（如表格、清单、报告），把要求直接写在需求里。

## 一键安装脚本

在仓库根目录执行：

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang zh --skill test-reporting
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill test-reporting
```
