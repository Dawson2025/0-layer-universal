---
resource_id: "2ec425f3-1ce6-4fc6-ab87-535bc974c566"
resource_type: "knowledge"
resource_name: "stage_handoffs"
---
# Stage Handoffs

## Between Stages
Each stage transition requires:
1. Exit criteria met in current stage
2. Handoff document created
3. Entry criteria checked for next stage

## Handoff Contents by Stage
| From Stage | To Stage | Key Contents |
|------------|----------|--------------|
| 00_request | 01_instructions | Requirements gathered |
| 01_instructions | 02_planning | What to do defined |
| 02_planning | 03_design | How to do it planned |
| 03_design | 04_development | Design specs ready |
| 04_development | 05_testing | Implementation done |

## Stage Handoff Template

```json
{
  "handoff_id": "uuid",
  "created": "ISO timestamp",
  "from": {
    "entity": "feature_X",
    "stage": "stage_N_XX_current"
  },
  "to": {
    "entity": "feature_X",
    "stage": "stage_N_XX_next"
  },
  "type": "stage",
  "payload": {
    "summary": "Stage completion summary",
    "deliverables": [],
    "tasks_completed": [],
    "tasks_remaining": [],
    "blockers": [],
    "artifacts": [],
    "notes": ""
  }
}
```

## Stage-Specific Handoff Details

### 00_request -> 01_instructions
- **Summary**: Initial requirements and context gathered
- **Key Deliverables**: Requirements document, stakeholder input
- **Artifacts**: `request.md`, `requirements.json`

### 01_instructions -> 02_planning
- **Summary**: Clear instructions defined
- **Key Deliverables**: Scope definition, acceptance criteria
- **Artifacts**: `instructions.md`, `scope.md`

### 02_planning -> 03_design
- **Summary**: Implementation plan created
- **Key Deliverables**: Task breakdown, timeline, dependencies
- **Artifacts**: `plan.md`, `tasks.json`

### 03_design -> 04_development
- **Summary**: Design specifications complete
- **Key Deliverables**: Architecture docs, interface specs
- **Artifacts**: `design.md`, `architecture.md`

### 04_development -> 05_testing
- **Summary**: Implementation complete
- **Key Deliverables**: Working code, unit tests
- **Artifacts**: Source files, `implementation_notes.md`

## Location

Stage handoff documents are stored in:
```
stage_N_XX_name/hand_off_documents/
├── from_previous_stage.json
└── to_next_stage.json
```

## Validation Checklist

Before creating a handoff:
- [ ] All exit criteria for current stage met
- [ ] Deliverables documented
- [ ] Artifacts created and referenced
- [ ] Blockers identified (if any)
- [ ] Summary is clear and concise

Before accepting a handoff:
- [ ] Schema validation passes
- [ ] Entry criteria can be met
- [ ] Required artifacts exist
- [ ] No unresolved blockers
