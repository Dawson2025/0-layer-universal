# Layer Renumbering Guide

## Overview

Layer renumbering shifts the `N` in `layer_N_*` directory names, filenames, and file contents. This is needed when entities move to a different depth in the hierarchy.

**Tool**: `.0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh`

## When to Renumber

### Moving Entities Deeper

An entity at layer 1 becomes a child of another layer 1 entity. Its internal references must shift from `layer_1_*` to `layer_2_*`, and its children from `layer_2_*` to `layer_3_*`.

### Moving Entities Shallower

A feature (layer 2) is promoted to a standalone project (layer 1). All internal references shift down by 1.

### Re-parenting

An entity moves from one parent to another at a different depth. The layer numbers must match the new position in the hierarchy.

### Tree Merges

When merging two entity trees, the incoming tree's layer numbers may conflict. Renumber the incoming tree to fit the target position.

## How to Renumber

### Step 1: Preview Changes

Always start with `--dry-run`:

```bash
bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh \
  ./path/to/entity --dry-run
```

This shows what would change without modifying anything.

### Step 2: Execute

```bash
bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh \
  ./path/to/entity --shift 1
```

### Step 3: Run agnostic-sync.sh

The tool lists all `0AGNOSTIC.md` files that need resync. Run `agnostic-sync.sh` on each:

```bash
SYNC=".0agnostic/agnostic-sync.sh"
for f in $(find ./path/to/entity -name "0AGNOSTIC.md" -type f); do
  dir=$(dirname "$f")
  bash "$SYNC" "$dir"
done
```

### Step 4: Rename the Top-Level Directory

The tool does **not** rename the top-level entity directory. Rename it manually if needed:

```bash
mv layer_1_feature_auth/ layer_2_feature_auth/
```

### Step 5: Verify and Commit

```bash
git diff --stat
git add .
git commit -m "[AI Context] layer renumbering: shifted +1 in entity_name"
```

## Tool Reference

```
Usage: renumber-layers.sh <directory> [options]

Options:
  --shift N       Shift amount (default: +1, negative to decrement)
  --min-layer M   Only renumber layers >= M (default: auto-detect)
  --max-layer X   Highest layer present (default: auto-detect)
  --dry-run       Show changes without executing
  --verbose       Show every operation
```

### What the Tool Changes

| Pattern | Changed? | Example |
|---------|----------|---------|
| `layer_N_*` directories | Yes | `layer_1_group/` -> `layer_2_group/` |
| `layer_N_*` filenames | Yes | `status_1.json` -> `status_2.json` |
| `layer_N_*` in file contents | Yes | References in .md, .json, .jsonld, .sh, .yaml |
| `stage_N_*` directories/content | Yes | `stage_1_01_*` -> `stage_2_01_*` |
| `sub_layer_N_*` | Yes | `sub_layer_1_*` -> `sub_layer_2_*` |
| `subxN_` prefixes | **No** | Tracks nesting depth, not layer number |
| Bare `layer_N/` directories | Yes | `layer_1/` -> `layer_2/` |
| Top-level entity directory | **No** | Must rename manually |

### Skipped Directories

`.git/`, `venv/`, `.venv/`, `node_modules/`, `__pycache__/`

### File Types Processed

`.md`, `.json`, `.jsonld`, `.sh`, `.txt`, `.yaml`, `.yml`

## Common Scenarios

### Shift All Layers Up by 1

Auto-detects the layer range and shifts everything:

```bash
renumber-layers.sh ./my_entity --shift 1
```

### Shift All Layers Down by 1

```bash
renumber-layers.sh ./my_entity --shift -1
```

### Shift Only Specific Layers

Shift layers 3+ up by 1, leaving layers 0-2 untouched:

```bash
renumber-layers.sh ./my_entity --shift 1 --min-layer 3
```

### Cascade Renumbering (Insert a Layer)

To insert a new layer 2 between existing layers 1 and 2, first shift layers 2+ up:

```bash
renumber-layers.sh ./my_entity --shift 1 --min-layer 2
```

Then create the new layer 2 entity in the gap.

## subxN_ Is Not a Layer Number

The `subxN_` prefix (e.g., `subx2_`, `subx3_`) tracks **nesting depth within sub-layers**, not the layer number. The renumbering tool intentionally ignores these.

Example: `subx2_layer_0_05_linux_ubuntu/` after shifting +1 becomes `subx2_layer_1_05_linux_ubuntu/` -- the `subx2_` stays, the `layer_0` becomes `layer_1`.

See `NESTED_DEPTH_NAMING.md` for full details on the subxN convention.

## Post-Renumbering Checklist

- [ ] `--dry-run` reviewed before live execution
- [ ] Top-level entity directory renamed manually (if needed)
- [ ] `agnostic-sync.sh` run on all `0AGNOSTIC.md` files listed by the tool
- [ ] `git diff --stat` reviewed for unexpected changes
- [ ] No stale `layer_N` references remain (search with `grep -r "layer_OLD_" ./entity/`)
- [ ] Parent entity references updated (parent's `0INDEX.md`, registry entries)
- [ ] Committed with `[AI Context] layer renumbering` message

## Research Context

When performing structural operations like renumbering, these research areas provide background on why the system is structured this way:

| Area | Location | Relevance |
|------|----------|-----------|
| Agent Delegation System | `layer_-1_research/.../layer_1_sub_feature_agent_delegation_system/` | Delegation patterns, stage agents, 0AGNOSTIC.md structure |
| Memory System | `.../layer_2_subx2_feature_memory_system/` | Memory architecture, context flow, AI memory tiers |
| Context Chain System | `.../layer_3_subx3_feature_context_chain_system/` | 8-avenue architecture, chain optimization, static/dynamic split |

---

*See also: LAYERS_EXPLAINED.md, NESTED_DEPTH_NAMING.md*
