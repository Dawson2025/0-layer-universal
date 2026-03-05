---
resource_id: "c63a8428-7ed1-4c19-8c54-30fdcba32b76"
resource_type: "output"
resource_name: "COMPLETE_ARCHITECTURE"
---
# Cursor Agent CLI — Complete Architecture

**Date**: 2026-02-27
**Focus**: How native mechanisms + application-implemented strategy work together

---

<!-- section_id: "3a51ae9c-0087-4d36-9e1b-80cca3130b67" -->
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

<!-- section_id: "2c427a9b-8bb7-492a-a80d-ca0fb9a1c2af" -->
## Task Execution Flow

<!-- section_id: "0a53aac0-35da-4e9c-b10b-1be4230c028c" -->
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

<!-- section_id: "b485fdf3-162c-42db-b518-c3d61548be41" -->
## Context Loading Pipeline

<!-- section_id: "985ffee5-e15d-45d0-a8ce-61f3950ed1ee" -->
### Step 1: Load Task Context

**Agent CLI Does**:
1. Parse task description
2. Load task context from your code

**You Control**:
- TaskContext class with identity, triggers, rules
- What goes in initial prompt

<!-- section_id: "c63e2a58-e782-4601-be80-76b4d9891dfd" -->
### Step 2: Load Session History

**Agent CLI Does**:
1. Find session file
2. Load previous turns (if resuming)
3. Include in context

**You Control**:
- What to persist in session state
- When to start new session

<!-- section_id: "3f794efe-a865-4fcc-8218-b7883fcd3a62" -->
### Step 3: Load Agent Rules

**Agent CLI Does**:
1. Apply static rules (always apply)
2. Apply dynamic rules (based on task)

**You Control**:
- What rules exist
- When to apply each rule

<!-- section_id: "ad7672d7-bfdc-476c-96ec-4ee67659a8f2" -->
### Step 4: Load MCP Tools

**Agent CLI Does**:
1. Read config (which servers enabled)
2. Launch MCP servers
3. Make tools available

**You Control**:
- Which servers to configure
- Server credentials
- Per-task tool access

<!-- section_id: "81f2e0e5-c42e-4e78-a7ea-5293de63f82c" -->
### Step 5: Generate Plan (Optional)

**Agent CLI Does**:
1. Analyze task + context
2. Generate step-by-step plan
3. (Optional) Show to user

**You Control**:
- Whether to require plan approval
- What constitutes a good plan

<!-- section_id: "6a85e8e9-33f8-49ea-baf9-b20aa81b7821" -->
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

<!-- section_id: "63e44f42-f291-4fee-b0da-89161bc925b0" -->
## Session State Management

<!-- section_id: "c3e53130-6a24-41ba-84c7-9f0733a6ea8f" -->
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

<!-- section_id: "b50739de-0ad0-4239-9396-ddd5f427cdc6" -->
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

<!-- section_id: "b0fe3815-e524-4955-a699-cafeb8b035a4" -->
## Error Handling & Recovery

<!-- section_id: "7199893e-425d-4b51-9ebd-356133445b68" -->
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

<!-- section_id: "9846d3ea-dfef-4b07-b534-785293b2b3b6" -->
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

<!-- section_id: "6860941f-ae56-41a3-a19a-8a30734f659f" -->
## Approval Gate Workflow

<!-- section_id: "180d23f9-0f9f-47c4-b2ad-2adf2c079421" -->
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

<!-- section_id: "b22144f5-8ce9-4f45-a622-f30003262315" -->
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

<!-- section_id: "f96d5611-1eba-44ff-b3fe-952a0040d049" -->
## Validation Gate Workflow

<!-- section_id: "ebbdbaad-3ece-4dad-be59-930907af56e9" -->
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

<!-- section_id: "bd31a09f-d258-4f68-a9a9-e57972a5a5fe" -->
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

<!-- section_id: "dadf9735-1b24-4e20-b336-ad74235b73b6" -->
## Practical Example

<!-- section_id: "911819b4-2037-4d91-9bf2-08991bc5f061" -->
### Task: Refactor Database Queries

```bash
cursor agent --plan \
  "Optimize database queries in src/db/queries.js. \
   Bottleneck: N+1 queries. \
   Target: <5 queries per user load. \
   Verify with perf_test.js"
```

<!-- section_id: "e0ca90d9-2f91-478f-b459-eac188a0aafb" -->
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

<!-- section_id: "1da65d96-a61d-44e2-80a6-a38ddb444ca0" -->
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

<!-- section_id: "bb777060-53e8-4fde-ab9f-893c3c16f4d2" -->
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

<!-- section_id: "d5093695-b4d4-45a3-ad60-6769d5add507" -->
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

<!-- section_id: "4e806e73-49e4-4989-864a-9c22d920e41d" -->
## Workflow Patterns

<!-- section_id: "603f76e7-85ba-42a3-8053-0091829d9d1c" -->
### Task-Focused Pattern
- Define specific, bounded task
- Let agent execute autonomously
- Review and approve as needed
- Move to next task

<!-- section_id: "5347ecda-3fc7-4216-9f5a-5ddbf168e02f" -->
### Exploratory Pattern
- Start with vague direction
- Agent generates plan
- Discuss and refine plan
- Execute refined plan

<!-- section_id: "ad75accc-0a21-4f1f-8989-b40e69190b64" -->
### Iterative Pattern
- Agent completes task
- Show results
- Request modifications
- Agent refines
- Repeat until satisfied

---

<!-- section_id: "16cbb234-dc6b-452e-b583-0a1c5e4c0aa0" -->
## Performance Considerations

<!-- section_id: "51069046-c57f-4bac-a777-aa6264791564" -->
### Token Efficiency

- Keep task descriptions concise (but complete)
- Reuse session context (don't start fresh each time)
- Archive old sessions (don't load centuries of history)

<!-- section_id: "fbb1b3de-82a5-4055-89fe-b441ff546887" -->
### Execution Speed

- Use auto-approval for safe operations (formatting, tests)
- Batch related tasks (stay in same session)
- Pre-stage context (have files ready)

<!-- section_id: "d0277fd0-c1ea-487e-9321-19c9b1692261" -->
### Quality Assurance

- Run validation before accepting
- Keep audit trail (episodic memory)
- Review agent work systematically

