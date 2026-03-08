---
resource_id: "f3a4b5c6-d7e8-4f9a-0b1c-2d3e4f5a6b7c"
resource_type: "document"
resource_name: "uuid-identity-system"
---

# UUID Identity System

<!-- section_id: "e2f3a4b5-c6d7-4e8f-9a0b-1c2d3e4f5a6b" -->
## MANDATORY: Resolving $(resolve-uuid UUID)

Context files (CLAUDE.md, AGENTS.md, GEMINI.md) contain `$(resolve-uuid UUID)` references. These are NOT runnable shell functions. You MUST resolve them to get the current filesystem path:

```bash
ROOT=$(git rev-parse --show-toplevel)
jq -r '.uuids["THE-UUID-HERE"].path // empty' "$ROOT/.uuid-index.json"
```

Do NOT copy `$(resolve-uuid ...)` into a shell command. Do NOT hardcode paths you see in old documentation — always resolve the UUID. UUIDs are nested under `.uuids` in the index and each entry has a `.path` field.

<!-- section_id: "a8b9c0d1-e2f3-4a5b-6c7d-8e9f0a1b2c3d" -->
## MANDATORY: Entity Lookup

When you need to find entities by name, path, or UUID, you MUST use entity-find.sh. Do NOT use Glob, Grep, or find commands for entity discovery — they miss nested registries, parent chains, and UUID relationships.

```bash
ROOT=$(git rev-parse --show-toplevel)
ENTITY_FIND="$ROOT/$(jq -r '.uuids["f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7"].path // empty' "$ROOT/.uuid-index.json")"
$ENTITY_FIND memory         # Find entities matching "memory"
$ENTITY_FIND --path chain   # Show paths only
$ENTITY_FIND --uuid memory  # Show UUIDs only
```

<!-- section_id: "b9c0d1e2-f3a4-4b5c-6d7e-8f9a0b1c2d3e" -->
## Other Tools (resolve UUID first, then run)

| Task | UUID to resolve |
|------|----------------|
| Entity lookup (fast) | `f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7` |
| Hierarchy navigation, validation, reference checks | `08a4e9bc-8cc1-457e-b966-0a912ae6dff7` |
| UUID resolution helper | `e3f4a5b6-c7d8-4e9f-0a1b-2c3d4e5f6a7b` |

For full command reference, load the `/uuid-query` skill.
