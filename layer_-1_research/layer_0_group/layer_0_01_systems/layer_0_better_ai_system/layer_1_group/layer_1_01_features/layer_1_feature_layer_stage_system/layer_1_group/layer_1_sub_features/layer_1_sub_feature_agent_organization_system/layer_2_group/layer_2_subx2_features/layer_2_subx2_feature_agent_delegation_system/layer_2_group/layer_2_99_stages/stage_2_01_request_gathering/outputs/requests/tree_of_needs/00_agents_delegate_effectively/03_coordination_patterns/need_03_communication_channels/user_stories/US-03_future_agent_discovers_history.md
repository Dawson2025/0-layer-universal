---
resource_id: "e5f31053-6d06-48fb-9798-8fd052f8301e"
resource_type: "output"
resource_name: "US-03_future_agent_discovers_history"
---
# US-3: Future agent discovers session history

**Need**: [Communication Channels](../README.md)

---

**As a** user who returns to a project after weeks and expects the AI to know what was done before,
**I want** any new agent to discover the full work history through episodic memory and stage reports,
**So that** the AI can contribute meaningfully without me having to summarize weeks of prior work.

### What Happens

1. User returns to a project after a long break and says "continue this project"
2. New agent reads episodic memory (`outputs/episodic/index.md`) for session history
3. New agent reads stage reports across all stages for current status
4. Agent builds a picture of: what has been done, what is in progress, what is next
5. Agent resumes productive work without the user needing to provide a history summary

### Acceptance Criteria

- Episodic memory + stage reports provide enough context to understand full project history
- New agent can identify current status and next steps from these files alone
- User does not need to summarize prior work to the new agent
