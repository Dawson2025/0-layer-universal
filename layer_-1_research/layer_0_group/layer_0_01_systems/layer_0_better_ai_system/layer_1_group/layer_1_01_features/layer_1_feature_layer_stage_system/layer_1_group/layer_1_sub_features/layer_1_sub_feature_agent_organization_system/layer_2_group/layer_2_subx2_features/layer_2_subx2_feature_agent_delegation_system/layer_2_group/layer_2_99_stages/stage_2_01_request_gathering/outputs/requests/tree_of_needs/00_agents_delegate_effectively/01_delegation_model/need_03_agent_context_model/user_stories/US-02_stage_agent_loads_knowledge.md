---
resource_id: "97ed063c-11be-4e1d-9a5e-dad015a8ade5"
resource_type: "output"
resource_name: "US-02_stage_agent_loads_knowledge"
---
# US-2: Stage agent loads domain knowledge on demand

**Need**: [Agent Context Model](../README.md)

---

**As a** user who expects the AI to understand domain concepts without loading everything at once,
**I want** the stage agent to load only the specific knowledge file relevant to its current task,
**So that** the AI stays efficient and does not waste context on irrelevant domain knowledge.

<!-- section_id: "16d9215d-3ee5-40d3-9906-5492f55a236c" -->
### What Happens

1. User tells the AI to work on a specific stage task
2. Stage agent reads its 0AGNOSTIC.md and identifies which domain knowledge is needed
3. Stage agent reads 1-2 targeted knowledge files from the parent entity's `.0agnostic/knowledge/`
4. Stage agent does NOT load the entire knowledge directory
5. Stage agent proceeds with domain understanding and maximum remaining context for its work

<!-- section_id: "697abfd0-5ba3-4765-9b26-2cde90fdabca" -->
### Acceptance Criteria

- Stage agent reads at most 1-2 knowledge files per task, guided by its 0AGNOSTIC.md
- The 0AGNOSTIC.md tells the agent exactly which knowledge file to read
- Stage agent never bulk-loads the entire knowledge directory
