# Gemini Account 2 — Hard Research Lane B (Feasibility + Architecture + Packaging)

**Date:** 2026-02-15  
**Priority:** Critical  
**Mission:** Stress-test feasibility and architecture quality for world-class execution under zero budget.

## Copy-Paste Prompt (Gemini Tab B)

```text
You are a principal software architect and feasibility analyst.
Goal: stress-test project feasibility for 20 world-class portfolio repos that must be built in 14 days with zero budget.
Current date: 2026-02-15.

Hard constraints:
- No paid APIs/services.
- Prefer free/open-source/local/self-host options.
- Flag anything with hidden paid dependency risk.

Inputs:
- If I provide shortlist from Gemini Tab A, evaluate those directly.
- If shortlist is not yet available, start with your own 60 high-signal candidates and label this as "provisional set". Keep structure ready to remap quickly.

Required analysis:
1) For each candidate, map free stack options:
   - frontend
   - backend
   - database
   - hosting
   - auth
   - analytics
2) Disqualify ideas needing paid dependency.
3) Estimate build effort for world-class scope:
   - 4-8h
   - 8-16h
   - 16h+
4) Suggest architecture pattern:
   - monolith
   - service split
   - event-driven
   - queue-based (if relevant)
5) Flag key risks:
   - scaling bottleneck
   - data dependency
   - deployment risk
   - demo fragility
6) Create execution cards for top candidates with:
   - repo name
   - one-line pitch
   - MVP features
   - stretch features
   - free stack
   - demo data source
   - build-time estimate
   - risk level

Output format (strict):
- Section 1: Free stack matrix
- Section 2: Disqualified ideas and reasons
- Section 3: Effort + architecture recommendations
- Section 4: Risk matrix by candidate
- Section 5: Execution cards
```

## Tasks

1. For each shortlisted candidate from Account 1, map fully free stack options:
- frontend
- backend
- database
- hosting
- auth
- analytics
2. Exclude ideas requiring paid APIs/services.
3. Estimate effort bands for world-class scope:
- 4-8h
- 8-16h
- 16h+
4. Suggest architecture pattern for each:
- monolith
- service split
- event-driven
- queue-based (when relevant)
5. Flag high-risk architecture concerns:
- scaling bottlenecks
- data dependency risk
- deployment risk
- demo fragility risk
6. Create preliminary execution cards for top candidates:
- repo name
- one-line pitch
- MVP features
- stretch features
- free stack
- demo data/source
- build-time estimate
- risk level

## Output Format

- Section 1: Free stack matrix
- Section 2: Disqualified ideas and reasons
- Section 3: Effort estimates + architecture recommendation
- Section 4: Risk matrix by candidate
- Section 5: Preliminary execution cards

## Delivery

1. Export Gemini conversation as markdown.
2. Save to: `sync/inbox/2026-02-15-gemini-web-account-2-feasibility.md`
