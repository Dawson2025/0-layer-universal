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

### Session-to-Session Handoffs
- MUST define how an agent preserves its state before session ends (stage reports, episodic memory)
- MUST define how the next session's agent discovers prior state (what to read first)
- MUST use stage reports as the primary session-to-session handoff mechanism for stage work
- SHOULD use episodic memory (`.0agnostic/episodic_memory/`) for session history beyond stage reports

### Agent-to-Agent Handoffs
- MUST define what the manager provides when delegating to a stage agent (task description, context pointers)
- MUST define what the stage agent returns to the manager (stage report, output summary)
- MUST NOT require the receiving agent to read the sending agent's full context
- SHOULD define a standard handoff document format for cross-entity transitions

### Cross-Entity Handoffs
- MUST define how parent entities hand off work to child entities (and vice versa)
- MUST use handoff documents in `hand_off_documents/incoming/` and `hand_off_documents/outgoing/`
- SHOULD define when a handoff document is required vs when a stage report suffices

### Handoff Completeness
- MUST define the minimum viable handoff: what information MUST be preserved at every transition
- MUST include: current status, key decisions made, open questions, next steps
- MUST NOT include: full operational history (that lives in stage outputs and episodic memory)

---

## Acceptance Criteria

- [ ] Session-to-session handoff protocol is documented
- [ ] Agent-to-agent handoff protocol is documented
- [ ] Cross-entity handoff protocol is documented
- [ ] Minimum viable handoff content is defined
- [ ] A new agent can pick up where the previous one left off by following the handoff protocol

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Existing handoff documents: `context_chain_system/layer_3_group/.../hand_off_documents/`
- Episodic memory system: `.0agnostic/episodic_memory/`
- Stage report protocol as a form of handoff
