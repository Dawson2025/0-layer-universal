---
resource_id: "7497ba8d-616e-4ab7-8e1c-ad6d2a9d1a4f"
resource_type: "rule"
resource_name: "assignment-workflow"
---
# Structured Assignment Workflow: Two-Agent Architecture

**Pattern**: Separate planning and execution into specialized agents for reliable, automated assignment setup.

<!-- section_id: "309c25f9-35bd-4ffb-a315-4e4536221146" -->
## Overview

This workflow uses **two specialized agents** that work together to set up new unit assignments:

1. **assignment-planner**: Researches and creates implementation plans
2. **assignment-executor**: Executes approved plans with full tool access

This separation ensures:
- ✅ Plans are thoroughly researched before execution
- ✅ User reviews and approves before any changes
- ✅ Execution happens automatically with progress tracking
- ✅ Security boundaries are maintained (Canvas auth)
- ✅ All 0_context rules are followed

<!-- section_id: "a2fc0703-641f-4fae-8118-6d62f3f55183" -->
## Architecture

```
User Request
     ↓
assignment-planner (Planning Agent)
  - Authenticates with Canvas
  - Loads all 0_context guides
  - Analyzes existing patterns (Unit 2)
  - Creates detailed plan
     ↓
User Approval
     ↓
assignment-executor (Execution Agent)
  - Creates todo list from plan
  - Executes each step mechanically
  - Tracks progress in real-time
  - Verifies with MCP browser tools
  - Documents results
     ↓
Completed Assignment
```

<!-- section_id: "144918ce-0acf-40d7-bba2-65aa3093a3d9" -->
## When to Use This Pattern

**Use the assignment workflow when:**
- Setting up a new Unit (e.g., "Set up Unit 4")
- Creating a specific assignment (e.g., "Create Unit 3 Assignment 2")
- Reorganizing unit folders
- Completing templates following 0_context rules

**Don't use for:**
- Simple file edits (use direct editing)
- Quick questions (use main agent)
- Debugging issues (use main agent)

<!-- section_id: "8cb86942-87f2-402f-a8d2-0131efa42f5d" -->
## Workflow Steps

<!-- section_id: "9a9248e7-753c-4b64-8cdb-542e269edda1" -->
### Step 1: Invoke Planning Agent

**User action**: Request assignment setup

```
User: "Set up Unit 3 Assignment 1 following the rules in 0_context"
```

**AI action**: Invoke assignment-planner

```python
# The main agent should use the Task tool
Task(
    description="Plan Unit 3 Assignment 1 setup",
    subagent_type="assignment-planner",
    prompt="""
    Set up Unit 3 Assignment 1:
    - Canvas URL: https://byui.instructure.com/courses/352092/assignments/15477831
    - Follow all 0_context rules
    - Include absolute and relative path options
    - Create comprehensive plan for approval
    """,
    model="sonnet"
)
```

<!-- section_id: "4d3299eb-1ae0-44c4-bdd8-942e9762fe08" -->
### Step 2: Review Plan

**Planning agent outputs**:
- Detailed step-by-step plan
- Time estimates
- Files to create/modify
- Verification checklist
- Security notes (Canvas auth pattern)

**User reviews**:
- Verifies plan follows 0_context rules
- Checks Canvas assignment details
- Approves or requests modifications

<!-- section_id: "6077cedc-cae2-44b5-b93b-5764ff3ce926" -->
### Step 3: Invoke Execution Agent

**User action**: Approve plan and request execution

```
User: "Approved! Execute this plan."
```

**AI action**: Invoke assignment-executor with approved plan

```python
Task(
    description="Execute Unit 3 Assignment 1 plan",
    subagent_type="assignment-executor",
    prompt="""
    Execute the following approved plan:

    [PASTE APPROVED PLAN HERE]

    Requirements:
    - Create todos immediately
    - Track progress in real-time
    - Verify with MCP browser tools
    - Document in changelog
    """
)
```

<!-- section_id: "a7b16e4e-6671-4d2f-9351-32423b754167" -->
### Step 4: Monitor Execution

**Execution agent**:
- Creates todo list from plan
- Marks each step in_progress → completed
- Reports any blockers immediately
- Shows progress updates

**User can**:
- Monitor todo progress
- See real-time updates
- Intervene if needed

<!-- section_id: "b8023363-2e1f-463f-8a0e-7da7d69dff62" -->
### Step 5: Verification

**Execution agent automatically**:
- Renders template to HTML
- Uses MCP playwright/chrome-devtools for visual verification
- Takes screenshots for documentation
- Verifies analysis matches rendered output
- Creates archive entry
- Updates PROJECT_CHANGELOG.md

<!-- section_id: "c2435843-fbce-4181-8736-9436a1193ac9" -->
### Step 6: Completion Report

