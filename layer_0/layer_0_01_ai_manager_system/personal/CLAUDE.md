<!-- derived_from: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac" -->
# Personal Orchestrator System

## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Position** | `layer_0/layer_0_01_ai_manager_system/personal/` |
| **Role** | **ORCHESTRATOR** - Multi-agent coordination and task delegation |

## Purpose

This directory contains your personal implementation of the layer_0 orchestrator, which coordinates multiple child agents to complete complex tasks.

---

## Core Files

| File | Purpose | Load When |
|------|---------|-----------|
| [`layer_0_orchestrator.gab.jsonld`](./layer_0_orchestrator.gab.jsonld) | **Orchestrator definition** - 5-mode-15-actor pattern | Starting orchestration |
| [`runtime/orchestrator_runtime.jsonld`](./runtime/orchestrator_runtime.jsonld) | **Runtime behaviors** - Spawn, handoff, error protocols | Understanding execution |
| [`tests/orchestrator_runner.sh`](./tests/orchestrator_runner.sh) | **Demo runner** - Shows full orchestration flow | Testing orchestration |
| [`tests/integration_test.sh`](./tests/integration_test.sh) | **Test suite** - Validates components | Verifying setup |

---

## 5-Mode-15-Actor Pattern

The orchestrator uses a 5-mode pattern with 10 mode actors and 5 state actors:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ORCHESTRATOR EXECUTION                          │
│                                                                         │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────┐ │
│  │ RECEIVE   │─►│DELEGATION │─►│MONITORING │─►│AGGREGATION│─►│REPORT │ │
│  │ MODE      │  │   MODE    │  │   MODE    │  │   MODE    │  │ MODE  │ │
│  │           │  │           │  │           │  │           │  │       │ │
│  │ • Parse   │  │ • Split   │  │ • Poll    │  │ • Collect │  │• Write│ │
│  │   task    │  │   task    │  │   status  │  │   results │  │ result│ │
│  │ • Validate│  │ • Spawn   │  │ • Handle  │  │ • Merge   │  │• Send │ │
│  │           │  │   agents  │  │   errors  │  │   data    │  │ up    │ │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  └───────┘ │
│                                                                         │
│  State Actors (persist across all modes):                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ LayerStateActor │ ChildRegistryActor │ TaskStateActor │ ...     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Modes

| Mode | Purpose | Key Actions |
|------|---------|-------------|
| **ReceiveMode** | Parse incoming task | Validate JSON, extract subtasks |
| **DelegationMode** | Spawn child agents | Create task files, call spawn_agent.sh |
| **MonitoringMode** | Track progress | Poll status files, handle timeouts |
| **AggregationMode** | Collect results | Merge child outputs, calculate confidence |
| **ReportMode** | Return results | Write to hand_off_documents/outgoing/to_above/ |

### State Actors

| Actor | Purpose |
|-------|---------|
| **LayerStateActor** | Tracks current layer (0, 1, -1) |
| **ChildRegistryStateActor** | Registry of spawned children |
| **TaskStateActor** | Current task state and progress |
| **ResourceBudgetStateActor** | Token/time/depth budgets |
| **StageStateActor** | Current stage (01-11) |

---

## Hand-off Documents

Communication with parent/children uses file-based IPC:

```
layer_0/layer_0_02_manager_handoff_documents/
├── incoming/
│   ├── from_above/          ← Tasks from parent/user
│   │   └── task_001.json
│   └── from_below/          ← Results from children
│       └── child_xxx/result.json
├── outgoing/
│   ├── to_above/            ← Results to parent/user
│   │   └── result_001.json
│   └── to_below/            ← Tasks to children
│       └── child_xxx/task.json
└── status/
    └── child_xxx.json       ← Child status tracking
```

---

## When to Use Orchestration

| Trigger | Action |
|---------|--------|
| Task in `incoming/from_above/` | Start ReceiveMode |
| Task requires multiple sub-agents | Use DelegationMode |
| Task spans multiple layers/stages | Use orchestrator |
| Explicit request for orchestration | Load this context |

---

## Spawning Agents

The orchestrator uses `spawn_agent.sh` from the research prototype:

```bash
# Location
layer_-1_research/.../prototype/spawn_agent.sh

# Usage
spawn_agent.sh -D -w /path/to/0_layer_universal claude task.json

# Options
-D              # Dynamic timeout (scales with task complexity)
-w DIR          # Working directory (0_layer_universal root)
-t SECONDS      # Static timeout override
```

---

## Context Chain Position

- **Parent**: `layer_0/layer_0_01_ai_manager_system/CLAUDE.md`
- **Sibling**: `professor/` (AALang)
- **Uses**: `layer_0/layer_0_02_manager_handoff_documents/`

---

## AALang Integration

@agent ctx:ContextLoadingAgent

### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += personal/CLAUDE.md
- `ctx:ContextLoadingStateActor.orchestratorReady` = true
- `ctx:NavigationStateActor.currentSystem` = "personal"

### Execution Instructions

When orchestration is needed:
1. Read `layer_0_orchestrator.gab.jsonld` for full agent definition
2. Check `incoming/from_above/` for pending tasks
3. Execute 5-mode flow: Receive → Delegate → Monitor → Aggregate → Report
4. Write results to `outgoing/to_above/`
