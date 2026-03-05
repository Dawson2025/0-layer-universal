---
resource_id: "d7d7cc17-2cf3-48d8-b1a5-7b2228a14333"
resource_type: "output"
resource_name: "06_SETUP_AND_USAGE"
---
# Claude Code CLI — Setup and Usage Guide

**Date**: 2026-02-28
**Focus**: How to set up and use Claude Code CLI with the complete configuration system

---

<!-- section_id: "9ddf2eb9-040b-457c-a51c-a5b7dd119307" -->
## Quick Start (5 Minutes)

<!-- section_id: "cb6ac83d-8789-47ba-9a2a-1babf7538e77" -->
### 1. Create Global Configuration

```bash
# Create ~/.claude directory
mkdir -p ~/.claude/projects

# Create global CLAUDE.md (universal rules)
cat > ~/.claude/CLAUDE.md << 'EOF'
# Claude Code Global Configuration

## [CRITICAL] Rules
1. Always report file changes with absolute paths
2. Never modify hidden files without permission
3. Always read CLAUDE.md files in the path from root to working directory

## Triggers
| Situation | Action |
|-----------|--------|
| Session starts | Load CLAUDE.md cascade from global → project → directory |
| User mentions a file | Use @file to load it on-demand |
| Need to check context | Use /context command |

## Current Status
Global configuration loaded. Ready for projects.
EOF
```

<!-- section_id: "b5b5e8e7-5056-40ff-8020-84c98948b6b3" -->
### 2. Initialize Your First Project

```bash
# Navigate to your project
cd /path/to/your/project

# Claude Code auto-detects working directory
claude /context  # Shows what's loaded

# Create project-specific CLAUDE.md (optional)
cat > ~/.claude/projects/[HASH]/CLAUDE.md << 'EOF'
# [Project Name] — Claude Code Configuration

## Project Context
- Role: [Your role in this project]
- Scope: [What you're working on]
- Current Status: Active development

## Skills
[List project-specific skills]

## Resources
[List project-specific resources]
EOF
```

<!-- section_id: "27ffab6a-a88b-48b5-87fe-94ad0bcb9c72" -->
### 3. Create MEMORY.md

```bash
# Create project memory (first 200 lines are auto-loaded)
cat > ~/.claude/projects/[HASH]/memory/MEMORY.md << 'EOF'
# Project Memory

## Quick Reference
- [Key fact 1]
- [Key fact 2]
- [Key fact 3]

## Navigation
- Codebase at: /path/to/code
- Tests at: /path/to/tests
- Docs at: /path/to/docs

---
[BOUNDARY: 200 lines]
---

## Detailed Topics

### Topic 1: Architecture
[Detailed architectural info]

### Topic 2: Testing
[Testing patterns and gotchas]
EOF
```

<!-- section_id: "a5b3c91a-0941-4bde-9a5e-b5b3ff691d61" -->
### 4. Start Using Claude Code

```bash
# Begin a conversation
claude

# Inside the conversation, you can:
/context              # See context breakdown
/memory               # View project memory
@path/to/file        # Load a file
/skill-name          # Invoke a skill
/remember: Note      # Save to MEMORY.md
```

---

<!-- section_id: "bc8799a3-34de-41bc-92b2-49796565a9e1" -->
## Complete Setup (Full Configuration)

<!-- section_id: "c47c29ea-b60a-4e11-8b0a-6603b1729074" -->
### Step 1: Install Claude Code CLI

```bash
# Install via Homebrew (macOS)
brew install anthropic/claude/claude-code-cli

# Or via pip
pip install claude-code

# Or download from https://claude.com/download
```

<!-- section_id: "315cd55e-5c77-4678-9ce9-32291003ac0d" -->
### Step 2: Create Global Configuration Directory

```bash
mkdir -p ~/.claude/{projects,skills,rules}
```

<!-- section_id: "b4ffc453-55e7-47e5-a5c2-964712855818" -->
### Step 3: Set Up Global CLAUDE.md

Create `~/.claude/CLAUDE.md` with universal rules:

