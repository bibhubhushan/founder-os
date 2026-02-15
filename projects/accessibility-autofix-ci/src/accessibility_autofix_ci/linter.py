"""Simple HTML accessibility checks and fixes."""

from __future__ import annotations

from html.parser import HTMLParser


class AccessibilityParser(HTMLParser):
    """Collect basic accessibility issues while parsing HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.issues: list[dict[str, str]] = []
        self._button_depth = 0
        self._button_text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}

        if tag == "img" and not attr_map.get("alt", "").strip():
            self.issues.append(
                {
                    "rule": "img-alt",
                    "message": "Image tag missing alt text",
                    "fix": "Add descriptive alt attribute to img element",
                }
            )

        if tag == "button":
            self._button_depth += 1
            self._button_text = ""

    def handle_data(self, data: str) -> None:
        if self._button_depth > 0:
            self._button_text += data.strip()

    def handle_endtag(self, tag: str) -> None:
        if tag == "button" and self._button_depth > 0:
            if not self._button_text.strip():
                self.issues.append(
                    {
                        "rule": "button-name",
                        "message": "Button has no accessible text",
                        "fix": "Add visible text or aria-label to button",
                    }
                )
            self._button_depth -= 1
            self._button_text = ""


def lint_html(content: str) -> list[dict[str, str]]:
    parser = AccessibilityParser()
    parser.feed(content)
    return parser.issues
