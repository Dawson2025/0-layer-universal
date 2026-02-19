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

### Channel Definitions
- MUST define the available communication channels and their purposes:
  - **Stage reports**: stage agent -> manager, async status after stage work
  - **Handoff documents**: entity -> entity, context transfer at entity boundaries
  - **Team tools**: agent <-> agent, real-time coordination during active work (SendMessage, broadcast)
  - **Episodic memory**: agent -> future agent, session-to-session continuity
  - **0INDEX.md**: manager dashboard, rolled-up view of all stages
- MUST define when to use each channel (not all communication needs the same channel)

### Channel Selection Rules
- MUST use stage reports for async status updates from stage agents to managers
- MUST use handoff documents for cross-entity context transfer
- MUST use team tools only for real-time coordination during active parallel work
- MUST use episodic memory for session history that transcends individual stages
- MUST NOT use team tools for async status (stage reports serve that purpose)
- MUST NOT use episodic memory as a substitute for stage reports

### Channel Content Standards
- MUST define content standards for each channel (what goes in a stage report vs a handoff doc vs episodic memory)
- MUST ensure channels do not duplicate each other (each piece of information lives in one place)
- SHOULD define content size limits per channel (stage reports: under 30 lines, handoff docs: under 50 lines)
- MUST NOT allow channels to become catch-all dumps of unstructured information

### Channel Discovery
- MUST make channels discoverable: an agent entering any entity can find all available communication
- MUST define standard locations for each channel type (stage reports in `outputs/`, handoffs in `hand_off_documents/`, episodic in `.0agnostic/episodic_memory/`)

---

## Acceptance Criteria

- [ ] All communication channels are defined with purpose and location
- [ ] Channel selection rules are documented (when to use which channel)
- [ ] Content standards exist per channel
- [ ] Channels do not duplicate each other
- [ ] An agent can discover all available communication channels from the entity structure

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Stage report protocol: `context_chain_system/.0agnostic/protocols/stage_report_protocol.md`
- Handoff documents: `layer_3_group/.../hand_off_documents/`
- Episodic memory: `.0agnostic/episodic_memory/`
- Team tools: Claude Code SendMessage, TaskCreate, TaskUpdate
