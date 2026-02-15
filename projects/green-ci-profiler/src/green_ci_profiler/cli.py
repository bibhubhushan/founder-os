"""CLI for green-ci-profiler."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from profiler import optimization_hint, summarize_steps


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 src/green_ci_profiler/cli.py <run.json>")
        return 1

    payload = json.loads(Path(argv[1]).read_text())
    steps = payload.get("steps", [])
    summary = summarize_steps(steps)

    print(json.dumps(summary, indent=2))
    print(f"hint: {optimization_hint(str(summary['top_step']))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
