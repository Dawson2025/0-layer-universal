# US-2: Stage agent knows its manager

**Need**: [Agent Hierarchy](../README.md)

---

**As a** user who expects stage agents to escalate issues they cannot solve on their own,
**I want** each stage agent to know which entity manager it reports to,
**So that** the agent escalates scope-exceeding issues to the right manager instead of getting stuck or guessing.

### What Happens

1. User delegates work and the stage agent encounters something outside its scope
2. Stage agent reads its 0AGNOSTIC.md and finds a parent pointer to the entity manager
3. Stage agent escalates the issue to its manager (via stage report or team tools)
4. Manager receives the escalation and presents it to the user or resolves it
5. User gets informed about cross-scope issues without the stage agent silently failing

### Acceptance Criteria

- Stage agent's 0AGNOSTIC.md includes a parent pointer to the entity manager
- Stage agent can identify its manager without reading external files
- Escalation goes to the correct manager, not a sibling or unrelated agent
