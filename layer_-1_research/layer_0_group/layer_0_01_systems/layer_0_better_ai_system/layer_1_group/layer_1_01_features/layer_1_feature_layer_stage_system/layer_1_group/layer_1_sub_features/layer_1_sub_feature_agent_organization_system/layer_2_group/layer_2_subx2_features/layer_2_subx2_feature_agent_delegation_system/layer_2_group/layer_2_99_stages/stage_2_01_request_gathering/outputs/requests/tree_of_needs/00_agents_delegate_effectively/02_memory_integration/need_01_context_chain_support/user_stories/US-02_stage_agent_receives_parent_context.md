---
resource_id: "ae9edc84-5b00-46ac-9f6d-fb0a1318de20"
resource_type: "output"
resource_name: "US-02_stage_agent_receives_parent_context"
---
# US-2: Stage agent receives parent domain context

**Need**: [Context Chain Support](../README.md)

---

**As a** user who delegates research to a stage agent and expects it to understand the parent project,
**I want** the stage agent's context chain to include the parent entity's identity and knowledge pointers,
**So that** the agent can load the right domain knowledge on demand without me telling it which files to read.

<!-- section_id: "bd8b622b-98c5-4e80-b578-d964cd022ac0" -->
### What Happens

1. User says "research the context chain architecture"
2. Manager spawns a research stage agent
3. Stage agent's context chain includes the parent entity's 0AGNOSTIC.md (identity + knowledge pointers)
4. Stage agent sees pointers to `.0agnostic/knowledge/` and knows which files contain domain concepts
5. Stage agent loads the specific knowledge file it needs, not the full parent context

<!-- section_id: "ce637cc2-0b5f-4e1a-a08e-ec9f226eb712" -->
### Acceptance Criteria

- Stage agent's chain includes parent 0AGNOSTIC.md pointers, not full knowledge content
- Stage agent can discover which knowledge file to read from the chain alone
- User does not need to point the agent to specific knowledge files
