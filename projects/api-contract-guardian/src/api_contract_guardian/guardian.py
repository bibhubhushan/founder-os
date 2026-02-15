"""Contract diff logic for API snapshots."""

from __future__ import annotations


def _paths(spec: dict) -> dict:
    return spec.get("paths", {})


def find_breaking_changes(old_spec: dict, new_spec: dict) -> list[str]:
    changes: list[str] = []

    old_paths = _paths(old_spec)
    new_paths = _paths(new_spec)

    for path_name, old_methods in old_paths.items():
        if path_name not in new_paths:
            changes.append(f"Removed path: {path_name}")
            continue

        new_methods = new_paths[path_name]
        for method_name, old_def in old_methods.items():
            if method_name not in new_methods:
                changes.append(f"Removed method: {method_name.upper()} {path_name}")
                continue

            old_required = set(old_def.get("request_required", []))
            new_required = set(new_methods[method_name].get("request_required", []))
            removed_required = sorted(old_required - new_required)
            if removed_required:
                label = ", ".join(removed_required)
                changes.append(
                    f"Request schema mismatch {method_name.upper()} {path_name}: removed required {label}"
                )

    return changes


def has_breaking_changes(old_spec: dict, new_spec: dict) -> bool:
    return len(find_breaking_changes(old_spec, new_spec)) > 0
