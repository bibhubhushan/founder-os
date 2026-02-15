"""Core prompt evaluation logic."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvalCase:
    """One evaluation case for a prompt output."""

    name: str
    output_text: str
    expected_keywords: tuple[str, ...]
    forbidden_keywords: tuple[str, ...]
    min_score: float = 0.6


@dataclass(frozen=True)
class EvalResult:
    """Result of one evaluation run."""

    name: str
    score: float
    passed: bool
    hit_keywords: tuple[str, ...]
    forbidden_hits: tuple[str, ...]


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())


def _keyword_hits(text: str, keywords: Iterable[str]) -> tuple[str, ...]:
    normalized = _normalize(text)
    hits = [keyword for keyword in keywords if keyword.lower() in normalized]
    return tuple(hits)


def evaluate_case(case: EvalCase) -> EvalResult:
    """Score a single case with expected and forbidden keyword rules."""

    hit_keywords = _keyword_hits(case.output_text, case.expected_keywords)
    forbidden_hits = _keyword_hits(case.output_text, case.forbidden_keywords)

    expected_total = max(len(case.expected_keywords), 1)
    base_score = len(hit_keywords) / expected_total

    penalty = 0.2 * len(forbidden_hits)
    final_score = max(0.0, min(1.0, base_score - penalty))

    return EvalResult(
        name=case.name,
        score=round(final_score, 3),
        passed=final_score >= case.min_score,
        hit_keywords=hit_keywords,
        forbidden_hits=forbidden_hits,
    )


def evaluate_suite(cases: Iterable[EvalCase]) -> tuple[EvalResult, ...]:
    """Evaluate all cases and return immutable results."""

    return tuple(evaluate_case(case) for case in cases)


def suite_score(results: Iterable[EvalResult]) -> float:
    """Return average score across a suite."""

    items = tuple(results)
    if not items:
        return 0.0
    average = sum(item.score for item in items) / len(items)
    return round(average, 3)
