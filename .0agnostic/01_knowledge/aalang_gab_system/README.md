---
resource_id: "6dc50370-0c20-45fa-82e3-b8cc876172c1"
resource_type: "readme
knowledge"
resource_name: "README"
---
# AALang & GAB System - Knowledge Reference

<!-- section_id: "e56886a0-fc85-4e83-bad2-18b941885deb" -->
## Overview

AALang (Actor-based Agent Language) is a programming language designed to run entirely within LLMs. Rather than traditional compilation to machine code, AALang programs execute within the LLM's context window as structured reasoning patterns.

GAB (Generic AALang Builder) is the compiler — it takes natural language descriptions of desired agent behavior and produces AALang agent definitions in JSON-LD format.

Both are created and maintained by Professor Barney (upstream: `yenrab/AALang-Gab`).

---

<!-- section_id: "b45dab5c-078a-44c2-a99c-0129b90ca9ce" -->
## Source Location

| Property | Value |
|----------|-------|
| **Local Path** | `layer_0/layer_0_01_ai_manager_system/professor/` |
| **Fork** | `https://github.com/Dawson2025/AALang-Gab.git` |
| **Upstream** | `https://github.com/yenrab/AALang-Gab.git` |
| **Type** | Git submodule |

<!-- section_id: "cc305545-dc9d-4cae-946a-a75fa1677aff" -->
### Key Source Files

| File | Purpose |
|------|---------|
| `gab.jsonld` | Main GAB agent spec (~170KB, ~1300 lines) |
| `gab-runtime.jsonld` | Runtime behaviors (debug, decisions, transitions) |
| `gab-formats.jsonld` | Output format definitions |
| `index.jsonld` | Navigation index |
| `README.md` | User-facing documentation |

---

<!-- section_id: "fc181261-8d89-4cfa-8890-8caf5fcc5cc4" -->
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

<!-- section_id: "a46cf490-970c-4fd9-a615-30de07ca99f8" -->
## Key Concepts at a Glance

<!-- section_id: "4206b196-95d6-44fa-bb09-bf7d7573bb8a" -->
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

<!-- section_id: "99920946-8ea0-43c3-b916-59c3c9103f4e" -->
### Professor's Positioning

AALang claims to solve problems with standard prompt engineering:
- Inconsistent behavior → **formal language specification**
- Hallucinations → **explicit mode constraints and actor responsibilities**
- Hard to maintain → **version-controllable JSON-LD specifications**
- No formal structure → **n-mode-m-actor architecture**
- Hard to debug → **structured reasoning patterns, self-check actors, AATest framework**

<!-- section_id: "b882a68e-b90d-4dbc-9f2d-0f8bb80a8248" -->
### Important Caveat (from professor's README)

> "Stateful AALang tools created by GAB need significant context windows to not lose the instructions and states."

This validates our concern about JSON-LD token cost. The professor acknowledges the context window pressure.

<!-- section_id: "152afd76-cc05-4476-9f16-8bd060175210" -->
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

<!-- section_id: "6e0a02dd-99da-4737-ac89-c27fafb38228" -->
### Communication Layers

1. **Agent-to-Agent**: P2P gossip protocol between separate agents
2. **Actor-to-Actor**: Local routing within a single agent
3. **Persona-to-Persona**: Internal reasoning within an actor

---

<!-- section_id: "f1685dd2-3f84-4973-bcc8-edb71cb0aabf" -->
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
