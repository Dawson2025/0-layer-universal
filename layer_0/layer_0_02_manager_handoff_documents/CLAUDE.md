# Manager Hand-off Documents

## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Position** | `layer_0/layer_0_02_manager_handoff_documents/` |
| **Role** | **IPC DIRECTORY** - File-based inter-process communication for agents |

## Purpose

This directory provides the communication infrastructure for multi-agent orchestration. All agent-to-agent communication goes through files in this directory.

---

## Directory Structure

```
layer_0_02_manager_handoff_documents/
├── CLAUDE.md              ← You are here
├── incoming/              ← Messages TO this agent
│   ├── from_above/        ← Tasks from parent/user
│   │   └── task_001.json
│   └── from_below/        ← Results from child agents
│       ├── child_xxx/
│       │   ├── result.json
│       │   ├── stdout.log
│       │   └── stderr.log
│       └── child_yyy/
│           └── result.json
├── outgoing/              ← Messages FROM this agent
│   ├── to_above/          ← Results to parent/user
│   │   └── result_001.json
│   └── to_below/          ← Tasks to child agents
│       ├── child_xxx/
│       │   ├── task.json
│       │   └── prompt.txt
│       └── child_yyy/
│           └── task.json
└── status/                ← Agent status tracking
    ├── child_xxx.json
    └── child_yyy.json
```

---

## Communication Protocol

### 4-Direction Flow

```
                    ┌─────────────────┐
                    │  PARENT/USER    │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 │
    ┌─────────────┐   ┌─────────────┐         │
    │ from_above/ │   │  to_above/  │         │
    │ (incoming)  │   │ (outgoing)  │         │
    └──────┬──────┘   └──────▲──────┘         │
           │                 │                 │
           │    ┌────────────┴────────────┐   │
           │    │     THIS AGENT          │   │
           │    │   (layer_0 orchestrator)│   │
           │    └────────────┬────────────┘   │
           │                 │                 │
    ┌──────▼──────┐   ┌──────┴──────┐         │
    │  to_below/  │   │ from_below/ │         │
    │ (outgoing)  │   │ (incoming)  │         │
    └──────┬──────┘   └──────▲──────┘         │
           │                 │                 │
           ▼                 │                 │
    ┌─────────────────────────────────────────┘
    │         CHILD AGENTS
    │  ┌─────────┐  ┌─────────┐  ┌─────────┐
    │  │ child_a │  │ child_b │  │ child_c │
    │  └─────────┘  └─────────┘  └─────────┘
```

---

## File Formats

### Task File (to_below/{child_id}/task.json)

```json
{
  "taskId": "subtask_001",
  "parentTaskId": "orchestrated_001",
  "description": "Analyze the rules directory",
  "context": {
    "layer": 0,
    "stage": "02_research",
    "targetPath": "layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/"
  },
  "priority": "normal",
  "timeout": 300
}
```

### Result File (from_below/{child_id}/result.json)

```json
{
  "taskId": "subtask_001",
  "status": "completed",
  "result": {
    "summary": "Found 131 rule files",
    "details": { ... },
    "confidence": 0.95
  },
  "metrics": {
    "tokensUsed": 1500,
    "executionTime": "45s"
  }
}
```

### Status File (status/{child_id}.json)

```json
{
  "childId": "child_1234567890_123456",
  "agentType": "claude",
  "status": "running",
  "progress": 50,
  "startTime": "2026-02-06T12:00:00Z",
  "lastUpdate": "2026-02-06T12:01:30Z"
}
```

---

## Usage Rules

### Reading Tasks

1. Check `incoming/from_above/` on session start
2. Parse JSON files for pending tasks
3. Mark as processed (move or delete after handling)

### Writing Results

1. Create result JSON following schema
2. Write to `outgoing/to_above/`
3. Include confidence score and metrics

### Spawning Children

1. Create `outgoing/to_below/{child_id}/` directory
2. Write `task.json` with subtask definition
3. Write `prompt.txt` with agent instructions
4. Create `status/{child_id}.json` to track

### Monitoring Children

1. Poll `status/{child_id}.json` for updates
2. Check `incoming/from_below/{child_id}/` for results
3. Handle timeouts and errors

---

## Context Chain Position

- **Parent**: `layer_0/CLAUDE.md`
- **Used By**: `layer_0/layer_0_01_ai_manager_system/personal/` (orchestrator)

---

## AALang Integration

@agent ctx:ContextLoadingAgent

### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += layer_0_02_manager_handoff_documents/CLAUDE.md
- `ctx:ContextLoadingStateActor.handoffProtocolAwareness` = true

### Immediate Actions

After loading this context:
1. Check `incoming/from_above/` for pending tasks
2. Check `incoming/from_below/` for child results
3. If tasks found, initiate orchestrator flow
