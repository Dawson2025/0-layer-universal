# US-2: Parallel agents coordinate in real time

**Need**: [Communication Channels](../README.md)

---

**As a** user who has the AI working on two tasks in parallel and wants them to not conflict,
**I want** parallel agents to use real-time messaging (SendMessage) to coordinate on shared concerns,
**So that** parallel work does not produce conflicting outputs that I have to manually reconcile.

### What Happens

1. User has two stage agents working in parallel on independent but related tasks
2. Agent A discovers a shared concern (e.g., a naming convention both agents need to follow)
3. Agent A uses SendMessage to notify Agent B of the concern
4. Agent B adjusts its work to align with Agent A's findings
5. Both agents produce compatible outputs without the manager mediating

### Acceptance Criteria

- Parallel agents use SendMessage for real-time coordination, not stage reports
- Shared concerns are resolved between agents without waiting for the manager
- User does not need to manually reconcile conflicting parallel outputs
