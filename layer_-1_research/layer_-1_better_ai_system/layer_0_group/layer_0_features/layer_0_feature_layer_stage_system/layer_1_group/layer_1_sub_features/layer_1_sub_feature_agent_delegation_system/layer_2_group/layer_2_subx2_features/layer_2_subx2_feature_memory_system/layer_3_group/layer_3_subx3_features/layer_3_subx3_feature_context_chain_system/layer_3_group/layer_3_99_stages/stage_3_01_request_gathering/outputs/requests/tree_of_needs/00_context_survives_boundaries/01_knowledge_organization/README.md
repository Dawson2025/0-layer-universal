# Branch: Knowledge is ORGANIZED

**Parent**: [00_context_survives_boundaries](../)

---

## Core Question

> "Where does each kind of content live, and how do the tiers connect?"

---

## Description

For context to survive boundaries, knowledge must be organized into clear tiers with defined rules for what goes where. Without this, agents either load too much (blowing the window) or too little (losing competence).

The three failure modes:
1. **Everything in static context** → context window overflow, wasted tokens
2. **Everything in stage outputs only** → agent must re-read thousands of lines
3. **Duplicated across locations** → two sources of truth that drift apart

---

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_three_tier_architecture](./need_01_three_tier_architecture/) | "What goes in each tier?" | Define pointer → distilled → full content pattern |
| [need_02_knowledge_graph](./need_02_knowledge_graph/) | "How are entities connected?" | Formalize relationships as JSON-LD graph |
| [need_03_reference_format](./need_03_reference_format/) | "How do tiers reference each other?" | Standard format for cross-tier links |

---

## Key Insight

Organization follows the brain's consolidation pattern: raw episodic memories (stage outputs) are distilled into semantic knowledge (.0agnostic/knowledge/), with navigation pointers (0AGNOSTIC.md) on top. Each tier serves a different access pattern — always-loaded, on-demand understanding, or on-demand detail.
