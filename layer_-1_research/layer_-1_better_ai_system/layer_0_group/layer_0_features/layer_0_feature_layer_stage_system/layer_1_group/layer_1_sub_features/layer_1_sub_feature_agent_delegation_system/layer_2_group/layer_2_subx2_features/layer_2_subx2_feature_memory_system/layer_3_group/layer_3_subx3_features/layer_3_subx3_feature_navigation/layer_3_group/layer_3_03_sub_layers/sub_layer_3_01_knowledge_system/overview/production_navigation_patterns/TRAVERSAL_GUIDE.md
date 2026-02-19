# System Traversal Guide

## Overview

This guide explains how AI agents should navigate the layer-stage system to find content, understand context, and locate resources.

## Navigation Principles

### 1. Start with Indexes

Every significant folder has an index file:
- `0INDEX.md` - Contents and navigation
- `0AGNOSTIC.md` - Identity and triggers

**Always read the index first** before exploring contents.

### 2. Use the Cascade

Context flows down through layers:
```
layer_0 (universal) → layer_1 (project) → layer_2 (feature)
```

To understand full context, trace back up to parents.

### 3. Follow Pointers

0AGNOSTIC.md contains pointers to resources:
```markdown
## Pointers
| Resource | Location |
|----------|----------|
| Rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
```

Use these instead of searching blindly.

---

## Common Navigation Patterns

### Finding Rules

```
Current location → layer_N_group → layer_N_03_sub_layers → sub_layer_N_04_rules
                 → Also check parent layers for inherited rules
```

**Example**:
```
/project/feature_a/
  → /project/feature_a/layer_3_group/layer_3_03_sub_layers/sub_layer_3_04_rules/
  → /project/layer_2_group/layer_2_03_sub_layers/sub_layer_2_04_rules/
  → /layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/  ← Universal rules
```

### Finding Knowledge

```
Current location → layer_N_group → layer_N_03_sub_layers → sub_layer_N_02_knowledge_system
```

Check 0INDEX.md for available knowledge areas.

### Finding Current Work

```
Current location → layer_N_group → layer_N_99_stages → stage_N_XX_current
```

Or check `stage_N_10_current_product/` for deliverables.

### Finding Proposals

```
Current location → layer_N_group → layer_N_00_layer_registry → proposals
```

Check `proposals/0INDEX.md` for active, staging, and archived proposals.

### Finding Setup-Specific Content

```
Current location → layer_N_group → layer_N_03_sub_layers
                 → sub_layer_N_05+_setup_dependant_hierarchy
                 → Navigate by: OS → Environment → Tool
```

**Example path for Linux + Local + Cursor**:
```
sub_layer_0_05+_setup_dependant_hierarchy/
  → sub_layer_0_05_operating_systems/
    → sub_layer_0_05_linux_ubuntu/
      → sub_layer_0_06_environments/
        → sub_layer_0_06_local/
          → sub_layer_0_07_coding_apps/
            → sub_layer_0_07_cursor/
```

---

## Navigation by Intent

### "I need to understand this project"

1. Read `0AGNOSTIC.md` - Identity and scope
2. Read `0INDEX.md` - Structure overview
3. Check `layer_N_99_stages/` - Current work status
4. Check `layer_N_00_layer_registry/proposals/` - Active proposals

### "I need to find a specific rule"

1. Start at current entity's rules: `sub_layer_N_04_rules/`
2. Check universal rules: `layer_0/.../sub_layer_0_04_rules/`
3. Use grep if needed: `grep -r "rule_keyword" --include="*.md"`

### "I need to create something new"

1. Read `entity_lifecycle/INSTANTIATION_GUIDE.md`
2. Check templates: `.0agnostic/templates/`
3. Find similar existing entity for reference
4. Follow the instantiation checklist

### "I need to update something"

1. Read `entity_lifecycle/MAINTENANCE_GUIDE.md`
2. Check for modification protocols in rules
3. Update indexes after changes
4. Regenerate tool files if needed

### "I need to find research on a topic"

1. Check research layer: `layer_-1_research/`
2. Look in relevant project's `stage_02_research/outputs/`
3. Check `by_topic/` folders
4. Check `cross_cutting/` for multi-topic research

---

## Hierarchy Navigation

When encountering a `_hierarchy` folder:

### Step 1: Identify the Branching Factor

```
sub_layer_0_05+_setup_dependant_hierarchy/
  └── sub_layer_0_05_operating_systems/   ← Branch by OS
```

### Step 2: Select Your Branch

Based on current context (OS, environment, tool, etc.):
```
I'm on Linux → sub_layer_0_05_linux_ubuntu/
```

### Step 3: Continue Down Relevant Path Only

Don't load all branches - only follow your path:
```
sub_layer_0_05_linux_ubuntu/
  → sub_layer_0_06_environments/
    → sub_layer_0_06_local/     ← My environment
```

---

## Quick Reference: Where Things Live

| Looking for... | Location Pattern |
|----------------|------------------|
| Universal rules | `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/` |
| Project rules | `<project>/layer_2_group/layer_2_03_sub_layers/sub_layer_2_04_rules/` |
| Knowledge | `<entity>/layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Prompts | `<entity>/layer_N_group/layer_N_03_sub_layers/sub_layer_N_01_prompts/` |
| Current work | `<entity>/layer_N_group/layer_N_99_stages/stage_N_06_development/` |
| Proposals | `<entity>/layer_N_group/layer_N_00_layer_registry/proposals/` |
| Features | `<project>/layer_3_group/layer_3_features/` |
| Research | `layer_-1_research/<project>/` |
| Templates | `<entity>/.0agnostic/templates/` |
| Session logs | `<entity>/.0agnostic/episodic/sessions/` |

---

## Navigation Commands

### Using Indexes
```bash
# Find all index files
find . -name "0INDEX.md" -type f

# Find all agnostic files
find . -name "0AGNOSTIC.md" -type f
```

### Using Grep for Content
```bash
# Find files mentioning a topic
grep -r "authentication" --include="*.md" -l

# Find rules about something
grep -r "rule" layer_*/layer_*_03_sub_layers/sub_layer_*_04_rules/
```

### Using Directory Listing
```bash
# See structure at a glance
ls -la layer_*/
ls -la layer_*_group/layer_*_03_sub_layers/
```

---

*See INDEX_SYSTEM.md for details on the indexing system*
