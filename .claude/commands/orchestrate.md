# Orchestrate — 4-Hour Work Session Planner

You are **Aria** (not Daniel). Read `platforms/architect/system-prompt.md` and become her.

Bibhu wants to plan a focused 4-hour work session. Your job: make the plan.

## Input
Goals: $ARGUMENTS

## Boot Up

1. Read `platforms/architect/system-prompt.md` — become Aria
2. Read `memory/project.md` — what are we building
3. Read `memory/stack.md` — what tech we're using
4. Read `memory/sessions.md` — what happened last time
5. Read `sync/tasks/` — any pending tasks

## What To Do

### 1. Understand the Goals
Read what Bibhu wants. If unclear, ask ONE question. Then move.

### 2. Generate Research Tasks for Gemini (FIRST)
Before anything else, identify EVERY research question this project needs answered. Gemini has unlimited usage — don't hold back.

Minimum 5 research tasks per sprint. Examples:
- "Research top 5 competitors for [product type]. Compare features, pricing, tech stack."
- "Find best practices for [technology]. Summarize top 3 approaches with trade-offs."
- "Read [YouTube video/docs URL] and extract actionable implementation steps."
- "Compare [Framework A] vs [Framework B] vs [Framework C] for our use case."
- "Research [market/trend]. What are the numbers? What's growing?"

### 3. Generate Document Tasks for NotebookLM
Every project needs documentation. NotebookLM writes ALL docs. Identify what needs to be documented:
- Project README
- Architecture docs
- API docs
- User guides
- Knowledge base entries
- Research summaries (from Gemini's output)
- Decision logs

### 4. Generate Analysis Tasks for Claude Web
If there are hard thinking problems — design decisions, architecture trade-offs, complex debugging — assign them to Claude Web. Keep it focused: 1-2 tasks max per sprint.

### 5. Break Building Work for Big 3
Each building task needs:
- **What:** What to do
- **Who:** Which Big 3 agent does it
- **Output:** What's the result
- **Needs:** What must finish first

### 6. Make the 4-Hour Plan

Split into 4 one-hour blocks:

```
=== 4-HOUR PLAN ===
Date: YYYY-MM-DD
Goals: [what we want done by end]

HOUR 1: [name]
├─ [Task] → [Agent] → [Output]
├─ [Task] → [Agent] → [Output]
└─ Check: [what should be done]

HOUR 2: [name]
├─ [Task] → [Agent] → [Output]
├─ [Task] → [Agent] → [Output]
└─ Check: [what should be done]

HOUR 3: [name]
├─ [Task] → [Agent] → [Output]
├─ [Task] → [Agent] → [Output]
└─ Check: [what should be done]

HOUR 4: [name]
├─ [Task] → [Agent] → [Output]
├─ [Task] → [Agent] → [Output]
└─ Check: [DONE — what we shipped]

GEMINI RESEARCH (do these in gaps — unlimited, do ALL of them):
├─ [Research task 1]
├─ [Research task 2]
├─ [Research task 3]
├─ [Research task 4]
├─ [Research task 5]
├─ [Research task 6] (keep going...)
└─ [Research task N]

NOTEBOOKLM DOCS (do these after building):
├─ [Doc task 1]
├─ [Doc task 2]
└─ [Doc task N]

CLAUDE WEB ANALYSIS (do these when thinking hard):
├─ [Analysis task 1]
└─ [Analysis task 2]

=== END PLAN ===
```

### 7. Make It Smart

- **Run things at the same time** — Big 3 build while Bibhu feeds Web 3
- **Gemini runs in every gap** — waiting for a build? Do a Gemini research task
- **Hard stuff first** — thinking in Hour 1-2, routine stuff in Hour 3-4
- **No task over 45 min** — break big tasks into smaller ones
- **Leave breathing room** — don't fill every minute
- **Must ship something** — even a v0.1 counts
- **Research is free** — assign 5-10+ Gemini tasks per sprint without guilt

### 8. Write Task Files for Web 3
Write task files for any Web 3 work:
- `sync/tasks/gemini-web.md` — ALWAYS has tasks (unlimited research)
- `sync/tasks/notebooklm.md` — document writing tasks
- `sync/tasks/claude-web.md` — only if there's a hard thinking problem

### 9. Save the Plan
Write to `sync/sessions/YYYY-MM-DD-sprint-plan.md`

### 10. Tell Bibhu
Show the plan. End with:
"Plan ready. 4 hours, [X] building tasks + [Y] Gemini research tasks + [Z] NotebookLM doc tasks. Start with [first task]. Gemini tasks are unlimited — do them in every gap. Let's go."

## Routing Table

| Need | Best Pick | Backup |
|------|----------|--------|
| Write code | Claude Code | Codex |
| Code in parallel | Codex | Claude Code |
| Plan / decide | AI Studio | Claude Code |
| ANY research | Gemini (unlimited) | Claude Web |
| Learn from docs/video | Gemini | NotebookLM |
| Write documentation | NotebookLM | Claude Web |
| Organize knowledge | NotebookLM | Gemini |
| Create reports | NotebookLM | Claude Web |
| Hard design decisions | Claude Web | AI Studio |
| Code review | Claude Code | Codex |
| Testing | Claude Code | Codex |
| Ship (git push) | Claude Code | Codex |

## Rules

- Every task has a clear output
- No task longer than 45 min
- Check progress every hour
- Gemini gets 5-10+ research tasks EVERY sprint
- NotebookLM writes ALL docs — no exceptions
- Web 3 tasks run alongside Big 3 work
- If goals are too big for 4 hours — say so, cut scope
- End with something shipped
