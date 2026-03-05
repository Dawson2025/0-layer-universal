---
resource_id: "23efc37c-0578-45e9-9120-fbedc46ce98b"
resource_type: "output"
resource_name: "US-03_stage_agent_follows_lifecycle"
---
# US-3: Stage agent follows lifecycle

**Need**: [Spawning Patterns](../README.md)

---

**As a** user who expects the AI to leave a stage in a clean state after working on it,
**I want** stage agents to follow a defined lifecycle (read identity, do work, write report, exit),
**So that** the stage is ready for the next agent or the next session without cleanup.

### What Happens

1. User tells the AI to work on a stage
2. Stage agent follows the lifecycle: read 0AGNOSTIC.md -> understand role and methodology
3. Stage agent does the work, producing outputs in the stage directory
4. Stage agent writes a `stage_report.md` before exiting
5. Stage is left in a clean, documented state for the next agent

### Acceptance Criteria

- Stage agent follows the lifecycle steps in order: read -> work -> report -> exit
- Stage report is written before the agent exits
- Stage directory is in a clean state that any future agent can resume from
