---
resource_id: "a9e3b7f5-b3f3-4688-b6a8-f245f720677d"
resource_type: "document"
resource_name: "default_view"
---
# Context Chain — Default View (Configurable Context)

> Chronological loading order of everything the user can change.
> Shows what the AI model sees, in the order it sees it.

> **Note**: No official unified context chain diagram exists from Anthropic. The official documentation covers each piece individually (settings, MCP, memory, skills, CLAUDE.md) but does not provide a single chronological visualization of everything loaded into context. This diagram was assembled from multiple official sources. See [Sources](#sources) below.

## Dimensions

| Tag | Meaning |
|-----|---------|
| `STATIC` | Automatically in every message sent to the AI model |
| `DYNAMIC` | Only enters context when invoked on-demand |

## Scope Levels (Official Claude Code Scopes)

| Scope | Meaning | Shared? |
|-------|---------|---------|
| `managed` | Deployed by IT/admin, highest precedence, cannot be overridden | Yes (all users on machine) |
| `user` | Personal config across all projects | No |
| `project` | Per-repo, committed to git, shared with collaborators | Yes (team) |
| `local` | Personal overrides for a specific project, gitignored | No |
| `session` | Unique to this chat session | N/A |
| `invocation` | Unique to a single tool call, ephemeral | N/A |

**Precedence**: managed > local > project > user (highest to lowest)

This view shows **only configurable context**. For the complete chain including fixed/immutable items, see [full_view.md](full_view.md).

---

## Loading Order

```
CONFIGURABLE CONTEXT CHAIN (chronological)
===========================================
What the AI model sees, in order, that YOU control.

     |
     v
+-----------------------------------------+
| 1. MANAGED SETTINGS              STATIC |
|    Scope: managed                        |
|                                          |
|    /etc/claude-code/                     |
|      managed-settings.json               |
|    Admin-deployed, cannot be overridden  |
|    Shared across all users on machine    |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 2. AUTO MEMORY                    STATIC |
|    Scope: project (by launch dir)        |
|                                          |
|    ~/.claude/projects/                   |
|      <project>/memory/MEMORY.md          |
|    Injected into system prompt           |
|    Lines after 200 truncated             |
|                                          |
|    Per launch directory only.            |
|    No global auto memory exists.         |
|    Different cwd = different memory.     |
|    NOT picked up on traversal (unlike    |
|    CLAUDE.md which is).                  |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 3a. MCP SCHEMAS (managed)         STATIC |
|     Scope: managed                       |
|                                          |
|     /etc/claude-code/                    |
|       managed-mcp.json                   |
|     Admin-deployed, can enforce          |
|     allowedMcpServers / deniedMcpServers |
|     Overrides all other MCP scopes       |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 3b. MCP SCHEMAS (user)            STATIC |
|     Scope: user                          |
|                                          |
|     ~/.claude.json -> mcpServers         |
|     Available across ALL projects        |
|                                          |
|     - perplexity     (4 schemas)         |
|     - canvas         (~40 schemas)       |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 3c. MCP SCHEMAS (local)           STATIC |
|     Scope: local                         |
|                                          |
|     ~/.claude.json ->                    |
|       projects["<cwd>"].mcpServers       |
|     Per launch directory, stored in      |
|     user settings (not version-          |
|     controlled, not shared)              |
|                                          |
|     - playwright     (~20 schemas)       |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 3d. MCP SCHEMAS (project)         STATIC |
|     Scope: project                       |
|                                          |
|     <repo>/.mcp.json                     |
|     Version-controlled, shared with      |
|     anyone who clones the repo           |
|                                          |
|     - filesystem     (in 0_layer_        |
|       universal/.mcp.json)               |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 3e. MCP SCHEMAS (IDE/extension)   STATIC |
|     Scope: session                       |
|                                          |
|     Auto-detected from active IDE        |
|     and browser extensions               |
|                                          |
|     - ide            (2 schemas)         |
|       (VS Code integration)             |
|     - claude-in-chrome (~20 schemas)     |
|       (Chrome extension)                |
|                                          |
|     Present only when IDE/extension      |
|     is running                           |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 4a. SKILL LISTINGS (user)         STATIC |
|     Scope: user                          |
|                                          |
|     ~/.claude/skills/                    |
|     Skills available across ALL projects |
|                                          |
|     - skill-creator                      |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 4b. SKILL LISTINGS (plugins)      STATIC |
|     Scope: user                          |
|                                          |
|     ~/.claude/plugins/                   |
|     Marketplace-installed plugins        |
|     ~/.claude/settings.json ->           |
|       enabledPlugins                     |
|                                          |
|     - document-skills (pdf, pptx,        |
|       xlsx, frontend-design, etc.)       |
|     - keybindings-help                   |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 4c. SKILL LISTINGS (project)      STATIC |
|     Scope: project                       |
|                                          |
|     <repo>/.claude/skills/               |
|     Available when launched from         |
|     this repo (version-controlled)       |
|                                          |
|     - context-gathering                  |
|     - handoff-creation                   |
|     - entity-creation                    |
|     - stage-workflow                     |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 5. CLAUDE.md CHAIN (cwd path)     STATIC |
|    Scope: mixed (user -> project)        |
|                                          |
|    Auto-loaded based on working          |
|    directory at session start            |
|                                          |
|    ~/.claude/CLAUDE.md       [user]      |
|             |                            |
|             v                            |
|    ~/CLAUDE.md               [user]      |
|             |                            |
|             v                            |
|    <workspace>/CLAUDE.md     [project]   |
|             |                            |
|             v                            |
|    <project>/CLAUDE.md       [project]   |
|             |                            |
|             v                            |
|    <project>/.claude.local.md [local]    |
|                                          |
|    Every line costs tokens on            |
|    EVERY API call                        |
+-----------------------------------------+
     |
     v
 ~~~ session begins, user sends messages ~~~
     |
     v
+-----------------------------------------+
| 6. TOOL CALL RESULTS            DYNAMIC |
|    Scope: invocation                     |
|                                          |
|    Enters context when AI invokes        |
|    a built-in tool                       |
|                                          |
|    - Bash output                         |
|    - Read file contents                  |
|    - Grep / Glob results                 |
|    - Edit / Write confirmations          |
|    - Task (subagent) results             |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 7. MCP TOOL RESULTS             DYNAMIC |
|    Scope: invocation                     |
|                                          |
|    Enters context when AI calls          |
|    an MCP tool                           |
|                                          |
|    - Canvas data                         |
|    - Perplexity responses                |
|    - Playwright snapshots                |
|    - Chrome extension reads              |
|    - IDE diagnostics                     |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 8. SKILL FULL CONTENT           DYNAMIC |
|    Scope: invocation                     |
|                                          |
|    Full skill prompt loads only          |
|    on /skill invoke                      |
|                                          |
|    - pdf, pptx, xlsx                     |
|    - frontend-design                     |
|    - webapp-testing                      |
|    - skill-creator, etc.                 |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 9. DEEPER SKILL LISTINGS        DYNAMIC |
|    Scope: invocation                     |
|                                          |
|    Skills in .claude/skills/ of          |
|    subdirectories beyond cwd --          |
|    only listed if AI traverses           |
|    into those directories                |
|                                          |
|    - diagram-generation (in context_     |
|      visualization sub-feature)          |
|    - entity-creation (in better_         |
|      ai_system/layer_0_group)            |
|    - stage_manager-workflow (in          |
|      layer_-1_99_stages)                |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 10. DEEPER CLAUDE.md FILES      DYNAMIC |
|     Scope: invocation                    |
|                                          |
|     CLAUDE.md beyond cwd path --         |
|     only loaded if AI traverses          |
|     into those directories               |
+-----------------------------------------+
```

---

## Filesystem Reference

> Triple-click a path to select it, then Ctrl+C → Ctrl+P → Ctrl+V → Enter to open.

### Managed Scope

Managed settings:

/etc/claude-code/managed-settings.json

Managed MCP:

/etc/claude-code/managed-mcp.json

### User Scope

User MCP servers (top-level mcpServers key):

/home/dawson/.claude.json

User settings:

/home/dawson/.claude/settings.json

CLAUDE.md (global):

/home/dawson/.claude/CLAUDE.md

CLAUDE.md (home):

/home/dawson/CLAUDE.md

User skills:

/home/dawson/.claude/skills/

User plugins/skills:

/home/dawson/.claude/plugins/marketplaces/claude-plugins-official/

### Project Scope

Auto memory:

/home/dawson/.claude/projects/-home-dawson/memory/MEMORY.md

Project MCP servers:

/home/dawson/dawson-workspace/code/0_layer_universal/.mcp.json

Project settings (path varies by repo):

\<repo\>/.claude/settings.json

CLAUDE.md (workspace):

/home/dawson/dawson-workspace/CLAUDE.md

CLAUDE.md (code):

/home/dawson/dawson-workspace/code/CLAUDE.md

CLAUDE.md (layer sys):

/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md

Project skills:

/home/dawson/dawson-workspace/code/0_layer_universal/.claude/skills/

### Local Scope

Local MCP servers (projects["cwd"].mcpServers key):

/home/dawson/.claude.json

Local settings (path varies by repo):

\<repo\>/.claude/settings.local.json

Local CLAUDE.md (path varies by repo):

\<repo\>/.claude.local.md

### Invocation Scope (examples)

Deeper skills (layer_0_group):

/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/.claude/skills/

---

## Key Insight

Items 1-5 (STATIC) are the cost you pay on **every single API call**. Items 6-9 (DYNAMIC) only cost tokens when actually used. The biggest optimization lever is keeping items 1-5 lean and pushing detail into items 6-9.

---

## Traversal Behavior: CLAUDE.md vs Auto Memory

A critical difference between two configurable static items:

| Behavior | CLAUDE.md (item 5) | Auto Memory (item 2) |
|----------|---------------------|----------------------|
| **At session start** | All CLAUDE.md files from root to cwd loaded | Only the MEMORY.md for the launch directory loaded |
| **During traversal** | Additional CLAUDE.md files appear as system-reminders when AI enters new directories | No other MEMORY.md files are picked up |
| **Scope** | Hierarchical — stacks as you go deeper (user -> project) | Flat — one project directory, one memory file |
| **Global equivalent** | `~/.claude/CLAUDE.md` (manual, always loaded) | None — no global auto memory exists |

**Implication**: Learnings recorded in one project's auto memory are invisible to sessions launched from a different directory, even if the work overlaps. CLAUDE.md does not have this limitation since it chains hierarchically and traverses dynamically.

---

## Scope Summary

```
 #  | Item                    | Static/Dynamic | Scope
----+-------------------------+----------------+-----------
  1 | Managed settings        | Static         | managed
  2 | Auto memory             | Static         | project
 3a | MCP schemas (managed)   | Static         | managed
 3b | MCP schemas (user)      | Static         | user
 3c | MCP schemas (local)     | Static         | local
 3d | MCP schemas (project)   | Static         | project
 3e | MCP schemas (IDE/ext)   | Static         | session
 4a | Skill listings (user)   | Static         | user
 4b | Skill listings (plugins)| Static         | user
 4c | Skill listings (project)| Static         | project
  5 | CLAUDE.md chain (cwd)   | Static         | user->local
  6 | Tool call results       | Dynamic        | invocation
  7 | MCP tool results        | Dynamic        | invocation
  8 | Skill full content      | Dynamic        | invocation
  9 | Deeper skill listings   | Dynamic        | invocation
 10 | Deeper CLAUDE.md files  | Dynamic        | invocation
```

---

## Sources

### Per-Item Sources

| # | Item | Sources |
|---|------|---------|
| 1 | Managed settings | [Settings: Managed](https://code.claude.com/docs/en/settings#managed-settings) |
| 2 | Auto memory | [Memory](https://code.claude.com/docs/en/memory), [GH #23750](https://github.com/anthropics/claude-code/issues/23750), [Session Memory](https://claudefa.st/blog/guide/mechanics/session-memory) |
| 3a | MCP schemas (managed) | [MCP: Managed](https://code.claude.com/docs/en/mcp#managed-mcp-servers) |
| 3b | MCP schemas (user) | [MCP: User](https://code.claude.com/docs/en/mcp#user-mcp-servers) |
| 3c | MCP schemas (local) | [MCP: Local](https://code.claude.com/docs/en/mcp#project-specific-mcp-servers), [Settings: Local](https://code.claude.com/docs/en/settings#local-settings) |
| 3d | MCP schemas (project) | [MCP: Project](https://code.claude.com/docs/en/mcp#shared-mcp-servers) |
| 3e | MCP schemas (IDE/ext) | [MCP](https://code.claude.com/docs/en/mcp) (auto-detection behavior) |
| 4a | Skill listings (user) | [Skills](https://code.claude.com/docs/en/skills), [Skills Guide PDF](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| 4b | Skill listings (plugins) | [Skills](https://code.claude.com/docs/en/skills) |
| 4c | Skill listings (project) | [Skills](https://code.claude.com/docs/en/skills) |
| 5 | CLAUDE.md chain | [Memory: CLAUDE.md](https://code.claude.com/docs/en/memory#claudemd), [Settings](https://code.claude.com/docs/en/settings) |
| 6 | Tool call results | [Claude Code Overview](https://code.claude.com/docs/en/overview) (built-in tools) |
| 7 | MCP tool results | [MCP](https://code.claude.com/docs/en/mcp) |
| 8 | Skill full content | [Skills](https://code.claude.com/docs/en/skills) |
| 9 | Deeper skill listings | [Skills](https://code.claude.com/docs/en/skills) (directory traversal behavior) |
| 10 | Deeper CLAUDE.md files | [Memory: CLAUDE.md](https://code.claude.com/docs/en/memory#claudemd) (traversal behavior) |

### General Sources

These sources informed the overall structure and multiple items:

- [Claude Code Settings & Scopes](https://code.claude.com/docs/en/settings) — official scope definitions (managed, user, project, local), precedence order, filesystem paths
- [Claude Code MCP Configuration](https://code.claude.com/docs/en/mcp) — MCP server scopes, managed-mcp.json, .mcp.json
- [Claude Code Memory](https://code.claude.com/docs/en/memory) — auto memory, MEMORY.md, CLAUDE.md, per-project scoping
- [Claude Code Skills](https://code.claude.com/docs/en/skills) — skill definitions, SKILL.md, scoping, invocation
- [Claude Code Overview](https://code.claude.com/docs/en/overview) — general architecture, built-in tools
- [GitHub Issue #23750](https://github.com/anthropics/claude-code/issues/23750) — auto memory opt-in/opt-out discussion
- [Claude Code Session Memory](https://claudefa.st/blog/guide/mechanics/session-memory) — session memory rollout timeline
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) — Anthropic's official skill-building guide

### No Official Unified Diagram

As of February 2026, Anthropic does not publish a single unified context chain diagram. Each documentation page covers its own piece:

- [Settings](https://code.claude.com/docs/en/settings) covers scopes and precedence but not loading order
- [MCP](https://code.claude.com/docs/en/mcp) covers server configuration but not its position relative to other context
- [Memory](https://code.claude.com/docs/en/memory) covers CLAUDE.md and auto memory but not the full chain
- [Skills](https://code.claude.com/docs/en/skills) covers skill files but not when they enter context relative to everything else

This diagram was assembled by cross-referencing these sources, inspecting system prompt content, and observing actual Claude Code behavior.

> **Anchor links**: Source URLs use `#fragment` anchors where the official docs support them (e.g., `#managed-settings`, `#claudemd`). If a specific anchor doesn't resolve, it will still land on the correct page.
