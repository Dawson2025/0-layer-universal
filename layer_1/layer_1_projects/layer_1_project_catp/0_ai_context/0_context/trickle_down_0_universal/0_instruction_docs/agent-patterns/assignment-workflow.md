---
resource_id: "180d412d-4285-4ce3-9ab1-9f8ac46b6d31"
resource_type: "document"
resource_name: "assignment-workflow"
---
# Structured Assignment Workflow: Two-Agent Architecture

**Pattern**: Separate planning and execution into specialized agents for reliable, automated assignment setup.

<!-- section_id: "7ae65c27-d9f3-4e54-9389-6e7dc6cc7eaa" -->
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

<!-- section_id: "87e3060b-4e43-4b0c-9fb0-d88229d6064c" -->
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

<!-- section_id: "8110b1cf-ea92-4179-9960-4053efd1274a" -->
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

<!-- section_id: "6e4d1192-3c62-4a2c-9f0f-91f7823382b1" -->
## Workflow Steps

<!-- section_id: "e736a3a1-1fb3-4321-94ae-5d9eb978b90a" -->
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

<!-- section_id: "f92fd3cf-3d80-406e-83fa-aec60e37746b" -->
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

<!-- section_id: "3674866f-aaf7-4e78-a3c8-635e763691fe" -->
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

<!-- section_id: "aaaad541-1e8d-48ad-ba78-2ac0fdc2077f" -->
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

<!-- section_id: "9a7b3e5b-9d19-499a-b137-bd0cbbf11351" -->
### Step 5: Verification

**Execution agent automatically**:
- Renders template to HTML
- Uses MCP playwright/chrome-devtools for visual verification
- Takes screenshots for documentation
- Verifies analysis matches rendered output
- Creates archive entry
- Updates PROJECT_CHANGELOG.md

<!-- section_id: "5a4de1aa-f838-4e2e-ae79-905a97d49195" -->
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

<!-- section_id: "80c06be8-ccd3-4de7-8c9c-c0d0beb2a362" -->
## Benefits

| Traditional Single-Agent | Two-Agent Architecture |
|--------------------------|------------------------|
| Planning mixed with execution | Separated concerns |
| User must monitor constantly | Approve once, agent executes |
| Plan mode blocks all edits | Execution agent has full access |
| Context diluted | Each agent optimized for its role |
| Manual todo tracking | Automated progress tracking |
| Inconsistent verification | MCP verification required |

<!-- section_id: "73944427-315e-45c4-bf33-57301488d302" -->
## Security Considerations

<!-- section_id: "8cab84dd-e915-4ff5-ac9f-b1b72d6a189f" -->
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

<!-- section_id: "06b124a9-dddb-4cc5-b509-547bab2585cc" -->
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

<!-- section_id: "82a016ce-fc9b-4737-9877-5b3478bc4b17" -->
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

<!-- section_id: "48228680-6f9c-4bd0-a662-fe7e77ffe964" -->
## Reference Example

See the completed Unit 3 Assignment 1 for a working example:
- Archive: `0_context/0_context/trickle-down-2-features/templates/unit-3-changes/2025-10-30-143500-unit3-assignment-1-reorganization-and-completion.md`
- Agents: `.claude/agents/agent-assignment-planner.md` and `.claude/agents/agent-assignment-executor.md`

<!-- section_id: "6ec413d9-fb7d-4c4b-80b3-8019aea176dd" -->
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
