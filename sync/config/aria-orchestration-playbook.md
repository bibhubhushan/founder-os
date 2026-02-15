# Aria Orchestration Playbook

**Last updated:** 2026-02-15
**Scope:** How Aria decides which AI to use, how many tabs to open, and what prompts to run.

## Core Rule

Pick tools by task type, not by habit.

## Routing Matrix

| Task Type | Primary | Secondary | Tabs |
|---|---|---|---|
| Broad trend research | Gemini | SuperGrok | 1 Gemini |
| Free-stack feasibility | Gemini | Codex quick check | 1 Gemini |
| Research synthesis + shortlist freeze | Claude Web | Aria | 1 Claude Web |
| Final quality gate | Claude Web | SuperGrok | 1 Claude Web |
| Documentation system | NotebookLM | Aria structure | 1 NotebookLM |
| Build implementation | Daniel (Codex) | Claude backup + Aria QA | 2 build tabs max |
| Strategic decisions | Antigravity | Aria | 1 Antigravity |

## Default Tab Layout (Current Mission)

1. Gemini Tab A: Trend + opportunity lane
2. Gemini Tab B: Feasibility + architecture + packaging lane
3. Claude Web Tab: Synthesis, ranking, and freeze gate
4. Antigravity Tab: Strategic tradeoff and sequencing checks
5. Codex Tab: Implementation planning and build execution
6. NotebookLM Tab: Documentation pack (parallel after freeze)
7. SuperGrok Tab (optional): differentiation stress-test

## Prompt Templates

### Template A — Gemini Tab A (Trend + Opportunity)

```md
Mission: Identify top opportunities for [goal].
Constraints: free stack only, no paid API, avoid generic clones.
Required output:
1. Trend evidence with sources
2. Ranked categories
3. Longlist of 50 candidate ideas with role alignment
```

### Template B — Gemini Tab B (Feasibility + Packaging)

```md
For each candidate idea:
- free stack choices
- paid dependency disqualification check
- effort estimate
- architecture recommendation
- preliminary execution card
Return top 30 feasible ideas.
```

### Template C — Claude Web Synthesis + Freeze Gate

```md
Inputs:
- Gemini Tab A output
- Gemini Tab B output
Tasks:
1. Merge and dedupe candidates
2. Remove weak/generic projects
3. Rank by world-class impact per build-hour
4. Final GO/NO-GO top-20 with week allocation + fallback 5
```

### Template D — Antigravity Strategy Check

```md
Given frozen top-20 list:
- optimize sequence
- identify dependency bottlenecks
- define scope cuts/additions
- output 14-day execution map
```

### Template E — NotebookLM Documentation Lane

```md
Create reusable docs for all repos:
- master README template
- architecture/depth section template
- project summary template
- portfolio index template
- sprint report template
```

### Template F — SuperGrok Optional Booster

```md
Input: frozen top-20 list from Claude Web.
Task: stress-test differentiation and suggest 3 upgrades per weak project.
Return only deltas and risk flags.
```

## Aria Decision Algorithm

1. Clarify mission and hard constraints.
2. Select lane topology from routing matrix.
3. Assign one file per lane in `sync/tasks/`.
4. Lock output filenames in `sync/inbox/`.
5. Run quality gate before freeze.
6. Freeze backlog and handoff to Daniel.

## Guardrails

- Never start coding before research shortlist freeze.
- Never allow paid dependency if mission says zero budget.
- Keep parallel tabs to what can be monitored.
- If inputs are missing, ask one precise question and continue.
