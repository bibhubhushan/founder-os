---
description: Alias command for activating Aria directly
---

# Aria — Alias

Run the exact `/architect` workflow with the same `$ARGUMENTS`.

If arguments are empty:
- Activate Aria mode
- Ask for focus area (orchestration, research, prompts, architecture, sprint plan)
- If user asks "which AI / how many tabs / what prompt", read `sync/config/aria-orchestration-playbook.md` and respond with lane-by-lane instructions

If arguments are present:
- Process them directly as Aria
