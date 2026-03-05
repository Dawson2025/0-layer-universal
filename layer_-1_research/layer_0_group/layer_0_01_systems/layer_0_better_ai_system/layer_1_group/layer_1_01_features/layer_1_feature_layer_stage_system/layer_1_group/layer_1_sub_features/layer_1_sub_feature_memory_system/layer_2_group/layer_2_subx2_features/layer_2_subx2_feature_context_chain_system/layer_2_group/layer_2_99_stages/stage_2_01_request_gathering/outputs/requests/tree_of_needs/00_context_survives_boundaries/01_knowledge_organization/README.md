---
resource_id: "80fd9fca-07f1-460c-8e37-9c5238bbe6dc"
resource_type: "readme
output"
resource_name: "README"
---
# Branch: Knowledge is ORGANIZED

**Parent**: [00_context_survives_boundaries](../)

---

<!-- section_id: "f846beb5-4643-4bfb-a034-e46498d3c15c" -->
## Core Question

> "Where does each kind of content live, and how do the tiers connect?"

---

<!-- section_id: "153f841c-729b-46bc-b5e9-95b5fae5be58" -->
## Description

For context to survive boundaries, knowledge must be organized into clear tiers with defined rules for what goes where. Without this, agents either load too much (blowing the window) or too little (losing competence).

The three failure modes:
1. **Everything in static context** → context window overflow, wasted tokens
2. **Everything in stage outputs only** → agent must re-read thousands of lines
3. **Duplicated across locations** → two sources of truth that drift apart

---

<!-- section_id: "b588a322-83cf-497d-899c-b7b9b5161cc5" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_three_tier_architecture](./need_01_three_tier_architecture/) | "What goes in each tier?" | Define pointer → distilled → full content pattern |
| [need_02_knowledge_graph](./need_02_knowledge_graph/) | "How are entities connected?" | Formalize relationships as JSON-LD graph |
| [need_03_reference_format](./need_03_reference_format/) | "How do tiers reference each other?" | Standard format for cross-tier links |

---

<!-- section_id: "cd4445ad-432c-4abf-9aff-6bd75fc8dbfa" -->
## Key Insight

Organization follows the brain's consolidation pattern: raw episodic memories (stage outputs) are distilled into semantic knowledge (.0agnostic/knowledge/), with navigation pointers (0AGNOSTIC.md) on top. Each tier serves a different access pattern — always-loaded, on-demand understanding, or on-demand detail.
