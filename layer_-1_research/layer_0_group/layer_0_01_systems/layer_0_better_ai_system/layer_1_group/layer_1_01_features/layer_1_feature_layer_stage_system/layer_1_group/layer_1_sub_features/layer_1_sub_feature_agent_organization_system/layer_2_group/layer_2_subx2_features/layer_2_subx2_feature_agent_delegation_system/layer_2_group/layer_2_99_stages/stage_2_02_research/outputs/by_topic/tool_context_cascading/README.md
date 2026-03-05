---
resource_id: "2fe7a58c-c875-48e6-829b-6a69382e0115"
resource_type: "readme
output"
resource_name: "README"
---
# Tool Context Cascading

## Research Question

How do the major AI coding tools handle context file cascading? Specifically: does each tool automatically walk up/down directory hierarchies loading its context file (CLAUDE.md, AGENTS.md, GEMINI.md, .cursorrules), or does each agent only see the single file in its working directory?

This matters for the agent delegation system because: if tools natively cascade, the layer-stage hierarchy can rely on that behavior for context propagation. If they don't, agents need explicit instructions to load parent context.

## Findings

### Claude Code (CLAUDE.md)

**Cascading**: YES — upward walk + on-demand downward.

- On session start, Claude Code walks from CWD upward to the filesystem root, loading every `CLAUDE.md` it finds
- All ancestor CLAUDE.md content is merged into the system prompt as static context
- Subdirectory CLAUDE.md files are loaded on-demand when the agent enters that directory
- The walk is: `CWD/CLAUDE.md` → `../CLAUDE.md` → `../../CLAUDE.md` → ... → root
- Additionally loads `~/.claude/CLAUDE.md` (user-level global) and project-specific memory

**Implication**: Full upward cascade is native. Agents at any level automatically see all parent context. This is the most natural fit for the layer-stage hierarchy.

### OpenAI Codex (AGENTS.md)

**Cascading**: YES — root-to-CWD walk.

- Codex walks from the repository root down to CWD, loading one `AGENTS.md` per directory
- The walk direction is opposite to Claude Code: root → child → grandchild → CWD
- Each file is loaded into the agent's context
- Respects `.codexignore` for excluding directories

**Implication**: Full cascade is native but in reverse direction (top-down). Same effect — agents see all ancestor context.

### Google Gemini CLI (GEMINI.md)

**Cascading**: YES — most aggressive, bidirectional BFS.

- Walks upward from CWD to root, similar to Claude Code
- Also walks downward via breadth-first search, up to 200 directories
- Uses just-in-time (JIT) loading — files discovered during BFS are loaded on-demand
- The broadest auto-discovery of any tool

**Implication**: Agents automatically see both ancestor AND descendant context. The layer-stage hierarchy's full tree is potentially visible.

### Cursor (.cursorrules / Rules)

**Cascading**: PARTIAL — glob-based targeting, not automatic walk.

- Does NOT automatically walk directories loading `.cursorrules` files
- Instead uses a rule-type targeting system: rules specify glob patterns for when they apply
- `Always` rules: loaded every time (equivalent to static context)
- `Auto Attached` rules: loaded when matched files are open (glob pattern match)
- `Agent Requested` rules: agent decides whether to load based on description
- `Manual` rules: only loaded when explicitly invoked

**Implication**: Cursor cannot rely on hierarchical cascading. Instead, each rule must explicitly declare its scope via glob patterns. This is more flexible (rules can apply to cross-cutting concerns) but doesn't naturally support the parent→child inheritance model.

## Summary Table

| Tool | Context File | Cascades? | Direction | Mechanism |
|------|-------------|-----------|-----------|-----------|
| Claude Code | `CLAUDE.md` | YES | Up (CWD→root) + down on-demand | Automatic walk |
| Codex | `AGENTS.md` | YES | Down (root→CWD) | Automatic walk |
| Gemini CLI | `GEMINI.md` | YES | Both (up + BFS down 200 dirs) | Automatic JIT |
| Cursor | `.cursorrules` / Rules | PARTIAL | N/A — glob targeting | Rule-type system |

## Design Implications

### What This Means for the Agent Delegation System

1. **Three of four tools cascade natively**: The layer-stage hierarchy can rely on automatic context propagation for Claude Code, Codex, and Gemini CLI. Only Cursor needs special handling.

2. **Cascading ≠ full context at every level**: Even though tools cascade, the CONTENT of each level's file should be minimal. Native cascading means agents accumulate ALL ancestor context. If each level's file is verbose, deep agents get overwhelmed. This supports the **minimal context model** — keep each level's file lean (identity + triggers + interface contracts), not comprehensive.

3. **Cursor's model is actually closest to the minimal context design**: Cursor's explicit glob-based targeting mirrors the "interface summaries + on-demand access" pattern. Instead of cascading everything, each rule explicitly declares what it applies to.

4. **The `.1merge/` system handles tool differences**: The agnostic-sync pipeline already generates different files for each tool. Tool-specific differences in cascading behavior can be handled by generating appropriately-scoped content per tool:
   - CLAUDE.md: lean pointers (cascading handles the rest)
   - AGENTS.md: lean pointers (same)
   - GEMINI.md: lean pointers (even more important — bidirectional BFS amplifies bloat)
   - .cursorrules: must be self-contained OR use glob targeting to pull in context

5. **The key insight**: Native cascading is an argument FOR minimal content per level, not against it. Because tools will automatically merge all ancestors, verbosity compounds. The minimal context model (own identity + neighbor interfaces + on-demand access) becomes even more important WITH cascading than without it.

## Sources

- Perplexity search: "Claude Code CLAUDE.md file cascading directory hierarchy loading" (2026-02-26)
- Perplexity search: "OpenAI Codex CLI AGENTS.md file directory cascading" (2026-02-26)
- Perplexity search: "Google Gemini CLI GEMINI.md context file cascading loading" (2026-02-26)
- Perplexity search: "Cursor AI .cursorrules context file cascading directory hierarchy" (2026-02-26)
- Perplexity ask: "AI coding tools context file cascading" (2026-02-26)

## Date

2026-02-26
