---
resource_id: "97108440-c616-4ce6-93d4-2a45e2a56678"
resource_type: "rule"
resource_name: "assignment-quick-start"
---
# Quick Start: Structured Assignment Workflow

**TL;DR**: Use `assignment-planner` to create a plan, get user approval, then use `assignment-executor` to execute it automatically.

<!-- section_id: "b0850a29-590c-4d90-8718-d8ee29049e97" -->
## 1-Minute Overview

```
User Request → assignment-planner → Plan → User Approval → assignment-executor → Done
```

<!-- section_id: "a469b128-665b-46fa-90da-9173dd570f25" -->
## Quick Example

<!-- section_id: "c946b270-40ee-48bf-b169-2ca1bb34a774" -->
### User Says:
```
"Set up Unit 3 Assignment 1"
```

<!-- section_id: "c6254e7c-f255-40fa-a043-adecb03636e1" -->
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

<!-- section_id: "aa013ca2-8559-4ed1-928c-ed70fb409fe5" -->
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

<!-- section_id: "7c1ca8fa-22df-4f01-980c-4db1c62977fc" -->
## Detailed Walkthrough

<!-- section_id: "7cd1f292-6336-4186-b595-0e3ad1151a34" -->
### Step 1: User Makes Request

User wants to set up a new assignment following 0_context rules.

**Example requests:**
- "Set up Unit 4 Assignment 2"
- "Create Unit 5 Task 1 with Canvas assignment https://..."
- "Organize Unit 3 into assignment folders"

<!-- section_id: "7a8785ad-fa5f-4fd4-9cce-dae247c9635f" -->
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

<!-- section_id: "e9c93bd8-5b13-4a95-b7b0-061b01ae7958" -->
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

<!-- section_id: "a8efb923-85be-4f01-a5a4-5273fb37c7dc" -->
### Step 4: User Approves Plan

**User says:**
- "Approved!"
- "Looks good, execute it"
- "Go ahead with this plan"

**OR requests changes:**
- "Can you also add X?"
- "Skip the folder reorganization"

If changes requested, re-invoke planning agent with modifications.

<!-- section_id: "2793180d-ebeb-4296-91a3-9e8cbd7e3b9b" -->
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

<!-- section_id: "fda78fe3-b6cc-4067-a448-a4465d0a1642" -->
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

<!-- section_id: "6ac08f0c-2146-4887-88bd-e4989658dd05" -->
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

<!-- section_id: "6c9685ef-2362-483e-9a96-b1d905e894b8" -->
## Common Patterns

<!-- section_id: "ebc2cde5-5c6a-415c-9103-c63fa173039c" -->
### Pattern 1: New Unit Assignment
```
User: "Set up Unit 4 Assignment 1"
→ planner extracts from Canvas
→ user approves
→ executor creates folders, moves files, completes template
→ done
```

<!-- section_id: "d5ed321d-aa3a-4e21-893c-534ba4920a2c" -->
### Pattern 2: Template Only
```
User: "Complete Unit 3 Assignment 2 template"
→ planner identifies existing structure, plans completion
→ user approves
→ executor fills in analysis and code
→ done
```

<!-- section_id: "2d65ecc9-f0d9-4b9e-a642-bfcba287a608" -->
### Pattern 3: Folder Reorganization
```
User: "Reorganize Unit 5 like Unit 2"
→ planner analyzes Unit 2 pattern, creates reorg plan
→ user approves
→ executor moves files, updates paths
→ done
```

<!-- section_id: "268d55b0-9b0d-48d3-a217-4b25547b0306" -->
## Troubleshooting

<!-- section_id: "66555642-35f7-403b-a1df-a06f58a203b6" -->
### "Canvas authentication failed"
- Verify `.env` file exists with credentials
- Test: `python3 0_context/.../canvas_authenticate.py`
- Check credentials are correct

<!-- section_id: "3af262e1-a735-4313-a5b0-8e616898a92c" -->
### "MCP browser tools not working"
- Try different MCP server: playwright → chrome-devtools → browser
- Check MCP configuration in `~/.config/mcp/mcp.json`

<!-- section_id: "c3cd3de3-5ef7-4ee3-90ea-f549b76d0997" -->
### "Template rendering failed"
- Execution agent will render from template directory
- Check Quarto env vars (or render from template dir)
- Verify Python packages installed in .venv

<!-- section_id: "8f18ae27-d579-459f-9739-18b9c0689e03" -->
### "Plan doesn't match 0_context rules"
- Planning agent loads all guides automatically
- If pattern is wrong, it's a bug - report it
- User can request modifications before approval

<!-- section_id: "b8ffba31-adef-41be-80d1-52d37de7283f" -->
## Security Notes

<!-- section_id: "57203cf3-9484-4cf8-b311-63f20756797e" -->
### Canvas Authentication
- ✅ Both agents use canvas_authenticate.py script
- ❌ Never read .env file directly
- ✅ Credentials never exposed in logs
- ✅ Security boundary maintained

<!-- section_id: "0c6f605e-a13d-425a-a7d6-bf7c20dc4095" -->
### Tool Access
- **Planner**: Read-only tools (safe)
- **Executor**: Full access (after user approval)

<!-- section_id: "5ba407ad-a7b1-495d-aa59-2d692ae0b69f" -->
### User Control
- User MUST approve plan before execution
- User can stop execution at any time
- All changes are tracked in git

<!-- section_id: "dbf747fe-37a8-40b0-8a67-df9fded30fce" -->
## Success Criteria

Assignment setup is successful when:
- ✅ All todos marked completed
- ✅ Template renders without errors
- ✅ MCP visual verification passed
- ✅ Analysis references match rendered output
- ✅ Archive entry created
- ✅ PROJECT_CHANGELOG.md updated
- ✅ User receives completion report

<!-- section_id: "472ba1dd-ba31-490c-beb4-e8b8c84c7e99" -->
## Next Steps

- **Full documentation**: `agent-patterns/assignment-workflow.md`
- **Planning agent details**: `.claude/agents/agent-assignment-planner.md`
- **Execution agent details**: `.claude/agents/agent-assignment-executor.md`
- **Canvas auth setup**: `trickle-down-0.5-environment/canvas-authentication-setup.md`

---

**Quick Start Version**: 1.0
**Created**: 2025-10-30
**Pattern**: Established with Unit 3 Assignment 1
