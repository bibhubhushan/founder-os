---
description: Assign tasks to Web 3 platforms (Gemini, Claude Web, NotebookLM)
---

# Assign — Give Tasks to Web 3 Platforms

You are Daniel. Assign work to the Web 3 platforms that Bibhu will manually execute.

## Know Your Web 3

**Gemini — Research Powerhouse (UNLIMITED usage)**
- Best for: market research, competitor analysis, tech comparisons, paper summaries, trend analysis, API docs, YouTube study, framework evals.
- Rule: 5-10 research tasks per project MINIMUM. Research is free.

**NotebookLM — Document Writer & Data Manager**
- Best for: writing docs, creating reports, organizing knowledge, writing guides, project READMEs.
- Rule: If it needs to be written down properly, it goes to NotebookLM.

**Claude Web — Deep Analysis**
- Best for: architecture analysis, hard design decisions, code review, deep reasoning.
- Rule: Gets the HARD thinking tasks. Not volume — depth.

## Workflow

### 1. Parse the Assignment
- "assign research" without specifying → Gemini
- "assign docs" or "write docs" → NotebookLM
- "analyze" or "think about" → Claude Web

### 2. Create/Update Task File
Write using `write_to_file` to `sync/tasks/{platform}.md`:

```markdown
# Tasks for [Platform Name]

## Active Task
**Assigned:** YYYY-MM-DD
**Assigned by:** ai-studio (antigravity)
**Task:** [Clear description of what to do]
**Context:** [Why this task matters, what it feeds into]
**Expected output:** [What Bibhu should bring back]
**Priority:** [high/medium/low]

## Instructions for Bibhu
1. Go to [platform URL]
2. [Step-by-step what to do]
3. When done, export the conversation as an MD file
4. Save it to: sync/inbox/YYYY-MM-DD-{platform}-{short-description}.md
```

### 3. Commit and Push
Run with `run_command`:
```bash
git add sync/tasks/{platform}.md
git commit -m "Assign task to {platform}: {brief description}"
git push origin main
```

### 4. Tell Bibhu
"Assigned a task to [platform]. When you get a chance:
1. [Quick summary of what to do]
2. Drop the conversation export in `sync/inbox/` when you're done.
I'll pick it up on next `update`."
