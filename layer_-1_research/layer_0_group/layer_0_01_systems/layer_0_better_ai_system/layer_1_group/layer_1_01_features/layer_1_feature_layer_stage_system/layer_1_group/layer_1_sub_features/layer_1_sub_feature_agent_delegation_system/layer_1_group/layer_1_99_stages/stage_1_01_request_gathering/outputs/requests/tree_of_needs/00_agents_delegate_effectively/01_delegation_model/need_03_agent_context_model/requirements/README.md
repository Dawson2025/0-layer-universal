# Agent Context Model -- Requirements Index

**Need**: [Agent Context Model](../README.md)

## Overview

These requirements define what each agent type (manager, stage agent, sub-feature agent) knows at any given time — split into static context (always loaded), dynamic context (loaded on demand), and never-loaded (out of scope). This prevents context window overflow by ensuring agents only carry what they need for their role. Each of the three agent types gets its own context model specification with explicit rules about what goes where.

## Key Themes

- **Three-Category Model**: Every agent type must have a documented split of static (always in context), dynamic (loaded when needed), and never-loaded (out of scope) content
- **Manager Context**: Static = identity + stage overview + children; Dynamic = stage reports + episodic memory; Never = stage methodology or output details
- **Stage Agent Context**: Static = stage identity + parent identity; Dynamic = relevant parent knowledge files + prior stage report; Never = peer stage outputs or manager coordination logic
- **Sub-Feature Agent Context**: Static = entity identity + children + stage overview; Dynamic = parent chain + own stage reports; Never = sibling entity internals

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Context Model Definition | Define static, dynamic, never-loaded for each agent type | [REQ-01_context_model_definition.md](./REQ-01_context_model_definition.md) |
| REQ-02 | Manager Context Model | What managers always load, load on demand, and never load | [REQ-02_manager_context_model.md](./REQ-02_manager_context_model.md) |
| REQ-03 | Stage Agent Context Model | What stage agents always load, load on demand, and never load | [REQ-03_stage_agent_context_model.md](./REQ-03_stage_agent_context_model.md) |
| REQ-04 | Sub-Feature Agent Context Model | What sub-feature agents always load, load on demand, and never load | [REQ-04_sub_feature_agent_context_model.md](./REQ-04_sub_feature_agent_context_model.md) |
