---
resource_id: "ed3a35d5-3a3e-4420-b772-be26ae1d3b5c"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Communication Channels

**Branch**: [03_coordination_patterns](../)
**Question**: "How do agents share information?"
**Version**: 1.0.0

---

<!-- section_id: "24401d27-b756-450c-8b61-fe799fdb877c" -->
## Definition

Communication channels are the mechanisms agents use to share information with each other. These include stage reports (stage agent to manager), handoff documents (entity to entity), team tools (real-time coordination), and episodic memory (async session-to-session continuity).

---

<!-- section_id: "baedb1c9-e994-47ef-b024-1b2636d7fb3f" -->
## Why This Matters

- Without defined channels, agents produce outputs that nobody reads
- Agents duplicate effort because they cannot see what others have done
- Real-time and async communication serve different purposes -- both are needed
- The right channel for the right message prevents both information loss and information overload

---

<!-- section_id: "31bed6f1-ec89-49f6-9eed-e4011b0e4c78" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "7da56244-00fd-42cd-a4b0-419f30dc16ce" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "34431ea6-0d54-44fa-8284-08715a243b33" -->
## Acceptance Criteria

- [ ] All communication channels are defined with purpose and location
- [ ] Channel selection rules are documented (when to use which channel)
- [ ] Content standards exist per channel
- [ ] Channels do not duplicate each other
- [ ] An agent can discover all available communication channels from the entity structure

---

<!-- section_id: "1bfe7c13-f6fb-4290-99e7-b2dc5059c788" -->
## Research References

- Stage report protocol: `context_chain_system/.0agnostic/protocols/stage_report_protocol.md`
- Handoff documents: `layer_3_group/.../hand_off_documents/`
- Episodic memory: `.0agnostic/episodic_memory/`
- Team tools: Claude Code SendMessage, TaskCreate, TaskUpdate
