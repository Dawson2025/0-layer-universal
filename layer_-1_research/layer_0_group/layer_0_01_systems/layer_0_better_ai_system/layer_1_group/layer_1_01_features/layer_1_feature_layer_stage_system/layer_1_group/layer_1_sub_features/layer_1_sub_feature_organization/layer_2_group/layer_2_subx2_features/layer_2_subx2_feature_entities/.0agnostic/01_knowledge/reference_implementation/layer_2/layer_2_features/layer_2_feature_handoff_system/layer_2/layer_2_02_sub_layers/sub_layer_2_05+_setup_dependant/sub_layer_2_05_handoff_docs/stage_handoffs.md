---
resource_id: "2ec425f3-1ce6-4fc6-ab87-535bc974c566"
resource_type: "knowledge"
resource_name: "stage_handoffs"
---
# Stage Handoffs

<!-- section_id: "01155b42-56fc-47c2-9e28-2ecfcd68aec5" -->
## Between Stages
Each stage transition requires:
1. Exit criteria met in current stage
2. Handoff document created
3. Entry criteria checked for next stage

<!-- section_id: "96881465-1f6b-43b4-ba07-eb7dbcf35685" -->
## Handoff Contents by Stage
| From Stage | To Stage | Key Contents |
|------------|----------|--------------|
| 00_request | 01_instructions | Requirements gathered |
| 01_instructions | 02_planning | What to do defined |
| 02_planning | 03_design | How to do it planned |
| 03_design | 04_development | Design specs ready |
| 04_development | 05_testing | Implementation done |

<!-- section_id: "1c3aa4a6-75cd-4c67-93c8-d354c6a9ac93" -->
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

<!-- section_id: "f4fb0fd4-39c9-495d-8bfe-d69aebb922c6" -->
## Stage-Specific Handoff Details

<!-- section_id: "a56605c0-5bed-4211-827f-df60b00dbcd6" -->
### 00_request -> 01_instructions
- **Summary**: Initial requirements and context gathered
- **Key Deliverables**: Requirements document, stakeholder input
- **Artifacts**: `request.md`, `requirements.json`

<!-- section_id: "a0b3ece6-b332-46b7-8e38-f079884b0e63" -->
### 01_instructions -> 02_planning
- **Summary**: Clear instructions defined
- **Key Deliverables**: Scope definition, acceptance criteria
- **Artifacts**: `instructions.md`, `scope.md`

<!-- section_id: "69e0634e-3c9a-4882-995a-680cc68ebd3b" -->
### 02_planning -> 03_design
- **Summary**: Implementation plan created
- **Key Deliverables**: Task breakdown, timeline, dependencies
- **Artifacts**: `plan.md`, `tasks.json`

<!-- section_id: "db1db8a4-373c-4c01-a0d3-667c5394b52e" -->
### 03_design -> 04_development
- **Summary**: Design specifications complete
- **Key Deliverables**: Architecture docs, interface specs
- **Artifacts**: `design.md`, `architecture.md`

<!-- section_id: "ae09e2f0-3c0c-414b-86f0-b32a9f237149" -->
### 04_development -> 05_testing
- **Summary**: Implementation complete
- **Key Deliverables**: Working code, unit tests
- **Artifacts**: Source files, `implementation_notes.md`

<!-- section_id: "9c7cc3a5-1e0f-4c3e-a703-2393aa7266ca" -->
## Location

Stage handoff documents are stored in:
```
stage_N_XX_name/hand_off_documents/
├── from_previous_stage.json
└── to_next_stage.json
```

<!-- section_id: "44e1d114-7892-400b-a9e5-10030565b649" -->
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
