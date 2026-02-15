"""CLI for prompt-eval-lab."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from evaluator import EvalCase, evaluate_suite, suite_score


def _load_cases(path: Path) -> tuple[EvalCase, ...]:
    payload = json.loads(path.read_text())
    cases = []
    for item in payload["cases"]:
        cases.append(
            EvalCase(
                name=item["name"],
                output_text=item["output_text"],
                expected_keywords=tuple(item.get("expected_keywords", [])),
                forbidden_keywords=tuple(item.get("forbidden_keywords", [])),
                min_score=float(item.get("min_score", 0.6)),
            )
        )
    return tuple(cases)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 src/prompt_eval_lab/cli.py <cases.json>")
        return 1

    cases_file = Path(argv[1])
    cases = _load_cases(cases_file)
    results = evaluate_suite(cases)

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.name}: score={result.score}")

    average = suite_score(results)
    print(f"Suite score: {average}")

    return 0 if all(result.passed for result in results) else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
