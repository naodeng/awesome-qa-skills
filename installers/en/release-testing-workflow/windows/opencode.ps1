$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LocalRepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..\..") -ErrorAction SilentlyContinue
$LocalScript = if ($LocalRepoRoot) { Join-Path $LocalRepoRoot "install-skills-windows.ps1" } else { $null }

if ($LocalScript -and (Test-Path $LocalScript)) {
  & $LocalScript -Tool "opencode" -Lang "en" -Skill "release-testing-workflow" @args
  exit $LASTEXITCODE
}

Write-Error "Installer wrapper not found: $LocalScript"
exit 1
