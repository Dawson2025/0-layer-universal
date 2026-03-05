---
resource_id: "d365f4de-faac-429f-952b-808e525817cc"
resource_type: "output"
resource_name: "APPLICATION_IMPLEMENTED"
---
# Cursor Agent CLI — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What users must create/customize (the content and strategy)

---

## Overview

Agent CLI provides **mechanisms for autonomous execution**. You provide **strategy and content**:

1. **Task Definitions** (what tasks to delegate)
2. **Agent Context** (what agents know about your system)
3. **Approval Policies** (which commands need human approval)
4. **Session Management** (how to organize work)
5. **Validation Rules** (ensuring quality results)
6. **MCP Server Configuration** (which tools agents can use)
7. **State Management** (what to remember across sessions)

---

## 1. Task Definitions — What to Delegate

### What You Must Create

You define exactly **which tasks are safe and valuable to delegate** to agents:

**Good Delegation Candidates**:
- Refactoring (specific file, clear goal)
- Bug fixes (identified issue, test case available)
- Performance optimization (benchmarks defined)
- Feature implementation (detailed spec provided)
- Documentation (structure defined)

**Poor Delegation Candidates**:
- Vague requests ("improve the code")
- High-risk operations (database migrations)
- Tasks without success criteria
- Tasks requiring business logic decisions

### Examples of Decisions YOU Make

**Task Specificity**:
- Refactor *which* file/function?
- Optimize *what* performance metric?
- Implement *which* feature with *what* requirements?

**Task Boundaries**:
- Is this a 5-minute task or 2-hour task?
- What is success? (tests passing? performance target? line count?)
- What can agent modify vs. what's off-limits?

### User Responsibility

- **Define tasks clearly** (agent quality depends on task clarity)
- **Provide context** (relevant files, specs, constraints)
- **Set success criteria** (how to verify completion)
- **Review results** (always validate agent work)
- **Learn what works** (iterate on task definition)

### Example Task Definitions

```bash
# GOOD: Specific, bounded, has success criteria
cursor agent "Refactor src/auth.py to async/await. \
  Replace Promise chains with async/await. \
  All tests in tests/auth.test.js must pass. \
  No breaking changes to API."

# GOOD: Clear scope with verification
cursor agent "Optimize src/db/queries.py. \
  Bottleneck: N+1 queries in user loading. \
  Target: <5 queries per page load. \
  Verify with performance_test.py"

# POOR: Vague, no success criteria
cursor agent "Improve the code"

# POOR: Too risky without detail
cursor agent "Update database schema"

# BETTER: Same task, specific and bounded
cursor agent "Add 'email' column to users table. \
  Create Prisma migration. \
  Run migration in test DB first. \
  Update type definitions in schema.ts"
```

---

## 2. Agent Context — What Agents Know

### What You Must Decide

**Context Sources**:
- System prompt (agent identity and constraints)
- Memory Bank entries (project-specific knowledge)
- Code context (relevant files, libraries)
- Success criteria (how to verify completion)

### Strategic Decisions YOU Make

**What to Include**:
- Which project conventions matter most?
- What patterns should agent follow?
- What are the gotchas?
- What's the current project phase?

**What to Exclude**:
- Every conversation (too much noise)
- Implementation details agent can figure out
- Unrelated project context

### User Responsibility

- **Build rich context** (agents perform better with good context)
- **Keep context current** (update when project changes)
- **Document patterns** (codify what agents should know)
- **Test context** (see if agent produces good results)

---

## 3. Approval Policies — Human Safeguards

### What You Must Decide

**Which Commands Need Approval**:
- Destructive operations (deletion, overwrites)
- Risky operations (database changes, deployment)
- Sensitive operations (security-related changes)

**Approval Modes**:
- Interactive: Ask for each command
- Batch: Pre-approve certain command patterns
- Auto-approve: Allowed commands (formatting, tests)

### User Responsibility

- **Set appropriate thresholds** (balance safety vs. speed)
- **Test approval policies** (verify they work as intended)
- **Update as needed** (adjust based on experience)

### Example Approval Policies

```json
{
    "approval_rules": {
        "require_approval": [
            "rm -rf",
            "git push",
            "DROP TABLE",
            "DELETE FROM",
            "chmod 777"
        ],
        "auto_approve": [
            "npm test",
            "prettier --write",
            "eslint --fix",
            "git add",
            "git commit"
        ],
        "interactive": true
    }
}
```

---

## 4. Session Management — Organizing Work

### What You Must Decide

**Session Boundaries**:
- One per task? (focused, many sessions)
- One per feature? (coherent, potentially long)
- One per day? (natural boundary)

**Session Resumption**:
- How long keep sessions active? (default: 2 hours)
- What context to preserve? (which files matter)
- How to organize old sessions? (archive, delete)

### User Responsibility

- **Choose boundaries** (no right answer, your preference)
- **Document sessions** (what was accomplished)
- **Clean up** (don't accumulate hundreds of sessions)

---

## 5. Validation Rules — Ensuring Quality

### What You Must Decide

**What to Validate**:
- Code formatting (follows project style)
- Tests passing (no regressions)
- Type safety (TypeScript, mypy)
- Performance (meets benchmarks)
- Security (no hardcoded secrets)

**Validation Timing**:
- Before accepting result (gate)
- After result (feedback loop)
- Both

### User Responsibility

- **Define rules** (what quality means to you)
- **Automate validation** (pre-commit hooks, CI/CD)
- **Fail gracefully** (tell agent what failed)

---

## 6. MCP Server Configuration — Agent Tools

### What You Must Decide

**Which Servers to Enable**:
- GitHub (repo operations)
- Canvas (course management)
- Tavily (web search)
- Custom APIs (your own tools)

**Per-Task Access**:
- All tasks get all servers?
- Restrict specific tasks?
- Enable/disable as needed?

### User Responsibility

- **Choose strategically** (don't load unused servers)
- **Configure securely** (use env vars for secrets)
- **Document** (what each server does)

---

## 7. State Management — Across Sessions

### What You Must Decide

**What to Persist**:
- Completed tasks (history)
- File modifications (what changed)
- Decisions made (why choices were made)
- Next steps (what's remaining)

**Storage Strategy**:
- Local JSON files (simple)
- Database (scalable)
- Git commits (version controlled)

### User Responsibility

- **Design schema** (what fields to track)
- **Implement serialization** (save/load state)
- **Clean up** (manage storage size)

---

## Summary: Application-Implemented = Strategy & Content

| Aspect | Agent CLI Does | You Must Provide |
|--------|---------------|------------------|\
| **Task Execution** | Run tasks autonomously | Define tasks clearly, provide context |
| **Session Management** | Persist state | Decide session boundaries |
| **Approval Gates** | Check before shell commands | Define approval policies |
| **Context Loading** | Manage agent memory | Write context from 0AGNOSTIC.md |
| **Validation** | Execute rules | Define what quality means |
| **MCP Tools** | Route to tools | Choose which servers to enable |
| **State Persistence** | Save/load state | Design what to remember |

---

## Key Principle

**Agent CLI provides autonomy. You provide safety rails and good task definitions.**

If Agent CLI is struggling:
- Task is too vague (agents can't succeed with unclear goals)
- Context is missing (agents don't know project conventions)
- Approval policies too restrictive (agents can't make progress)
- Validation rules unreasonable (hard to meet criteria)

All of these are **your** decisions, not Agent CLI's.

