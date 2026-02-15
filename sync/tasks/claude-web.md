# Tasks for Claude Web — Deep Analyst

**Role:** Focused thinking on hard problems. Architecture analysis, design decisions, complex debugging, one clear answer. Not a research farm — that's Gemini. Claude Web goes DEEP on specific questions.

## Active Tasks

### 2026-02-15 — World-Class Quality Gate for 20 Projects (Priority: Critical)
**Assigned by:** codex (Aria)
**Mission:** Validate the active research shortlist for world-class quality, recruiter impact, and 2-week execution realism.
**Context:** Claude Code unavailable today; Codex + Antigravity execution must be tightly scoped.
**Expected output:** Final go/no-go 20 list with quality interventions.

#### Copy-Paste Prompt (Claude Web)
```text
You are the final quality gate and freeze authority for selecting 20 world-class portfolio projects.
Current date: 2026-02-15.

Inputs:
- sync/inbox/2026-02-15-gemini-web-account-1-trends.md
- sync/inbox/2026-02-15-gemini-web-account-2-feasibility.md

Hard constraints:
- Zero paid API/service dependency.
- Two-week build horizon.
- Must maximize recruiter signal and demo quality.

Required process:
1) Merge and deduplicate candidates.
2) Remove weak/generic ideas and explain each removal.
3) Detect hidden paid dependencies and replace with free alternatives.
4) Score candidates using weighted model:
   - impact/recruiter signal (30%)
   - technical depth (25%)
   - build-time feasibility (20%)
   - differentiation (15%)
   - demo reliability (10%)
5) Rank by world-class impact per build-hour.
6) For selected projects, suggest scope cuts/additions to hit world-class bar.
7) Freeze final decision set.

Output format (strict):
- Section 1: Merge + dedupe notes
- Section 2: Removed ideas with reasons
- Section 3: Paid dependency risk table with free replacements
- Section 4: Scored ranking table
- Section 5: GO top-20
- Section 6: NO-GO list
- Section 7: 5 backups
- Section 8: Week 1 / Week 2 allocation
```

#### Analysis Tasks
1. Ingest:
   - `sync/inbox/2026-02-15-gemini-web-account-1-trends.md`
   - `sync/inbox/2026-02-15-gemini-web-account-2-feasibility.md`
2. Merge and de-duplicate candidate set.
3. Remove weak/generic ideas and explain each removal.
4. Flag hidden paid-service dependencies and free alternatives.
5. Re-rank by "world-class impact per build-hour".
6. Recommend where to cut scope or add depth for each selected project.
7. Produce final frozen output:
   - GO top-20
   - NO-GO list
   - 5 backups
   - Week 1 / Week 2 allocation

#### Delivery
1. Run analysis in Claude Web.
2. Export conversation as markdown.
3. Save to: `sync/inbox/2026-02-15-claude-web-worldclass-20project-quality-gate.md`

### 2026-02-15 — Revenue Conversion Quality Gate (Priority: Medium)
**Assigned by:** codex (Aria)
**Mission:** Stress-test pricing, outreach, and conversion strategy for INR 100,000 week goal.
**Context:** After Day-1 build and social proof setup, monetization is the main objective.
**Expected output:** One conversion-focused recommendation set.

#### Analysis Tasks
1. Review service offers and identify which 2 should be primary for fast close.
2. Stress-test outreach messaging for trust gap (no credibility history).
3. Suggest pricing floor/ceiling and negotiation boundaries.
4. Identify top 5 failure modes in closing deals this week and mitigations.

#### Delivery
1. Run analysis in Claude Web.
2. Export conversation as markdown.
3. Save to: `sync/inbox/2026-02-15-claude-web-revenue-conversion-gate.md`

## How Claude Web Works

Claude Web handles the hard thinking. When the Big 3 need a focused, web-enhanced analysis on one specific problem, Claude Web does it.

**What to assign:**
- "Analyze this architecture and find the weak points"
- "Compare these 2 approaches for our specific use case — which is better and why?"
- "Review this code and give a detailed critique"
- "Research this one specific question deeply and give a clear recommendation"
- "Think through the trade-offs of [decision] for our project"

**Expected output:** Clear analysis with a recommendation. Not a research dump — a decision.
