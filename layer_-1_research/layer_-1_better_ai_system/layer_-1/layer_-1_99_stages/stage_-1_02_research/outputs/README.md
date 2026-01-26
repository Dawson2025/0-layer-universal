# Research Outputs

Research findings for the Better AI System project.

## Structure

```
outputs/
├── 01_understanding_in_progress/     Research being refined
│   ├── by_need/                      Per Tree of Needs need
│   ├── by_topic/                     Cross-cutting topics
│   └── synthesis/                    Combined insights
│
├── 02_finished_understanding/        Approved, ready for instructions stage
│   ├── by_need/                      Per Tree of Needs need
│   ├── by_topic/                     Cross-cutting topics
│   └── synthesis/                    Combined insights
│
└── README.md                         This file
```

---

## 01_understanding_in_progress/

Research that is being developed and refined. Not yet approved.

**Workflow:**
1. Create research docs here
2. Refine with user input
3. When approved, move to `02_finished_understanding/`
4. Then move to `stage_-1_03_instructions/outputs/` for implementation

### Current Contents

| Folder | File | Topic | Status |
|--------|------|-------|--------|
| by_topic | `agnostic_memory_system_research.md` | Memory patterns | Started |
| by_topic | `existing_solutions.md` | Clawdbot analysis | Complete |
| by_topic | `memory_systems.md` | Memory approaches (Clawdbot, Layer-Stage, SHIMI) | Complete |
| by_topic | `rule_propagation_problem.md` | Universal rules not loading | In Progress |
| by_topic | `system_prompt_architecture.md` | What goes IN vs REFERENCED | Draft - Awaiting Input |

---

## 02_finished_understanding/

Research that has been approved and is ready to move to the instructions stage.

### Current Contents

(Empty - no finished understanding yet)

---

## Workflow

```
┌─────────────────────────┐
│ Create research doc     │
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ 01_understanding_in_    │
│ progress/               │  ← Refine here
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ User approves           │
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ 02_finished_            │
│ understanding/          │  ← Move when approved
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ stage_-1_03_            │
│ instructions/outputs/   │  ← Move for implementation
└─────────────────────────┘
```

---

## Input

Research is based on:
- Tree of Needs v1.4.0 from request_gathering stage
- Handoff document: `../hand_off_documents/incoming/20260126_to_research_handoff.md`
