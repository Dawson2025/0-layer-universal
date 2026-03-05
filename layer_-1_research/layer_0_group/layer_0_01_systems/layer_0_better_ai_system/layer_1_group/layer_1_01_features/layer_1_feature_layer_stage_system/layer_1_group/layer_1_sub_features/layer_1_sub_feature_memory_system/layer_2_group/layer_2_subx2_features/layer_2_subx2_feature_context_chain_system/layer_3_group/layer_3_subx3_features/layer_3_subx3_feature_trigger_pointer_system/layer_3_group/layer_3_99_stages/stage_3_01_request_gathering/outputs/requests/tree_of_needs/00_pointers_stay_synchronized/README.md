---
resource_id: "2c3c89f6-6378-430a-aa2d-6c3278e00db7"
resource_type: "readme
output"
resource_name: "README"
---
# Root Need: Pointers Stay Synchronized

**The fundamental goal all pointer system requirements derive from.**

---

## Definition

> Pointer files always resolve to the correct canonical location, even after directories are moved or renamed. Stale pointers are detected automatically and agents are prompted to fix them.

---

## The Problem

Current pointer files use hardcoded relative paths. When directories move:
- Paths break silently
- No agent is warned about the stale reference
- Manual path computation is error-prone and tedious
- No way to validate all pointers at once

---

## The Vision

A system where:
- Pointer files self-declare their target via structured frontmatter
- A script resolves targets dynamically (by entity name, not by hardcoded path)
- Hooks trigger validation automatically after edits
- Stale pointers are caught during `agnostic-sync.sh` runs
- New pointers are trivial to create (fill in frontmatter, run script)

---

## Three Branches

| Branch | Question | Description |
|--------|----------|-------------|
| [**01_pointer_format**](./01_pointer_format/) | "How are pointers structured?" | YAML frontmatter format, required fields, body conventions |
| [**02_path_resolution**](./02_path_resolution/) | "How are canonical paths found?" | Entity search, stage navigation, subpath resolution |
| [**03_trigger_automation**](./03_trigger_automation/) | "How are pointers validated automatically?" | Hooks, agnostic-sync integration, CI-ready validation |

---

## Branch Structure

```
00_pointers_stay_synchronized/           (this folder - the root)
|
+-- 01_pointer_format/                   How pointers are structured
|   +-- need_01_frontmatter_standard     YAML fields, required vs optional
|   +-- need_02_body_convention          Canonical location line, description
|
+-- 02_path_resolution/                  How canonical paths are found
|   +-- need_01_entity_search            Find entity dirs by name
|   +-- need_02_relative_path_compute    Compute portable relative paths
|
+-- 03_trigger_automation/               How pointers validate automatically
    +-- need_01_hook_triggers            Claude Code PostToolUse hooks
    +-- need_02_sync_integration         agnostic-sync.sh end-of-run validation
```

---

## Success Criteria

The root need is satisfied when:
- [ ] All pointer files use YAML frontmatter with `pointer_to:` and `canonical_entity:`
- [ ] `pointer-sync.sh` resolves all pointers correctly
- [ ] `pointer-sync.sh --validate` exits 0 when all pointers are valid, 1 when any are broken
- [ ] Claude Code hook fires after editing pointer files
- [ ] `agnostic-sync.sh` reports pointer validation at end of run
- [ ] Creating a new pointer takes <1 minute (fill frontmatter, run script)
