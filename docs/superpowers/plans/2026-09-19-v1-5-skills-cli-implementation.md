# v1.5 Skills CLI / Agent Skills Ecosystem Implementation Plan

## Goal

在一个 v1.5 迭代内完成附件 `awesome-qa-skills-skills-cli-integration-pack` 的可交付实现：保留现有双语 QA Skill 分类、`skill-up` 评测与自有安装器，引入可验证的 Agent Skills / `skills` CLI 分发兼容层，并让新贡献者可以生成通过项目门禁的双语 Skill 骨架。

## Spec and constraints

- 规格来源：任务附件中的 15 份 Skills CLI / Agent Skills integration pack 文档。
- 架构边界：`awesome-qa-skills` 是 QA Skill source/governance layer，`skill-up` 是 evaluation layer，`skills` CLI 是 distribution layer；CLI 不是运行时依赖。
- 不改动既有 `skills/{en|zh}/{category}/{skill}` 路径，不删除现有 macOS/Linux/Windows 安装器。
- 双语 canonical name 可以跨语言重复，但同一语言内不得重复；默认安装单一语言，避免同名覆盖。
- 每个 leaf Skill 必须保持可独立复制/安装，局部引用必须可解析，不得硬依赖其他 Skill 的内部文件。
- 只有经过当前仓库验证的 agent/CLI 才标记为 Tested；其余只标记为 Ecosystem compatible。
- 不提交或推送；保留任务开始前已有工作区改动。

## Task 1 — Compatibility contract and static validator

先为 validator 编写失败测试，再实现 `scripts/check_skills_cli_compatibility.py` 与入口 `scripts/check_skills_cli_compatibility.sh`。覆盖：

- SKILL.md / frontmatter / `name` / directory match / description contract；
- same-language duplicate canonical name；
- broken local Markdown resource references；
- cross-Skill internal-file references；
- failure categories `CONTRACT`, `BILINGUAL`, `RESOURCE_REFERENCE`；
- machine-readable JSON report and actionable text output。

将 validator 纳入 `check_skills_quality.sh`，并让当前仓库全量通过。

## Task 2 — CLI verification and distribution smoke fixtures

- 锁定并记录实际验证的 `skills` CLI version（当前验证候选为 `1.7.0`）。
- 用 CLI 验证 `skills/en`、`skills/zh`、代表性 leaf 的 discovery/list/install/remove 路径；所有 smoke 使用隔离临时目录。
- 新增不会修改源树的 smoke script/test，并在 CI 中使用固定版本；latest 只作为可选 canary，不作为 required gate。
- 输出兼容矩阵，明确 Tested / Ecosystem compatible、collection/leaf、legacy fallback 和语言碰撞策略。

## Task 3 — Authoring contract and scaffold generator

先为 generator 编写失败测试，再实现 `scripts/create_skill.py`：

- `--name`、`--category`，默认生成 EN/ZH；`--single-language` 仅在显式指定时生效；
- 生成 `SKILL.md`、`prompts/<name>.md`、`agents/openai.yaml`、`evals/eval.yaml` 与 success/incomplete/scope cases；
- 非法 canonical name、同语言 collision、已有目录默认拒绝；`--overwrite` 才允许覆盖；
- 生成 TODO/待翻译标记，不伪装双语完成；
- scaffold 后自动执行静态兼容检查与现有 Skill integrity/eval checks；失败时返回非零且保留可修复骨架。

同步 `SKILL_AUTHORING.md/_EN.md`、`AGENTS.md` 和脚手架使用文档。

## Task 4 — Documentation, ADR, and repository entry points

新增双语 integration guide、compatibility matrix、ADR；更新双语 README 和 `scripts/INSTALL_SKILLS.md`，补齐：

- CLI 安装、list/use/update/remove 的已验证语法；
- manual copy 与现有 installers fallback；
- Tested vs Ecosystem compatible；
- EN/ZH 独立安装与同名 collision；
- troubleshooting / rollback / legacy installer maintenance-mode decision；
- 命令版本依赖说明。

## Task 5 — CI, discovery quality, and full verification

- 更新 `.github/workflows/project-quality.yml`：静态兼容门禁、固定 CLI discovery/install smoke、既有 eval/schema 门禁保持不变。
- 增加 description/discovery audit 输出及 trigger/negative-trigger authoring guidance，不批量改写已有 Skill 文案。
- 运行双语文档、完整质量门禁、脚本单测、CLI smoke、diff 检查；检查工作区只包含本迭代相关改动。
- 最后复核 GitHub Project #4：v1.5 卡为当前开发状态且 Target Version 为 v1.5，原有卡片仍为 v1.6/v1.7/v1.8/v1.9，状态/版本无错位。

## Completion evidence

- `bash scripts/check_skills_cli_compatibility.sh --fail-on-findings`
- `bash scripts/check_skills_quality.sh`
- `python3 -m unittest discover -s scripts/tests -p 'test_*.py' -v`
- CLI 1.7.0 EN/ZH discovery and isolated representative install smoke
- `python3 scripts/check_docs_bilingual.py --repo-root .`
- `git diff --check` and final `git status --short`
- Project #4 card/status/version verification
