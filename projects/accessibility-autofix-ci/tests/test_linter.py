"""Tests for accessibility linter."""

import unittest

from src.accessibility_autofix_ci.linter import lint_html


class LinterTests(unittest.TestCase):
    def test_should_flag_img_without_alt(self) -> None:
        issues = lint_html("<img src='x.png'>")
        self.assertTrue(any(item["rule"] == "img-alt" for item in issues))

    def test_should_flag_empty_button(self) -> None:
        issues = lint_html("<button></button>")
        self.assertTrue(any(item["rule"] == "button-name" for item in issues))

    def test_should_pass_when_accessible_markup_present(self) -> None:
        issues = lint_html("<img src='x.png' alt='preview'><button>Save</button>")
        self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
