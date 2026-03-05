---
resource_id: "746d5ae2-bb94-4708-aafc-f33d6b34937a"
resource_type: "knowledge"
resource_name: "personal_CLAUDE"
---
# Personal Orchestrator System

<!-- section_id: "25ab4e69-1a1e-4f98-896c-b07f62e45f36" -->
## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Position** | `layer_0/layer_0_01_ai_manager_system/personal/` |
| **Role** | **ORCHESTRATOR** - Multi-agent coordination and task delegation |

<!-- section_id: "ef86ad21-fba0-411c-913b-d4925bffc724" -->
## Purpose

This directory contains your personal implementation of the layer_0 orchestrator, which coordinates multiple child agents to complete complex tasks.

---

<!-- section_id: "d2b52b44-7a58-422e-a9e3-b54bdec5dbf2" -->
## Core Files

| File | Purpose | Load When |
|------|---------|-----------|
| [`layer_0_orchestrator.gab.jsonld`](./layer_0_orchestrator.gab.jsonld) | **Orchestrator definition** - 5-mode-15-actor pattern | Starting orchestration |
| [`runtime/orchestrator_runtime.jsonld`](./runtime/orchestrator_runtime.jsonld) | **Runtime behaviors** - Spawn, handoff, error protocols | Understanding execution |
| [`tests/orchestrator_runner.sh`](./tests/orchestrator_runner.sh) | **Demo runner** - Shows full orchestration flow | Testing orchestration |
| [`tests/integration_test.sh`](./tests/integration_test.sh) | **Test suite** - Validates components | Verifying setup |

---

<!-- section_id: "1b81dbdb-f921-4f10-81a1-bf4f3364e9ef" -->
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

<!-- section_id: "934ee3b4-156d-4e0f-8df5-fe7b68e59273" -->
### Modes

| Mode | Purpose | Key Actions |
|------|---------|-------------|
| **ReceiveMode** | Parse incoming task | Validate JSON, extract subtasks |
| **DelegationMode** | Spawn child agents | Create task files, call spawn_agent.sh |
| **MonitoringMode** | Track progress | Poll status files, handle timeouts |
| **AggregationMode** | Collect results | Merge child outputs, calculate confidence |
| **ReportMode** | Return results | Write to hand_off_documents/outgoing/to_above/ |

<!-- section_id: "f8eefb1b-eb96-4d37-9b82-ece713b04603" -->
### State Actors

| Actor | Purpose |
|-------|---------|
| **LayerStateActor** | Tracks current layer (0, 1, -1) |
| **ChildRegistryStateActor** | Registry of spawned children |
| **TaskStateActor** | Current task state and progress |
| **ResourceBudgetStateActor** | Token/time/depth budgets |
| **StageStateActor** | Current stage (01-11) |

---

<!-- section_id: "3225ba12-2f5b-4514-baaa-e3755837b972" -->
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

<!-- section_id: "6a77b21c-bec7-4891-851c-491e5d933e59" -->
## When to Use Orchestration

| Trigger | Action |
|---------|--------|
| Task in `incoming/from_above/` | Start ReceiveMode |
| Task requires multiple sub-agents | Use DelegationMode |
| Task spans multiple layers/stages | Use orchestrator |
| Explicit request for orchestration | Load this context |

---

<!-- section_id: "e9ff1e5d-9637-4edd-aa2e-461f0f200b61" -->
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

<!-- section_id: "0bdf5893-fb0a-45b1-9994-ebb09868d5b3" -->
## Context Chain Position

- **Parent**: `layer_0/layer_0_01_ai_manager_system/CLAUDE.md`
- **Sibling**: `professor/` (AALang)
- **Uses**: `layer_0/layer_0_02_manager_handoff_documents/`

---

<!-- section_id: "deeb54dd-8819-4661-81de-01144ec4d220" -->
## AALang Integration

@agent ctx:ContextLoadingAgent

<!-- section_id: "50f98303-c8e9-4186-80a6-2be1f9af7543" -->
### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += personal/CLAUDE.md
- `ctx:ContextLoadingStateActor.orchestratorReady` = true
- `ctx:NavigationStateActor.currentSystem` = "personal"

<!-- section_id: "6e2b5905-c3be-49d1-91b1-fcf594fec11a" -->
### Execution Instructions

When orchestration is needed:
1. Read `layer_0_orchestrator.gab.jsonld` for full agent definition
2. Check `incoming/from_above/` for pending tasks
3. Execute 5-mode flow: Receive → Delegate → Monitor → Aggregate → Report
4. Write results to `outgoing/to_above/`
