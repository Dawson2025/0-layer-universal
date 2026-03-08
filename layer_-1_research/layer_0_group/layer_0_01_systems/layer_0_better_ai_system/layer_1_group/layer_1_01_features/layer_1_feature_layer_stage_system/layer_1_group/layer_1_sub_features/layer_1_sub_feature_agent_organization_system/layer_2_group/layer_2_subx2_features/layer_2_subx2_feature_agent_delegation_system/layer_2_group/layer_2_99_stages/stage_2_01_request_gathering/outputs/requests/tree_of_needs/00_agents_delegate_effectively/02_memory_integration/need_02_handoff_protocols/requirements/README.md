---
resource_id: "0e02947e-659a-4ded-a0ae-c81e8b893b14"
resource_type: "readme_output"
resource_name: "README"
---
# Handoff Protocols -- Requirements Index

**Need**: [Handoff Protocols](../README.md)

<!-- section_id: "40047d95-e606-4f52-900c-78d599fd92bb" -->
## Overview

These requirements define how context is preserved across four types of agent transitions: session-to-session (same stage, different sessions), agent-to-agent (manager delegates to stage agent and back), cross-entity (parent hands off to child entity), and the minimum viable handoff content for any transition. Stage reports are the primary mechanism for session handoffs; handoff documents serve cross-entity transitions. The receiving agent must never need to read the sending agent's full context.

<!-- section_id: "9e96a3f9-5225-4857-982c-8ebb56a6782d" -->
## Key Themes

- **Session Continuity**: Stage reports + episodic memory preserve state between sessions; the next agent reads these first and knows exactly what to do
- **Delegation Handoffs**: Managers provide task + context pointers when delegating; stage agents return stage reports when done — no full-context transfer in either direction
- **Cross-Entity Transfers**: Parent-to-child handoffs use `hand_off_documents/incoming/` with clear scope and expectations; child-to-parent uses `outgoing/`
- **Minimum Viable Handoff**: Every transition must preserve status, key decisions, open questions, and next steps — never full operational history

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Session-to-Session Handoffs | How agents preserve state between sessions | [REQ-01_session_to_session_handoffs.md](./REQ-01_session_to_session_handoffs.md) |
| REQ-02 | Agent-to-Agent Handoffs | What managers provide when delegating, what agents return | [REQ-02_agent_to_agent_handoffs.md](./REQ-02_agent_to_agent_handoffs.md) |
| REQ-03 | Cross-Entity Handoffs | How parent entities hand off to child entities | [REQ-03_cross_entity_handoffs.md](./REQ-03_cross_entity_handoffs.md) |
| REQ-04 | Handoff Completeness | Minimum viable handoff content at every transition | [REQ-04_handoff_completeness.md](./REQ-04_handoff_completeness.md) |
