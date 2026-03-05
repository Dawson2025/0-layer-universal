---
resource_id: "bdc8f9a1-a188-4bdb-8fb2-e7d4e72df9a7"
resource_type: "output"
resource_name: "REQ-02_agent_to_agent_handoffs"
---
# Agent-to-Agent Handoffs

**Need**: [Handoff Protocols](../README.md)

---

- MUST define what the manager provides when delegating to a stage agent (task description, context pointers)
- MUST define what the stage agent returns to the manager (stage report, output summary)
- MUST NOT require the receiving agent to read the sending agent's full context
- SHOULD define a standard handoff document format for cross-entity transitions
