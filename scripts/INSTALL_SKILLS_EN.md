<div align="right"><strong>🇬🇧 English</strong> | <a href="./INSTALL_SKILLS.md">🇨🇳 中文</a></div>

# Install Skills

This guide covers installing QA Skills from the repository. Use the `skills` CLI for a single Skill, the repository scripts for batch installs, or copy a Skill directory manually.

| Method | Best for |
| --- | --- |
| [`skills` CLI](#use-the-skills-cli) | Recommended for installing one Skill or the full English collection |
| [Repository installers](#use-the-repository-installers) | Batch installs by tool and language on macOS, Linux, or Windows |
| [Per-Skill shortcuts](#use-a-per-skill-shortcut) | Installing one Skill with a generated repository script |
| [Clone the full repository](#clone-the-full-repository) | Keep all Skills and docs inside a project |
| [Add a Git submodule](#add-a-git-submodule) | Track this repository's version in a Git project |
| [Manual copy](#copy-a-skill-manually) | Choosing a custom target or using another compatible tool |
| [Community-recommended external Skills](#community-recommended-external-skills) | Install Skills maintained by other projects |

Installation distributes Skill files only; it does not automatically run scripts inside a Skill package.

## Choose a language first

Chinese and English Skills share the same canonical names, such as `functional-testing`. Install one language per tool target by default to avoid same-name Skills overwriting each other or being treated as duplicates.

The repository-level `skills` CLI entry discovers English Skills by default. To install a Chinese Skill, pass the `skills/zh` directory as the source. Do not add `-zh` or `-en` to the Skill name.

## Use the `skills` CLI

The CLI requires Node.js and `npx`. These commands let the CLI detect the target agent:

```bash
# Install one English Skill
npx skills add naodeng/awesome-qa-skills --skill functional-testing

# Install one English Skill and target Codex
npx skills add naodeng/awesome-qa-skills --skill functional-testing -a codex

# Install the full English collection
npx skills add naodeng/awesome-qa-skills
```

For a Chinese Skill, specify the `skills/zh` source:

```bash
# Install one Chinese Skill
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing

# Install the full Chinese collection
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh
```

### Pin the CLI version and manage installed Skills

Use the short commands above for routine installs. The repository compatibility check pins `skills@1.7.0`; use the pinned commands to reproduce that check or require a fixed CLI version:

```bash
# Install the English Skill to Codex's global target
npx --yes skills@1.7.0 add naodeng/awesome-qa-skills --skill functional-testing -g -a codex -y

# Explicitly install the Chinese Skill to Codex's global target
npx --yes skills@1.7.0 add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing -g -a codex -y

# List, update, or remove global installation records
npx --yes skills@1.7.0 list --json
npx --yes skills@1.7.0 update -g -y
npx --yes skills@1.7.0 remove functional-testing -g -y
```

The pinned CLI also exposes `use` for one-off use. It requires an interactive terminal, and its exact flags depend on the CLI version:

```bash
npx --yes skills@1.7.0 use https://github.com/naodeng/awesome-qa-skills --skill api-testing --agent codex
```

See the [Skills CLI integration guide](../docs/integrations/SKILLS_CLI_INTEGRATION_EN.md) for the repository's distribution contract and compatibility scope, and the [official CLI documentation](https://www.skills.sh/docs/cli) for basic usage.

## Use the repository installers

Choose a tool, language, and optional Skill. Add `--dry-run` to preview operations; a dry run does not write files.

### macOS / Linux

```bash
# Preview installing Chinese functional-testing to Codex
bash scripts/install-skills-mac.sh --tool codex --lang zh --skill functional-testing --dry-run

# Install one Chinese Skill
bash scripts/install-skills-mac.sh --tool codex --lang zh --skill functional-testing

# Install all English Skills supported by Cursor
bash scripts/install-skills-mac.sh --tool cursor --lang en

# Install to a custom directory
bash scripts/install-skills-mac.sh --tool codex --lang zh --dest /path/to/skills
```

### Windows (PowerShell)

```powershell
# Preview installing Chinese functional-testing to Codex
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill functional-testing -DryRun

# Install one Chinese Skill
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Skill functional-testing

# Install to a custom directory
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh -Dest C:\skills
```

The scripts accept these parameters:

| Parameter | Values | Description |
| --- | --- | --- |
| `--tool` / `-Tool` | `claude`, `claudecode`, `cursor`, `codex`, `kiro`, `opencode`, `trae`, `all` | Choose a target. `all` installs to every supported tool. |
| `--lang` / `-Lang` | `zh`, `en`, `all` | Choose Chinese, English, or both languages. |
| `--skill` / `-Skill` | A Skill directory name or `all` | Install one Skill by its canonical name or the full collection. |
| `--dest` / `-Dest` | A directory path | Override the tool's default target directory. |
| `--dry-run` / `-DryRun` | Switch | Show the planned copy operations without writing files. |

`--lang all` places the two language trees in separate `zh/` and `en/` subdirectories under the target. Use it only if the target tool discovers Skills in that layout; choose one language per tool target by default.

The scripts synchronize each Skill directory and replace an existing directory with the same name. Run a dry run first, and back up any files you edited in an installed Skill.

Default installer targets:

| Tool | macOS / Linux | Windows |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `%USERPROFILE%\.claude\skills\` |
| Cursor | `~/.cursor/skills/` | `%USERPROFILE%\.cursor\skills\` |
| Codex | `~/.codex/skills/` | `%USERPROFILE%\.codex\skills\` |
| Kiro | `~/.kiro/skills/` | `%USERPROFILE%\.kiro\skills\` |
| OpenCode | `~/.opencode/skills/` | `%USERPROFILE%\.opencode\skills\` |
| Trae | `~/.trae/skills/` | `%USERPROFILE%\.trae\skills\` |

With `--dest` / `-Dest`, the installer adds language, category, and Skill folders below the path, for example `<target>/zh/testing-types/functional-testing/`.

## Use a per-Skill shortcut

Shortcuts under `installers/` are generated by `scripts/generate-install-shortcuts.sh`. Do not edit generated files by hand. If you need to change their behavior, edit the generator and regenerate the directory. Run shortcuts from a repository checkout so they can read the Skill source files.

```bash
# macOS / Linux: install Chinese functional-testing to Codex
bash installers/zh/functional-testing/mac/codex.sh
```

```powershell
# Windows: install Chinese functional-testing to Codex
powershell -ExecutionPolicy Bypass -File .\installers\zh\functional-testing\windows\codex.ps1
```

Shortcut layout:

```text
installers/{zh|en}/{skill-name}/{mac|windows}/{tool-script}
```

## Copy a Skill manually

From the repository root, copy one Skill directory to the selected tool's Skills folder. This example installs the Chinese Skill for Codex:

```bash
mkdir -p ~/.codex/skills
cp -R skills/zh/testing-types/functional-testing ~/.codex/skills/functional-testing
```

PowerShell example:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\zh\testing-types\functional-testing" "$HOME\.codex\skills\functional-testing"
```

Replace `skills/zh/` with `skills/en/` for the English version. You can also select a Skill from `testing-workflows/` or `skill-engineering/`.

## Clone the full repository

To keep all Skills, documentation, and installer scripts in your project, clone the repository:

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git .skills/awesome-qa-skills
```

After cloning, choose Skills under `skills/zh/` or `skills/en/`. Cloning the repository does not install Skills into an AI tool's default directory.

## Add a Git submodule

Use a submodule to pin this repository's version in a Git project:

```bash
git submodule add https://github.com/naodeng/awesome-qa-skills.git .skills/awesome-qa-skills
```

## Community-recommended external Skills

The following Skills are maintained by other projects. They are listed for discovery, are not part of this repository's catalog, and have not been runtime-evaluated by this repository. Check each upstream source for current version, license, and tool compatibility.

### UIZZE anti-ui-slop

Checks whether an interface has a product-specific design contract, required states, and a pre-ship UX quality gate. The upstream source currently lists Apache-2.0, v1.3.1, and compatibility information for Claude Code, Codex, Cursor, and GitHub Copilot. See the [upstream Skill](https://github.com/uizze/uizze/tree/main/skills/anti-ui-slop) and [community submission](https://github.com/naodeng/awesome-qa-skills/issues/3).

```bash
npx skills add https://uizze.com --skill anti-ui-slop
```

### UI Verify triage-visual-changes

Triages visual differences after a UI Verify build, distinguishing real regressions, intended changes, and rendering noise. It requires a UI Verify account (a free tier is available) and MCP connection. The community submission lists UI Verify plugin v0.1.0 (checked 2026-10-19). See the [upstream Skill](https://github.com/uiverify/uiverify/tree/main/packages/skills/skills/triage-visual-changes) and [community submission](https://github.com/naodeng/awesome-qa-skills/issues/33).

```bash
npx skills add uiverify/uiverify --skill triage-visual-changes
```

For Claude Code, you can also use the plugin marketplace command: `/plugin marketplace add uiverify/uiverify`.

## Troubleshooting

- **The CLI cannot find a Chinese Skill:** use the GitHub source under `skills/zh` instead of the repository root.
- **The same Skill appears twice:** remove the other language version from the target and install only the language you need.
- **The tool does not discover an installed Skill:** verify the target path matches the tool configuration; when using the CLI, specify the agent with `-a` if needed.
- **You want to inspect what the script will copy:** run the repository installer with `--dry-run` first.
- **You need to reproduce the repository compatibility check:** use `skills@1.7.0` and see the [Skills CLI integration guide](../docs/integrations/SKILLS_CLI_INTEGRATION_EN.md).

## Related documentation

- [README: supported AI tools](../README_EN.md#supported-ai-tools)
- [Skills CLI integration guide](../docs/integrations/SKILLS_CLI_INTEGRATION_EN.md)
- [Workflow / Eval / installation synchronization checklist](../docs/governance/WORKFLOW_EVAL_INSTALL_SYNC_EN.md)
