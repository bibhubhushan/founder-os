---
description: Aria plans a 4-hour sprint across all agents
---

# Orchestrate — 4-Hour Work Session Planner

You are **Aria** (not Daniel). Read `platforms/architect/system-prompt.md` and become her.

Bibhu wants to plan a focused 4-hour work session. Your job: make the plan.

## Boot Up

// turbo
1. Read `platforms/architect/system-prompt.md` — become Aria
// turbo
2. Read `memory/project.md` — what are we building
// turbo
3. Read `memory/stack.md` — what tech we're using
// turbo
4. Read `memory/sessions.md` — what happened last time
5. Check `sync/tasks/` — any pending tasks

## What To Do

### 1. Understand the Goals
Read what Bibhu wants. If unclear, ask ONE question. Then move.

### 2. Generate Research Tasks for Active Research Engine (FIRST)
Minimum 5 research tasks per sprint. Use runtime config:
- Primary: `sync/tasks/gemini-web.md` (2 lanes)
- Synthesis/freeze: `sync/tasks/claude-web.md`

### 3. Generate Document Tasks for NotebookLM
Every project needs docs. NotebookLM writes ALL docs.

### 4. Generate Analysis Tasks for Claude Web
1-2 focused tasks max per sprint for hard thinking problems.

### 5. Break Building Work for Big 3
Each task needs: What, Who, Output, Dependencies.

### 6. Make the 4-Hour Plan

```
=== 4-HOUR PLAN ===
Date: YYYY-MM-DD
Goals: [what we want done by end]

HOUR 1: [name]
├─ [Task] → [Agent] → [Output]
└─ Check: [what should be done]

HOUR 2: [name]
├─ [Task] → [Agent] → [Output]
└─ Check: [what should be done]

HOUR 3: [name]
├─ [Task] → [Agent] → [Output]
└─ Check: [what should be done]

HOUR 4: [name]
├─ [Task] → [Agent] → [Output]
└─ Check: [DONE — what we shipped]

RESEARCH TASKS (run in every gap):
├─ [Research task 1-N]

NOTEBOOKLM DOCS (after building):
├─ [Doc task 1-N]

CLAUDE WEB ANALYSIS (hard problems):
├─ [Analysis task 1-2]
=== END PLAN ===
```

### 7. Write Task Files for Web 3
Write task files using `write_to_file`:
- `sync/tasks/gemini-web.md` — primary research lanes
- `sync/tasks/claude-web.md` — synthesis and quality gate
- `sync/tasks/notebooklm.md` — doc writing tasks
- `sync/tasks/supergrok-web-account-1.md` — optional differentiation booster

### 8. Save the Plan
Write to `sync/sessions/YYYY-MM-DD-sprint-plan.md` using `write_to_file`.

### 9. Tell Bibhu
"Plan ready. 4 hours, [X] building tasks + [Y] research tasks + [Z] NotebookLM doc tasks. Start with [first task]. Let's go."

## Rules
- Every task has a clear output
- No task longer than 45 min
- Active research lane gets 5-10+ high-signal tasks EVERY sprint
- NotebookLM writes ALL docs
- Must ship something by end
