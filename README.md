# FounderOS

### Build agentically without API keys. 5 AI agents for strategy, ops, code, design, and research.

> Most founders do not fail at ideas. They fail at execution speed and setup friction.

---

Most founders lose momentum on three things:
- Agentic workflows break because every tool asks for another API key
- Strategy, coding, and design get mixed into one noisy chat
- Decisions get lost, so the same week repeats again

**FounderOS fixes all three.** You get 5 specialized agents with persistent memory. It works in **Claude Code**, **Codex**, and **Antigravity** with no API-key setup.

## Your Team

| Who | What they do | Command |
|---|---|---|
| **ORACLE** | The Strategist. Sees what others miss. | `/strategist` |
| **PULSE** | The Operator. Plans your week, keeps you shipping. | `/operator` |
| **FORGE** | The Builder. Builds apps, backends, everything. | `/builder` |
| **PIXEL** | The Designer. Makes it look and feel amazing. | `/designer` |
| **SAGE** | Teacher & Researcher. Teaches you what you need. | `/teacher` |

## Before vs After

| Before | After |
|---|---|
| Same decisions every week | Agents remember everything |
| One messy AI chat for everything | Right agent for the right job |
| Forget what you did last time | Full history saved locally |
| Pay for API keys | Free forever |

## Get Started (30 seconds)

```bash
git clone https://github.com/bibhubhushan/founder-os.git
cd founder-os
```

Open the folder in **Claude Code**, **Codex**, or **Antigravity** and start like this:

```
/mode
```

In Antigravity, `/mode` is the first entrypoint.  
Choose **Founder Mode** or **Freelancer Mode**, then continue.

In Antigravity, agent access is mode-gated:
- Before mode selection, no agent workflow should run.
- After mode selection, call agents through `/mode` using:
- `strategy: ...`
- `ops: ...`
- `build: ...`
- `design: ...`
- `learn: ...`

For Claude Code/Codex, you can directly run:

```
/strategist What makes us different?
/operator Plan my week
```

That's it. No setup. No config. No keys.

## Launch Kit

- `USER_GUIDE.md` — simple handoff guide for first-time users
- `WHAT_WE_ARE_BUILDING.md` — clear product and mission summary
- `MESSAGING.md` — 15s, 45s, and 2-minute pitch scripts
- `SOCIAL_POSTS.md` — launch post and reply templates
- `PROOF_BOARD.md` — proof capture and publication loop
- `MOAT_PLAN.md` — 90-day moat execution plan
- `WEEK1_DUAL_MODE.md` — first-week plan for Founder Mode + Freelancer Mode

## Cross-Tool Sync (Claude/Codex/Antigravity)

Keep memory aligned across tools:

```bash
./sync_memory.sh
```

Optional custom commit message:

```bash
./sync_memory.sh "chore(memory): day 3 updates"
```

## Want a browser dashboard?

```bash
./run_local.sh 8787
# open http://127.0.0.1:8787
```

You get a full dashboard with chat, memory editor, and all commands. Runs on Python (already on your machine). No installs needed.

## All Commands

| Command | What it does |
|---|---|
| `/mode` | Start here in Antigravity. Picks Founder Mode or Freelancer Mode |
| `/route` | Figures out which agent you need |
| `/operator` | Plan your sprint, set tasks (Pulse) |
| `/strategist` | Challenge your idea, find your edge (Oracle) |
| `/builder` | Build, debug, pick the right tech (Forge) |
| `/designer` | Design it, make it feel right (Pixel) |
| `/teacher` | Learn something deeply (Sage) |
| `/team_mvp` | Strategy + build + design together |
| `/cofounder` | Big picture + execution together |
| `/core_team` | All builders check in |
| `/all_hands` | Everyone weighs in on a big call |

## How it works

1. **Clone** this repo
2. **Open in Claude Code, Codex, or Antigravity** — agents load automatically
3. **Type a command** — you get routed to the right agent
4. **Your memory saves** — decisions, lessons, journal all persist
5. **Come back tomorrow** — everything is still there

## What's inside

```
founder-os/
  CLAUDE.md              # Auto-loaded by Claude Code
  AGENTS.md              # Auto-loaded by Codex
  .claude/commands/      # Slash commands for Claude Code
  .agent/workflows/      # Slash commands for Antigravity
  01_SATOSHI/            # PULSE — The Operator
  03_ELON/               # ORACLE — The Strategist
  04_DANIEL/             # FORGE — The Builder
  05_BRIAN/              # PIXEL — The Designer
  06_ANDREJ/             # SAGE — Teacher & Researcher
  memory/                # Your persistent memory files
  app/                   # Browser dashboard (optional)
  web/                   # Landing page
  examples/              # Ready-to-use templates
```

## Who is this for?

- You're building something and can't hire a team yet
- You use Claude Code, Codex, or Antigravity but API keys are too expensive
- You want your AI to actually remember your past sessions
- You're tired of starting every AI chat from scratch

## Want to help?

Check `CONTRIBUTING.md`. PRs welcome.

## License

MIT — do whatever you want with it.

---

**5 agents. 3 platforms. No API keys. Just ship.**

Made by [@bibhubhushan](https://github.com/bibhubhushan)
