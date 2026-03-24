param(
  [ValidateSet("claude", "cursor", "codex", "kiro", "opencode", "all")]
  [string]$Tool = "all",

  [ValidateSet("zh", "en", "all")]
  [string]$Lang = "all",

  [string]$Skill = "all",

  [string]$Dest = "",

  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..")
$SkillsRoot = Join-Path $RepoRoot "skills"

function Get-DefaultDestForTool {
  param([string]$ToolName)
  switch ($ToolName) {
    "claude"  { return (Join-Path $HOME ".claude\skills") }
    "cursor"  { return (Join-Path $HOME ".cursor\skills") }
    "codex"   { return (Join-Path $HOME ".codex\skills") }
    "kiro"    { return (Join-Path $HOME ".kiro\skills") }
    "opencode"{ return (Join-Path $HOME ".opencode\skills") }
    default   { throw "Unsupported tool: $ToolName" }
  }
}

function Get-SkillDirs {
  param(
    [string]$SectionDir,
    [string]$LangFilter
  )
  if (-not (Test-Path $SectionDir)) { return @() }
  $dirs = Get-ChildItem -Path $SectionDir -Directory
  if ($LangFilter -eq "zh") {
    $dirs = $dirs | Where-Object { $_.Name -notlike "*-en" }
  }
  elseif ($LangFilter -eq "en") {
    $dirs = $dirs | Where-Object { $_.Name -like "*-en" }
  }
  if ($Skill -ne "all") {
    $dirs = $dirs | Where-Object { $_.Name -eq $Skill }
  }
  return $dirs
}

function Sync-SkillDir {
  param(
    [string]$Source,
    [string]$Target
  )
  if ($DryRun) {
    Write-Host "[DRY-RUN] copy $Source -> $Target"
    return
  }

  $targetParent = Split-Path -Parent $Target
  if (-not (Test-Path $targetParent)) {
    New-Item -ItemType Directory -Path $targetParent | Out-Null
  }

  if (Test-Path $Target) {
    Remove-Item -Recurse -Force $Target
  }
  New-Item -ItemType Directory -Path $Target | Out-Null
  Copy-Item -Recurse -Force (Join-Path $Source "*") $Target
}

function Install-ForTool {
  param([string]$ToolName)

  $targetRoot = $Dest
  if ([string]::IsNullOrWhiteSpace($targetRoot)) {
    $targetRoot = Get-DefaultDestForTool -ToolName $ToolName
  }

  Write-Host "==> Installing skills for tool: $ToolName"
  Write-Host "    Target: $targetRoot"
  Write-Host "    Language: $Lang"

  $sections = @("testing-types", "testing-workflows")
  foreach ($section in $sections) {
    $sectionDir = Join-Path $SkillsRoot $section
    $skillDirs = Get-SkillDirs -SectionDir $sectionDir -LangFilter $Lang
    foreach ($skillDir in $skillDirs) {
      $dst = Join-Path (Join-Path $targetRoot $section) $skillDir.Name
      Sync-SkillDir -Source $skillDir.FullName -Target $dst
    }
  }
}

if (-not (Test-Path (Join-Path $SkillsRoot "testing-types")) -or -not (Test-Path (Join-Path $SkillsRoot "testing-workflows"))) {
  throw "skills source not found under: $SkillsRoot"
}

$tools = @()
if ($Tool -eq "all") {
  $tools = @("claude", "cursor", "codex", "kiro", "opencode")
} else {
  $tools = @($Tool)
}

foreach ($t in $tools) {
  Install-ForTool -ToolName $t
}

if ($DryRun) {
  Write-Host "Dry-run completed. No files were written."
} else {
  Write-Host "Installation completed."
}
