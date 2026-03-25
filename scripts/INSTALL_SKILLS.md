# Skills One-Click Installer

This repository provides one-click installers for:
- Claude Code
- Cursor
- Codex
- Kiro
- OpenCode

## macOS / Linux

```bash
bash scripts/install-skills-mac.sh --tool all --lang all
```

Common usage:

```bash
# install Chinese skills to Codex
bash scripts/install-skills-mac.sh --tool codex --lang zh

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

Common usage:

```powershell
# install Chinese skills to Codex
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh

# install English skills to Cursor (preview only)
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool cursor -Lang en -DryRun

# install only one skill
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang all -Skill functional-testing

# install to custom path
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool claude -Lang all -Dest C:\skills
```

## Tool target defaults

- Claude Code: `~/.claude/skills` (Windows: `%USERPROFILE%\.claude\skills`)
- Cursor: `~/.cursor/skills` (Windows: `%USERPROFILE%\.cursor\skills`)
- Codex: `~/.codex/skills` (Windows: `%USERPROFILE%\.codex\skills`)
- Kiro: `~/.kiro/skills` (Windows: `%USERPROFILE%\.kiro\skills`)
- OpenCode: `~/.opencode/skills` (Windows: `%USERPROFILE%\.opencode\skills`)

## Notes

- Source directories:
  - `skills/zh/testing-types`
  - `skills/zh/testing-workflows`
  - `skills/en/testing-types`
  - `skills/en/testing-workflows`
- `--skill` uses canonical skill names from language directories.
  - Chinese example: `functional-testing`
  - English example: `functional-testing`
- Install target layout:
  - `.../skills/zh/testing-types/...`
  - `.../skills/en/testing-types/...`
  - (same for `testing-workflows`)
