# US-1: Manager decides to delegate

**Need**: [Spawning Patterns](../README.md)

---

**As a** user who tells the AI to do design work and expects it to delegate rather than attempt the work in the manager context,
**I want** the manager to have clear criteria for when to spawn a stage agent versus doing work itself,
**So that** the AI consistently delegates specialized work instead of sometimes doing it in the wrong context.

### What Happens

1. User says "design the agent delegation system"
2. Manager evaluates spawning criteria: "Does this require stage methodology? Yes -- design stage."
3. Manager decides to spawn a stage agent (not attempt design work in the manager context)
4. Manager delegates to a design stage agent with task description + directory pointer
5. Stage agent handles the specialized work with its full methodology

### Acceptance Criteria

- Spawning criteria documentation answers "should I spawn?" for common scenarios
- Manager consistently delegates stage work rather than attempting it in-context
- User gets specialized stage work, not generic manager-level output
