# UUID and Database Patterns Research

## Date: 2026-03-02
## Related: `rename_propagation_research.md`, `../../stage_3_04_design/outputs/uuid_identity_system_design.md`

---

## 1. UUID Usage Across Database Types

UUIDs (Universally Unique Identifiers) are a standard identity mechanism used across **every major database paradigm**, not just relational databases.

### Survey of UUID Adoption

| Database Type | Examples | How UUIDs Are Used |
|---------------|----------|-------------------|
| **Relational (SQL)** | PostgreSQL, MySQL, SQLite | Primary keys — PostgreSQL has native `UUID` type, MySQL uses `CHAR(36)` or `BINARY(16)` |
| **Document (NoSQL)** | MongoDB, CouchDB, Firestore | MongoDB uses 12-byte ObjectIDs (similar concept). CouchDB defaults to UUID for `_id`. Firestore auto-generates document IDs |
| **Key-Value** | Redis, DynamoDB | Keys are often UUIDs to avoid collisions across distributed nodes |
| **Graph** | Neo4j, ArangoDB | Node and edge identifiers are often UUIDs |
| **Column-Family** | Cassandra, HBase | Cassandra has native `uuid` and `timeuuid` types — heavily used as partition keys |
| **Search Engines** | Elasticsearch | Document `_id` defaults to auto-generated UUID-like strings |

### Why UUIDs Are Universal

1. **Distributed generation** — no central counter needed (unlike auto-increment)
2. **Merge safety** — two databases generate IDs independently, merge without collision
3. **No coordination** — any process can generate an ID without network calls
4. **Immutability** — ID decoupled from mutable properties (name, location, schema)

### UUID v4 Specifically

UUID v4 (random) is the most commonly used version for application-level identifiers because:
- No dependency on name, path, timestamp, or MAC address
- 2^122 possible values — collision probability is effectively zero
- Simple to generate (`uuidgen`, `uuid.uuid4()`, `crypto.randomUUID()`)
- 36-character string format: `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`

---

## 2. Our System as a Document Database

### The Analogy

The layer-stage hierarchy is functionally a **filesystem-backed document database**. The parallels are structural, not just metaphorical:

| Document DB Concept | Layer-Stage Equivalent | Example |
|---|---|---|
| **Database** | `0_layer_universal/` root | The entire managed hierarchy |
| **Collection** | `layer_N_group/` directory | `layer_1_sub_features/` holds all sub-feature "documents" |
| **Document** | Entity directory + `0AGNOSTIC.md` | `layer_2_subx2_feature_context_chain_system/` |
| **Document ID** (`_id`) | `entity_id` UUID in `0AGNOSTIC.md` | `entity_id: "a1b2c3d4-..."` |
| **Embedded subdocument** | `.0agnostic/` resources | `01_knowledge/`, `02_rules/`, etc. |
| **Nested collection** | `layer_N+1_group/` children | Children of a feature are a nested collection |
| **Foreign key / reference** | Pointer file with `canonical_entity_id` | Points to another document by UUID |
| **Index** | `.uuid-index.json`, `stage_index.json` | Maps UUID → filesystem path for fast lookup |
| **Schema** | `entity_structure.md` | Canonical structure all entities must follow |
| **View / projection** | `CLAUDE.md` (auto-generated) | Read-only view of `0AGNOSTIC.md` for a specific tool |
| **Migration script** | `agnostic-sync.sh`, `assign-entity-uuids.sh` | Schema evolution and data migration |

### Closest Match: CouchDB / MongoDB

The system most closely resembles **CouchDB** because:
1. **Documents are self-contained** — each entity carries its own resources in `.0agnostic/`
2. **Documents have internal structure** — not flat key-value, but nested (knowledge, rules, protocols)
3. **Unique IDs are the primary accessor** — `entity_id` UUID, not name or path
4. **Views are generated** — `CLAUDE.md` is a materialized view of `0AGNOSTIC.md`, like CouchDB views are materialized from documents
5. **Eventual consistency** — `agnostic-sync.sh` propagates changes (like CouchDB replication)

MongoDB parallels:
- **Collections** = `layer_N_group/` directories
- **Embedded documents** = `.0agnostic/` subdirectories
- **References** = pointer files (like MongoDB `$ref` / `ObjectId` references)
- **Indexes** = `.uuid-index.json` (like `db.collection.createIndex()`)

### What This Means for Design

Recognizing the document database pattern validates several design decisions:

1. **UUIDs as primary keys** — standard practice in every database type
2. **Indexes for fast lookup** — `.uuid-index.json` is just a database index
3. **References by ID, not name** — pointer files are foreign keys
4. **Schema enforcement** — `entity_structure.md` is the schema definition
5. **Denormalization** — each entity carries its own resources (like document DB denormalization)
6. **Generated views** — `CLAUDE.md` is a materialized view, regenerated on change

---

## 3. Index Architecture Decisions

### Current Design: Hierarchical Indexes

| Index File | Scope | Contents |
|---|---|---|
| `.uuid-index.json` | Root (global) | All entity UUIDs → paths |
| `stage_index.json` | Per entity | That entity's stage UUIDs → directories |
| `resource_index.json` | Per entity | That entity's resource UUIDs → file paths |

### Alternative: Unified Master Index

A single root-level `.uuid-index.json` could contain ALL UUIDs:

```json
{
  "entities": { "uuid": {"name": "...", "path": "..."} },
  "stages": { "uuid": {"entity_id": "...", "name": "...", "directory": "..."} },
  "resources": { "uuid": {"entity_id": "...", "type": "...", "path": "..."} }
}
```

**Pros**: Single file to query, single rebuild command, simpler resolution algorithm
**Cons**: Larger file, single point of failure, harder to distribute/decentralize

### Recommendation: Hybrid

- **Root `.uuid-index.json`**: Contains ALL UUIDs (entities + stages + resources) for fast global lookup
- **Per-entity `stage_index.json`**: Kept as local authoritative source, used by root index as input
- **Per-entity `resource_index.json`**: Same — local source of truth, feeds into root index
- **Root index is rebuilt from local indexes** — `--rebuild-index` aggregates all local indexes into the root

This mirrors how databases work: local data files + global indexes. The local files are authoritative; the global index is derived.

---

## 4. Caching Strategy

### Current: Rebuild-on-Miss

The `.uuid-index.json` is rebuilt:
- On `--rebuild-index` (explicit)
- When a UUID lookup fails (auto-rebuild)

### Enhanced: Incremental Updates

Instead of full rebuilds, the index could be updated incrementally:

| Event | Index Action |
|---|---|
| Entity created | Add entry to root index |
| Entity renamed | Update path in root index (UUID stays) |
| Entity deleted | Remove from root index |
| Stage created | Add to entity's `stage_index.json` + root index |
| Resource created | Add to entity's `resource_index.json` + root index |

This could be triggered by:
- `agnostic-sync.sh` (already runs after changes)
- Git hooks (post-commit)
- `pointer-sync.sh` (detect and self-heal)

### Index Staleness Detection

Add a hash-based staleness check:
1. Root index stores hash of each entity's `0AGNOSTIC.md`
2. On lookup, compare stored hash vs current file hash
3. If different, rebuild that entity's portion of the index
4. Much faster than full rebuild for large repos

---

## Sources

- RFC 4122 — UUID specification
- MongoDB documentation — document model, indexes, references
- CouchDB documentation — document structure, views, replication
- PostgreSQL documentation — UUID type, indexing
- Cassandra documentation — UUID and timeuuid partition keys
