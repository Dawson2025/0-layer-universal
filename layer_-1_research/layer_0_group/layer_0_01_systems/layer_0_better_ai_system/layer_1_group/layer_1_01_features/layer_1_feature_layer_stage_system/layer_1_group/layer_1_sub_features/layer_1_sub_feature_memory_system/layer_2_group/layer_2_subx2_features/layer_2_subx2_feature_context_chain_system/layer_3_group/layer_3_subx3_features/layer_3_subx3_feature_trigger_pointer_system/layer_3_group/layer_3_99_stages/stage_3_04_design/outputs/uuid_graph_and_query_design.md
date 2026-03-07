---
resource_id: "f8a2b4c6-d0e1-4f3a-5b7c-9d1e3f5a7b8c"
resource_type: "output"
resource_name: "uuid_graph_and_query_design"
---
# Design: UUID Graph Traversal & Query CLI

<!-- section_id: "a1b3c5d7-e9f0-4a2b-6c8d-0e2f4a6b8c9d" -->
## Status: IMPLEMENTED
<!-- section_id: "b2c4d6e8-f0a1-4b3c-7d9e-1f3a5b7c9d0e" -->
## Date: 2026-03-06
<!-- section_id: "c3d5e7f9-a0b1-4c2d-8e0f-2a4b6c8d0e1f" -->
## Author: AI Agent (stage_3_04_design)
<!-- section_id: "d4e6f8a0-b1c2-4d3e-9f0a-3b5c7d9e1f2a" -->
## Related Design: `uuid_identity_system_design.md` (Sections 4, 12)

---

<!-- section_id: "e5f7a9b1-c2d3-4e4f-0a1b-4c6d8e0f2a3b" -->
## 1. Problem Statement

The UUID identity system (design doc Sections 1-14) established UUIDs for entities, stages, and resources with a flat index for lookup. However, agents need to:

1. **Navigate hierarchy**: Given an entity, find its parent and children without reading 0AGNOSTIC.md files
2. **Query flexibly**: Filter the index by type, name pattern, resource type, parent, path — like a database SELECT
3. **Access resource catalogs**: Find all resources within an entity without scanning the filesystem

These capabilities transform the UUID index from a simple key-value store into a filesystem-backed document database (design doc Section 12).

---

<!-- section_id: "f6a8b0c2-d3e4-4f5a-1b2c-5d7e9f1a3b4c" -->
## 2. Parent/Children Graph Design

<!-- section_id: "a7b9c1d3-e4f5-4a6b-2c3d-6e8f0a2b4c5d" -->
### 2.1 Data Source

Parent references are extracted from `**Parent**: \`../path/0AGNOSTIC.md\`` lines in each entity's 0AGNOSTIC.md Identity section. This is already the canonical parent declaration — no new data source needed.

<!-- section_id: "b8c0d2e4-f5a6-4b7c-3d4e-7f9a1b3c5d6e" -->
### 2.2 Resolution Algorithm

```
For each entity with 0AGNOSTIC.md:
  1. Read first 8KB of file
  2. Search for pattern: **Parent**: `<relative_path>`
  3. Resolve relative path from entity directory to get absolute parent path
  4. Read parent's 0AGNOSTIC.md, extract entity_id
  5. Store: entity.parent_id = parent.entity_id
  6. After all entities processed, invert to compute children[]:
     For each entity with parent_id:
       parent.children.append(entity.entity_id)
```

<!-- section_id: "c9d1e3f5-a6b7-4c8d-4e5f-8a0b2c4d6e7f" -->
### 2.3 Index Schema Extension

Entity entries in `.uuid-index.json` gain two new fields:

```json
{
  "a79b61a7-...": {
    "type": "entity",
    "name": "layer_2_subx2_feature_context_chain_system",
    "path": "layer_-1_research/.../layer_2_subx2_feature_context_chain_system",
    "parent_id": "f62dcffc-...",
    "children": ["5d5be68b-...", "7a74444f-...", "ae555d77-..."]
  }
}
```

- `parent_id`: UUID of the parent entity, or absent/null for root entities
- `children`: Array of child entity UUIDs (computed, not stored in source files)

<!-- section_id: "d0e2f4a6-b7c8-4d9e-5f6a-9b1c3d5e7f8a" -->
### 2.4 Edge Cases

