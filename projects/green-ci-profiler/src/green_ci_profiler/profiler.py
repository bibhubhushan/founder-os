"""CI profiling and energy estimation helpers."""

from __future__ import annotations

ENERGY_PER_MINUTE_WH = 2.8


def summarize_steps(steps: list[dict[str, int | str]]) -> dict[str, object]:
    total_ms = sum(int(step["duration_ms"]) for step in steps)
    total_minutes = total_ms / 60000
    total_energy_wh = round(total_minutes * ENERGY_PER_MINUTE_WH, 2)

    ranked = sorted(steps, key=lambda step: int(step["duration_ms"]), reverse=True)
    top_step = ranked[0]["name"] if ranked else "none"

    return {
        "total_ms": total_ms,
        "total_minutes": round(total_minutes, 2),
        "estimated_energy_wh": total_energy_wh,
        "top_step": top_step,
    }


def optimization_hint(step_name: str) -> str:
    normalized = step_name.lower()
    if "test" in normalized:
        return "Shard tests and cache dependencies for the test stage."
    if "build" in normalized:
        return "Enable incremental build cache and trim artifact scope."
    if "lint" in normalized:
        return "Run changed-files lint mode before full lint sweep."
    return "Profile this step with timing breakdown and remove idle waits."
