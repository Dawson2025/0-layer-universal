---
resource_id: "9f9415c9-c752-4388-9e81-5c0c19b9bb29"
resource_type: "document"
resource_name: "WORKFLOW"
---
# AI Manager Framework

**Layer**: 0 (Universal)
**Purpose**: Standard system for AI agent coordination across all stages and projects

---

<!-- section_id: "cec7a506-dc69-45f8-8963-9463d34a9705" -->
## Overview

Every stage in the staging system includes an `_ai_manager/` folder that tells AI agents:
- What their role is at this stage
- What to read first
- What outputs to create
- When/how to hand off

---

<!-- section_id: "3a0917ee-6e09-4951-94a7-8bb8d036a44f" -->
## Stage Structure (with AI Manager)

```
stage_0_XX_[name]/
├── ai_agent_system/        ← AI coordination (stage-specific guidance)
├── hand_off_documents/     ← incoming.json / outgoing.json
└── outputs/                ← Detailed artifacts
    └── [OUTPUT_FILES].md
```

---

<!-- section_id: "aa70e07a-2679-45e3-824c-7951899e17f3" -->
## AI Manager by Stage

<!-- section_id: "52a56fa4-21b9-47bc-9f8d-8ae7c0db0115" -->
### Stage 0.01: Request Gathering

**Role**: Understand and document requirements

**Entry Protocol**:
1. Read hand_off_documents/incoming.json
2. Read ai_agent_system/ guidance
3. Review user's original request

**Tasks**:
- Clarify ambiguities with user
- Document requirements
- Define acceptance criteria

**Exit Protocol**:
- Create `outputs/REQUEST_*.md`
- Update hand_off_documents/outgoing.json → COMPLETE
- Note: "Ready for stage_0_03"

---

<!-- section_id: "cbc99c98-4d0f-49ed-854b-bbdfc15c6cbb" -->
### Stage 0.03: Instructions/Specifications

**Role**: Create technical specifications

**Entry Protocol**:
1. Read hand_off_documents/incoming.json
2. Read ai_agent_system/ guidance
3. Read stage_0_01_request_gathering/outputs/REQUEST_*.md

**Tasks**:
- Define technical approach
- Specify interfaces
- Document constraints

**Exit Protocol**:
- Create `outputs/SPEC_*.md`
- Update hand_off_documents/outgoing.json → COMPLETE
- Note: "Ready for stage_0_04"

---

<!-- section_id: "03839c69-9cdb-4153-8b71-3009b1f78c18" -->
### Stage 0.04: Planning

**Role**: Create execution plan

**Entry Protocol**:
1. Read hand_off_documents/incoming.json
2. Read ai_agent_system/ guidance
3. Read stage_0_03_instructions/outputs/SPEC_*.md

**Tasks**:
- Break into phases/steps
- Identify dependencies
- Create rollback plan

**Exit Protocol**:
- Create `outputs/PLAN_*.md`
- Update hand_off_documents/outgoing.json → COMPLETE
- Note: "Ready for stage_0_05"

---

<!-- section_id: "383be5d8-a697-44fe-867f-bbc6d878a625" -->
### Stage 0.06: Development

**Role**: Execute plan, track progress

**Entry Protocol**:
1. Read hand_off_documents/incoming.json
2. Read ai_agent_system/ guidance
3. Read stage_0_04_planning/outputs/PLAN_*.md

**Tasks**:
- Execute steps from plan
- Track progress
- Handle blockers
- Generate outputs

**Exit Protocol**:
- Update `outputs/PROGRESS_*.md`
- Store generated files in outputs/
- Update hand_off_documents/outgoing.json with final status

---

<!-- section_id: "f9eeee83-b471-415a-b4f8-c383bb9e542f" -->
## Universal Rules for All AI Agents

<!-- section_id: "16624177-e85c-4f55-b1fd-07ccb394a960" -->
### File Operations
1. **ALWAYS** check `CROSS_OS_COMPATIBILITY_RULES.md` before creating files
2. **NEVER** use forbidden characters: `* ? < > : " | \ /`
3. **USE** lowercase with underscores

<!-- section_id: "b65679aa-224f-4926-8031-f02aaf94af11" -->
### Token Efficiency
1. Read hand_off_documents/incoming.json first (~500 tokens)
2. Only read outputs/ files when details needed
3. Reference files, don't repeat content

<!-- section_id: "0f6de8c4-905f-4c99-937a-b079ba9213e9" -->
### Handoff Protocol
1. Update hand_off_documents/outgoing.json before stopping
2. List clear next actions
3. Note any blockers
4. Another agent should be able to continue seamlessly

---

<!-- section_id: "98c66505-b2c9-42c1-a127-3ba0b836e335" -->
## Templates

See `_templates/` folder for:
- `HANDOFF_TEMPLATE.md`
- `AI_MANAGER_INSTRUCTIONS_TEMPLATE.md`
- `REQUEST_TEMPLATE.md`
- `SPEC_TEMPLATE.md`
- `PLAN_TEMPLATE.md`
- `PROGRESS_TEMPLATE.md`

---

<!-- section_id: "3a303a9e-1a10-4dea-b3ef-fee116eedf4d" -->
## Creating a New Project

1. Create `layer_0_99_stages/` folder
2. Create stage folders: `stage_0_01_*`, `stage_0_02_*`, etc.
3. In each stage, create:
   - `ai_agent_system/` (from template)
   - `hand_off_documents/`
   - `outputs/`
4. Start work in stage_0_01_request_gathering
