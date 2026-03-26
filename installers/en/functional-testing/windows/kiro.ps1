$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceRepo = "/Users/nao.deng/awsomeCode/awesome-qa-skills"
$LocalRepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..\..") -ErrorAction SilentlyContinue
$LocalScript = if ($LocalRepoRoot) { Join-Path $LocalRepoRoot "install-skills-windows.ps1" } else { $null }

if ($LocalScript -and (Test-Path $LocalScript)) {
  & $LocalScript -Tool "kiro" -Lang "en" -Skill "functional-testing" @args
  exit $LASTEXITCODE
}

& (Join-Path $SourceRepo "install-skills-windows.ps1") -Tool "kiro" -Lang "en" -Skill "functional-testing" @args
exit $LASTEXITCODE
