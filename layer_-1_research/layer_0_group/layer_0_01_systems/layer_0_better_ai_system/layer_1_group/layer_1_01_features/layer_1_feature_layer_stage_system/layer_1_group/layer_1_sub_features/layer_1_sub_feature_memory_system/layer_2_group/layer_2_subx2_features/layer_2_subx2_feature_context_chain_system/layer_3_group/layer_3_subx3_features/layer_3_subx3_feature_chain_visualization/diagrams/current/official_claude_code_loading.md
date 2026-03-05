---
resource_id: "921c97ab-6758-4f3d-95b1-201fbc05d592"
resource_type: "document"
resource_name: "official_claude_code_loading"
---
# Official Claude Code Context Loading

**Purpose**: Document how Claude Code officially loads context, based on official Anthropic documentation.

**Sources**:
- [Claude Code Memory Documentation](https://code.claude.com/docs/en/memory)
- [Claude Code Settings Documentation](https://code.claude.com/docs/en/settings)
- [Claude Code How It Works](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude Code MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Claude Code Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)

---

<!-- section_id: "6dcc3f31-27fd-45a5-a58f-7e7eee5bd936" -->
## Session Initialization Sequence

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│         OFFICIAL CLAUDE CODE SESSION INITIALIZATION SEQUENCE                     │
│         (What happens when you run `claude` in a directory)                      │
└─────────────────────────────────────────────────────────────────────────────────┘

    User runs: claude [options] [directory]
                    │
                    │ Working directory captured
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 1: SessionStart Hook Fires (if configured)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: .claude/settings.json or ~/.claude/settings.json (hooks field)   │
    │                                                                           │
    │  PURPOSE:                                                                 │
    │  • Run custom scripts before Claude sees any files                        │
    │  • Fetch recent issues, check git status, load dynamic context            │
    │  • Can write to CLAUDE_ENV_FILE to set environment variables              │
    │                                                                           │
    │  RECEIVES: JSON input indicating new session, resumed, or cleared         │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 2: Memory Files Loaded (CLAUDE.md Chain)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  CLAUDE.md DISCOVERY: Recursive Upward Traversal                          │
    │                                                                           │
    │  Claude Code traverses from working directory UPWARD to filesystem root,  │
    │  loading all CLAUDE.md or .claude/CLAUDE.md files found in parent dirs.   │
    │                                                                           │
    │  LOADING ORDER (highest precedence to lowest):                            │
    │                                                                           │
    │  1. System CLAUDE.md (deployed by IT to system directories)               │
    │       └── Cannot be overridden                                            │
    │                                                                           │
    │  2. User CLAUDE.md                                                        │
    │       └── ~/.claude/CLAUDE.md                                             │
    │       └── Applies to all projects                                         │
    │                                                                           │
    │  3. Project CLAUDE.md                                                     │
    │       └── {project}/CLAUDE.md OR {project}/.claude/CLAUDE.md              │
    │       └── Committed to source control, shared with team                   │
    │                                                                           │
    │  4. Local CLAUDE.md                                                       │
    │       └── {project}/CLAUDE.local.md                                       │
    │       └── Automatically gitignored, personal preferences                  │
    │       └── HIGHEST precedence for instructions                             │
    │                                                                           │
    │  ALSO LOADED: All .md files in .claude/rules/ directory                   │
    │       └── Same priority as main CLAUDE.md                                 │
    │       └── Enables modular rule organization                               │
    │                                                                           │
    │  NOTE: CLAUDE.md files in SUBDIRECTORIES are NOT loaded at startup.       │
    │        They load on-demand when Claude reads files in those directories.  │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 3: System Prompt Initialized
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: Hardcoded in Claude Code + optional overrides                    │
    │                                                                           │
    │  CONTAINS:                                                                │
    │  • Claude Code's core instructions                                        │
    │  • What tools are available (Read, Write, Edit, Bash, etc.)               │
    │  • How to behave as an agentic coding assistant                           │
    │  • Git Safety Protocol                                                    │
    │  • Security rules                                                         │
    │                                                                           │
    │  CAN BE CUSTOMIZED:                                                       │
    │  • --system-prompt "..."      (replaces entire system prompt)             │
    │  • --append-system-prompt "..." (adds to default prompt)                  │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 4: MCP Server Connections Established
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  MCP SERVER SOURCES:                                                      │
    │                                                                           │
    │  1. Managed MCP servers (system-wide, deployed by IT)                     │
    │       └── /etc/claude-code/ (Linux/WSL)                                   │
    │       └── /Library/Application Support/ClaudeCode/ (macOS)                │
    │       └── C:\Program Files\ClaudeCode\ (Windows)                          │
    │                                                                           │
    │  2. User MCP servers                                                      │
    │       └── ~/.claude.json (mcpServers field)                               │
    │       └── Available across all projects                                   │
    │                                                                           │
    │  3. Project MCP servers                                                   │
    │       └── .mcp.json (in project root)                                     │
    │       └── Committed to source control, shared with team                   │
    │       └── Requires user approval before connecting                        │
    │                                                                           │
    │  IMPORTANT: MCP definitions are in ~/.claude.json and .mcp.json           │
    │             NOT in settings.json (settings.json only enables/disables)    │
    │                                                                           │
    │  LOADED INTO CONTEXT: Tool definitions (metadata about available tools)   │
    │       └── Typically 500 - 10,000+ tokens depending on server count        │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 5: Settings Hierarchy Applied
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SETTINGS PRECEDENCE (highest to lowest):                                 │
    │                                                                           │
    │  1. Managed Settings (CANNOT be overridden)                               │
    │       └── /etc/claude-code/managed-settings.json (Linux/WSL)              │
    │       └── /Library/Application Support/ClaudeCode/managed-settings.json   │
    │       └── C:\Program Files\ClaudeCode\managed-settings.json (Windows)     │
    │                                                                           │
    │  2. Command Line Arguments                                                │
    │       └── --allowedTools, --system-prompt, etc.                           │
    │       └── Temporary session overrides                                     │
    │                                                                           │
    │  3. Local Project Settings                                                │
    │       └── .claude/settings.local.json                                     │
    │       └── Personal project-specific, gitignored                           │
    │                                                                           │
    │  4. Shared Project Settings                                               │
    │       └── .claude/settings.json                                           │
    │       └── Team-shared, committed to source control                        │
    │                                                                           │
    │  5. User Settings                                                         │
    │       └── ~/.claude/settings.json                                         │
    │       └── Personal global settings                                        │
    │                                                                           │
    │  PRINCIPLE: "Deny takes precedence over allow"                            │
    │       └── If ANY level denies a tool, it's denied                         │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 6: Skill Descriptions Loaded
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SOURCE: .claude/skills/*/SKILL.md (YAML frontmatter only)                │
    │                                                                           │
    │  LOADED: Skill name, description, estimated token cost                    │
    │  NOT LOADED: Full SKILL.md content (loaded on-demand when invoked)        │
    │                                                                           │
    │  PURPOSE: Allow Claude to decide which skills to use                      │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 7: Context Window Initialized
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Claude is informed of:                                                   │
    │  • Context window size (typically 200K tokens)                            │
    │  • Current token usage (system prompt + tools + memory + MCP)             │
    │  • Available token budget for conversation                                │
    │                                                                           │
    │  ENV VARS that affect this:                                               │
    │  • CLAUDE_CODE_MAX_OUTPUT_TOKENS (default 32,000, max 64,000)             │
    │  • CLAUDE_AUTOCOMPACT_PCT_OVERRIDE (auto-compaction threshold)            │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 8: Conversation History Restored (if resuming)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  If using --continue, --resume, or /resume:                               │
    │                                                                           │
    │  • Previous messages, tool calls, results appended to context             │
    │  • Session-scoped permissions are NOT restored (must re-grant)            │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    STEP 9: Session Ready for User Interaction
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Claude now has:                                                          │
    │  • Project knowledge from CLAUDE.md chain                                 │
    │  • Available tools (built-in + MCP)                                       │
    │  • Permissions from settings hierarchy                                    │
    │  • Dynamic context from SessionStart hooks                                │
    │  • Awareness of context budget                                            │
    │                                                                           │
    │  Ready to receive first user message and begin agentic loop.              │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "7c311e8c-73cd-4d35-ba6c-66a47213d97f" -->
## File Locations Reference

<!-- section_id: "4168a579-07fe-4a11-b771-30febe27887b" -->
### Memory Files (CLAUDE.md)

| Scope | Location | Shared? | Precedence |
|-------|----------|---------|------------|
| System | System directories (deployed by IT) | Yes | Highest |
| User | `~/.claude/CLAUDE.md` | No | High |
| Project | `CLAUDE.md` or `.claude/CLAUDE.md` | Yes (git) | Medium |
| Local | `CLAUDE.local.md` | No (gitignored) | Lowest (wins) |
| Rules | `.claude/rules/*.md` | Yes (git) | Same as project |

<!-- section_id: "e7c3d4af-b111-4c7e-93c0-2fe64fc7e400" -->
### Settings Files

| Scope | Location | Shared? | Precedence |
|-------|----------|---------|------------|
| Managed | `/etc/claude-code/managed-settings.json` (Linux) | Yes (IT) | Highest |
| CLI | Command line arguments | No | High |
| Local Project | `.claude/settings.local.json` | No (gitignored) | Medium |
| Project | `.claude/settings.json` | Yes (git) | Low |
| User | `~/.claude/settings.json` | No | Lowest |

<!-- section_id: "beadec3e-644b-46b4-822c-ec947fe9adbc" -->
### MCP Server Definitions

| Scope | Location | Shared? |
|-------|----------|---------|
| Managed | System directories | Yes (IT) |
| User | `~/.claude.json` (mcpServers field) | No |
| Project | `.mcp.json` | Yes (git) |

<!-- section_id: "682e4318-cada-4d35-94e7-26b665215395" -->
### Other Configuration

| Type | User Location | Project Location |
|------|---------------|------------------|
| Commands | `~/.claude/commands/*.md` | `.claude/commands/*.md` |
| Agents | `~/.claude/agents/*.md` | `.claude/agents/*.md` |
| Skills | N/A | `.claude/skills/*/SKILL.md` |

---

<!-- section_id: "f702c66b-72ce-477a-947f-61ef1105e42c" -->
## Auto-Loaded vs On-Demand

<!-- section_id: "3f4a3927-6a32-4c49-b76d-309c5c045db0" -->
### Automatically Loaded at Session Start

| What | Source | Notes |
|------|--------|-------|
| System prompt | Hardcoded | Immutable core instructions |
| Built-in tools | Hardcoded | Read, Write, Edit, Bash, Glob, Grep, Task, etc. |
| CLAUDE.md chain | All CLAUDE.md files from ~ to cwd | Upward traversal only |
| .claude/rules/*.md | Project .claude/rules/ | Same priority as CLAUDE.md |
| CLAUDE.local.md | Project root | Personal overrides |
| MCP tool definitions | ~/.claude.json + .mcp.json | Metadata only |
| Skill descriptions | .claude/skills/*/SKILL.md | YAML frontmatter only |
| Settings | All settings.json files | Merged by precedence |

<!-- section_id: "48aa4e08-e989-40cd-a976-588338859136" -->
### Loaded On-Demand (NOT at startup)

| What | When Loaded | Notes |
|------|-------------|-------|
| Subdirectory CLAUDE.md | When Claude reads files in that directory | Lazy loading |
| Skill full content | When skill is invoked | Conserves context |
| Subagent definitions | When subagent is spawned | Own context window |
| @imported files | When parent CLAUDE.md is loaded | Follows import chain |

---

<!-- section_id: "341dce3b-fc6b-44dc-a686-8183aa706416" -->
## CLAUDE.md Features

<!-- section_id: "aa36b156-7fc4-4593-953d-7b3baa4a2ef1" -->
### @import System

CLAUDE.md files can reference other files:

```markdown
# Project Guidelines

@docs/coding-standards.md
@docs/api-conventions.md
@docs/security-rules.md
```

- Imports evaluated relative to importing file (not cwd)
- Maximum 5 levels of nesting
- Imported content loaded with parent CLAUDE.md

<!-- section_id: "976b1cff-0cbf-4388-b847-db66abbf5bd0" -->
### .claude/rules/ Directory

Alternative to @imports for modular organization:

```
.claude/
├── CLAUDE.md           (main file)
└── rules/
    ├── code-style.md   (auto-loaded)
    ├── testing.md      (auto-loaded)
    ├── security.md     (auto-loaded)
    └── frontend/
        └── react.md    (auto-loaded)
```

All .md files in .claude/rules/ (including subdirectories) are auto-loaded.

<!-- section_id: "101eaa6a-0e6a-42e3-979f-6caf187c633f" -->
### Case Sensitivity

**CRITICAL**: Filename must be exactly `CLAUDE.md`:
- ✅ `CLAUDE.md`
- ❌ `claude.md`
- ❌ `Claude.md`
- ❌ `CLAUDE.MD`

---

<!-- section_id: "558c9e8d-15b0-4310-9849-c7afd98f5f68" -->
## Environment Variables

<!-- section_id: "34d07266-2394-4631-8f7a-c6acdd8bb7bc" -->
### Key Variables for Context/Loading

| Variable | Purpose |
|----------|---------|
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output tokens (default 32K, max 64K) |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Context auto-compaction threshold (1-100%) |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Load CLAUDE.md from --add-dir directories |
| `CLAUDE_CONFIG_DIR` | Custom config storage location |
| `MAX_THINKING_TOKENS` | Extended thinking budget |

---

<!-- section_id: "16d1e3d4-5521-477f-89c2-f6eefcd4c3d6" -->
## Summary: What Claude Knows at Session Start

When you run `claude` in a directory, Claude immediately knows:

1. **Identity**: Claude Code agentic coding assistant
2. **Tools**: All built-in tools + connected MCP server tools
3. **Permissions**: Merged from all settings.json files
4. **Project Knowledge**: All CLAUDE.md content from path traversal
5. **Rules**: All .claude/rules/*.md content
6. **Skills Available**: Descriptions of .claude/skills/
7. **Context Budget**: How many tokens available

Claude does NOT automatically know:
- Contents of subdirectory CLAUDE.md files
- Full skill content (until invoked)
- Individual file contents (must Read)
- Subagent capabilities (until spawned)

---

**Sources**:
- [Claude Code Memory](https://code.claude.com/docs/en/memory)
- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Claude Code How It Works](https://code.claude.com/docs/en/how-claude-code-works)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Claude Code Sub-agents](https://code.claude.com/docs/en/sub-agents)

*Last updated: 2026-02-05*