| Scenario | Handling |
|----------|----------|
| Entity has no `**Parent**:` reference | No `parent_id` field (true root) |
| Parent path doesn't resolve to existing file | Warning to stderr, no `parent_id` (61 cases) |
| Parent file exists but has no `entity_id` | Warning, no `parent_id` (154 cases) |
| Circular parent references | Would create cycles — detected by --parent --verbose chain walk |
| Multiple `**Parent**:` lines | First match used |

<!-- section_id: "e1f3a5b7-c8d9-4e0f-6a7b-0c2d4e6f8a9b" -->
### 2.5 Statistics (Current)

| Metric | Count |
|--------|-------|
| Total entities | 351 |
| Entities with resolved parent_id | 122 |
| Entities with children | 34 |
| Root entities (no parent) | 229 |
| Roots with fixable parent refs | 215 (parent exists but lacks entity_id or path is wrong) |
| True roots | 14 (layer_-1_research, layer_0, layer_1, etc.) |

---

<!-- section_id: "f2a4b6c8-d9e0-4f1a-7b8c-1d3e5f7a9b0c" -->
## 3. Query CLI Design

<!-- section_id: "a3b5c7d9-e0f1-4a2b-8c9d-2e4f6a8b0c1d" -->
### 3.1 Interface

```bash
pointer-sync.sh --query [key=value ...]
```

Multiple key=value pairs are AND-combined. Values support fnmatch glob patterns.

<!-- section_id: "b4c6d8e0-f1a2-4b3c-9d0e-3f5a7b9c1d2e" -->
### 3.2 Supported Filter Keys

| Key | Applies To | Example | Description |
|-----|-----------|---------|-------------|
| `type` | All entries | `type=entity` | Filter by entry type (entity, stage, resource) |
| `name` | All entries | `name=*research*` | Glob match on entry name |
| `path` | All entries | `path=*layer_1*` | Glob match on entry path |
| `resource_type` | Resources | `resource_type=script` | Filter resources by type |
| `entity_id` | Stages, Resources | `entity_id=a79b...` | Find entries belonging to an entity |
| `parent_id` | Entities | `parent_id=f62d...` | Find children of a specific parent |
| `has_children` | Entities | `has_children=true` | Find entities that have/lack children |

<!-- section_id: "c5d7e9f1-a2b3-4c4d-0e1f-4a6b8c0d2e3f" -->
### 3.3 Implementation

The query engine is implemented as an embedded Python script that:
1. Loads `.uuid-index.json` (O(1) file read, ~3ms for 2.6MB)
2. Parses key=value pairs from arguments
3. Iterates all entries, applying `fnmatch.fnmatch()` for glob patterns
4. Prints matching entries as formatted table

Performance: <100ms for full scan of 5,313 entries.

<!-- section_id: "d6e8f0a2-b3c4-4d5e-1f2a-5b7c9d1e3f4a" -->
### 3.4 Output Format

```
UUID                                  TYPE      NAME                    PATH
a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9  entity    layer_2_subx2...        layer_-1_research/...
5d5be68b-1234-4abc-9def-567890abcdef  entity    layer_3_subx3...        layer_-1_research/...
```

---

<!-- section_id: "e7f9a1b3-c4d5-4e6f-2a3b-6c8d0e2f4a5b" -->
## 4. Per-Entity Resource Indexes

<!-- section_id: "f8a0b2c4-d5e6-4f7a-3b4c-7d9e1f3a5b6c" -->
### 4.1 Purpose

Resource indexes enable agents to discover all UUID-bearing files within an entity without filesystem scanning. They sit at `.0agnostic/resource_index.json` and serve as the entity-local component of the three-tier index architecture (local → root).

<!-- section_id: "a9b1c3d5-e6f7-4a8b-4c5d-8e0f2a4b6c7d" -->
### 4.2 Schema

```json
{
  "file_id": "uuid-of-this-index-file",
  "generated": "2026-03-06T10:30:00Z",
  "entity_id": "parent-entity-uuid",
  "entity_name": "entity_directory_name",
  "entity_path": "relative/path/from/repo/root",
  "resources": [
    {
      "resource_id": "uuid-of-resource",
      "id_field": "resource_id|file_id",
      "resource_type": "knowledge|rule|protocol|script|data|output|...",
      "resource_name": "human_readable_name",
      "path": "relative/path/from/entity/root"
    }
  ]
}
```

<!-- section_id: "b0c2d4e6-f7a8-4b9c-5d6e-9f1a3b5c7d8e" -->
### 4.3 Generation

