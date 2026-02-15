# Decisions

Architecture and design decisions with rationale. Never delete — this is the decision log.

<!-- Format:
## YYYY-MM-DD — [Decision Title]
**Context:** What problem we were solving
**Decision:** What we chose
**Alternatives:** What else we considered
**Rationale:** Why this choice
-->

## 2026-02-15 — Codex Agent Runtime for Daniel + Aria
**Context:** Daniel and Aria existed as command personas, but lacked a shared runtime contract, explicit handoff protocol, and direct control-plane operations in Codex.
**Decision:** Added `.codex/agents/runtime.md` plus role profiles (`.codex/agents/daniel.md`, `.codex/agents/aria.md`), upgraded `/daniel` and `/architect`, introduced `/aria` alias, and introduced `/agent` for health/status/handoff workflows.
**Alternatives:** Keep only persona prompts and rely on ad-hoc behavior; add platform-wide changes before Codex-specific hardening.
**Rationale:** A runtime contract with explicit execution, verification, memory persistence, and handoff rules makes agents operationally reliable and easier to scale across sessions.

## 2026-02-15 — Dual Command Registration for Aria and Agent
**Context:** Slash command parsing can resolve against `.agent/workflows` in addition to `.codex/commands`, which caused `/aria` and `/agent` inconsistencies.
**Decision:** Added `.agent/workflows/aria.md` and `.agent/workflows/agent.md` as aliases/control-plane mirrors.
**Alternatives:** Keep commands only in `.codex/commands`; require manual retries when parser path differs.
**Rationale:** Registering in both command locations removes parser ambiguity and makes command behavior consistent.

## 2026-02-15 — Separate Skill Picker from Slash Commands
**Context:** The UI skill picker (`$`) only showed `Daniel`, while `/aria` exists as a slash command. This created confusion that Aria was missing or Daniel was outdated.
**Decision:** Added global Aria skill at `~/.codex/skills/aria` and updated Daniel skill metadata in `~/.codex/skills/daniel/agents/openai.yaml` to runtime-first wording.
**Alternatives:** Rely only on slash commands; leave skill picker unchanged.
**Rationale:** Keeping both skill and slash registries aligned makes agent activation predictable and reduces command UX confusion.

## 2026-02-15 — Research-First Routing for Portfolio Discovery
**Context:** Broad market and trend research for choosing portfolio projects was being started directly in-session, which conflicts with Web 3 routing rules.
**Decision:** Route initial broad research to Gemini first via `sync/tasks/gemini-web.md`, then use Aria for synthesis and project selection.
**Alternatives:** Keep doing first-pass research directly in Aria sessions.
**Rationale:** Gemini has unlimited research bandwidth and is the designated research engine; Aria should optimize decisions from aggregated evidence.

## 2026-02-15 — Mission Pivot to INR 100,000 Income Sprint
**Context:** Bibhu changed goal from portfolio-first to immediate earning-first with limited paid skills and no social media presence.
**Decision:** Prioritize cashflow plan: Gemini for income trend research, NotebookLM for sales/delivery docs, Claude Web for plan stress-test, then Daniel executes service stack and outreach assets.
**Alternatives:** Continue portfolio-first plan and delay monetization.
**Rationale:** Fast revenue reduces pressure and creates real-world proof; portfolio can be built from paid delivery outcomes.

## 2026-02-15 — One-Day 20-Project Free-Stack Blitz
**Context:** Goal changed from income sprint to publishing 20 GitHub projects in one day; zero budget for paid APIs.
**Decision:** Run Gemini-first intense research to select 20 high-signal projects that can be built fast using only free/open-source tooling; then execute in parallel batches with AI-agent supervision.
**Alternatives:** Build fewer deeper projects; continue income-first plan first.
**Rationale:** Immediate output volume on GitHub creates fast visible momentum while preserving zero-cost constraints.

## 2026-02-15 — World-Class Quality over One-Day Quantity
**Context:** Mission updated again: 20 projects must be world-class, and timeline extended to 2 weeks at full working-hour pace.
**Decision:** Keep 20-project target, add stricter quality gates, run 4 parallel Gemini research tracks first, then execute a 14-day plan with Codex + Antigravity lanes.
**Alternatives:** One-day rapid publish with lower depth.
**Rationale:** World-class quality yields stronger long-term portfolio signal while still preserving aggressive output and zero-cost constraints.

## 2026-02-15 — Split Gemini Research into 4 Account-Specific Task Files
**Context:** Bibhu is running four separate Gemini Pro accounts and needs independent instructions per account.
**Decision:** Replaced single combined Gemini task with a coordinator file plus four account-specific files in `sync/tasks/`.
**Alternatives:** Keep one large task file with four sections.
**Rationale:** Separate files reduce copy/paste friction, keep each account focused, and simplify parallel execution tracking.

