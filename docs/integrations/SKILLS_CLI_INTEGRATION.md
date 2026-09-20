<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILLS_CLI_INTEGRATION_EN.md">🇬🇧 English</a></div>

# Skills CLI / Agent Skills 集成契约

状态：V2 单迭代交付。`skills` CLI 是默认分发入口，`skills@1.7.0` 是仓库 CI 的固定兼容性验证版本。

本契约只覆盖分发、发现、安装路径和仓库边界。它不把 CLI 加入 Skill 运行时，也不替代 `skill-up` 行为评测、业务验收、发布批准或生产验证。

## 快速开始

仓库级入口默认 English-first，按 leaf Skill 的 canonical name 安装：

```bash
# 安装 English functional-testing
npx skills add naodeng/awesome-qa-skills --skill functional-testing

# 可选：显式指定 Codex target
npx skills add naodeng/awesome-qa-skills --skill functional-testing -a codex

# 安装 English 全量集合
npx skills add naodeng/awesome-qa-skills
```

中文必须显式选择语言源；同一 target 默认只安装一种语言：

```bash
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing
```

## V2 分发契约

1. leaf 目录名、`SKILL.md` frontmatter 的 `name` 和 CLI `--skill` ID 必须一致。
2. 新 Skill 必须能从仓库级入口被发现，不能依赖隐藏的叶子路径或未记录的别名。
3. leaf Skill 必须可独立安装或复制，自己的 `SKILL.md`、prompt、metadata 和资源必须自洽。
4. `skills/en` 和 `skills/zh` 保持相同 canonical name；同一语言内不允许重复。
5. `description` 同时服务触发与 discovery，必须说明能力、触发时机和 QA 区分度。
6. CLI 是分发层，不是 Skill 的运行时依赖；安装不应隐式执行 Skill 脚本。

仓库级源默认映射到 English。需要中文时使用显式 `skills/zh` 源，不依赖 CLI 对同名 Skill 的隐式去重或 namespacing。

## 固定版本与高级命令

README 的日常命令保持简单、不锁定版本。复现 CI 或需要确定性工具版本时使用 `skills@1.7.0`：

```bash
# 固定版本安装 English functional-testing 到全局 Codex target
npx --yes skills@1.7.0 add naodeng/awesome-qa-skills --skill functional-testing -g -a codex -y

# 固定版本显式安装 Chinese functional-testing
npx --yes skills@1.7.0 add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing -g -a codex -y

# 查看记录、更新和移除
npx --yes skills@1.7.0 list --json
npx --yes skills@1.7.0 update -g -y
npx --yes skills@1.7.0 remove functional-testing -g -y
```

`use`、`update`、`remove` 和 Agent target 属于 CLI 版本行为。升级 pin 前先运行 `npx --yes skills@<version> --help`，再更新脚本、CI 和本文件。

## 兼容性门禁

提交前运行：

```bash
bash scripts/check_skills_cli_compatibility.sh
```

该入口完成一组小而稳定的检查：

- 本地静态契约：`SKILL.md`、frontmatter、`name`、目录一致性、同语言重复、EN/ZH canonical name 对齐。
- 代表性发现：`requirements-analysis`、`functional-testing`、`api-testing`、`performance-testing`、`ai-agent-testing`、`release-testing-workflow`、`skill-change-verification`。
- 固定 `skills@1.7.0` 的 repository-level `--list` discovery。
- English-first 的 `functional-testing` 全局 Codex smoke，并验证安装后的 `SKILL.md`、canonical name 和 English 标题。

CI 在现有 `project-quality.yml` 中使用一个 `skills-cli-compatibility` job，并将 `SKILLS_CLI_PACKAGE` 指向当前 checkout，确保 PR 验证的是本次变更而不是固定远程默认分支。手动运行未设置该变量时，默认使用 `naodeng/awesome-qa-skills`；要对本地 checkout 复现 CI，可运行 `SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh`。不会运行 latest Canary，也不把 Skill 总数作为契约。该 gate 不声称完成全量真实安装、模型 replay、浏览器运行时、业务验收或发布证据。

## Tested 与 Ecosystem compatible

- **Tested by this repository**：固定 `skills@1.7.0`、仓库级 English discovery、上述代表性名称和 English `functional-testing` Codex 安装 smoke。
- **Ecosystem compatible**：上游 CLI 声明可用但没有本仓库持续 gate 证据的 Agent、版本或路径。不能把它写成项目 Tested。

## 旧安装器与手工路径

CLI 是首选分发层，但现有路径继续保留：

```bash
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/
bash scripts/install-skills-mac.sh --tool codex --lang zh
```

Windows 安装器和手工复制同样不因 CLI 引入而删除。它们是兼容性备用路径，不改变 canonical name 或目录布局。

## V2 明确不做

- 不新增 `skills-manifest.json`、`package.json`、CLI runtime dependency 或自有包管理器。
- 不重构 `skills/en` / `skills/zh`、不改 canonical name、不引入 `-en` / `-zh` 后缀。
- 不删除旧安装器，不新增独立 canary workflow，不做复杂 Canary 或多 Agent 全矩阵。
- 不要求 164 个 Skill 全量真实安装，不把 trigger eval 扩建或 `skill-up` 架构改造混入本迭代。

## 排障

- 静态检查失败：先修 `CONTRACT`、`BILINGUAL` 或 `DISCOVERY` 输出，再重跑完整质量门禁。
- discovery 找不到代表性 Skill：确认仓库根入口、canonical name 和远程分支内容，而不是改成叶子 URL 绕过检查。
- EN/ZH 覆盖：清理目标中的已有语言后只安装一个语言集合；不要假设同名 Skill 会自动隔离。
- CLI 上游破坏：保留静态契约和旧安装器，暂停推荐 CLI 的发布性声明；固定 pin 不自动升级。
