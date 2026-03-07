---
resource_id: "55a843af-f18c-4a4b-8efc-c50915259b09"
resource_type: "protocol"
resource_name: "uuid_assignment_protocol"
---
# UUID Assignment Protocol

<!-- section_id: "a1b2c3d4-e5f6-4789-0abc-def012345678" -->
## Purpose

Assign stable UUID v4 identifiers to all entities, files, directories, stages, and sections in the layer-stage hierarchy. UUIDs are immutable — they survive renames, moves, and reorganizations.

<!-- section_id: "b2c3d4e5-f6a7-4890-1bcd-ef0123456789" -->
## When to Use

- After creating new entities (run `assign-entity-uuids.sh`)
- After creating new files without `resource_id:` headers (run `assign-file-uuids.sh`)
- After creating new directories without `.dir-id` files (run `assign-dir-uuids.sh`)
- After adding new `## Section` headers without `<!-- section_id -->` (run `assign-section-uuids.sh`)
- After creating new stages (run `create-stage-indexes.sh`)

<!-- section_id: "c3d4e5f6-a7b8-4901-2cde-f01234567890" -->
## Tools

| Tool | resource_id | Purpose |
|------|-------------|---------|
| `assign-entity-uuids.sh` | `92ab3def-22d7-48cd-91be-6744c3466240` | Assigns `entity_id:` to all `0AGNOSTIC.md` files |
| `assign-file-uuids.sh` | `68c9cfcc-9915-47f6-be3a-2c75fbd7ef7e` | Assigns `resource_id:` to `.md`, `.sh`, `.json`, `.jsonld` files |
| `assign-dir-uuids.sh` | `c7d8e9f0-1a2b-4c3d-e4f5-6a7b8c9d0e1f` | Creates `.dir-id` files in directories |
| `assign-section-uuids.sh` | `d8e9f0a1-2b3c-4d5e-f6a7-8b9c0d1e2f3a` | Adds `<!-- section_id -->` comments to `##` headers |
| `create-stage-indexes.sh` | `bcac347f-f4e3-4047-8171-ed9a20022624` | Creates `stage_index.json` for each entity's stages |

All tools are in `tools/` relative to this protocol document.

<!-- section_id: "d4e5f6a7-b8c9-4012-3def-012345678901" -->
## Workflow

1. **Entity UUIDs first**: `./tools/assign-entity-uuids.sh` — scans all `0AGNOSTIC.md` files
2. **File UUIDs**: `./tools/assign-file-uuids.sh` — scans all trackable files
3. **Directory UUIDs**: `./tools/assign-dir-uuids.sh` — creates `.dir-id` in each directory
4. **Section UUIDs**: `./tools/assign-section-uuids.sh` — adds section anchors
5. **Stage indexes**: `./tools/create-stage-indexes.sh` — maps stage names to UUIDs
6. **Rebuild global index**: `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --rebuild-index`

All tools support `--dry-run` for preview and can accept a custom root directory as argument.

<!-- section_id: "e5f6a7b8-c9d0-4123-4ef0-123456789012" -->
## UUID Format

- UUID v4 (random): `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`
- Entities: `entity_id: "..."` in `## Identity` section of `0AGNOSTIC.md`
- Files: `resource_id: "..."` in YAML frontmatter (`.md`) or comment header (`.sh`, `.json`)
- Directories: single UUID in `.dir-id` file
- Sections: `<!-- section_id: "..." -->` HTML comment before `##` headers
- Stages: `stage_index.json` mapping stage names to UUIDs

---

*Tools in this protocol handle UUID assignment. For UUID lookup and querying, see the pointer_sync_protocol.*