## 2026-02-15 — Research Lane Rebalance: 2 Gemini + 1 SuperGrok
**Context:** Available research capacity changed from 4 Gemini accounts to 2 Gemini accounts plus 1 SuperGrok account.
**Decision:** Updated coordinator and task files to run three parallel lanes: Gemini-1 (trend), Gemini-2 (feasibility + packaging), SuperGrok-1 (benchmark + differentiation + ranking).
**Alternatives:** Keep four Gemini files and leave two unused; force SuperGrok to mimic one Gemini lane without role tuning.
**Rationale:** Lane rebalance matches actual capacity and preserves full research coverage with minimal coordination overhead.

## 2026-02-15 — Aria Orchestration Playbook as Single Operating Standard
**Context:** Aria behavior could drift because routing/tab/prompt logic was spread across multiple files and older assumptions.
**Decision:** Added `sync/config/aria-orchestration-playbook.md` and wired Aria runtime/commands/workflows/skill to read it by default.
**Alternatives:** Keep ad-hoc orchestration guidance inside command text only.
**Rationale:** Centralized orchestration policy improves consistency, removes ambiguity, and makes "which AI, how many tabs, what prompt" deterministic.

## 2026-02-15 — Capacity-Aware Aria Routing (Codex-First + Deep Research)
**Context:** Actual weekly capacity changed: Codex available for coding, Claude limited as backup, Antigravity available for strategy, ChatGPT Deep Research available, NotebookLM available.
**Decision:** Updated runtime/playbook to make ChatGPT Deep Research the primary research lane, keep Gemini/SuperGrok as optional expansion lanes, and lock Codex as primary builder.
**Alternatives:** Keep Gemini-first routing as default despite changed availability.
**Rationale:** Capacity-aware routing prevents tool mismatch and keeps execution aligned with real availability.

## 2026-02-15 — Deep Research Primary Task + Orchestrate Alignment
**Context:** Aria orchestration commands still contained Gemini-first wording that could cause execution drift.
**Decision:** Added `sync/tasks/chatgpt-deep-research.md` as primary research task and updated orchestrate command/workflow plus quality-gate wording to active-research terminology.
**Alternatives:** Keep legacy command wording and rely on manual interpretation.
**Rationale:** Aligning command text with runtime policy reduces ambiguity and makes Aria deterministic under pressure.

## 2026-02-15 — Weekly Phased Goal: Build → Social Proof → Revenue
**Context:** Weekly target is INR 100,000, with user-defined sequence: first build 20 projects, then social media presence, then money.
**Decision:** Adopt phased week execution model and add operational tasks for each phase (build quality gate, social content pack, revenue conversion gate).
**Alternatives:** Focus only on building; delay social and monetization setup.
**Rationale:** Sequencing from assets to proof to conversion improves trust and close rates from zero credibility starting point.

## 2026-02-15 — Research Lock Topology: 2 Gemini + 1 Claude
**Context:** User requested immediate hard research using 2 Gemini tabs and 1 Claude tab before any repo creation.
**Decision:** Set Gemini as primary research engine (two lanes), Claude Web as synthesis/freeze gate, and SuperGrok as optional booster.
**Alternatives:** ChatGPT Deep Research primary lane; build-first without freeze gate.
**Rationale:** Matches available tools and enforces high-confidence top-20 selection before implementation.

## 2026-02-15 — Prompt-Hardened Research Execution Pack
**Context:** Research tasks were structurally correct, but execution still required manual prompt authoring in each web tab.
**Decision:** Added copy-paste "hard research" prompts to Gemini lane A, Gemini lane B, Claude freeze gate, and SuperGrok booster task files, plus explicit run-order instructions in the Gemini coordinator.
**Alternatives:** Keep task files as checklist-only and write prompts ad-hoc each session.
**Rationale:** Prompt hardening reduces ambiguity, speeds tab execution, and improves repeatability under high-hour sprint pressure.

## 2026-02-15 — Provisional Freeze from SuperGrok Snapshot
**Context:** `sync/inbox/` had no persisted research files, but user provided a full SuperGrok-style ranking/benchmark output in-session and requested momentum toward the 20-repo sprint.
**Decision:** Captured the user-provided research into a SuperGrok inbox snapshot and generated a `PROVISIONAL-FROZEN` Claude quality gate output at `sync/inbox/2026-02-15-claude-web-worldclass-20project-quality-gate.md`.
**Alternatives:** Block execution until all Gemini exports are present; keep analysis only in chat without file persistence.
**Rationale:** Preserving momentum with a file-based freeze enables immediate execution while still allowing controlled deltas if stronger lane outputs arrive.

## 2026-02-15 — Cross-Agent 10-Task Pack + Daniel Build Trigger
**Context:** User requested a direct assignment of 10 tasks across ChatGPT, Gemini, Grok, NotebookLM, and Antigravity, and asked Daniel to start building immediately.
**Decision:** Added a unified assignment manifest (`sync/tasks/cross-agent-10pack.md`), added Antigravity task file (`sync/tasks/antigravity.md`), and created Daniel handoff file (`sync/sessions/2026-02-15-agent-handoff-daniel-001.md`) with Batch A start order.
**Alternatives:** Keep only existing Gemini/Claude tasks and postpone Antigravity/ChatGPT assignments; wait for full research completion before any build work.
**Rationale:** Explicit task IDs and platform ownership improve execution speed, reduce coordination overhead, and keep Daniel unblocked.
