---
description: Archive current project and start a new one fresh
---

# New Project — Archive and Start Fresh

You are Daniel. Read `platforms/ai-studio/system-instructions.md` — you ARE him.

## Workflow

### 1. Archive Current Project
// turbo
- Read `memory/project.md` — is there an active project?
- If yes:
  - Create `memory/archive/[project-name].md` with full state using `write_to_file`
  - Move relevant decisions from `memory/decisions.md` to the archive
  - Keep `memory/preferences.md` (those are about Bibhu, not the project)
  - Keep `memory/mistakes.md` (lessons are universal)
  - Log to `memory/sessions.md`: "Archived [project-name]"

### 2. Reset for New Project
- Clear `memory/project.md` — write new project description using `write_to_file`
- Clear `memory/stack.md` — fresh tech decisions
- Clear `memory/decisions.md` — fresh architecture log
- Keep `memory/preferences.md` and `memory/mistakes.md` intact

### 3. Bootstrap
If the user gave enough detail, immediately route to the /scaffold workflow.
Otherwise, ask Bibhu one question to clarify, then scaffold.

### 4. Respond as Daniel
"Alright, [old project] is archived. Starting fresh with [new project]. Let's go."
