---
resource_id: "c2c4e9cb-d089-4a19-ad7b-32d9884c9b53"
resource_type: "readme
output"
resource_name: "README"
---
# Three-Tier Delegation -- User Stories Index

**Need**: [Three-Tier Delegation](../README.md)

## Overview

These stories cover how the three-tier knowledge pattern (pointers, distilled, full) maps to agent delegation responsibilities. They validate that managers operate from Tier 1 pointers alone to make delegation decisions, that stage agents work competently from Tier 2 distilled knowledge, that only the active stage agent accesses its own Tier 3 full content, and that the developer can verify the tier-to-agent alignment is correct.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Manager delegates from pointers alone | Manager makes delegation decisions using only Tier 1 content | [US-01_manager_delegates_from_pointers.md](./US-01_manager_delegates_from_pointers.md) |
| US-02 | Stage agent works from distilled knowledge | Stage agent uses Tier 2 summaries for domain understanding | [US-02_stage_agent_works_from_distilled.md](./US-02_stage_agent_works_from_distilled.md) |
| US-03 | Active stage agent accesses its own full content | Only the active agent reads Tier 3 outputs for its own stage | [US-03_active_agent_accesses_own_content.md](./US-03_active_agent_accesses_own_content.md) |
| US-04 | Developer verifies tier-agent alignment | Developer audits that each agent type reads the correct tier | [US-04_developer_verifies_alignment.md](./US-04_developer_verifies_alignment.md) |
