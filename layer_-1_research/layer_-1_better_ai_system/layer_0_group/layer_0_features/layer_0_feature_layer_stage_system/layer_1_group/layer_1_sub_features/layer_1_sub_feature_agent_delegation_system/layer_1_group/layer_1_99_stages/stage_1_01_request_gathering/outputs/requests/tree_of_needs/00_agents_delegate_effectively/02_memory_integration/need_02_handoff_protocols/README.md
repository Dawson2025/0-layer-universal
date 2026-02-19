# Need: Handoff Protocols

**Branch**: [02_memory_integration](../)
**Question**: "How is context preserved when transitioning between agents?"
**Version**: 1.0.0

---

## Definition

Handoff protocols define how context is transferred when one agent stops and another starts. This includes session-to-session transitions (same role, different session), agent-to-agent transitions (manager to stage agent), and cross-entity transitions (parent to child entity agent).

---

## Why This Matters

- Without handoff protocols, every new session or new agent starts from scratch
- Critical decisions, progress, and understanding are lost at each transition
- Re-discovery wastes tokens and time -- agents repeat work already done
- The delegation model only works if the delegated agent can pick up where the last agent left off

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Session-to-session handoff protocol is documented
- [ ] Agent-to-agent handoff protocol is documented
- [ ] Cross-entity handoff protocol is documented
- [ ] Minimum viable handoff content is defined
- [ ] A new agent can pick up where the previous one left off by following the handoff protocol

---

## Research References

- Existing handoff documents: `context_chain_system/layer_3_group/.../hand_off_documents/`
- Episodic memory system: `.0agnostic/episodic_memory/`
- Stage report protocol as a form of handoff
