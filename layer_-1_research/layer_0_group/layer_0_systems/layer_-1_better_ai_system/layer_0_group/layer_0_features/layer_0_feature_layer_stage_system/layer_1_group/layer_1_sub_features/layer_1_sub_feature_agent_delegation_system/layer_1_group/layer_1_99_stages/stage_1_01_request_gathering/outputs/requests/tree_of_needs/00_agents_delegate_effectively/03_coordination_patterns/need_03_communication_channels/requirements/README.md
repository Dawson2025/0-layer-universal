# Communication Channels -- Requirements Index

**Need**: [Communication Channels](../README.md)

## Overview

These requirements define the five communication channels available to agents and the rules for when to use each one. Stage reports serve async status (stage agent → manager), handoff documents serve cross-entity transfers, team tools serve real-time coordination during parallel work, episodic memory serves session-to-session continuity, and 0INDEX.md serves as the manager dashboard. Each channel has a defined purpose, content standards, and size limits — and channels must not duplicate each other.

## Key Themes

- **Channel Definitions**: Five distinct channels with clear purposes — stage reports, handoff documents, team tools (SendMessage/broadcast), episodic memory, and 0INDEX.md
- **Selection Rules**: Stage reports for async status, handoff docs for entity transfers, team tools only for active parallel coordination, episodic for session history; no mixing purposes
- **Content Standards**: Each channel has size limits (reports: 30 lines, handoffs: 50 lines) and no duplication — each piece of information lives in exactly one channel
- **Discoverability**: Agents entering any entity can find all channels at standard locations (outputs/, hand_off_documents/, .0agnostic/episodic_memory/)

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Channel Definitions | Available channels and their purposes | [REQ-01_channel_definitions.md](./REQ-01_channel_definitions.md) |
| REQ-02 | Channel Selection Rules | When to use each channel | [REQ-02_channel_selection_rules.md](./REQ-02_channel_selection_rules.md) |
| REQ-03 | Channel Content Standards | What goes in each channel, size limits, no duplication | [REQ-03_channel_content_standards.md](./REQ-03_channel_content_standards.md) |
| REQ-04 | Channel Discovery | How agents find available communication channels | [REQ-04_channel_discovery.md](./REQ-04_channel_discovery.md) |
