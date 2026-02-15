# accessibility-autofix-ci

HTML accessibility linting with deterministic autofix suggestions.

## Features
- Detects missing image alt text
- Detects button elements without visible text/labels
- Emits machine-readable suggestions for CI comments

## Run
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 src/accessibility_autofix_ci/cli.py examples/page.html
```
