# Universal Staging System

**Layer**: 0 (Universal)
**Purpose**: Standard structure for tracking tasks across all projects and OS systems

**Related**: `AI_MANAGER_FRAMEWORK.md` - AI agent coordination details

---

## Stage Structure

```
0.99_stages/
├── stage_0.00_request_gathering/
│   ├── HANDOFF.md              # Short summary (read first)
│   ├── _ai_manager/            # AI coordination
│   │   └── INSTRUCTIONS.md     # What AI should do here
│   └── output/                 # Detailed artifacts
│       └── REQUEST_*.md        # Full request details
│
├── stage_0.01_instructions/
│   ├── HANDOFF.md
│   ├── _ai_manager/
│   │   └── INSTRUCTIONS.md
│   └── output/
│       └── SPEC_*.md           # Technical specifications
│
├── stage_0.02_planning/
│   ├── HANDOFF.md
│   ├── _ai_manager/
│   │   └── INSTRUCTIONS.md
│   └── output/
│       └── PLAN_*.md           # Execution plans
│
└── stage_0.03_execution/
    ├── HANDOFF.md
    ├── _ai_manager/
    │   └── INSTRUCTIONS.md
    └── output/
        ├── PROGRESS_*.md       # Progress tracking
        └── [generated files]   # Scripts, configs, etc.
```

---

## Handoff Documents

**Purpose**: Short documents (~20-50 lines) that let agents quickly understand:
- Current status
- What's been done
- What needs to be done next
- Where to find detailed info

**Format**:
```markdown
# Stage X.XX Handoff: [Project Name]

## Status: [In Progress / Blocked / Complete]

## Summary
[2-3 sentences]

## Completed
- Item 1
- Item 2

## Next Actions
- [ ] Action 1
- [ ] Action 2

## Output Files
- `output/FILE.md` - Description

## Blockers
- [Any blockers]

## Pickup Instructions
[What the next agent should do first]
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

### Stage 0.00: Request Gathering
- Capture user requirements
- Define problem statement
- List acceptance criteria

### Stage 0.01: Instructions (Spec)
- Technical specifications
- API/interface definitions
- Data structures

### Stage 0.02: Planning
- Step-by-step execution plan
- Dependencies
- Time estimates
- Rollback plans

### Stage 0.03: Execution
- Track progress
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
