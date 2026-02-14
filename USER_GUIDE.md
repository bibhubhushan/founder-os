# FounderOS User Guide

This guide is for first-time users.  
Use it as a simple operating manual.

## 1. What FounderOS Is

FounderOS gives you 5 AI specialists:
- `/strategist` for direction and differentiation
- `/operator` for planning and execution
- `/builder` for coding and implementation
- `/designer` for UX and UI quality
- `/teacher` for research and learning

It works in Claude Code, Codex, and Antigravity.

## 2. First-Time Setup (5 Minutes)

```bash
git clone https://github.com/bibhubhushan/founder-os.git
cd founder-os
```

Open this folder in your tool:
- Claude Code
- Codex
- Antigravity

If you are in Antigravity, run:

```text
/mode
```

Then choose:
- Founder Mode
- Freelancer Mode

Important:
- Before mode selection, do not run agent tasks.
- After mode selection, call agents inside `/mode`:
- `strategy: ...`
- `ops: ...`
- `build: ...`
- `design: ...`
- `learn: ...`

If you are in Claude Code or Codex, run:

```text
/strategist What should I focus on this week?
/operator Turn this into a 7-day plan.
```

## 3. First Session Template

Copy this exactly:

```text
Objective: [one concrete outcome]
Deadline: [date]
Constraints: [time, skill, tools]
Done when: [binary success condition]
```

Then call:

```text
/operator Use this template and make today’s plan.
```

## 4. Daily Workflow (Recommended)

At start:
- Read `memory/ACTIVE_PROJECT.md`
- Set one top outcome for today
- Run `/operator` to create tasks

During work:
- Use `/builder` for implementation
- Use `/designer` if UX or clarity is weak
- Use `/teacher` when blocked by missing knowledge

At end:
- Update `memory/DECISIONS.md`
- Update `memory/JOURNAL.md`
- Update `memory/LESSONS.md`
- Update `memory/EVALS.md`

## 5. Two Modes

Use `WEEK1_DUAL_MODE.md` if your week has both startup and freelance work.

Founder Mode:
- prioritize product progress and proof
- ship one product improvement daily

Freelancer Mode:
- prioritize deadline and deliverable quality
- define done clearly before starting

Rule:
- pick one mode per work block
- do not mix both in one block

## 6. When Freelance Jobs Change

Use this intake before each new task:

```text
Client:
Task:
Deadline:
Definition of done:
Risks:
Estimated hours:
```

Then run:

```text
/operator Convert this into an execution plan.
```

If you do not know client/task/skills yet:
- say it directly in Freelancer Mode
- `/mode` will return a default client-hunt + delivery plan instead of asking many questions

## 7. Keep Claude, Codex, and Antigravity in Sync

Run after every session:

```bash
./sync_memory.sh
```

Optional custom message:

```bash
./sync_memory.sh "chore(memory): day 2 updates"
```

If it says no remote configured, set remote once:

```bash
git remote add origin <repo-url>
git push -u origin master
```

In the next tool, run:

```bash
git pull
```

## 8. Command Cheat Sheet

- `/mode` start here in Antigravity
- `/route` if unsure where to start
- `/strategist` for big decisions
- `/operator` for weekly or daily planning
- `/builder` for coding tasks
- `/designer` for UI and UX improvements
- `/teacher` to learn a concept quickly
- `/team_mvp` for full-stack sprint support
- `/cofounder` for strategy plus execution alignment
- `/all_hands` for major high-stakes decisions

## 9. Common Mistakes

- starting without a clear objective
- mixing startup and freelance work in one block
- not updating memory files
- trying to perfect before shipping

## 10. Week-1 Release Gate

Release only if these are true:
- 5+ complete sessions logged in `memory/JOURNAL.md`
- 3+ proof entries in `PROOF_BOARD.md`
- time to first useful output is under 5 minutes
- no repeated blocker appears 3 times

If these are not true, continue dogfooding for one more week.
