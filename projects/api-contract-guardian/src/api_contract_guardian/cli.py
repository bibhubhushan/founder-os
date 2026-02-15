"""CLI for api-contract-guardian."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from guardian import find_breaking_changes


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: python3 src/api_contract_guardian/cli.py <old.json> <new.json>")
        return 1

    old_spec = json.loads(Path(argv[1]).read_text())
    new_spec = json.loads(Path(argv[2]).read_text())

    changes = find_breaking_changes(old_spec, new_spec)
    if not changes:
        print("No breaking changes detected.")
        return 0

    print("Breaking changes:")
    for change in changes:
        print(f"- {change}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
