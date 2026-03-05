---
resource_id: "2bdda6f2-a002-4c68-a24b-58defca92976"
resource_type: "document"
resource_name: "cursor_capabilities"
---
# Cursor IDE — AI Capabilities Reference

*Last updated: 2026-02-24*

<!-- section_id: "77843456-0d8a-41db-b698-d24ffa43d32f" -->
## Overview

Cursor is a VS Code-based AI coding IDE. It wraps VS Code with AI agent capabilities including Agent mode, Plan mode, rules system, hooks, background agents, and MCP server support.

<!-- section_id: "fab62589-30e2-4b09-9117-c52387abe91a" -->
## Key AI Features

<!-- section_id: "f81b829b-5570-45c2-98a5-b94aa36ae722" -->
### 1. Agent Mode

Primary AI interaction mode. Activated via Cmd+. (Mac) or Ctrl+. (Linux/Windows).

- Auto-pulls context from codebase
- Executes terminal commands
- Edits files autonomously
- Spawns subagents for parallel work (v2.0+)
- Can run multiple agents simultaneously

<!-- section_id: "86f7b924-0c6f-4f5b-84cb-12b5e734c447" -->
### 2. Plan Mode

Structured planning before implementation:
- Agent creates a step-by-step plan
- User reviews and approves
- Agent executes the approved plan
- Supports iterative refinement

<!-- section_id: "c53fa2fb-3678-4afd-97ee-0b2cb4124a93" -->
### 3. Rules System (Context Delivery)

Four rule types, in priority order:

| Type | Location | Scope | Applied |
|------|----------|-------|---------|
| Team Rules | Dashboard (Team/Enterprise) | Org-wide | Always (enforced) |
| Project Rules | `.cursor/rules/*.mdc` | Per-repo | See application types |
| User Rules | Cursor Settings | Per-machine | Always |
| AGENTS.md | Repo root | Per-repo | By agent |

#### .mdc File Format

Project rules use `.mdc` files with optional YAML frontmatter:

```
---
description: Explains rule purpose for intelligent application
globs: "src/**/*.ts"
alwaysApply: false
---

# Rule content in markdown

Your instructions here...
```

#### Application Types

| Type | Behavior |
|------|----------|
| Always Apply | Included in every chat session |
| Apply Intelligently | Agent decides based on `description` field |
| Apply to Specific Files | Activates when files match `globs` pattern |
| Apply Manually | Only when user writes `@rule-name` in chat |

#### Directory Structure

```
.cursor/
  rules/
    rule-name.mdc          # With frontmatter
    simple-rule.md          # Plain markdown (no frontmatter)
    frontend/
      components.md         # Hierarchical organization
```

<!-- section_id: "2c216deb-8847-4e5d-9ecc-4dfce3e6893c" -->
### 4. .cursorrules (DEPRECATED)

Legacy single-file approach at repo root. Still functional but deprecated.
- Agent mode may ignore `.cursorrules` — use `.mdc` files instead
- Migration: convert content to `.cursor/rules/*.mdc`

<!-- section_id: "11696c46-fbd8-42c5-9efc-b751d4675281" -->
### 5. AGENTS.md

Simple markdown file at repo root for basic agent instructions.
- Plain markdown, no frontmatter needed
- Lower priority than Project Rules and Team Rules
- Good for lightweight, portable agent configuration

<!-- section_id: "b0a44452-eb25-4050-ac40-0b829eb8e9f8" -->
### 6. Onboard / Demo Testing

Cursor's "demos not diffs" feature (cursor.com/onboard):
- Connects to a repository
- Takes screenshots and video recordings of changes
- Captures logs for verification
- Enables visual review of AI-generated changes

<!-- section_id: "29fd4f0c-27e7-4180-bb37-6c0272460fc0" -->
### 7. MCP Server Support

Cursor supports Model Context Protocol servers:
- Configure in Cursor settings
- Provides additional tools to the AI agent
- Same MCP servers can be shared across Cursor and Claude Code

<!-- section_id: "bb31de82-0994-4da2-99bf-b6a140fa55f4" -->
### 8. Hooks

Pre/post execution hooks for agent actions:
- Trigger on file changes, terminal commands, etc.
- Similar to Claude Code's hook system

<!-- section_id: "fd24a968-79f4-4ab6-8b11-7fbaefd70cb7" -->
### 9. Background Agents

Long-running agents that work in the background:
- Continue working while you do other things
- Report results when complete

<!-- section_id: "c0f78ada-3a04-4819-ab9b-3aba913d8f08" -->
## Native Tools Available to Cursor Agent

| Tool | Purpose |
|------|---------|
| `codebase_search` | Semantic search — understands intent |
| `grep` | Fast exact text/pattern matching |
| `read_file` | Read files with offset/limit support |
| `write` | Create or overwrite files |
| `search_replace` | Exact string replacements |
| `edit_notebook` | Jupyter notebook editing |
| `run_terminal_cmd` | Terminal command execution |
| `glob_file_search` | File system pattern matching |
| `list_dir` | Directory listing |
| `todo_write` | TODO management / task tracking |
| `read_lints` | Linter error detection |
| `web_search` | External information lookup |

<!-- section_id: "3590eca4-c2f5-4246-81bf-c7bf4a4c3fc8" -->
## Layer-Stage System Integration

<!-- section_id: "e87d3369-3ef6-4ad6-b5b9-719e9960508d" -->
### How agnostic-sync.sh Maps to Cursor

| agnostic-sync.sh Output | Cursor Reads |
|--------------------------|-------------|
| `.cursorrules` | Legacy format — lean: Identity + Navigation sections |
| `.cursor/rules/*.mdc` | Modern format (not yet generated by sync) |

<!-- section_id: "75aeef82-27c4-48b6-b392-3542d7e7bdb8" -->
### Migration Path

Current state: `agnostic-sync.sh` generates `.cursorrules` (lean format).
Future state: Generate `.cursor/rules/*.mdc` files with proper frontmatter.

Proposed mapping:
- `0AGNOSTIC.md` Identity → `.cursor/rules/identity.mdc` (alwaysApply: true)
- `0AGNOSTIC.md` Triggers → `.cursor/rules/triggers.mdc` (alwaysApply: true)
- `.0agnostic/02_rules/static/` → `.cursor/rules/static/` (alwaysApply: true)
- `.0agnostic/02_rules/dynamic/` → `.cursor/rules/dynamic/` (apply intelligently)
- Hot promoted rules → `.cursor/rules/promoted.mdc` (alwaysApply: true)

<!-- section_id: "704a4cd0-eb5f-4906-870f-6e14365ef6cb" -->
## Sources

- [Cursor Rules Docs](https://cursor.com/docs/context/rules)
- [Cursor AI Review 2026](https://prismic.io/blog/cursor-ai)
- [Cursor Best Practices](https://github.com/digitalchild/cursor-best-practices)
- [Cursor Agent Mode .mdc Guide](https://dev.to/nedcodes/cursor-agent-mode-ignores-cursorrules-use-mdc-instead-5flb)
- [Cursor Rules Guide](https://design.dev/guides/cursor-rules/)
