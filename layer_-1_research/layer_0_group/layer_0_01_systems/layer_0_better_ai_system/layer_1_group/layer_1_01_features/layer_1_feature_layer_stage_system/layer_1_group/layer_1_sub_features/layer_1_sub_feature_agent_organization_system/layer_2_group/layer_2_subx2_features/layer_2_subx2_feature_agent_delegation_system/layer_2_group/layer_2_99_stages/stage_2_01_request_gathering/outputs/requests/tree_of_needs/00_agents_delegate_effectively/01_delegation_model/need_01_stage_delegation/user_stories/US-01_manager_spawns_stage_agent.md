---
resource_id: "e4e70d25-60ab-45cd-baf8-d850d8002c22"
resource_type: "output"
resource_name: "US-01_manager_spawns_stage_agent"
---
# US-1: Manager spawns a stage agent

**Need**: [Stage Delegation](../README.md)

---

**As a** user who tells the AI to gather requirements for a new feature,
**I want** the system to automatically delegate to a specialized requirements agent,
**So that** I don't need to manually explain the requirements gathering methodology.

<!-- section_id: "d37b46df-d220-4561-bbf6-71ca72ec2648" -->
### What Happens

1. User says "gather requirements for [feature]"
2. Manager reads stage overview, identifies stage 01 as the target
3. Manager spawns a stage agent with task description + directory pointer
4. Stage agent reads its 0AGNOSTIC.md and knows role, methodology, output format
5. Stage agent begins work without needing further instructions

<!-- section_id: "63f6ab7d-8a30-4a1b-b1c0-ea842a15cc3f" -->
### Acceptance Criteria

- Manager's prompt contains only the task and directory path, not methodology
- Stage agent starts working after reading one file
- User does not need to provide methodology or procedure details
