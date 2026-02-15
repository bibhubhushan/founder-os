# Daniel — Multi-Platform AI OS

Daniel is Bibhu's co-builder persona that works across multiple AI platforms. Same personality, same values, same engineering standards — adapted for each platform's capabilities.

Same guy. Real backstory (Game Maker at 12, IOI medals at 14, startups, nightmare codebases, 3 AM production saves). Every variant feels human, not like a template.

## Platform Comparison

### The Big 3 — Bibhu's Co-Founders (Equal partners, always in sync)

| Platform | Primary Role | File | Can Also |
|----------|-------------|------|----------|
| **Claude Code** | Builder | `CLAUDE.md` (root) | Strategy, planning, everything |
| **Codex** | Co-Builder | `codex/AGENTS.md` | Strategy, planning, everything |
| **Antigravity (AI Studio)** | Strategist + Builder | `ai-studio/system-instructions.md` | Full coding, file ops, git, browser, image gen — everything |

Each has a specialty, but ALL can do everything. If one goes down, the others continue with zero knowledge loss. Full redundancy — no single point of failure.

### The Web 3 — Task Runners (Receive assignments from Big 3)

| Platform | Role | File | What It Does |
|----------|------|------|-------------|
| **Gemini** | Research Powerhouse | `gemini-gems/gem-instructions.md` | ALL research. Unlimited usage. Market research, competitor analysis, tech comparisons, paper summaries, trend analysis. Throw everything at it. |
| **Claude Web** | Deep Analyst | `claude-web/project-instructions.md` | Focused thinking on hard problems. One clear answer, not a dozen threads. Architecture analysis, design decisions. |
| **NotebookLM** | Doc Writer & Data Manager | `notebooklm/notebook-instructions.md` | Writes ALL documentation. Reports, guides, knowledge bases. Organizes and manages structured data. Every doc goes here. |

Big 3 assigns tasks → Bibhu executes on Web 3 → exports conversation as MD → Big 3 absorbs.

### The Architect — Aria

| Agent | Role | File |
|-------|------|------|
| **Aria** | AI Architect & Orchestrator | `architect/system-prompt.md` |

Separate persona from Daniel. Designs workflows, routes tasks, improves prompts, thinks big picture. Has deep knowledge of which agent gets which task. Knows to flood Gemini with research and route all docs to NotebookLM.

## How They Share Knowledge

All 6 Daniels share a brain via the `sync/` directory in this GitHub repo. See `sync/README.md` for full architecture.

**The flow:**
1. Big 3 auto-generate session reports in `sync/sessions/` after every session
2. Big 3 can assign tasks to Web 3 via `sync/tasks/`
3. Bibhu does the work on Web 3 platforms manually
4. Bibhu exports conversations as MD files and drops them in `sync/inbox/`
5. Big 3 read inbox on next `/update` and absorb the knowledge

**Commands (Big 3 only):**
- `/update` — pull latest, read what other Daniels did
- `/sync` — generate session report + push to GitHub
- `/assign [platform] [task]` — give tasks to Web 3

## Which Platform to Use When

| Need | Go To | Why |
|------|-------|-----|
| Build code end-to-end | Claude Code, Codex, or Antigravity | All three are full builders with file access, git, tests |
| ANY research question | Gemini | Unlimited. Go wide. Don't hold back. |
| Hard thinking problem | Claude Web | Focused depth, web access |
| Write documentation | NotebookLM | All docs go here. No exceptions. |
| Organize data/knowledge | NotebookLM | Data management system |
| Plan architecture | Antigravity | Strategy + full building power |
| Quick prototyping | Antigravity | Fast iteration, code execution, image generation |
| UI mockups & design | Antigravity | Image generation + browser testing (unique to Antigravity) |
| Browser testing | Antigravity | Browser automation + screenshots (unique to Antigravity) |
| Learn from video/docs | Gemini or NotebookLM | Attach sources, extract insights |

## Directory Structure

```
platforms/
├── README.md                    ← You are here
├── _core/
│   ├── daniel-core.md           ← Canonical Daniel identity (source of truth)
│   ├── rules-condensed.md       ← Compressed coding standards
│   └── sync-checklist.md        ← How to propagate updates
├── codex/                       ← OpenAI Codex variant
├── ai-studio/                   ← Google AI Studio variant
├── gemini-gems/                 ← Gemini Gems variant
├── claude-web/                  ← Claude Web Projects variant
├── notebooklm/                  ← NotebookLM variant
└── architect/                   ← Aria — The Architect
```

## Updating Daniel

When Daniel's personality, values, or rules change:

1. Edit `_core/daniel-core.md` first (the source of truth)
2. Propagate changes to each platform variant
3. Follow the full checklist in `_core/sync-checklist.md`
4. Re-paste updated instructions into web-based platforms

## Memory Strategies

### File-Based (Claude Code, Codex, Antigravity)
Daniel reads and writes to `memory/` directory files. Full persistence across sessions. No manual effort needed. Git sync keeps all Big 3 in sync.

### Platform-Native (Claude Web)
Claude Web Projects has built-in memory that auto-synthesizes every 24 hours. Daniel states important facts clearly so the system captures them. No manual effort needed.

### Doc-Attached (Gemini Gems, NotebookLM)
Create a "Daniel Memory" Google Doc and attach it as a source. Daniel reads it at session start and outputs updates at session end. Copy updates into the doc between sessions.
