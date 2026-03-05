---
resource_id: "d365f4de-faac-429f-952b-808e525817cc"
resource_type: "output"
resource_name: "APPLICATION_IMPLEMENTED"
---
# Cursor Agent CLI — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What users must create/customize (the content and strategy)

---

<!-- section_id: "e614048f-247b-401a-8a98-7b82866ab08e" -->
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

<!-- section_id: "0263742a-676a-4286-bab6-73eb8300213a" -->
## 1. Task Definitions — What to Delegate

<!-- section_id: "a2e598f3-3fa2-43c8-8cf0-662a1df76734" -->
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

<!-- section_id: "cb42dedc-558b-443e-8b75-ffb3eca3c06e" -->
### Examples of Decisions YOU Make

**Task Specificity**:
- Refactor *which* file/function?
- Optimize *what* performance metric?
- Implement *which* feature with *what* requirements?

**Task Boundaries**:
- Is this a 5-minute task or 2-hour task?
- What is success? (tests passing? performance target? line count?)
- What can agent modify vs. what's off-limits?

<!-- section_id: "12dbe757-1557-408b-977e-24738b4bbce6" -->
### User Responsibility

- **Define tasks clearly** (agent quality depends on task clarity)
- **Provide context** (relevant files, specs, constraints)
- **Set success criteria** (how to verify completion)
- **Review results** (always validate agent work)
- **Learn what works** (iterate on task definition)

<!-- section_id: "45767ed0-94cd-4017-a4f5-e5a1db1517c7" -->
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

<!-- section_id: "e0c635d9-b542-447a-919b-58be284212d1" -->
## 2. Agent Context — What Agents Know

<!-- section_id: "fb4ef530-c29f-497d-a0e6-17600f6acbbd" -->
### What You Must Decide

**Context Sources**:
- System prompt (agent identity and constraints)
- Memory Bank entries (project-specific knowledge)
- Code context (relevant files, libraries)
- Success criteria (how to verify completion)

<!-- section_id: "75ab8ce3-e44c-4849-ab66-d34625242164" -->
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

<!-- section_id: "665c165a-bdc8-4a6b-9c63-62da9899c7e0" -->
### User Responsibility

- **Build rich context** (agents perform better with good context)
- **Keep context current** (update when project changes)
- **Document patterns** (codify what agents should know)
- **Test context** (see if agent produces good results)

---

<!-- section_id: "a11a1be5-f3e4-4ed6-94da-72b159b26a63" -->
## 3. Approval Policies — Human Safeguards

<!-- section_id: "8f257d6d-cf7f-4cf9-b2c7-8e9f74992e69" -->
### What You Must Decide

**Which Commands Need Approval**:
- Destructive operations (deletion, overwrites)
- Risky operations (database changes, deployment)
- Sensitive operations (security-related changes)

**Approval Modes**:
- Interactive: Ask for each command
- Batch: Pre-approve certain command patterns
- Auto-approve: Allowed commands (formatting, tests)

<!-- section_id: "9c130ff6-e9b3-4864-80f5-55a2993f7332" -->
### User Responsibility

- **Set appropriate thresholds** (balance safety vs. speed)
- **Test approval policies** (verify they work as intended)
- **Update as needed** (adjust based on experience)

<!-- section_id: "83db494f-4449-4648-bfb5-53d863435a24" -->
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

<!-- section_id: "3f3fb256-fe3d-4e4a-9294-6347632f6a7b" -->
## 4. Session Management — Organizing Work

<!-- section_id: "b06cdfb5-9466-4ae5-9484-fd0f2d081c09" -->
### What You Must Decide

**Session Boundaries**:
- One per task? (focused, many sessions)
- One per feature? (coherent, potentially long)
- One per day? (natural boundary)

**Session Resumption**:
- How long keep sessions active? (default: 2 hours)
- What context to preserve? (which files matter)
- How to organize old sessions? (archive, delete)

<!-- section_id: "434ef6c2-823c-4172-b6ad-18dcfc1e6c5f" -->
### User Responsibility

- **Choose boundaries** (no right answer, your preference)
- **Document sessions** (what was accomplished)
- **Clean up** (don't accumulate hundreds of sessions)

---

<!-- section_id: "80097394-c044-4bae-95ec-e62e453420c0" -->
## 5. Validation Rules — Ensuring Quality

<!-- section_id: "2fc98e2b-cc1b-4319-8b8e-baa7e633911b" -->
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

<!-- section_id: "412e317d-60c5-47fc-afb5-f69e3b00036b" -->
### User Responsibility

- **Define rules** (what quality means to you)
- **Automate validation** (pre-commit hooks, CI/CD)
- **Fail gracefully** (tell agent what failed)

---

<!-- section_id: "ea28b69e-d348-4ee3-a8f0-99d37a33188f" -->
## 6. MCP Server Configuration — Agent Tools

<!-- section_id: "6cd21424-7e93-406b-bffd-e68c689f47e0" -->
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

<!-- section_id: "324394bd-2427-4d9b-906d-dc83a67a2db6" -->
### User Responsibility

- **Choose strategically** (don't load unused servers)
- **Configure securely** (use env vars for secrets)
- **Document** (what each server does)

---

<!-- section_id: "d4c2310e-c126-4941-96e2-c35db925bdbf" -->
## 7. State Management — Across Sessions

<!-- section_id: "8716a813-f8f2-4f92-8a8a-db01e32b1f6e" -->
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

<!-- section_id: "9f2aa4b9-5622-475e-b39b-a445c80b4b7b" -->
### User Responsibility

- **Design schema** (what fields to track)
- **Implement serialization** (save/load state)
- **Clean up** (manage storage size)

---

<!-- section_id: "f18ca161-3e02-4261-838a-34a09a234391" -->
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

<!-- section_id: "ff852e22-fe36-48c3-860f-077f1a07be44" -->
## Key Principle

**Agent CLI provides autonomy. You provide safety rails and good task definitions.**

If Agent CLI is struggling:
- Task is too vague (agents can't succeed with unclear goals)
- Context is missing (agents don't know project conventions)
- Approval policies too restrictive (agents can't make progress)
- Validation rules unreasonable (hard to meet criteria)

All of these are **your** decisions, not Agent CLI's.

