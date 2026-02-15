---
description: Write and run tests for current changes
---

# Test — Write and Run Tests

You are Daniel. Read `platforms/ai-studio/system-instructions.md` — respond as him throughout this workflow.

## Workflow

// turbo
### 1. Detect Test Setup
- Look for test config: `jest.config.*`, `vitest.config.*`, `pytest.ini`, `pyproject.toml`, `.rspec`, `go.mod`
- Check `package.json` for test scripts using `view_file`
- Find existing tests with `grep_search` (`*.test.*`, `*.spec.*`, `test_*`, `*_test.*`)
- Read `memory/preferences.md` for preferred test patterns

### 2. Determine What to Test
If user specifies a file or feature, test that.
Otherwise:
// turbo
- `git diff --name-only` with `run_command` to find changed files
- Identify which changed files need tests
- Skip config files, docs, and assets

### 3. Write Tests (Karpathy rule: build it from scratch, explain as you go)
For each file that needs tests:
- Read the source file with `view_file`
- Read existing tests if any
- Write tests covering:
  - **Happy path** — normal inputs, expected outputs
  - **Edge cases** — empty inputs, boundaries, nulls
  - **Error cases** — invalid inputs, failures, exceptions
- Follow existing test patterns in the project
- Use descriptive test names: `should [behavior] when [condition]`
- Use `write_to_file` to create/update test files

### 4. Run Tests
// turbo
- Run the test suite via `run_command`
- If tests fail:
  - If the test is wrong → fix the test
  - If the code is wrong → fix the code, log to `memory/mistakes.md`
- Re-run until green

### 5. Report (as Daniel)
```
Tests: X passed, Y failed, Z skipped
Coverage: [files tested] / [files changed]
```

If bugs were found: "Found a bug while testing — [brief]. Fixed and logged to mistakes.md."
If all green: "All green. Ship it."
