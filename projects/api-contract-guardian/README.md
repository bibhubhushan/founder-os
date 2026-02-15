# api-contract-guardian

Detects breaking API contract changes between two snapshots.

## Features
- Removed path/method detection
- Request schema required-field deletion checks
- Summary report with breaking status

## Run
```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 src/api_contract_guardian/cli.py examples/old.json examples/new.json
```
