# Session-to-Session Handoffs

**Need**: [Handoff Protocols](../README.md)

---

- MUST define how an agent preserves its state before session ends (stage reports, episodic memory)
- MUST define how the next session's agent discovers prior state (what to read first)
- MUST use stage reports as the primary session-to-session handoff mechanism for stage work
- SHOULD use episodic memory (`.0agnostic/episodic_memory/`) for session history beyond stage reports