`create-resource-indexes.sh` generates indexes by:
1. Discovering entities (directories with both `0AGNOSTIC.md` and `.0agnostic/`)
2. Using `git ls-files` to find tracked files within each entity
3. Reading file headers (first 8KB) for UUID fields
4. Excluding derived files (CLAUDE.md, .integration.md, etc.)
5. Inferring resource types from paths and explicit fields
6. Writing atomic JSON output

<!-- section_id: "c1d3e5f7-a8b9-4c0d-6e7f-0a2b4c6d8e9f" -->
### 4.4 Aggregation into Root Index

The root `build_uuid_index()` function (Phase 3 of the rebuild process) reads all `resource_index.json` files and aggregates their entries into `.uuid-index.json`. Duplicate UUIDs (from overlapping git ls-files scopes) are deduplicated with first-seen-wins.

---

<!-- section_id: "d2e4f6a8-b9c0-4d1e-7f8a-1b3c5d7e9f0a" -->
## 5. Architectural Context

This design extends the UUID identity system design (Sections 4 and 12) by adding:

| Concept | Document DB Parallel | Implementation |
|---------|---------------------|----------------|
| Parent/children graph | Document references + denormalized children | `parent_id` + `children[]` in index |
| Query CLI | Collection query with filters | `--query` with fnmatch patterns |
| Resource indexes | Per-document embedded indexes | `.0agnostic/resource_index.json` |
| Three-phase rebuild | Index aggregation pipeline | entities → stages → resources |

The system now supports all four primary database operations:
- **Create**: `uuidgen` + insert into frontmatter/header
- **Read**: `--lookup`, `--parent`, `--children`, `--query`
- **Update**: Edit source files, `--rebuild-index` to refresh
- **Delete**: Remove files, `--gc` to clean index (via design doc Section 13)

---

<!-- section_id: "a1c3e5f7-b2d4-4a6b-8c0d-2e4f6a8b0c1d" -->
## 6. Agent Interaction Layer Design (2026-03-06)

The question of **how agents interact** with the UUID index system is as important as the system itself. This section designs the agent-facing interface based on industry research.

<!-- section_id: "b2d4f6a8-c3e5-4b7c-9d1e-3f5a7b9c1d2e" -->
### 6.1 Design Decision: Bash + Skills Over SQL or Custom Tools

**Decision**: Agents interact with the UUID system through bash commands (pointer-sync.sh CLI, jq on JSON) guided by Claude Code skills. No SQL database or custom MCP tools.

**Rationale** (from research Section 8):

| Alternative | Why Not |
|-------------|---------|
| SQL (SQLite/PostgreSQL) | Text-to-SQL has 5-10% error rates. Requires schema learning. Adds infrastructure. Agents already know bash. |
| Custom MCP tools | Each tool costs 500+ tokens in tool descriptions. Increases tool selection confusion. Black-box debugging. |
| Direct file manipulation | Too low-level. No query abstraction. Error-prone for complex lookups. |

**Why bash + skills wins**:
1. **Zero prompt overhead** — no tool descriptions needed; bash is pretrained
2. **Skill loads on-demand** — zero tokens until `/uuid-query` is invoked
3. **Familiar interface** — agents have internalized grep, jq, CLI patterns from training
4. **Transparent debugging** — every command is visible and reproducible
5. **Graceful degradation** — without the skill, agents can still `grep` the raw JSON

<!-- section_id: "c3e5a7b9-d4f6-4c8d-0e2f-4a6b8c0d2e3f" -->
### 6.2 Skill Interface Design: `/uuid-query`

The recommended Claude Code skill would provide:

```
/uuid-query — Query and navigate the UUID identity system

WHEN TO USE:
- Finding entities, stages, or resources by UUID, name, or pattern
- Navigating parent/children hierarchy
- Discovering resources within an entity
- Checking pointer integrity

COMMANDS:
  # Lookup by UUID or name
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --lookup <uuid-or-name>

  # Navigate hierarchy
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid>            # Direct parent
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid> --verbose   # Full chain to root
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --children <uuid>           # Direct children

  # Query with filters (AND-combined, glob patterns)
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=entity name=*research*
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=resource resource_type=script
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query parent_id=<uuid>
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query has_children=true

  # Find references to a UUID
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --find-references <uuid>

  # Direct jq queries for advanced use
  jq '.[] | select(.type=="entity" and (.name | test("memory")))' .uuid-index.json

  # Per-entity resource catalog
  jq '.resources[] | select(.resource_type=="knowledge")' <entity>/.0agnostic/resource_index.json

WHEN NOT TO USE:
- Simple file reads (use Read tool directly)
- Creating new entities (use /entity-creation skill)
- Modifying pointer files (use pointer-sync.sh --sync)
```

