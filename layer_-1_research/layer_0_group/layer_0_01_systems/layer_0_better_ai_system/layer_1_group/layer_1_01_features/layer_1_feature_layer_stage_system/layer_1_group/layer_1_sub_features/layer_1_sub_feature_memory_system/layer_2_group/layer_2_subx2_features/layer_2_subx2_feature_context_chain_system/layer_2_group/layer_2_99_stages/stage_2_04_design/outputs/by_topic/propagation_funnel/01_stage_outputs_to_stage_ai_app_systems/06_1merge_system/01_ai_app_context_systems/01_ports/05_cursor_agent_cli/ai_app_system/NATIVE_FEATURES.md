# Cursor Agent CLI — Native Features

**Date**: 2026-02-27
**Focus**: What the CLI tool provides natively

---

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

## 1. Task Execution

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

### What Agent Does NOT Do
- Execute shell commands without approval
- Make destructive changes without confirmation
- Guarantee task completion (may fail or need guidance)
- Provide rollback capability

---

## 2. Session Management

### The Mechanism

Sessions persist state across multiple invocations:

```bash
cursor agent --workspace ~/my-project
# Creates session, returns session-id

cursor agent resume session-id
# Continues previous work
```

**Storage**: `~/.cursor/sessions/[session-id]/`

### What Agent Does
- Create sessions on-demand
- Save state after each turn
- Allow resumption within time window
- Maintain full execution history

### What Agent Does NOT Do
- Provide session recovery after crashes
- Support session sharing between users
- Offer session migration

---

## 3. Shell Command Execution

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

### What Agent Does
- Execute approved commands
- Capture output
- Handle errors
- Report results

### What Agent Does NOT Do
- Execute without approval
- Clean up after failed commands
- Manage long-running processes

---

## 4. MCP Tool Integration

### The Mechanism

Access external tools via MCP protocol:

```
Agent uses tools:
- canvas_assignment_list (Canvas API)
- github_search (GitHub search)
- execute_javascript (custom tool)
```

### What Agent Does
- Load configured MCP servers
- Call tools when needed
- Handle tool errors
- Return results to context

### What Agent Does NOT Do
- Auto-discover tools
- Provide tool documentation
- Validate tool safety

---

## 5. State Management

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

### What Agent Does
- Save state after each turn
- Load state on resume
- Maintain context continuity
- Track modifications

### What Agent Does NOT Do
- Provide conflict resolution (parallel modifications)
- Offer version control
- Merge concurrent changes

---

## 6. Cloud Agents

### The Mechanism

Remote execution with cloud infrastructure:

```bash
cursor agent --cloud "Implement user authentication"
```

### What Agent Does
- Submit task to cloud
- Monitor execution
- Stream results
- Provide resumption tokens

### What Agent Does NOT Do
- Guarantee execution time
- Provide resource scaling
- Offer cost optimization

---

## 7. Plan Mode

### The Mechanism

Agent creates plan before execution:

```bash
cursor agent --plan "Refactor database queries"
# Generates multi-step plan
# User approves plan
# Agent executes
```

### What Agent Does
- Analyze task
- Generate step-by-step plan
- Present plan for approval
- Execute approved plan

### What Agent Does NOT Do
- Guarantee plan success
- Adapt plan mid-execution
- Provide alternative plans

---

## 8. Resume Capability

### The Mechanism

Continue interrupted sessions:

```bash
cursor agent resume session-id
# Loads previous state
# Continues from last checkpoint
```

### What Agent Does
- Save checkpoints
- Allow resumption
- Maintain context

### What Agent Does NOT Do
- Handle network interruptions gracefully
- Provide checkpoint rollback
- Merge concurrent modifications

---

## 9. Error Handling

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

### What Agent Does
- Catch errors
- Analyze failures
- Suggest corrections
- Retry with modifications

### What Agent Does NOT Do
- Guarantee error recovery
- Provide rollback
- Auto-fix all errors

---

## 10. Logging

### The Mechanism

Track execution history:

```
~/.cursor/sessions/[session-id]/
├── history.log (full execution log)
├── state.json (current state snapshot)
└── modifications/ (file changes record)
```

### What Agent Does
- Log all operations
- Record output
- Track state changes
- Enable debugging

### What Agent Does NOT Do
- Rotate logs automatically
- Provide log analysis
- Offer log replay

---

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

