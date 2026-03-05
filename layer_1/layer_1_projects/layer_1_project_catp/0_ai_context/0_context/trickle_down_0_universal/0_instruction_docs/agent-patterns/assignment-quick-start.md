---
resource_id: "ae8084c5-4971-42df-82b4-59027c8a92ba"
resource_type: "document"
resource_name: "assignment-quick-start"
---
# Quick Start: Structured Assignment Workflow

**TL;DR**: Use `assignment-planner` to create a plan, get user approval, then use `assignment-executor` to execute it automatically.

<!-- section_id: "84686b15-d837-44c5-8668-47c730cfe833" -->
## 1-Minute Overview

```
User Request → assignment-planner → Plan → User Approval → assignment-executor → Done
```

<!-- section_id: "5b0d47ee-3ab3-4d8f-9e0e-30c406ee7944" -->
## Quick Example

<!-- section_id: "016f8345-e71a-4577-ac11-345d019607e5" -->
### User Says:
```
"Set up Unit 3 Assignment 1"
```

<!-- section_id: "16ddb00b-e37b-462f-9a98-736eae657f99" -->
### You Do:

**Step 1**: Invoke planning agent
```
Use the Task tool with subagent_type="assignment-planner"
```

**Step 2**: Wait for plan output

**Step 3**: User approves plan

**Step 4**: Invoke execution agent
```
Use the Task tool with subagent_type="assignment-executor"
Paste the approved plan in the prompt
```

**Step 5**: Monitor todos and wait for completion

<!-- section_id: "54d5cf5e-8d20-4cf5-803f-67628a0c488d" -->
## When to Use

✅ **Use this pattern for:**
- "Set up Unit X Assignment Y"
- "Create Unit Z template"
- "Reorganize Unit W folders"
- Any multi-step assignment setup

❌ **Don't use for:**
- Simple file edits
- Quick questions
- One-off changes

<!-- section_id: "f46943d8-c652-43ac-8ae4-fe5021b260e2" -->
## Detailed Walkthrough

<!-- section_id: "66b6bd89-3aa8-4194-afa4-425ff463610f" -->
### Step 1: User Makes Request

User wants to set up a new assignment following 0_context rules.

**Example requests:**
- "Set up Unit 4 Assignment 2"
- "Create Unit 5 Task 1 with Canvas assignment https://..."
- "Organize Unit 3 into assignment folders"

<!-- section_id: "3d556636-089b-43c5-a99f-6253d5c5df77" -->
### Step 2: Invoke Planning Agent

**Use the Task tool:**

```python
Task(
    description="Plan Unit X Assignment Y setup",
    subagent_type="assignment-planner",
    prompt="""
    Set up Unit X Assignment Y:
    - Canvas URL: https://byui.instructure.com/courses/.../assignments/...
    - Follow all 0_context rules
    - Include both absolute and relative paths
    - Create comprehensive plan for approval
    """,
    model="sonnet"  # Optional, but recommended for planning
)
```

<!-- section_id: "08bf978b-e550-4988-9f90-9d7d454f0159" -->
### Step 3: Review Planning Agent Output

**Planning agent will:**
- Authenticate with Canvas (using canvas_authenticate.py)
- Extract assignment requirements
- Analyze Unit 2 pattern
- Create step-by-step plan
- Estimate time
- List files to create/modify
- Include verification checklist

**Output format:**
```markdown
## Plan: Unit X Assignment Y Setup

### Phase 1: Canvas Extraction (5 min)
1. Authenticate with Canvas
2. Extract assignment content
...

### Phase 2: Folder Reorganization (10 min)
...

**Estimated time**: ~60 minutes
**Files to create**: 5
**Files to modify**: 3
```

<!-- section_id: "9a5726a7-1da0-4934-a74e-007319f9ee7b" -->
### Step 4: User Approves Plan

**User says:**
- "Approved!"
- "Looks good, execute it"
- "Go ahead with this plan"

**OR requests changes:**
- "Can you also add X?"
- "Skip the folder reorganization"

If changes requested, re-invoke planning agent with modifications.

<!-- section_id: "a32a3dab-232c-4e1b-bff7-89e0b6e44167" -->
### Step 5: Invoke Execution Agent

**Use the Task tool with approved plan:**

```python
Task(
    description="Execute Unit X Assignment Y plan",
    subagent_type="assignment-executor",
    prompt="""
    Execute the following approved plan:

    [PASTE THE ENTIRE APPROVED PLAN HERE]

    Requirements:
    - Create todos from plan steps
    - Track progress in real-time
    - Verify with MCP browser tools
    - Create archive entry and update changelog
    """
)
```

<!-- section_id: "5dc8c504-f5d9-4fca-9122-d2647db388e4" -->
### Step 6: Monitor Execution

