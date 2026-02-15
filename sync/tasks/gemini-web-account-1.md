# Gemini Account 1 — Hard Research Lane A (Trend + Opportunity Intelligence)

**Date:** 2026-02-15  
**Priority:** Critical  
**Mission:** Produce a high-confidence opportunity map for world-class portfolio project selection.

## Copy-Paste Prompt (Gemini Tab A)

```text
You are a principal market-intelligence analyst helping select 20 world-class GitHub portfolio projects.

Goal:
- Build a high-confidence opportunity map for projects that can be shipped in 14 days.
- Current date: 2026-02-15.

Hard constraints:
- Zero budget: no paid APIs/services in final project set.
- Avoid generic clone projects.
- Prioritize ideas with strong recruiter signal in 2025-2026.

Required process:
1) Identify high-signal trend categories across:
   - product engineering
   - AI tooling
   - automation
   - developer platforms
   - data applications
2) Use evidence and include sources for every trend claim.
3) Rank categories using a weighted model:
   - GitHub trend activity (40%)
   - hiring relevance (35%)
   - demo value (25%)
4) Generate 60 candidate project ideas from top categories.
5) For each idea include:
   - one-line pitch
   - "why now" signal
   - role alignment (frontend/full-stack/AI/devtools/data)
   - likely reviewer persona
6) Mark top 25 high-conviction candidates with short reasoning.

Output format (strict):
- Section 1: Trend evidence with source links
- Section 2: Ranked categories and weighted score table
- Section 3: Top 60 candidate ideas with tags
- Section 4: Top 25 shortlist with rationale
```

## Tasks

1. Identify top 2025-2026 trend categories with high recruiter attention across:
- product engineering
- AI tooling
- automation
- developer platforms
- data applications
2. Rank categories by weighted signal:
- GitHub trend activity
- hiring relevance
- demo value
3. Generate top 60 candidate project ideas from those categories.
4. Tag each candidate with role alignment and likely reviewer persona:
- frontend
- full-stack
- AI engineer
- devtools
- data/ML
5. Add "why this matters now" one-liner for each candidate.
6. Mark top 25 high-conviction candidates.

## Output Format

- Section 1: Trend evidence with sources
- Section 2: Ranked categories
- Section 3: Top 60 candidate ideas with role tags
- Section 4: Top 25 high-conviction shortlist

## Delivery

1. Export Gemini conversation as markdown.
2. Save to: `sync/inbox/2026-02-15-gemini-web-account-1-trends.md`
