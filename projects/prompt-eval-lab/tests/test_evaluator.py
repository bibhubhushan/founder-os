"""Tests for evaluator module."""

import unittest

from src.prompt_eval_lab.evaluator import EvalCase, evaluate_case, suite_score


class EvaluatorTests(unittest.TestCase):
    def test_should_pass_when_expected_keywords_hit(self) -> None:
        case = EvalCase(
            name="happy",
            output_text="Includes setup and testing steps.",
            expected_keywords=("setup", "testing"),
            forbidden_keywords=("skip",),
            min_score=0.8,
        )

        result = evaluate_case(case)

        self.assertTrue(result.passed)
        self.assertEqual(result.score, 1.0)

    def test_should_penalize_when_forbidden_term_present(self) -> None:
        case = EvalCase(
            name="risky",
            output_text="Do setup but skip testing.",
            expected_keywords=("setup", "testing"),
            forbidden_keywords=("skip testing",),
            min_score=0.9,
        )

        result = evaluate_case(case)

        self.assertFalse(result.passed)
        self.assertLessEqual(result.score, 0.8)

    def test_should_compute_suite_average(self) -> None:
        self.assertEqual(suite_score(()), 0.0)


if __name__ == "__main__":
    unittest.main()
