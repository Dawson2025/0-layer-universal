---
resource_id: "0d4714f7-45c9-4cdc-a86a-ce3a717cb5ee"
resource_type: "output"
resource_name: "US-02_agent_finds_details"
---
# US-02: Agent knows where to find details

**Need**: [Three-Tier Architecture](../README.md)

---

**As a** user who asks the AI a specific technical question (e.g., STDP timing window),
**I want** the AI to look up the exact source file instead of searching blindly,
**So that** I get a precise answer quickly, not a vague guess or a long wait while it hunts through files.

<!-- section_id: "4c64d060-aaf6-48c9-8e68-713788dcea1f" -->
### What Happens

1. User asks the AI a detailed domain question
2. Agent reads the relevant knowledge file (Tier 2) which contains a summary
3. Knowledge file has a "See [file] Section [X]" reference pointing to the full explanation (Tier 3)
4. Agent loads one targeted file and reads the specific section
5. User gets a precise, sourced answer

<!-- section_id: "a7883ae0-bdfc-4a17-99ff-e8782a6f93be" -->
### Acceptance Criteria

- Every knowledge file claim has a "See [file] Section [X]" reference to its source
- Agent loads one targeted file instead of searching across all outputs
