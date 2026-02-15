# Tasks for Gemini — Coordinator

**Date:** 2026-02-15  
**Assigned by:** codex (Aria)  
**Mission:** Primary research engine for selecting world-class top-20 projects before coding starts.

**Task-pack link:** `sync/tasks/cross-agent-10pack.md` (Task IDs 03-04)

**Status:** Primary (mandatory before build).

## Parallel Assignment Map

Use one account per file:

1. `sync/tasks/gemini-web-account-1.md` — Trend + Opportunity Intelligence
2. `sync/tasks/gemini-web-account-2.md` — Free Stack + Architecture Feasibility + Packaging
3. `sync/tasks/supergrok-web-account-1.md` — Benchmark + Differentiation + Ranking

## Run Order (Now)

1. Start `sync/tasks/gemini-web-account-1.md` in Gemini Tab A.
2. Start `sync/tasks/gemini-web-account-2.md` in Gemini Tab B at the same time.
3. Optional: start `sync/tasks/supergrok-web-account-1.md` in SuperGrok for benchmark lane.
4. Wait until both Gemini outputs are exported into `sync/inbox/`.
5. Run Claude synthesis/freeze via `sync/tasks/claude-web.md`.
6. No coding before frozen top-20 file exists.

## Merge Instructions

After Gemini lane outputs are done:

1. Feed both Gemini outputs into Claude Web synthesis gate (`sync/tasks/claude-web.md`).
2. Freeze final top-20 list only after Claude output.
3. Save frozen output to: `sync/inbox/2026-02-15-claude-web-worldclass-20project-quality-gate.md`

## Hard Constraints

- No paid AI API usage.
- Use only free/open-source/local/offline options.
- Focus on world-class depth, not generic ideas.
