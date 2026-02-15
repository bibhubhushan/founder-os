"""Tests for API contract guardian."""

import unittest

from src.api_contract_guardian.guardian import find_breaking_changes, has_breaking_changes


class GuardianTests(unittest.TestCase):
    def test_should_detect_removed_method(self) -> None:
        old = {"paths": {"/users": {"post": {"request_required": ["email"]}}}}
        new = {"paths": {"/users": {}}}

        changes = find_breaking_changes(old, new)

        self.assertTrue(any("Removed method" in item for item in changes))

    def test_should_detect_removed_required_field(self) -> None:
        old = {"paths": {"/users": {"post": {"request_required": ["email", "name"]}}}}
        new = {"paths": {"/users": {"post": {"request_required": ["email"]}}}}

        self.assertTrue(has_breaking_changes(old, new))


if __name__ == "__main__":
    unittest.main()
