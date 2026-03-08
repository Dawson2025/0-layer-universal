---
resource_id: "25be6047-be7f-46ad-94e8-74b8fb40f7f6"
resource_type: "readme_output"
resource_name: "README"
---
# Agent Hierarchy -- Requirements Index

**Need**: [Agent Hierarchy](../README.md)

<!-- section_id: "45ff00b2-fa89-466e-b935-a277c62ce947" -->
## Overview

These requirements define the management structure of the agent tree — who manages whom, what decisions each level can make, and how agents discover their position in the hierarchy. The entity tree maps 1:1 to the agent management tree: each entity has one manager, each stage has one active agent, and parent-child relationships are explicit. Authority flows downward (managers direct their agents), escalation flows upward (stage agents escalate to managers), and sibling agents never direct each other.

<!-- section_id: "73d2d5d8-c10a-46af-96ac-408b464e193c" -->
## Key Themes

- **1:1 Entity-Agent Mapping**: Every entity has exactly one manager; every stage has exactly one active agent; parent entities manage child entities through their managers
- **Authority and Escalation**: Stage agents decide within their stage scope, escalate cross-stage decisions; child managers escalate to parent managers; siblings never direct each other
- **Hierarchy Navigation**: Any agent can discover its manager and direct reports from its `0AGNOSTIC.md` parent/children fields — the hierarchy is always derivable from the file system

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Hierarchy Structure | 1:1 entity-to-agent mapping, parent-child relationships | [REQ-01_hierarchy_structure.md](./REQ-01_hierarchy_structure.md) |
| REQ-02 | Authority Rules | What each agent level decides independently vs escalates | [REQ-02_authority_rules.md](./REQ-02_authority_rules.md) |
| REQ-03 | Hierarchy Navigation | Discovering hierarchy from any agent's context | [REQ-03_hierarchy_navigation.md](./REQ-03_hierarchy_navigation.md) |
