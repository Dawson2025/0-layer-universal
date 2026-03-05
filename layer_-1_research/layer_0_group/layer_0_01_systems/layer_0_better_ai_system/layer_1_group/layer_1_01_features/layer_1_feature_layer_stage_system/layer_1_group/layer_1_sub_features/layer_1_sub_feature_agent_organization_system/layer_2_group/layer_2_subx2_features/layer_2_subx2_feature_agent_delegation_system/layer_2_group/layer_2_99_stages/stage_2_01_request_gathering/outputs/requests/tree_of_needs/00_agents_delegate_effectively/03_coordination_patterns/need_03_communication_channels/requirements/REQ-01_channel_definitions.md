---
resource_id: "403db1fb-e186-4931-bf1b-5fcdb6a5732b"
resource_type: "output"
resource_name: "REQ-01_channel_definitions"
---
# Channel Definitions

**Need**: [Communication Channels](../README.md)

---

- MUST define the available communication channels and their purposes:
  - **Stage reports**: stage agent -> manager, async status after stage work
  - **Handoff documents**: entity -> entity, context transfer at entity boundaries
  - **Team tools**: agent <-> agent, real-time coordination during active work (SendMessage, broadcast)
  - **Episodic memory**: agent -> future agent, session-to-session continuity
  - **0INDEX.md**: manager dashboard, rolled-up view of all stages
- MUST define when to use each channel (not all communication needs the same channel)
