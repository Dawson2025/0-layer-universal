---
resource_id: "86d8bc4b-cf9c-4d97-ba84-87328b157de1"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Context Chain Support

**Branch**: [02_memory_integration](../)
**Question**: "How do context chains enable delegation decisions?"
**Version**: 1.0.0

---

<!-- section_id: "dc08234b-10ea-450a-a490-78186f9ba38d" -->
## Definition

Context chains -- the automatic loading of context from root to current entity through the hierarchy -- provide the foundation for delegation. A manager's context chain gives it the identity and status information needed to decide what to delegate. A stage agent's context chain gives it the domain understanding needed to do its work.

---

<!-- section_id: "86e261fb-8bc3-4480-900c-34a39c06cae0" -->
## Why This Matters

- Without context chains, agents must manually discover and load every file they need
- Manual loading is error-prone: agents miss files, load the wrong ones, or load too many
- Context chains ensure that hierarchy-level context (parent identity, grandparent scope) is always available
- Delegation decisions require knowing where you are in the hierarchy -- context chains provide this

---

<!-- section_id: "3bb63e15-965a-448e-951c-68395887982b" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "c1649f9e-5e20-44df-bf27-1417e976aef8" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "fa7d5831-f8bb-42f8-9536-137bdd7f4cc3" -->
## Acceptance Criteria

- [ ] Context chain loading rules are defined per agent type
- [ ] Manager's chain provides sufficient info for delegation decisions
- [ ] Stage agent's chain provides parent entity context without overloading
- [ ] Chain depth is limited and documented per agent type
- [ ] Content filtering is defined per chain level

---

<!-- section_id: "e44ad023-0f4b-46a4-bf54-8cdba83fd940" -->
## Research References

- Context chain system research: chain architecture, static vs dynamic context
- Context chain system tree of needs: `00_context_survives_boundaries/03_knowledge_retrieval/`
