---
resource_id: "9ba9d018-9d50-4099-abd1-81092ee20b4c"
resource_type: "output"
resource_name: "US-03_chain_stops_at_right_depth"
---
# US-3: Chain stops at the right depth

**Need**: [Context Chain Support](../README.md)

---

**As a** user who works in a deeply nested project and wants the AI to stay performant,
**I want** the context chain to load only the stage and its parent entity, not every ancestor up to root,
**So that** the AI's context window is not consumed by irrelevant ancestor context.

<!-- section_id: "000f3e20-f21a-4375-8c05-5baabf7580cd" -->
### What Happens

1. User tells the AI to work on a stage deep in the hierarchy (e.g., layer -1 > project > feature > sub-feature > stage)
2. Stage agent's context chain loads: its own 0AGNOSTIC.md + parent entity's 0AGNOSTIC.md
3. Chain does NOT load grandparent, great-grandparent, or root-level context
4. Stage agent has maximum context window available for its actual work
5. User gets fast, focused responses because the agent is not bloated with ancestor context

<!-- section_id: "8ff27a9e-8d7e-433c-9dad-7cd01c4b1be8" -->
### Acceptance Criteria

- Stage agent's chain is limited to 2 levels (self + parent entity)
- Ancestors beyond the parent are not loaded into the stage agent's context
- Context window usage is predictable and bounded
