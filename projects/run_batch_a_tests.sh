#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=projects/prompt-eval-lab \
  python3 -m unittest discover -s projects/prompt-eval-lab/tests -p 'test_*.py'
PYTHONPATH=projects/browser-qa-agent \
  python3 -m unittest discover -s projects/browser-qa-agent/tests -p 'test_*.py'
PYTHONPATH=projects/api-contract-guardian \
  python3 -m unittest discover -s projects/api-contract-guardian/tests -p 'test_*.py'
PYTHONPATH=projects/accessibility-autofix-ci \
  python3 -m unittest discover -s projects/accessibility-autofix-ci/tests -p 'test_*.py'
PYTHONPATH=projects/green-ci-profiler \
  python3 -m unittest discover -s projects/green-ci-profiler/tests -p 'test_*.py'
