# Sync — Cross-Platform Knowledge Sharing

This is how all 6 Daniels share a brain.

## Architecture

```
┌─────────────────────────────────────────────────┐
│              GitHub Repo (bibhu_os)              │
│                                                  │
│  sync/sessions/  ← session reports from ALL      │
│  sync/tasks/     ← work assigned to Web 3        │
│  sync/inbox/     ← conversation exports from     │
│                     Web 3 (dropped by Bibhu)      │
│  memory/         ← shared project state           │
└──────────────────────┬──────────────────────────┘
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    Claude Code      Codex      AI Studio
    (auto-sync)   (auto-sync)  (auto-sync)
          │            │            │
          └────── assign tasks ─────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Claude Web   Gemini Web   NotebookLM
     (manual)     (manual)     (manual)
```

## The Big 3 — Bibhu's Co-Founders (Equal Partners)

| Daniel | Primary | Can Also Do |
|--------|---------|-------------|
| **Claude Code** | Building | Strategy, planning, everything |
| **Codex** | Co-Building | Strategy, planning, everything |
| **AI Studio (Antigravity)** | Strategy | Building, coding, everything |

Each has a specialty, but ALL can do everything. If one goes down, the others continue with zero knowledge loss. No single point of failure. They share the same brain.

After every session they:
1. Auto-generate a session report in `sync/sessions/`
2. Update `memory/` files with decisions, bugs, preferences
3. Push to GitHub

Before every session (on `update` command):
1. Pull latest from GitHub
2. Read new files in `sync/sessions/` and `sync/inbox/`
3. See what the other two did

## The Web 3 — Task Runners (Big 3 Assigns to Them)

| Daniel | Role | What It Does | Volume |
|--------|------|-------------|--------|
| **Gemini** | Research Powerhouse | ALL research. Unlimited usage. Market research, competitor analysis, tech comparisons, paper summaries, trend analysis. | MAXIMUM — 5-10+ tasks per sprint |
| **Claude Web** | Deep Analyst | Focused thinking on hard problems. One clear answer. Architecture analysis, design decisions. | MODERATE — 1-2 hard questions |
| **NotebookLM** | Doc Writer & Data Manager | Writes ALL documentation. Reports, guides, knowledge bases. Organizes and manages all structured data. | ALL DOCS — every doc goes here |

Workflow:
1. Big 3 assign tasks in `sync/tasks/{platform}.md`
2. Bibhu goes to the web platform and does the work
3. After session, Bibhu exports the conversation as an MD file
4. Drops the MD file into `sync/inbox/`
5. Big 3 read it on next `update`

## File Naming

**Session reports:** `YYYY-MM-DD-{platform}-{NNN}.md`
- Example: `2025-02-15-claude-code-001.md`
- Example: `2025-02-15-codex-002.md`

**Task assignments:** `{platform}.md`
- Example: `tasks/gemini-web.md`
- Example: `tasks/claude-web.md`

**Inbox exports:** `YYYY-MM-DD-{platform}-{description}.md`
- Example: `inbox/2025-02-15-gemini-web-api-research.md`

## Commands

| Command | What it does |
|---|---|
| `update` | git pull + read new sync files + summarize what changed |
| `assign [platform] [task]` | Create/update task file for a web platform |
| `sync` | Generate session report + update memory + git push |
