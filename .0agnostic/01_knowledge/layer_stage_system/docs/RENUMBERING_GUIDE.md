---
resource_id: "bec7c645-8ba5-4344-a860-cff5cdb9cf92"
resource_type: "knowledge"
resource_name: "RENUMBERING_GUIDE"
---
# Layer Renumbering Guide

<!-- section_id: "d1133651-851a-44a3-98f7-c38d9dc0730e" -->
## Overview

Layer renumbering shifts the `N` in `layer_N_*` directory names, filenames, and file contents. This is needed when entities move to a different depth in the hierarchy.

**Tool**: `.0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh`

<!-- section_id: "5a9bcf60-86fc-4692-806f-de5e2e69b312" -->
## When to Renumber

<!-- section_id: "f58c0d50-379e-4ab0-af62-be1b37f5ec95" -->
### Moving Entities Deeper

An entity at layer 1 becomes a child of another layer 1 entity. Its internal references must shift from `layer_1_*` to `layer_2_*`, and its children from `layer_2_*` to `layer_3_*`.

<!-- section_id: "8f9a661e-2b42-4086-b591-90c59a58dc61" -->
### Moving Entities Shallower

A feature (layer 2) is promoted to a standalone project (layer 1). All internal references shift down by 1.

<!-- section_id: "b8e54321-026c-496b-bf7f-24c7a6f586ab" -->
### Re-parenting

An entity moves from one parent to another at a different depth. The layer numbers must match the new position in the hierarchy.

<!-- section_id: "c3ac79d8-1614-4941-984d-055bb7c9d665" -->
### Tree Merges

When merging two entity trees, the incoming tree's layer numbers may conflict. Renumber the incoming tree to fit the target position.

<!-- section_id: "7dd4b8e4-2875-480c-812a-ae3cf03bcca0" -->
## How to Renumber

<!-- section_id: "dd17601d-471c-4bba-aafc-598af77520af" -->
### Step 1: Preview Changes

Always start with `--dry-run`:

```bash
bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh \
  ./path/to/entity --dry-run
```

This shows what would change without modifying anything.

<!-- section_id: "d379a89e-ca43-46eb-8c59-db8ea7fc335f" -->
### Step 2: Execute

```bash
bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh \
  ./path/to/entity --shift 1
```

<!-- section_id: "cdcd3837-5c3c-4654-b6d7-d55b22828506" -->
### Step 3: Run agnostic-sync.sh

The tool lists all `0AGNOSTIC.md` files that need resync. Run `agnostic-sync.sh` on each:

```bash
SYNC=".0agnostic/agnostic-sync.sh"
for f in $(find ./path/to/entity -name "0AGNOSTIC.md" -type f); do
  dir=$(dirname "$f")
  bash "$SYNC" "$dir"
done
```

<!-- section_id: "ce3204e1-4de7-4a41-94e9-36ae8a9ee4b5" -->
### Step 4: Rename the Top-Level Directory

The tool does **not** rename the top-level entity directory. Rename it manually if needed:

```bash
mv layer_1_feature_auth/ layer_2_feature_auth/
```

<!-- section_id: "11ddda27-85c5-40df-9e3f-c67557b83b7e" -->
### Step 5: Verify and Commit

```bash
git diff --stat
git add .
git commit -m "[AI Context] layer renumbering: shifted +1 in entity_name"
```

<!-- section_id: "f4ebc6a9-cfe0-441b-8bb5-f832c5cfeeb9" -->
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

<!-- section_id: "57e54ee2-7265-43ea-85b2-25fadf0f536a" -->
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

<!-- section_id: "6c0e0bea-f9b9-4187-9aa0-6f6fa84935bc" -->
### Skipped Directories

`.git/`, `venv/`, `.venv/`, `node_modules/`, `__pycache__/`

<!-- section_id: "77108e88-1a12-45c0-827c-63aa81ab1a08" -->
### File Types Processed

`.md`, `.json`, `.jsonld`, `.sh`, `.txt`, `.yaml`, `.yml`

<!-- section_id: "ddd9c707-345c-404e-ba13-f107bc6dc64f" -->
## Common Scenarios

<!-- section_id: "235cef54-a69d-467a-8a47-65deaa91c4f0" -->
### Shift All Layers Up by 1

Auto-detects the layer range and shifts everything:

```bash
renumber-layers.sh ./my_entity --shift 1
```

<!-- section_id: "2e9423c3-4702-49b1-b4f3-0cb6a3f0c5ef" -->
### Shift All Layers Down by 1

```bash
renumber-layers.sh ./my_entity --shift -1
```

<!-- section_id: "90266f09-bf42-4000-8c0b-6ed12bf63f6d" -->
### Shift Only Specific Layers

Shift layers 3+ up by 1, leaving layers 0-2 untouched:

```bash
renumber-layers.sh ./my_entity --shift 1 --min-layer 3
```

<!-- section_id: "e3bd355c-b8f8-4982-9a33-c20e710619ff" -->
### Cascade Renumbering (Insert a Layer)

To insert a new layer 2 between existing layers 1 and 2, first shift layers 2+ up:

```bash
renumber-layers.sh ./my_entity --shift 1 --min-layer 2
```

Then create the new layer 2 entity in the gap.

<!-- section_id: "e52a2795-4db0-4546-ac2f-bb379ec2e3d0" -->
## subxN_ Is Not a Layer Number

The `subxN_` prefix (e.g., `subx2_`, `subx3_`) tracks **nesting depth within sub-layers**, not the layer number. The renumbering tool intentionally ignores these.

Example: `subx2_layer_0_05_linux_ubuntu/` after shifting +1 becomes `subx2_layer_1_05_linux_ubuntu/` -- the `subx2_` stays, the `layer_0` becomes `layer_1`.

See `NESTED_DEPTH_NAMING.md` for full details on the subxN convention.

<!-- section_id: "28244c95-e9d7-4b3c-9deb-4c209f26de21" -->
## Post-Renumbering Checklist

- [ ] `--dry-run` reviewed before live execution
- [ ] Top-level entity directory renamed manually (if needed)
- [ ] `agnostic-sync.sh` run on all `0AGNOSTIC.md` files listed by the tool
- [ ] `git diff --stat` reviewed for unexpected changes
- [ ] No stale `layer_N` references remain (search with `grep -r "layer_OLD_" ./entity/`)
- [ ] Parent entity references updated (parent's `0INDEX.md`, registry entries)
- [ ] Committed with `[AI Context] layer renumbering` message

<!-- section_id: "6f87bf74-4363-4215-b378-701abc6e6be8" -->
## Research Context

When performing structural operations like renumbering, these research areas provide background on why the system is structured this way:

| Area | Location | Relevance |
|------|----------|-----------|
| Agent Delegation System | `layer_-1_research/.../layer_1_sub_feature_agent_delegation_system/` | Delegation patterns, stage agents, 0AGNOSTIC.md structure |
| Memory System | `.../layer_2_subx2_feature_memory_system/` | Memory architecture, context flow, AI memory tiers |
| Context Chain System | `.../layer_3_subx3_feature_context_chain_system/` | 8-avenue architecture, chain optimization, static/dynamic split |

---

*See also: LAYERS_EXPLAINED.md, NESTED_DEPTH_NAMING.md*
