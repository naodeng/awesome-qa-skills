# Share Context

本文档为后续拆分任务、并行 agent 或分片执行提供共享上下文。它不替代根目录 `AGENTS.md`、`README.md`、`CONTRIBUTING.md`、`skills/DIRECTORY_GUIDE.md` 或 `skills/SKILL_STYLE_GUIDE.md`；遇到冲突时，以更靠近编辑位置的项目规则和用户最新指令为准。

## Project Snapshot

`awesome-qa-skills` 是按语言分区维护的 AI 测试辅助技能库，不是可执行应用。核心资产是可复制到 Codex、Cursor、Claude Code、Kiro、OpenCode、Trae 等工具里的 agent skill 目录。

项目当前主线：

- 中文技能位于 `skills/zh/`。
- 英文技能位于 `skills/en/`。
- 工作流技能位于 `testing-workflows/`，覆盖日常测试、迭代测试、发布测试和技能路由。
- 测试类型技能位于 `testing-types/`，覆盖功能、API、自动化、性能、安全、移动端、可访问性、测试策略、测试用例、缺陷、报告以及工具专项技能。
- 安装脚本位于根目录、`scripts/` 和 `installers/`。
- 公共参考素材位于 `resources/`；不要和单个 skill 内部的 `references/` 混用。

## Repository Layout

```text
awesome-qa-skills/
├── skills/
│   ├── zh/
│   │   ├── testing-types/
│   │   └── testing-workflows/
│   └── en/
│       ├── testing-types/
│       └── testing-workflows/
├── scripts/
├── installers/
├── docs/
├── resources/
├── legacy-prompts/
├── README.md / README_EN.md
├── skills-index.md
├── AGENTS.md
└── LICENSE
```

单个 skill 的标准结构：

```text
skills/{zh|en}/{testing-types|testing-workflows}/<skill-name>/
├── SKILL.md
├── prompts/
├── agents/openai.yaml
├── evals/
├── output-formats.md
├── quick-start.md
├── reference.md
├── references/
├── examples/
└── scripts/
```

并非每个可选文件夹都必须存在，但 `SKILL.md`、`prompts/`、`agents/openai.yaml` 和 `evals/` 是核心内容。新增或修改 skill 时必须配置 skill-up 测试用例。

## Skill Authoring Rules

编辑或新增 skill 时保持这些约束：

- 中英文目录名一致，例如 `functional-testing` 在 `skills/zh/...` 与 `skills/en/...` 下同名。
- 英文目录不再使用 `-en` 后缀。
- Prompt 统一放在 `prompts/`，英文 prompt 文件名不带 `_EN`。
- `SKILL.md` frontmatter 至少包含 `name` 和 `description`。
- `name` 使用小写、数字、连字符，并与目录名、`agents/openai.yaml` 的 `metadata.key` 一致。
- `description` 使用 `Use this skill when ...; triggers include ...` 风格，说明适用场景和触发词，避免只写能力介绍。
- `SKILL.md` 保持轻量，写清何时使用、如何使用、参考文件、常见误区、最佳实践和交付前自检。
- 深规则、长示例、故障排查优先放入 `references/` 或 `examples/`。
- `prompts/` 是完整执行规范，应包含输入、要做的事、执行规则、最低覆盖清单、输出和质量要求。
- `evals/` 是新增 skill 的必需项，至少包含 `evals/eval.yaml` 和 `evals/cases/*.yaml`；用例至少覆盖成功路径、输入不完整、范围/风险边界。
- 默认输出 Markdown；如支持 CSV、JSON、Excel、Word 等格式，放到 `output-formats.md` 或模板文件中说明。

## Bilingual Sync

仓库按中英文双份维护。除非用户明确要求只改单语，否则：

- 改中文 skill 时检查对应英文 skill。
- 改英文 skill 时检查对应中文 skill。
- 保持中英文结构、入口、prompt skeleton、核心流程和 metadata 对齐。
- 不要求机械翻译；中文内容应适合中文 QA 团队，英文内容应适合英文团队。
- 如果只改了一边，最终汇报必须说明原因和剩余同步风险。

