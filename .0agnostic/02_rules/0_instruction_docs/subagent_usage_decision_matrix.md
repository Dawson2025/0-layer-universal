---
resource_id: "23dda005-4b89-4ff2-a5af-da286f4477c4"
resource_type: "rule"
resource_name: "subagent_usage_decision_matrix"
---
# Subagent Usage Decision Matrix

**Purpose:** Guide for when AI agents should use subagents/Task tool vs. main conversation in Claude Code.

**Last Updated:** 2026-01-15

---

## Quick Decision (3 Questions)

```
1. Can work be done in parallel?
   └── No  → Stay in main thread
   └── Yes → Question 2

2. Is work independent (no shared files/context)?
   └── No  → Stay in main thread
   └── Yes → Question 3

3. Is output verbose or task self-contained?
   └── No  → Stay in main thread
   └── Yes → Use Subagent/Task tool
```

---

## Decision Matrix

| Situation | Use Subagent? | Reason |
|-----------|---------------|--------|
| Writing multiple files (3+) | **YES** | Keeps file content out of main context |
| Searching large codebase | **YES** | Parallel search, isolated results |
| Running tests | **YES** | Verbose output stays isolated |
| Code review | **YES** | Specialized focus, clean summary |
| Research/exploration | **YES** | Preserves main context for implementation |
| Processing logs/docs | **YES** | High-volume output isolation |
| 2-3 specific files | **NO** | Overhead not worth it |
| Quick targeted change | **NO** | Latency cost too high |
| Iterative refinement needed | **NO** | Back-and-forth requires main thread |
| Shared context between steps | **NO** | Context isolation would break workflow |
| Simple sequential operations | **NO** | No parallelization benefit |

---

## When to Use Subagents

### Ideal Cases

1. **Context Preservation**
   - Exploration and implementation stay out of main conversation
   - Preserves context availability for later work
   - Prevents "context bloat" from verbose operations

2. **Self-Contained Tasks**
   - Work can return a summary without needing iteration
   - Clear inputs and outputs
   - No mid-task user decisions required

3. **Verbose Output**
   - Test runs
   - Documentation fetches
   - Log processing
   - Large file reads

4. **Parallel Work**
   - Independent domains (different file sets)
   - No file overlap between tasks
   - Research across multiple areas

5. **Specialized Expertise**
   - Code review with specific guidelines
   - Security scanning
   - Style/lint checking
   - Domain-specific analysis

6. **Repeatable Workflows**
   - Same task pattern used frequently
   - Defined in `.claude/agents/` for reuse

### Anthropic's Recommendation

> "This is the part of the workflow where you should consider strong use of subagents, especially for complex problems. Telling Claude to use subagents to verify details or investigate particular questions it might have, **especially early on in a conversation or task**, tends to **preserve context availability** without much downside in terms of lost efficiency."

---

## When to Stay in Main Conversation

### Ideal Cases

1. **Small Scope**
   - Working with 2-3 specific files
   - Simple sequential operations
   - Quick, targeted changes

2. **Iteration Required**
   - Frequent back-and-forth with user
   - Iterative refinement needed
   - Multiple phases share significant context

3. **Latency Sensitive**
   - Subagents start fresh (loading overhead)
   - ~20k token overhead before actual work begins

4. **Context Sharing Required**
   - Tasks need to communicate
   - Operations depend on each other
   - Shared state between steps

---

## Overhead Awareness

Both Tasks and subagents have approximately **20,000 tokens** of context loading overhead before actual work begins.

**Don't use subagents for:**
- Trivial tasks that take fewer tokens than the overhead
- Tasks requiring less than 30 seconds of work
- Simple file reads or single-file edits

---

## Execution Patterns

### Parallel Pattern
Use when work spans **independent domains** with no file overlap.

```
Good: Search frontend/, backend/, docs/ simultaneously
Bad:  Edit config.json while another agent reads it
```

### Sequential Pattern
Use when **output from one step feeds the next**.

```
Schema → API → Frontend (data structure must exist first)
Research → Planning → Implementation
Implementation → Testing → Security audit
```

### Background Pattern
Use for **non-blocking research** while continuing other work.

```
Ask Claude to "run this in the background"
Press Ctrl+B to background a running task
Check /tasks to see progress
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Over-parallelizing | Token waste, coordination overhead | Group related micro-tasks |
| Under-parallelizing | Sequential work that could parallelize | Look for domain independence |
| Vague invocations | Subagent lacks context | Include scope, file refs, expected output |
| Using for 2-3 files | Overhead exceeds benefit | Stay in main thread |
| Nested spawning | Subagents can't spawn subagents | Chain from main conversation |

---

## Invocation Quality

Subagents have temporary context windows - they can't ask clarifying questions. Provide:

**Bad:** "Fix authentication"

**Good:** "Fix OAuth redirect loop where successful login redirects to /login instead of /dashboard. Reference the auth middleware in src/lib/auth.ts."

Always include:
- Specific scope
- Relevant file references
- Expected output format
- Success criteria

---

## Task Tool vs Custom Subagents

| Feature | Task Tool | Custom Subagent |
|---------|-----------|-----------------|
| Setup | None required | Define in `.claude/agents/` |
| Reusability | One-off | Reusable across sessions |
| Tool restrictions | Inherits all | Can limit tools |
| Model selection | Default | Can specify model |
| Use case | Ad-hoc research | Recurring workflows |

**Start with Task tool for one-off work. Create custom subagents for repeated patterns.**

---

## Examples

### Use Subagent
```
User: "Create documentation guides for all entity types"
→ Self-contained, writes multiple files, verbose output
→ Main context only needs final summary
```

### Stay in Main Thread
```
User: "Fix the typo in README.md"
→ Single file, trivial change
→ Overhead would exceed the work itself
```

### Use Subagent
```
User: "Search the codebase for all database connections"
→ Parallel search across many files
→ Results summarized back
```

### Stay in Main Thread
```
User: "Let's iterate on this API design together"
→ Requires back-and-forth
→ Shared context between iterations
```

---

## Related Documents

- `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md` - Terminal usage rules
- `ai_agent_documentation_rule.md` - Documentation requirements
- `when-to-use-terminal-wrapper.md` - Similar decision pattern for tools
- `testing-agent-protocol.md` - Agent coordination example

---

## Sources

- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code Docs: Create Custom Subagents](https://code.claude.com/docs/en/sub-agents)
- [Task Tool vs Subagents Analysis](https://amitkoth.com/claude-code-task-tool-vs-subagents/)
