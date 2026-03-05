---
resource_id: "7aef6c1d-a038-4c10-91fc-513a7b2edf6b"
resource_type: "readme
output"
resource_name: "README"
---
# Context Chain Support -- Requirements Index

**Need**: [Context Chain Support](../README.md)

## Overview

These requirements define how context chains enable delegation by ensuring each agent type gets the right amount of hierarchy context. Managers need enough chain context to decide which stage needs work; stage agents need parent identity and domain pointers but not the full ancestor tree. The key constraint is progressive content filtering — each ancestor level loads less detail — and chain depth limits per agent type to prevent context overflow.

## Key Themes

- **Chain Loading for Delegation**: The context chain must include entity identity, children list, and stage status — enough for managers to make delegation decisions without reading stage details
- **Depth Limits by Agent Type**: Managers load 3 levels (self + parent + grandparent); stage agents load 2 levels (self + parent entity); deeper ancestors are not loaded automatically
- **Progressive Filtering**: Self gets full content, parent gets identity + triggers, grandparent gets identity only — no sibling entities loaded through the chain

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Chain Loading for Delegation | Which chain entries support delegation decisions | [REQ-01_chain_loading_for_delegation.md](./REQ-01_chain_loading_for_delegation.md) |
| REQ-02 | Chain Depth for Agent Types | How far up the hierarchy each agent type loads | [REQ-02_chain_depth_for_agent_types.md](./REQ-02_chain_depth_for_agent_types.md) |
| REQ-03 | Chain Content Filtering | What content from each chain level is loaded | [REQ-03_chain_content_filtering.md](./REQ-03_chain_content_filtering.md) |
