---
resource_id: "3a7c9e1f-b2d4-4f6a-8c0d-2e4f6a8b0c1d"
resource_type: "skill
document"
resource_name: "SKILL"
---
# Skill: UUID Query

<!-- section_id: "4b8d0e2f-c3e5-4a7b-9d1e-3f5a7b9c1d2e" -->
## Purpose

Query and navigate the UUID identity system for entity lookup, hierarchy traversal, and resource discovery.

<!-- section_id: "5c9e1f3a-d4f6-4b8c-0e2f-4a6b8c0d2e3f" -->
## When to Use

- You need entity metadata (UUID, type, path, parent, children)
- You need parent/child relationships between entities
- You need to find resources within a specific entity
- You need to look up an entity, stage, or resource by UUID
- You need to search for entities/resources by name pattern
- You need to check the integrity of the pointer system

<!-- section_id: "6d0f2a4b-e5a7-4c9d-1f3a-5b7c9d1e3f4a" -->
## When NOT to Use

- Simple file reads where you already know the path (use Read tool)
- Creating new entities (use `/entity-creation` skill)
- Modifying pointer files (use `pointer-sync.sh --sync`)
- General file searching (use Glob/Grep tools)
- Editing 0AGNOSTIC.md or other source files (use Edit tool directly)

<!-- section_id: "7e1a3b5c-f6b8-4d0e-2a4b-6c8d0e2f4a5b" -->
## Commands

### Fast Entity Lookup (preferred for simple name searches)

```bash
.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh <pattern>      # Find entity by name (~5ms)
.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh --path <pattern>  # Just show paths
.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh --uuid <pattern>  # Just show UUIDs
```

### Lookup by UUID

```bash
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --lookup <uuid>
```

### Navigate Hierarchy

```bash
# Direct parent
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid>

# Full chain to root
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid> --verbose

# Direct children
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --children <uuid>
```

### Query with Filters

Filters are AND-combined. Values support glob patterns.

```bash
# List all entities
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=entity

# Find by name pattern
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=entity name=*research*

# Find resources by type
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=resource resource_type=script

# Find resources within an entity
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=resource entity_id=<uuid>

# Find children of a parent
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query parent_id=<uuid>

# Find entities with children
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query has_children=true
```

**Available filter keys**: `type`, `name`, `path`, `resource_type`, `entity_id`, `parent_id`, `has_children`

### Reference and Integrity

```bash
# Find all references to a UUID (reverse lookup)
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --find-references <uuid>

# Validate system integrity
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --validate

# Rebuild the UUID index from source files
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --rebuild-index
```

### Advanced: Direct jq Queries

```bash
# Custom entity search
jq '.[] | select(.type=="entity" and (.name | test("memory")))' .uuid-index.json

# Per-entity resource catalog
jq '.resources[]' <entity-path>/.0agnostic/resource_index.json

# Filter resources by type within an entity
jq '.resources[] | select(.resource_type=="knowledge")' <entity-path>/.0agnostic/resource_index.json
```

<!-- section_id: "8f2b4c6d-a7c9-4e1f-3b5c-7d9e1f3a5b6c" -->
## Output Format

Query results are formatted as a table:

```
UUID                                  TYPE      NAME                    PATH
a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9  entity    context_chain_system    layer_-1_research/...
5d5be68b-1234-4abc-9def-567890abcdef  entity    trigger_pointer_system  layer_-1_research/...
```

Parent chain (with `--verbose`) shows the full ancestry:

```
child-uuid → parent-uuid → grandparent-uuid → ... → root-uuid
```

<!-- section_id: "9a3c5d7e-b8d0-4f2a-4c6d-8e0f2a4b6c7d" -->
## References

| Resource | Path | Content |
|----------|------|---------|
| Knowledge | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` | How the pointer sync system works |
| Rule | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` | Pointer file format requirements |
| Protocol | `.0agnostic/03_protocols/pointer_sync_protocol/pointer_sync_protocol.md` | Step-by-step usage guide |
| Script | `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh` | The CLI tool itself |
| Index | `.uuid-index.json` | The UUID index (5,313 entries) |

---

*This skill exposes the UUID identity system through bash commands that agents already understand. No SQL, no custom tools — just familiar CLI patterns.*
