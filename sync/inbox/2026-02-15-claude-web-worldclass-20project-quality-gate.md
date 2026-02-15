# Claude Web — World-Class 20 Project Quality Gate (Frozen v1)

**Date:** 2026-02-15
**Owner:** Aria/Codex synthesis
**Freeze status:** `PROVISIONAL-FROZEN` (ready to build; replace only if stronger Gemini evidence arrives)

## Inputs Used

- `sync/inbox/2026-02-15-supergrok-account-1-quality-and-ranking.md`
- User-pasted benchmark/ranking analysis (same session)

## Constraint Checks

- Enforced: no paid AI API/service dependency.
- Enforced: 14-day execution horizon.
- Enforced: non-generic, recruiter-visible, demoable outcomes.
- Enforced: each project must include a clear differentiation hook.

## Removed / NO-GO Reasoning

- Blockchain AI marketplace: over-scoped and high integration risk for 14 days.
- VR/AR AI experience: hardware and testing constraints too high.
- Quantum simulation app: compute/knowledge overhead too high for sprint goal.
- Robotics control interface: hardware dependency risk.
- GPT-5-specific chatbot framing: violates zero-paid dependency constraint.
- Generic sentiment-analysis-only app: low differentiation.
- Tutorial-clone full-stack AI app (generic): weak signal unless deeply specialized.

## GO Top-20 (Final Build List)

| # | Repo | One-line pitch | Free stack | Effort | Week |
|---|---|---|---|---|---|
| 1 | `agent-orchestrator-studio` | Multi-agent workflow planner with execution graph + run logs | Next.js, FastAPI, SQLite, Redis, Docker | 8-16h | 1 |
| 2 | `realtime-collab-editor-ai` | CRDT-based realtime editor with local AI rewrite/summarize | React, Yjs, Node, WebSocket, Ollama | 8-16h | 1 |
| 3 | `local-rag-workbench` | Local-first RAG playground with eval and chunk strategy compare | Python, FastAPI, Chroma, Ollama | 8-16h | 1 |
| 4 | `prompt-eval-lab` | Prompt/version regression harness with scorecards | Python, pytest, SQLite, Streamlit | 4-8h | 1 |
| 5 | `incident-copilot-selfhosted` | Converts logs/incidents into postmortem draft + action items | FastAPI, Postgres, LangChain OSS, Ollama | 8-16h | 1 |
| 6 | `mlops-mini-platform` | Train-register-deploy-monitor pipeline for small models | DVC, MLflow OSS, FastAPI, Docker | 8-16h | 1 |
| 7 | `model-observability-lite` | Drift/latency/error monitoring dashboard for inference APIs | Prometheus, Grafana, FastAPI, Postgres | 8-16h | 1 |
| 8 | `data-lineage-tracker` | Dataset and feature lineage with reproducibility checks | Python, OpenLineage, Postgres, dbt-core | 8-16h | 1 |
| 9 | `semantic-code-search-local` | Codebase semantic search with local embeddings | Rust or Python, Tantivy/FAISS, Ollama | 8-16h | 1 |
|10| `browser-qa-agent` | Browser automation QA agent with failure triage | Playwright, Node, SQLite, GitHub Actions | 4-8h | 1 |
|11| `api-contract-guardian` | Contract-testing gate that blocks breaking API changes | Pact, Node, CI workflows, OpenAPI | 4-8h | 2 |
|12| `accessibility-autofix-ci` | Detects and proposes accessibility fixes in PRs | axe-core, Playwright, Node, CI bot | 4-8h | 2 |
|13| `job-queue-inspector` | Visual queue debugging + retry/poison-message workflows | BullMQ, Redis, React, Nest/Fastify | 4-8h | 2 |
|14| `feature-flag-experiment-kit` | Lightweight flags + A/B results with audit history | Next.js, Postgres, Prisma, Docker | 8-16h | 2 |
|15| `privacy-analytics-dashboard` | Product analytics without third-party trackers | PostHog OSS, Next.js, ClickHouse OSS | 8-16h | 2 |
|16| `green-ci-profiler` | CI energy/time profiler with optimization suggestions | GitHub Actions, Python, SQLite, Charts | 4-8h | 2 |
|17| `finops-anomaly-detector` | Detects cloud spend anomalies from exported billing CSVs | Python, Prophet/sklearn, Streamlit | 4-8h | 2 |
|18| `zero-trust-auth-starter` | Passkey + device-bound auth starter with audit trails | NextAuth/Auth.js, WebAuthn, Postgres | 8-16h | 2 |
|19| `offline-first-sync-starter` | Offline-first sync template with conflict resolution demo | PouchDB/CouchDB, React, Service Worker | 8-16h | 2 |
|20| `synthetic-data-studio` | Generate privacy-safe synthetic tabular datasets + quality report | Python, SDV, Pandas, Streamlit | 8-16h | 2 |

## 5 Backups

1. `explainable-ai-dashboard` — model decision trace and SHAP visual analysis.
2. `adaptive-ui-engine` — behavior-aware UI adaptation with strict guardrails.
3. `cyber-threat-hunter-lite` — log anomaly + triage assistant.
4. `multimodal-retrieval-demo` — text-image retrieval with local embeddings.
5. `recommendation-system-starter` — reproducible recommendation benchmark kit.

## Build Guardrails (Non-Negotiable)

- No external paid APIs in critical path.
- Each repo must include: live demo video, architecture diagram, README with tradeoffs, and benchmark metric.
- Default quality floor: tests for happy path + 1 error path, CI pass, deterministic setup script.
- Keep each repo under a single clear problem statement; avoid feature sprawl.

## Execution Lock

Coding can start now against the GO Top-20 list above.
If Gemini lane exports later introduce stronger evidence, apply changes only through explicit delta review, not ad-hoc replacement.
