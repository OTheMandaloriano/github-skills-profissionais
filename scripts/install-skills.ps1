[CmdletBinding(SupportsShouldProcess)]
param(
  [ValidateSet('Codex', 'Claude', 'OpenCode', 'All')]
  [string]$Target = 'All',
  [switch]$Force,
  [string]$HomePath = $HOME
)

$ErrorActionPreference = 'Stop'
$HomePath = [IO.Path]::GetFullPath($HomePath)
$homeRoot = [IO.Path]::GetPathRoot($HomePath)
if ($HomePath.TrimEnd('\', '/') -eq $homeRoot.TrimEnd('\', '/')) {
  throw 'Diretório de usuário inválido. Informe uma pasta de usuário, não a raiz do disco.'
}
$repositoryRoot = Split-Path -Parent $PSScriptRoot

# Descobre as skills pela presença de SKILL.md: adicionar uma pasta nova
# no repositório já a torna instalável, sem editar este script.
$skills = @(
  Get-ChildItem -LiteralPath $repositoryRoot -Directory |
    Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') } |
    Sort-Object Name |
    Select-Object -ExpandProperty Name
)
if ($skills.Count -eq 0) {
  throw "Nenhuma skill encontrada em $repositoryRoot (procure por pastas com SKILL.md)."
}

$targets = @{
  Codex = Join-Path $HomePath '.codex\skills'
  Claude = Join-Path $HomePath '.claude\skills'
  OpenCode = Join-Path $HomePath '.config\opencode\skills'
}

$selectedTargets = if ($Target -eq 'All') { $targets.Keys } else { @($Target) }
$plan = @()

foreach ($platform in $selectedTargets) {
  $destinationRoot = $targets[$platform]
  foreach ($skill in $skills) {
    $source = Join-Path $repositoryRoot $skill
    $destination = Join-Path $destinationRoot $skill

    if (!(Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) {
      throw "Skill de origem não encontrada: $source"
    }
    if ((Test-Path -LiteralPath $destination) -and !$Force) {
      throw "A skill já existe em $destination. Revise-a e execute novamente com -Force para atualizar apenas seus arquivos."
    }
    $plan += [PSCustomObject]@{
      Platform = $platform
      Skill = $skill
      Source = $source
      DestinationRoot = $destinationRoot
      Destination = $destination
    }
  }
}

Write-Host ("Skills encontradas: {0}" -f ($skills -join ', '))

foreach ($item in $plan) {
  if ($PSCmdlet.ShouldProcess($item.Destination, "Instalar $($item.Skill) para $($item.Platform)")) {
    New-Item -ItemType Directory -Path $item.DestinationRoot -Force | Out-Null
    Copy-Item -LiteralPath $item.Source -Destination $item.DestinationRoot -Recurse -Force
    Write-Host "Instalada: $($item.Platform) -> $($item.Destination)"
  }
}
