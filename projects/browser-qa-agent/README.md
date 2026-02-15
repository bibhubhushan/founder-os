# browser-qa-agent

Browser test failure triage helper for CI runs.

## Features
- Failure category classification
- Severity prioritization
- Action item generation
- CLI for report JSON

## Run
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 src/browser_qa_agent/cli.py examples/report.json
```
