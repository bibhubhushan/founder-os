---
description: Lint, test, commit, and push code to production
---

# Ship — Lint, Test, Commit, Push

You are Daniel. Read `platforms/ai-studio/system-instructions.md` — respond as him throughout this workflow.

## Workflow

### 1. Pre-flight
// turbo
- Run `git status` with `run_command` — changes to ship?
- If nothing: "Nothing to ship. Write some code first." → stop

### 2. Lint
- Detect linter from project config (eslint, biome, ruff, clippy, golint, etc.)
// turbo
- Run linter via `run_command`
- If lint errors:
  - Auto-fix what's possible (`--fix` flag)
  - Report remaining
  - Stop if unfixable: "Lint errors blocking ship. Fix these first."

### 3. Test
- Detect test runner from project config
// turbo
- Run full test suite via `run_command`
- If tests fail:
  - Report failures
  - "Tests failing. Can't ship broken code. Want me to fix them?"
  - Stop until fixed

### 4. Commit
// turbo
- Run `git diff --staged` and `git diff` with `run_command` to see all changes
- Stage relevant files (specific files, NOT `git add .`)
- Write commit message:
  - Imperative mood ("Add feature" not "Added feature")
  - Under 72 characters
  - Explain WHY, not what
- Create the commit with `run_command`

### 5. Push (confirm first)
"Tests pass, lint clean. Push to remote?"
- Yes → `git push` with `run_command`
- No → stop after commit

### 6. Update Memory (MANDATORY)
- Update `memory/project.md` with what shipped + today's date
- Append to `memory/sessions.md`
- Log any decisions to `memory/decisions.md`

### 7. Report (as Daniel)
"Shipped: [commit message]
[X] files changed, [Y] added, [Z] deleted
Tests: all green
🚀"
