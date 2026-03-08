---
resource_id: "a14f670f-cff8-44c8-80b4-92ef6c4929ad"
resource_type: "readme_output"
resource_name: "README"
---
# Three-Tier Delegation -- Requirements Index

**Need**: [Three-Tier Delegation](../README.md)

<!-- section_id: "422ea45c-e0f7-4c8d-889c-1a625277d29c" -->
## Overview

These requirements map the three-tier knowledge architecture (pointers, distilled, full) to delegation roles. Managers operate at Tier 1 (0AGNOSTIC.md, stage overview, children list) and make delegation decisions from pointers alone. Stage agents work at Tier 2 (distilled knowledge files) for domain understanding, plus their own Tier 3 (stage outputs) for active work. The key constraint is that tiers must be genuinely distilled (not copied) and kept current through consolidation.

<!-- section_id: "3d9e23cc-3452-404a-b3d9-176f3d0fe8f1" -->
## Key Themes

- **Tier-to-Agent Mapping**: Manager = Tier 1 (pointers); Stage Agent = Tier 2 (distilled) + own Tier 3 (active outputs); agents must not routinely access other stages' Tier 3
- **Delegation from Pointers**: All delegation decisions must be makeable from Tier 1 alone — if a manager needs to read Tier 3 to decide what to delegate, the system is broken
- **Tier Integrity**: Tier 1 must always be current; Tier 2 must be distilled from Tier 3 (not a copy); consolidation maintains the relationship between tiers

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Tier-to-Agent Mapping | Which tier each agent type primarily operates at | [REQ-01_tier_to_agent_mapping.md](./REQ-01_tier_to_agent_mapping.md) |
| REQ-02 | Delegation-Aware Tiering | Delegation decisions from Tier 1 alone, stage work from Tier 2+3 | [REQ-02_delegation_aware_tiering.md](./REQ-02_delegation_aware_tiering.md) |
| REQ-03 | Tier Integrity | Keeping tiers current, distilled not duplicated | [REQ-03_tier_integrity.md](./REQ-03_tier_integrity.md) |
