# Complete Guide to Claude Skills: Structure, Activation & Workflow

## 📁 FOLDER STRUCTURE

### Basic Structure (Minimum Required)
```
my-skill/
└── SKILL.md          ← Required: Contains name, description, instructions
```

### Advanced Structure (With Resources)
```
my-skill/
├── SKILL.md              ← Main skill file (REQUIRED)
├── reference-docs/       ← Additional documentation
│   ├── SYSTEM_DESIGN.md
│   ├── MODERN_STACKS.md
│   └── MOBILE_DEVELOPMENT.md
├── scripts/              ← Executable code
│   ├── build.py
│   └── validate.js
├── resources/            ← Assets, templates, images
│   ├── logo.png
│   ├── template.docx
│   └── config.json
└── examples/             ← Example inputs/outputs
    ├── input-example.md
    └── output-example.md
```

### Your Programming Expert Structure
```
ultimate-programming-expert/
├── SKILL.md                           ← 38KB main skill file
└── reference-docs/
    ├── SYSTEM_DESIGN.md               ← 21KB architecture patterns
    ├── MODERN_STACKS.md               ← 32KB production code templates
    └── MOBILE_DEVELOPMENT.md          ← 37KB iOS/Android/RN/Flutter
```

---

## 📝 SKILL.md FILE FORMAT

```yaml
---
name: Ultimate Full-Stack Engineering Expert
description: World-class expertise for building Instagram/Reddit/Snapchat/Spotify scale applications with production-ready architecture
---

# Main Instructions

Your detailed instructions go here...

## Section 1
Content...

## Section 2
Content...
```

### Required Fields:
| Field | Max Length | Purpose |
|-------|-----------|---------|
| `name` | 64 chars | Human-friendly skill name |
| `description` | 200 chars | **CRITICAL** - Claude uses this to decide when to load your skill |

### Optional Fields:
| Field | Example | Purpose |
|-------|---------|---------|
| `dependencies` | `python>=3.8, pandas>=1.5.0` | Required packages |

---

## 🎯 WHERE TO ADD SKILLS (3 Methods)

### Method 1: Claude.ai (Web/Desktop/Mobile)

**Requirements:** Pro, Max, Team, or Enterprise plan + Code Execution enabled

**Steps:**
1. Go to **Settings** → **Capabilities**
2. Make sure **Code Execution** is ON
3. Scroll to **Skills** section
4. Click **"Upload Skill"**
5. Select your `.zip` file
6. Toggle the skill ON to activate

**Location in UI:**
```
Claude.ai → Settings (⚙️) → Capabilities → Skills → Upload Skill
```

### Method 2: Claude Code (Terminal/IDE)

**For Personal Skills:**
```bash
# Create in your home directory
mkdir -p ~/.claude/skills/ultimate-programming-expert
cp -r your-skill/* ~/.claude/skills/ultimate-programming-expert/
```

**For Project-Specific Skills:**
```bash
# Create in project root
mkdir -p ./skills/ultimate-programming-expert
cp -r your-skill/* ./skills/ultimate-programming-expert/
```

**Directory Structure:**
```
~/.claude/
└── skills/
    └── ultimate-programming-expert/
        ├── SKILL.md
        └── reference-docs/
            ├── SYSTEM_DESIGN.md
            ├── MODERN_STACKS.md
            └── MOBILE_DEVELOPMENT.md
```

### Method 3: Claude API

```bash
# Upload via API
curl -X POST "https://api.anthropic.com/v1/skills" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "display_title=Ultimate Programming Expert" \
  -F "files[]=@ultimate-programming-expert/SKILL.md;filename=ultimate-programming-expert/SKILL.md" \
  -F "files[]=@ultimate-programming-expert/reference-docs/SYSTEM_DESIGN.md;filename=ultimate-programming-expert/reference-docs/SYSTEM_DESIGN.md"
```

---

## 📦 HOW TO CREATE THE ZIP FILE

### Correct Structure ✅
```
ultimate-programming-expert.zip
└── ultimate-programming-expert/      ← Folder as root
    ├── SKILL.md
    └── reference-docs/
        ├── SYSTEM_DESIGN.md
        ├── MODERN_STACKS.md
        └── MOBILE_DEVELOPMENT.md
```

### Incorrect Structure ❌
```
ultimate-programming-expert.zip
├── SKILL.md                          ← Files directly in root (WRONG!)
└── reference-docs/
```

### Commands to Create ZIP:

**macOS/Linux:**
```bash
cd /path/to/parent/directory
zip -r ultimate-programming-expert.zip ultimate-programming-expert/
```

**Windows (PowerShell):**
```powershell
Compress-Archive -Path "ultimate-programming-expert" -DestinationPath "ultimate-programming-expert.zip"
```

**Windows (File Explorer):**
1. Right-click the `ultimate-programming-expert` folder
2. Send to → Compressed (zipped) folder

---

## ⚡ HOW ACTIVATION WORKS (Progressive Disclosure)

Claude uses a smart 3-tier loading system:

