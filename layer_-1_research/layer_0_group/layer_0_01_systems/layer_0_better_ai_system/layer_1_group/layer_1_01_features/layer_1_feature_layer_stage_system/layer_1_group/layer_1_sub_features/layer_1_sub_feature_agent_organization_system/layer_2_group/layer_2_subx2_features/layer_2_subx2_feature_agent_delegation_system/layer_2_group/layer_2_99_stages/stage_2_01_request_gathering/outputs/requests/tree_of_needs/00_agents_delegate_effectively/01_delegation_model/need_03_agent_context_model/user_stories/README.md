---
resource_id: "55a0cf9d-d7f4-463f-8570-4fd4c79124eb"
resource_type: "readme
output"
resource_name: "README"
---
# Agent Context Model -- User Stories Index

**Need**: [Agent Context Model](../README.md)

<!-- section_id: "dbad021a-9554-488e-9ece-7e875f369880" -->
## Overview

These stories cover how each agent type (manager, stage agent, sub-feature agent) loads the right amount of context without overflow or incompetence. They validate that static, dynamic, and never-loaded boundaries are defined per agent type, that agents operate within their scoped context, and that the developer can audit whether those boundaries are being respected.

<!-- section_id: "679e5e4d-090b-4086-b25f-7c2b125e85d3" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Manager loads only what it needs | Manager context excludes stage-level operational detail | [US-01_manager_loads_only_needed.md](./US-01_manager_loads_only_needed.md) |
| US-02 | Stage agent loads domain knowledge on demand | Stage agent reads parent knowledge without loading peer stages | [US-02_stage_agent_loads_knowledge.md](./US-02_stage_agent_loads_knowledge.md) |
| US-03 | Sub-feature agent sees its own tree | Sub-feature agent loads only its own children and scope | [US-03_sub_feature_sees_own_tree.md](./US-03_sub_feature_sees_own_tree.md) |
| US-04 | Developer can audit context boundaries | Developer inspects what each agent type actually loads | [US-04_developer_audits_boundaries.md](./US-04_developer_audits_boundaries.md) |