<!-- section_id: "d4f6b8c0-e5a7-4d9e-1f3a-5b7c9d1e3f4a" -->
### 6.3 Harness Engineering Alignment

This design follows the harness engineering framework (constrain/inform/verify/correct):

| Function | How the Skill Serves It |
|----------|------------------------|
| **Inform** | Skill teaches agents available commands and when to use each |
| **Constrain** | Commands have defined input/output contracts (not free-form) |
| **Verify** | `--validate` checks integrity; agents can self-verify results |
| **Correct** | `--sync` auto-fixes stale paths; `--rebuild-index` recovers from corruption |

The skill is part of the agent harness, not a standalone tool. It makes agents more capable by teaching them patterns they already understand.

---

<!-- section_id: "e5a7c9d1-f6b8-4e0f-2a4b-6c8d0e2f4a5b" -->
## 7. Concurrency Architecture: Future Database Backend (2026-03-06)

<!-- section_id: "f6b8d0e2-a7c9-4f1a-3b5c-7d9e1f3a5b6c" -->
### 7.1 The Virtual Filesystem Pattern

When concurrency demands exceed file-locking capabilities, the architecture supports upgrading the **storage backend** without changing the **agent interface**:

```
Current:  Agent → pointer-sync.sh → jq → .uuid-index.json (JSON file)
Future:   Agent → pointer-sync.sh → sqlite3 → .uuid-index.db (SQLite file)
```

The agent still runs the same bash commands. The script internally switches from `jq` to `sqlite3`. This is the "virtual filesystem" pattern validated by Vercel, Letta, and LangSmith in production.

<!-- section_id: "a7c9e1f3-b8d0-4a2b-4c6d-8e0f2a4b6c7d" -->
### 7.2 SQLite Migration Design

| Component | Current (JSON) | Future (SQLite) |
|-----------|---------------|-----------------|
| Storage format | `.uuid-index.json` (2.6MB) | `.uuid-index.db` (~1MB, B-tree indexed) |
| Read concurrency | Unlimited (file reads) | Unlimited (WAL mode) |
| Write concurrency | One at a time (mkdir lock) | One writer + many readers (WAL mode) |
| Query engine | `jq` + `fnmatch` in Python | SQL with `json_extract()`, `LIKE`, `GLOB` |
| Index rebuild | Full JSON rewrite | `INSERT OR REPLACE` per entry |
| Full-text search | Not supported | FTS5 on name, path columns |
| Lookup time | <0.03ms (in-memory after load) | <0.01ms (B-tree index) |
| CLI compatibility | `pointer-sync.sh --query` | Same CLI, different backend |

<!-- section_id: "b8d0f2a4-c9e1-4b3c-5d7e-9f1a3b5c7d8e" -->
### 7.3 Schema Design (for future SQLite migration)

```sql
CREATE TABLE uuid_entries (
  uuid TEXT PRIMARY KEY,
  type TEXT NOT NULL,           -- 'entity', 'stage', 'resource'
  name TEXT NOT NULL,
  path TEXT NOT NULL,
  parent_id TEXT,               -- FK to uuid_entries.uuid (nullable)
  entity_id TEXT,               -- owning entity UUID (for stages/resources)
  resource_type TEXT,           -- 'knowledge', 'rule', 'script', etc.
  resource_name TEXT,
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_type ON uuid_entries(type);
CREATE INDEX idx_name ON uuid_entries(name);
CREATE INDEX idx_parent ON uuid_entries(parent_id);
CREATE INDEX idx_entity ON uuid_entries(entity_id);
CREATE INDEX idx_resource_type ON uuid_entries(resource_type);

-- Children are computed via parent_id (no separate table needed)
-- Full-text search for natural language queries
CREATE VIRTUAL TABLE uuid_fts USING fts5(name, path, resource_name, content=uuid_entries);
```

<!-- section_id: "c9e1a3b5-d0f2-4c4d-6e8f-0a2b4c6d8e9f" -->
### 7.4 Migration Trigger Conditions

Do NOT migrate until any one of:
- Index exceeds 50K entries (currently 5,313)
- 3+ agents regularly write concurrently
- Query latency exceeds 500ms (currently <100ms)
- Need atomic multi-entity operations
- Multi-machine concurrent access required

**Current assessment**: No migration needed. JSON approach is correct for current scale.

---

