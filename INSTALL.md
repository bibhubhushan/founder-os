# Install FounderOS (Antigravity)

## Prerequisites

- Access to Google Antigravity
- A workspace where markdown files and workflows are available

## Setup

1. Copy this repo into your Antigravity workspace.
2. Keep folder structure unchanged.
3. Confirm these folders exist:
   - `.agent/workflows/`
   - `01_SATOSHI/`, `03_ELON/`, `04_DANIEL/`, `05_BRIAN/`, `06_ANDREJ/`
   - `memory/`
4. Open `START_HERE.md`.
5. Fill `memory/ACTIVE_PROJECT.md` before first use.

## First Run

1. Start the local app:
   - `./run_local.sh 8787`
2. Open `http://127.0.0.1:8787`
3. Send: `/route I need to plan and ship this week`
4. Execute recommended agent command
5. End by updating memory files

## Upgrade Path

When pulling updates:
1. Keep your existing `memory/*` data
2. Pull new workflow/instruction files
3. Review `CHANGELOG.md`

## Troubleshooting

- Wrong routing: use `/route` with a clearer intent sentence
- Lost context: verify `memory/ACTIVE_PROJECT.md` and `memory/JOURNAL.md`
- Conflicting agent advice: run `/all_hands` and force one decision
