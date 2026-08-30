# AGENTS.md

本文件面向 coding agent（Cursor、Codex、Claude Code 等），补充 README 之外的项目操作约定。人类贡献者请优先看 [README.md](README.md)、[CONTRIBUTING.md](CONTRIBUTING.md)、[skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md)。

## Project overview

`awesome-qa-skills` 是按语言分区的 **AI 测试辅助技能库**，不是可执行应用。核心产出是可复制到各 AI 工具的 skill 目录。

| 分区 | 路径 |
| --- | --- |
| 中文技能 | `skills/zh/` |
| 英文技能 | `skills/en/` |
| 工作流 | `skills/{zh,en}/testing-workflows/`（日常 / 迭代 / 发布 / 路由） |
| 测试类型 | `skills/{zh,en}/testing-types/`（功能、API、性能、安全等） |
| Skill Engineering | `skills/{zh,en}/skill-engineering/`（Skill 编写与仓库治理） |
| 安装脚本 | 根目录 `install-skills-*.sh` + `scripts/` + `installers/` |
| 参考素材 | `resources/`（公共素材池，勿与 skill 内 `references/` 混淆） |
| 旧版提示词 | `legacy-prompts/`（兼容旧根级提示词；正式入口以 skill 内 `prompts/` 为准） |

在线站点：https://inaodeng.com/qaskills/

## Repository map (edit here)

改 skill 时，先定位到正确语言与类别，再改同名目录：

```text
skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/
├── SKILL.md                 # 必需：入口 + YAML frontmatter
├── prompts/                 # 必需：主提示词
├── agents/openai.yaml       # 必需：OpenAI / Codex 元数据
├── evals/                   # 必需：skill-up 评测用例
├── output-formats.md        # 可选
├── quick-start.md           # 可选
├── reference.md             # 可选（工作流映射等）
├── references/              # 可选：按需加载的深资料
├── examples/                # 可选：示例输入输出
└── scripts/                 # 可选：本 skill 辅助脚本
```

规则：

- 中英文 skill **目录名一致**（如 `functional-testing`），不再使用 `-en` 后缀。
- Prompt 统一放在 `prompts/`；英文 prompt 文件名 **不带** `_EN`。
- 改中文 skill 时，同步检查并更新对应英文目录（反之亦然），除非用户明确只要单语。
- 保持 skill **可独立安装**：一个 skill 目录复制出去后应自洽。

## SKILL.md conventions

Frontmatter 最少包含：

```yaml
---
name: skill-name
description: Use this skill when ...; triggers include 中文触发词 and English triggers.
---
```

要求：

- `name`：小写、数字、连字符；与目录名、`agents/openai.yaml` 的 `metadata.key` 一致。
- `description`：第三人称祈使（`Use this skill when...`）；同时写清 **做什么** 与 **何时用**；包含触发词；宜短于 1024 字符。
- 正文保持精简，并包含：执行流程、核心约束、**按需加载**（写清何时读 `prompts/` / `references/` / `examples/` / `scripts/`）、交付前自检、常见误区。
- `prompts/` 仍是完整执行规范；`SKILL.md` 不要做成只有「打开 prompts」的空壳。
- 入口文件保持轻量、直接、可执行；深度规则、长示例、故障排查优先放到 `references/` 或 `examples/`。
- 默认输出 Markdown；需要 Excel/CSV/JSON/Word 时指向 `output-formats.md`。
- 每个新增或修改的 skill 都必须配置并维护 `evals/`（skill-up：`eval.yaml` + `cases/*.yaml`）；至少覆盖成功路径、信息不完整、范围/风险边界三类用例。详见 [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)。

参考现有 skill（如 `skills/zh/testing-types/functional-testing/`），不要照搬 [CONTRIBUTING.md](CONTRIBUTING.md) 里较旧的「basic/intermediate/advanced」三层 prompt 结构——当前以单主 prompt + 可选增强版 skill 为准。

批量优化 / 脚手架：

```bash
python3 scripts/optimize_skills_skillup.py
python3 scripts/scaffold_skill_evals.py --pilot   # 或 --skill <path> / --all-missing
```

## agents/openai.yaml

每个 skill 必须有 `agents/openai.yaml`，且与 `SKILL.md` 对齐：

