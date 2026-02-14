# FounderOS System Spec (v1)

This document defines the minimum contract for reliable FounderOS behavior.

## 1. Runtime Loop

1. Intake user request
2. Route to specialist (`/route` or explicit command)
3. Execute specialist workflow
4. Produce concrete output (plan/spec/code/review)
5. Persist memory updates
6. Record evaluation

## 2. Routing Contract

Inputs:
- User intent sentence
- Current project context from `memory/ACTIVE_PROJECT.md`

Outputs:
- Selected command/agent
- Rationale in one sentence
- Next action

Fallback:
- If ambiguous, request one clarifying choice among: strategy, ops, build, design, learning

## 3. Agent Contract

Each agent must:
- Stay within domain scope
- Defer cross-domain work to correct specialist
- Return actionable output (not generic advice)
- Use current memory context

## 4. Memory Contract

Required files:
- `memory/ACTIVE_PROJECT.md`
- `memory/DECISIONS.md`
- `memory/JOURNAL.md`
- `memory/LESSONS.md`
- `memory/EVALS.md`

Every session should append at least:
- One decision or explicit “no decision” note
- One journal line
- One evaluation entry

## 5. Output Quality Contract

Responses should be:
- Specific
- Measurable
- Time-bound
- Owner-assigned (user/agent)

## 6. Success Metrics

Track weekly:
- `% tasks completed without re-prompt`
- `time-to-first-action` from request to first executable task
- `features shipped/week`
- `decision revisit rate` (lower is better)
