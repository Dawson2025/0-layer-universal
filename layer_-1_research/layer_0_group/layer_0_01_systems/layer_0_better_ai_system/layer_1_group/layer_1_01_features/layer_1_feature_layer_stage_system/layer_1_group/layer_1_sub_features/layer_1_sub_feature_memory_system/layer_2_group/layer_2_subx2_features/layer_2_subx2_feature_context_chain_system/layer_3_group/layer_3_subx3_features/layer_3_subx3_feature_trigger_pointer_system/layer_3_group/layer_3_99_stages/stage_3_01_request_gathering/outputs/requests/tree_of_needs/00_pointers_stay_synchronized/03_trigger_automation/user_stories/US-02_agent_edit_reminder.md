---
resource_id: "e502afac-1483-476e-8039-ecb7ee4cac4e"
resource_type: "output"
resource_name: "US-02_agent_edit_reminder"
---
# US-02: Agent Edits Trigger Validation Reminder

**Need**: [Trigger Automation](../README.md)

---

**As an** AI agent editing pointer files,
**I want** a hook to automatically remind me to validate pointers after my edits,
**So that** I don't accidentally leave stale pointers behind without knowing.

<!-- section_id: "c8c0680e-5143-42ca-867c-de4bfdfa68cb" -->
### What Happens

1. AI agent uses a file editing tool on a `.md` file
2. The system detects that the file has pointer YAML frontmatter
3. A non-blocking notification reminds the agent: "This is a pointer file — validate pointers"
4. Agent sees the reminder and runs validation
5. If validation fails, agent runs full sync to fix paths

<!-- section_id: "4939b2f7-32c2-4daa-b0d9-c79cf7ae031a" -->
### Acceptance Criteria

- Hook fires automatically after Edit/Write on `.md` files
- Reminder only appears for actual pointer files (has `pointer_to:` in frontmatter)
- Hook does not block or slow down normal file operations
- Hook timeout is ≤10 seconds
- Non-pointer `.md` files are silently ignored
