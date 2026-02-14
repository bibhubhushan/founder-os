#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-8787}"
python3 app/server.py --port "$PORT"
