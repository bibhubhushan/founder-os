"""Tests for triage rules."""

import unittest

from src.browser_qa_agent.triage import Failure, classify_failure, triage_failure


class TriageTests(unittest.TestCase):
    def test_should_classify_timeout_as_locator_timeout(self) -> None:
        self.assertEqual(classify_failure("Timeout waiting for locator"), "locator_timeout")

    def test_should_classify_connection_issue_as_network(self) -> None:
        self.assertEqual(classify_failure("Connection reset by peer"), "network")

    def test_should_return_high_for_network_and_auth(self) -> None:
        result = triage_failure(Failure(test_name="a", message="401 unauthorized"))
        self.assertEqual(result["severity"], "high")


if __name__ == "__main__":
    unittest.main()
