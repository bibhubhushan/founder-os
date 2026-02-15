# Multi-Agent Patterns

**Added:** 2025-02-15
**Source:** Research + bibhu_os design
**Added by:** Aria

## Common Patterns

### 1. Supervisor
One agent manages others. Decides who does what.
```
Supervisor → Agent A
           → Agent B
           → Agent C
```
**Use when:** Tasks need routing based on type.
**bibhu_os uses this:** Aria (architect) plans, Daniels (builders) execute.

### 2. Peer Network
All agents are equal. Share a common workspace.
```
Agent A ←→ Agent B ←→ Agent C
```
**Use when:** Agents have equal capability and need to collaborate.
**bibhu_os uses this:** Big 3 (Claude Code, Codex, AI Studio) are peers.

### 3. Hub and Spoke
Central knowledge store. Agents read/write to it.
```
Agent A → Hub ← Agent B
Agent C → Hub ← Agent D
```
**Use when:** Agents are on different platforms and can't talk directly.
**bibhu_os uses this:** GitHub repo is the hub. All agents read/write to it.

### 4. Pipeline
Output of one agent is input to the next.
```
Agent A → Agent B → Agent C → Done
```
**Use when:** Tasks have clear stages (research → plan → build → test).
**bibhu_os uses this:** Aria plans → Daniel builds → Daniel tests → Daniel ships.

### 5. Redundancy
Multiple agents can do the same job. If one fails, another takes over.
```
Agent A (primary) → fails
Agent B (backup)  → picks up work
```
**Use when:** Reliability matters. Can't afford downtime.
**bibhu_os uses this:** All Big 3 can do everything. If one's down, others continue.

## What bibhu_os Does

bibhu_os combines patterns 2, 3, 4, and 5:
- **Peer network** for Big 3
- **Hub and spoke** for cross-platform sync
- **Pipeline** for Aria → Daniel workflow
- **Redundancy** across all Big 3
