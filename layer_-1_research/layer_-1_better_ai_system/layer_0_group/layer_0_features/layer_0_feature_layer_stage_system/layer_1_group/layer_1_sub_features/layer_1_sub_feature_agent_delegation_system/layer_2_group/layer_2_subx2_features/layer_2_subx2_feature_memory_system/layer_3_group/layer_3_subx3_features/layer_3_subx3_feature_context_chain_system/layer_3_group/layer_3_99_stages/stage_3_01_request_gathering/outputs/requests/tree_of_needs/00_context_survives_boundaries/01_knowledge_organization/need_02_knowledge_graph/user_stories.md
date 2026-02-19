# Need: Knowledge Graph — User Stories

## Actors

- **Agent**: AI agent working in the layer-stage system
- **Developer**: Human maintaining the system
- **Script**: Automated tool (graph generator)

---

### US-1: Agent discovers related entities
**As an** agent entering a new entity,
**I want to** read the knowledge graph and see what entities are connected,
**So that** I load relevant sibling/parent context without guessing.

**Acceptance**: Agent reads graph, identifies parent + children + cross-references in one query.

---

### US-2: Agent finds shortest context path
**As an** agent needing context from a distant entity,
**I want to** traverse the graph to find the most direct path,
**So that** I load minimum context rather than walking the entire tree.

**Acceptance**: Graph traversal returns typed path between any two entities.

---

### US-3: Script regenerates graph after changes
**As the** developer who just created a new entity,
**I want** the graph to regenerate automatically,
**So that** the new entity appears in the graph without manual editing.

**Acceptance**: Script parses all 0AGNOSTIC.md files and outputs valid JSON-LD. Idempotent.

---

### US-4: Developer validates chain integrity
**As the** developer,
**I want to** run chain-validate and get a report comparing graph vs file system,
**So that** I fix broken references before agents encounter them.

**Acceptance**: Reports orphaned nodes, missing nodes, broken edges.
