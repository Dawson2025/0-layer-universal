# Consolidation Process -- User Stories Index

**Need**: [Consolidation Process](../README.md)

## Overview

These stories cover the process of distilling raw stage outputs (Tier 3) into concise knowledge files (Tier 2) at natural stage boundaries. They validate that the developer performs consolidation at the right moments using a defined protocol, that agents surface reminders when consolidation is due, and that the developer can verify the quality and compression ratio of the distilled result against its source material.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Developer distills research at stage boundary | Developer creates Tier 2 knowledge files when a stage completes | [US-01_developer_distills_research.md](./US-01_developer_distills_research.md) |
| US-02 | Agent triggers consolidation reminder | Agent detects a stage boundary and prompts the developer to consolidate | [US-02_agent_triggers_consolidation_reminder.md](./US-02_agent_triggers_consolidation_reminder.md) |
| US-03 | Developer verifies consolidation quality | Developer checks compression ratio and accuracy of distilled content | [US-03_developer_verifies_consolidation_quality.md](./US-03_developer_verifies_consolidation_quality.md) |
