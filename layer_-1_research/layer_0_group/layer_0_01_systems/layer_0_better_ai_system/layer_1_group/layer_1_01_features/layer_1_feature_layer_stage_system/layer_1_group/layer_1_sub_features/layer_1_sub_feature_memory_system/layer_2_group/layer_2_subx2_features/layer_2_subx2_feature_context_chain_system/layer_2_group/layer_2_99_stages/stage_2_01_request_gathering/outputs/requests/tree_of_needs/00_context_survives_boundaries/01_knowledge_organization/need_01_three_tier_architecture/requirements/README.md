---
resource_id: "18f82772-1e3b-4db5-9819-cf653bdd2b71"
resource_type: "readme
output"
resource_name: "README"
---
# Three-Tier Architecture -- Requirements Index

**Need**: [Three-Tier Architecture](../README.md)

<!-- section_id: "2db704d0-d9e9-468f-aa72-d09c7a2db6b9" -->
## Overview

These requirements define the three-tier knowledge architecture that prevents agents from either overloading on raw outputs or operating without sufficient context. They establish exactly what content belongs in each tier -- pointers (Tier 1), distilled knowledge (Tier 2), and full stage outputs (Tier 3) -- with strict boundary rules, size budgets, and anti-patterns. The goal is to ensure an agent reading only Tier 1 and Tier 2 can work competently without ever touching Tier 3.

<!-- section_id: "2424e64e-eeaa-47bb-8b5d-9cb8bdcc578c" -->
## Key Themes

- **Tier Boundary Enforcement**: Each tier has explicit inclusion/exclusion rules, size budgets, and a defined directional flow from stages up through knowledge to pointers -- never the reverse
- **Knowledge File Discipline**: Tier 2 knowledge files must follow a standard template, distill rather than duplicate their sources, and always reference the stage outputs they derive from
- **Pointer Minimalism**: 0AGNOSTIC.md (Tier 1) is strictly limited to identity, pointers, and triggers -- substantive content is forbidden at this level

---

| REQ # | Name | Description | File |
|-------|------|-------------|------|
| REQ-01 | Tier Definitions | Define what content belongs (and does not belong) in each tier | [REQ-01_tier_definitions.md](./REQ-01_tier_definitions.md) |
| REQ-02 | Knowledge File Standards | Standard template and conventions for Tier 2 knowledge files | [REQ-02_knowledge_file_standards.md](./REQ-02_knowledge_file_standards.md) |
| REQ-03 | Pointer Standards | Rules for what belongs in 0AGNOSTIC.md (Tier 1) | [REQ-03_pointer_standards.md](./REQ-03_pointer_standards.md) |
