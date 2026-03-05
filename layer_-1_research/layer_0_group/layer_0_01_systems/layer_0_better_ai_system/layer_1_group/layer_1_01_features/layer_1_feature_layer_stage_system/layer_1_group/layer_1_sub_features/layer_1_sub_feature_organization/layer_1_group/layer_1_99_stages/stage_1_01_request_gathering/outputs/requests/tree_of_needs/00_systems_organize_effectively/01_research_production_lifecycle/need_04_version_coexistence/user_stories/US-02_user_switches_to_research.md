---
resource_id: "a4e53504-0d28-4d0a-8086-fa913f257f8b"
resource_type: "output"
resource_name: "US-02_user_switches_to_research"
---
# User Switches to Research Mode

**As a** user who wants to work with experimental patterns,
**I want to** tell the agent "use research context chain" and have it switch to loading research content,
**So that** I can access experimental patterns when I need them while knowing that production mode is always one command away.

## Acceptance Criteria

**Scenario 1: Trigger phrase activates research mode**
- **Given** I am in a session where the agent is in default production mode,
- **When** I say "use research context chain",
- **Then** the agent loads the context chain mode rule (`context_chain_mode.md`), acknowledges the switch with a confirmation message, and begins loading `layer_-1_research/` content alongside production context.

**Scenario 2: Research mode includes both research and production**
- **Given** the agent has switched to research mode,
- **When** it loads context for a topic that exists in both research and production,
- **Then** both versions are accessible — the agent can reference production patterns for comparison while working with research content.

**Scenario 3: Returning to production mode is straightforward**
- **Given** the agent is currently in research mode,
- **When** the user says "switch back to production" or starts a new session,
- **Then** the agent reverts to production-only context loading, and no research content persists in the active context chain.