<!-- section_id: "d0e1f2a3-b4c5-4d6e-7f8a-9b0c1d2e3f4a" -->
## 8. Infrastructure Layer Design: Hybrid Knowledge Architecture (2026-03-06)

Building on the two-layer separation (interface vs infrastructure) from research Section 11, this section designs the infrastructure layer that sits behind our bash/skill interface.

<!-- section_id: "e1f2a3b4-c5d6-4e7f-8a9b-0c1d2e3f4a5b" -->
### 8.1 The Two-Layer Principle

**Interface layer** (Sections 6-7): Agent-facing. Bash + skills + virtual filesystem. NEVER changes.

**Infrastructure layer** (this section): Backend. Can use any combination of data stores. Chosen for **functionality** (what queries are possible), not agent performance (which is dominated by LLM computation at 87-99.9%).

<!-- section_id: "f2a3b4c5-d6e7-4f8a-9b0c-1d2e3f4a5b6c" -->
### 8.2 Hybrid Knowledge Store Design

The infrastructure layer supports four data representation types, each optimized for different query patterns:

| Data Store | What It Holds | Query Pattern | Technology |
|-----------|---------------|---------------|------------|
| **Structured store** | Entity metadata (UUID, type, path, parent, timestamps) | Exact match, range, full-text | SQLite + FTS5 |
| **Graph store** | Entity relationships (parent chains, siblings, resource ownership) | Traversal, path finding, pattern matching | JSON-LD @graph (AALang-compatible) or SQLite recursive CTEs |
| **Vector store** | Semantic embeddings of entity names, descriptions, resource content | Similarity search, semantic queries | sqlite-vec extension |
| **Temporal store** | Relationship history (when parent changed, when entity created/modified) | Historical queries, evolution tracking | SQLite with `valid_from`/`valid_to` columns |

All four stores live in a **single SQLite database file** (`.uuid-index.db`), using SQLite extensions for graph and vector operations. This preserves our single-file philosophy.

<!-- section_id: "a3b4c5d6-e7f8-4a9b-0c1d-2e3f4a5b6c7d" -->
### 8.3 Unified Query Router

The pointer-sync.sh query engine dispatches to the appropriate store(s) based on query type:

```
pointer-sync.sh --query "type=entity parent=abc-123"
  → Structured store (exact match on fields)

pointer-sync.sh --query "children of entity X recursively"
  → Graph store (recursive CTE traversal)

pointer-sync.sh --query "entities related to memory architecture"
  → Vector store (embed query, find nearest neighbors)
  → + Structured store (filter by type=entity)
  → Fusion: merge and re-rank results

pointer-sync.sh --query "parent history of entity X"
  → Temporal store (list parent changes over time)
```

The agent doesn't specify which store to use. The query router auto-detects based on:
- Named fields (type=, parent=) → structured
- Traversal keywords (children, ancestors, path) → graph
- Natural language / no field names → vector
- History keywords (history, when, changed) → temporal

<!-- section_id: "b4c5d6e7-f8a9-4b0c-1d2e-3f4a5b6c7d8e" -->
### 8.4 Extended Schema (Hybrid)

Building on the SQLite schema from Section 7.3:

```sql
-- Core structured store (same as Section 7.3)
CREATE TABLE uuid_entries (
  uuid TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  name TEXT NOT NULL,
  path TEXT NOT NULL,
  parent_id TEXT,
  entity_id TEXT,
  resource_type TEXT,
  resource_name TEXT,
  updated_at TEXT DEFAULT (datetime('now'))
);

-- Vector store (sqlite-vec extension)
CREATE VIRTUAL TABLE uuid_vectors USING vec0(
  uuid TEXT PRIMARY KEY,
  embedding FLOAT[384]    -- All-MiniLM-L6-v2 dimensions
);

-- Temporal store (relationship history)
CREATE TABLE uuid_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  uuid TEXT NOT NULL,
  field TEXT NOT NULL,        -- 'parent_id', 'path', 'name', etc.
  old_value TEXT,
  new_value TEXT,
  changed_at TEXT DEFAULT (datetime('now')),
  FOREIGN KEY (uuid) REFERENCES uuid_entries(uuid)
);

-- Full-text search (already in Section 7.3)
CREATE VIRTUAL TABLE uuid_fts USING fts5(name, path, resource_name, content=uuid_entries);
```

<!-- section_id: "c5d6e7f8-a9b0-4c1d-2e3f-4a5b6c7d8e9f" -->
### 8.5 Migration Strategy

