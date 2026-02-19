# Need: Communication Channels

**Branch**: [03_coordination_patterns](../)
**Question**: "How do agents share information?"
**Version**: 1.0.0

---

## Definition

Communication channels are the mechanisms agents use to share information with each other. These include stage reports (stage agent to manager), handoff documents (entity to entity), team tools (real-time coordination), and episodic memory (async session-to-session continuity).

---

## Why This Matters

- Without defined channels, agents produce outputs that nobody reads
- Agents duplicate effort because they cannot see what others have done
- Real-time and async communication serve different purposes -- both are needed
- The right channel for the right message prevents both information loss and information overload

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] All communication channels are defined with purpose and location
- [ ] Channel selection rules are documented (when to use which channel)
- [ ] Content standards exist per channel
- [ ] Channels do not duplicate each other
- [ ] An agent can discover all available communication channels from the entity structure

---

## Research References

- Stage report protocol: `context_chain_system/.0agnostic/protocols/stage_report_protocol.md`
- Handoff documents: `layer_3_group/.../hand_off_documents/`
- Episodic memory: `.0agnostic/episodic_memory/`
- Team tools: Claude Code SendMessage, TaskCreate, TaskUpdate
