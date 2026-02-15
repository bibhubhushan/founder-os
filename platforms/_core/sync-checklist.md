# Sync Checklist — Updating Daniel Across Platforms

When Daniel's personality, values, or rules change, propagate the update to all variants.

## Steps

1. Edit `platforms/_core/daniel-core.md` (the source of truth)
2. Update date in `daniel-core.md`
3. Propagate changes to each variant:

| # | Platform | File to Update |
|---|----------|---------------|
| 1 | Claude Code | `CLAUDE.md` (project root) |
| 2 | OpenAI Codex | `platforms/codex/AGENTS.md` |
| 3 | Google AI Studio | `platforms/ai-studio/system-instructions.md` |
| 4 | Gemini Gems | `platforms/gemini-gems/gem-instructions.md` |
| 5 | Claude Web | `platforms/claude-web/project-instructions.md` |
| 6 | NotebookLM | `platforms/notebooklm/notebook-instructions.md` |

4. After updating NotebookLM, verify character count is still under 10,000
5. Re-paste updated instructions into web-based platforms (AI Studio, Gems, Claude Web, NotebookLM)

## What Lives Where

- **Identity, vibe, values, philosophy, rules** → `_core/daniel-core.md`
- **Coding standards** → `standards/rules.md` (full) + `_core/rules-condensed.md` (compressed)
- **Memory protocol** → Platform-specific (different per variant)
- **Tool usage** → Platform-specific (different per variant)
- **Commands/triggers** → Platform-specific (different per variant)

## When to Sync

- Daniel's personality or backstory changes
- Values are added or modified
- Rules are added or modified
- Building philosophy is updated
- Coding standards change (update both full and condensed versions)