This hybrid architecture is an **additive extension** of the Section 7 SQLite design, not a replacement:

| Phase | What | When |
|-------|------|------|
| Current | JSON file with jq | Now (sufficient) |
| Phase 1 | SQLite with structured queries | When triggers from Section 7.4 hit |
| Phase 2 | + FTS5 for full-text search | With Phase 1 |
| Phase 3 | + sqlite-vec for semantic search | When natural language queries needed |
| Phase 4 | + temporal history table | When relationship evolution tracking needed |
| Phase 5 | + CRDT merge for multi-agent writes | When 3+ agents write concurrently |

Each phase is independent and backward-compatible. The CLI interface remains unchanged throughout.

---

<!-- section_id: "d6e7f8a9-b0c1-4d2e-3f4a-5b6c7d8e9f0a" -->
## 9. AALang/GAB Integration Architecture (2026-03-06)

AALang (Actor-based Agent Language) and its JSON-LD graph format offer a unique integration opportunity: our `.gab.jsonld` agent definitions are ALREADY knowledge graphs that describe entity relationships, constraints, and capabilities.

<!-- section_id: "e7f8a9b0-c1d2-4e3f-4a5b-6c7d8e9f0a1b" -->
### 9.1 How AALang JSON-LD Maps to Our Entity Graph

| Our Entity System | AALang Equivalent | Notes |
|-------------------|-------------------|-------|
| Entity (layer_N_feature_X) | `LLMAgent` or `Actor` node | Each entity has an agent definition |
| Parent-child relationship | `containedBy` / `contains` edges | Direct mapping |
| Entity stages (01-11) | `Mode` nodes | Stages = behavioral modes of the entity |
| Entity resources (.0agnostic/) | Actor `isolated_context` | Resources = actor's private state |
| Context chain (parent traversal) | Communication Layer 1 (actor-to-actor routing) | Chain = communication path |
| Cross-entity communication | Communication Layer 0 (gossip P2P) | Handoff documents = agent messages |
| Stage-specific rules | Mode `constraints` | Rules = mode constraints |

<!-- section_id: "f8a9b0c1-d2e3-4f4a-5b6c-7d8e9f0a1b2c" -->
### 9.2 AALang as Query Infrastructure

AALang's JSON-LD `@graph` arrays can be queried with standard tools:

```bash
# List all actors (entities) in a graph
jq '."@graph"[] | select(."@type" == "Actor") | {id: ."@id", purpose: .purpose}' system.gab.jsonld

# Find what communicates with what (edges)
jq '."@graph"[] | select(.canMessage) | {from: ."@id", to: .canMessage}' system.gab.jsonld

# Get mode constraints (traversal rules)
jq '."@graph"[] | select(."@type" == "Mode") | {mode: ."@id", constraints: .constraints}' system.gab.jsonld
```

This is already our recommended approach (see context_chain_system `0AGNOSTIC.md` Section "JSON-LD Navigation"). The UUID system would extend this by indexing `@id` values into the UUID graph, enabling cross-file graph traversal.

<!-- section_id: "a9b0c1d2-e3f4-4a5b-6c7d-8e9f0a1b2c3d" -->
### 9.3 Integration Points

| Integration | How | Benefit |
|------------|-----|---------|
| UUID ↔ @id mapping | Each entity's UUID maps to its `@id` in the JSON-LD graph | Cross-reference between UUID index and agent definitions |
| Skill ↔ Mode mapping | `/uuid-query` skill knows which modes (stages) are valid for queries | Stage-aware querying |
| pointer-sync.sh ↔ @graph | Index builder extracts relationships from `.gab.jsonld` `@graph` arrays | Automatic relationship discovery |
| MCP integration | AALang is MCP-ready; pointer-sync.sh could expose as MCP tool | Other agents can query our UUID system via MCP |
| A2A communication | AALang supports agent-to-agent gossip protocol | Multi-agent UUID system coordination |

<!-- section_id: "b0c1d2e3-f4a5-4b6c-7d8e-9f0a1b2c3d4e" -->
### 9.4 Future: System-Wide Knowledge Graph

The ultimate integration generates a **unified JSON-LD knowledge graph** of the entire entity hierarchy:

