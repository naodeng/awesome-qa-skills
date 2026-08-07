$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LocalRepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..\..") -ErrorAction SilentlyContinue
$LocalScript = if ($LocalRepoRoot) { Join-Path $LocalRepoRoot "install-skills-windows.ps1" } else { $null }

if ($LocalScript -and (Test-Path $LocalScript)) {
  & $LocalScript -Tool "opencode" -Lang "zh" -Skill "test-case-reviewer" @args
  exit $LASTEXITCODE
}

Write-Error "Installer wrapper not found: $LocalScript"
exit 1
