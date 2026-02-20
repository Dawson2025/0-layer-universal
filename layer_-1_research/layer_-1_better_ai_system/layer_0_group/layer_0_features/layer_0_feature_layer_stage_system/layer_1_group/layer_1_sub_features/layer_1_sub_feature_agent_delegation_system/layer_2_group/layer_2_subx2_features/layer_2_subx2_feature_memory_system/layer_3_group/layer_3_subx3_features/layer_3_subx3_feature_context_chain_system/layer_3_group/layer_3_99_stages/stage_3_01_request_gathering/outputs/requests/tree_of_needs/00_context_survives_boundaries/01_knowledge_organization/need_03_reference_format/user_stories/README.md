# Reference Format Standard -- User Stories Index

**Need**: [Reference Format Standard](../README.md)

## Overview

These stories cover how knowledge files reference each other across tiers using a consistent, parseable format. They validate that agents can follow references from distilled knowledge to full source content, that automated scripts can parse and validate all references across the system, and that developers creating new knowledge files apply the standard format correctly from the start.

## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Agent follows reference to source | Agent navigates from a Tier 2 reference to the Tier 3 source file | [US-01_agent_follows_reference.md](./US-01_agent_follows_reference.md) |
| US-02 | Script validates all references | Validation script parses and checks every reference in the system | [US-02_script_validates_references.md](./US-02_script_validates_references.md) |
| US-03 | Developer creates new knowledge file | Developer writes a new knowledge file using the standard reference format | [US-03_developer_creates_knowledge_file.md](./US-03_developer_creates_knowledge_file.md) |
