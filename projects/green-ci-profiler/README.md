# green-ci-profiler

CI step profiler that estimates energy and identifies optimization targets.

## Features
- Aggregates step durations
- Estimates relative energy usage
- Ranks top cost steps
- Produces optimization hints

## Run
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 src/green_ci_profiler/cli.py examples/run.json
```
