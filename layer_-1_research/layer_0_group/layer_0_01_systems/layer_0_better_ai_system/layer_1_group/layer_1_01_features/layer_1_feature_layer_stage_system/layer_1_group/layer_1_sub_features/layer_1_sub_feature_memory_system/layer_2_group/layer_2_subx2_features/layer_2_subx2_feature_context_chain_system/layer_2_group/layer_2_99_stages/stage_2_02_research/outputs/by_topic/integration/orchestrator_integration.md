---
resource_id: "add9cdf2-80f6-4c80-8e45-7d9863b7f62b"
resource_type: "output"
resource_name: "orchestrator_integration"
---
# Orchestrator Integration

<!-- section_id: "6b818d8a-bcba-492a-adb3-6e4347b45fa7" -->
## How Orchestrators Work in Our System

The layer-stage system uses AALang orchestrators for multi-agent coordination. The pattern is: one **universal orchestrator** at layer 0, with **project-level orchestrators** that inherit from it at deeper layers.

---

<!-- section_id: "8803e424-468f-4da2-8ab6-15e7432cc8d8" -->
## Layer 0 Orchestrator

**Source**: `layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`
**Pattern**: 5-mode-15-actor

<!-- section_id: "d477ed2f-ac18-4168-bb34-3ebaa04a7e72" -->
### Purpose

Coordinates multi-agent work across the entire system. When a task requires spawning multiple agents or delegating across layers, the orchestrator manages:

- Receiving and parsing the request
- Breaking it into subtasks
- Delegating to appropriate agents
- Monitoring progress
- Aggregating results
- Reporting the final outcome

<!-- section_id: "9439aecf-d3f4-4a7e-a355-6180b3ec230c" -->
### The 5-Mode Flow

```
Request comes in
       │
       ▼
┌──────────────────┐
│ Mode 1: Receive  │  Parse request, identify layer/stage, validate
│ Senior: Validates│
│ Junior: Extracts │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Mode 2: Delegate │  Break into tasks, assign to agents
│ Senior: Plans    │  (max 3 concurrent, max depth 5)
│ Junior: Creates  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Mode 3: Monitor  │  Track agent progress, handle failures
│ Senior: Evaluates│  (circuit breaker: 3 failures trips)
│ Junior: Checks   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Mode 4: Aggregate│  Collect results, merge, validate
│ Senior: Validates│
│ Junior: Merges   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Mode 5: Report   │  Format and deliver final result
│ Senior: Reviews  │
│ Junior: Formats  │
└──────────────────┘
```

<!-- section_id: "22e8202c-de3c-41be-8ade-00f8629e11bf" -->
### Spawnable Agents

The orchestrator can delegate to:
- `claude` (Claude Code sessions)
- `codex` (OpenAI Codex)
- `gemini` (Google Gemini)
- `aider` (Aider coding assistant)

<!-- section_id: "a3de955a-43f3-421d-bd2b-1e298aae05d5" -->
### Safeguards

| Safeguard | Limit | Purpose |
|-----------|-------|---------|
| Max recursion depth | 5 | No infinite delegation chains |
| No identical re-delegation | — | Can't assign the same task twice |
| Max concurrent agents | 3 | Resource control |
| Circuit breaker | 3 consecutive failures per agent type | Auto-disable failing agents |
| Hand-off documents required | — | All IPC through file system |

<!-- section_id: "0b7c3e75-ff97-4ba5-b532-043e8ae3b556" -->
### State Actors

| State Actor | Purpose |
|-------------|---------|
| `LayerStateActor` | Current layer position |
| `ChildRegistryStateActor` | Spawned agents and their status |
| `TaskStateActor` | Delegated tasks and progress |
| `ResourceBudgetStateActor` | Resource consumption tracking |
| `StageStateActor` | Current stage in workflow |

---

<!-- section_id: "39edbef4-2d7d-4b45-9b3b-a9a71044644c" -->
## Project-Level Orchestrators

**Example**: `layer_6_sub_feature_module_03/layer_6_orchestrator.gab.jsonld`
**Pattern**: 5-mode-15-actor (inherited)

