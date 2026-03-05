---
resource_id: "927c3637-3c9e-4f9a-8c2c-55515c22398f"
resource_type: "output"
resource_name: "US-01_agent_loads_relevant_context"
---
# US-01: Agent loads most relevant context on entry

**Need**: [Scored Context Retrieval](../README.md)

---

**As a** user who tells the AI to work on a specific entity,
**I want** the system to automatically rank and load the most relevant knowledge files for the task,
**So that** the AI reads the most useful files first instead of guessing or asking me which ones to read.

<!-- section_id: "4b67c7d5-17ce-45ae-a62f-340ca588be93" -->
### What Happens

1. User tells the AI to work on an entity (e.g., "work on the memory system design")
2. System scores available knowledge files by relevance to the task, recency, and importance
3. Agent receives a ranked list and loads the top-scoring files first
4. User gets informed work from the start, without manually directing the AI to specific files

<!-- section_id: "499013ac-5cb3-4998-a56e-1a6e6cd533ff" -->
### Acceptance Criteria

- Agent receives a ranked list of files scored by composite of recency, relevance, and importance
- Top-scored files are demonstrably more relevant than random selection
- Agent loads top files automatically without user having to specify which files to read