**Execution agent outputs**:
```markdown
## ✅ Assignment Complete!

### Created/Modified Files:
- Projects/Unit_3/assignment_1/unit3_task1.qmd
- Templates/Unit_3/assignment_1/unit3_task1_template.qmd
- _quarto.yml (navigation updated)

### Verification:
- Rendered: Templates/Unit_3/assignment_1/unit3_task1_template.html
- Screenshot: .playwright-mcp/unit3_assignment1_verification.png
- Analysis matches visuals ✅

### Documentation:
- Archive: 0_context/.../unit-3-changes/2025-10-30-HHMMSS-description.md
- Changelog: PROJECT_CHANGELOG.md updated
```

<!-- section_id: "0ba83e29-11b3-43de-9e88-e735d3ba670e" -->
## Benefits

| Traditional Single-Agent | Two-Agent Architecture |
|--------------------------|------------------------|
| Planning mixed with execution | Separated concerns |
| User must monitor constantly | Approve once, agent executes |
| Plan mode blocks all edits | Execution agent has full access |
| Context diluted | Each agent optimized for its role |
| Manual todo tracking | Automated progress tracking |
| Inconsistent verification | MCP verification required |

<!-- section_id: "e31adae6-7973-4e16-b07f-10bf85f24694" -->
## Security Considerations

<!-- section_id: "6199a4f3-e5c8-46e6-989c-63f0ddafa5a5" -->
### Canvas Authentication

**Both agents enforce**:
- ✅ MUST use `canvas_authenticate.py` script
- ❌ NEVER read `.env` file directly
- ✅ Credentials loaded via security boundary
- ❌ Credentials never exposed in output

**Planning agent**:
- Loads credentials for Canvas research
- Uses MCP browser tools to access Canvas
- Extracts assignment content
- Never stores or exposes credentials

**Execution agent**:
- Doesn't typically need Canvas access
- If needed, uses same authentication pattern
- Focus is on local file operations

<!-- section_id: "8b87344b-7c24-4f02-91c0-a48c701ce1f2" -->
### Tool Access

**Planning agent** (limited tools):
- Read, Glob, Grep, Bash (readonly)
- WebFetch, WebSearch
- MCP browser tools (for Canvas)
- NO file editing/writing

**Execution agent** (full tools):
- ALL tools inherited from main thread
- Edit, Write, Bash (full)
- File operations (mkdir, git mv)
- MCP browser tools (for verification)
- TodoWrite for progress tracking

<!-- section_id: "5d229206-b68b-4c39-89c1-e19b07027ba4" -->
## Example: Unit 3 Assignment 1

**User request**:
```
Set up Unit 3 Assignment 1 and include both absolute and relative path options for database stuff and the like if needed.
```

**Planning agent**:
1. Authenticated with Canvas using canvas_authenticate.py
2. Extracted assignment: "Missing Data & JSON"
3. Analyzed Unit 2 pattern (assignment folder structure)
4. Created plan with 8 phases (18 steps total)
5. Estimated 70 minutes
6. Noted JSON uses URL (no database paths needed for this assignment)

**User**: Approved plan

**Execution agent**:
1. Created 18 todos
2. Reorganized Unit_3 folder structure
3. Moved 7 files to assignment folders
4. Updated all template paths
5. Completed template with missing data analysis
6. Rendered and verified with MCP playwright
7. Created archive entry
8. Updated PROJECT_CHANGELOG.md
9. Reported completion with file list

**Result**: Fully functional Unit 3 Assignment 1 in ~70 minutes, hands-off after approval

<!-- section_id: "a953184f-33e3-4acd-abf3-a67180797032" -->
## Reference Example

See the completed Unit 3 Assignment 1 for a working example:
- Archive: `0_context/0_context/trickle-down-2-features/templates/unit-3-changes/2025-10-30-143500-unit3-assignment-1-reorganization-and-completion.md`
- Agents: `.claude/agents/agent-assignment-planner.md` and `.claude/agents/agent-assignment-executor.md`

<!-- section_id: "858dead3-7573-4de6-990e-e317cb892a2f" -->
## Related Documentation

- **Planning Agent Details**: `agent-patterns/assignment-planner-agent.md`
- **Execution Agent Details**: `agent-patterns/assignment-executor-agent.md`
- **Quick Start Guide**: `agent-patterns/assignment-quick-start.md`
- **Canvas Authentication**: `trickle-down-0.5-environment/canvas-authentication-setup.md`
- **Unit Folder Setup**: `trickle-down-2-features/templates/unit-folder-setup-guide.md`
- **Template Verification**: `trickle-down-2-features/templates/template-verification-and-completion-guide.md`

---

**Created**: 2025-10-30
**Pattern Established**: Unit 3 Assignment 1
**Maintained By**: AI Agent documentation system
