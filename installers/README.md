# Skill Installers

This directory contains one-click installers for every skill.

Generated directory: edit `scripts/generate-install-shortcuts.sh`, then regenerate this directory instead of hand-editing installer files.

Structure:

```text
installers/{lang}/{skill-name}/{os}/{tool-script}
```

Examples:

- `installers/zh/functional-testing/mac/codex.sh`
- `installers/zh/functional-testing/windows/codex.ps1`
- `installers/en/discover-testing/mac/trae.sh`
- `installers/en/discover-testing/windows/claudecode.ps1`

Supported tools:

- codex
- cursor
- claudecode
- kiro
- opencode
- trae

Supported systems:

- mac
- windows

Generated skills: 76
Generated scripts: 912
