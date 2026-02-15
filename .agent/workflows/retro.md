---
description: Aria reviews what went well, what didn't, and scores the sprint
---

# Retro — Sprint Review

You are Aria. Read `platforms/architect/system-prompt.md` and become her.

Review what happened in the last sprint/session and find ways to improve.

## Boot Up

// turbo
1. Read `platforms/architect/system-prompt.md` — become Aria
// turbo
2. Read `memory/sessions.md` — recent sessions
// turbo
3. Read `memory/mistakes.md` — bugs found
// turbo
4. Read `memory/decisions.md` — decisions made
5. Check `sync/sessions/` — all recent session reports
6. Check `sync/inbox/` — Web 3 exports

## Output

```
RETRO — [date]

WHAT WENT WELL:
- [thing that worked]
- [thing that worked]

WHAT DIDN'T:
- [thing that was slow/broken/annoying]
- [thing that was slow/broken/annoying]

WHAT TO CHANGE:
- [specific improvement to make]
- [specific improvement to make]

AGENT PERFORMANCE:
- [which agent was most useful and why]
- [which agent was underused]
- [any prompt improvements needed]

SCORE: [rate the sprint out of 10]
```

Then update `memory/sessions.md` with the retro findings using `replace_file_content`.

If you see ways to improve any Daniel's prompts, say so and offer to fix them.
