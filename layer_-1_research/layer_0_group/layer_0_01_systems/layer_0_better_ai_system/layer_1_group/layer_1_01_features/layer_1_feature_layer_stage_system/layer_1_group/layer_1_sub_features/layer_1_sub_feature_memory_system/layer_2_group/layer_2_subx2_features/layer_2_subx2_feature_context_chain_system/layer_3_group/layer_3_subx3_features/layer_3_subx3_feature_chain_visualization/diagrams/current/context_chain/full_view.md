---
resource_id: "c6c3482b-bb3b-4a4e-8507-5ff10745f7c9"
resource_type: "document"
resource_name: "full_view"
---
# Context Chain — Full View (All Context)

> Chronological loading order of everything sent to the AI model.
> Each item tagged as fixed or configurable, static or dynamic, with scope.

> **Note**: No official unified context chain diagram exists from Anthropic. The official documentation covers each piece individually (settings, MCP, memory, skills, CLAUDE.md) but does not provide a single chronological visualization of everything loaded into context. This diagram was assembled from multiple official sources. See [Sources](#sources) below.

<!-- section_id: "a75c4a63-31d5-46f7-8be9-e933ef00f56f" -->
## Dimensions

| Tag | Meaning |
|-----|---------|
| `FIXED` | Set by Anthropic / Claude Code — user cannot change this |
| `CONFIGURABLE` | User can author, edit, or control this content |
| `STATIC` | Automatically in every message sent to the AI model |
| `DYNAMIC` | Only enters context when invoked on-demand |

<!-- section_id: "56d6d906-5cff-42fd-9377-6ebe46a15348" -->
## Scope Levels (Official Claude Code Scopes)

| Scope | Meaning | Shared? |
|-------|---------|---------|
| `global` | Same for all Claude Code users (set by Anthropic) | N/A |
| `managed` | Deployed by IT/admin, highest precedence, cannot be overridden | Yes (all users on machine) |
| `user` | Personal config across all projects | No |
| `project` | Per-repo, committed to git, shared with collaborators | Yes (team) |
| `local` | Personal overrides for a specific project, gitignored | No |
| `session` | Unique to this chat session | N/A |
| `invocation` | Unique to a single tool call, ephemeral | N/A |

**Precedence**: managed > local > project > user (highest to lowest)

For only the configurable items, see [default_view.md](default_view.md).

---

<!-- section_id: "bea6cfa8-3ae7-44c6-aad9-f00d6e2a131e" -->
## Loading Order

```
FULL CONTEXT CHAIN (chronological)
====================================
Everything the AI model sees, in order.

     |
     v
+-----------------------------------------+
| 1. SYSTEM PROMPT        FIXED | STATIC  |
|    Scope: global                         |
|                                          |
|    Hardcoded by Claude Code binary       |
|    - Agent role & behavior               |
|    - Tool usage rules & preferences      |
|    - Git safety protocol                 |
|    - PR/commit workflows                 |
|    - Tone/style guidelines               |
|    Same for all users of this version    |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 2. BROWSER SECURITY     FIXED | STATIC  |
|    RULES                                 |
|    Scope: global                         |
|                                          |
|    Hardcoded, immutable                  |
|    - Critical injection defense          |
|    - Social engineering defense          |
|    - User privacy protections            |
|    - Prohibited actions list             |
|    - Explicit permission actions list    |
|    - Copyright requirements              |
|    - Download restrictions               |
|    Same for all users                    |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 3. ENVIRONMENT          FIXED | STATIC  |
|    DETECTION                             |
|    Scope: session                        |
|                                          |
|    Auto-detected at session start        |
|    - Platform (linux/mac/windows)        |
|    - OS version                          |
|    - Working directory                   |
|    - Git repo status                     |
|    - Current date                        |
|    - Model ID                            |
|    Snapshot taken once, fixed for session |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 4. MANAGED SETTINGS  CONFIGURABLE |     |
|                           STATIC        |
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
| 5. AUTO MEMORY       CONFIGURABLE |     |
|                           STATIC        |
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
| 6a. BUILT-IN TOOL       FIXED | STATIC  |
|     SCHEMAS                              |
|     Scope: global                        |
|                                          |
|     Hardcoded in Claude Code binary      |
|     Bash, Read, Write, Edit, Glob,       |
|     Grep, Task, WebFetch, WebSearch,     |
|     Skill, EnterPlanMode, etc.           |
|     Same for all users of this version   |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 6b. MCP SCHEMAS      CONFIGURABLE |     |
|     (managed)             STATIC        |
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
| 6c. MCP SCHEMAS      CONFIGURABLE |     |
|     (user)                STATIC        |
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
| 6d. MCP SCHEMAS      CONFIGURABLE |     |
|     (local)               STATIC        |
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
| 6e. MCP SCHEMAS      CONFIGURABLE |     |
|     (project)             STATIC        |
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
| 6f. MCP SCHEMAS        FIXED | STATIC  |
|     (IDE/extension)                      |
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
| 7a. SKILL LISTINGS  CONFIGURABLE |      |
|     (user)                STATIC        |
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
| 7b. SKILL LISTINGS  CONFIGURABLE |      |
|     (plugins)             STATIC        |
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
| 7c. SKILL LISTINGS  CONFIGURABLE |      |
|     (project)             STATIC        |
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
| 8. CLAUDE.md CHAIN   CONFIGURABLE |     |
|    (cwd path)             STATIC        |
|    Scope: mixed (user -> local)          |
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
+-----------------------------------------+
     |
     v
 ~~~ session begins, user sends messages ~~~
     |
     v
+-----------------------------------------+
| 9. CONVERSATION      FIXED | STATIC    |
|    HISTORY                               |
|    Scope: session                        |
|                                          |
|    All prior messages + tool results     |
|    in current session                    |
|    Accumulates over time                 |
|    Auto-compressed near context limit    |
|    Reset completely on new session       |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 10. TOOL CALL        CONFIGURABLE |     |
|     RESULTS               DYNAMIC       |
|     Scope: invocation                    |
|                                          |
|     Enters context when AI invokes       |
|     a built-in tool                      |
|                                          |
|     - Bash output                        |
|     - Read file contents                 |
|     - Grep / Glob results                |
|     - Edit / Write confirmations         |
|     - Task (subagent) results            |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 11. MCP TOOL         CONFIGURABLE |     |
|     RESULTS                DYNAMIC      |
|     Scope: invocation                    |
|                                          |
|     Enters context when AI calls         |
|     an MCP tool                          |
|                                          |
|     - Canvas data                        |
|     - Perplexity responses               |
|     - Playwright snapshots               |
|     - Chrome extension reads             |
|     - IDE diagnostics                    |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 12. SKILL FULL       CONFIGURABLE |     |
|     CONTENT                DYNAMIC      |
|     Scope: invocation                    |
|                                          |
|     Full skill prompt loads only         |
|     on /skill invoke                     |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 13. DEEPER SKILL     CONFIGURABLE |     |
|     LISTINGS               DYNAMIC      |
|     Scope: invocation                    |
|                                          |
|     Skills in .claude/skills/ of         |
|     subdirectories beyond cwd --         |
|     only listed if AI traverses          |
|     into those directories               |
|                                          |
|     - diagram-generation (in context_    |
|       visualization sub-feature)         |
|     - entity-creation (in better_        |
|       ai_system/layer_0_group)           |
|     - stage_manager-workflow (in         |
|       layer_-1_99_stages)               |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 14. DEEPER           CONFIGURABLE |     |
|     CLAUDE.md FILES        DYNAMIC      |
|     Scope: invocation                    |
|                                          |
|     CLAUDE.md beyond cwd path --         |
|     only loaded if AI traverses          |
|     into those directories               |
+-----------------------------------------+
     |
     v
+-----------------------------------------+
| 15. WEB CONTENT        FIXED | DYNAMIC |
|     Scope: invocation                    |
|                                          |
|     External pages via WebFetch /        |
|     WebSearch                            |
|     User chooses what to fetch but       |
|     doesn't control the content          |
+-----------------------------------------+
```

---

<!-- section_id: "73089069-e2a6-4c2b-b3af-7eef66cd0fb8" -->
## Filesystem Reference

> Triple-click a path to select it, then Ctrl+C → Ctrl+P → Ctrl+V → Enter to open.

<!-- section_id: "d5432d01-507b-420b-bbee-256046a01ce0" -->
### Managed Scope

Managed settings:

p/etc/claude-code/managed-settings.json

Managed MCP:

/etc/claude-code/managed-mcp.json

<!-- section_id: "27864072-d003-44ff-aa2e-9acb21e72bae" -->
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

<!-- section_id: "5efee8ce-59bc-4ed7-b77e-72b5e0635ceb" -->
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

<!-- section_id: "3f6be415-1b82-4a17-97b5-c840719389e1" -->
### Local Scope

Local MCP servers (projects["cwd"].mcpServers key):

/home/dawson/.claude.json

Local settings (path varies by repo):

\<repo\>/.claude/settings.local.json

Local CLAUDE.md (path varies by repo):

\<repo\>/.claude.local.md

<!-- section_id: "a5a4da8c-8198-4def-9fc9-819a123f1a5c" -->
### Invocation Scope (examples)

Deeper skills (layer_0_group):

/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/.claude/skills/

Deeper skills (layer_-1_99_stages):

/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_-1_group/layer_-1_99_stages/.claude/skills/

---

<!-- section_id: "b111f287-185e-49be-b8e2-9cdef7707510" -->
## Summary

```
 #  | Item                    | Fixed/Config   | Static/Dynamic | Scope
----+-------------------------+----------------+----------------+------------
  1 | System prompt           | Fixed          | Static         | global
  2 | Browser security rules  | Fixed          | Static         | global
  3 | Environment detection   | Fixed          | Static         | session
  4 | Managed settings        | Configurable   | Static         | managed
  5 | Auto memory             | Configurable   | Static         | project
 6a | Built-in tool schemas   | Fixed          | Static         | global
 6b | MCP schemas (managed)   | Configurable   | Static         | managed
 6c | MCP schemas (user)      | Configurable   | Static         | user
 6d | MCP schemas (local)     | Configurable   | Static         | local
 6e | MCP schemas (project)   | Configurable   | Static         | project
 6f | MCP schemas (IDE/ext)   | Fixed          | Static         | session
 7a | Skill listings (user)   | Configurable   | Static         | user
 7b | Skill listings (plugins)| Configurable   | Static         | user
 7c | Skill listings (project)| Configurable   | Static         | project
  8 | CLAUDE.md chain (cwd)   | Configurable   | Static         | user->local
  9 | Conversation history    | Fixed          | Static         | session
 10 | Tool call results       | Configurable   | Dynamic        | invocation
 11 | MCP tool results        | Configurable   | Dynamic        | invocation
 12 | Skill full content      | Configurable   | Dynamic        | invocation
 13 | Deeper skill listings   | Configurable   | Dynamic        | invocation
 14 | Deeper CLAUDE.md files  | Configurable   | Dynamic        | invocation
 15 | Web content             | Fixed          | Dynamic        | invocation
```

---

<!-- section_id: "65bc5456-4c86-4079-84b9-5703400e8582" -->
## Key Insight

The static chain (items 1-9) is the baseline cost of every API call. Within that, items 1-3 and 9 are fixed overhead you can't reduce. Items 4-8 are where optimization matters most — every token there is sent on every single message. Items 10-14 are efficient by design, only entering context when needed.

The most impactful optimization: keep items 4-8 lean and push detail into items 10-13 (read on-demand rather than inlining in CLAUDE.md).

---

<!-- section_id: "f11749c2-92ff-4d4c-a7dd-350dc6161f4c" -->
## Traversal Behavior: CLAUDE.md vs Auto Memory

A critical difference between two configurable static items:

| Behavior | CLAUDE.md (item 8) | Auto Memory (item 5) |
|----------|---------------------|----------------------|
| **At session start** | All CLAUDE.md files from root to cwd loaded | Only the MEMORY.md for the launch directory loaded |
| **During traversal** | Additional CLAUDE.md files appear as system-reminders when AI enters new directories | No other MEMORY.md files are picked up |
| **Scope** | Hierarchical — stacks as you go deeper (user -> local) | Flat — one project directory, one memory file |
| **Global equivalent** | `~/.claude/CLAUDE.md` (manual, always loaded) | None — no global auto memory exists |

**Implication**: Learnings recorded in one project's auto memory are invisible to sessions launched from a different directory, even if the work overlaps. CLAUDE.md does not have this limitation since it chains hierarchically and traverses dynamically.

---

<!-- section_id: "5ef46a46-ee5c-4ab8-964b-f6a2d65c2140" -->
## Sources

<!-- section_id: "e6a88ac6-42b0-4cf1-810e-fe573ccb8b05" -->
### Per-Item Sources

| # | Item | Sources |
|---|------|---------|
| 1 | System prompt | [Claude Code Overview](https://code.claude.com/docs/en/overview) (fixed, hardcoded in binary) |
| 2 | Browser security rules | [Claude Code Overview](https://code.claude.com/docs/en/overview) (injected when browser tools present) |
| 3 | Environment detection | [Claude Code Overview](https://code.claude.com/docs/en/overview) (auto-detected at session start) |
| 4 | Managed settings | [Settings: Managed](https://code.claude.com/docs/en/settings#managed-settings) |
| 5 | Auto memory | [Memory](https://code.claude.com/docs/en/memory), [GH #23750](https://github.com/anthropics/claude-code/issues/23750), [Session Memory](https://claudefa.st/blog/guide/mechanics/session-memory) |
| 6a | Built-in tool schemas | [Claude Code Overview](https://code.claude.com/docs/en/overview) (hardcoded tools) |
| 6b | MCP schemas (managed) | [MCP: Managed](https://code.claude.com/docs/en/mcp#managed-mcp-servers) |
| 6c | MCP schemas (user) | [MCP: User](https://code.claude.com/docs/en/mcp#user-mcp-servers) |
| 6d | MCP schemas (local) | [MCP: Local](https://code.claude.com/docs/en/mcp#project-specific-mcp-servers), [Settings: Local](https://code.claude.com/docs/en/settings#local-settings) |
| 6e | MCP schemas (project) | [MCP: Project](https://code.claude.com/docs/en/mcp#shared-mcp-servers) |
| 6f | MCP schemas (IDE/ext) | [MCP](https://code.claude.com/docs/en/mcp) (auto-detection behavior) |
| 7a | Skill listings (user) | [Skills](https://code.claude.com/docs/en/skills), [Skills Guide PDF](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) |
| 7b | Skill listings (plugins) | [Skills](https://code.claude.com/docs/en/skills) |
| 7c | Skill listings (project) | [Skills](https://code.claude.com/docs/en/skills) |
| 8 | CLAUDE.md chain | [Memory: CLAUDE.md](https://code.claude.com/docs/en/memory#claudemd), [Settings](https://code.claude.com/docs/en/settings) |
| 9 | Conversation history | [Claude Code Overview](https://code.claude.com/docs/en/overview) (session management, auto-compression) |
| 10 | Tool call results | [Claude Code Overview](https://code.claude.com/docs/en/overview) (built-in tools) |
| 11 | MCP tool results | [MCP](https://code.claude.com/docs/en/mcp) |
| 12 | Skill full content | [Skills](https://code.claude.com/docs/en/skills) |
| 13 | Deeper skill listings | [Skills](https://code.claude.com/docs/en/skills) (directory traversal behavior) |
| 14 | Deeper CLAUDE.md files | [Memory: CLAUDE.md](https://code.claude.com/docs/en/memory#claudemd) (traversal behavior) |
| 15 | Web content | [Claude Code Overview](https://code.claude.com/docs/en/overview) (WebFetch/WebSearch tools) |

<!-- section_id: "97848bfd-f089-43e4-9991-66c73cec142b" -->
### General Sources

These sources informed the overall structure and multiple items:

- [Claude Code Settings & Scopes](https://code.claude.com/docs/en/settings) — official scope definitions (managed, user, project, local), precedence order, filesystem paths
- [Claude Code MCP Configuration](https://code.claude.com/docs/en/mcp) — MCP server scopes, managed-mcp.json, .mcp.json
- [Claude Code Memory](https://code.claude.com/docs/en/memory) — auto memory, MEMORY.md, CLAUDE.md, per-project scoping
- [Claude Code Skills](https://code.claude.com/docs/en/skills) — skill definitions, SKILL.md, scoping, invocation
- [Claude Code Overview](https://code.claude.com/docs/en/overview) — general architecture, built-in tools, system prompt
- [GitHub Issue #23750](https://github.com/anthropics/claude-code/issues/23750) — auto memory opt-in/opt-out discussion
- [Claude Code Session Memory](https://claudefa.st/blog/guide/mechanics/session-memory) — session memory rollout timeline
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) — Anthropic's official skill-building guide

<!-- section_id: "2512ddf4-3488-4711-8452-a827e60b4ed0" -->
### No Official Unified Diagram

As of February 2026, Anthropic does not publish a single unified context chain diagram. Each documentation page covers its own piece:

- [Settings](https://code.claude.com/docs/en/settings) covers scopes and precedence but not loading order
- [MCP](https://code.claude.com/docs/en/mcp) covers server configuration but not its position relative to other context
- [Memory](https://code.claude.com/docs/en/memory) covers CLAUDE.md and auto memory but not the full chain
- [Skills](https://code.claude.com/docs/en/skills) covers skill files but not when they enter context relative to everything else
- [Overview](https://code.claude.com/docs/en/overview) describes tools and capabilities but not the complete loading sequence

This diagram was assembled by cross-referencing these sources, inspecting system prompt content, and observing actual Claude Code behavior.

> **Anchor links**: Source URLs use `#fragment` anchors where the official docs support them (e.g., `#managed-settings`, `#claudemd`). If a specific anchor doesn't resolve, it will still land on the correct page.
