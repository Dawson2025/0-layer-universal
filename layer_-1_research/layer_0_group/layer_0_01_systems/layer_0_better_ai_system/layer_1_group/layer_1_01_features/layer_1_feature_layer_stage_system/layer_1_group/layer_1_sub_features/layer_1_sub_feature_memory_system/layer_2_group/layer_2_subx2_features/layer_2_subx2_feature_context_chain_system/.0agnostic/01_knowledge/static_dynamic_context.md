---
resource_id: "ef8edc79-2c0d-4985-9835-de24846fc3dd"
resource_type: "knowledge"
resource_name: "static_dynamic_context"
---
# Static vs Dynamic Context

**Layer**: layer_2 (Research Sub-Feature)
**Stage**: 02_research → 05_design
**Date**: 2026-02-17
**Topic**: The two dimensions of context classification — timing and ownership

---

<!-- section_id: "40eaa9c1-d2fc-4291-9ec6-2456a57d405f" -->
## Overview

Context in the layer-stage system is classified along two independent dimensions:

1. **Timing**: When does the context enter the AI model's working memory?
2. **Ownership**: Who controls whether and how the context is loaded?

These dimensions are orthogonal — any combination is possible.

---

<!-- section_id: "d423c401-395b-4816-9c98-8f04148a2c4b" -->
## Dimension 1: Timing (Static vs Dynamic)

| Type | When Loaded | Token Cost | Examples |
|------|------------|-----------|---------|
| **Static** | Every API message, automatically | Constant (per call) | CLAUDE.md chain, MCP schemas, skill listings, auto memory |
| **Dynamic** | Only when explicitly invoked | On-demand (pay per use) | Tool results, skill full content, deeper CLAUDE.md, .0agnostic/ reads |

<!-- section_id: "558b1ad3-44be-4fea-8376-9d5104bc39b1" -->
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

<!-- section_id: "2dcd5a01-3268-43b8-b4f9-7f7234275ae1" -->
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

<!-- section_id: "8306bc0b-b4da-4541-9160-1a047d19d83c" -->
## Dimension 2: Ownership (Fixed vs Configurable)

| Type | Who Controls | Can Modify? | Examples |
|------|-------------|-----------|---------|
| **Fixed** | Claude Code runtime / Anthropic | No | System prompt, tool schemas, loading order, cascade behavior |
| **Configurable** | Project author / user | Yes | CLAUDE.md content, .0agnostic/ resources, skills, MCP servers |

<!-- section_id: "373bc520-3fa7-4b4d-9a79-33fe87a5a424" -->
### Fixed Context

These items are determined by Claude Code itself and cannot be changed by the user:
- The system prompt preamble (identity, tool descriptions, safety rules)
- The order in which CLAUDE.md files are loaded (root → cwd)
- How path rules match directories
- The tool call/result format

<!-- section_id: "45d46ece-37fc-4fef-871a-500e8a295c20" -->
### Configurable Context

Everything the user can edit to change what the AI sees:
- CLAUDE.md content (via 0AGNOSTIC.md → agnostic-sync.sh)
- .0agnostic/ resources (rules, skills, knowledge, agents)
- .claude/rules/ path rules
- MCP server configurations
- Auto memory (MEMORY.md)

---

<!-- section_id: "bb7247a3-a2e5-44f9-93c5-8d32bddb945f" -->
## The 2x2 Matrix

| | **Fixed** | **Configurable** |
|---|---|---|
| **Static** | System prompt preamble, tool schemas, loading order | CLAUDE.md content, MCP schemas, skill listings, auto memory |
| **Dynamic** | Tool call format, cascade mechanics | .0agnostic/ resources, .gab.jsonld, skills content, episodic memory |

<!-- section_id: "b879726e-cc67-424c-aacf-61e679af6370" -->
### Optimization Strategy

The biggest optimization lever is the **Static + Configurable** quadrant:

| Strategy | Action | Impact |
|----------|--------|--------|
| Keep CLAUDE.md lean | Identity + triggers + pointers only | Fewer tokens per call |
| Use .0agnostic/ for detail | Push rules, knowledge, prompts to on-demand | Pay only when needed |
| Minimize MCP servers | Only enable servers you use | Fewer schema tokens |
| Prune auto memory | Keep MEMORY.md under 200 lines | Controlled token cost |

---

<!-- section_id: "6ff3c665-10d0-404d-b85d-5db5e7d87e05" -->
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

<!-- section_id: "aaa09820-8dfc-485b-bfa3-e83032ae2887" -->
## Related Documents

- Context chain default view (full diagram): `layer_3_group/.../chain_visualization/diagrams/current/context_chain/default_view.md`
- How context works: `sub_layer_2_01_knowledge_system/overview/production_context_system/HOW_CONTEXT_WORKS.md`
- Avenue web architecture: `./avenue_web_architecture.md`
