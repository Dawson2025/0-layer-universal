---
resource_id: "60e4160d-aa0d-4c5c-99d5-b01bd8bc3c8c"
resource_type: "output"
resource_name: "US-02_agent_triggers_consolidation_reminder"
---
# US-02: Agent triggers consolidation reminder

**Need**: [Consolidation Process](../README.md)

---

**As a** user moving the AI from one stage to another,
**I want** the system to remind me that consolidation should happen before proceeding,
**So that** knowledge files are updated and the next stage starts with current information.

### What Happens

1. User tells the AI to transition from one stage to the next (e.g., research to design)
2. Stage-workflow skill detects the transition and triggers a consolidation reminder
3. System prompts the user: "Stage outputs have changed. Consolidate to knowledge files before proceeding?"
4. User either consolidates now or defers with awareness that knowledge may be stale

### Acceptance Criteria

- Stage-workflow skill includes a consolidation check at stage transitions
- Reminder is visible and actionable (not buried in logs)
- User can defer but is aware of the consequence
