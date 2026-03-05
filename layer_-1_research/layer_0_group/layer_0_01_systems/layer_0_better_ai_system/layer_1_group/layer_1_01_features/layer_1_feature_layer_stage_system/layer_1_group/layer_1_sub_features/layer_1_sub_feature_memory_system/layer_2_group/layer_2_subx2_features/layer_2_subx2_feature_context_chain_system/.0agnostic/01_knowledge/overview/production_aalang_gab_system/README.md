---
resource_id: "41015f14-80d7-447f-8844-2d63911e114f"
resource_type: "readme
knowledge"
resource_name: "README"
---
# AALang & GAB System - Knowledge Reference

<!-- section_id: "2e58837d-67e2-4eef-b1a7-2893fa8e51db" -->
## Overview

AALang (Actor-based Agent Language) is a programming language designed to run entirely within LLMs. Rather than traditional compilation to machine code, AALang programs execute within the LLM's context window as structured reasoning patterns.

GAB (Generic AALang Builder) is the compiler — it takes natural language descriptions of desired agent behavior and produces AALang agent definitions in JSON-LD format.

Both are created and maintained by Professor Barney (upstream: `yenrab/AALang-Gab`).

---

<!-- section_id: "ecaf1efc-07db-4f48-8779-790d9744b72b" -->
## Source Location

| Property | Value |
|----------|-------|
| **Local Path** | `layer_0/layer_0_01_ai_manager_system/professor/` |
| **Fork** | `https://github.com/Dawson2025/AALang-Gab.git` |
| **Upstream** | `https://github.com/yenrab/AALang-Gab.git` |
| **Type** | Git submodule |

<!-- section_id: "c974b235-e7a6-4132-87c4-cb112b3f15c7" -->
### Key Source Files

| File | Purpose |
|------|---------|
| `gab.jsonld` | Main GAB agent spec (~170KB, ~1300 lines) |
| `gab-runtime.jsonld` | Runtime behaviors (debug, decisions, transitions) |
| `gab-formats.jsonld` | Output format definitions |
| `index.jsonld` | Navigation index |
| `README.md` | User-facing documentation |

---

<!-- section_id: "2fb33541-18df-4fca-8430-37ba583a6f8d" -->
## Knowledge Files in This Directory

| File | Topic |
|------|-------|
| [mode_actor_pattern.md](mode_actor_pattern.md) | Core execution pattern — modes, actors, personas, state |
| [gab_compiler.md](gab_compiler.md) | How GAB works — the 4-mode compiler pipeline |
| [runtime_and_formats.md](runtime_and_formats.md) | Runtime behaviors and output format specs |
| [agent_patterns.md](agent_patterns.md) | Common patterns (4-mode-13-actor, 5-mode-15-actor) |
| [jsonld_design_vs_runtime.md](jsonld_design_vs_runtime.md) | **IMPORTANT** — Why AALang uses JSON-LD and the design-time vs run-time distinction |
| [professor_docs_analysis.md](professor_docs_analysis.md) | Analysis of professor's upstream documentation and what it resolves |

---

<!-- section_id: "ef60e3dc-1520-42a5-bef5-3c2a92e42bb3" -->
## Key Concepts at a Glance

<!-- section_id: "22a8e9a1-3498-41cf-9cfb-07fe655650ae" -->
### What Makes AALang Different (from professor's README)

- **First programming language designed to run entirely within the LLM** — not adapted from human-readable languages
- **Context-window native**: State is managed through messages in the LLM context window, not external databases
- **Semantic execution**: Mode transitions use confidence thresholds and satisfaction indicators, not control flow
- **Definition Adoption**: LLMs don't create actor instances — they ADOPT definitions dynamically (the LLM BECOMES the actor)
- **Persona-driven**: Actors can employ Senior (strategic) and Junior (execution) personas for multi-perspective reasoning
- **Graph-based**: Uses JSON-LD (linked data) format, not traditional code syntax
- **MCP and A2A ready**: Integrates with Model Context Protocol; supports Agent-to-Agent gossip-based P2P for distributed execution
- **Bounded non-determinism**: Same input produces consistently bounded (not identical) behavior across LLM instances
- **Self-check system**: Built-in quality assurance — actors can analyze their own instructions for issues

<!-- section_id: "ab01c2a1-55e6-40a1-aa74-e71fbebac449" -->
### Professor's Positioning

AALang claims to solve problems with standard prompt engineering:
- Inconsistent behavior → **formal language specification**
- Hallucinations → **explicit mode constraints and actor responsibilities**
- Hard to maintain → **version-controllable JSON-LD specifications**
- No formal structure → **n-mode-m-actor architecture**
- Hard to debug → **structured reasoning patterns, self-check actors, AATest framework**

<!-- section_id: "db6a55ab-241a-4150-bc76-ee086a31a982" -->
### Important Caveat (from professor's README)

> "Stateful AALang tools created by GAB need significant context windows to not lose the instructions and states."

This validates our concern about JSON-LD token cost. The professor acknowledges the context window pressure.

<!-- section_id: "09347b1e-c66e-4bcb-a83b-771a39676040" -->
### Core Architecture

```
Agent
├── Modes (sequential phases, e.g. Clarification → Discussion → Formalization → Generation)
│   ├── Mode Actor (Senior Persona) — strategic thinking, validation
│   └── Mode Actor (Junior Persona) — execution, implementation
├── State Actors (persist across ALL modes)
│   ├── ProductNameStateActor
│   ├── UnderstandingIndicatorsStateActor
│   ├── SatisfactionIndicatorsStateActor
│   ├── DebugModeStateActor
│   └── DecisionLogStateActor
└── Message Interface (communication layer)
```

<!-- section_id: "af10f789-0509-4e4c-83ca-669fbf208800" -->
### Communication Layers

1. **Agent-to-Agent**: P2P gossip protocol between separate agents
2. **Actor-to-Actor**: Local routing within a single agent
3. **Persona-to-Persona**: Internal reasoning within an actor

---

<!-- section_id: "8323346c-28db-4bc5-9225-4a4a3eea300a" -->
## When to Load This Knowledge

| Situation | Load |
|-----------|------|
| Understanding agent definitions | `mode_actor_pattern.md` |
| Creating new agents via GAB | `gab_compiler.md` |
| Debugging agent execution | `runtime_and_formats.md` |
| Choosing a pattern for a new agent | `agent_patterns.md` |
| General AALang overview | This file (README.md) |

---

*Knowledge area: aalang_gab_system*
*Last updated: 2026-02-07*