```markdown
# Claude Code Global Configuration

## [CRITICAL] Rules
1. File Change Reporting: Report all changes with absolute paths
2. Context Traversal: Read CLAUDE.md files from root to current directory
3. Memory Management: First 200 lines of MEMORY.md are auto-loaded

## Triggers
| Situation | Action |
|-----------|--------|
| Session starts | Load CLAUDE.md cascade |
| User says /context | Display token usage breakdown |
| User says /memory | Show project MEMORY.md with file selector |

## Resources
| Resource | Location |
|----------|----------|
| Global rules | ~/.claude/rules/ |
| Project-specific | ~/.claude/projects/[HASH]/CLAUDE.md |
| Directory-chain | [DIR]/CLAUDE.md (walks up to git root) |

## Current Status
Global configuration ready. Projects can inherit these rules.
```

<!-- section_id: "daf1709d-2465-47e9-8497-758d093505d9" -->
### Step 4: Configure settings.json

Create `~/.claude/settings.json`:

```json
{
  "version": "1.0",
  "context_window": "200k",
  "default_model": "claude-opus-4-6",
  "auto_memory_enabled": true,
  "memory_lines_loaded": 200,
  "compaction_threshold": 0.9,
  "history_format": "jsonl",
  "mcp_servers": [
    {
      "name": "canvas",
      "type": "python",
      "command": "python -m mcp_servers.canvas",
      "env": {
        "CANVAS_API_KEY": "${env:CANVAS_API_KEY}"
      },
      "enabled": false
    }
  ]
}
```

<!-- section_id: "2e9a5325-3b3d-4b90-b4a9-0cb3dbf8bc89" -->
### Step 5: Configure keybindings.json

Create `~/.claude/keybindings.json`:

```json
{
  "keybindings": [
    {
      "key": "enter",
      "command": "submit-message",
      "when": "terminal_focused"
    },
    {
      "key": "shift+enter",
      "command": "new-line",
      "when": "terminal_focused"
    },
    {
      "key": "ctrl+shift+c",
      "command": "show-context",
      "when": "terminal_focused"
    },
    {
      "key": "ctrl+shift+m",
      "command": "show-memory",
      "when": "terminal_focused"
    }
  ]
}
```

<!-- section_id: "9e886d56-31ce-45bf-a496-bd0d41bcf12a" -->
### Step 6: Start Your First Project

```bash
cd /path/to/your/project

# Claude Code auto-creates project directory
# Check what's loaded
claude /context

# Create project CLAUDE.md (optional but recommended)
mkdir -p ~/.claude/projects/[PROJECT_HASH]
cat > ~/.claude/projects/[PROJECT_HASH]/CLAUDE.md << 'EOF'
# [Project Name] Context

## Identity
- Role: [Your role]
- Scope: [What you're doing]
- Parent: ~/.claude/CLAUDE.md (global)

## Current Status
[Brief status summary]

## Skills
[List of available skills]
EOF

# Create project memory
mkdir -p ~/.claude/projects/[PROJECT_HASH]/memory
cat > ~/.claude/projects/[PROJECT_HASH]/memory/MEMORY.md << 'EOF'
# [Project Name] Memory

## Current Status
[One-line summary]

## Quick Reference
- Key file 1
- Key file 2
- Key file 3

---
[200 lines boundary]
---

## Topics
[Detailed info]
EOF

# Start working!
claude
```

---

<!-- section_id: "7e81bbef-d367-47bd-91a8-93dfef54bb99" -->
## How the System Works Together

<!-- section_id: "7237cf1a-ed93-4709-9f9f-d01b42ec8cfa" -->
### Session Flow

```
1. User types: claude
   ↓
2. Claude Code hashes working directory
   ↓
3. Claude Code discovers and loads CLAUDE.md cascade:
   ~/.claude/CLAUDE.md (global)
   + ~/.claude/projects/[HASH]/CLAUDE.md (project)
   + [CURRENT_DIR]/CLAUDE.md (if in layered project)
   + [PARENT_DIR]/CLAUDE.md (if in layered project)
   ...continues up to git root or home
   ↓
4. Claude Code loads first 200 lines of:
   ~/.claude/projects/[HASH]/memory/MEMORY.md
   ↓
5. Claude Code loads settings:
   context_window, default_model, MCP servers, keybindings
   ↓
6. Context window is ready (~10K tokens)
   ↓
7. User starts conversation with ~190K tokens available
```

<!-- section_id: "6ebca686-651f-4000-9d31-75d331ee891b" -->
### File Discovery Order (CLAUDE.md)

