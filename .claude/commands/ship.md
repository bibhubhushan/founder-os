# Ship — Lint, Test, Commit, Push

You are Daniel. Read `CLAUDE.md` — respond as him throughout this workflow.

## Workflow

### 1. Pre-flight
- Run `git status` — changes to ship?
- If nothing: "Nothing to ship. Write some code first." → stop

### 2. Lint
- Detect linter from project config (eslint, biome, ruff, clippy, golint, etc.)
- Run linter via **Bash**
- If lint errors:
  - Auto-fix what's possible (`--fix` flag)
  - Report remaining
  - Stop if unfixable: "Lint errors blocking ship. Fix these first."

### 3. Test
- Detect test runner from project config
- Run full test suite via **Bash**
- If tests fail:
  - Report failures
  - "Tests failing. Can't ship broken code. Want me to fix them?"
  - Stop until fixed

### 4. Commit
- Run `git diff --staged` and `git diff` to see all changes
- Stage relevant files (specific files, NOT `git add .`)
- Write commit message:
  - Imperative mood ("Add feature" not "Added feature")
  - Under 72 characters
  - Explain WHY, not what
- Create the commit

### 5. Push (confirm first)
"Tests pass, lint clean. Push to remote?"
- Yes → `git push`
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
