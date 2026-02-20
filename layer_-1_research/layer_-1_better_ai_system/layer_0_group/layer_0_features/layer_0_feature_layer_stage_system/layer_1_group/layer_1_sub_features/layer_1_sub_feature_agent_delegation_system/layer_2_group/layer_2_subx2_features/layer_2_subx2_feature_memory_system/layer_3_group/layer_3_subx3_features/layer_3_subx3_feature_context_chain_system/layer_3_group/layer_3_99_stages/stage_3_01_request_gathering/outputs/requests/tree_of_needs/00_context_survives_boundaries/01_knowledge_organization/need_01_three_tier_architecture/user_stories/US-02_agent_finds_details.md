# US-02: Agent knows where to find details

**Need**: [Three-Tier Architecture](../README.md)

---

**As a** user who asks the AI a specific technical question (e.g., STDP timing window),
**I want** the AI to look up the exact source file instead of searching blindly,
**So that** I get a precise answer quickly, not a vague guess or a long wait while it hunts through files.

### What Happens

1. User asks the AI a detailed domain question
2. Agent reads the relevant knowledge file (Tier 2) which contains a summary
3. Knowledge file has a "See [file] Section [X]" reference pointing to the full explanation (Tier 3)
4. Agent loads one targeted file and reads the specific section
5. User gets a precise, sourced answer

### Acceptance Criteria

- Every knowledge file claim has a "See [file] Section [X]" reference to its source
- Agent loads one targeted file instead of searching across all outputs
