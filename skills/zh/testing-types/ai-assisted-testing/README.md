# AI 辅助测试

## Skill 介绍

用于让 AI 协助需求分析、测试设计、数据准备、脚本草拟、缺陷归纳或报告整理，并跟踪人工复核、采纳版本、执行证据与成本。AI 产物默认是草稿；业务 oracle、断言、隐私、高风险取舍和发布接受必须由人确认。

## 如何使用

1. 打开当前目录下的 `SKILL.md`，先确认这个技能是否匹配你的任务。
2. 在 AI 工具里调用 `@skill ai-assisted-testing`，再补充任务范围、风险、数据使用限制和期望交付物。
3. 复核 `AIA-##` 发现及来源链；没有真实运行证据的结果保持 `NOT_RUN` 或 `BLOCKED`。
4. 如果有格式要求（如表格、清单、报告），把要求直接写在需求里。

## 一键安装脚本

在仓库根目录执行：

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang zh --skill ai-assisted-testing
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill ai-assisted-testing
```