```jsonld
{
  "@context": {"@vocab": "https://layer-stage.dev/ontology/"},
  "@graph": [
    {
      "@id": "uuid:a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9",
      "@type": "Entity",
      "name": "context_chain_system",
      "layer": 2,
      "containedBy": {"@id": "uuid:f62dcffc-..."},
      "contains": [
        {"@id": "uuid:chain_viz_uuid"},
        {"@id": "uuid:context_loading_uuid"},
        {"@id": "uuid:trigger_pointer_uuid"}
      ],
      "stages": ["01_request_gathering", "02_research", ...],
      "resources": [...]
    },
    ...
  ]
}
```

This graph could be:
- Queried with SPARQL (W3C standard)
- Loaded into Neo4j or ArangoDB for graph algorithms
- Extended with vector embeddings for semantic queries
- Synced across machines via Merkle-DAG (SHIMI pattern)
- Used as AALang agent context (LLMs understand JSON-LD natively)

**Decision**: This is a future capability. Current implementation stays with structured JSON index. JSON-LD knowledge graph generation would be added as a `pointer-sync.sh --export-graph` command when graph traversal queries are needed beyond what recursive CTEs provide.

---

<!-- section_id: "a0b1c2d3-e4f5-4a6b-7c8d-9e0f1a2b3c4d" -->
## 10. Skill Context Avenue Design: `/uuid-query` (2026-03-06)

This section designs the context avenue architecture for exposing the UUID identity system to agents through the skill system. It connects to the interface design in Section 6.2 and the existing `.0agnostic/` resources (knowledge, rules, protocols) already created during development.

<!-- section_id: "b1c2d3e4-f5a6-4b7c-8d9e-0f1a2b3c4d5e" -->
### 10.1 Problem: Agents Don't Know the UUID System Exists

The UUID identity system has a CLI (`pointer-sync.sh`), documentation (knowledge, rules, protocols), and query capabilities (Sections 3-6). But agents only discover it if:
1. They happen to read a trigger in `0AGNOSTIC.md` that mentions pointer-sync
2. They stumble on `.0agnostic/01_knowledge/pointer_sync/`
3. A user explicitly tells them to use it

A **skill** solves this by making the UUID system discoverable through the standard skill-matching mechanism: agents check WHEN/WHEN NOT conditions against their current task. If a match, they load the skill and gain the full UUID query interface.

<!-- section_id: "c2d3e4f5-a6b7-4c8d-9e0f-1a2b3c4d5e6f" -->
### 10.2 Skill Architecture (Three Tiers)

The skill follows the established three-tier pattern from the context avenue web:

```
Tier 1: Canonical Skill Definition
  Location: .0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/
  Contents: SKILL.md + references/
  Purpose: Tool-agnostic source of truth for what the skill teaches

Tier 2: Tool-Specific Ports
  Location: .claude/skills/uuid-query/SKILL.md (Claude Code)
            .codex/skills/uuid-query/SKILL.md (Codex CLI, if supported)
  Purpose: Adapted for each tool's skill format and frontmatter
  Method: agnostic-sync.sh copies + adapts from canonical

Tier 3: Embedded References (in generated context files)
  Location: CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md
  Purpose: Agents without skill-loading capability still see trigger text
  Method: agnostic-sync.sh injects trigger + skill reference from 0AGNOSTIC.md
```

<!-- section_id: "d3e4f5a6-b7c8-4d9e-0f1a-2b3c4d5e6f7a" -->
### 10.3 Skill Content Design

The `/uuid-query` skill content is derived from the interface designed in Section 6.2:

```markdown
# /uuid-query — Query and navigate the UUID identity system

WHEN TO USE:
- You need entity metadata (UUID, type, path, parent, children)
- You need parent/child relationships between entities
- You need to find resources within a specific entity
- You need to look up an entity, stage, or resource by UUID
- You need to search for entities/resources by name pattern

WHEN NOT TO USE:
- Simple file reads where you already know the path (use Read tool)
- Creating new entities (use /entity-creation skill)
- Modifying pointer files (use pointer-sync.sh --sync)
- General file searching (use Glob/Grep tools)

COMMANDS:
  # Lookup by UUID
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --lookup <uuid>

  # Lookup by name (searches index for matching entries)
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query name=<exact-or-glob-pattern>

  # Navigate hierarchy
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid>            # Direct parent
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid> --verbose   # Full chain to root
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --children <uuid>           # Direct children

  # Query with filters (AND-combined, glob patterns supported)
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=entity
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=entity name=*research*
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=resource resource_type=script
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=resource entity_id=<uuid>
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query parent_id=<uuid>
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query has_children=true

  # Find all references to a UUID (reverse lookup)
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --find-references <uuid>

  # Validate system integrity
  .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --validate

  # Advanced: Direct jq on index
  jq '.[] | select(.type=="entity" and (.name | test("memory")))' .uuid-index.json

  # Per-entity resource catalog
  jq '.resources[]' <entity>/.0agnostic/resource_index.json

REFERENCES:
  Knowledge:  .0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md
  Rule:       .0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md
  Protocol:   .0agnostic/03_protocols/pointer_sync_protocol/pointer_sync_protocol.md
  Script:     .0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh
```

