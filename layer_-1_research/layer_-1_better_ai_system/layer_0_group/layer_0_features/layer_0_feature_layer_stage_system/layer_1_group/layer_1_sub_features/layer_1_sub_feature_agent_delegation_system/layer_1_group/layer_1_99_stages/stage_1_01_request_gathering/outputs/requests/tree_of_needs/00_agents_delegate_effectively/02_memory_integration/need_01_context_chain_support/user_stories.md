# Need: Context Chain Support -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Context Chain**: The automatic loading mechanism that traverses the hierarchy

---

### US-1: Manager receives hierarchy context automatically

**As a** manager entering an entity directory,
**I want** the context chain to automatically load my identity, my children, and my parent's scope,
**So that** I know where I am in the hierarchy and can make delegation decisions immediately.

**Acceptance**: Manager's static context includes self identity, children list, and parent scope without manual file reads.

---

### US-2: Stage agent receives parent domain context

**As a** stage agent spawned to work on research,
**I want** my context chain to include the parent entity's identity and pointers to domain knowledge,
**So that** I can load the right knowledge file on demand without guessing which file to read.

**Acceptance**: Stage agent's chain includes parent 0AGNOSTIC.md pointers, not full knowledge content.

---

### US-3: Chain stops at the right depth

**As a** stage agent deep in the hierarchy,
**I want** the context chain to load only my stage and my parent entity (not every ancestor up to root),
**So that** my context window is not consumed by irrelevant ancestor context.

**Acceptance**: Stage agent's chain is limited to 2 levels (self + parent entity).

---

### US-4: Chain loads identity, not detail

**As a** manager whose context chain includes grandparent context,
**I want** the grandparent level to include only its identity and scope (not its full 0AGNOSTIC.md),
**So that** I get orientation without wasting tokens on irrelevant detail.

**Acceptance**: Each ancestor level loads progressively less content.

---
