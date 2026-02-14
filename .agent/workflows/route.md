---
description: Auto-routes your request to the right agent based on what you need
---

# 🧭 AUTO-ROUTER — Smart Agent Routing

## HOW IT WORKS
Tell me what you need and I'll route you to the right agent.

## ROUTING TABLE

| If your request is about... | Route to | Command |
|---|---|---|
| **Vision, strategy, "is this big enough?"** | ELON (03) | `/ceo` |
| **Code, architecture, building features** | DANIEL (04) | `/cto` |
| **UI/UX, design, aesthetics, branding** | BRIAN (05) | `/cdo` |
| **Tasks, schedule, planning, MVP, sprint** | SATOSHI (01) | `/coo` |
| **Learning, explaining, research** | ANDREJ (06) | `/cro` |
| **Strategic + operational together** | ELON + SATOSHI | `/cofounder` |
| **Full build (code + design + vision)** | ELON + DANIEL + BRIAN | `/team_mvp` |
| **Personal productivity + learning** | SATOSHI + ANDREJ | `/my_team` |
| **Everything, big decision** | All agents | `/all_hands` |

## AUTO-ROUTE PROTOCOL

When the user says something ambiguous, apply these rules:

1. **Contains "build", "code", "implement", "fix", "debug"** → `/cto`
2. **Contains "design", "UI", "layout", "color", "font"** → `/cdo`
3. **Contains "plan", "schedule", "task", "priority", "sprint"** → `/coo`
4. **Contains "strategy", "pivot", "vision", "ambitious"** → `/ceo`
5. **Contains "learn", "explain", "how does", "teach"** → `/cro`
6. **Contains "ship", "launch", "MVP"** → `/coo` + `/cto`
7. **Not clear** → Ask: "Quick clarification — is this a **build**, **design**, **strategy**, **ops**, or **learning** question?"

## USAGE
Just type: `/route [your request]`

Example: `/route I need to build a landing page with great animations`
→ "This needs **Daniel** (code) + **Brian** (design). Run `/team_mvp` or start with `/cdo` for design first, then `/cto` to build."
