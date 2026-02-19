# Need: Context Chain Support

**Branch**: [02_memory_integration](../)
**Question**: "How do context chains enable delegation decisions?"
**Version**: 1.0.0

---

## Definition

Context chains -- the automatic loading of context from root to current entity through the hierarchy -- provide the foundation for delegation. A manager's context chain gives it the identity and status information needed to decide what to delegate. A stage agent's context chain gives it the domain understanding needed to do its work.

---

## Why This Matters

- Without context chains, agents must manually discover and load every file they need
- Manual loading is error-prone: agents miss files, load the wrong ones, or load too many
- Context chains ensure that hierarchy-level context (parent identity, grandparent scope) is always available
- Delegation decisions require knowing where you are in the hierarchy -- context chains provide this

---

## Requirements

### Chain Loading for Delegation
- MUST define which context chain entries are relevant for delegation decisions (entity identity, children list, stage status)
- MUST ensure the manager's context chain includes enough information to decide "which stage needs work?"
- MUST ensure the stage agent's context chain includes the parent entity's identity and scope
- MUST NOT load the full parent knowledge directory automatically -- only pointers and triggers

### Chain Depth for Agent Types
- MUST define the appropriate chain depth for each agent type (how far up the hierarchy to load)
- SHOULD limit manager chain depth to: self + parent + grandparent (3 levels)
- SHOULD limit stage agent chain depth to: self + parent entity (2 levels)
- MUST NOT load the entire chain from root to leaf for every agent -- only what is needed

### Chain Content Filtering
- MUST define what content from each chain level is loaded (identity only? identity + triggers? full 0AGNOSTIC.md?)
- SHOULD load progressively less detail at each parent level (self: full, parent: identity + triggers, grandparent: identity only)
- MUST NOT load sibling entities through the chain (only direct ancestors)

---

## Acceptance Criteria

- [ ] Context chain loading rules are defined per agent type
- [ ] Manager's chain provides sufficient info for delegation decisions
- [ ] Stage agent's chain provides parent entity context without overloading
- [ ] Chain depth is limited and documented per agent type
- [ ] Content filtering is defined per chain level

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Context chain system research: chain architecture, static vs dynamic context
- Context chain system tree of needs: `00_context_survives_boundaries/03_knowledge_retrieval/`
