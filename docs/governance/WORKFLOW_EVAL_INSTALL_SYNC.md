<div align="right"><strong>🇨🇳 中文</strong> | <a href="./WORKFLOW_EVAL_INSTALL_SYNC_EN.md">🇬🇧 English</a></div>

# Workflow / Eval / 安装同步清单

本清单把当前 10 个跨阶段 Workflow 的物理路径、双语包、最低 Eval 工件和安装入口放在同一处核对。它是文档与结构证据，不代表 Workflow 已在真实项目运行。

## 10 个 Workflow

| Workflow | 中文路径 | English 路径 | Eval 结构 |
| --- | --- | --- | --- |
| `daily-testing-workflow` | `skills/zh/testing-workflows/daily-testing-workflow` | `skills/en/testing-workflows/daily-testing-workflow` | `eval.yaml` + 三类 case |
| `discover-testing` | `skills/zh/testing-workflows/discover-testing` | `skills/en/testing-workflows/discover-testing` | `eval.yaml` + 三类 case |
| `multi-role-quality-synthesis` | `skills/zh/testing-workflows/multi-role-quality-synthesis` | `skills/en/testing-workflows/multi-role-quality-synthesis` | `eval.yaml` + 三类 case |
| `product-quality-perspective` | `skills/zh/testing-workflows/product-quality-perspective` | `skills/en/testing-workflows/product-quality-perspective` | `eval.yaml` + 三类 case |
| `project-delivery-perspective` | `skills/zh/testing-workflows/project-delivery-perspective` | `skills/en/testing-workflows/project-delivery-perspective` | `eval.yaml` + 三类 case |
| `qa-quality-perspective` | `skills/zh/testing-workflows/qa-quality-perspective` | `skills/en/testing-workflows/qa-quality-perspective` | `eval.yaml` + 三类 case |
| `release-testing-workflow` | `skills/zh/testing-workflows/release-testing-workflow` | `skills/en/testing-workflows/release-testing-workflow` | `eval.yaml` + 三类 case |
| `sprint-testing-workflow` | `skills/zh/testing-workflows/sprint-testing-workflow` | `skills/en/testing-workflows/sprint-testing-workflow` | `eval.yaml` + 三类 case |
| `technical-quality-perspective` | `skills/zh/testing-workflows/technical-quality-perspective` | `skills/en/testing-workflows/technical-quality-perspective` | `eval.yaml` + 三类 case |
| `ux-quality-perspective` | `skills/zh/testing-workflows/ux-quality-perspective` | `skills/en/testing-workflows/ux-quality-perspective` | `eval.yaml` + 三类 case |

## 安装入口

```bash
# macOS / Linux
bash scripts/install-skills-mac.sh --tool codex --lang zh
bash scripts/install-skills-mac.sh --tool codex --lang en --dry-run

# Windows
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh

# npx skills
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh/testing-workflows/discover-testing -g -a codex -y
```

`--lang zh|en|all` 只控制源语言，`--skill` 使用物理 slug；中文和英文同名包建议分开安装，避免互相覆盖。根安装脚本、Windows 脚本和每 Skill shortcut 均以 [安装说明](../../scripts/INSTALL_SKILLS.md) 为准。

## 验收

- 双语目录、`SKILL.md`、`agents/openai.yaml`、`evals/eval.yaml` 和三类 case 均存在。
- 安装器 dry-run 能解析语言、工具和 Skill 参数；真实安装/运行仍需用户环境验证。
- 运行 `check_docs_bilingual.py`、`validate_skill_evals.sh` 和完整质量门禁。

## 导航

- [Quality Score 与最低 Eval 契约](./QUALITY_SCORE_EVAL_CONTRACT.md)
- [双语一致性契约](./BILINGUAL_CONSISTENCY_CONTRACT.md)
- [v1.4 收口](./PHASE_0_V1_4_CLOSEOUT.md)
