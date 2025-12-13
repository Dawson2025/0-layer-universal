# 0.00 Sub-Layer Registry (Stable IDs)

**Purpose**: Make sub-layer references stable even when numeric ordering changes.

## Problem

Sublayer numbers (e.g., `sub_layer_0.10_*`) are **ordering labels**, not identifiers. If we insert/reorder sublayers, renumbering breaks every doc that hard-links to `sub_layer_0.xx_*` paths.

## Solution

Use **stable slugs** (e.g., `mcp_servers_and_tools_setup`) and resolve them via:

- Registry file: `sub_layer_registry.yaml`
- Alias links: `aliases/<slug>.md` (these point to the current numbered folder)

When writing docs, prefer linking to:

`layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/aliases/<slug>.md`

Instead of linking directly to:

`layer_0_universal/0.02_sub_layers/sub_layer_0.xx_<slug>/...`

## Automation

Generate/update the registry + aliases:

```bash
python3 layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/scripts/sub_layer_registry.py generate
```

Check for hard-linked numeric references in docs:

```bash
python3 layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/scripts/sub_layer_registry.py check-hardlinks
```

