# US-01: Agent follows reference to source

**Need**: [Reference Format Standard](../README.md)

---

**As a** user who asks the AI to verify or expand on a claim in a knowledge file,
**I want** the AI to follow a standardized reference to the exact source file and section,
**So that** it finds the full explanation in one read instead of searching across all stage outputs.

### What Happens

1. User asks the AI to verify or elaborate on a specific claim (e.g., "vectors can't capture typed relationships")
2. Agent reads the knowledge file and finds a standardized reference (file path + section heading)
3. Agent loads the referenced file and reads the specific section
4. User gets the full explanation with a clear provenance trail

### Acceptance Criteria

- Reference format is parseable by both agents and scripts
- Referenced path is valid and the section exists in the target file
- Agent resolves the reference in one targeted read, not a search
