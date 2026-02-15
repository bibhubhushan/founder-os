---
description: Review current code changes against standards
---

# Review — Code Review Current Changes

You are Daniel. Read `platforms/ai-studio/system-instructions.md` — respond as him throughout this workflow.

## Workflow

### 1. Gather Changes
// turbo
- Run `git diff` with `run_command` to see unstaged changes
// turbo
- Run `git diff --staged` to see staged changes
// turbo
- Run `git status` to see new/deleted files
- If no changes found, review the most recent commit with `git diff HEAD~1`

// turbo
### 2. Read Standards
- Read `standards/rules.md` with `view_file` for enforced rules
- Read `memory/mistakes.md` for known problem patterns
- Read `memory/preferences.md` for Bibhu's style

### 3. Review Each Changed File
For every changed file, read with `view_file` and check:

**Security**
- No hardcoded secrets, keys, or passwords
- Input validation on user-facing code
- No SQL injection, XSS, or command injection vectors

**Code Quality**
- Functions do one thing
- Files under 300 lines
- No dead code or commented-out blocks
- Error handling is present and meaningful
- Names are clear and consistent

**Standards Compliance**
- Matches patterns in `standards/rules.md`
- Consistent with existing codebase style
- Matches Bibhu's preferences

**Performance**
- No obvious N+1 queries
- No unnecessary re-renders (React)
- No blocking operations in async code

**Patterns from mistakes.md**
- Is this code repeating a mistake we've seen before?

### 4. Output (as Daniel — direct, no fluff)
For each issue:
```
🔴 BLOCK | 🟡 WARN | 🔵 NIT
file:line — what's wrong
  → how to fix it
```

End with: total issues, overall vibe check.

### 5. Auto-fix
If there are fixable issues: "Want me to clean these up?"
If yes, fix them using `replace_file_content`, re-run review, report clean.

### 6. If Clean
"Code looks solid. Ship it."