**Execution agent will:**
1. Create todo list (you'll see it)
2. Execute each step (updating todos)
3. Report progress
4. Handle any errors
5. Verify with MCP tools
6. Document results

**You'll see:**
```
[1. [completed] Extract Canvas assignment
 2. [in_progress] Create folder structure
 3. [pending] Move files
 4. [pending] Update template paths
...]
```

<!-- section_id: "9ba4355d-7011-4bb3-89dd-acd7ed5230f1" -->
### Step 7: Completion

**Execution agent reports:**
```markdown
## ✅ Assignment Complete!

### Files Created/Modified:
- Projects/Unit_X/assignment_Y/...
- Templates/Unit_X/assignment_Y/...

### Verification:
- Rendered successfully ✅
- MCP visual verification passed ✅
- Analysis matches visuals ✅

### Documentation:
- Archive entry created
- CHANGELOG updated
```

<!-- section_id: "cb55a178-f0c9-4c2a-bc3d-b00bfb2a98e4" -->
## Common Patterns

<!-- section_id: "64d45975-ec1b-4033-bb51-de5e8a73b677" -->
### Pattern 1: New Unit Assignment
```
User: "Set up Unit 4 Assignment 1"
→ planner extracts from Canvas
→ user approves
→ executor creates folders, moves files, completes template
→ done
```

<!-- section_id: "f3ff45a3-d13b-429b-89f8-6c5f8106169e" -->
### Pattern 2: Template Only
```
User: "Complete Unit 3 Assignment 2 template"
→ planner identifies existing structure, plans completion
→ user approves
→ executor fills in analysis and code
→ done
```

<!-- section_id: "691185f4-bda0-41cb-8dd1-3e1d9c8af66a" -->
### Pattern 3: Folder Reorganization
```
User: "Reorganize Unit 5 like Unit 2"
→ planner analyzes Unit 2 pattern, creates reorg plan
→ user approves
→ executor moves files, updates paths
→ done
```

<!-- section_id: "6c29b12d-db6e-472c-bc59-90659651cd93" -->
## Troubleshooting

<!-- section_id: "ca69185c-9412-4c29-a80f-ac6d91695dcf" -->
### "Canvas authentication failed"
- Verify `.env` file exists with credentials
- Test: `python3 0_context/.../canvas_authenticate.py`
- Check credentials are correct

<!-- section_id: "c7f47b03-3ded-41e3-b6cf-4cde99458153" -->
### "MCP browser tools not working"
- Try different MCP server: playwright → chrome-devtools → browser
- Check MCP configuration in `~/.config/mcp/mcp.json`

<!-- section_id: "dbc501df-aa6c-4298-81dd-17cb0b006953" -->
### "Template rendering failed"
- Execution agent will render from template directory
- Check Quarto env vars (or render from template dir)
- Verify Python packages installed in .venv

<!-- section_id: "4f5d19a4-28f4-452c-b6fc-7df80295891c" -->
### "Plan doesn't match 0_context rules"
- Planning agent loads all guides automatically
- If pattern is wrong, it's a bug - report it
- User can request modifications before approval

<!-- section_id: "2b79fc0b-38fb-43ad-8606-e0797f74c2f8" -->
## Security Notes

<!-- section_id: "4d09f4ae-15e1-46fb-90c6-5d5ec96f5d9b" -->
### Canvas Authentication
- ✅ Both agents use canvas_authenticate.py script
- ❌ Never read .env file directly
- ✅ Credentials never exposed in logs
- ✅ Security boundary maintained

<!-- section_id: "3c934512-61cc-4088-af74-6adc85f42379" -->
### Tool Access
- **Planner**: Read-only tools (safe)
- **Executor**: Full access (after user approval)

<!-- section_id: "0914ec84-cf4f-4c10-813d-0935dde94c49" -->
### User Control
- User MUST approve plan before execution
- User can stop execution at any time
- All changes are tracked in git

<!-- section_id: "9f6b8c98-e0f2-4cac-8cae-40aceb33edb3" -->
## Success Criteria

Assignment setup is successful when:
- ✅ All todos marked completed
- ✅ Template renders without errors
- ✅ MCP visual verification passed
- ✅ Analysis references match rendered output
- ✅ Archive entry created
- ✅ PROJECT_CHANGELOG.md updated
- ✅ User receives completion report

<!-- section_id: "4c1d9aef-abd8-48b4-8e53-8998ac8de7fd" -->
## Next Steps

- **Full documentation**: `agent-patterns/assignment-workflow.md`
- **Planning agent details**: `.claude/agents/agent-assignment-planner.md`
- **Execution agent details**: `.claude/agents/agent-assignment-executor.md`
- **Canvas auth setup**: `trickle-down-0.5-environment/canvas-authentication-setup.md`

---

**Quick Start Version**: 1.0
**Created**: 2025-10-30
**Pattern**: Established with Unit 3 Assignment 1
