---
resource_id: "73bcde88-ef62-4350-9b9c-3818b203d841"
resource_type: "output"
resource_name: "NATIVE_FEATURES"
---
# Cursor Agent CLI — Native Features

**Date**: 2026-02-27
**Focus**: What the CLI tool provides natively

---

<!-- section_id: "b2941056-3629-424f-ab27-4fc4c240bb19" -->
## Overview

Cursor Agent CLI provides autonomous task execution with:

1. **Task Execution** (autonomous agent execution)
2. **Session Management** (persistence across turns)
3. **Shell Command Execution** (with user approval)
4. **MCP Tool Integration** (external tool access)
5. **State Management** (remembers context between runs)
6. **Cloud Agents** (remote execution option)
7. **Plan Mode** (agent generates plans before executing)
8. **Resume Capability** (continue interrupted tasks)
9. **Error Handling** (retry logic, fallback)
10. **Logging** (execution history and outputs)

---

<!-- section_id: "6a30267e-7bf1-4407-84dd-193e87f2def5" -->
## 1. Task Execution

<!-- section_id: "f1f72fff-7d78-4631-9a10-69f8136e14e7" -->
### The Mechanism

Accept task descriptions and execute autonomously:

```bash
cursor agent "Refactor src/auth.js to use async/await"
```

**What Agent Does**:
- Parse task description
- Analyze project structure
- Create execution plan
- Execute steps sequentially
- Request user approval for shell commands
- Report results

<!-- section_id: "c9422c08-8e4f-4ef8-a8d9-96d1c72b12ee" -->
### What Agent Does NOT Do
- Execute shell commands without approval
- Make destructive changes without confirmation
- Guarantee task completion (may fail or need guidance)
- Provide rollback capability

---

<!-- section_id: "edcb5119-f4e7-41d3-9bd4-aac85c4c9099" -->
## 2. Session Management

<!-- section_id: "3116d040-87f7-41f6-bd8e-2fad51c77fd3" -->
### The Mechanism

Sessions persist state across multiple invocations:

```bash
cursor agent --workspace ~/my-project
# Creates session, returns session-id

cursor agent resume session-id
# Continues previous work
```

**Storage**: `~/.cursor/sessions/[session-id]/`

<!-- section_id: "13c4690e-f29e-4157-a934-dbc3791ddb99" -->
### What Agent Does
- Create sessions on-demand
- Save state after each turn
- Allow resumption within time window
- Maintain full execution history

<!-- section_id: "65ad7767-fd9b-4908-891f-5c89cca19ceb" -->
### What Agent Does NOT Do
- Provide session recovery after crashes
- Support session sharing between users
- Offer session migration

---

<!-- section_id: "103125f6-6777-41c7-a27d-8ead50eeb950" -->
## 3. Shell Command Execution

<!-- section_id: "b9f7400b-69b0-4bcb-85c8-97a0680f83a0" -->
### The Mechanism

Execute shell commands with approval gate:

```
Agent: "I'll run npm test to verify changes"
Request approval: [y/n]? y
> npm test
✅ Tests pass (1200ms)
```

**Approval Types**:
- Interactive: Ask for each command
- Batch: Pre-approve certain commands
- Manual: User approves all

<!-- section_id: "3703d5d1-505e-4c4f-b5ca-b3115b2f6e45" -->
### What Agent Does
- Execute approved commands
- Capture output
- Handle errors
- Report results

<!-- section_id: "8cc3b677-4f51-49bb-8257-fa30c4896383" -->
### What Agent Does NOT Do
- Execute without approval
- Clean up after failed commands
- Manage long-running processes

---

<!-- section_id: "c1ef866e-47b0-4bad-87fd-cfd412bba247" -->
## 4. MCP Tool Integration

<!-- section_id: "4a3f9c65-03a9-471c-a1c8-98d33b2f7ab8" -->
### The Mechanism

Access external tools via MCP protocol:

```
Agent uses tools:
- canvas_assignment_list (Canvas API)
- github_search (GitHub search)
- execute_javascript (custom tool)
```

<!-- section_id: "d182b492-56a5-47f4-bfcc-121c50f6f779" -->
### What Agent Does
- Load configured MCP servers
- Call tools when needed
- Handle tool errors
- Return results to context

<!-- section_id: "a0b7c3da-c709-4d80-8475-db159aa29d4a" -->
### What Agent Does NOT Do
- Auto-discover tools
- Provide tool documentation
- Validate tool safety

---

<!-- section_id: "fa5b49d9-f6c2-4d50-9776-25b27660e133" -->
## 5. State Management

<!-- section_id: "f11e1d26-d249-4c93-b60b-c1aab8221968" -->
### The Mechanism

Remember context across turns:

```json
{
  "session_id": "abc123",
  "current_task": "...",
  "completed_steps": [...],
  "file_modifications": [...],
  "conversation_history": [...],
  "working_memory": {...}
}
```

<!-- section_id: "1c0d55ba-b166-46c0-9406-e9b46015920f" -->
### What Agent Does
- Save state after each turn
- Load state on resume
- Maintain context continuity
- Track modifications

