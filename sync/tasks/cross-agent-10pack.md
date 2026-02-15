# Cross-Agent 10 Task Pack (Week Execution)

**Date:** 2026-02-15  
**Week window:** 2026-02-16 to 2026-02-22  
**Assigned by:** codex (Aria)  
**Mission:** Run 10 parallel tasks across ChatGPT, Gemini, Grok, NotebookLM, and Antigravity, then let Daniel execute builds at maximum pace.

## Hard Constraints

- Zero paid API/service dependency in all recommended builds.
- Avoid generic clone projects.
- Every output must be exportable to `sync/inbox/` as markdown.
- Use concrete dates in plans and sequence.

## Task Map (10 Total)

| ID | Platform | Task | Output file |
|---|---|---|---|
| 01 | ChatGPT | Demand map: top buyer problems solved by the frozen top-20 ideas; include evidence and urgency score | `sync/inbox/2026-02-16-chatgpt-demand-map.md` |
| 02 | ChatGPT | Offer/pricing map: convert top-20 into 2 sellable service offers with pricing floors/ceilings and close script | `sync/inbox/2026-02-16-chatgpt-offer-pricing-map.md` |
| 03 | Gemini Tab A | Trend + opportunity refresh with source-backed deltas against current frozen top-20 | `sync/inbox/2026-02-16-gemini-a-trend-deltas.md` |
| 04 | Gemini Tab B | Free-stack feasibility, build-time estimates, and risk cards for all 20 projects | `sync/inbox/2026-02-16-gemini-b-feasibility-cards.md` |
| 05 | Grok | Benchmark 100 strong portfolio repos and flag overused low-signal patterns | `sync/inbox/2026-02-16-grok-benchmark-and-antipatterns.md` |
| 06 | Grok | Differentiation deltas: 2-3 upgrades per weak project in frozen top-20 | `sync/inbox/2026-02-16-grok-differentiation-deltas.md` |
| 07 | NotebookLM | Master docs kit for 20 repos (README, architecture, demo script, project card templates) | `sync/inbox/2026-02-16-notebooklm-docs-kit.md` |
| 08 | NotebookLM | Social + monetization kit (7-day calendar, 20 post drafts, outreach templates, proposal template) | `sync/inbox/2026-02-16-notebooklm-social-monetization-kit.md` |
| 09 | Antigravity | 100-hour week execution board (hour blocks, daily goals, dependency map, failover plan) | `sync/inbox/2026-02-16-antigravity-execution-board.md` |
| 10 | Antigravity | Build sequencing for Daniel: batch order, scope cuts, quality gates, and recovery playbook | `sync/inbox/2026-02-16-antigravity-build-sequencing.md` |

## Run Order

1. Run Tasks 03, 04, 05 in parallel first (research confidence).
2. Run Task 06 after Task 05 or after freeze deltas are available.
3. Run Tasks 07 and 08 in parallel with research.
4. Run Tasks 09 and 10 once first research deltas are available.
5. Run Tasks 01 and 02 after updated shortlist confidence.

## Daniel Trigger

Daniel starts implementation from frozen list immediately and applies only explicit delta updates from tasks 03/04/06/10.
