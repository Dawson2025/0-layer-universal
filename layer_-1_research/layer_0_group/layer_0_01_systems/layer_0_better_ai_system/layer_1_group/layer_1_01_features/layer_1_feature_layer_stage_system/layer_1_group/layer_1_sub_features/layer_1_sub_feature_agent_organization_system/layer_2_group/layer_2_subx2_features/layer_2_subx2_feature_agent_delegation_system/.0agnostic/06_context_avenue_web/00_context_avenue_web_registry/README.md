---
resource_id: "6f0fc50e-cf7e-48f7-9db0-0e4faa49991b"
resource_type: "readme
document"
resource_name: "README"
---
# Context Avenue Web Registry

Management hub for the context avenue web. Tracks all avenues, their ordering, and population status. Provides tooling for insert/delete/move/reorder operations.

## Files

| File | Purpose |
|------|---------|
| `registry.json` | Machine-readable manifest — avenue numbers, names, scopes, population status |
| `manage-avenues.sh` | CLI tool for CRUD operations — insert, delete, move, list, status, sync |
| `README.md` | This file — documents ordering principle and usage |

## Ordering Principle

Avenues are ordered from **most comprehensive** (can include everything) to **most fragmented** (scoped to specific events/paths).

## Usage

### List avenues

```bash
./manage-avenues.sh list
```

### Check which avenues have content

```bash
./manage-avenues.sh status
```

### Insert a new avenue

Inserts at the given position, renumbers everything at or above that position up by 1.

```bash
./manage-avenues.sh insert 03 auto_memory
# Creates 03_auto_memory/, renumbers old 03→04, 04→05, etc.
```

### Delete an avenue

Removes the avenue and renumbers everything above it down by 1.

```bash
./manage-avenues.sh delete 03
# Removes 03_auto_memory/, renumbers old 04→03, 05→04, etc.
```

### Move an avenue

Moves an avenue from one position to another, renumbering the affected range.

```bash
./manage-avenues.sh move 05 02
# Moves avenue 05 to position 02, shifts 02-04 up by 1
```

### Sync registry.json

Regenerates `registry.json` from the current directory state. Run this after manual changes.

```bash
./manage-avenues.sh sync
```

## After any operation

1. Run `manage-avenues.sh sync` to update `registry.json`
2. Update any `0AGNOSTIC.md` references that mention avenue numbers/names
3. Run `agnostic-sync.sh` to regenerate tool-specific files
4. Commit the changes
