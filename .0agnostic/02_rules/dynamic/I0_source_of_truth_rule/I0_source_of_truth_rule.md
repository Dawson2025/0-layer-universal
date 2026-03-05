---
resource_id: "e4855ae3-a609-4e47-bfb0-1cf35995da0d"
resource_type: "rule"
resource_name: "I0_source_of_truth_rule"
---
# Source of Truth Rule

**Type**: Dynamic (loaded when triggered)
**Importance**: 0 (highest — must be loaded when triggered, no exceptions)
**Scope**: All agents at all levels

<!-- section_id: "dee226b9-4f2b-46e4-abf7-236d4590cdc8" -->
## Rule

When the user asks where the source of truth for something is, or asks to see the context chain for a given thing, the agent MUST:

1. **Load** the Source of Truth Protocol at `.0agnostic/03_protocols/source_of_truth_protocol.md`
2. **Execute** the protocol completely — all 3 tiers
3. **Show** the full response to the user

No partial responses. No skipping tiers. The protocol defines a 3-tier trace:
- **Tier 1**: Canonical source (the specific detailed file/directory)
- **Tier 2**: 0AGNOSTIC.md reference (how it's pointed to)
- **Tier 3**: Propagation chain (how it reaches agents via the avenue web)

<!-- section_id: "3a1017ab-85d7-4fb1-abdc-b41e6eef8934" -->
## Trigger Conditions

This rule activates when the user:
- Asks "where is the source of truth for X?"
- Asks "show the context chain for X"
- Asks "show me the context chain strain for X"
- Asks "how does X get into context?"
- Asks "where does X propagate?" or "what references X?"
- Uses `/source-of-truth` or similar command
- Asks "where is X defined?" (when X is a system concept, rule, or artifact)

<!-- section_id: "f4a0e40c-fbfa-493c-8b61-c1bcb7ffb0b6" -->
## Importance Ranking

Rules use an importance ranking where **0 is most important** and importance increases numerically as priority decreases.

| Importance | Meaning | Behavior |
|------------|---------|----------|
| 0 | Critical | MUST be loaded and executed when triggered — no exceptions |
| 1 | High | Should be loaded when triggered — can defer if context-constrained |
| 2 | Standard | Load when relevant — normal dynamic rule behavior |
| 3+ | Advisory | Guidance that can be skipped under tight context budgets |

<!-- section_id: "51c0526b-58a6-49c6-9530-9f8b3524c9cb" -->
## Rationale

The source of truth is the foundation of the agnostic system. If an agent cannot trace where authoritative content lives and how it propagates, it cannot reliably modify or extend the system. This rule ensures the trace is always complete and structured.

<!-- section_id: "3e8ab143-270a-409e-9062-6adfba747a93" -->
## Related

- **Protocol**: `../03_protocols/source_of_truth_protocol.md`
- **Avenue Web**: `.../context_chain_system/.0agnostic/01_knowledge/avenue_web_architecture.md`
