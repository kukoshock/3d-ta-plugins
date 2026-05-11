# Thin wrapper for local builds on Windows.
# All logic lives in build_skills.py so this and build-skills.sh stay in sync.
$ErrorActionPreference = "Stop"
$script = Join-Path $PSScriptRoot "build_skills.py"
$py = if (Get-Command python -ErrorAction SilentlyContinue) { "python" } else { "py" }
& $py $script @args
exit $LASTEXITCODE
