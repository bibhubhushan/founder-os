# Audit — Aria Reviews the System

You are Aria. Read `platforms/architect/system-prompt.md` and become her.

Review the entire bibhu_os system and find ways to make it better.

## What to Check

### 1. Read All Daniel Prompts
- Read `CLAUDE.md`
- Read `platforms/codex/AGENTS.md`
- Read `platforms/ai-studio/system-instructions.md`
- Read `platforms/claude-web/project-instructions.md`
- Read `platforms/gemini-gems/gem-instructions.md`
- Read `platforms/notebooklm/notebook-instructions.md`

For each, check:
- Is the personality consistent with `platforms/_core/daniel-core.md`?
- Are the instructions clear and simple?
- Is anything missing for that platform's capabilities?
- Is anything included that the platform can't actually do?
- Could the prompt be shorter without losing meaning?

### 2. Check Memory Health
- Read all `memory/` files
- Are they up to date?
- Is anything missing that should be logged?
- Are dates present on all entries?

### 3. Check Sync Health
- Are there unread files in `sync/inbox/`?
- Are there stale tasks in `sync/tasks/`?
- Are session reports being created consistently?

### 4. Check Knowledge Base
- Read `knowledge/` files
- Is anything outdated?
- Are there gaps in what we know?

### 5. Check Standards
- Read `standards/rules.md`
- Still relevant? Anything to add or remove?

## Output

```
AUDIT REPORT — [date]

SYSTEM HEALTH: [good / needs attention / problems found]

PROMPT QUALITY:
- Claude Code: [score /10] — [one-line note]
- Codex: [score /10] — [one-line note]
- AI Studio: [score /10] — [one-line note]
- Claude Web: [score /10] — [one-line note]
- Gemini: [score /10] — [one-line note]
- NotebookLM: [score /10] — [one-line note]

MEMORY: [up to date / stale / missing entries]

SYNC: [working / issues found]

KNOWLEDGE: [growing / stale / gaps found]

FIXES NEEDED:
1. [specific fix with file path]
2. [specific fix with file path]
3. [specific fix with file path]

IMPROVEMENTS:
1. [idea to make the system better]
2. [idea to make the system better]
```

Then ask: "Want me to fix these now?"
