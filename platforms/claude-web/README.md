# Daniel for Claude Web (Projects)

## What This Is

Daniel persona adapted for Claude's web app using the Projects feature. Claude Web has built-in project memory (auto-synthesized every 24 hours) and web access, but no file system or bash.

## Setup

1. Go to [claude.ai](https://claude.ai)
2. Click **Projects** in the sidebar
3. Create a new project (e.g., "Daniel - [Project Name]")
4. Click the project settings (gear icon)
5. Paste the contents of `project-instructions.md` into the **Custom Instructions** field
6. (Optional) Upload `standards/rules.md` as a **Project Knowledge** document for full coding standards

## How Memory Works

Claude Web Projects has built-in memory:
- It automatically synthesizes key facts from your conversations every 24 hours
- Daniel will explicitly state important decisions so the auto-synthesis captures them
- At the end of each session, Daniel provides a summary for the memory system to absorb
- No manual state management needed

## Best For

- Research-heavy building (web access for docs, APIs, tutorials)
- Architecture planning and system design
- Code review (paste code into chat)
- Debugging (paste errors and relevant code)
- Prototyping and code generation
- Learning new technologies with Daniel's teaching philosophy

## Limitations

- Cannot run code or access your file system
- Cannot make git commits or run tests directly
- All code must be copy-pasted by you into your editor
- Daniel will provide exact commands for you to run locally
