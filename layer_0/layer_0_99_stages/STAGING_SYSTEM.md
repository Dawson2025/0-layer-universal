# Universal Staging System

**Layer**: 0 (Universal)
**Purpose**: Standard structure for tracking tasks across all projects and OS systems

**Related**: `AI_MANAGER_FRAMEWORK.md` - AI agent coordination details

---

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

## Stage Definitions

### Stage 0.01: Request Gathering
- Capture user requirements
- Define problem statement
- List acceptance criteria

### Stage 0.02: Research
- Gather context and explore options
- Validate assumptions
- Capture constraints or unknowns

### Stage 0.03: Instructions (Spec)
- Technical specifications
- API/interface definitions
- Data structures

### Stage 0.04: Planning
- Step-by-step execution plan
- Dependencies
- Time estimates
- Rollback plans

### Stage 0.05: Design
- Architecture and interface decisions

### Stage 0.06: Development
- Implement changes

### Stage 0.07: Testing
- Verify functionality

### Stage 0.08: Criticism
- Review against standards

### Stage 0.09: Fixing
- Address review findings

### Stage 0.10: Current Product
- Active deliverables and guides

### Stage 0.11: Archives
- Historical artifacts and superseded docs
- Log completed items
- Note blockers
- Store generated output

### Stage 0.04: Verification (optional)
- Test results
- Validation checks
- Sign-off

### Stage 0.05: Completion (optional)
- Final summary
- Lessons learned
- Documentation updates

---

## Agent Workflow

### Starting a Task
1. Read `HANDOFF.md` in current stage
2. Check status and next actions
3. Read referenced output files if needed
4. Continue from pickup instructions

### During Work
1. Update `HANDOFF.md` status as you progress
2. Add detailed output to `output/` folder
3. Keep handoff concise

### Completing a Stage
1. Update `HANDOFF.md` with completion status
2. Create `HANDOFF.md` in next stage
3. Reference any output files

### Handing Off to Another Agent
1. Ensure `HANDOFF.md` is current
2. List clear next actions
3. Note any blockers or context needed

---

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

## Cross-Project Rules

1. **Always create handoff docs** when starting a stage
2. **Keep handoffs under 100 lines**
3. **Put details in output folder**
4. **Update handoff when status changes**
5. **Reference, don't repeat** detailed content

---

## Template Files

See `_templates/` folder for:
- `HANDOFF_TEMPLATE.md`
- `REQUEST_TEMPLATE.md`
- `SPEC_TEMPLATE.md`
- `PLAN_TEMPLATE.md`
- `PROGRESS_TEMPLATE.md`
