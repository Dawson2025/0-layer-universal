# US-4: Agent knows which channel to use

**Need**: [Communication Channels](../README.md)

---

**As a** user who expects the AI to put information in the right place without being told,
**I want** agents to have clear rules for which communication channel to use in each situation,
**So that** information reaches the right audience and I can find it where I expect it.

### What Happens

1. User delegates work and the agent needs to communicate something
2. Agent consults channel selection rules from its 0AGNOSTIC.md or protocols
3. Agent uses the correct channel: stage report (for status), handoff doc (for entity transfer), team tools (for real-time coordination), episodic memory (for session history)
4. Information lands in the right place and is discoverable by the right audience
5. User finds status in stage reports, history in episodic memory, and handoffs in handoff docs

### Acceptance Criteria

- Channel selection rules are unambiguous for common communication scenarios
- Each channel has a defined purpose, format, and audience
- Agents do not put information in the wrong channel (e.g., status updates in episodic memory)
- User can predict where to find each type of information
