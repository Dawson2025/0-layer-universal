---
resource_id: "9a97a596-94be-42b9-93d1-b49d53d2e313"
resource_type: "rule"
resource_name: "init-command"
---
# Universal AI Agent Initialization System
*TD0 Universal: /init Command Protocol*

<!-- section_id: "3316751c-9b4f-46b2-985f-597e9db32d67" -->
## Purpose
The `/init` command provides complete project context to any AI coding agent by loading the Trickle-Down documentation hierarchy in the correct order.

<!-- section_id: "c84fd80c-e626-4597-9528-1fca768ab0cf" -->
## Command Specification

<!-- section_id: "7de8cc69-ed72-4cf9-8682-fb80ab3cf5a8" -->
### Usage
```
/init [optional: specific-focus-area]
```

**Examples**:
- `/init` - Full context loading
- `/init authentication` - Full context + focus on authentication feature
- `/init testing` - Full context + focus on testing workflows

<!-- section_id: "6bf9b581-0fea-44fa-9355-300b7beb09db" -->
### Loading Sequence

#### Step 1: Agent Declaration Protocol
**AI Agent must declare**:
```
AI Agent: [Agent Name - e.g., Warp AI Assistant, Claude Code, Cursor, etc.]
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [focus area if specified, otherwise "Full Context Loading"]
Initialize: Starting Trickle-Down context loading...
```

#### Step 2: TD0 Universal Context Loading
**Load in order**:
1. `docs/0_universal/trickle-down-0.0-ai-coding-systems/ai-coding-system-selection.md`
   - Understanding of why we use structured AI coding systems
   - Available options and selection criteria

2. `docs/1_trickle_down/trickle-down-0.5-environment/ai-agent-setup.md`
   - This project's WSL Ubuntu environment requirements
   - Agent-specific environment integration

3. `docs/1_trickle_down/trickle-down-0.5-environment/agent-specific/[agent-name]-spec-kit.md`
   - Agent-specific Spec Kit integration instructions
   - Session management protocols

4. `docs/0_context/0_universal_instructions/terminal-tool-replacement.md`
   - Critical terminal tool replacement protocol
   - Mandatory use of robust script runner system
   - Prevention of terminal hanging issues

5. `docs/0_context/0_universal_instructions/manual-steps-automation.md`
   - Mandatory execution of manual steps by AI agents
   - Browser automation and web interface interaction
   - No delegation of manual tasks to users

#### Step 3: TD1 Project Context Loading
**Load in order**:
1. `docs/1_trickle_down/trickle-down-1-project/constitution.md`
   - Complete project constitution with principles and standards
   - Development process requirements and non-negotiables

2. `docs/1_trickle_down/trickle-down-1-project/trickle-down-1.0-spec-kit-implementation/spec-kit-selection.md`
   - Why this project uses GitHub Spec Kit
   - Spec Kit workflow phases and implementation

3. `docs/for_ai/requirements/USER_STORIES.md` (first 50 lines)
   - Core user stories (US-001 through US-010+)
   - Understanding of user-driven development

#### Step 4: TD2 Feature Context (if focus area specified)
**If focus area provided**:
1. `docs/2_features/[focus-area]/feature-spec.md`
   - Detailed feature specification
   - Acceptance criteria and technical requirements

2. `docs/2_features/[focus-area]/implementation-plan.md` 
   - Implementation planning context
   - Architecture and environmental considerations

3. `docs/2_features/[focus-area]/implementation-tasks.md`
   - Concrete implementation tasks
   - Dependencies and parallelization strategy

#### Step 5: Current Project State Assessment
**Execute commands to understand current state**:
1. `pwd` - Verify we're in correct WSL Ubuntu location
2. `git status` - Check current Git state and uncommitted changes  
3. `ls -la features/` - See current feature development status
4. Check if Golden Rule test can run: `python scripts/automation/run_user_stories.py --help`

#### Step 6: Agent Readiness Declaration
**AI Agent declares**:
```
Context Loading: Complete ✅
Environment: WSL Ubuntu verified ✅  
Project: Language Tracker constitution loaded ✅
Coding System: GitHub Spec Kit workflow ready ✅
Current State: [summarize git status, features, etc.] ✅
Focus Area: [if specified] ready for development ✅

Ready for: [Spec Kit phase or development task]
Session Goals: [based on focus area or ask user]
```

<!-- section_id: "61dff4f8-35f3-4d48-8437-5ff953b7f919" -->
## Agent-Specific Implementation

<!-- section_id: "36323f63-dcab-40d9-92c7-d48e9fadc113" -->
### For Warp AI Assistant
**Tools to use during /init**:
- `read_any_files` - Load all documentation in sequence
- `run_command` - Execute project state assessment commands
- `create_todo_list` - Set up session goals based on focus area
- `search_codebase` - Understand existing implementation if needed

<!-- section_id: "0a1dd559-a218-477a-b22f-581b6bdc25a5" -->
### For Claude Code Agent  
**Integration points**:
- VS Code workspace loading
- Extension configuration verification
- File tree navigation for documentation reading

<!-- section_id: "343ce181-5d7e-4265-9e76-04d4ae8c6e76" -->
### For Cursor Agent
**IDE-specific features**:
- Project file indexing
- Documentation panel setup
- Context window management

**Critical Terminal Tool Rules**:
- **MANDATORY**: Read `MASTER_DOCUMENTATION.md` for complete documentation
- **Universal Terminal**: See `UNIVERSAL_TERMINAL_EXECUTION.md` for universal best practices
- **Cursor-Specific**: If you are a Cursor agent, see `CURSOR_TERMINAL_EXECUTION.md` for Python script handling
- Node.js commands → Use agent's terminal tool directly: `<agent_tool>("npx <command> ; exit")`
- System commands → Use agent's terminal tool directly: `<agent_tool>("<command> ; exit")`
- Always add `; exit` to commands to prevent hanging on both success and failure

<!-- section_id: "b41678b7-38db-4b9d-8c52-5c9df0b3b368" -->
### For GitHub Copilot Agent
**Preparation steps**:
- Repository context synchronization
- Code completion model warming
- Documentation embedding preparation

<!-- section_id: "71cfe0f9-9845-4642-a530-8050817671d4" -->
## Error Handling

<!-- section_id: "639f1d9a-4c3c-47f2-aa79-6bff086a3c02" -->
### Missing Documentation
**If any TD file is missing**:
1. Report which files are missing
2. Continue with available documentation
3. Note gaps in context loading
4. Suggest creation of missing documentation

<!-- section_id: "6637c528-9aa7-46e5-948e-e705a269e099" -->
### Environment Issues
**If WSL Ubuntu verification fails**:
1. Report environment mismatch
2. Provide environment setup guidance  
3. Reference TD0.5 environment documentation
4. Suggest environment switching if needed

<!-- section_id: "1038f4a7-1042-40b7-9587-01afc5c1c5c7" -->
### Focus Area Not Found
**If specified focus area doesn't exist**:
1. List available feature areas
2. Suggest closest match
3. Offer to create new feature specification
4. Default to general context loading

---
*Universal /init Command System*
*All AI Agents: Use this protocol for consistent project context loading*
