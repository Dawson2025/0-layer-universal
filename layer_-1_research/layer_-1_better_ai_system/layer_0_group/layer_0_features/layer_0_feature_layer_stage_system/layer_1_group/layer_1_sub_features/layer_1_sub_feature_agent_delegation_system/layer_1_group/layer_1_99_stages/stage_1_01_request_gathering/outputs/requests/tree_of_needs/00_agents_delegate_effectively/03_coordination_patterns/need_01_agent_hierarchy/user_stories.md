# Need: Agent Hierarchy -- User Stories

## Actors

- **Entity Manager**: AI agent managing an entity (e.g., context_chain_system manager)
- **Stage Agent**: AI agent working within a specific stage
- **Child Manager**: AI agent managing a child entity
- **Developer**: Human maintaining the system (Dawson)

---

### US-1: Entity manager knows its direct reports

**As an** entity manager,
**I want** my 0AGNOSTIC.md to list my stages and my child entities,
**So that** I know exactly which agents I manage and can delegate to.

**Acceptance**: Manager's 0AGNOSTIC.md contains a children table and a stage overview table.

---

### US-2: Stage agent knows its manager

**As a** stage agent spawned to work on design,
**I want** my 0AGNOSTIC.md to reference my parent entity manager,
**So that** I know who to escalate to when I encounter something outside my scope.

**Acceptance**: Stage agent's 0AGNOSTIC.md includes a parent pointer to the entity manager.

---

### US-3: Child manager escalates to parent

**As a** child entity manager that encounters a cross-entity decision,
**I want** a clear escalation path to my parent entity manager,
**So that** the decision is made at the right level of the hierarchy.

**Acceptance**: Escalation path is documented and follows the entity tree upward.

---

### US-4: Developer visualizes the agent tree

**As the** developer reviewing the system,
**I want to** see the full agent hierarchy as a tree (which managers manage which agents),
**So that** I can verify the structure is correct and identify gaps.

**Acceptance**: Hierarchy can be derived from 0AGNOSTIC.md parent/children fields across all entities.

---
