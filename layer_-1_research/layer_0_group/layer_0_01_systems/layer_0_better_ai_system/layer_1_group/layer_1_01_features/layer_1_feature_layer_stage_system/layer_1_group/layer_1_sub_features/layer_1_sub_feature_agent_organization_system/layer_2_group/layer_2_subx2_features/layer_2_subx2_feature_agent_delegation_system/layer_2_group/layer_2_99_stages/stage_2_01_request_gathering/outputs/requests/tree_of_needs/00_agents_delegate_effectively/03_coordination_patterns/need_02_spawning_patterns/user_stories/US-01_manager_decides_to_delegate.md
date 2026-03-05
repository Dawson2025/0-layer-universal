---
resource_id: "8dfa7837-b3de-42e4-9a9f-101f7f375b71"
resource_type: "output"
resource_name: "US-01_manager_decides_to_delegate"
---
# US-1: Manager decides to delegate

**Need**: [Spawning Patterns](../README.md)

---

**As a** user who tells the AI to do design work and expects it to delegate rather than attempt the work in the manager context,
**I want** the manager to have clear criteria for when to spawn a stage agent versus doing work itself,
**So that** the AI consistently delegates specialized work instead of sometimes doing it in the wrong context.

<!-- section_id: "0859a697-9e99-4386-a172-c997f3fc1a89" -->
### What Happens

1. User says "design the agent delegation system"
2. Manager evaluates spawning criteria: "Does this require stage methodology? Yes -- design stage."
3. Manager decides to spawn a stage agent (not attempt design work in the manager context)
4. Manager delegates to a design stage agent with task description + directory pointer
5. Stage agent handles the specialized work with its full methodology

<!-- section_id: "a83148f1-9185-4f96-af31-236c629ac239" -->
### Acceptance Criteria

- Spawning criteria documentation answers "should I spawn?" for common scenarios
- Manager consistently delegates stage work rather than attempting it in-context
- User gets specialized stage work, not generic manager-level output