## Independence And Linking

每个 skill 应能独立复制安装。维护时注意：

- 禁止 skill A 的 markdown 链接指向 skill B 的内部文件。
- 允许同一 skill 的 zh/en 对应 `prompts/` 互链。
- 跨 skill 推荐关系用文字描述，不用相对路径硬链其他 skill 的内部文件。
- 不要把 `resources/` 下的大段素材无差别复制进多个 skill。
- 示例、prompt、配置和 curl 中禁止写入真实 token、密码、cookie、私钥或内部密钥。

## Common Workflows

新增或编辑 skill 的常规步骤：

1. 定位语言、分类和同名目录。
2. 先读相邻 skill 的结构与写法，延续现有模式。
3. 修改 `SKILL.md`、`prompts/<skill-name>.md`、`agents/openai.yaml`。
4. 必须补充 `evals/eval.yaml` 和 `evals/cases/*.yaml`，新增 skill 不允许缺少测试用例。
5. 按需补充 `output-formats.md`、`examples/`、`references/`、`scripts/`。
6. 若新增 skill，更新 `skills-index.md`、`skills/zh/README.md`、`skills/en/README.md`、根 README 或英文 README 中的入口。
7. 若影响安装入口，检查或重新生成 `installers/`。
8. 跑质量命令并修复与本次改动相关的问题。

安装器或脚本类改动：

- 先读 `scripts/INSTALL_SKILLS.md` 和相邻脚本。
- 保持工具名、语言分区和安装路径稳定。
- 脚本改完至少跑对应 dry-run 或生成命令。

## Quality Commands

仓库没有应用构建步骤。改 skill、脚本或目录结构后，在仓库根目录优先运行：

```bash
bash scripts/check_skills_quality.sh
```

质量门禁包含：

```bash
python3 scripts/organize_project_dirs.py
python3 scripts/validate_agents_metadata.py
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
python3 scripts/validate_skills_integrity.py --fail-on-findings
python3 scripts/check_external_snapshots.py --skills-root skills --max-per-skill 5
bash scripts/validate_skill_evals.sh
```

安装相关改动可补充：

```bash
bash scripts/install-skills-mac.sh --tool cursor --lang zh --dry-run
bash scripts/generate-install-shortcuts.sh
```

若 `skill-up` 未安装，eval YAML 校验脚本可能只能做有限检查；最终汇报应说明实际运行结果。

## Git And Workspace Safety

- 工作区可能已有用户改动，先用 `git status --short` 观察，不要假设干净。
- 不回退、覆盖、删除或重置非本次产生的改动。
- 不执行破坏性 git 操作，除非用户明确要求。
- 未经用户明确要求，不提交、不 push、不改 git config。
- 如果用户要求提交，只 stage 本次相关文件，并使用 Conventional Commits，例如 `docs(readme): ...` 或 `feat(functional-testing): ...`。

## Agent Handoff Notes

给后续分片或 agent 的建议：

- 先读根目录 `AGENTS.md` 和离目标文件最近的说明文件。
- 先用 `rg` / `rg --files` 定位文件，不要全仓库盲改。
- 优先复用已有 skill 结构、prompt skeleton、metadata 写法和脚本模式。
- 改动范围只服务当前任务，不顺手重构无关 skill。
- 对测试、构建、校验失败先定位根因，再修复。
- 汇报时说明改了什么、为什么这样改、跑了哪些检查、是否还有风险。

## Useful Entry Points

- 项目介绍：`README.md`、`README_EN.md`
- 贡献流程：`CONTRIBUTING.md`
- 全量索引：`skills-index.md`
- 目录规范：`skills/DIRECTORY_GUIDE.md`
- skill 写作规范：`skills/SKILL_STYLE_GUIDE.md`
- skill authoring 与 eval：`skills/SKILL_AUTHORING.md`
- 安装说明：`scripts/INSTALL_SKILLS.md`
- 一键质量门禁：`scripts/check_skills_quality.sh`
