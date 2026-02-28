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

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Context chain loading rules are defined per agent type
- [ ] Manager's chain provides sufficient info for delegation decisions
- [ ] Stage agent's chain provides parent entity context without overloading
- [ ] Chain depth is limited and documented per agent type
- [ ] Content filtering is defined per chain level

---

## Research References

- Context chain system research: chain architecture, static vs dynamic context
- Context chain system tree of needs: `00_context_survives_boundaries/03_knowledge_retrieval/`
