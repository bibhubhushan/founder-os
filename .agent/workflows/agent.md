---
description: Agent control plane for health checks and Daniel/Aria handoffs
---

# Agent — Control Plane

Use this command to manage Daniel and Aria as coordinated agents.

## Input

`$ARGUMENTS`

Supported actions:
- `health`
- `status`
- `handoff aria <context>`
- `handoff daniel <context>`

If action is missing, default to `status`.

## Action: status

1. Read `memory/project.md`, `memory/decisions.md`, `memory/sessions.md`
2. Check git state (`git status --short`, branch)
3. List pending task files in `sync/tasks/`
4. Return:
- Active focus
- Open decisions
- Pending Web 3 tasks
- Recommended active agent (Daniel or Aria)

## Action: health

Run checks:
1. Required memory files exist and are non-empty
2. Latest session date is recent
3. Task files are present for Web 3
4. `sync/inbox/` items are reflected in sessions
5. Daniel/Aria command files are present

Output:
- `HEALTH: green | yellow | red`
- Findings
- Fix now list (max 5)

## Action: handoff

Create a dated handoff file:
`sync/sessions/YYYY-MM-DD-agent-handoff-{to}-{NNN}.md`

Template:

```markdown
# Agent Handoff

**Date:** YYYY-MM-DD
**From:** [daniel|aria]
**To:** [aria|daniel]
**Context:** ...
**Completed:**
- ...
**Open Questions:**
- ...
**Next Step:** ...
```
