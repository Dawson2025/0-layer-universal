---
resource_id: "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: uuid-query
description: "Query and navigate the UUID identity system for entity lookup, hierarchy traversal, and resource discovery. Use when you need entity metadata, parent/child relationships, resource locations, or UUID lookups across the layer-stage hierarchy."
---

# UUID Query Skill

<!-- section_id: "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b" -->
## WHEN to Use
- You need entity metadata (UUID, type, path, parent, children)
- You need parent/child relationships between entities
- You need to find resources within a specific entity
- You need to look up an entity, stage, or resource by UUID
- You need to search for entities/resources by name pattern
- You need to check the integrity of the pointer system
- You need to understand the hierarchy structure

<!-- section_id: "f6a7b8c9-d0e1-4f2a-3b4c-5d6e7f8a9b0c" -->
## WHEN NOT to Use
- Simple file reads where you already know the path (use Read tool)
- Creating new entities (use `/entity-creation` skill)
- Modifying pointer files (use `pointer-sync.sh --sync`)
- General file searching (use Glob/Grep tools)
- Editing 0AGNOSTIC.md or other source files (use Edit tool directly)

<!-- section_id: "a7b8c9d0-e1f2-4a3b-4c5d-6e7f8a9b0c1d" -->
## Steps

1. **Identify what you need**: entity lookup, hierarchy navigation, resource search, or integrity check
2. **Run the appropriate command** from the Commands section below
3. **Parse the output**: Results are formatted as a table (UUID, TYPE, NAME, PATH)
4. **Use the paths**: Resolved paths can be passed directly to the Read tool

<!-- section_id: "b8c9d0e1-f2a3-4b4c-5d6e-7f8a9b0c1d2e" -->
## Commands

### Lookup

```bash
# By UUID
.0agnostic/pointer-sync.sh --lookup <uuid>

# By name pattern
.0agnostic/pointer-sync.sh --query name=*memory*
```

### Hierarchy Navigation

```bash
# Direct parent
.0agnostic/pointer-sync.sh --parent <uuid>

# Full chain to root
.0agnostic/pointer-sync.sh --parent <uuid> --verbose

# Direct children
.0agnostic/pointer-sync.sh --children <uuid>
```

### Filtered Queries

Filters are AND-combined. Values support glob patterns.

```bash
# All entities
.0agnostic/pointer-sync.sh --query type=entity

# Entities matching name
.0agnostic/pointer-sync.sh --query type=entity name=*research*

# Resources of a type
.0agnostic/pointer-sync.sh --query type=resource resource_type=script

# Resources within an entity
.0agnostic/pointer-sync.sh --query type=resource entity_id=<uuid>

# Children of a parent
.0agnostic/pointer-sync.sh --query parent_id=<uuid>

# Entities with children
.0agnostic/pointer-sync.sh --query has_children=true
```

**Filter keys**: `type`, `name`, `path`, `resource_type`, `entity_id`, `parent_id`, `has_children`

### Integrity & Maintenance

```bash
# Find all references to a UUID
.0agnostic/pointer-sync.sh --find-references <uuid>

# Validate all pointers
.0agnostic/pointer-sync.sh --validate

# Rebuild index from source
.0agnostic/pointer-sync.sh --rebuild-index
```

### Advanced: Direct jq

```bash
# Custom search on index
jq '.[] | select(.type=="entity" and (.name | test("memory")))' .uuid-index.json

# Per-entity resource catalog
jq '.resources[]' <entity>/.0agnostic/resource_index.json
```

<!-- section_id: "c9d0e1f2-a3b4-4c5d-6e7f-8a9b0c1d2e3f" -->
## Output Format

```
UUID                                  TYPE      NAME                    PATH
a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9  entity    context_chain_system    layer_-1_research/...
```

<!-- section_id: "d0e1f2a3-b4c5-4d6e-7f8a-9b0c1d2e3f4a" -->
## References

| Resource | Path |
|----------|------|
| Knowledge | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` |
| Rule | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` |
| Protocol | `.0agnostic/03_protocols/pointer_sync_protocol.md` |
| Script | `.0agnostic/pointer-sync.sh` |
| Index | `.uuid-index.json` (5,313 entries) |

---

*Exposes the UUID identity system through bash commands. No SQL, no custom tools.*
