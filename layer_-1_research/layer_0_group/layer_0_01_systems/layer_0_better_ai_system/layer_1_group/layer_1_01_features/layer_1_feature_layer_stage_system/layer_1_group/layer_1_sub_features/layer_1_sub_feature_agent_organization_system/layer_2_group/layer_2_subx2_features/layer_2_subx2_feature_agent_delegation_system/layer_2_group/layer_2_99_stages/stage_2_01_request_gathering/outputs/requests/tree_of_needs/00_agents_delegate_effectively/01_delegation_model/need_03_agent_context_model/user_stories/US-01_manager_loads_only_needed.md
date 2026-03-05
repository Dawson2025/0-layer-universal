---
resource_id: "9a25bd4c-698d-4727-86bb-39cfae1b8bd4"
resource_type: "output"
resource_name: "US-01_manager_loads_only_needed"
---
# US-1: Manager loads only what it needs

**Need**: [Agent Context Model](../README.md)

---

**As a** user who wants the AI to respond quickly to coordination requests,
**I want** the manager agent to load only its identity, stage overview, and children list into static context,
**So that** the AI has room in its context window for actual coordination work instead of being filled with stage details.

### What Happens

1. User starts a session and asks the AI to manage a project
2. Manager loads its static context: identity, stage overview, children list
3. Manager does NOT load stage-level methodology, knowledge files, or output details
4. Manager has ample context window space for reading reports, making decisions, and delegating
5. User gets fast, focused coordination responses

### Acceptance Criteria

- Manager's static context is under 200 lines and contains zero stage methodology
- Manager can still make delegation decisions from its static context alone
- Context window is not consumed by operational detail
