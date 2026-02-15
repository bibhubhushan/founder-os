# prompt-eval-lab

Prompt regression harness with deterministic scoring.

## Features
- Keyword hit scoring with forbidden-term penalties
- Pass/fail gate per case
- Suite-level score summary
- CLI for JSON-based evaluation

## Run
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 src/prompt_eval_lab/cli.py examples/cases.json
```
