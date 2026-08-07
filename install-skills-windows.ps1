$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LocalScript = Join-Path $ScriptDir "scripts\install-skills-windows.ps1"

if (Test-Path $LocalScript) {
  & $LocalScript @args
  exit $LASTEXITCODE
}

Write-Error "Installer implementation not found: $LocalScript"
exit 1
