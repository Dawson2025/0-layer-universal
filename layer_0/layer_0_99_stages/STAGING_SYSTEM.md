---
resource_id: "93a519db-5960-4a16-9f18-c42cee0ea968"
resource_type: "document"
resource_name: "STAGING_SYSTEM"
---
# Universal Staging System

**Layer**: 0 (Universal)
**Purpose**: Standard structure for tracking tasks across all projects and OS systems

**Related**: `AI_MANAGER_FRAMEWORK.md` - AI agent coordination details

---

<!-- section_id: "b9428c6a-bb8a-4189-849f-20d794f73f05" -->
## Stage Structure

```
layer_0_99_stages/
├── stage_0_01_request_gathering/
│   ├── ai_agent_system/        # AI coordination
│   ├── hand_off_documents/     # incoming.json / outgoing.json
│   └── outputs/                # Detailed artifacts
│
├── stage_0_02_research/
│   ├── ai_agent_system/
│   ├── hand_off_documents/
│   └── outputs/
│
├── stage_0_03_instructions/
│   ├── ai_agent_system/
│   ├── hand_off_documents/
│   └── outputs/
│
├── stage_0_04_planning/
├── stage_0_05_design/
├── stage_0_06_development/
├── stage_0_07_testing/
├── stage_0_08_criticism/
├── stage_0_09_fixing/
├── stage_0_10_current_product/
└── stage_0_11_archives/
```

---

<!-- section_id: "4be68772-675f-4c5f-8fcf-f2347e6b6ceb" -->
## Handoff Documents

**Purpose**: Concise handoff files that let agents quickly understand:
- Current status
- What's been done
- What needs to be done next
- Where to find detailed info

**Format** (JSON handoff):
```json
{
  "schemaVersion": "1.0.0",
  "stage": "stage_0_03_instructions",
  "status": "in_progress",
  "summary": "Constraints defined, pending planning.",
  "next_actions": ["Create planning outline", "Identify dependencies"],
  "outputs": ["outputs/SPEC_LAYER_STAGE.md"]
}
```

---

<!-- section_id: "8a4a4165-d4a2-480e-a36c-f3e0101de17d" -->
## Output Folders

**Purpose**: Store detailed artifacts that handoff docs reference

**Contents**:
- Full REQUEST/SPEC/PLAN/PROGRESS documents
- Generated scripts and configs
- Logs and debug output
- Screenshots (if needed)

**Naming Convention**:
- `REQUEST_[project_name].md`
- `SPEC_[project_name].md`
- `PLAN_[project_name].md`
- `PROGRESS_[project_name].md`

---

<!-- section_id: "d0afa17a-0730-434f-90dc-e4d06aa6008f" -->
## Stage Definitions

<!-- section_id: "0aa5d832-78d9-41eb-b395-e6eb25f4dcd2" -->
### Stage 0.01: Request Gathering
- Capture user requirements
- Define problem statement
- List acceptance criteria

<!-- section_id: "e6098803-d9b7-4b4f-b1dd-d621a38cab41" -->
### Stage 0.02: Research
- Gather context and explore options
- Validate assumptions
- Capture constraints or unknowns

<!-- section_id: "3575b286-749a-4cee-b189-fb22b5a14e4a" -->
### Stage 0.03: Instructions (Spec)
- Technical specifications
- API/interface definitions
- Data structures

<!-- section_id: "a1c96572-7b44-4871-9830-411d8456d5b3" -->
### Stage 0.04: Planning
- Step-by-step execution plan
- Dependencies
- Time estimates
- Rollback plans

<!-- section_id: "a7d24a14-6fe4-4d47-862c-0f3349208e2c" -->
### Stage 0.05: Design
- Architecture and interface decisions

<!-- section_id: "f91ce40e-56b6-4778-892b-eb3c72736eb8" -->
### Stage 0.06: Development
- Implement changes

<!-- section_id: "db7147dd-275b-4036-88db-523f75940359" -->
### Stage 0.07: Testing
- Verify functionality

<!-- section_id: "c255eaac-bebf-476c-857a-a54db388e83d" -->
### Stage 0.08: Criticism
- Review against standards

<!-- section_id: "d27fdfd0-c04d-4dc7-8185-89484190de3b" -->
### Stage 0.09: Fixing
- Address review findings

<!-- section_id: "f0dacc24-8347-4deb-8d65-e3b81005f58b" -->
### Stage 0.10: Current Product
- Active deliverables and guides

<!-- section_id: "2d71ad9a-e1d2-4178-b030-0640ba890b9d" -->
### Stage 0.11: Archives
- Historical artifacts and superseded docs
- Log completed items
- Note blockers
- Store generated output

<!-- section_id: "d7193626-4517-4432-80c8-01a466088855" -->
### Stage 0.04: Verification (optional)
- Test results
- Validation checks
- Sign-off

<!-- section_id: "9ba25b74-bcc8-4d27-9418-2d5974a21be2" -->
### Stage 0.05: Completion (optional)
- Final summary
- Lessons learned
- Documentation updates

---

<!-- section_id: "7980a48d-876c-4426-9fb8-dc0b9407e33e" -->
## Agent Workflow

<!-- section_id: "ac5f19de-7dcd-4077-a162-495f0da0902e" -->
### Starting a Task
1. Read `HANDOFF.md` in current stage
2. Check status and next actions
3. Read referenced output files if needed
4. Continue from pickup instructions

<!-- section_id: "3ecde48f-9791-42aa-a591-13742c0b3bfe" -->
### During Work
1. Update `HANDOFF.md` status as you progress
2. Add detailed output to `output/` folder
3. Keep handoff concise

<!-- section_id: "aaef1fab-6ec3-4ef3-8522-ae8906b451b1" -->
### Completing a Stage
1. Update `HANDOFF.md` with completion status
2. Create `HANDOFF.md` in next stage
3. Reference any output files

<!-- section_id: "cc378d57-413f-4cba-a0f7-0fc3b0bd52d3" -->
### Handing Off to Another Agent
1. Ensure `HANDOFF.md` is current
2. List clear next actions
3. Note any blockers or context needed

---

<!-- section_id: "f0ae17cd-fbae-45ee-b7c5-d000e4f45096" -->
## Token Efficiency

**Why this structure saves tokens:**
1. Agents read short handoff first (~500 tokens)
2. Only read detailed output if needed
3. No need to repeat context - reference files instead
4. Clear pickup points reduce backtracking

**Example token savings:**
- Old: Read 5000-token detailed doc every time
- New: Read 500-token handoff, reference details as needed

---

<!-- section_id: "4707d725-adcd-437a-9d2e-d811aaee23e4" -->
## Cross-Project Rules

1. **Always create handoff docs** when starting a stage
2. **Keep handoffs under 100 lines**
3. **Put details in output folder**
4. **Update handoff when status changes**
5. **Reference, don't repeat** detailed content

---

<!-- section_id: "0f99ea45-18d1-4103-bb6a-b1fdfc921dcd" -->
## Template Files

See `_templates/` folder for:
- `HANDOFF_TEMPLATE.md`
- `REQUEST_TEMPLATE.md`
- `SPEC_TEMPLATE.md`
- `PLAN_TEMPLATE.md`
- `PROGRESS_TEMPLATE.md`
