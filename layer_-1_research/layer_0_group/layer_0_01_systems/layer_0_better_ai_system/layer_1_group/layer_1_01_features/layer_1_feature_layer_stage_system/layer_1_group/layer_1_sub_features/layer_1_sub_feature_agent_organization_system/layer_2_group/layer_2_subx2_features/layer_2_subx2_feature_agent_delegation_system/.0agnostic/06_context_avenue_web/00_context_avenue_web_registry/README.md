---
resource_id: "6f0fc50e-cf7e-48f7-9db0-0e4faa49991b"
resource_type: "readme_document"
resource_name: "README"
---
# Context Avenue Web Registry

Management hub for the context avenue web. Tracks all avenues, their ordering, and population status. Provides tooling for insert/delete/move/reorder operations.

<!-- section_id: "7894e7bd-8b12-49ab-af27-18fc39bc98e8" -->
## Files

| File | Purpose |
|------|---------|
| `registry.json` | Machine-readable manifest — avenue numbers, names, scopes, population status |
| `manage-avenues.sh` | CLI tool for CRUD operations — insert, delete, move, list, status, sync |
| `README.md` | This file — documents ordering principle and usage |

<!-- section_id: "3fa8864d-92e5-45ad-aa6b-1975739e3075" -->
## Ordering Principle

Avenues are ordered from **most comprehensive** (can include everything) to **most fragmented** (scoped to specific events/paths).

<!-- section_id: "b9c3e7f2-c949-4ac6-82d2-1b868f00ed88" -->
## Usage

<!-- section_id: "ed3f89d4-9cfd-4ae9-95b5-6ee0acd01267" -->
### List avenues

```bash
./manage-avenues.sh list
```

<!-- section_id: "1803e3ec-5e7f-4e6f-b661-fdbcd0351677" -->
### Check which avenues have content

```bash
./manage-avenues.sh status
```

<!-- section_id: "4e216d19-2bd5-4c96-9960-81e654741ba8" -->
### Insert a new avenue

Inserts at the given position, renumbers everything at or above that position up by 1.

```bash
./manage-avenues.sh insert 03 auto_memory
# Creates 03_auto_memory/, renumbers old 03→04, 04→05, etc.
```

<!-- section_id: "dc6901fe-b8e9-4096-bcbe-08488e503d14" -->
### Delete an avenue

Removes the avenue and renumbers everything above it down by 1.

```bash
./manage-avenues.sh delete 03
# Removes 03_auto_memory/, renumbers old 04→03, 05→04, etc.
```

<!-- section_id: "d4520965-a9b7-4435-91e5-7dea6abe97ed" -->
### Move an avenue

Moves an avenue from one position to another, renumbering the affected range.

```bash
./manage-avenues.sh move 05 02
# Moves avenue 05 to position 02, shifts 02-04 up by 1
```

<!-- section_id: "0f2db014-8eeb-42f7-94b2-e9b881915df4" -->
### Sync registry.json

Regenerates `registry.json` from the current directory state. Run this after manual changes.

```bash
./manage-avenues.sh sync
```

<!-- section_id: "c9c2e311-09d5-43ef-b641-e19cab011146" -->
## After any operation

1. Run `manage-avenues.sh sync` to update `registry.json`
2. Update any `0AGNOSTIC.md` references that mention avenue numbers/names
3. Run `agnostic-sync.sh` to regenerate tool-specific files
4. Commit the changes