<!-- section_id: "d32ebee5-f7ee-4c42-9591-9ca186b04c89" -->
### How Inheritance Works

Project orchestrators use `"extends"` to inherit from layer_0:

```json
{
  "modes": [
    {
      "name": "ReceiveMode",
      "extends": "layer_0_orchestrator.ReceiveMode",
      "overrides": {
        "scope": "project_only"
      }
    }
  ]
}
```

Each mode inherits all behavior from the universal orchestrator but adds project-specific constraints.

<!-- section_id: "3a1cd11b-aa19-46fd-acae-b46df6c464cf" -->
### Key Differences from Layer 0

| Aspect | Layer 0 | Project Level |
|--------|---------|---------------|
| Scope | Entire system | Single project |
| Children | Layer managers | Feature orchestrators |
| Cross-boundary work | Handles directly | Escalates to parent |
| State actor | StageStateActor | ProjectContextStateActor |

<!-- section_id: "646d15fb-fe7b-49cf-9be1-5b10c45d72ba" -->
### Project Orchestrator Children (Module 03 Example)

The module 03 orchestrator manages:
- 6 layer_7 feature orchestrators (one per assignment type)
- 1 features orchestrator (coordinates all features)

---

<!-- section_id: "60704a25-c9b3-4861-b319-039b15ffcd83" -->
## Hand-Off Documents as IPC

The orchestrator communicates with child agents through the file system:

```
hand_off_documents/
├── incoming/
│   ├── from_above/    ← Tasks FROM parent orchestrator
│   └── from_below/    ← Results FROM child agents
└── outgoing/
    ├── to_above/      ← Results TO parent orchestrator
    └── to_below/      ← Tasks TO child agents
```

This maps directly to the orchestrator's modes:
- **Receive mode** reads from `incoming/from_above/`
- **Delegation mode** writes to `outgoing/to_below/`
- **Monitoring mode** reads from `incoming/from_below/`
- **Report mode** writes to `outgoing/to_above/`

---

<!-- section_id: "41d5a36d-feff-43e2-bc52-655bca0fddf0" -->
## How CLAUDE.md Managers Relate to Orchestrators

Every layer has both a **CLAUDE.md** (human-readable management instructions) and potentially an **orchestrator.gab.jsonld** (AALang agent definition):

| File | Purpose | Audience |
|------|---------|----------|
| `CLAUDE.md` | Management instructions, hand-off protocols, workflows | AI agents reading context |
| `orchestrator.gab.jsonld` | Formal agent definition with modes, actors, state | AALang execution engine |

The CLAUDE.md describes WHAT to do. The orchestrator defines HOW to do it structurally.

Currently, CLAUDE.md files are the primary mechanism (Claude Code reads them automatically). Orchestrator `.jsonld` files provide a more formal specification of the same coordination patterns.

---

<!-- section_id: "03e602df-4be9-448c-bf21-b27b50393856" -->
## Current Integration Status

<!-- section_id: "1b0412a0-8ac7-4e02-8bfc-5529731b10e5" -->
### What's Defined

- Layer 0 universal orchestrator (complete 5-mode spec with safeguards)
- Project-level orchestrator template with inheritance
- Hand-off document protocol matching orchestrator modes
- Spawnable agent types (claude, codex, gemini, aider)

<!-- section_id: "57cbc353-5328-46d9-8653-f521c3003239" -->
### Open Questions

1. **Are orchestrators executed or declarative?** The `.jsonld` files are complete agent definitions, but are they loaded into an LLM for execution, or do they serve as formal documentation of the coordination pattern?

2. **How does this relate to Claude Code's agent teams?** Claude Code has its own experimental agent teams feature. How does that interact with AALang's orchestrator model?

3. **Is `spawn_agent.sh` operational?** The personal orchestrator references `spawn_agent.sh` from a research prototype. Is this script working?

4. **Circuit breaker state persistence**: The orchestrator defines a circuit breaker (3 failures trips), but where is this state maintained between sessions?

---

*Research feature: layer_0_feature_aalang_integration/orchestrator*
*Last updated: 2026-02-07*
