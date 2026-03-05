---
resource_id: "58ebd44c-fdaf-46ae-b8c8-436544b85ec9"
resource_type: "document"
resource_name: "stage_handoffs"
---
# Stage Handoffs

<!-- section_id: "9cedbebb-d8bf-4910-a156-2567355c68ce" -->
## Between Stages
Each stage transition requires:
1. Exit criteria met in current stage
2. Handoff document created
3. Entry criteria checked for next stage

<!-- section_id: "7a1f1ccc-de30-4492-8678-2852cde1d615" -->
## Handoff Contents by Stage
| From Stage | To Stage | Key Contents |
|------------|----------|--------------|
| 00_request | 01_instructions | Requirements gathered |
| 01_instructions | 02_planning | What to do defined |
| 02_planning | 03_design | How to do it planned |
| 03_design | 04_development | Design specs ready |
| 04_development | 05_testing | Implementation done |

<!-- section_id: "80b52c87-f6d9-4285-96c3-1ff132461151" -->
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

<!-- section_id: "62fe91f8-899e-4492-9507-0aed1a0dd446" -->
## Stage-Specific Handoff Details

<!-- section_id: "4a61fc8c-9fd7-4bc0-a0c0-d6104acd1fe0" -->
### 00_request -> 01_instructions
- **Summary**: Initial requirements and context gathered
- **Key Deliverables**: Requirements document, stakeholder input
- **Artifacts**: `request.md`, `requirements.json`

<!-- section_id: "a3fac5e7-8fa7-4411-bb7a-a56f00cdbc5f" -->
### 01_instructions -> 02_planning
- **Summary**: Clear instructions defined
- **Key Deliverables**: Scope definition, acceptance criteria
- **Artifacts**: `instructions.md`, `scope.md`

<!-- section_id: "c8616256-fa52-4d02-a442-fb290cc0d286" -->
### 02_planning -> 03_design
- **Summary**: Implementation plan created
- **Key Deliverables**: Task breakdown, timeline, dependencies
- **Artifacts**: `plan.md`, `tasks.json`

<!-- section_id: "aa48969e-cae6-43b4-a130-330c8979664d" -->
### 03_design -> 04_development
- **Summary**: Design specifications complete
- **Key Deliverables**: Architecture docs, interface specs
- **Artifacts**: `design.md`, `architecture.md`

<!-- section_id: "c3586eef-f457-4c62-a2e1-b636ea7dc909" -->
### 04_development -> 05_testing
- **Summary**: Implementation complete
- **Key Deliverables**: Working code, unit tests
- **Artifacts**: Source files, `implementation_notes.md`

<!-- section_id: "46d665c7-a056-4459-81f1-022d9651d36f" -->
## Location

Stage handoff documents are stored in:
```
stage_N_XX_name/hand_off_documents/
├── from_previous_stage.json
└── to_next_stage.json
```

<!-- section_id: "7be6cce0-4395-4835-a529-e4008ea7da54" -->
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
