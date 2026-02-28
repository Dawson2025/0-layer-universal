# Cursor Agent CLI — Complete Architecture

**Date**: 2026-02-27
**Focus**: How native mechanisms + application-implemented strategy work together

---

## System Overview

Agent CLI combines **native mechanisms** (what it provides) with **application-implemented strategy** (what you provide):

```
┌───────────────────────────────────────────┐
│ Agent CLI Native Mechanisms               │
├───────────────────────────────────────────┤
│ • Autonomous task execution               │
│ • Session persistence                     │
│ • Shell command execution + approval      │
│ • MCP tool integration                    │
│ • State management                        │
│ • Error handling & retry                  │
│ • Plan generation + approval              │
│ • Cloud agent support                     │
│ • Logging & history                       │
└───────────────────────────────────────────┘
                           ↓
┌───────────────────────────────────────────┐
│ Your Strategy (What You Provide)          │
├───────────────────────────────────────────┤
│ • Task definitions (specific, bounded)    │
│ • Agent context (from 0AGNOSTIC.md)       │
│ • Approval policies (safety rails)        │
│ • Session organization (boundaries)       │
│ • Validation rules (quality gates)        │
│ • MCP server selection (which tools)      │
│ • State schema (what to remember)         │
└───────────────────────────────────────────┘
                           ↓
                    Working System
```

---

## Task Execution Flow

### When You Invoke Agent CLI

```
$ cursor agent "Refactor src/auth.js to async/await"

1. User provides task description

2. Agent CLI loads context:
   ├─ Your agent context (from 0AGNOSTIC.md)
   ├─ Recent session history
   ├─ Project structure
   └─ Previous decisions

3. Agent generates plan:
   ├─ Analyze codebase
   ├─ Identify files to modify
   ├─ Plan changes step-by-step
   └─ (Optional: Show plan for approval)

4. Agent executes plan:
   ├─ Make modifications
   ├─ For each shell command:
   │   ├─ Show command to user
   │   ├─ Request approval: [y/n]?
   │   └─ Execute if approved
   ├─ Run validation (tests, linting)
   └─ Report results

5. Session state saved:
   ├─ Record task completion
   ├─ Save file modifications
   ├─ Update episodic memory
   └─ Create handoff for next session

6. Results returned to user
```

---

## Context Loading Pipeline

### Step 1: Load Task Context

**Agent CLI Does**:
1. Parse task description
2. Load task context from your code

**You Control**:
- TaskContext class with identity, triggers, rules
- What goes in initial prompt

### Step 2: Load Session History

**Agent CLI Does**:
1. Find session file
2. Load previous turns (if resuming)
3. Include in context

**You Control**:
- What to persist in session state
- When to start new session

### Step 3: Load Agent Rules

**Agent CLI Does**:
1. Apply static rules (always apply)
2. Apply dynamic rules (based on task)

**You Control**:
- What rules exist
- When to apply each rule

### Step 4: Load MCP Tools

**Agent CLI Does**:
1. Read config (which servers enabled)
2. Launch MCP servers
3. Make tools available

**You Control**:
- Which servers to configure
- Server credentials
- Per-task tool access

### Step 5: Generate Plan (Optional)

**Agent CLI Does**:
1. Analyze task + context
2. Generate step-by-step plan
3. (Optional) Show to user

**You Control**:
- Whether to require plan approval
- What constitutes a good plan

### Step 6: Execute & Validate

**Agent CLI Does**:
1. Execute steps
2. Run validations (tests, rules)
3. Adjust if failures
4. Report results

**You Control**:
- Validation rules
- Approval gates
- Retry strategies

---

## Session State Management

### During Execution

```json
{
  "session_id": "session-2026-02-27-001",
  "task_description": "Refactor auth.js to async/await",
  "status": "in_progress",
  "steps_completed": [
    "Analyzed file structure",
    "Identified Promise chains",
    "Generated refactoring plan"
  ],
  "current_step": "Execute refactoring",
  "file_modifications": {
    "src/auth.js": {
      "status": "modified",
      "changes": 15,
      "tests": "passing"
    }
  },
  "commands_executed": [
    "npm test",
    "eslint --fix"
  ],
  "validation_results": {
    "tests": "passing",
    "linting": "clean",
    "types": "valid"
  }
}
```

### Resuming Session

```
$ cursor agent resume session-2026-02-27-001

1. Load previous state
2. Show what was accomplished
3. Ask: Continue? [y/n]?
4. Resume from checkpoint
5. Continue execution
```

---

## Error Handling & Recovery

### When Agent Encounters Error

```
$ cursor agent "Fix bug in src/parser.js"

[Step 1] Analyze parser.js
✅ Complete

[Step 2] Run tests to identify failure
❌ Test failed: Expected array, got undefined

[Agent analyzes failure]

[Step 3] Fix implementation
→ Modified: src/parser.js (line 42)
→ Run tests again

[Step 2 RETRY] Run tests
✅ All tests passing

[Step 4] Validate fix
→ Code review: Looks good
→ Performance: No regression

✅ Task complete: Bug fixed
```

### Retry Logic

```python
# From your validation code
@retry(max_attempts=3, backoff_seconds=1)
def execute_step(step_description):
    """Execute with automatic retry."""
    try:
        result = agent_execute(step_description)
        return result
    except Exception as e:
        # Agent analyzes error
        # Suggests fix
        # Retries
        raise
```

