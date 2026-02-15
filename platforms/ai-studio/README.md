# Daniel for Antigravity (Google AI Studio)

## What This Is

Daniel persona adapted for Antigravity — Google AI Studio's agentic coding platform. Antigravity is a **full-power builder** with file access, terminal execution, browser tools, image generation, and task management. It is an equal member of the Big 3, not a limited paste-based tool.

## Setup

1. The `system-instructions.md` file is automatically loaded by Antigravity when working in the `bibhu_os` workspace.
2. No manual copy-paste needed — Antigravity reads files directly.

### Memory Directory
Antigravity reads and writes to `memory/` and `standards/` directories directly via file tools. No symlinks or manual setup required.

## Capabilities

| Capability | How |
|---|---|
| Read files | `view_file`, `view_file_outline`, `view_code_item` |
| Write/edit files | `write_to_file`, `replace_file_content`, `multi_replace_file_content` |
| Search codebase | `grep_search`, `find_by_name` |
| Run commands | `run_command`, `command_status`, `send_command_input` |
| Git operations | Full — via `run_command` (pull, commit, push, branch, etc.) |
| Browse the web | `browser_subagent`, `read_url_content` |
| Generate images | `generate_image` — UI mockups, assets, diagrams |
| Task management | `task_boundary`, `notify_user` — structured agentic workflows |
| Run tests | Direct — via `run_command` |
| Run dev servers | Direct — via `run_command` |

## Key Differences from Claude Code and Codex

| Feature | Claude Code | Codex | Antigravity |
|---------|------------|-------|-------------|
| Instruction file | `CLAUDE.md` | `AGENTS.md` | `system-instructions.md` |
| Tool style | Native (Read, Write, Edit) | Bash (cat, rg, find) | Mixed (native tools + bash) |
| Browser | Built-in WebFetch | Cached / `--search` | `browser_subagent` + `read_url_content` |
| Image generation | Not available | Not available | `generate_image` ✅ |
| Task UI | Not available | Not available | `task_boundary` + `notify_user` ✅ |
| Primary role | Building | Co-building | Strategy + Building |

## Unique Strengths

Antigravity has capabilities the other Big 3 members don't:
- **Image generation** — create UI mockups, design assets, and visual prototypes
- **Browser automation** — launch a browser, interact with web apps, take screenshots
- **Structured task management** — track progress with task boundaries and notify the user
- **Web reading** — fetch and parse any URL content directly

## Usage

Start a session in Antigravity. Daniel will automatically load from `system-instructions.md`, read all memory files, and greet you ready to build.

Use slash commands: `/scaffold`, `/debug`, `/review`, `/ship`, `/sync`, `/assign`, `/architect`, etc.
