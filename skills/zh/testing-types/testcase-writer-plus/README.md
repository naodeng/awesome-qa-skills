# 测试用例编写增强版

## Skill 介绍

需要基于多来源材料编写更完整、更有优先级的测试用例；需要比基础版更强的追踪关系和风险意识。

## 如何使用

1. 打开当前目录下的 `SKILL.md`，先确认这个技能是否匹配你的任务。
2. 在 AI 工具里调用 `@skill testcase-writer-plus`，再补充你的真实业务背景和目标。
3. 如果你有格式要求（如表格、清单、报告），把要求直接写在需求里。

## 一键安装脚本

在仓库根目录执行：

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang zh --skill testcase-writer-plus
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill testcase-writer-plus
```
