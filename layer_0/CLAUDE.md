# Layer 0 - Universal

## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Role** | **UNIVERSAL LAYER** - Rules, knowledge, and systems that apply to ALL projects |

## Purpose

Layer 0 contains everything that applies universally across all projects, features, and work. This includes the AI system, orchestration, context loading, and foundational rules.

---

## Directory Structure

```
layer_0/
├── CLAUDE.md                              ← You are here
│
├── layer_0_01_ai_manager_system/          ← AI SYSTEM ROOT
│   ├── CLAUDE.md
│   ├── professor/                         ← AALang/GAB (submodule)
│   │   ├── CLAUDE.md
│   │   ├── gab.jsonld                     ← Main language spec
│   │   ├── gab-runtime.jsonld             ← Runtime spec
│   │   └── gab-formats.jsonld             ← Format definitions
│   └── personal/                          ← Your orchestrator
│       ├── CLAUDE.md
│       ├── layer_0_orchestrator.gab.jsonld      ← Agent definition
│       ├── layer_0_orchestrator.integration.md  ← Readable summary (auto-generated)
│       └── runtime/orchestrator_runtime.jsonld
│
├── layer_0_02_manager_handoff_documents/  ← AGENT IPC
│   ├── CLAUDE.md
│   ├── incoming/                          ← Tasks & results TO this layer
│   ├── outgoing/                          ← Tasks & results FROM this layer
│   └── status/                            ← Child agent tracking
│
├── layer_0_03_context_agents/             ← CONTEXT LOADING
│   ├── CLAUDE.md
│   ├── context_loading.gab.jsonld              ← Agent definition
│   └── context_loading.integration.md          ← Readable summary (auto-generated)
│
├── layer_0_04_sub_layers/                 ← FOUNDATIONAL CONTENT
│   ├── sub_layer_0_01_knowledge_system/
│   ├── sub_layer_0_02_principles/
│   ├── sub_layer_0_03_rules/
│   ├── sub_layer_0_04_protocols/
│   └── sub_layer_0_05+_setup_dependant_hierarchy/
│
└── layer_0_99_stages/                     ← STAGE-SPECIFIC CONTENT
    ├── stage_0_01_request_gathering/
    ├── stage_0_02_research/
    └── ...
```

---

## Key Systems

### 1. AI Manager System (`layer_0_01_ai_manager_system/`)

The core AI capabilities:

| Component | Location | Purpose |
|-----------|----------|---------|
| **Professor (AALang)** | `professor/` | AI language, Mode-Actor patterns, GAB compiler |
| **Personal (Orchestrator)** | `personal/` | Multi-agent coordination, task delegation |

**Load when**: Understanding AI patterns, creating agents, orchestrating tasks

### 2. Hand-off Documents (`layer_0_02_manager_handoff_documents/`)

File-based inter-process communication:

| Directory | Purpose |
|-----------|---------|
| `incoming/from_above/` | Tasks from parent/user |
| `incoming/from_below/` | Results from child agents |
| `outgoing/to_above/` | Results to parent/user |
| `outgoing/to_below/` | Tasks to child agents |
| `status/` | Child agent status tracking |

**Load when**: Multi-agent tasks, orchestration, checking pending work

### 3. Context Agents (`layer_0_03_context_agents/`)

Context loading and traversal:

- Uses 4-mode-13-actor pattern
- Traverses CLAUDE.md chain
- Manages state actors for context tracking
- **Summary**: Read `context_loading.integration.md` (same base name as the `.gab.jsonld`)

**Load when**: Understanding context loading, debugging context issues

### 4. Sub-layers (`layer_0_04_sub_layers/`)

Foundational content organized by type:

| Sub-layer | Content |
|-----------|---------|
| `sub_layer_0_01_knowledge_system/` | Reference knowledge |
| `sub_layer_0_02_principles/` | Guiding principles |
| `sub_layer_0_03_rules/` | Mandatory rules |
| `sub_layer_0_04_protocols/` | Standard protocols |
| `sub_layer_0_05+_setup_*` | Setup-dependent content |

---

## Agent Context Convention

