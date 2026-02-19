# Need: Agent Context Model -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Sub-Feature Agent**: AI agent managing a child entity within the hierarchy
- **Developer**: Human maintaining the system (Dawson)

---

### US-1: Manager loads only what it needs

**As a** manager starting a new session,
**I want** my static context to contain only my identity, stage overview, and children list,
**So that** my context window has room for coordination work rather than being filled with stage details.

**Acceptance**: Manager's static context is under 200 lines and contains zero stage methodology.

---

### US-2: Stage agent loads domain knowledge on demand

**As a** stage agent that needs to understand a domain concept,
**I want to** know exactly which knowledge file to read from the parent entity's `.0agnostic/knowledge/`,
**So that** I load one targeted file instead of the entire knowledge directory.

**Acceptance**: Stage agent reads at most 1-2 knowledge files per task, guided by its 0AGNOSTIC.md.

---

### US-3: Sub-feature agent sees its own tree

**As a** sub-feature agent managing a child entity,
**I want** my context model to include my entity identity and my own stages, but not my sibling entities' internals,
**So that** I stay focused on my scope without being distracted by unrelated context.

**Acceptance**: Sub-feature agent's context excludes all sibling entity details.

---

### US-4: Developer can audit context boundaries

**As the** developer reviewing the system,
**I want** a documented context model for each agent type showing exactly what goes in static, dynamic, and never-loaded,
**So that** I can verify agents are operating within their intended scope.

**Acceptance**: Context model document exists with three columns (static / dynamic / never) for each agent type.

---
