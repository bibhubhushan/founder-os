# Knowledge Base

Long-term knowledge that persists across projects. Unlike `memory/` (which tracks current project state), this is permanent learning.

## Structure

```
knowledge/
├── tools/       ← Tools, frameworks, libraries we've evaluated
├── papers/      ← AI research papers and key takeaways
├── patterns/    ← Code patterns, architecture patterns, solutions we've used
└── README.md    ← You are here
```

## How It Works

- Any Daniel or Aria can add to the knowledge base
- Entries have dates and sources
- Aria reviews and organizes periodically
- This is the team's long-term brain — survives across projects

## File Format

Each file in a subfolder:

```markdown
# [Topic Name]
**Added:** YYYY-MM-DD
**Source:** [where this came from]
**Added by:** [which agent]

## What It Is
[Brief explanation]

## Why It Matters
[Why we care]

## Key Takeaways
- [Point 1]
- [Point 2]

## How to Use It
[Practical application]
```
