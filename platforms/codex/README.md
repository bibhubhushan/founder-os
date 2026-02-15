# Daniel for OpenAI Codex

## What This Is

Daniel persona adapted for OpenAI Codex. Codex is the closest to Claude Code — full file access, bash execution, and agentic coding capabilities. The `AGENTS.md` file is Codex's equivalent of `CLAUDE.md`.

## Setup

### Option 1: Per-Project (Recommended)
Copy `AGENTS.md` to your project root:
```bash
cp platforms/codex/AGENTS.md /path/to/your/project/AGENTS.md
```

### Option 2: Global
Copy to your global Codex config:
```bash
mkdir -p ~/.codex
cp platforms/codex/AGENTS.md ~/.codex/AGENTS.md
```

### Memory Directory
Ensure the `memory/` and `standards/` directories are accessible from the project root. If using Daniel across multiple projects, symlink them:
```bash
ln -s /path/to/bibhu_os/memory ./memory
ln -s /path/to/bibhu_os/standards ./standards
```

## Key Differences from Claude Code

| Feature | Claude Code | Codex |
|---------|------------|-------|
| Instruction file | `CLAUDE.md` | `AGENTS.md` |
| Tool abstractions | Read, Write, Edit, Grep, Glob | Direct bash (cat, grep, find, etc.) |
| Web browsing | Built-in WebFetch | Cached by default, `--search` for live |
| File hierarchy | Project root only | Walks from repo root to current dir |

## Usage

Start a Codex session in your project directory. Daniel will automatically load from `AGENTS.md` and begin the boot-up sequence (reading memory files, greeting you).

Use natural language triggers: "scaffold a Next.js app", "debug this error", "review the changes", "ship it".
