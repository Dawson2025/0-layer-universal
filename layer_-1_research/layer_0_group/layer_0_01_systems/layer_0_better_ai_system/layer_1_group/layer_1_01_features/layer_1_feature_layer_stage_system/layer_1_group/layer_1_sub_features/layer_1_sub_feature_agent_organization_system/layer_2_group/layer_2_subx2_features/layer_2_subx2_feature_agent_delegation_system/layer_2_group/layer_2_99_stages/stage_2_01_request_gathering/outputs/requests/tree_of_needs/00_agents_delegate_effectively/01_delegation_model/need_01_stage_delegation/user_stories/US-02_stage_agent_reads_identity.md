---
resource_id: "90b8e1eb-c765-43ad-9128-7f35734c94f0"
resource_type: "output"
resource_name: "US-02_stage_agent_reads_identity"
---
# US-2: Stage agent reads its own identity

**Need**: [Stage Delegation](../README.md)

---

**As a** user who delegates a task and expects the AI to just start working,
**I want** the stage agent to read its own identity file and immediately know its role, methodology, and output format,
**So that** the AI never comes back asking me how it should do the work.

### What Happens

1. User delegates a task (e.g., "do the research for this feature")
2. Manager spawns a stage agent and points it to the stage directory
3. Stage agent reads `0AGNOSTIC.md` in its stage directory
4. Stage agent discovers its role, methodology, output format, and success criteria
5. Stage agent begins producing outputs without asking clarifying questions about process

### Acceptance Criteria

- Stage agent reads one file and has everything needed to start working
- User is not asked about methodology, output format, or success criteria
- The 0AGNOSTIC.md contains role, methodology, output format, and success criteria sections
