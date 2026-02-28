# Instructions Outputs

Implementation instructions for the Better AI System project.

## Structure

```
outputs/
├── 01_instructions_in_progress/      Instructions being developed
│   ├── by_need/                      Per Tree of Needs need
│   ├── by_topic/                     Cross-cutting topics
│   └── synthesis/                    Combined instructions
│
├── 02_finished_instructions/         Approved, ready for planning/design
│   ├── by_need/                      Per Tree of Needs need
│   ├── by_topic/                     Cross-cutting topics
│   └── synthesis/                    Combined instructions
│
└── README.md                         This file
```

---

## 01_instructions_in_progress/

Instructions that are being developed and refined. Not yet approved.

**Workflow:**
1. Receive approved understanding from `stage_-1_02_research/outputs/02_finished_understanding/`
2. Create instruction docs here
3. Refine with user input
4. When approved, move to `02_finished_instructions/`

---

## 02_finished_instructions/

Instructions that have been approved and are ready for planning/design stages.

---

## Workflow

```
┌─────────────────────────────────────┐
│ Research: 02_finished_understanding │
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ 01_instructions_in_progress/        │  ← Create instructions here
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ User approves                       │
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ 02_finished_instructions/           │  ← Move when approved
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ stage_-1_04_design/ or              │
│ stage_-1_05_planning/               │  ← Next stages use these
└─────────────────────────────────────┘
```

---

## Input

Instructions are based on:
- Finished understanding from `stage_-1_02_research/outputs/02_finished_understanding/`
- Tree of Needs v1.4.0