---

## Approval Gate Workflow

### Interactive Approval

```
Agent: "I'll run 'npm test' to verify changes"
Request approval: [y/n]?

User: y

> npm test
✅ Tests pass (1250ms)

Agent: "I'll run 'npm run build' to check build"
Request approval: [y/n]?

User: n (Wait, let me review code first)

Agent: Waiting for approval...

User: [Reviews code]

User: y

> npm run build
✅ Build successful
```

### Batch Approval

```json
{
  "approval_rules": {
    "auto_approve": [
      "npm test",
      "prettier --write",
      "eslint --fix"
    ],
    "require_approval": [
      "git push",
      "rm -rf",
      "DROP TABLE"
    ]
}
```

---

## Validation Gate Workflow

### Static Validation (Before Accepting Result)

```python
# Your validation code
class ResultValidator:
    @staticmethod
    def validate_refactoring(result):
        """Validate refactoring result."""

        # Rule 1: All tests must pass
        if not result['tests_pass']:
            raise ValidationError("Tests failing")

        # Rule 2: No new linting issues
        if result['lint_errors'] > 0:
            raise ValidationError("Linting errors introduced")

        # Rule 3: No breaking changes
        if result['api_changes'] and not safe_changes(result['api_changes']):
            raise ValidationError("Breaking API changes detected")

        return True  # Valid
```

**Agent workflow**:
```
[Execute refactoring]
✅ Changes made
✅ Tests passing
✅ Linting clean
✅ API safe

[Validate against rules]
✅ Validation passed

[Return result to user]
```

---

## Context Composition

At any point, Agent CLI includes:

```
┌─ Task description
├─ Agent context (from 0AGNOSTIC.md)
├─ Session history (if resuming)
├─ Applied rules (static + dynamic)
├─ MCP tool descriptions
├─ Previous errors (if retrying)
└─ Current execution state
```

**Token Budget** (typical 128K context):
- ~500 tokens: Task description
- ~1000 tokens: Agent context + rules
- ~2000 tokens: Session history
- ~1000 tokens: MCP tool descriptions
- ~X tokens: Execution state
- ~Remaining: Agent working space

---

## Practical Example

### Task: Refactor Database Queries

```bash
cursor agent --plan \
  "Optimize database queries in src/db/queries.js. \
   Bottleneck: N+1 queries. \
   Target: <5 queries per user load. \
   Verify with perf_test.js"
```

### Agent Plan (Shown to User)

```
## Execution Plan

1. Analyze current queries (1-2 min)
2. Identify N+1 patterns (5 min)
3. Implement query optimization (10-15 min)
4. Run performance benchmark (2 min)
5. Verify against target (1 min)
6. Run full test suite (3 min)

Total estimated time: 22-28 minutes

Approval: [y/n]? y
```

### Execution

```
[Step 1] Analyzing queries...
✅ Found 3 N+1 patterns in user loading

[Step 2] Optimizing...
→ Using SELECT * with JOIN instead of loop
→ Batching queries
→ Adding caching layer

[Validation] Tests running...
✅ All tests passing

[Performance] Running benchmark...
Before: 42 queries (450ms)
After: 4 queries (85ms)
✅ Target: <5 queries [MET]

[Step 3] Code review...
→ Style: Clean
→ Comments: Added where needed
→ Backwards compatible: Yes

✅ Task complete: Performance improved 5.3x
```

### Session Saved

```json
{
  "session_id": "session-2026-02-27-query-opt",
  "completed": true,
  "accomplishment": "Optimized N+1 queries",
  "metrics": {
    "queries_before": 42,
    "queries_after": 4,
    "time_reduction": "450ms → 85ms (5.3x faster)"
  },
  "files_modified": ["src/db/queries.js"],
  "tests_status": "passing",
  "next_steps": [
    "Monitor performance in production",
    "Consider caching strategy",
    "Document optimization approach"
  ]
}
```

---

## The System Works When

✅ **Tasks are specific and bounded** (agent can succeed)
✅ **Context is rich and current** (agent understands project)
✅ **Approval policies are reasonable** (agent can make progress)
✅ **Validation rules are achievable** (agent can meet success criteria)
✅ **Session state is well-designed** (agent can resume effectively)
✅ **MCP servers are configured** (agent has needed tools)
✅ **Error handling is robust** (agent can recover from failures)

The system fails when any of these are missing or misaligned.

---

## Workflow Patterns

### Task-Focused Pattern
- Define specific, bounded task
- Let agent execute autonomously
- Review and approve as needed
- Move to next task

### Exploratory Pattern
- Start with vague direction
- Agent generates plan
- Discuss and refine plan
- Execute refined plan

### Iterative Pattern
- Agent completes task
- Show results
- Request modifications
- Agent refines
- Repeat until satisfied

---

## Performance Considerations

### Token Efficiency

- Keep task descriptions concise (but complete)
- Reuse session context (don't start fresh each time)
- Archive old sessions (don't load centuries of history)

### Execution Speed

- Use auto-approval for safe operations (formatting, tests)
- Batch related tasks (stay in same session)
- Pre-stage context (have files ready)

### Quality Assurance

- Run validation before accepting
- Keep audit trail (episodic memory)
- Review agent work systematically

