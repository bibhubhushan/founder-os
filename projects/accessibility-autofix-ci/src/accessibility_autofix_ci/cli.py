"""CLI for accessibility-autofix-ci."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from linter import lint_html


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 src/accessibility_autofix_ci/cli.py <page.html>")
        return 1

    content = Path(argv[1]).read_text()
    issues = lint_html(content)

    if not issues:
        print("No accessibility issues found.")
        return 0

    print(json.dumps({"issues": issues}, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