```
┌─────────────────────────────────────────────────────────────┐
│  TIER 1: Always in Memory (Lightweight)                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ name: "Ultimate Full-Stack Engineering Expert"       │   │
│  │ description: "World-class expertise for building..." │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                  │
│            User asks about building an app                  │
│                          ↓                                  │
├─────────────────────────────────────────────────────────────┤
│  TIER 2: Loaded on Match                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Full SKILL.md content                                │   │
│  │ - Core instructions                                  │   │
│  │ - Guidelines                                         │   │
│  │ - Examples                                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                  │
│       User asks about specific topic (e.g., database)       │
│                          ↓                                  │
├─────────────────────────────────────────────────────────────┤
│  TIER 3: Loaded on Demand                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Reference files:                                     │   │
│  │ - SYSTEM_DESIGN.md (when architecture needed)        │   │
│  │ - MODERN_STACKS.md (when code templates needed)      │   │
│  │ - MOBILE_DEVELOPMENT.md (when mobile dev needed)     │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Why This Matters:
- **Saves tokens** - Only loads what's needed
- **Faster responses** - Less context to process
- **Smarter matching** - Description determines when to activate

---

## 🔄 COMPLETE WORKFLOW

### Step-by-Step Process:

```
┌──────────────────────────────────────────────────────────────┐
│  1. CREATE SKILL FILES                                       │
│     ├── Write SKILL.md with name + description + instructions│
│     └── Add reference files if needed                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│  2. ORGANIZE FOLDER                                          │
│     ├── Folder name = skill name                             │
│     ├── SKILL.md at root                                     │
│     └── Reference docs in subfolders                         │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│  3. CREATE ZIP (for Claude.ai)                               │
│     └── zip -r skill-name.zip skill-name/                    │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│  4. UPLOAD TO CLAUDE                                         │
│     ├── Claude.ai: Settings → Capabilities → Upload Skill    │
│     ├── Claude Code: Copy to ~/.claude/skills/               │
│     └── API: POST to /v1/skills endpoint                     │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│  5. ENABLE SKILL                                             │
│     └── Toggle ON in Skills list                             │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│  6. TEST & USE                                               │
│     ├── Ask Claude questions matching skill description      │
│     ├── Check Claude's thinking to verify skill loaded       │
│     └── Iterate on description if not triggering correctly   │
└──────────────────────────────────────────────────────────────┘
```

---

## 🧪 TESTING YOUR SKILL

### Before Upload Checklist:
- [ ] SKILL.md has valid YAML frontmatter (--- at start and end)
- [ ] Name is under 64 characters
- [ ] Description is under 200 characters and clearly states when to use
- [ ] Folder name matches skill name
- [ ] All referenced files exist
- [ ] ZIP contains folder (not loose files)

### Test Prompts for Programming Expert:
```
✅ "Build me an Instagram-like app architecture"
✅ "How would you design a Reddit voting system?"
✅ "Create a Spotify-style audio streaming backend"
✅ "Design a scalable real-time chat system"
✅ "Set up a React Native app with authentication"
```

### Verify Skill is Loading:
In Claude.ai, you can see skills in Claude's chain of thought:
```
[Thinking] I see the user wants to build an app. Let me check my skills...
[Loading Skill] ultimate-full-stack-engineering-expert
[Reading] SKILL.md - Core instructions loaded
[Reading] reference-docs/MODERN_STACKS.md - Need production templates
```

---

## 🚀 QUICK START: Add Your Programming Expert Skill

### For Claude.ai:

```bash
# 1. Download the skill files I created
# 2. Create the ZIP structure
cd /path/to/downloads
mkdir ultimate-programming-expert
# Move SKILL.md and reference-docs folder here

# 3. Create ZIP
zip -r ultimate-programming-expert.zip ultimate-programming-expert/

# 4. Upload to Claude.ai
# Go to: Settings → Capabilities → Skills → Upload Skill
# Select: ultimate-programming-expert.zip

# 5. Enable the skill (toggle ON)

# 6. Test it!
# Ask: "Design me an Instagram-scale photo sharing app"
```

### For Claude Code:

```bash
# 1. Create skills directory
mkdir -p ~/.claude/skills/

# 2. Copy your skill
cp -r ultimate-programming-expert ~/.claude/skills/

# 3. Verify structure
ls -la ~/.claude/skills/ultimate-programming-expert/
# Should show:
# SKILL.md
# reference-docs/

# 4. Start Claude Code - skill loads automatically!
claude

# 5. Test it
> Build me a Reddit-style voting system with anti-manipulation
```

---

## 📊 COMPARISON: Skills vs Other Features

| Feature | Purpose | When to Use |
|---------|---------|-------------|
| **Skills** | Reusable expertise/workflows | Complex, repeatable tasks |
| **Projects** | Context for specific work | Single project context |
| **Custom Instructions** | Personal preferences | Tone, style, format |
| **MCP** | External data connections | Real-time data access |
| **Artifacts** | Visual outputs | Code, diagrams, documents |

---

## 🎓 BEST PRACTICES

1. **One Skill = One Domain** - Don't mix web dev + cooking recipes
2. **Clear Description** - This is how Claude decides to load your skill
3. **Include Examples** - Shows Claude what success looks like
4. **Start Simple** - Add complexity later
5. **Test Incrementally** - Verify each change works
6. **Use Reference Files** - Keep SKILL.md focused, details in subfiles

---

## ❓ TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Skill not triggering | Make description more specific |
| YAML error on upload | Check `---` markers, use spaces not tabs |
| Claude ignores instructions | Add examples, make rules clearer |
| Too slow to respond | Move large content to reference files |
| ZIP won't upload | Ensure folder is root, not loose files |

---

## 🔗 RESOURCES

- **Official Docs:** https://docs.claude.com/en/docs/claude-code/skills
- **Skills GitHub:** https://github.com/anthropics/skills
- **Agent Skills Standard:** https://agentskills.io
- **Help Center:** https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
