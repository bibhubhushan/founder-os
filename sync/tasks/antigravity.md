# Tasks for Antigravity (AI Studio) — Strategy and Sequencing

**Date:** 2026-02-15  
**Assigned by:** codex (Aria)  
**Priority:** Critical  
**Mission:** Convert frozen project shortlist into an execution system Daniel can run at high speed.

## Active Tasks

### 2026-02-16 — 100-Hour Week Execution Board
**Goal:** Build an hour-by-hour plan for 2026-02-16 to 2026-02-22.

#### Prompt
```text
You are the strategy lead for a 100-hour build week.
Create a concrete execution board for 2026-02-16 to 2026-02-22.

Inputs:
- sync/inbox/2026-02-15-claude-web-worldclass-20project-quality-gate.md
- Goal: publish 20 world-class repos, then convert to INR 100,000 path.

Output:
1) Daily hour blocks
2) Project batching logic
3) Dependency chain and critical path
4) Buffer blocks and failure-recovery slots
5) Daily KPI scoreboard
```

#### Delivery
1. Export Antigravity output as markdown.
2. Save to: `sync/inbox/2026-02-16-antigravity-execution-board.md`

### 2026-02-16 — Daniel Build Sequencing + Recovery Playbook
**Goal:** Decide exact build order and fallback operations for all 20 repos.

#### Prompt
```text
Given the frozen top-20 file, design Daniel's build sequencing plan.

Required:
1) Batch order (5 repos per batch)
2) Scope cuts per repo to maintain quality under time pressure
3) Quality gate checklist before each publish
4) Delta-application rule when research updates arrive
5) Recovery playbook for blocked repos (swap with backups)
```

#### Delivery
1. Export Antigravity output as markdown.
2. Save to: `sync/inbox/2026-02-16-antigravity-build-sequencing.md`
