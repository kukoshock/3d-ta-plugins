#!/usr/bin/env bash
# Thin wrapper used by the GitHub Actions release workflow.
# All logic lives in build_skills.py so the Windows (PowerShell) wrapper and
# the CI (Bash) wrapper produce byte-identical output.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$HERE/build_skills.py" "$@"
