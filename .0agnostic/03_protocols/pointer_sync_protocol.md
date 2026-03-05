---
resource_id: "ad9a7a96-744f-45a7-b5a7-d82a9cd15a95"
resource_type: "protocol"
resource_name: "pointer_sync_protocol"
---
# Pointer Sync Protocol

**Scope**: All agents | **Trigger**: When creating, moving, or validating pointer files

<!-- section_id: "ae43a743-59f9-4b23-a3f2-09c9ae378d4b" -->
## 1. Purpose

Pointer files reference canonical content locations using relative paths. When directories move, these paths break silently. This protocol ensures pointer files stay synchronized with their canonical targets.

<!-- section_id: "651e083b-8ace-4d64-9c39-1f79b3c2c035" -->
## 2. Pointer File Format

Every pointer file MUST have YAML frontmatter with these fields:

```yaml
---
pointer_to: logical_id            # Required: human-readable identifier
canonical_entity: entity_name     # Required: directory name to find via search
canonical_entity_id: "uuid"       # Required: entity UUID from .uuid-index.json
canonical_stage: stage_name       # Optional: stage directory within entity
canonical_stage_id: "uuid"        # Optional: stage UUID from stage_index.json
canonical_subpath: relative/path  # Optional: path within stage/entity
---
```

**UUID fields**: `canonical_entity_id` and `canonical_stage_id` are stable identifiers that survive renames. The script resolves UUIDs first, falling back to name-based resolution for backward compatibility.

The body MUST include a `> **Canonical location**:` line that the script updates:

```markdown
> **Canonical location**: `auto/updated/relative/path`
```

<!-- section_id: "9bb0c194-52ee-4485-97eb-c930062a682c" -->
## 3. Creating a Pointer File

1. Add YAML frontmatter with `pointer_to`, `canonical_entity`, and optionally `canonical_stage` + `canonical_subpath`
2. Add the `> **Canonical location**:` line (can be empty — the script fills it)
3. Add a brief description of what the pointer references
4. Add "Do not duplicate content here — read the canonical location instead."
5. Run `pointer-sync.sh` to compute and fill the relative path

<!-- section_id: "f1264c84-1db5-4cdb-8bc6-a53a1b4f8325" -->
## 4. Running the Sync

| Command | Purpose |
|---------|---------|
| `pointer-sync.sh` | Update all pointer files with current paths |
| `pointer-sync.sh --dry-run` | Preview changes without modifying files |
| `pointer-sync.sh --validate` | Check all pointers resolve; exit 1 if broken |
| `pointer-sync.sh --verbose` | Show detailed resolution steps |
| `pointer-sync.sh --rebuild-index` | Rebuild `.uuid-index.json` from all entity UUIDs |
| `pointer-sync.sh --find-references UUID` | Find all pointers referencing a given UUID |
| `pointer-sync.sh --detect-cycles` | Check for circular pointer references |
| `pointer-sync.sh --gc` | Find orphaned UUIDs (no matching entity directory) |

**Script location**: `.0agnostic/pointer-sync.sh`

<!-- section_id: "d9a470ca-7637-4331-9f69-2f9352c58f00" -->
## 5. When to Run

| Event | Action |
|-------|--------|
| After moving/renaming directories | `pointer-sync.sh` (update all) |
| After `agnostic-sync.sh` | Automatic — pointer validation runs at end |
| After creating a new pointer | `pointer-sync.sh --validate` (verify it resolves) |
| Before committing | `pointer-sync.sh --validate` (catch stale pointers) |
| After Edit/Write on pointer file | Automatic via Claude Code hook |

<!-- section_id: "6bc4bd8b-1681-44bc-870f-569edc743c22" -->
## 6. Automatic Execution (Hooks)

The pointer system has a Claude Code hook (`pointer-edit-guard.sh`) that fires after Edit/Write operations on files containing `pointer_to:`. It reminds the agent to run `pointer-sync.sh --validate` after modifying pointer files.

Hook configuration: `.claude/settings.json` → `PostToolUse` → `Edit|Write`

<!-- section_id: "f34bc46a-dd56-49e1-a83b-39eadb503980" -->
## 7. Resolution Algorithm

For each pointer file:
1. **UUID-first**: If `canonical_entity_id` exists, look up the entity path in `.uuid-index.json`
2. **Name fallback**: If no UUID or UUID lookup fails, `find` the entity directory by `canonical_entity` name
3. **Stage resolution**: If `canonical_stage_id` exists, look up in the entity's `stage_index.json`; otherwise find by `canonical_stage` name
4. If `canonical_subpath` is set, append it
5. Compute relative path from pointer file's directory to canonical target
6. Update the `> **Canonical location**:` line
7. If name fallback was used, emit a deprecation warning

**UUID index location**: `.uuid-index.json` at repo root
**Stage index location**: `stage_*_00_stage_registry/stage_index.json` within each entity

<!-- section_id: "5a125099-9b35-4312-af78-c6249a7b0f44" -->
## 8. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| "entity not found" | Directory renamed or moved | Update `canonical_entity` in frontmatter, or add `canonical_entity_id` |
| "stage not found" | Stage directory missing | Check entity has the expected stage, or add `canonical_stage_id` |
| "subpath does not exist" | Content moved within entity | Update `canonical_subpath` in frontmatter |
| "no Canonical location line" | Pointer body missing required line | Add `> **Canonical location**: \`\`` to body |
| "UUID not in index" | Entity renamed without index rebuild | Run `pointer-sync.sh --rebuild-index` |
| "name fallback warning" | Pointer missing UUID fields | Run `migrate-pointers.sh` to add UUID fields |