<!-- section_id: "e4f5a6b7-c8d9-4e0f-1a2b-3c4d5e6f7a8b" -->
### 10.4 Resource Dependencies

The skill references existing production resources — it does NOT create new knowledge, only makes existing knowledge discoverable:

| Resource Type | Already Exists | Path (root .0agnostic/) |
|--------------|----------------|------------------------|
| Knowledge | Yes | `01_knowledge/pointer_sync/pointer_sync_knowledge.md` |
| Rule (static) | Yes | `02_rules/static/pointer_sync_rule/pointer_sync_rule.md` |
| Protocol | Yes | `03_protocols/pointer_sync_protocol/pointer_sync_protocol.md` |
| Script | Yes | `pointer-sync.sh` |
| Skill (canonical) | **No — to be created** | `06_context_avenue_web/01_file_based/05_skills/uuid-query/SKILL.md` |
| Skill (Claude port) | **No — to be created** | `.claude/skills/uuid-query/SKILL.md` (or via agnostic-sync) |

The `references/` subdirectory in the skill folder will contain pointers (not copies) to the knowledge, rule, and protocol files.

<!-- section_id: "f5a6b7c8-d9e0-4f1a-2b3c-4d5e6f7a8b9c" -->
### 10.5 Porting Matrix

| AI Tool | Skill Location | Port Method | Skill Discovery |
|---------|---------------|-------------|-----------------|
| Claude Code | `.claude/skills/uuid-query/SKILL.md` | Direct port with Claude YAML frontmatter | `/uuid-query` invocation or WHEN condition match |
| Codex CLI | `.codex/skills/uuid-query/SKILL.md` | Adapted for Codex format (if skill system exists) | Codex skill matching |
| Cursor | `.cursorrules` reference | Lean trigger text via agnostic-sync.sh (no separate skill file) | Trigger keyword match in rules |
| Gemini | `GEMINI.md` reference | Full trigger text via agnostic-sync.sh | Trigger keyword match in context |
| Copilot | `.github/copilot-instructions.md` reference | Medium trigger text via agnostic-sync.sh | Trigger keyword match in instructions |
| OpenAI | `OPENAI.md` reference | Full trigger text via agnostic-sync.sh | Trigger keyword match in context |

For tools without a dedicated skill system (Cursor, Gemini, Copilot, OpenAI), the skill content is embedded in the generated context file as a trigger entry in `0AGNOSTIC.md`. The `agnostic-sync.sh` script propagates it to all generated files.

<!-- section_id: "a6b7c8d9-e0f1-4a2b-3c4d-5e6f7a8b9c0d" -->
### 10.6 Integration with 0AGNOSTIC.md

The skill requires two additions to the root `0AGNOSTIC.md`:

**Triggers table** (new row):
```markdown
| Querying UUID identity system (entity lookup, hierarchy, resources) | Load skill: uuid-query |
```

**Resources table** (new row):
```markdown
| UUID Query Skill | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/SKILL.md` | Agent interface for UUID system queries |
```

These entries ensure that:
1. `agnostic-sync.sh` includes the trigger in all generated context files
2. Agents matching the trigger condition discover the skill
3. The resource table provides direct path for on-demand loading

<!-- section_id: "b7c8d9e0-f1a2-4b3c-4d5e-6f7a8b9c0d1e" -->
### 10.7 Connection to Section 6 Interface Design

This skill context avenue implements the `/uuid-query` skill interface designed in Section 6.2. The relationship:

| Section 6 (Interface Design) | Section 10 (Context Avenue) |
|-----------------------------|-----------------------------|
| Defines WHAT the skill teaches | Defines WHERE it lives and HOW it's delivered |
| Specifies commands and WHEN/WHEN NOT | Specifies file structure, porting, discovery |
| Designed the agent-facing interface | Designs the delivery system for that interface |
| Part of the agent interaction layer | Part of the context avenue web (Avenue A3: Skills) |

Together, Sections 6 and 10 fully specify the `/uuid-query` skill from interface to implementation to delivery.
