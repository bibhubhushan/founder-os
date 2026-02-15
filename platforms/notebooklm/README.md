# Daniel for NotebookLM

## What This Is

Daniel persona adapted for Google NotebookLM. This is the compressed variant — NotebookLM has a 10,000 character limit for instructions, so Daniel's personality is condensed while keeping the core identity intact. Full coding standards are attached as a separate source document.

## Setup

1. Go to [notebooklm.google.com](https://notebooklm.google.com)
2. Create a new notebook
3. Click the notebook settings (gear icon or "Customize" option)
4. Paste the contents of `notebook-instructions.md` into the instructions field
5. Add sources:
   - Upload `standards-attachment.md` as a source (or paste into a Google Doc and add it)
   - (Optional) Create a Google Doc called "Daniel Memory" and add it as a source — this serves as persistent memory between sessions

## Character Count

Current: ~4,400 / 10,000 characters. There's room to expand if needed.

## Memory Management

NotebookLM doesn't have persistent memory across sessions. Daniel uses an attached Google Doc:

1. Create a Google Doc called "Daniel Memory"
2. Add it as a source to the notebook
3. At the end of each session, Daniel outputs a "Session Update" block
4. Copy that block and paste it into the Daniel Memory doc
5. Next session, Daniel reads the updated memory doc and picks up where you left off

## Best For

- Studying codebases (attach code files as sources)
- Learning from documentation, tutorials, and videos (attach as sources)
- Code review with full context (attach relevant files)
- Architecture discussions grounded in reference material
- Research and synthesis from multiple sources

## Limitations

- 10,000 character limit on instructions (currently well under)
- Cannot run code or access your file system
- Cannot browse the web
- Memory requires manual updates to the Google Doc
- All code must be copy-pasted by you into your editor
