"""Failure triage rules for browser automation output."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Failure:
    test_name: str
    message: str


def classify_failure(message: str) -> str:
    normalized = message.lower()

    if "timeout" in normalized or "locator" in normalized:
        return "locator_timeout"
    if "net::" in normalized or "connection" in normalized:
        return "network"
    if "401" in normalized or "403" in normalized or "unauthorized" in normalized:
        return "auth"
    if "expect(" in normalized or "assert" in normalized:
        return "assertion"
    return "unknown"


def severity_for_category(category: str) -> str:
    if category in {"auth", "network"}:
        return "high"
    if category in {"locator_timeout", "assertion"}:
        return "medium"
    return "low"


def action_for_category(category: str) -> str:
    if category == "locator_timeout":
        return "Stabilize selectors and add deterministic wait conditions."
    if category == "network":
        return "Mock network dependencies and retry transient calls."
    if category == "auth":
        return "Validate test credentials and auth token setup."
    if category == "assertion":
        return "Update assertion target or repair broken UI/data assumptions."
    return "Capture trace and screenshot, then inspect flaky context."


def triage_failure(failure: Failure) -> dict[str, str]:
    category = classify_failure(failure.message)
    return {
        "test_name": failure.test_name,
        "category": category,
        "severity": severity_for_category(category),
        "action": action_for_category(category),
    }
