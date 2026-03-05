---
resource_id: "ad9a7a96-744f-45a7-b5a7-d82a9cd15a95"
resource_type: "protocol"
resource_name: "pointer_sync_protocol"
---
# Pointer Sync Protocol

**Scope**: All agents | **Trigger**: When creating, moving, or validating pointer files

## 1. Purpose

Pointer files reference canonical content locations using relative paths. When directories move, these paths break silently. This protocol ensures pointer files stay synchronized with their canonical targets.

## 2. Pointer File Format

Every pointer file MUST have YAML frontmatter with these fields:

```yaml
---
pointer_to: logical_id            # Required: human-readable identifier
canonical_entity: entity_name     # Required: directory name to find via search
canonical_stage: stage_name       # Optional: stage directory within entity
canonical_subpath: relative/path  # Optional: path within stage/entity
---
```

The body MUST include a `> **Canonical location**:` line that the script updates:

```markdown
> **Canonical location**: `auto/updated/relative/path`
```

## 3. Creating a Pointer File

1. Add YAML frontmatter with `pointer_to`, `canonical_entity`, and optionally `canonical_stage` + `canonical_subpath`
2. Add the `> **Canonical location**:` line (can be empty — the script fills it)
3. Add a brief description of what the pointer references
4. Add "Do not duplicate content here — read the canonical location instead."
5. Run `pointer-sync.sh` to compute and fill the relative path

## 4. Running the Sync

| Command | Purpose |
|---------|---------|
| `pointer-sync.sh` | Update all pointer files with current paths |
| `pointer-sync.sh --dry-run` | Preview changes without modifying files |
| `pointer-sync.sh --validate` | Check all pointers resolve; exit 1 if broken |
| `pointer-sync.sh --verbose` | Show detailed resolution steps |

**Script location**: `.0agnostic/pointer-sync.sh`

## 5. When to Run

| Event | Action |
|-------|--------|
| After moving/renaming directories | `pointer-sync.sh` (update all) |
| After `agnostic-sync.sh` | Automatic — pointer validation runs at end |
| After creating a new pointer | `pointer-sync.sh --validate` (verify it resolves) |
| Before committing | `pointer-sync.sh --validate` (catch stale pointers) |
| After Edit/Write on pointer file | Automatic via Claude Code hook |

## 6. Automatic Execution (Hooks)

The pointer system has a Claude Code hook (`pointer-edit-guard.sh`) that fires after Edit/Write operations on files containing `pointer_to:`. It reminds the agent to run `pointer-sync.sh --validate` after modifying pointer files.

Hook configuration: `.claude/settings.json` → `PostToolUse` → `Edit|Write`

## 7. Resolution Algorithm

For each pointer file:
1. Extract `canonical_entity` from frontmatter
2. `find` the entity directory by name under `0_layer_universal/`
3. If `canonical_stage` is set, find that stage within the entity
4. If `canonical_subpath` is set, append it
5. Compute relative path from pointer file's directory to canonical target
6. Update the `> **Canonical location**:` line

## 8. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| "entity not found" | Directory renamed or moved | Update `canonical_entity` in frontmatter |
| "stage not found" | Stage directory missing | Check entity has the expected stage |
| "subpath does not exist" | Content moved within entity | Update `canonical_subpath` in frontmatter |
| "no Canonical location line" | Pointer body missing required line | Add `> **Canonical location**: \`\`` to body |
