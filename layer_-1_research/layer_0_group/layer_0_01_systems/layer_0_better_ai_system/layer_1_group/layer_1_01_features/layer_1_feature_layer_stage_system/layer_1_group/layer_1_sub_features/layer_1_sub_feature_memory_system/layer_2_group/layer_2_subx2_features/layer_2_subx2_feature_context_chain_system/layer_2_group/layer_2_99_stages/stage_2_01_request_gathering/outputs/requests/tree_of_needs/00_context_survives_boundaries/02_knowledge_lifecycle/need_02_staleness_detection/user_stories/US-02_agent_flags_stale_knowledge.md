---
resource_id: "89ee34cb-d13e-4cef-a92a-e72a6af8eee6"
resource_type: "output"
resource_name: "US-02_agent_flags_stale_knowledge"
---
# US-02: Agent flags potentially stale knowledge

**Need**: [Staleness Detection](../README.md)

---

**As a** user whose AI is reading knowledge files during a session,
**I want** the AI to detect when a knowledge file's sources have been updated since the knowledge was written,
**So that** the AI warns me instead of silently acting on outdated information.

### What Happens

1. AI reads a knowledge file as part of normal context loading
2. AI checks the knowledge file's date against its referenced source files' dates
3. If sources are newer than the knowledge file, AI flags it as potentially stale
4. AI warns the user: "This knowledge file may be outdated -- source was updated on [date]. Should I re-read the source directly?"

### Acceptance Criteria

- Agent can compare knowledge file date against source file dates
- Stale files are flagged with a warning to the user, not silently used
- User can choose to proceed with stale knowledge or have the AI re-read the source
