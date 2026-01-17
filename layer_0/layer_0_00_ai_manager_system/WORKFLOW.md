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
stage_X.XX_[name]/
├── HANDOFF.md              ← Status summary (read first)
├── _ai_manager/            ← AI coordination
│   ├── INSTRUCTIONS.md     ← What to do at this stage
│   ├── CONTEXT.md          ← Background info (optional)
│   └── RULES.md            ← Stage-specific rules (optional)
└── output/                 ← Detailed artifacts
    └── [OUTPUT_FILES].md
```

---

## AI Manager by Stage

### Stage 0.00: Request Gathering

**Role**: Understand and document requirements

**Entry Protocol**:
1. Read HANDOFF.md
2. Read _ai_manager/INSTRUCTIONS.md
3. Review user's original request

**Tasks**:
- Clarify ambiguities with user
- Document requirements
- Define acceptance criteria

**Exit Protocol**:
- Create `output/REQUEST_*.md`
- Update HANDOFF.md → COMPLETE
- Note: "Ready for stage_0.01"

---

### Stage 0.01: Instructions/Specifications

**Role**: Create technical specifications

**Entry Protocol**:
1. Read HANDOFF.md
2. Read _ai_manager/INSTRUCTIONS.md
3. Read stage_0.00/output/REQUEST_*.md

**Tasks**:
- Define technical approach
- Specify interfaces
- Document constraints

**Exit Protocol**:
- Create `output/SPEC_*.md`
- Update HANDOFF.md → COMPLETE
- Note: "Ready for stage_0.02"

---

### Stage 0.02: Planning

**Role**: Create execution plan

**Entry Protocol**:
1. Read HANDOFF.md
2. Read _ai_manager/INSTRUCTIONS.md
3. Read stage_0.01/output/SPEC_*.md

**Tasks**:
- Break into phases/steps
- Identify dependencies
- Create rollback plan

**Exit Protocol**:
- Create `output/PLAN_*.md`
- Update HANDOFF.md → COMPLETE
- Note: "Ready for stage_0.03"

---

### Stage 0.03: Execution

**Role**: Execute plan, track progress

**Entry Protocol**:
1. Read HANDOFF.md
2. Read _ai_manager/INSTRUCTIONS.md
3. Read stage_0.02/output/PLAN_*.md

**Tasks**:
- Execute steps from plan
- Track progress
- Handle blockers
- Generate outputs

**Exit Protocol**:
- Update `output/PROGRESS_*.md`
- Store generated files in output/
- Update HANDOFF.md with final status

---

## Universal Rules for All AI Agents

### File Operations
1. **ALWAYS** check `CROSS_OS_COMPATIBILITY_RULES.md` before creating files
2. **NEVER** use forbidden characters: `* ? < > : " | \ /`
3. **USE** lowercase with underscores

### Token Efficiency
1. Read HANDOFF.md first (~500 tokens)
2. Only read output/ files when details needed
3. Reference files, don't repeat content

### Handoff Protocol
1. Update HANDOFF.md before stopping
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

1. Create `0.99_stages/` folder
2. Create stage folders: `stage_0.00_*`, `stage_0.01_*`, etc.
3. In each stage, create:
   - `HANDOFF.md` (from template)
   - `_ai_manager/INSTRUCTIONS.md` (from template)
   - `output/` folder
4. Start work in stage_0.00
