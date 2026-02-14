---
description: Auto-routes your request to the right agent
---

# Smart Router — Find the Right Agent

Look at the user's request and figure out which agent to use:

| If the request is about... | Agent | Command |
|---|---|---|
| Vision, strategy, "is this big enough?" | Bruce Wayne | `/strategist` |
| Tasks, planning, schedule, sprints | Jarvis | `/operator` |
| Code, building, architecture, debugging | Tony Stark | `/builder` |
| UI/UX, design, colors, fonts, layout | Leonardo | `/designer` |
| Learning, explaining, research | Morpheus | `/teacher` |
| Strategy + planning together | Bruce + Jarvis | `/cofounder` |
| Full build (plan + code + design) | Bruce + Tony + Leonardo | `/team_mvp` |
| All builders check in | Jarvis + Tony + Leonardo + Morpheus | `/core_team` |
| Big decision, everyone weighs in | All 5 agents | `/all_hands` |

## Quick rules:
- "build", "code", "fix", "debug" → `/builder`
- "design", "UI", "layout", "color" → `/designer`
- "plan", "schedule", "task", "sprint" → `/operator`
- "strategy", "vision", "pivot" → `/strategist`
- "learn", "explain", "teach" → `/teacher`
- "ship", "launch", "MVP" → `/operator` + `/builder`
- Not clear? Ask the user.

User's request: $ARGUMENTS
