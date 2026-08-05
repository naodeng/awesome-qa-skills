# 代码审查

## Skill 介绍

需要审查 PR / Diff，按风险分级给出可落地修复建议；适合合入前拦截逻辑、安全、资损与可维护性缺陷。

## 如何使用

1. 打开当前目录下的 `SKILL.md`，先确认这个技能是否匹配你的任务。
2. 在 AI 工具里调用 `@skill code-review`，再补充 Diff、业务目标、技术栈与上下游依赖。
3. 如果你有格式要求（如表格、清单、报告），把要求直接写在需求里。

## 一键安装脚本

在仓库根目录执行：

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang zh --skill code-review
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill code-review
```
