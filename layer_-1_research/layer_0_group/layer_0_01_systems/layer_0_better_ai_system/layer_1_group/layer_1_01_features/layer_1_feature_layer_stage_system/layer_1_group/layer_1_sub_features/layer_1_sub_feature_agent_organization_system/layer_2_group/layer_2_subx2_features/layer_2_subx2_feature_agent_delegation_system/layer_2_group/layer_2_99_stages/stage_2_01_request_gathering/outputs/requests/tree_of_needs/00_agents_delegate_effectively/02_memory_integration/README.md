---
resource_id: "f2481005-62a5-4f9d-a2c2-d54155129b0c"
resource_type: "readme
output"
resource_name: "README"
---
# Branch: Memory Integration

**Parent**: [00_agents_delegate_effectively](../)

---

<!-- section_id: "e645c9c9-de0a-401d-ab39-e123f7830faf" -->
## Core Question

> "How does what agents remember support delegation?"

---

<!-- section_id: "23941e7c-476a-44e9-b72b-e6ad454d6dea" -->
## Description

Delegation depends on context availability. A manager cannot delegate effectively if it does not know what state a stage is in. A stage agent cannot do its work if it cannot access domain knowledge. Memory -- in the form of context chains, handoff protocols, and tiered knowledge -- is the infrastructure that makes delegation possible.

The three failure modes without memory integration:
1. **Context amnesia** -- agents start fresh every session, re-discovering what has been done
2. **Context loss at transitions** -- handoffs between agents lose critical information
3. **Wrong detail level** -- managers load full details when they need summaries, or agents get only pointers when they need substance

---

<!-- section_id: "6177859c-6bc5-4877-9ef8-c1ed612ac0c4" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_context_chain_support](./need_01_context_chain_support/) | "How do context chains enable delegation decisions?" | Context loading informs what to delegate and to whom |
| [need_02_handoff_protocols](./need_02_handoff_protocols/) | "How is context preserved across agent transitions?" | Session-to-session and agent-to-agent context transfer |
| [need_03_three_tier_delegation](./need_03_three_tier_delegation/) | "How does the three-tier pattern apply to delegation context?" | Pointers for managers, distilled for stage agents, full in stage outputs |

---

<!-- section_id: "d04c7f26-d152-4209-8c14-7f02c0c50d1b" -->
## Key Insight

Memory integration is not just about persistence -- it is about the right information reaching the right agent at the right time. The delegation model defines who does what; memory integration defines what each agent knows when it starts working. These two branches are tightly coupled: delegation decisions depend on memory, and memory structure serves delegation.
