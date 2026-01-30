# Quick Start: Structured Assignment Workflow

**TL;DR**: Use `assignment-planner` to create a plan, get user approval, then use `assignment-executor` to execute it automatically.

## 1-Minute Overview

```
User Request → assignment-planner → Plan → User Approval → assignment-executor → Done
```

## Quick Example

### User Says:
```
"Set up Unit 3 Assignment 1"
```

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

## Detailed Walkthrough

### Step 1: User Makes Request

User wants to set up a new assignment following 0_context rules.

**Example requests:**
- "Set up Unit 4 Assignment 2"
- "Create Unit 5 Task 1 with Canvas assignment https://..."
- "Organize Unit 3 into assignment folders"

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

### Step 4: User Approves Plan

**User says:**
- "Approved!"
- "Looks good, execute it"
- "Go ahead with this plan"

**OR requests changes:**
- "Can you also add X?"
- "Skip the folder reorganization"

If changes requested, re-invoke planning agent with modifications.

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

## Common Patterns

### Pattern 1: New Unit Assignment
```
User: "Set up Unit 4 Assignment 1"
→ planner extracts from Canvas
→ user approves
→ executor creates folders, moves files, completes template
→ done
```

### Pattern 2: Template Only
```
User: "Complete Unit 3 Assignment 2 template"
→ planner identifies existing structure, plans completion
→ user approves
→ executor fills in analysis and code
→ done
```

### Pattern 3: Folder Reorganization
```
User: "Reorganize Unit 5 like Unit 2"
→ planner analyzes Unit 2 pattern, creates reorg plan
→ user approves
→ executor moves files, updates paths
→ done
```

## Troubleshooting

### "Canvas authentication failed"
- Verify `.env` file exists with credentials
- Test: `python3 0_context/.../canvas_authenticate.py`
- Check credentials are correct

### "MCP browser tools not working"
- Try different MCP server: playwright → chrome-devtools → browser
- Check MCP configuration in `~/.config/mcp/mcp.json`

### "Template rendering failed"
- Execution agent will render from template directory
- Check Quarto env vars (or render from template dir)
- Verify Python packages installed in .venv

### "Plan doesn't match 0_context rules"
- Planning agent loads all guides automatically
- If pattern is wrong, it's a bug - report it
- User can request modifications before approval

## Security Notes

### Canvas Authentication
- ✅ Both agents use canvas_authenticate.py script
- ❌ Never read .env file directly
- ✅ Credentials never exposed in logs
- ✅ Security boundary maintained

### Tool Access
- **Planner**: Read-only tools (safe)
- **Executor**: Full access (after user approval)

### User Control
- User MUST approve plan before execution
- User can stop execution at any time
- All changes are tracked in git

## Success Criteria

Assignment setup is successful when:
- ✅ All todos marked completed
- ✅ Template renders without errors
- ✅ MCP visual verification passed
- ✅ Analysis references match rendered output
- ✅ Archive entry created
- ✅ PROJECT_CHANGELOG.md updated
- ✅ User receives completion report

## Next Steps

- **Full documentation**: `agent-patterns/assignment-workflow.md`
- **Planning agent details**: `.claude/agents/agent-assignment-planner.md`
- **Execution agent details**: `.claude/agents/agent-assignment-executor.md`
- **Canvas auth setup**: `trickle-down-0.5-environment/canvas-authentication-setup.md`

---

**Quick Start Version**: 1.0
**Created**: 2025-10-30
**Pattern**: Established with Unit 3 Assignment 1
