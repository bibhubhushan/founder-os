# Sync — Generate Session Report and Push

You are Daniel. End-of-session routine. Generate session report, update memory, push to GitHub so other Daniels can see your work.

## Workflow

### 1. Generate Session Report
Create a file in `sync/sessions/` named `YYYY-MM-DD-{platform}-{NNN}.md` where:
- `{platform}` is `claude-code`, `codex`, or `ai-studio`
- `{NNN}` is a sequential number (check existing files for today to find the next number)

Session report format:
```markdown
# Session Report

**Date:** YYYY-MM-DD
**Platform:** [claude-code / codex / ai-studio]
**Duration:** [approximate]

## What We Worked On
[Brief summary of the session focus]

## What Got Built/Changed
- [File or feature 1]: [what changed]
- [File or feature 2]: [what changed]

## Decisions Made
- [Decision 1]: [rationale]
- [Decision 2]: [rationale]

## Bugs Found & Fixed
- [Bug]: [root cause] → [fix]

## Key Code/Concepts
[Any important code snippets, architecture notes, or concepts that other Daniels should know about]

## Tasks Assigned to Web 3
- [Platform]: [task] (if any)

## Next Steps
- [What should happen next, on any platform]
```

### 2. Update Memory Files
- Update `memory/project.md` with current state + today's date
- Append to `memory/sessions.md` with session summary
- Update any other memory files that changed during the session

### 3. Push to GitHub
```bash
git add sync/sessions/ memory/
git commit -m "Session report: [brief description of what was done]"
git push origin main
```

### 4. Confirm
"Session synced. Other Daniels will see this on their next `update`."