<!-- section_id: "74ecb2b0-32a7-46bd-9e59-84f54d69da4b" -->
### What Agent Does NOT Do
- Provide conflict resolution (parallel modifications)
- Offer version control
- Merge concurrent changes

---

<!-- section_id: "79450e71-0e58-4235-8256-f0006165e23e" -->
## 6. Cloud Agents

<!-- section_id: "be2b2aa1-225e-40c5-a78d-6982e1ce5cf7" -->
### The Mechanism

Remote execution with cloud infrastructure:

```bash
cursor agent --cloud "Implement user authentication"
```

<!-- section_id: "30dc9610-b320-468c-9d2f-e3ad2e6f503e" -->
### What Agent Does
- Submit task to cloud
- Monitor execution
- Stream results
- Provide resumption tokens

<!-- section_id: "0c012c99-1bf9-4d57-b4e4-923e17acacdb" -->
### What Agent Does NOT Do
- Guarantee execution time
- Provide resource scaling
- Offer cost optimization

---

<!-- section_id: "2463f520-d9b9-4f58-aedf-ab8a68d7b1ba" -->
## 7. Plan Mode

<!-- section_id: "0f5f39b2-8dbf-41a0-89b3-0d513b72fbf5" -->
### The Mechanism

Agent creates plan before execution:

```bash
cursor agent --plan "Refactor database queries"
# Generates multi-step plan
# User approves plan
# Agent executes
```

<!-- section_id: "c13380a4-695c-4b63-948a-18b9802ded73" -->
### What Agent Does
- Analyze task
- Generate step-by-step plan
- Present plan for approval
- Execute approved plan

<!-- section_id: "0e1834af-ba98-4370-b99f-360983dba38c" -->
### What Agent Does NOT Do
- Guarantee plan success
- Adapt plan mid-execution
- Provide alternative plans

---

<!-- section_id: "51a78a95-69c1-4b9b-9775-9b2ef4974b04" -->
## 8. Resume Capability

<!-- section_id: "1b338b30-7098-4c27-bac6-5de71d73a5fc" -->
### The Mechanism

Continue interrupted sessions:

```bash
cursor agent resume session-id
# Loads previous state
# Continues from last checkpoint
```

<!-- section_id: "e3e3c439-cbc6-4745-b32c-a910e018a753" -->
### What Agent Does
- Save checkpoints
- Allow resumption
- Maintain context

<!-- section_id: "dc800b2e-a7e7-45ca-a380-bef3690b2341" -->
### What Agent Does NOT Do
- Handle network interruptions gracefully
- Provide checkpoint rollback
- Merge concurrent modifications

---

<!-- section_id: "2b4a5751-ddd0-46a9-b04c-a6365d68f7d5" -->
## 9. Error Handling

<!-- section_id: "c74ace7f-37f5-4b0f-b736-b1c5a3e0c377" -->
### The Mechanism

Handle failures and retry:

```
Step 1: npm test
❌ Error: Tests failed (3 failures)

Agent analyzes failure
Suggests fix
Retries with modifications
✅ Tests pass (retry 1)
```

<!-- section_id: "0cf9c7ed-9e9e-4e67-a7cc-06bb2e1062e6" -->
### What Agent Does
- Catch errors
- Analyze failures
- Suggest corrections
- Retry with modifications

<!-- section_id: "c6eb88fe-9ac6-4757-96ea-7a3bddc2fbc9" -->
### What Agent Does NOT Do
- Guarantee error recovery
- Provide rollback
- Auto-fix all errors

---

<!-- section_id: "3f3a4721-7a45-40b3-8d77-9494505b096d" -->
## 10. Logging

<!-- section_id: "ccc78b9f-0858-4cb6-b376-2c7af91d68c1" -->
### The Mechanism

Track execution history:

```
~/.cursor/sessions/[session-id]/
├── history.log (full execution log)
├── state.json (current state snapshot)
└── modifications/ (file changes record)
```

<!-- section_id: "082da881-2749-4150-9177-9f3cd3e7a756" -->
### What Agent Does
- Log all operations
- Record output
- Track state changes
- Enable debugging

<!-- section_id: "5edd2fcb-9652-4373-bcd5-859d5f021319" -->
### What Agent Does NOT Do
- Rotate logs automatically
- Provide log analysis
- Offer log replay

---

<!-- section_id: "7b23165d-7654-48e2-a7d8-3dd84feac6d5" -->
## Summary: Native = Mechanisms Provided

✅ **Native**: Execute tasks autonomously with user approval gates
❌ **Not native**: You decide which tasks to delegate

✅ **Native**: Persist session state across invocations
❌ **Not native**: You decide session boundaries

✅ **Native**: Execute shell commands
❌ **Not native**: You decide which commands are safe

✅ **Native**: Call MCP tools
❌ **Not native**: You configure which tools

✅ **Native**: Generate execution plans
❌ **Not native**: You approve or modify plans

