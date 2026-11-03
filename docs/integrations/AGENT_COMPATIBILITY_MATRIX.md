<div align="right"><strong>🇨🇳 中文</strong> | <a href="./AGENT_COMPATIBILITY_MATRIX_EN.md">🇬🇧 English</a></div>

# Agent 兼容与分发验证矩阵

本表区分仓库结构/安装器证据、skills CLI 发现证据和 Agent Host 内真实调用。源码静态兼容或 `--dry-run` 不代表 Host 已加载或成功执行 Skill。状态截至 2026-11-03；安装、升级、卸载和 ZIP 的逐项结果见[机器可读验证记录](./agent-compatibility-evidence-2026-11-03.json)。

| 能力 | Codex | Claude Code | Cursor | 证据边界 |
| --- | --- | --- | --- | --- |
| 安装入口 | macOS/Linux 安装器 | macOS/Linux 安装器 | macOS/Linux 安装器 | `--tool` 目标 × 5 个 Workflow 包 × 2 种语言 × 每项 2 次，共 60 次隔离安装；逐文件 SHA-256 与源码一致 |
| canonical name / 单 Skill 目录 | 支持 | 支持 | 支持 | `validate_agents_metadata.py`、独立性检查、安装文件结构 |
| Agent Skills CLI 发现 | `skills@1.7.0` 仓库 Gate | 同左，按 Gate 所覆盖 CLI 行为解释 | 同左，按 Gate 所覆盖 CLI 行为解释 | CLI Gate 不证明内置 Host Runtime 兼容 |
| 中文/英文选择 | `--lang zh|en` | `--lang zh|en` | `--lang zh|en` | 60 次安装均落入独立临时根目录；逐文件与对应源码比对一致，未改真实用户配置 |
| References / Scripts | 按包内资源分发 | 按包内资源分发 | 按包内资源分发 | 5 个包的中英文版本均逐文件校验；打包 ZIP 与源码文件清单及内容一致 |
| 单 Skill ZIP | 可用通用打包器 | 可用通用打包器 | 可用通用打包器 | 10 个 ZIP 均有根级 `SKILL.md`、`agents/openai.yaml`、Eval 配置；归档内容逐文件一致，不代表 Agent 原生 ZIP 安装体验 |
| 升级 / 卸载 / 残留 | Codex 安装目标已验证 | 安装器目标可选 | 安装器目标可选 | Codex 临时目标对 5 个包 × 2 种语言完成 10 次同路径升级、卸载预览/实际删除及 0 残留扫描；未声称 Claude Code/Cursor Host 升级运行已验证 |
| Host 自动发现 / Prompt 执行 | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | 需在各 Host 的真实用户环境单独验收 |
| Workflow 跨阶段自动编排 / Host 恢复 | `NOT_RUN` | `NOT_RUN` | `NOT_RUN` | 仓库提供并验证文件型 Run State CLI；它可校验 Checkpoint 并拒绝过期或重复阶段，但不执行 Skill 或调度 Host 阶段 |

## 复现命令

```bash
bash scripts/check_skills_cli_compatibility.sh
bash scripts/install-skills-mac.sh --tool codex --lang en --skill pr-quality-review --dest /tmp/qa-skills-install --dry-run
python3 scripts/manage_skill_packages.py pack --skill-dir skills/en/testing-workflows/pr-quality-review --output /tmp/pr-quality-review-en.zip
python3 scripts/manage_skill_packages.py check-residue --install-root /tmp/qa-skills-install --repo-root . --json
```

实际 Host 验收需记录 Host 名称与版本、Skill 版本、安装方式、加载证据、输入案例、输出与时间；没有这些记录时保持 `NOT_RUN`。
