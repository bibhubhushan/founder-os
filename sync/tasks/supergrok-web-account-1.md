# SuperGrok Account 1 — Benchmark + Differentiation + Final Ranking

**Date:** 2026-02-15  
**Priority:** Critical  
**Mission:** Act as optional booster lane to stress-test differentiation and ranking quality.

**Task-pack link:** `sync/tasks/cross-agent-10pack.md` (Task IDs 05-06)

## Copy-Paste Prompt (SuperGrok Optional Booster)

```text
You are a portfolio differentiation and benchmark strategist.
Goal: stress-test whether candidate projects are truly world-class and not generic.
Current date: 2026-02-15.

Inputs:
- sync/inbox/2026-02-15-gemini-web-account-1-trends.md
- sync/inbox/2026-02-15-gemini-web-account-2-feasibility.md
- sync/inbox/2026-02-15-claude-web-worldclass-20project-quality-gate.md (if available)

Required process:
1) Benchmark 50 strong GitHub portfolio repos.
2) Identify overused low-signal project patterns to avoid.
3) For each serious candidate, propose 2-3 differentiation hooks:
   - workflow uniqueness
   - dataset angle
   - UX/UI edge
   - automation/reliability edge
4) Define world-class rubric:
   - engineering quality
   - product thinking
   - UI quality
   - docs quality
   - measurable impact
5) Score candidates (1-10 each dimension).
6) Produce top-20 ranking for a 14-day sprint with week split + 5 backups.
7) If Claude frozen list exists, return only deltas and why.

Output format (strict):
- Section 1: Overused patterns to avoid
- Section 2: Differentiation hooks by candidate
- Section 3: Rubric and scored table
- Section 4: Final ranked top-20 with week allocation
- Section 5: Backup list + risk notes
```

## Inputs

- `sync/inbox/2026-02-15-gemini-web-account-1-trends.md`
- `sync/inbox/2026-02-15-gemini-web-account-2-feasibility.md`
- `sync/inbox/2026-02-15-claude-web-worldclass-20project-quality-gate.md` (if available)

## Tasks

1. Benchmark 50 strong GitHub portfolio repositories.
2. Identify overused low-signal project types to avoid.
3. For each serious candidate idea, propose 2-3 differentiation hooks:
- unique workflow
- dataset angle
- UX/UI edge
- automation/reliability feature
4. Define world-class rubric:
- engineering quality
- product thinking
- UI quality
- docs quality
- measurable impact
5. Score candidates using the rubric (1-10 per dimension).
6. Produce top-20 final ranking for a 14-day sprint with:
- Week 1 and Week 2 assignment
- fallback list (5 projects)
7. If Claude frozen list exists, return only deltas (what should change and why).

## Output Format

- Section 1: Overused patterns to avoid
- Section 2: Differentiation hooks by candidate
- Section 3: Rubric + scored table
- Section 4: Final ranked top 20 + week allocation
- Section 5: Fallback list and risk notes

## Delivery

1. Export SuperGrok conversation as markdown.
2. Save to: `sync/inbox/2026-02-15-supergrok-account-1-quality-and-ranking.md`
