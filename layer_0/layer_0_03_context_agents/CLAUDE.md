# Context Agents

## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Position** | `layer_0/layer_0_03_context_agents/` |
| **Role** | **CONTEXT LOADING** - Agents that manage context traversal and loading |

## Purpose

This directory contains agents that handle context loading across the layer-stage system. They ensure agents properly understand their position and have access to relevant rules, knowledge, and configurations.

---

## Core Files

| File | Purpose | Load When |
|------|---------|-----------|
| [`context_loading.gab.jsonld`](./context_loading.gab.jsonld) | **Context loading agent** - 4-mode-13-actor pattern (via jq) | Precise mode constraints |
| [`context_loading.integration.md`](./context_loading.integration.md) | **Readable summary** - auto-generated from .gab.jsonld | Quick reference (same base name) |
| [`ARCHITECTURE.md`](./ARCHITECTURE.md) | **Architecture overview** - Design decisions and patterns | Understanding the system |

---

## 4-Mode-13-Actor Pattern

The context loading agent uses a 4-mode pattern with 8 mode actors and 5 state actors:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      CONTEXT LOADING EXECUTION                          │
│                                                                         │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐      │
│  │ LOADING   │───►│VALIDATION │───►│PROPAGATION│───►│ DELIVERY  │      │
│  │   MODE    │    │   MODE    │    │   MODE    │    │   MODE    │      │
│  │           │    │           │    │           │    │           │      │
│  │ • Find    │    │ • Check   │    │ • Inherit │    │ • Deliver │      │
│  │   files   │    │   schema  │    │   rules   │    │   context │      │
│  │ • Parse   │    │ • Validate│    │ • Apply   │    │ • Update  │      │
│  │   content │    │   required│    │   overrides│   │   state   │      │
│  └───────────┘    └───────────┘    └───────────┘    └───────────┘      │
│                                                                         │
│  State Actors (persist across all modes):                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ ContextLoadingStateActor │ NavigationStateActor │ ...           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Modes

| Mode | Purpose | Key Actions |
|------|---------|-------------|
| **LoadingMode** | Find and parse files | Traverse directories, read CLAUDE.md files |
| **ValidationMode** | Validate content | Check required fields, verify schema |
| **PropagationMode** | Apply inheritance | Merge parent context, handle overrides |
| **DeliveryMode** | Deliver context | Update state actors, make context available |

### State Actors

| Actor | Purpose |
|-------|---------|
| **ContextLoadingStateActor** | Tracks loaded files, rules awareness |
| **NavigationStateActor** | Current depth, path, parent reference |
| **LayerStateActor** | Current layer (0, 1, -1) |
| **StageStateActor** | Current stage (01-11) |
| **ConfidenceStateActor** | Confidence in loaded context |

---

## Context Chain

The context loading agent traverses this chain:

```
~/.claude/CLAUDE.md              (Position 1: Global)
         │
         ▼
~/CLAUDE.md                      (Position 2: User Root)
         │
         ▼
~/dawson-workspace/CLAUDE.md     (Position 3: Workspace)
         │
         ▼
.../code/CLAUDE.md               (Position 4: Code Root)
         │
         ▼
.../0_layer_universal/CLAUDE.md  (Position 5: Layer System)
         │
    ┌────┼────┬────────┐
    ▼    ▼    ▼        ▼
layer_0  layer_1  layer_-1  ...
```

---

## Integration with AI System

The context agents work with the AI Manager System:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌─────────────────────┐     ┌─────────────────────┐       │
│  │   CONTEXT AGENTS    │────►│   AI MANAGER SYSTEM │       │
│  │                     │     │                     │       │
│  │  Provides:          │     │  Uses:              │       │
│  │  • Loaded context   │     │  • Context for      │       │
│  │  • Navigation state │     │    orchestration    │       │
│  │  • Rule awareness   │     │  • Layer/stage info │       │
│  └─────────────────────┘     └─────────────────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Context Chain Position

- **Parent**: `layer_0/CLAUDE.md`
- **Siblings**:
  - `layer_0/layer_0_01_ai_manager_system/` (AI system)
  - `layer_0/layer_0_02_manager_handoff_documents/` (IPC)

---

## AALang Integration

@agent ctx:ContextLoadingAgent

### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += layer_0_03_context_agents/CLAUDE.md
- `ctx:ContextLoadingStateActor.contextAgentAwareness` = true

### Automatic Behavior

The context loading agent should automatically:
1. Traverse CLAUDE.md chain on session start
2. Update state actors with loaded context
3. Propagate inherited rules to child contexts
4. Handle @override markers appropriately
