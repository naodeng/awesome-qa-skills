$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceRepo = "/Users/nao.deng/awsomeCode/awesome-qa-skills"
$LocalScript = Join-Path $ScriptDir "scripts\install-skills-windows.ps1"

if (Test-Path $LocalScript) {
  & $LocalScript @args
  exit $LASTEXITCODE
}

& (Join-Path $SourceRepo "scripts\install-skills-windows.ps1") @args
exit $LASTEXITCODE