```
Search Order (top = highest priority):
1. ~/.claude/CLAUDE.md (global)
2. ~/.claude/projects/[HASH]/CLAUDE.md (project)
3. [CURRENT_DIR]/CLAUDE.md (current directory)
4. [PARENT_DIR]/CLAUDE.md (parent directory)
5. [GRANDPARENT_DIR]/CLAUDE.md (grandparent)
...
6. [GIT_ROOT]/CLAUDE.md (git repo root)
7. ~ (home directory, if reached)

Files are MERGED (later = higher priority)
Result: Single merged context loaded
```

<!-- section_id: "e6b420f6-aa78-4f74-aee8-94d09b152885" -->
### Configuration Hierarchy

```
Defaults (built-in)
  ↓ overridden by
~/.claude/settings.json (global)
  ↓ overridden by
Project settings (if any)
  ↓ overridden by
CLI flags (command-line arguments)

Result: Effective settings for session
```

---

<!-- section_id: "31e4df03-57af-4396-837c-28ad6eada446" -->
## Common Workflows

<!-- section_id: "b61f3df2-eb5e-4f85-9227-2afdd44d2a1a" -->
### Workflow 1: Single Project (No Layers)

```
Project: ~/my-project/
├── CLAUDE.md          (optional: project-specific)
└── code/
    └── ...

Configuration:
- Use ~/.claude/CLAUDE.md (global rules)
- Optionally create ~/my-project/CLAUDE.md (project rules)
- Create ~/.claude/projects/[HASH]/memory/MEMORY.md (project memory)
```

<!-- section_id: "e7826c66-198e-4c12-aaa2-aebac8ac75d5" -->
### Workflow 2: Layered Project (With Layers)

```
Project: ~/layer-stage-system/
├── CLAUDE.md          (layer 0: universal rules)
├── layer_1/
│   ├── CLAUDE.md      (layer 1: project rules)
│   └── layer_1_projects/
│       ├── CLAUDE.md  (layer 1 projects: group rules)
│       └── layer_1_project_school/
│           ├── CLAUDE.md (layer 1 project: specific rules)
│           └── layer_1/
│               ├── CLAUDE.md (layer 2: sub-project rules)
│               └── ...

Configuration:
- ~/.claude/CLAUDE.md (global)
- ~/.claude/projects/[HASH]/CLAUDE.md (project root rules)
- CLAUDE.md cascade walks up: current → parent → grandparent → git root
- MEMORY.md (project-level, not per-layer)
```

<!-- section_id: "3490e5cf-4647-4bb1-a0bb-379c782deb45" -->
### Workflow 3: Multi-Project Workspace

```
Workspace: ~/workspace/
├── project-a/        (Hash: abc123)
├── project-b/        (Hash: def456)
└── project-c/        (Hash: ghi789)

Configuration:
- ~/.claude/CLAUDE.md (shared across all projects)
- ~/.claude/projects/abc123/CLAUDE.md (project-a specific)
- ~/.claude/projects/def456/CLAUDE.md (project-b specific)
- ~/.claude/projects/ghi789/CLAUDE.md (project-c specific)
- Each project has separate MEMORY.md and history.jsonl
```

---

<!-- section_id: "be2b2588-d40b-45dc-812a-2df95123a9f6" -->
## Troubleshooting

<!-- section_id: "266208b7-8b66-425d-9484-50b30ff1a75c" -->
### Issue: Claude Seems to Not Know About Project Rules

**Cause**: Project CLAUDE.md not created or in wrong location

**Fix**:
```bash
# Check project hash
cd /path/to/project
ls ~/.claude/projects/

# Create project CLAUDE.md
mkdir -p ~/.claude/projects/[HASH]
cat > ~/.claude/projects/[HASH]/CLAUDE.md << 'EOF'
# [Project] Context
...
EOF

# Verify it loads
claude /context  # Should show your project CLAUDE.md
```

<!-- section_id: "4b18b4ef-074e-4561-9c14-f6c2562ac69f" -->
### Issue: Running Out of Tokens

**Cause**: Too much context loaded, or conversation is very long

**Fix**:
1. Trim CLAUDE.md (keep essential rules only)
2. Use `/context` to see what's taking space
3. Use subagents for parallel work
4. Archive old history.jsonl

<!-- section_id: "5f2d62e5-21f9-46a2-ae5e-f4c722196c18" -->
### Issue: MEMORY.md Not Loading

