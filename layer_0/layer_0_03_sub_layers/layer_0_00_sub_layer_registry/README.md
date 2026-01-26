# 0.00 Sub-Layer Registry (Stable IDs)

**Purpose**: Make sub-layer references stable even when numeric ordering changes.

**Updated**: 2026-01-13

## Current Sub_Layers

| Slug | Number | Description |
|------|--------|-------------|
| `basic_prompts_throughout` | 0.01 | Init prompts |
| `software_engineering_knowledge_system` | 0.02 | Engineering knowledge |
| `universal_principles` | 0.03 | Core principles |
| `universal_rules` | 0.04 | Universal rules |
| `setup_dependant_sub_layers` | 0.05-0.014 | **Unified setup tree** |

> **Note**: Old sub_layers 0.05-0.14 were consolidated into `sub_layer_0_05+_setup_dependant` which contains OS, environments, coding apps, AI apps, MCP servers, tools, protocols, and agent setup.

## Problem

Sublayer numbers (e.g., `sub_layer_0_10_*`) are **ordering labels**, not identifiers. If we insert/reorder sublayers, renumbering breaks every doc that hard-links to `sub_layer_0_xx_*` paths.

## Solution

Use **stable slugs** (e.g., `setup_dependant_sub_layers`) and resolve them via:

- Registry file: `sub_layer_registry.yaml`
- Alias links: `aliases/<slug>.md` (these point to the current numbered folder)

When writing docs, prefer linking to:

`layer_0/layer_0_03_sub_layers/layer_0_00_sub_layer_registry/aliases/<slug>.md`

Instead of linking directly to:

`layer_0/layer_0_03_sub_layers/sub_layer_0_xx_<slug>/...`

## Automation

Generate/update the registry + aliases:

```bash
python3 layer_0/layer_0_03_sub_layers/layer_0_00_sub_layer_registry/scripts/sub_layer_registry.py generate
```

Check for hard-linked numeric references in docs:

```bash
python3 layer_0/layer_0_03_sub_layers/layer_0_00_sub_layer_registry/scripts/sub_layer_registry.py check-hardlinks
```
