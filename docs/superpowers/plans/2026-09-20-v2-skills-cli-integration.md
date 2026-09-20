# Implementation Plan: V2 Skills CLI Distribution Compatibility

## Goal

将 Skills CLI 设为仓库的稳定默认分发入口，保持现有 `skills/en`、`skills/zh` 目录、canonical name、双语体系和旧安装器不变；在一个迭代内完成分发契约、兼容性门禁、English-first 安装 smoke 以及文档同步。

## Scope

### In scope

- README / README_EN.md 的 CLI-first Quick Start 和 English-first / explicit Chinese 说明。
- `docs/integrations/SKILLS_CLI_INTEGRATION.md` 及英文对应文档。
- `scripts/check_skills_cli_compatibility.py` 的稳定静态契约检查。
- `scripts/check_skills_cli_compatibility.sh` 的固定 `skills@1.7.0` 远程代表性 discovery 与 English functional-testing smoke。
- 现有 `project-quality.yml` 中的单个 `skills-cli-compatibility` job。
- AGENTS、作者指南、安装文档和双语检查映射同步。
- 清理上一版中不属于 V2 DoD 的 audit、generator、复杂本地 smoke、matrix/ADR 扩展。

### Out of scope

- manifest、package.json、运行时依赖、独立 canary workflow、复杂 Canary/多 Agent 矩阵。
- 全量 Skill 真实安装、全量 trigger eval 补齐、重构现有 `skills/en` / `skills/zh`。
- 删除或改名旧安装器、改变 canonical name、创建/更新远程 Project 卡、push 或 release。

## File map

- `scripts/tests/test_check_skills_cli_compatibility.py`: 先补充失败测试，再覆盖 block scalar frontmatter、缺失根目录和代表性 Skill 契约。
- `scripts/check_skills_cli_compatibility.py`: 实现最小且健壮的静态分发检查。
- `scripts/check_skills_cli_compatibility.sh`: 串联静态检查、固定 CLI discovery 和 English-first 安装 smoke。
- `.github/workflows/project-quality.yml`: 保留现有质量 job，新增单个兼容性 job，移除 latest/schedule Canary。
- `README.md`, `README_EN.md`, `scripts/INSTALL_SKILLS.md`: CLI-first 安装入口和高级用法。
- `docs/integrations/SKILLS_CLI_INTEGRATION.md`, `docs/integrations/SKILLS_CLI_INTEGRATION_EN.md`: V2 分发契约、验证边界和故障排查。
- `skills/SKILL_AUTHORING.md`, `skills/SKILL_AUTHORING_EN.md`, `AGENTS.md`: 贡献者契约和命令。
- `scripts/check_docs_bilingual.py`: 仅保留实际存在的双语文档对。
- 删除上一版 V2 范围之外的审计、脚手架、复杂 smoke、matrix 和 ADR 文件及其测试/引用。

## Execution tasks

1. 先修改兼容性检查测试，运行目标测试确认新增场景按预期失败。
2. 用最小实现修复静态 checker，并运行目标测试；随后做必要的小范围重构。
3. 实现 shell wrapper 的固定版本远程 discovery、代表性名称验证和 English functional-testing smoke。
4. 收敛 workflow、README、集成文档、安装文档、作者指南和 AGENTS 到同一 V2 契约。
5. 删除越界实现并清理所有引用，保留历史计划文档作为工作记录。
6. 运行单元测试、完整质量门禁、兼容性 wrapper、双语检查、shell 语法检查和 `git diff --check`，检查工作区仅包含本次范围内的预期变化。

## Acceptance criteria

- 默认 README 命令是 `npx skills add naodeng/awesome-qa-skills --skill functional-testing`。
- repository-level 默认发现 English；中文必须显式指定 `skills/zh` 源。
- 静态检查验证 name/目录、frontmatter、同语言重复、代表性 Skill，且能处理合法 block scalar description。
- wrapper 使用固定 `skills@1.7.0`，不依赖固定总数，能验证代表性 discovery 和 English functional-testing 实际安装文件。
- workflow 只有一个兼容性 job，没有 latest Canary 或独立新 workflow。
- 现有质量脚本、skill-up eval、旧安装器路径和双语文档检查保持通过。
- 未引入 manifest、package.json 或 CLI runtime dependency。