**Cause**: File not at correct path, or >200 lines not formatted correctly

**Fix**:
```bash
# Check path
ls ~/.claude/projects/[HASH]/memory/MEMORY.md

# Check first 200 lines
head -200 ~/.claude/projects/[HASH]/memory/MEMORY.md

# Verify boundary marker
grep "^---" ~/.claude/projects/[HASH]/memory/MEMORY.md | head -1
```

<!-- section_id: "5ca5e8e9-d398-4f00-af38-1ae93a07cf03" -->
### Issue: Keybindings Not Working

**Cause**: keybindings.json syntax error or not loaded

**Fix**:
```bash
# Validate JSON
python -m json.tool ~/.claude/keybindings.json

# Check it's loaded
claude /context  # Should show keybindings section
```

---

<!-- section_id: "bc94d6d5-e68a-480b-b4c0-1b2c844b5038" -->
## Best Practices for Setup

<!-- section_id: "54434e02-8ec9-42be-aeef-7d20515313af" -->
### 1. Keep Global CLAUDE.md Under 300 Lines

Global rules apply to **every project**. Don't make it bloated.

<!-- section_id: "fde43d7b-bcdf-469c-86df-70bad866c35f" -->
### 2. Put Project-Specific Content in Project CLAUDE.md

Not in global CLAUDE.md. Use cascade to override globally.

<!-- section_id: "87cc2a59-8f4f-4bd0-9cca-c5da4a6278b2" -->
### 3. First 200 Lines of MEMORY.md Are Critical

These are auto-loaded every session. Make them count:
- Current status (one sentence)
- Quick navigation (file paths, key concepts)
- Essential facts you use in every session

<!-- section_id: "1ca30094-a68a-4b8c-aa15-ad79d0f9c820" -->
### 4. Document Everything in Markdown

CLAUDE.md and MEMORY.md are human-readable. Make them searchable and clear.

<!-- section_id: "57b2d345-4f3b-4792-b84d-384d0e1141c5" -->
### 5. Update MEMORY.md and status.json Regularly

After significant work, update both to reflect progress.

<!-- section_id: "a57ea623-8db4-425b-ba88-466af45c6b09" -->
### 6. Use @file and @folder Strategically

Load files on-demand, not all at once. Keeps token count low.

<!-- section_id: "c12e0462-b997-466d-8d48-4b8b0a737c1e" -->
### 7. Enable MCP Servers Only When Needed

Don't enable Canvas, GitHub, etc. unless you're using them. Extra context = fewer tokens for responses.

---

<!-- section_id: "40761b7e-d67d-4443-8bdf-cbbc4674a996" -->
## Advanced: MCP Server Integration

<!-- section_id: "ddc2acb6-2d92-476e-99c8-069585d540ca" -->
### Add Canvas MCP Server

```json
{
  "name": "canvas",
  "type": "python",
  "command": "python -m mcp_servers.canvas",
  "env": {
    "CANVAS_API_KEY": "${env:CANVAS_API_KEY}",
    "CANVAS_DOMAIN": "canvas.instructure.com"
  },
  "enabled": true
}
```

Set environment variable:
```bash
export CANVAS_API_KEY="your-api-key-here"
```

<!-- section_id: "c5df98f6-01a1-4d61-9499-d9dc176166d5" -->
### Add GitHub MCP Server

```json
{
  "name": "github",
  "type": "node",
  "command": "npx @github/mcp-server-github",
  "env": {
    "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
  },
  "enabled": true
}
```

Set environment variable:
```bash
export GITHUB_TOKEN="your-github-token-here"
```

---

<!-- section_id: "380fb5ce-f9a6-4dae-857e-af8ff51bb0b4" -->
## Summary: Complete Claude Code CLI System

✅ **Global Config** (`~/.claude/CLAUDE.md`, `settings.json`, `keybindings.json`)
✅ **Project Config** (`~/.claude/projects/[HASH]/CLAUDE.md`)
✅ **Directory Chain** (`[DIR]/CLAUDE.md` cascades up to git root)
✅ **Project Memory** (`~/.claude/projects/[HASH]/memory/MEMORY.md`)
✅ **Conversation History** (`~/.claude/projects/[HASH]/history.jsonl`)
✅ **MCP Servers** (External tools integration)

All pieces work together to create a powerful, flexible context system.
