# Official Claude Code Context Loading

**Purpose**: Document how Claude Code (the tool) officially loads context, separate from any custom additions.

**Source**: Claude Code's built-in behavior as of 2026-02

---

## Official Loading Sequence

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│         OFFICIAL CLAUDE CODE CONTEXT LOADING (Tool's Built-in Behavior)         │
└─────────────────────────────────────────────────────────────────────────────────┘

    User runs: claude [options] [directory]
                    │
                    │ Working directory determined
                    │ (defaults to current directory)
                    │
    ════════════════════════════════════════════════════════════════════════════
    PHASE 1: ANTHROPIC SYSTEM PROMPT (Hardcoded, Immutable)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 1: System Prompt Injection                                         │
    │                                                                           │
    │  SOURCE: Hardcoded in Claude Code binary                                  │
    │  CONTROLLED BY: Anthropic                                                 │
    │                                                                           │
    │  CONTAINS:                                                                │
    │  • "You are Claude Code, Anthropic's official CLI for Claude"             │
    │  • Model identity and safety rules                                        │
    │  • Tool usage instructions (how to use Read, Write, Bash, etc.)           │
    │  • Git Safety Protocol                                                    │
    │  • Security rules for browser automation                                  │
    │  • Copyright requirements                                                 │
    │                                                                           │
    │  USER CONTROL: ❌ None                                                    │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    PHASE 2: TOOL REGISTRATION (Built into Claude Code)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 2: Built-in Tools                                                  │
    │                                                                           │
    │  SOURCE: Claude Code application                                          │
    │  CONTROLLED BY: Anthropic                                                 │
    │                                                                           │
    │  TOOLS REGISTERED:                                                        │
    │  • Read, Write, Edit, NotebookEdit                                        │
    │  • Bash, Glob, Grep                                                       │
    │  • Task (subagents)                                                       │
    │  • WebFetch, WebSearch                                                    │
    │  • AskUserQuestion, Skill                                                 │
    │  • EnterPlanMode, ExitPlanMode                                            │
    │  • TaskCreate, TaskUpdate, TaskGet, TaskList                              │
    │                                                                           │
    │  USER CONTROL: ❌ None (tools are fixed)                                  │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    PHASE 3: USER CONFIGURATION (~/.claude/)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 3: Global Settings                                                 │
    │                                                                           │
    │  SOURCE: ~/.claude/settings.json                                          │
    │  CONTROLLED BY: User                                                      │
    │                                                                           │
    │  CAN CONTAIN:                                                             │
    │  • MCP server configurations                                              │
    │  • Permission settings (allow/deny patterns)                              │
    │  • Model preferences                                                      │
    │  • API keys                                                               │
    │                                                                           │
    │  USER CONTROL: ✅ Full (user edits file)                                  │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 4: MCP Server Connections                                          │
    │                                                                           │
    │  SOURCE: MCP configs in ~/.claude/settings.json                           │
    │  CONTROLLED BY: User                                                      │
    │                                                                           │
    │  CONNECTS TO:                                                             │
    │  • Configured MCP servers (perplexity, playwright, filesystem, etc.)      │
    │  • Registers additional tools (mcp__servername__toolname)                 │
    │                                                                           │
    │  USER CONTROL: ✅ Full (user configures MCP servers)                      │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 5: Global CLAUDE.md                                                │
    │                                                                           │
    │  SOURCE: ~/.claude/CLAUDE.md                                              │
    │  CONTROLLED BY: User                                                      │
    │  OFFICIAL FEATURE: ✅ Yes (documented Claude Code feature)                │
    │                                                                           │
    │  PURPOSE:                                                                 │
    │  • Machine-level instructions that apply to ALL sessions                  │
    │  • User's personal coding preferences                                     │
    │  • Global rules and behaviors                                             │
    │                                                                           │
    │  USER CONTROL: ✅ Full (user writes file)                                 │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    PHASE 4: PATH-BASED CLAUDE.md LOADING (Official Feature)
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 6+: Path CLAUDE.md Files                                           │
    │                                                                           │
    │  SOURCE: CLAUDE.md files from ~ to working directory                      │
    │  CONTROLLED BY: User                                                      │
    │  OFFICIAL FEATURE: ✅ Yes (documented Claude Code feature)                │
    │                                                                           │
    │  BEHAVIOR:                                                                │
    │  Claude Code traverses from user home (~) to working directory            │
    │  and loads every CLAUDE.md file found along the path.                     │
    │                                                                           │
    │  EXAMPLE (cwd = /home/user/projects/myapp):                               │
    │    1. ~/.claude/CLAUDE.md        (global)                                 │
    │    2. ~/CLAUDE.md                (if exists)                              │
    │    3. ~/projects/CLAUDE.md       (if exists)                              │
    │    4. ~/projects/myapp/CLAUDE.md (if exists)                              │
    │                                                                           │
    │  USER CONTROL: ✅ Full (user creates files in path)                       │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    PHASE 5: PROJECT CONFIGURATION
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ORDER 7: Project Settings                                                │
    │                                                                           │
    │  SOURCE: {working_dir}/.claude/settings.json                              │
    │  CONTROLLED BY: User/Project                                              │
    │  OFFICIAL FEATURE: ✅ Yes                                                 │
    │                                                                           │
    │  CAN CONTAIN:                                                             │
    │  • Project-specific permissions                                           │
    │  • Project-specific MCP servers                                           │
    │  • Allowed/denied tool patterns                                           │
    │                                                                           │
    │  USER CONTROL: ✅ Full (user/team edits file)                             │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
    ════════════════════════════════════════════════════════════════════════════
    PHASE 6: SESSION READY
    ════════════════════════════════════════════════════════════════════════════
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Agent ready to receive user messages                                     │
    │                                                                           │
    │  TOTAL AUTO-LOADED:                                                       │
    │  • System prompt (immutable)                                              │
    │  • Built-in tools                                                         │
    │  • MCP servers + their tools                                              │
    │  • Global settings                                                        │
    │  • All CLAUDE.md files in path                                            │
    │  • Project settings                                                       │
    │                                                                           │
    │  EVERYTHING ELSE: Agent must read manually using tools                    │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

## Official Claude Code Features Summary

| Feature | Location | Auto-loaded? | User Control |
|---------|----------|--------------|--------------|
| System prompt | Hardcoded | ✅ | ❌ |
| Built-in tools | Hardcoded | ✅ | ❌ |
| Global settings | ~/.claude/settings.json | ✅ | ✅ |
| MCP servers | ~/.claude/settings.json | ✅ | ✅ |
| Global CLAUDE.md | ~/.claude/CLAUDE.md | ✅ | ✅ |
| Path CLAUDE.md | Every CLAUDE.md from ~ to cwd | ✅ | ✅ |
| Project settings | .claude/settings.json | ✅ | ✅ |
| Skills | .claude/skills/ | ❌ (via Skill tool) | ✅ |

---

## What Claude Code Does NOT Auto-Load

These require agent action (Read tool) or explicit invocation:

| File Type | How to Access |
|-----------|---------------|
| `index.jsonld` | Agent must Read |
| `SKILL.md` | Via Skill tool or Read |
| `*.jsonld` schemas | Agent must Read |
| `status.json` | Agent must Read |
| `AGENTS.md` | Agent must Read |
| Any other file | Agent must Read |

---

## Key Insight: CLAUDE.md is the Official Extension Point

Claude Code officially supports CLAUDE.md files as the primary way to inject custom instructions:

1. **Global** (~/.claude/CLAUDE.md) - Applies to all sessions
2. **Path-based** (any CLAUDE.md in path) - Applies based on location
3. **Project** ({project}/CLAUDE.md) - Applies to project

Everything beyond CLAUDE.md requires agent-driven loading.

---

*Last updated: 2026-02-05*
*Based on Claude Code behavior as of 2026-02*
