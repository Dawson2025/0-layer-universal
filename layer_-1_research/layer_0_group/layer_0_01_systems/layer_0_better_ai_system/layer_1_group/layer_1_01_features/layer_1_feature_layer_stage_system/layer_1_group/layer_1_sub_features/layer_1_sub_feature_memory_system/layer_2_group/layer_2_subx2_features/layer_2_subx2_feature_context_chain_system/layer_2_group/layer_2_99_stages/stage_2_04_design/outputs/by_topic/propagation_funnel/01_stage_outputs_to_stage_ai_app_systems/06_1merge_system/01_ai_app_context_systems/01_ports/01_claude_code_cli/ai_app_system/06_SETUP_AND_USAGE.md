# Claude Code CLI — Setup and Usage Guide

**Date**: 2026-02-28
**Focus**: How to set up and use Claude Code CLI with the complete configuration system

---

## Quick Start (5 Minutes)

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

## Complete Setup (Full Configuration)

### Step 1: Install Claude Code CLI

```bash
# Install via Homebrew (macOS)
brew install anthropic/claude/claude-code-cli

# Or via pip
pip install claude-code

# Or download from https://claude.com/download
```

### Step 2: Create Global Configuration Directory

```bash
mkdir -p ~/.claude/{projects,skills,rules}
```

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

## How the System Works Together

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

## Common Workflows

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

## Troubleshooting

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

### Issue: Running Out of Tokens

**Cause**: Too much context loaded, or conversation is very long

**Fix**:
1. Trim CLAUDE.md (keep essential rules only)
2. Use `/context` to see what's taking space
3. Use subagents for parallel work
4. Archive old history.jsonl

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

## Best Practices for Setup

### 1. Keep Global CLAUDE.md Under 300 Lines

Global rules apply to **every project**. Don't make it bloated.

### 2. Put Project-Specific Content in Project CLAUDE.md

Not in global CLAUDE.md. Use cascade to override globally.

### 3. First 200 Lines of MEMORY.md Are Critical

These are auto-loaded every session. Make them count:
- Current status (one sentence)
- Quick navigation (file paths, key concepts)
- Essential facts you use in every session

### 4. Document Everything in Markdown

CLAUDE.md and MEMORY.md are human-readable. Make them searchable and clear.

### 5. Update MEMORY.md and status.json Regularly

After significant work, update both to reflect progress.

### 6. Use @file and @folder Strategically

Load files on-demand, not all at once. Keeps token count low.

### 7. Enable MCP Servers Only When Needed

Don't enable Canvas, GitHub, etc. unless you're using them. Extra context = fewer tokens for responses.

---

## Advanced: MCP Server Integration

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

## Summary: Complete Claude Code CLI System

✅ **Global Config** (`~/.claude/CLAUDE.md`, `settings.json`, `keybindings.json`)
✅ **Project Config** (`~/.claude/projects/[HASH]/CLAUDE.md`)
✅ **Directory Chain** (`[DIR]/CLAUDE.md` cascades up to git root)
✅ **Project Memory** (`~/.claude/projects/[HASH]/memory/MEMORY.md`)
✅ **Conversation History** (`~/.claude/projects/[HASH]/history.jsonl`)
✅ **MCP Servers** (External tools integration)

All pieces work together to create a powerful, flexible context system.
