# Need: Scored Context Retrieval — User Stories

---

### US-1: Agent loads most relevant context on entry
**As an** agent entering the memory_system entity,
**I want** the system to rank available knowledge files by relevance to my task,
**So that** I read the most useful files first and skip irrelevant ones.

**Acceptance**: Agent receives ranked list, top files are demonstrably relevant.

---

### US-2: Agent prioritizes recent over stale
**As an** agent working on an active design task,
**I want** recently updated files to score higher than old ones,
**So that** I work with current information, not outdated research.

**Acceptance**: Recency factor in scoring visibly affects ranking.

---

### US-3: Developer tunes scoring weights
**As the** developer,
**I want to** adjust the balance between recency, relevance, and importance,
**So that** different contexts (research vs active development) prioritize differently.

**Acceptance**: Weights are configurable, not hardcoded.
