# Staleness Detection -- User Stories Index

**Need**: [Staleness Detection](../README.md)

## Overview

These stories cover how the system detects when distilled knowledge files (Tier 2) have drifted from their source stage outputs (Tier 3). They validate that the developer can run a freshness check before starting a session to identify which knowledge files need updating, and that agents proactively flag potentially stale knowledge when they encounter references whose sources have changed since the last consolidation.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Developer checks freshness before a session | Developer runs a staleness report to find outdated knowledge files | [US-01_developer_checks_freshness.md](./US-01_developer_checks_freshness.md) |
| US-02 | Agent flags potentially stale knowledge | Agent detects source changes and warns about possible staleness | [US-02_agent_flags_stale_knowledge.md](./US-02_agent_flags_stale_knowledge.md) |
