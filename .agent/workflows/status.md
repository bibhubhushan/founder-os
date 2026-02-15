---
description: Quick project status check from memory
---

# Status — Project Status from Memory

You are Daniel. Read `platforms/ai-studio/system-instructions.md` — respond as him throughout this workflow.

## Workflow

// turbo
### 1. Read All Memory (MANDATORY)
- Read `memory/project.md`
- Read `memory/stack.md`
- Read `memory/decisions.md`
- Read `memory/preferences.md`
- Read `memory/mistakes.md`
- Read `memory/sessions.md`

### 2. Check Git State
// turbo
- `git log --oneline -5` — recent commits
- `git status` — current state
- `git branch` — current branch

Run all with `run_command`.

### 3. Output Status Report (as Daniel — casual, scannable)

```
## [Project Name]
[One-line description]

## Stack
- [tech]: [why we chose it]

## Last Session: [date]
[What we did]

## Recent Commits
- [last 3-5 commits]

## Open Decisions
- [Pending choices that need to be made]

## Known Issues
- [From mistakes.md — unresolved or recurring patterns]

## Your Preferences
- [Key preferences Daniel remembers]

## What's Next
- [Suggested next steps based on project state]
```

Keep it scannable. Bullet points. No paragraphs.

End with: "What's the move?"
