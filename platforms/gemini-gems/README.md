# Daniel for Gemini Gems

## What This Is

Daniel persona adapted for Google Gemini's Gems feature. Gems support custom instructions plus attached documents, making them great for document-heavy work and learning.

## Setup

1. Go to [gemini.google.com](https://gemini.google.com)
2. Click **Gem Manager** in the sidebar
3. Click **Create Gem**
4. Name it **Daniel**
5. Paste the contents of `gem-instructions.md` into the **Instructions** field
6. Attach the following documents:
   - `standards-attachment.md` (upload as a file or paste into a Google Doc and attach)
   - (Optional) Create a Google Doc called "Daniel Memory" and attach it — this serves as persistent memory between sessions

## Memory Management

Since Gems don't have persistent memory across sessions, we use an attached Google Doc:

1. Create a Google Doc called "Daniel Memory"
2. Attach it to the Gem
3. At the end of each session, Daniel will output a "Session Update" block
4. Copy that block and paste it into the Daniel Memory doc
5. Next session, Daniel reads the memory doc and picks up where you left off

## Best For

- Learning from attached resources (YouTube videos, articles, docs)
- Code review with attached code files
- Architecture planning with reference documents
- Building with context from attached specs or designs
- Shareable — can share the Gem with team members

## Limitations

- Cannot run code or access your file system
- Cannot browse the web (only reads attached URLs)
- Memory requires manual updates to the Google Doc
- All code must be copy-pasted by you into your editor
