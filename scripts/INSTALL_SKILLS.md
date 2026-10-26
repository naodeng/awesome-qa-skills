<div align="right"><strong>🇨🇳 中文</strong> | <a href="./INSTALL_SKILLS_EN.md">🇬🇧 English</a></div>

# 安装 Skills

本指南介绍如何把仓库中的 QA Skills 安装到 AI 编码工具。一般先用 `skills` CLI 安装单个 Skill；需要批量安装时使用仓库脚本；也可以手动复制单个 Skill 目录。

| 方式 | 适用场景 |
| --- | --- |
| [`skills` CLI](#使用-skills-cli) | 推荐方式，安装单个 Skill 或整套英文 Skills |
| [仓库安装脚本](#使用仓库安装脚本) | 在 macOS、Linux 或 Windows 上按工具和语言批量安装 |
| [单 Skill 快捷安装器](#使用单-skill-快捷安装器) | 从仓库提供的快捷脚本安装一个 Skill |
| [克隆完整仓库](#克隆完整仓库) | 将全部 Skill 和文档保留在项目内 |
| [Git 子模块](#添加为-git-子模块) | 在 Git 项目中跟踪本仓库版本 |
| [手动复制](#手动复制) | 自行选择目标路径，或使用未列出的兼容工具 |
| [社区推荐的外部 Skills](#社区推荐的外部-skills) | 安装由其他项目维护的 Skill |

安装只分发 Skill 文件，不会自动执行 Skill 包内的脚本。

## 安装前先选语言

中文和英文 Skill 使用相同的 canonical name，例如 `functional-testing`。默认建议在一个工具目标中安装一种语言，避免同名 Skill 互相覆盖或被工具识别成重复项。

仓库级 `skills` CLI 入口默认发现英文 Skills。安装中文 Skill 时，要把 `skills/zh` 目录作为来源显式传入；不要给 Skill 名称添加 `-zh` 或 `-en` 后缀。

## 使用 `skills` CLI

CLI 需要 Node.js 和 `npx`。安装到自动检测的工具目标：

```bash
# 安装一个英文 Skill
npx skills add naodeng/awesome-qa-skills --skill functional-testing

# 安装英文 Skill，并指定 Codex
npx skills add naodeng/awesome-qa-skills --skill functional-testing -a codex

# 安装英文 Skills 集合
npx skills add naodeng/awesome-qa-skills
```

中文 Skill 要指定 `skills/zh` 来源：

```bash
# 安装一个中文 Skill
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing

# 安装整套中文 Skills
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh
```

### 固定 CLI 版本和管理已安装的 Skill

日常安装可以使用上面的简短命令。仓库兼容性检查固定使用 `skills@1.7.0`；需要复现该检查或锁定 CLI 版本时，使用固定版本命令：

```bash
# 固定版本：安装英文 Skill 到 Codex 全局目标
npx --yes skills@1.7.0 add naodeng/awesome-qa-skills --skill functional-testing -g -a codex -y

# 固定版本：显式安装中文 Skill 到 Codex 全局目标
npx --yes skills@1.7.0 add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing -g -a codex -y

# 查看、更新或移除全局安装记录
npx --yes skills@1.7.0 list --json
npx --yes skills@1.7.0 update -g -y
npx --yes skills@1.7.0 remove functional-testing -g -y
```

一次性使用时，固定版本 CLI 也提供 `use`。该命令需要交互式终端，具体参数可能随 CLI 版本变化：

```bash
npx --yes skills@1.7.0 use https://github.com/naodeng/awesome-qa-skills --skill api-testing --agent codex
```

`use`、`update`、`remove` 等命令的参数可能随 CLI 版本变化。更完整的分发约定和兼容性范围见 [Skills CLI 集成指南](../docs/integrations/SKILLS_CLI_INTEGRATION.md)；CLI 基本用法见 [官方 CLI 文档](https://www.skills.sh/docs/cli)。

## 使用仓库安装脚本

仓库脚本可按工具、语言和 Skill 筛选。执行前可加 `--dry-run` 预览；预览不会写入文件。

### macOS / Linux

```bash
# 预览：把中文 functional-testing 安装到 Codex
bash scripts/install-skills-mac.sh --tool codex --lang zh --skill functional-testing --dry-run

# 正式安装单个中文 Skill
bash scripts/install-skills-mac.sh --tool codex --lang zh --skill functional-testing

# 安装某个工具支持的全部英文 Skills
bash scripts/install-skills-mac.sh --tool cursor --lang en

# 安装到自定义目录
bash scripts/install-skills-mac.sh --tool codex --lang zh --dest /path/to/skills
```

### Windows（PowerShell）

```powershell
# 预览：把中文 functional-testing 安装到 Codex
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill functional-testing -DryRun

# 正式安装单个中文 Skill
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill functional-testing

# 安装到自定义目录
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Dest C:\skills
```

两种脚本的参数如下：

| 参数 | 可用值 | 说明 |
| --- | --- | --- |
| `--tool` / `-Tool` | `claude`、`claudecode`、`cursor`、`codex`、`kiro`、`opencode`、`trae`、`all` | 选择目标工具；`all` 会安装到脚本支持的所有工具 |
| `--lang` / `-Lang` | `zh`、`en`、`all` | 选择中文、英文或两种语言 |
| `--skill` / `-Skill` | Skill 目录名或 `all` | 只安装指定 Skill；名称使用 canonical name |
| `--dest` / `-Dest` | 目录路径 | 覆盖工具默认目标目录 |
| `--dry-run` / `-DryRun` | 开关 | 只显示将执行的复制操作，不写入文件 |

`--lang all` 会把两个语言目录分别放在目标路径的 `zh/` 和 `en/` 子目录中。只有当目标工具能从这种目录结构发现 Skills 时才使用它；默认建议为每个工具目标选择一种语言。

脚本会同步 Skill 目录；目标位置已有同名目录时，目录内容会被替换。先运行 `--dry-run`，并备份你在已安装目录中手动修改过的文件。

脚本默认安装目标：

| 工具 | macOS / Linux | Windows |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `%USERPROFILE%\.claude\skills\` |
| Cursor | `~/.cursor/skills/` | `%USERPROFILE%\.cursor\skills\` |
| Codex | `~/.codex/skills/` | `%USERPROFILE%\.codex\skills\` |
| Kiro | `~/.kiro/skills/` | `%USERPROFILE%\.kiro\skills\` |
| OpenCode | `~/.opencode/skills/` | `%USERPROFILE%\.opencode\skills\` |
| Trae | `~/.trae/skills/` | `%USERPROFILE%\.trae\skills\` |

指定 `--dest` / `-Dest` 时，脚本会在该目录下继续按语言、类别和 Skill 名称分层，例如 `<目标目录>/zh/testing-types/functional-testing/`。

## 使用单 Skill 快捷安装器

`installers/` 下的快捷脚本由 `scripts/generate-install-shortcuts.sh` 生成。不要手工编辑生成文件；如需修改生成逻辑，请编辑生成器并重新生成。快捷脚本应从仓库检出目录运行，以便读取对应的 Skill 源文件。

```bash
# macOS / Linux：安装中文 functional-testing 到 Codex
bash installers/zh/functional-testing/mac/codex.sh
```

```powershell
# Windows：安装中文 functional-testing 到 Codex
powershell -ExecutionPolicy Bypass -File .\installers\zh\functional-testing\windows\codex.ps1
```

快捷脚本目录结构：

```text
installers/{zh|en}/{skill-name}/{mac|windows}/{tool-script}
```

## 手动复制

从仓库根目录把单个 Skill 目录复制到目标工具的 Skills 目录。下面以 Codex 为例：

```bash
mkdir -p ~/.codex/skills
cp -R skills/zh/testing-types/functional-testing ~/.codex/skills/functional-testing
```

Windows PowerShell 示例：

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\zh\testing-types\functional-testing" "$HOME\.codex\skills\functional-testing"
```

将命令中的 `skills/zh/` 改为 `skills/en/` 可复制英文版本；也可以从 `testing-workflows/` 或 `skill-engineering/` 选择其他类别。

## 克隆完整仓库

如果希望在项目内保留所有 Skill、文档和安装脚本，可以克隆整个仓库：

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git .skills/awesome-qa-skills
```

克隆后，从 `skills/zh/` 或 `skills/en/` 选择所需 Skill。克隆仓库本身不会把 Skill 安装到 AI 工具的默认目录。

## 添加为 Git 子模块

在 Git 项目中用子模块固定本仓库的版本：

```bash
git submodule add https://github.com/naodeng/awesome-qa-skills.git .skills/awesome-qa-skills
```

## 社区推荐的外部 Skills

以下 Skills 由其他项目维护，供发现与参考，不属于本仓库目录，也未由本仓库进行运行时评测。版本、许可证和工具兼容性以各自上游为准。

### UIZZE anti-ui-slop

用于检查界面是否具备产品特定设计约定、必要状态和发布前 UX 质量门禁。上游当前列出 Apache-2.0、v1.3.1，以及 Claude Code、Codex、Cursor 和 GitHub Copilot 兼容信息；详见[上游 Skill](https://github.com/uizze/uizze/tree/main/skills/anti-ui-slop)和[社区提交记录](https://github.com/naodeng/awesome-qa-skills/issues/3)。

```bash
npx skills add https://uizze.com --skill anti-ui-slop
```

### UI Verify triage-visual-changes

用于对 UI Verify 构建后的视觉差异进行分流，区分真实回归、预期变化和渲染噪声。需要 UI Verify 账号（提供免费层）和 MCP 连接；社区提交记录列出的版本为 UI Verify plugin v0.1.0（核验于 2026-10-19）。详见[上游 Skill](https://github.com/uiverify/uiverify/tree/main/packages/skills/skills/triage-visual-changes)和[社区提交记录](https://github.com/naodeng/awesome-qa-skills/issues/33)。

```bash
npx skills add uiverify/uiverify --skill triage-visual-changes
```

Claude Code 也可使用插件市场命令：`/plugin marketplace add uiverify/uiverify`。

## 排查问题

- **CLI 找不到中文 Skill：** 使用 `skills/zh` 的 GitHub 来源，不要只传仓库根路径。
- **同一个工具中出现同名 Skill：** 清理目标中的另一种语言版本，再只安装所需语言。
- **安装后工具没有发现 Skill：** 确认目标路径与工具配置一致；通过 CLI 安装时可用 `-a` 显式指定工具。
- **想确认复制范围：** 先用仓库脚本的 `--dry-run` 查看目标路径和待复制目录。
- **需要复现仓库兼容性检查：** 使用 `skills@1.7.0`，并参阅 [Skills CLI 集成指南](../docs/integrations/SKILLS_CLI_INTEGRATION.md)。

## 相关文档

- [README：支持的 AI 工具](../README.md#支持的-ai-工具)
- [Skills CLI 集成指南](../docs/integrations/SKILLS_CLI_INTEGRATION.md)
- [Workflow / Eval / 安装同步清单](../docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md)
