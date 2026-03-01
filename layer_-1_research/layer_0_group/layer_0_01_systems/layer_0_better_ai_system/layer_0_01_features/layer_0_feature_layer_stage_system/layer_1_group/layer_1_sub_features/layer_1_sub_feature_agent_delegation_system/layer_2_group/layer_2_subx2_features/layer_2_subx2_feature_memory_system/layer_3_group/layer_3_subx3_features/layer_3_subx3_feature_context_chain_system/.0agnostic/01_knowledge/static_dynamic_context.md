# Static vs Dynamic Context

**Layer**: layer_2 (Research Sub-Feature)
**Stage**: 02_research → 05_design
**Date**: 2026-02-17
**Topic**: The two dimensions of context classification — timing and ownership

---

## Overview

Context in the layer-stage system is classified along two independent dimensions:

1. **Timing**: When does the context enter the AI model's working memory?
2. **Ownership**: Who controls whether and how the context is loaded?

These dimensions are orthogonal — any combination is possible.

---

## Dimension 1: Timing (Static vs Dynamic)

| Type | When Loaded | Token Cost | Examples |
|------|------------|-----------|---------|
| **Static** | Every API message, automatically | Constant (per call) | CLAUDE.md chain, MCP schemas, skill listings, auto memory |
| **Dynamic** | Only when explicitly invoked | On-demand (pay per use) | Tool results, skill full content, deeper CLAUDE.md, .0agnostic/ reads |

### Static Context Budget

Static context is the "tax" paid on every single API call:

```
CLAUDE.md chain:     ~2,000 tokens (varies by depth)
MCP schemas:         ~3,000 tokens (perplexity, canvas, playwright, chrome)
Skill listings:      ~1,500 tokens (entity-creation, stage-workflow, etc.)
Auto memory:         ~800 tokens (MEMORY.md, first 200 lines)
Managed settings:    ~200 tokens
                     ─────────
Total static:        ~7,500 tokens per API call
```

### Dynamic Context Loading

Dynamic context only costs tokens when used:

```
Read 0AGNOSTIC.md:    ~100 tokens (lean by design)
Read .gab.jsonld:     ~2,000 tokens (full GAB with modes/actors)
Read .integration.md: ~200 tokens (summary)
Read a rule:          ~150 tokens (focused)
Read a skill:         ~300 tokens (on invocation)
Read episodic memory: ~500 tokens (session history)
```

---

## Dimension 2: Ownership (Fixed vs Configurable)

| Type | Who Controls | Can Modify? | Examples |
|------|-------------|-----------|---------|
| **Fixed** | Claude Code runtime / Anthropic | No | System prompt, tool schemas, loading order, cascade behavior |
| **Configurable** | Project author / user | Yes | CLAUDE.md content, .0agnostic/ resources, skills, MCP servers |

### Fixed Context

These items are determined by Claude Code itself and cannot be changed by the user:
- The system prompt preamble (identity, tool descriptions, safety rules)
- The order in which CLAUDE.md files are loaded (root → cwd)
- How path rules match directories
- The tool call/result format

### Configurable Context

Everything the user can edit to change what the AI sees:
- CLAUDE.md content (via 0AGNOSTIC.md → agnostic-sync.sh)
- .0agnostic/ resources (rules, skills, knowledge, agents)
- .claude/rules/ path rules
- MCP server configurations
- Auto memory (MEMORY.md)

---

## The 2x2 Matrix

| | **Fixed** | **Configurable** |
|---|---|---|
| **Static** | System prompt preamble, tool schemas, loading order | CLAUDE.md content, MCP schemas, skill listings, auto memory |
| **Dynamic** | Tool call format, cascade mechanics | .0agnostic/ resources, .gab.jsonld, skills content, episodic memory |

### Optimization Strategy

The biggest optimization lever is the **Static + Configurable** quadrant:

| Strategy | Action | Impact |
|----------|--------|--------|
| Keep CLAUDE.md lean | Identity + triggers + pointers only | Fewer tokens per call |
| Use .0agnostic/ for detail | Push rules, knowledge, prompts to on-demand | Pay only when needed |
| Minimize MCP servers | Only enable servers you use | Fewer schema tokens |
| Prune auto memory | Keep MEMORY.md under 200 lines | Controlled token cost |

---

## Context Flow Diagram

```
┌─────────────────────────────────────────────────────┐
│                  STATIC CONTEXT                     │
│  (loaded into every API message automatically)      │
│                                                     │
│  ┌─────────────┐  ┌──────────┐  ┌──────────────┐   │
│  │ CLAUDE.md   │  │ MCP      │  │ Skill        │   │
│  │ chain       │  │ schemas  │  │ listings     │   │
│  │ (cascade)   │  │ (all)    │  │ (names only) │   │
│  └──────┬──────┘  └──────────┘  └──────────────┘   │
│         │                                           │
│  ┌──────┴──────┐  ┌──────────────────────────┐      │
│  │ Auto memory │  │ Managed settings         │      │
│  │ (MEMORY.md) │  │ (admin-deployed)         │      │
│  └─────────────┘  └──────────────────────────┘      │
└─────────────────────────────────────────────────────┘
                         │
              session begins, user chats
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│                 DYNAMIC CONTEXT                     │
│  (enters only when agent explicitly invokes)        │
│                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │
│  │ Tool results │  │ MCP results  │  │ Skill    │  │
│  │ (Read, Bash) │  │ (perplexity) │  │ content  │  │
│  └──────────────┘  └──────────────┘  └──────────┘  │
│                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │
│  │ Deeper       │  │ 0AGNOSTIC    │  │ .0agno-  │  │
│  │ CLAUDE.md    │  │ chain walk   │  │ stic/    │  │
│  └──────────────┘  └──────────────┘  └──────────┘  │
│                                                     │
│  ┌──────────────┐  ┌──────────────┐                 │
│  │ .gab.jsonld  │  │ Episodic     │                 │
│  │ (via jq)     │  │ memory       │                 │
│  └──────────────┘  └──────────────┘                 │
└─────────────────────────────────────────────────────┘
```

---

## Related Documents

- Context chain default view (full diagram): `layer_4_group/.../chain_visualization/diagrams/current/context_chain/default_view.md`
- How context works: `sub_layer_3_01_knowledge_system/overview/production_context_system/HOW_CONTEXT_WORKS.md`
- Avenue web architecture: `./avenue_web_architecture.md`
