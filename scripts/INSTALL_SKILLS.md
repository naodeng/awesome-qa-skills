# Skills One-Click Installer

This repository provides one-click installers for:
- Claude Code
- Cursor
- Codex
- Kiro
- OpenCode
- Trae

For the bilingual Workflow package list, Eval minimum, and installation synchronization checklist, see [`docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md`](../docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md).

## macOS / Linux

```bash
bash scripts/install-skills-mac.sh --tool all --lang all
```

Or run from the project root:

```bash
bash ./install-skills-mac.sh --tool all --lang all
```

Common usage:

```bash
# install Chinese skills to Codex
bash scripts/install-skills-mac.sh --tool codex --lang zh

# install all skills to Trae
bash scripts/install-skills-mac.sh --tool trae --lang all

# install English skills to Cursor (preview only)
bash scripts/install-skills-mac.sh --tool cursor --lang en --dry-run

# install only one skill
bash scripts/install-skills-mac.sh --tool codex --lang all --skill functional-testing

# install to custom path
bash scripts/install-skills-mac.sh --tool claude --lang all --dest /path/to/skills
```

## Windows (PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool all -Lang all
```

Or run from the project root:

```powershell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

Common usage:

```powershell
# install Chinese skills to Codex
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh

# install all skills to Trae
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool trae -Lang all

# install English skills to Cursor (preview only)
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool cursor -Lang en -DryRun

# install only one skill
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang all -Skill functional-testing

# install to custom path
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool claude -Lang all -Dest C:\skills
```

## Install with the Agent Skills CLI

The [`skills` CLI](https://www.skills.sh/docs/cli) is the recommended distribution path. Node.js is required. The repository-level source is English-first and the leaf directory is addressed by its canonical Skill name.

```bash
# install one English Skill
npx skills add naodeng/awesome-qa-skills --skill functional-testing

# optionally target Codex
npx skills add naodeng/awesome-qa-skills --skill functional-testing -a codex

# install the full English collection
npx skills add naodeng/awesome-qa-skills
```

Chinese is an explicit source selection because EN and ZH intentionally share canonical names:

```bash
# install one Chinese Skill
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing
```

### Advanced and CI-pinned commands

CI fixes the compatibility check to `skills@1.7.0`. Use the pinned form when reproducing CI or when a deterministic tool version is required:

```bash
# install functional-testing globally for Codex
npx --yes skills@1.7.0 add naodeng/awesome-qa-skills --skill functional-testing -g -a codex -y

# list project-scope records
npx --yes skills@1.7.0 list --json

# update global-scope records
npx --yes skills@1.7.0 update -g -y

# remove one global-scope Skill
npx --yes skills@1.7.0 remove functional-testing -g -y
```

For one-off use, the pinned CLI also exposes `use`; it requires an interactive terminal and its exact flags are version-dependent:

```bash
npx --yes skills@1.7.0 use https://github.com/naodeng/awesome-qa-skills --skill api-testing --agent codex
```

Replace `codex` with another agent name supported by the selected CLI version. Install one language at a time because the Chinese and English directories contain same-named Skills. The repository's Tested / Ecosystem compatible boundary and isolated smoke evidence are in [`docs/integrations/SKILLS_CLI_INTEGRATION.md`](../docs/integrations/SKILLS_CLI_INTEGRATION.md).

## Tool target defaults

- Claude Code: `~/.claude/skills` (Windows: `%USERPROFILE%\.claude\skills`)
- Cursor: `~/.cursor/skills` (Windows: `%USERPROFILE%\.cursor\skills`)
- Codex: `~/.codex/skills` (Windows: `%USERPROFILE%\.codex\skills`)
- Kiro: `~/.kiro/skills` (Windows: `%USERPROFILE%\.kiro\skills`)
- OpenCode: `~/.opencode/skills` (Windows: `%USERPROFILE%\.opencode\skills`)
- Trae: `~/.trae/skills` (Windows: `%USERPROFILE%\.trae\skills`)

## Notes

- The CLI is the preferred distribution path, not a runtime dependency.
- Existing manual, macOS/Linux, and Windows installers remain supported as fallback/maintenance-mode paths.
- A command is guaranteed only for the pinned version or when marked version-dependent; run `npx --yes skills@<version> --help` before changing the pin.
- Do not install both `skills/en` and `skills/zh` into one unverified target: their canonical names intentionally overlap.

- Source directories:
  - `skills/zh/testing-types`
  - `skills/zh/testing-workflows`
  - `skills/zh/skill-engineering`
  - `skills/en/testing-types`
  - `skills/en/testing-workflows`
  - `skills/en/skill-engineering`
- Per-skill one-click installers are generated under:
  - `installers/{lang}/{skill-name}/mac/{tool}.sh`
  - `installers/{lang}/{skill-name}/windows/{tool}.ps1`
  - These shortcut installers are generated files and should be run from this repository checkout so they can resolve `skills/{lang}/...` by relative path. Use the root scripts when you need a custom destination or a portable command.
- `--skill` uses canonical skill names from language directories.
  - Chinese example: `functional-testing`
  - English example: `functional-testing`
- `claude` and `claudecode` point to the same install target.
- Install target layout:
  - `.../skills/zh/testing-types/...`
  - `.../skills/en/testing-types/...`
  - (same for `testing-workflows`)
  - (same for `skill-engineering`)
