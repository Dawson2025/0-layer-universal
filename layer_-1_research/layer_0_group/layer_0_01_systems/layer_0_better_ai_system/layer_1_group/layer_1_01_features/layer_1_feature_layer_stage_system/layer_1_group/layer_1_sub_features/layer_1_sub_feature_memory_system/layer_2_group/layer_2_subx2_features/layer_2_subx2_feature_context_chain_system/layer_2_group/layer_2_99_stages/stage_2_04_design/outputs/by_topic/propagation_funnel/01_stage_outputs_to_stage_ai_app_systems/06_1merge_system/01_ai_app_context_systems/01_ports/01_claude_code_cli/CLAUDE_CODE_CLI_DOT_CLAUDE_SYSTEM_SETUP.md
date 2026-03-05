---
resource_id: "5521877f-d6a2-4eda-9fb1-4db95f282e3d"
resource_type: "output"
resource_name: "CLAUDE_CODE_CLI_DOT_CLAUDE_SYSTEM_SETUP"
---
# Claude Code CLI — .claude Directory System Setup

**Date Created**: 2026-02-27
**Status**: Verified via direct filesystem exploration
**Source**: Exploration of ~/.claude directory structure and file contents

---

## Overview

Claude Code CLI stores all its persistent configuration, state, and memory in the **~/.claude/** directory. This is the "home base" for all Claude Code sessions, independent of the project being worked on.

The `.claude` directory implements:
1. **Global configuration** (CLAUDE.md with universal rules)
2. **Per-project memory** (in `projects/` subdirectories)
3. **Skills system** (reusable workflows and instructions)
4. **Session/plan management** (tracking ongoing work)
5. **Team coordination** (multi-agent teams and task lists)
6. **Telemetry and state** (usage tracking, debug logs, history)

---

## Part 1: Directory Structure Overview

### Complete Directory Tree

```
~/.claude/
├── CLAUDE.md                      # Global config (universal rules)
├── settings.json                  # User preferences
├── settings.local.json            # Local overrides
├── .credentials.json              # API keys, auth tokens
├── history.jsonl                  # Session conversation history
├── stats-cache.json               # Usage/performance metrics
├──
├── projects/                      # Per-project memory & state
│   ├── -home-dawson/
│   │   ├── memory/
│   │   │   ├── MEMORY.md          # Auto-memory (200 lines in prompt, rest on-demand)
│   │   │   ├── mcp_api_usage.md   # MCP API call tracking
│   │   │   ├── episodic.md        # Session history aggregated
│   │   │   └── [topic-files].md   # Domain-specific knowledge
│   │   └── session-data/          # Current session state
│   └── [other-project-ids]/
│
├── skills/                        # Reusable skill definitions
│   ├── skill-creator/             # Meta-skill for creating skills
│   ├── [other-skill-names]/
│   └── [skill-folders]/SKILL.md   # Skill definitions
│
├── plans/                         # Plan mode documents
│   ├── [plan-name-1].md
│   ├── [plan-name-2].md
│   └── [generated-plan-ids]/
│
├── teams/                         # Multi-agent team management
│   ├── [team-name-1]/
│   │   ├── config.json            # Team members list
│   │   └── [member-files]
│   └── [team-name-2]/
│
├── tasks/                         # Task list management (per team)
│   ├── [team-name-1]/             # Tasks for this team
│   │   └── task-*.json            # Individual task files
│   └── [team-name-2]/
│
├── session-env/                   # Session state snapshots
│   ├── [project-id-1]/
│   │   ├── context.json           # Current context state
│   │   ├── variables.json         # Session variables
│   │   └── [tool-state]/
│   └── [project-id-2]/
│
├── file-history/                  # File change tracking
│   ├── [project-id-1]/
│   │   ├── [file-path-hash].json  # Tracked file changes
│   │   └── ...
│   └── [project-id-2]/
│
├── hooks/                         # Custom hooks directory
│   ├── [hook-name].sh             # Shell scripts
│   └── [hook-name].py             # Python scripts
│
├── cache/                         # Caching
│   ├── context-cache.json
│   ├── model-cache.json
│   └── api-response-cache/
│
├── debug/                         # Debug logs
│   ├── trace-*.log
│   ├── error-*.log
│   └── performance-*.log
│
├── chrome/                        # Chrome/Browser automation state
│   ├── profile/                   # Browser profile
│   └── cookies.json               # Session cookies
│
├── downloads/                     # Downloaded files
│   └── [downloaded-files]
│
├── paste-cache/                   # Clipboard caching
│   └── [cached-pastes].json
│
├── .git/                          # Internal version control
│   └── [git-metadata]
│
├── plugins/                       # External plugins
│   ├── plugin-*.json
│   └── [plugin-state]/
│
├── ide/                           # IDE integrations
│   ├── cursor-config.json
│   ├── vscode-settings.json
│   └── [other-ide-configs]
│
├── shell-snapshots/               # Shell state snapshots
│   └── [env-snapshots].json
│
├── todos/                         # Todo tracking
│   └── [todo-lists].json
│
├── telemetry/                     # Analytics data
│   ├── usage-*.json
│   └── events-*.log
│
├── statsig/                       # Feature flag service data
│   └── [statsig-cache].json
│
└── .git/                          # If .claude is version controlled
    └── [git-config]
```

---

## Part 2: Core Configuration Files

### ~/.claude/CLAUDE.md

**Purpose**: Global Claude Code configuration applied to **every session**, across all projects.

**Content**:
- Critical rules (filesystem change protocol, commit/push rules, context traversal)
- Layer-stage system overview
- Agnostic system explanation
- Entity creation guidelines
- Triggers table (when to load rules/skills)
- Skill locations and descriptions
- Resources (rule paths, knowledge bases, protocols)

**Key Property**: This file is **NOT auto-generated** — it's hand-edited and represents global policy.

**When Loaded**: At the start of every Claude Code session, before project-specific CLAUDE.md files.

### ~/.claude/settings.json

**Purpose**: User preferences for Claude Code behavior.

**Example**:
```json
{
  "default_model": "claude-opus",
  "max_context_tokens": 200000,
  "auto_memory_enabled": true,
  "auto_commit_enabled": false,
  "compaction_threshold": 0.9,
  "file_history_depth": 50,
  "telemetry_enabled": true,
  "theme": "dark"
}
```

### ~/.claude/.credentials.json

**Purpose**: Securely store API keys and authentication tokens.

**Contains** (encrypted):
- OpenAI API key
- Anthropic API key (for external Anthropic services)
- GitHub token (for repo operations)
- Custom API credentials
- Session tokens

**Security**: File is encrypted at rest, never displayed in logs.

### ~/.claude/history.jsonl

**Purpose**: Complete conversation history across all sessions (optional, for personal archival).

**Format**: JSONL (one JSON object per line, one per turn).

**Structure**:
```json
{
  "timestamp": "2024-02-27T10:30:00Z",
  "project": "my-project",
  "model": "claude-opus",
  "user_message": "What is this function?",
  "assistant_response": "This function...",
  "tokens_used": {
    "prompt": 250,
    "completion": 180,
    "total": 430
  },
  "tools_used": ["read", "grep"],
  "tags": ["code-review", "documentation"]
}
```

**Size**: Can grow very large (GBs for heavy usage). Useful for tracking patterns but not loaded into context.

### ~/.claude/stats-cache.json

**Purpose**: Usage statistics and performance metrics.

**Contains**:
- Total tokens used (by project, by time period)
- API calls count
- Session durations
- Tool usage frequency
- Error rates
- Model performance (latency, quality metrics)

**Used for**: Optimization decisions, cost tracking, finding bottlenecks.

---

## Part 3: Per-Project Memory System

### Directory: ~/.claude/projects/[project-id]/

**Purpose**: Memory and state specific to a single project.

**Project ID Format**: Hashed from working directory path. Example: `-home-dawson` (represents `/home/dawson`).

### Subdirectory: memory/

```
~/.claude/projects/[project-id]/memory/
├── MEMORY.md              # Entrypoint (first 200 lines auto-injected)
├── [topic-1].md          # Topic file 1 (loaded on-demand)
├── [topic-2].md          # Topic file 2 (loaded on-demand)
├── debugging.md          # Debugging tips & patterns
├── mcp_api_usage.md      # API call tracking
├── episodic.md           # Auto-aggregated session history
└── [domain-knowledge]/   # Domain-specific docs
```

**MEMORY.md Structure**:
```markdown
# Auto Memory — [Project Name]

## Current Status
[One-line summary of where we are]

## Key Learnings
[Quick reference topics with links]

## Quick Reference
[Essential info needed every session]

---
[Detailed content beyond 200 lines]
---
## [Topic 1 - Detailed notes]
## [Topic 2 - Detailed notes]
```

**How It's Used**:
1. **Session start**: Read MEMORY.md (first 200 lines)
2. **Auto-injected**: Those 200 lines go into system prompt
3. **On-demand**: Full MEMORY.md loaded via `/memory` command
4. **Topic files**: Loaded by name when mentioned or needed

### Subdirectory: session-data/

Stores current session state:

```
session-data/
├── context.json          # What's currently loaded in context
├── variables.json        # Session variables
├── models/
│   └── [model-config].json
├── tools/
│   └── [tool-state].json
└── timestamp.json        # Session start time
```

---

## Part 4: Skills System

### Directory: ~/.claude/skills/

**Purpose**: Reusable workflows and specialized knowledge (like prompts with attached tools).

**Structure**:
```
skills/
├── skill-creator/        # Meta-skill for creating new skills
│   ├── SKILL.md         # Skill definition
│   ├── template.md      # Template for new skills
│   └── examples/        # Example skills
├── [skill-name]/
│   ├── SKILL.md         # Main definition
│   ├── implementation.md # How it works
│   ├── examples/        # Use cases
│   └── resources/       # Supporting files
└── [another-skill]/
```

**SKILL.md Format**:
```markdown
---
name: skill-name
description: "What this skill does"
tags: [category, subtopic]
---

# [Skill Name]

## WHEN to Use
- Condition 1
- Condition 2

## WHEN NOT to Use
- Condition A

## Prerequisites
- [Requirement 1]

## How to Invoke
/skill-name [args]

## Execution Steps
1. Step 1
2. Step 2

## References
- [Related skill]
- [Documentation]
```

**Built-In Skills**:
- `/skill-creator` — Create new skills
- (Others added by user or Claude Code)

**Invoking Skills**: Type `/skill-name` in Claude Code to load and execute.

---

## Part 5: Plans & Plan Mode

### Directory: ~/.claude/plans/

**Purpose**: Store design and implementation plans created in "plan mode".

**File Format**:
```
[plan-name]-[random-id].md

Example: recursive-floating-quill.md (identifies a specific plan)
```

**When Plans Are Created**:
1. User enters plan mode: `claude --plan`
2. Claude designs an implementation approach
3. Plan is saved to this directory
4. User can exit, resume, or approve the plan

**Plan Structure**:
```markdown
# Plan: [Task Name]

## Context
[Problem statement, current state, requirements]

## Implementation Plan

### Phase 1: [Name]
- Step 1
- Step 2

### Phase 2: [Name]
- Step A
- Step B

## Critical Files
[Files that must be modified]

## Verification
[How to test the implementation]
```

---

## Part 6: Teams & Task Management

### Directory: ~/.claude/teams/

**Purpose**: Multi-agent team coordination.

**Structure**:
```
teams/
├── [team-name]/
│   ├── config.json       # Team members, settings
│   └── [member-files]    # Member-specific state
└── [team-name-2]/
```

**config.json Example**:
```json
{
  "team_name": "code-review-team",
  "created": "2024-02-27T10:00:00Z",
  "members": [
    {
      "name": "researcher",
      "agentId": "agent-uuid-1",
      "agentType": "Explore",
      "status": "idle"
    },
    {
      "name": "implementer",
      "agentId": "agent-uuid-2",
      "agentType": "general-purpose",
      "status": "in_progress"
    }
  ],
  "shared_context": {
    "project_root": "/path/to/project",
    "target_task": "Refactor auth module"
  }
}
```

### Directory: ~/.claude/tasks/

**Purpose**: Task lists per team.

**Structure**:
```
tasks/
├── [team-name]/
│   ├── task-001.json
│   ├── task-002.json
│   └── task-list.json    # Summary of all tasks
└── [team-name-2]/
```

**task-*.json Format**:
```json
{
  "id": "001",
  "subject": "Add error handling to auth",
  "description": "Implement try-catch blocks for database errors...",
  "status": "pending",
  "owner": "implementer",
  "blockedBy": ["task-001"],
  "blocks": ["task-003"],
  "created": "2024-02-27T10:00:00Z",
  "updated": "2024-02-27T10:15:00Z"
}
```

---

## Part 7: Session & Environment State

### Directory: ~/.claude/session-env/

**Purpose**: Snapshot the session environment for recovery and state persistence.

**Structure**:
```
session-env/
└── [project-id]/
    ├── context.json      # Loaded context snapshot
    ├── variables.json    # Defined variables
    ├── models/
    │   └── claude-opus-config.json
    ├── tools/
    │   └── [tool-state].json
    └── timestamp.json
```

**context.json Example**:
```json
{
  "loaded_files": [
    "/home/user/project/auth.py",
    "/home/user/project/models/user.py"
  ],
  "memory_loaded": true,
  "rules_active": ["default", "testing"],
  "token_usage": {
    "prompt": 5000,
    "completion": 2000,
    "total": 7000
  },
  "timestamp": "2024-02-27T10:30:00Z"
}
```

### Directory: ~/.claude/file-history/

**Purpose**: Track file changes across sessions for context.

**Structure**:
```
file-history/
└── [project-id]/
    ├── [file-hash-1].json
    ├── [file-hash-2].json
    └── index.json        # File → hash mapping
```

**File Entry**:
```json
{
  "path": "/home/user/project/auth.py",
  "hash": "sha256:abc123...",
  "last_modified": "2024-02-27T10:00:00Z",
  "sessions_mentioning_it": 45,
  "times_read": 32,
  "times_modified": 3,
  "size_bytes": 2450
}
```

---

## Part 8: Hooks System

### Directory: ~/.claude/hooks/

**Purpose**: Custom scripts that execute on lifecycle events.

**Available Hooks**:
- `onSessionStart.sh` — Runs when session begins
- `onSessionEnd.sh` — Runs when session ends
- `onFileRead.sh` — Runs when file is read
- `onFileWrite.sh` — Runs when file is written
- `onError.sh` — Runs when error occurs
- `onMemoryUpdate.sh` — Runs when MEMORY.md updated

**Example Hook**:
```bash
#!/bin/bash
# onSessionStart.sh

# Load custom environment variables
source ~/.bashrc

# Log session info
echo "Session started at $(date)" >> ~/.claude/session.log

# Optional: Load project-specific setup
if [ -f ".devenv" ]; then
  source .devenv
fi
```

**Usage**: Hooks are optional. If present, Claude Code executes them.

---

## Part 9: Debug, Cache & Telemetry

### Directory: ~/.claude/debug/

**Purpose**: Diagnostic logs for troubleshooting.

**Contents**:
- `trace-*.log` — Detailed execution traces
- `error-*.log` — Error messages and stack traces
- `performance-*.log` — Timing data

**Example Usage**:
```
tail -f ~/.claude/debug/error-*.log     # Watch for errors
grep "timeout" ~/.claude/debug/trace-*.log
```

### Directory: ~/.claude/cache/

**Purpose**: Performance optimization via caching.

**Types**:
- **context-cache.json**: Recent context loads
- **model-cache.json**: Model responses (for same query)
- **api-response-cache/**: API call results

**TTL**: Entries expire after 1 hour by default.

### Directory: ~/.claude/telemetry/

**Purpose**: Analytics and usage tracking (privacy-respecting).

**Collects**:
- Tokens used (per model, per day)
- API calls count
- Tool usage frequency
- Error rates
- Session duration

**Privacy**: Telemetry can be disabled via `settings.json: telemetry_enabled: false`.

---

## Part 10: Browser & IDE Integration

### Directory: ~/.claude/chrome/

**Purpose**: Browser automation state (for Claude in Chrome MCP).

**Contents**:
- `profile/` — Persistent browser profile
- `cookies.json` — Session cookies
- `storage.json` — Local storage data

**Used by**: `/perplexity-extract` and other browser skills.

### Directory: ~/.claude/ide/

**Purpose**: IDE-specific configurations and integrations.

**Contents**:
- `cursor-config.json` — Cursor IDE settings
- `vscode-settings.json` — VS Code settings
- `sublime-config.json` — Sublime Text config
- (Other IDE configs as needed)

**Example**:
```json
{
  "ide": "cursor",
  "rules_sync_enabled": true,
  "rules_path": ".cursor/rules",
  "auto_load_claude_config": true
}
```

---

## Part 11: Version Control & Git

### Directory: ~/.claude/.git/

**Purpose**: Claude Code's own version control (for internal state management).

**Note**: This is separate from project repos. It tracks changes to the `.claude` directory itself.

**Usage**: Allows recovery from accidental deletions of settings or memory files.

---

## Part 12: Complete Session Startup Flow

```
USER STARTS CLAUDE CODE
  ↓
CLAUDE CODE INITIALIZATION:
  1. Check if ~/.claude exists
  2. Load ~/.claude/CLAUDE.md (global rules)
  3. Load ~/.claude/settings.json (preferences)
  ↓
PROJECT IDENTIFICATION:
  1. Determine project ID from working directory
  2. Check ~/.claude/projects/[project-id]/
  ↓
LOAD PROJECT CONTEXT:
  1. Load ~/.claude/projects/[project-id]/memory/MEMORY.md (first 200 lines)
  2. Load ~/.claude/projects/[project-id]/session-data/context.json
  3. Check ~/.claude/projects/[project-id]/session-data/variables.json
  ↓
LOAD GLOBAL CONTEXT:
  1. Read CLAUDE.md (global rules)
  2. Read project CLAUDE.md (if exists)
  3. Read applicable skills from ~/.claude/skills/
  4. Read hooks from ~/.claude/hooks/ (if any)
  ↓
INITIALIZE SESSION:
  1. Create session environment in ~/.claude/session-env/[project-id]/
  2. Initialize file tracking in ~/.claude/file-history/[project-id]/
  3. Start history logging in ~/.claude/history.jsonl
  4. Execute onSessionStart.sh hook (if exists)
  ↓
RUN COMPACTION (if needed):
  1. Check context size
  2. If approaching limit, trim low-value items
  3. Store trimmed data in cache
  ↓
READY FOR INTERACTION:
  User can now type commands/requests
  ↓
ON EACH TURN:
  1. Read user input
  2. Check triggers (from CLAUDE.md)
  3. Load additional context if needed
  4. Execute tools
  5. Update memory (if /remember used)
  6. Log turn to history.jsonl
  ↓
SESSION CLEANUP (on exit):
  1. Execute onSessionEnd.sh hook
  2. Save final state to session-data/
  3. Update MEMORY.md if needed
  4. Commit history.jsonl
```

---

## Part 13: Context Loading Cascade

When Claude Code loads context, it follows this priority order:

```
1. CLAUDE.md (this file, ~/.claude/CLAUDE.md)
   ↓ (highest priority)

2. .claude/rules/                  (global rules directory)
   - Static rules (always apply)
   - Dynamic rules (scenario-specific)
   ↓

3. [Project Root]/CLAUDE.md         (project-specific rules)
   ↓

4. [Project Root]/.0agnostic/       (project's agnostic system)
   - 02_rules/
   - 01_knowledge/
   - 06_context_avenue_web/05_skills/
   ↓

5. ~/.claude/projects/[id]/memory/MEMORY.md (project memory, 200 lines)
   - Rest loaded on-demand via /memory command
   ↓

6. Tool descriptions & MCP servers  (what tools are available)
   ↓

7. User's current request           (what they're asking)
   ↓ (lowest priority)
```

**Important**: Earlier items override later items. Global CLAUDE.md rules override project rules.

---

## Summary: Native Components of .claude

### NATIVE TO .claude DIRECTORY

✅ **CLAUDE.md** — Global configuration (universal rules, triggers, skills)
✅ **settings.json** — User preferences (model, token limits, etc.)
✅ **.credentials.json** — Encrypted API keys
✅ **projects/** — Per-project memory (MEMORY.md, topic files, session state)
✅ **skills/** — Reusable skill definitions
✅ **plans/** — Design plans from plan mode
✅ **teams/** — Multi-agent team configurations
✅ **tasks/** — Task lists for teams
✅ **session-env/** — Current session state snapshots
✅ **file-history/** — File tracking for context
✅ **hooks/** — Custom lifecycle scripts
✅ **cache/** — Performance optimization caching
✅ **debug/** — Diagnostic logs
✅ **history.jsonl** — Full conversation history
✅ **chrome/** — Browser automation state
✅ **ide/** — IDE integration configs
✅ **telemetry/** — Usage analytics

### NOT NATIVE (Should Be Elsewhere)

❌ **Project code** (should be in project directory, not ~/.claude/)
❌ **Git repositories** (each project has its own .git/)
❌ **External credentials** (keep in password managers, only export to .credentials.json)
❌ **Large datasets** (cache them, don't store in ~/.claude/)

---

## References

- **Claude Code Documentation**: https://code.claude.com/docs
- **Memory System**: https://code.claude.com/docs/en/memory
- **Settings & Config**: https://code.claude.com/docs/en/settings
- **This System**: Explored from ~/.claude/ directory structure