Each `.gab.jsonld` has a matching `.integration.md` (same base name, auto-generated):
- `layer_0_orchestrator.gab.jsonld` → `layer_0_orchestrator.integration.md`
- `context_loading.gab.jsonld` → `context_loading.integration.md`

Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints.

---

## Session Start Protocol

When starting a session in layer_0:

```
1. Load this CLAUDE.md
         │
         ▼
2. Identify task type
         │
    ┌────┴────┬────────────┬─────────────┐
    ▼         ▼            ▼             ▼
  AI Work   Orchestration  Context    Rules/Knowledge
    │         │            │             │
    ▼         ▼            ▼             ▼
  Load      Load         Load          Load
professor/ personal/  context_agents/ sub_layers/
         │
         ▼
3. Check hand_off_documents/incoming/
         │
         ▼
4. Begin work with full context
```

---

## Integration Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           LAYER 0 INTEGRATION                           │
│                                                                         │
│   ┌───────────────────────────────────────────────────────────────┐    │
│   │                    AI MANAGER SYSTEM                          │    │
│   │  ┌─────────────────────┐     ┌─────────────────────┐         │    │
│   │  │     PROFESSOR       │     │      PERSONAL       │         │    │
│   │  │   (AALang/GAB)      │────►│   (Orchestrator)    │         │    │
│   │  └─────────────────────┘     └──────────┬──────────┘         │    │
│   └──────────────────────────────────────────┼───────────────────┘    │
│                                              │                         │
│                                              ▼                         │
│   ┌───────────────────────────────────────────────────────────────┐   │
│   │                 HAND-OFF DOCUMENTS                            │   │
│   │  incoming/ ◄──── tasks from above, results from below        │   │
│   │  outgoing/ ────► results to above, tasks to below            │   │
│   └───────────────────────────────────────────────────────────────┘   │
│                                              │                         │
│                    ┌─────────────────────────┘                         │
│                    ▼                                                   │
│   ┌────────────────────────┐     ┌────────────────────────────────┐   │
│   │    CONTEXT AGENTS      │     │         SUB-LAYERS             │   │
│   │  • Load CLAUDE.md chain│     │  • Knowledge  • Principles     │   │
│   │  • Track state actors  │     │  • Rules      • Protocols      │   │
│   └────────────────────────┘     └────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Context Chain Position

- **Parent**: `0_layer_universal/CLAUDE.md`
- **Children**:
  - `layer_0_01_ai_manager_system/CLAUDE.md`
  - `layer_0_02_manager_handoff_documents/CLAUDE.md`
  - `layer_0_03_context_agents/CLAUDE.md`
  - `layer_0_04_sub_layers/CLAUDE.md`

---

## Agnostic System

This directory uses the agnostic system for tool-independent context:

| Component | Purpose |
|-----------|---------|
| `0AGNOSTIC.md` | Source of truth — edit this for context changes |
| `.0agnostic/` | On-demand resources (rules, skills, agents, knowledge, scripts) |
| `agnostic-sync.sh` | Regenerates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md |
| `.1merge/` | Tool-specific overrides (not yet set up for layer_0) |

**Note**: This `CLAUDE.md` contains hand-crafted Claude-specific content (directory structure, integration flows). Until a `.1merge/` is set up, do NOT regenerate via `agnostic-sync.sh` — edit manually instead.

---

## AALang Integration

@agent ctx:ContextLoadingAgent

### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += layer_0/CLAUDE.md
- `ctx:LayerStateActor.currentLayer` = 0
- `ctx:NavigationStateActor.inLayerSystem` = true

### Available Resources

After loading layer_0 context:
1. AI system available at `layer_0_01_ai_manager_system/`
2. Hand-off documents at `layer_0_02_manager_handoff_documents/`
3. Context agents at `layer_0_03_context_agents/`
4. Rules and knowledge at `layer_0_04_sub_layers/`

### Next Steps

Based on task:
- **AI/agent work** → Load `layer_0_01_ai_manager_system/CLAUDE.md`
- **Multi-agent** → Load `personal/CLAUDE.md` + check `incoming/`
- **Rules/compliance** → Load `layer_0_04_sub_layers/sub_layer_0_03_rules/`
