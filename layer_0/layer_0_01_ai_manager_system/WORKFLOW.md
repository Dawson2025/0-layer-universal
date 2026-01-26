# AI Manager Framework

**Layer**: 0 (Universal)
**Purpose**: Standard system for AI agent coordination across all stages and projects

---

## Overview

Every stage in the staging system includes an `_ai_manager/` folder that tells AI agents:
- What their role is at this stage
- What to read first
- What outputs to create
- When/how to hand off

---

## Stage Structure (with AI Manager)

```
stage_0_XX_[name]/
├── ai_agent_system/        ← AI coordination (stage-specific guidance)
├── hand_off_documents/     ← incoming.json / outgoing.json
└── outputs/                ← Detailed artifacts
    └── [OUTPUT_FILES].md
```

---

## AI Manager by Stage

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

## Universal Rules for All AI Agents

### File Operations
1. **ALWAYS** check `CROSS_OS_COMPATIBILITY_RULES.md` before creating files
2. **NEVER** use forbidden characters: `* ? < > : " | \ /`
3. **USE** lowercase with underscores

### Token Efficiency
1. Read hand_off_documents/incoming.json first (~500 tokens)
2. Only read outputs/ files when details needed
3. Reference files, don't repeat content

### Handoff Protocol
1. Update hand_off_documents/outgoing.json before stopping
2. List clear next actions
3. Note any blockers
4. Another agent should be able to continue seamlessly

---

## Templates

See `_templates/` folder for:
- `HANDOFF_TEMPLATE.md`
- `AI_MANAGER_INSTRUCTIONS_TEMPLATE.md`
- `REQUEST_TEMPLATE.md`
- `SPEC_TEMPLATE.md`
- `PLAN_TEMPLATE.md`
- `PROGRESS_TEMPLATE.md`

---

## Creating a New Project

1. Create `layer_0_99_stages/` folder
2. Create stage folders: `stage_0_01_*`, `stage_0_02_*`, etc.
3. In each stage, create:
   - `ai_agent_system/` (from template)
   - `hand_off_documents/`
   - `outputs/`
4. Start work in stage_0_01_request_gathering
