---
resource_id: "8c22bca7-0522-48be-b84d-46a4ac7203b9"
resource_type: "output"
resource_name: "US-03_stage_agent_loads_domain_context"
---
# US-3: Stage agent loads domain context from parent

**Need**: [Stage Delegation](../README.md)

---

**As a** user who expects the AI to understand the project domain without being re-explained everything,
**I want** the stage agent to automatically find and load the relevant domain knowledge from the parent entity,
**So that** I don't have to re-explain domain concepts every time a new stage starts.

### What Happens

1. User says "design the agent delegation system"
2. Manager spawns a design stage agent and points to the stage directory
3. Stage agent reads its 0AGNOSTIC.md, which tells it where domain knowledge lives
4. Stage agent reads 1-2 specific knowledge files from the parent entity's `.0agnostic/knowledge/`
5. Stage agent has domain understanding and begins design work

### Acceptance Criteria

- Stage agent reads at most 1-2 knowledge files, not the entire knowledge directory
- The 0AGNOSTIC.md contains pointers to where domain knowledge lives
- User does not need to re-explain domain concepts that are already documented