```yaml
version: 1
metadata:
  key: "<与 SKILL.md name 相同>"
interface:
  display_name: "..."
  short_description: "..."   # 建议 ≤160 字符
  default_prompt: "Use the <skill-name> skill ..."
policy:
  allow_implicit_invocation: true   # 或 false
```

## Independence & linking rules

校验脚本会检查跨 skill 依赖：

- **禁止** skill A 的 markdown 链接指向 skill B 的内部文件（破坏独立安装）。
- **允许** 同一 skill 的 zh/en 对应 `prompts/` 互链。
- 跨 skill 推荐关系写在文案里即可，不要用相对路径硬绑其它 skill 目录。
- 外部 URL 快照/镜像保持精简（见 `scripts/check_external_snapshots.py`）。

## Dev / quality commands

本仓库无应用构建步骤。改 skill、脚本或目录结构后，在仓库根目录运行：

```bash
# 一键质量门禁（pre-commit 也会跑）
bash scripts/check_skills_quality.sh
```

分步等价于：

```bash
python3 scripts/organize_project_dirs.py
python3 scripts/validate_agents_metadata.py
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
python3 scripts/validate_skills_integrity.py --fail-on-findings
python3 scripts/check_external_snapshots.py --skills-root skills --max-per-skill 5
bash scripts/validate_skill_evals.sh
python3 scripts/check_docs_bilingual.py --repo-root .
```

安装相关改动可参考：

```bash
bash scripts/install-skills-mac.sh --tool cursor --lang zh --dry-run
bash scripts/generate-install-shortcuts.sh   # 若改了安装器生成逻辑
```

改脚本、安装器或目录生成逻辑后，至少跑一次相关命令做基本验证，确认没有改坏安装路径、语言分区或工具名。

启用 git hook（可选）：

```bash
bash scripts/setup-git-hooks.sh
```

提交前应保证 `check_skills_quality.sh` 通过。

## How to add or edit a skill

1. 在 `skills/zh/...` 与（通常）`skills/en/...` 建立同名目录。
2. 写 `SKILL.md`、`prompts/<name>.md`、`agents/openai.yaml`。
3. 补齐 `evals/eval.yaml` 和 `evals/cases/*.yaml`，新增 skill 不允许没有测试用例。
4. 按需补 `output-formats.md`、`examples/`、`scripts/`。
5. 更新索引文档：`docs/catalog/skills-index.md`、`skills/zh/README.md` / `skills/en/README.md`、根 `README.md` / `README_EN.md`（若新增对外入口）。
6. 若影响安装入口，检查 `scripts/` 与 `installers/`。
7. 跑 `bash scripts/check_skills_quality.sh` 并修到绿。

增强版 skill（如 `*-plus`）视为独立 skill，仍遵循同一目录与元数据规范。

## Content & security guidelines

- **禁止**在示例、prompt、文档中硬编码真实 Bearer token、密码、cookie、私钥；用环境变量或占位符。
- 示例 curl / 配置必须脱敏。
- Prompt 与文档默认中文优先写 `skills/zh`，英文写 `skills/en`；术语（k6、Playwright、API）可保留英文。
- 不要大范围重写无关 skill；改动范围只服务当前需求。
- 不要把 `resources/` 下的大段示例无必要地复制进多个 skill。

## Commit & PR instructions

- Commit 遵循 [Conventional Commits](https://www.conventionalcommits.org/)：`feat|fix|docs|refactor(scope): subject`
- Scope 常用 skill 名或区域，例如：`feat(functional-testing): ...`、`docs(readme): ...`
- PR 说明应写清：改了哪些 skill / 语言、是否双端同步、质量脚本是否通过。
- 不要提交密钥、本机绝对路径、或仅本地有效的安装路径。
- 未经用户明确要求，不要 `git push`、不要改 git config。

## Docs map (when stuck)

| 问题 | 文档 |
| --- | --- |
| 怎么用 / 装 skill | [README.md](README.md)、[scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) |
| 目录规范 | [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md)、[skills/SKILL_STYLE_GUIDE.md](skills/SKILL_STYLE_GUIDE.md) |
| 贡献流程 | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 常见问题 | [FAQ.md](FAQ.md) |
| 技能总览 | [docs/catalog/skills-index.md](docs/catalog/skills-index.md) |

## Nested AGENTS.md

若某个子目录（例如大型 skill 或 `scripts/`）需要更细的 agent 说明，可在该目录再放 `AGENTS.md`；**离编辑文件最近的文件优先**，用户对话指令覆盖一切。
