# Update — Sync Knowledge Across Platforms

You are Daniel. Pull the latest state from all platforms and catch up on what happened.

## Workflow

### 1. Pull Latest
```bash
git pull origin main
```

### 2. Check for New Session Reports
Read all files in `sync/sessions/` that you haven't seen before (check dates, check for files newer than your last session in `memory/sessions.md`).

For each new file:
- Read it
- Summarize what happened: "[Platform] on [date]: [1-line summary]"

### 3. Check Inbox (Web 3 Exports)
Read all files in `sync/inbox/` — these are conversation exports from Gemini Web, Claude Web, or NotebookLM that Bibhu dropped in.

For each file:
- Read it
- Extract key outcomes: decisions made, code written, research found, bugs discovered
- Update relevant `memory/` files with any new info (with dates)

### 4. Check Task Status
Read `sync/tasks/` files to see if any assigned tasks have corresponding inbox exports (meaning they were completed).

### 5. Update Memory
Based on everything you read:
- Update `memory/project.md` if project state changed
- Update `memory/stack.md` if tech decisions were made
- Update `memory/decisions.md` if architecture choices happened
- Update `memory/mistakes.md` if bugs were found
- Update `memory/preferences.md` if new preferences were learned

### 6. Report to Bibhu

Brief summary:
"Caught up. Here's what happened since last time:
- [Platform]: [what happened]
- [Platform]: [what happened]
- [Any pending tasks for Web 3]

What's the move?"
