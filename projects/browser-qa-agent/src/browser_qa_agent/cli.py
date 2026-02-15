"""CLI for browser-qa-agent."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from triage import Failure, triage_failure


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 src/browser_qa_agent/cli.py <report.json>")
        return 1

    payload = json.loads(Path(argv[1]).read_text())
    failures = payload.get("failures", [])

    triaged = [triage_failure(Failure(test_name=item["test_name"], message=item["message"])) for item in failures]

    for item in triaged:
        print(f"[{item['severity'].upper()}] {item['test_name']} -> {item['category']}")
        print(f"  action: {item['action']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
