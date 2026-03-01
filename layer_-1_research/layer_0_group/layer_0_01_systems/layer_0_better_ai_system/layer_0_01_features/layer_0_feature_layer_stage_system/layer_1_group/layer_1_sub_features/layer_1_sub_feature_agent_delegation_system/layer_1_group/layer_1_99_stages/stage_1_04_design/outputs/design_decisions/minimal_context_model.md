# Design Decision: Minimal Context Model

## Decision

Agents in the layer-stage hierarchy receive **minimal context by default**: their own STATIC identity, compact interface summaries of direct neighbors, and on-demand access to any context via delegation or file reads. Full context cascade is NOT used for agent-to-agent context sharing.

## Status

**Decided** — 2026-02-26

## Context

The agent delegation system organizes agents in a hierarchy (layers and stages). The question: how much parent/ancestor context does each agent need?

### The Original Assumption

Full STATIC context from every ancestor level cascades down to every descendant. A stage-04 agent in a layer-3 entity would receive STATIC from: root, layer_-1, layer_0, layer_1, layer_2, layer_3, and its own stage.

### Why Full Cascade Was Rejected

1. **Most ancestor STATIC is irrelevant**: Ancestor STATIC context contains triggers, pointers, and identity information that only matters to agents AT that level. A stage-04 design agent doesn't need to know the layer_0 root manager's triggers.

2. **Context window waste**: Deep hierarchies (7+ levels) compound context size. If each level's STATIC is ~200 tokens, an agent at depth 7 carries 1,400+ tokens of ancestor context, most unused.

3. **Multi-agent research confirms minimal is better**: CrewAI, LangGraph, and AutoGen all use selective/minimal context — none cascade full parent context to children. See `../stage_1_02_research/outputs/by_topic/multi_agent_context_patterns/README.md`.

4. **Tool cascading amplifies the problem**: Claude Code, Codex, and Gemini CLI automatically cascade CLAUDE.md files up the directory tree. If we put comprehensive content in every level's CLAUDE.md, deep agents get ALL of it automatically — making bloat even worse. See `../stage_1_02_research/outputs/by_topic/tool_context_cascading/README.md`.

## The Minimal Context Model

### Three-Layer Context Model

Each agent always has:

| Layer | Content | Loaded |
|-------|---------|--------|
| **Own STATIC** | Full identity, methodology, IS/IS NOT, triggers, current status | Always (in 0AGNOSTIC.md) |
| **Neighbor interfaces** | Compact summaries of direct parent + direct children: what they provide, what they accept, how to communicate | Always (in 0AGNOSTIC.md navigation/delegation sections) |
| **On-demand DYNAMIC** | Any context from any level, loaded when needed | On-demand (read specific files via `.0agnostic/01_knowledge/`, delegate up/down) |

### What Neighbor Interfaces Look Like

A neighbor interface summary is 2-5 lines per neighbor:

```
Parent: agent_delegation_system (../../0AGNOSTIC.md)
- Provides: domain knowledge in .0agnostic/01_knowledge/, delegation principles
- Accepts: stage reports at outputs/reports/stage_report.md
- Communicate via: stage report protocol
```

This is NOT the full parent STATIC context. It's a compact contract describing the interface.

### The Relay Pattern

Agents don't query across the hierarchy directly. Instead, they relay through neighbors:

```
Team Agent → Project Agent → Content Agent → Template Agent
(each hop is a delegation or query to a direct neighbor)
```

If a stage-04 agent needs information from three levels up, it asks its parent, who asks its parent, who asks its parent. Each relay adds context and filtering — the response back is scoped and relevant.

### What This Means for CLAUDE.md Files

Since AI coding tools cascade CLAUDE.md automatically, the content must be minimal:

- **Identity**: 1-2 lines (role, scope)
- **Navigation**: Table of parent/children/stages paths
- **Triggers**: When to load this context
- **Pointers**: Where to find on-demand resources

NOT included in CLAUDE.md: full methodology, domain knowledge, current state details, comprehensive rules. These stay in 0AGNOSTIC.md and .0agnostic/ for on-demand loading.

## Alternatives Considered

### Full STATIC Cascade

Every ancestor's STATIC context is loaded into every descendant.

**Rejected because**: Context waste compounds at depth. Most ancestor STATIC is irrelevant to descendants. Multi-agent research shows this underperforms minimal approaches.

### Full Isolation (No Shared Context)

Each agent has only its own context, with no inherited information.

**Rejected because**: Agents need SOME awareness of their neighbors — at minimum, how to delegate up/down and what interfaces exist. Full isolation forces agents to discover everything from scratch.

### Selective Cascade (Cherry-Pick Sections)

Cascade only certain sections of ancestor STATIC (e.g., identity but not triggers).

**Rejected because**: Adds complexity to the sync tooling (agnostic-sync.sh would need section-level filtering). The interface summary approach is simpler — write a compact summary once rather than filtering a long document.

## Trade-offs Accepted

1. **Agents may need more round-trips**: If an agent needs deep ancestor context, it must relay through neighbors or explicitly read files. This is slower than having it pre-loaded.

2. **Interface summaries must be maintained**: Each level needs accurate neighbor interface descriptions. If these become stale, agents may not know how to communicate with their neighbors.

3. **Cursor needs special handling**: Unlike Claude Code/Codex/Gemini CLI, Cursor doesn't cascade automatically. Cursor rules must be self-contained or use glob targeting to pull in the right context.

## Implementation Notes

### For agnostic-sync.sh

The sync tool already generates lean CLAUDE.md files from 0AGNOSTIC.md STATIC content. No changes needed — the key is ensuring 0AGNOSTIC.md STATIC sections are written with the minimal context model in mind (compact, pointer-heavy, not verbose).

### For Entity/Stage Templates

The STAGE_AGENT_TEMPLATE.md already follows this pattern:
- Identity section is compact
- Inputs table references files by path (on-demand)
- Navigation section has parent/child pointers
- Current Status is a brief summary with pointers to detail

### For the Relay Pattern

No tooling changes needed. The delegation contract already works this way:
- Manager provides: task description + directory pointer
- Agent discovers: its own methodology from 0AGNOSTIC.md
- Agent loads: parent context on-demand from `../../.0agnostic/`

## Related Decisions

- **0AGNOSTIC.md as stage identity** — the minimal context model defines WHAT goes in 0AGNOSTIC.md
- **Two-halves pattern (Principle 9)** — operational + current state, both kept lean
- **Stage reports for async communication** — the interface through which agents communicate status up
- **Scope boundary decisions (Principle 8)** — when agents need context beyond their scope, they delegate rather than pre-loading

## Cross-Stage Traceability

| Stage | Connection |
|-------|-----------|
| Stage 01 (Requirements) | need_03: agent_context_model — what each agent type knows |
| Stage 02 (Research) | `tool_context_cascading/` — how tools handle cascading |
| Stage 02 (Research) | `multi_agent_context_patterns/` — how frameworks handle shared context |
| Stage 06 (Development) | STAGE_AGENT_TEMPLATE.md, agnostic-sync.sh — already implements minimal pattern |
