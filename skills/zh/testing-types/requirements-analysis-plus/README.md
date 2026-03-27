# 需求分析增强版

## Skill 介绍

需要基于多份材料做更深入的需求分析；需要比基础版更强的冲突检查、优先级和追问。

## 如何使用

1. 打开当前目录下的 `SKILL.md`，先确认这个技能是否匹配你的任务。
2. 在 AI 工具里调用 `@skill requirements-analysis-plus`，再补充你的真实业务背景和目标。
3. 如果你有格式要求（如表格、清单、报告），把要求直接写在需求里。

## 一键安装脚本

在仓库根目录执行：

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang zh --skill requirements-analysis-plus
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill requirements-analysis-plus
```
