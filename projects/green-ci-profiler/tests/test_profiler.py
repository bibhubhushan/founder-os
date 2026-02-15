"""Tests for green-ci-profiler."""

import unittest

from src.green_ci_profiler.profiler import optimization_hint, summarize_steps


class ProfilerTests(unittest.TestCase):
    def test_should_compute_total_duration(self) -> None:
        summary = summarize_steps([
            {"name": "lint", "duration_ms": 1000},
            {"name": "test", "duration_ms": 2000},
        ])

        self.assertEqual(summary["total_ms"], 3000)
        self.assertEqual(summary["top_step"], "test")

    def test_should_give_test_hint_for_test_stage(self) -> None:
        hint = optimization_hint("unit-test")
        self.assertIn("Shard tests", hint)


if __name__ == "__main__":
    unittest.main()
