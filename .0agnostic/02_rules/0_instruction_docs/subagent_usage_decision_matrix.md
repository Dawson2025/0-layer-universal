---
resource_id: "23dda005-4b89-4ff2-a5af-da286f4477c4"
resource_type: "rule"
resource_name: "subagent_usage_decision_matrix"
---
# Subagent Usage Decision Matrix

**Purpose:** Guide for when AI agents should use subagents/Task tool vs. main conversation in Claude Code.

**Last Updated:** 2026-01-15

---

<!-- section_id: "d3457471-bc16-4db7-92be-a46855ee713d" -->
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

<!-- section_id: "41076452-9c94-4246-9fdf-099ca63a5e4c" -->
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

<!-- section_id: "ae800648-cccc-4d37-8ced-20ccd2528cdf" -->
## When to Use Subagents

<!-- section_id: "c1b0477c-28bb-4124-98b4-c6440433805a" -->
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

<!-- section_id: "8ccd62aa-a5a8-4ace-9bf3-63e9a74ac849" -->
### Anthropic's Recommendation

> "This is the part of the workflow where you should consider strong use of subagents, especially for complex problems. Telling Claude to use subagents to verify details or investigate particular questions it might have, **especially early on in a conversation or task**, tends to **preserve context availability** without much downside in terms of lost efficiency."

---

<!-- section_id: "111a774a-e86e-46f2-99b7-6c4d039c59b0" -->
## When to Stay in Main Conversation

<!-- section_id: "c01b3e33-efec-4144-9e27-9019b11fe2aa" -->
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

<!-- section_id: "b8d3a66e-1a65-4054-bb3e-e2cee10a0cb7" -->
## Overhead Awareness

Both Tasks and subagents have approximately **20,000 tokens** of context loading overhead before actual work begins.

**Don't use subagents for:**
- Trivial tasks that take fewer tokens than the overhead
- Tasks requiring less than 30 seconds of work
- Simple file reads or single-file edits

---

<!-- section_id: "9a5b876d-ad84-4fc5-91cf-67a3e4fabf01" -->
## Execution Patterns

<!-- section_id: "6b24f8ad-7993-4c7a-bec1-e9b6862c0a3f" -->
### Parallel Pattern
Use when work spans **independent domains** with no file overlap.

```
Good: Search frontend/, backend/, docs/ simultaneously
Bad:  Edit config.json while another agent reads it
```

<!-- section_id: "c2c24888-bda9-4798-8ecc-e581ead0265b" -->
### Sequential Pattern
Use when **output from one step feeds the next**.

```
Schema → API → Frontend (data structure must exist first)
Research → Planning → Implementation
Implementation → Testing → Security audit
```

<!-- section_id: "6df0416a-ba2f-404d-b261-22e690f0c238" -->
### Background Pattern
Use for **non-blocking research** while continuing other work.

```
Ask Claude to "run this in the background"
Press Ctrl+B to background a running task
Check /tasks to see progress
```

---

<!-- section_id: "eb3e53d9-15dd-4d1c-8c71-c6a29a40a14c" -->
## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Over-parallelizing | Token waste, coordination overhead | Group related micro-tasks |
| Under-parallelizing | Sequential work that could parallelize | Look for domain independence |
| Vague invocations | Subagent lacks context | Include scope, file refs, expected output |
| Using for 2-3 files | Overhead exceeds benefit | Stay in main thread |
| Nested spawning | Subagents can't spawn subagents | Chain from main conversation |

---

<!-- section_id: "cce20905-afd7-4e45-a60b-50a2fec6fdcf" -->
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

<!-- section_id: "aa3adad0-d017-49f9-b2b3-17fbd77172bc" -->
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

<!-- section_id: "acada0d2-79b6-416b-8bbf-99833a4e1eaf" -->
## Examples

<!-- section_id: "13d4bb9b-3fcb-4789-ab9f-d111a700428b" -->
### Use Subagent
```
User: "Create documentation guides for all entity types"
→ Self-contained, writes multiple files, verbose output
→ Main context only needs final summary
```

<!-- section_id: "ef3ff2d9-074b-43e9-b14f-abd9b8bf54a3" -->
### Stay in Main Thread
```
User: "Fix the typo in README.md"
→ Single file, trivial change
→ Overhead would exceed the work itself
```

<!-- section_id: "576914c7-eea6-4676-b262-b9a7e47fc783" -->
### Use Subagent
```
User: "Search the codebase for all database connections"
→ Parallel search across many files
→ Results summarized back
```

<!-- section_id: "387f9059-fef0-4455-aa99-c89a925ae8e1" -->
### Stay in Main Thread
```
User: "Let's iterate on this API design together"
→ Requires back-and-forth
→ Shared context between iterations
```

---

<!-- section_id: "ecc32e79-9de4-42d9-9adb-45916469c04a" -->
## Related Documents

- `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md` - Terminal usage rules
- `ai_agent_documentation_rule.md` - Documentation requirements
- `when-to-use-terminal-wrapper.md` - Similar decision pattern for tools
- `testing-agent-protocol.md` - Agent coordination example

---

<!-- section_id: "d724c65a-80ad-4ff5-bd96-911ddf217fc3" -->
## Sources

- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code Docs: Create Custom Subagents](https://code.claude.com/docs/en/sub-agents)
- [Task Tool vs Subagents Analysis](https://amitkoth.com/claude-code-task-tool-vs-subagents/)
