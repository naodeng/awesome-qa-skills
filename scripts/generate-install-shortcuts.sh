#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_ROOT="$REPO_ROOT/skills"
TARGET_ROOT="$REPO_ROOT/installers"
SOURCE_REPO="$REPO_ROOT"

TOOLS=(codex cursor claudecode kiro opencode trae)
LANGS=(zh en)

mkdir -p "$TARGET_ROOT"

write_mac_script() {
  local lang="$1"
  local skill="$2"
  local tool="$3"
  local file="$4"

  cat >"$file" <<EOF
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"
LOCAL_REPO_ROOT="\$(cd "\$SCRIPT_DIR/../../../../" && pwd)"
SOURCE_REPO="$SOURCE_REPO"

if [[ -x "\$LOCAL_REPO_ROOT/install-skills-mac.sh" ]]; then
  exec bash "\$LOCAL_REPO_ROOT/install-skills-mac.sh" --tool "$tool" --lang "$lang" --skill "$skill" "\$@"
fi

exec bash "\$SOURCE_REPO/install-skills-mac.sh" --tool "$tool" --lang "$lang" --skill "$skill" "\$@"
EOF
  chmod +x "$file"
}

write_windows_script() {
  local lang="$1"
  local skill="$2"
  local tool="$3"
  local file="$4"

  cat >"$file" <<EOF
\$ScriptDir = Split-Path -Parent \$MyInvocation.MyCommand.Path
\$SourceRepo = "$SOURCE_REPO"
\$LocalRepoRoot = Resolve-Path (Join-Path \$ScriptDir "..\..\..\..") -ErrorAction SilentlyContinue
\$LocalScript = if (\$LocalRepoRoot) { Join-Path \$LocalRepoRoot "install-skills-windows.ps1" } else { \$null }

if (\$LocalScript -and (Test-Path \$LocalScript)) {
  & \$LocalScript -Tool "$tool" -Lang "$lang" -Skill "$skill" @args
  exit \$LASTEXITCODE
}

& (Join-Path \$SourceRepo "install-skills-windows.ps1") -Tool "$tool" -Lang "$lang" -Skill "$skill" @args
exit \$LASTEXITCODE
EOF
}

skill_count=0
script_count=0

for lang in "${LANGS[@]}"; do
  while IFS= read -r skill_dir; do
    [[ -n "$skill_dir" ]] || continue
    skill_name="$(basename "$skill_dir")"
    ((skill_count+=1))

    mac_dir="$TARGET_ROOT/$lang/$skill_name/mac"
    windows_dir="$TARGET_ROOT/$lang/$skill_name/windows"
    mkdir -p "$mac_dir" "$windows_dir"

    for tool in "${TOOLS[@]}"; do
      write_mac_script "$lang" "$skill_name" "$tool" "$mac_dir/$tool.sh"
      write_windows_script "$lang" "$skill_name" "$tool" "$windows_dir/$tool.ps1"
      ((script_count+=2))
    done
  done < <(find "$SKILLS_ROOT/$lang" -mindepth 2 -maxdepth 2 -type d | sort)
done

cat >"$TARGET_ROOT/README.md" <<EOF
# Skill Installers

This directory contains one-click installers for every skill.

Structure:

\`\`\`
installers/{lang}/{skill-name}/{os}/{tool-script}
\`\`\`

Examples:

- \`installers/zh/functional-testing/mac/codex.sh\`
- \`installers/zh/functional-testing/windows/codex.ps1\`
- \`installers/en/discover-testing/mac/trae.sh\`
- \`installers/en/discover-testing/windows/claudecode.ps1\`

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

Generated skills: $skill_count
Generated scripts: $script_count
EOF

echo "generated_skills=$skill_count"
echo "generated_scripts=$script_count"
