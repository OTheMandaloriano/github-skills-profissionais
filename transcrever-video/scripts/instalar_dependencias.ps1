[CmdletBinding(SupportsShouldProcess)]
param(
  [switch]$Check,
  [switch]$Upgrade
)

$ErrorActionPreference = 'Stop'

$skillRoot = Split-Path -Parent $PSScriptRoot
$requirements = Join-Path $skillRoot 'requirements.txt'

function Get-PythonLauncher {
  # Prefere o "python" do PATH; ignora o atalho da Microsoft Store.
  $python = Get-Command 'python' -ErrorAction SilentlyContinue
  if ($python -and $python.Source -notlike '*WindowsApps*') {
    return @{ Exe = $python.Source; Prefix = @() }
  }

  $py = Get-Command 'py' -ErrorAction SilentlyContinue
  if ($py) { return @{ Exe = $py.Source; Prefix = @('-3') } }

  throw 'Python 3 nao encontrado no PATH. Instale em https://www.python.org/downloads/ e marque "Add python.exe to PATH".'
}

function Invoke-Python {
  param($Launcher, [string[]]$Arguments)
  & $Launcher.Exe @($Launcher.Prefix + $Arguments)
}

function Test-Modules {
  param($Launcher)
  $code = "import importlib.util as u, sys; sys.exit(0 if all(u.find_spec(m) for m in ('faster_whisper','yt_dlp')) else 1)"
  Invoke-Python $Launcher @('-c', $code) | Out-Null
  return ($LASTEXITCODE -eq 0)
}

function Get-Ffmpeg {
  param($Launcher)
  $path = (Get-Command 'ffmpeg' -ErrorAction SilentlyContinue).Source
  if ($path) { return $path }
  $code = "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
  $embedded = Invoke-Python $Launcher @('-c', $code) 2>$null
  if ($LASTEXITCODE -eq 0 -and $embedded) { return ($embedded | Select-Object -Last 1).Trim() }
  return $null
}

$python = Get-PythonLauncher
$version = (Invoke-Python $python @('-c', "import sys; print(sys.version.split()[0])") | Select-Object -Last 1).Trim()
Write-Host "Python: $version ($($python.Exe))"

if ([version]$version -lt [version]'3.9') {
  throw "Python 3.9 ou superior e necessario. Encontrado: $version"
}

$modulesOk = Test-Modules $python
$ffmpegPath = Get-Ffmpeg $python

if ($Check) {
  Write-Host ("{0} faster-whisper + yt-dlp" -f $(if ($modulesOk) { 'OK   ' } else { 'FALTA' }))
  Write-Host ("{0} ffmpeg: {1}" -f $(if ($ffmpegPath) { 'OK   ' } else { 'FALTA' }), $(if ($ffmpegPath) { $ffmpegPath } else { 'nao encontrado' }))
  if ($modulesOk -and $ffmpegPath) { exit 0 } else { exit 1 }
}

if (-not $modulesOk) {
  if (-not (Test-Path -LiteralPath $requirements)) {
    throw "requirements.txt nao encontrado em $skillRoot"
  }
  $pipArgs = @('-m', 'pip', 'install', '--user', '--disable-pip-version-check', '-r', $requirements)
  if ($Upgrade) { $pipArgs += '--upgrade' }

  if ($PSCmdlet.ShouldProcess('faster-whisper, yt-dlp, imageio-ffmpeg', 'pip install --user')) {
    Invoke-Python $python $pipArgs
    if ($LASTEXITCODE -ne 0) { throw "pip falhou com codigo $LASTEXITCODE" }
    $modulesOk = Test-Modules $python
  }
}

if (-not $ffmpegPath) { $ffmpegPath = Get-Ffmpeg $python }

if ($modulesOk -and $ffmpegPath) {
  Write-Host "Dependencias prontas. ffmpeg: $ffmpegPath"
  exit 0
}

Write-Warning 'Ainda falta algo. Rode novamente com -Check para ver o status.'
exit 1
