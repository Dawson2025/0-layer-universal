# US-4: Agent recovers after compaction

**Need**: [Handoff Protocols](../README.md)

---

**As a** user whose AI session hits context limits and gets compacted (loses conversation history),
**I want** the agent to recover its working state by reading identity files, stage reports, and episodic memory,
**So that** compaction does not mean starting from scratch and I don't lose all my progress.

### What Happens

1. User is working with the AI and the context window gets compacted (conversation history is lost)
2. Agent reads its 0AGNOSTIC.md to recover identity and role
3. Agent reads stage reports to understand current project status
4. Agent reads episodic memory to recover recent session details
5. Agent resumes productive work within minutes, not after a lengthy re-exploration

### Acceptance Criteria

- Agent recovers competence in under 5 minutes of reading, not 30 minutes of re-exploration
- Recovery requires only reading existing files (0AGNOSTIC.md, stage reports, episodic memory)
- User does not need to re-explain the entire project after compaction
