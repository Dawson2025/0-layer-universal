# Source of Truth Rule

**Type**: Dynamic (loaded when triggered)
**Importance**: 0 (highest — must be loaded when triggered, no exceptions)
**Scope**: All agents at all levels

## Rule

When the user asks where the source of truth for something is, or asks to see the context chain for a given thing, the agent MUST:

1. **Load** the Source of Truth Protocol at `layer_0/.0agnostic/03_protocols/source_of_truth_protocol.md`
2. **Execute** the protocol completely — all 3 tiers
3. **Show** the full response to the user

No partial responses. No skipping tiers. The protocol defines a 3-tier trace:
- **Tier 1**: Canonical source (the specific detailed file/directory)
- **Tier 2**: 0AGNOSTIC.md reference (how it's pointed to)
- **Tier 3**: Propagation chain (how it reaches agents via the avenue web)

## Trigger Conditions

This rule activates when the user:
- Asks "where is the source of truth for X?"
- Asks "show the context chain for X"
- Asks "how does X get into context?"
- Uses `/source-of-truth` or similar command
- Asks "where is X defined?" (when X is a system concept, rule, or artifact)

## Importance Ranking

Rules use an importance ranking where **0 is most important** and importance increases numerically as priority decreases.

| Importance | Meaning | Behavior |
|------------|---------|----------|
| 0 | Critical | MUST be loaded and executed when triggered — no exceptions |
| 1 | High | Should be loaded when triggered — can defer if context-constrained |
| 2 | Standard | Load when relevant — normal dynamic rule behavior |
| 3+ | Advisory | Guidance that can be skipped under tight context budgets |

## Rationale

The source of truth is the foundation of the agnostic system. If an agent cannot trace where authoritative content lives and how it propagates, it cannot reliably modify or extend the system. This rule ensures the trace is always complete and structured.

## Related

- **Protocol**: `../03_protocols/source_of_truth_protocol.md`
- **Avenue Web**: `.../context_chain_system/.0agnostic/01_knowledge/avenue_web_architecture.md`
