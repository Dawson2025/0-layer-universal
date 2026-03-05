---
resource_id: "5e23bf39-2c01-4d73-baba-ef2df60cb420"
resource_type: "knowledge"
resource_name: "TRAVERSAL_GUIDE"
---
# System Traversal Guide

<!-- section_id: "2aa2b7eb-dc85-4109-a8ab-760c26971c75" -->
## Overview

This guide explains how AI agents should navigate the layer-stage system to find content, understand context, and locate resources.

<!-- section_id: "bb9c47c1-5cfa-4464-899c-42f091a23eea" -->
## Navigation Principles

<!-- section_id: "a0078e20-22e8-431b-903f-f87fd1c4edda" -->
### 1. Start with Indexes

Every significant folder has an index file:
- `0INDEX.md` - Contents and navigation
- `0AGNOSTIC.md` - Identity and triggers

**Always read the index first** before exploring contents.

<!-- section_id: "e1e386f8-a246-4c19-9263-b3fa7ba69627" -->
### 2. Use the Cascade

Context flows down through layers:
```
layer_0 (universal) → layer_1 (project) → layer_2 (feature)
```

To understand full context, trace back up to parents.

<!-- section_id: "23d3e401-f322-44d7-837c-5713f2587357" -->
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

<!-- section_id: "1fb847bb-4fd8-400a-9e9a-9b0a6d6bac60" -->
## Common Navigation Patterns

<!-- section_id: "f152323a-3a0c-4288-b2f5-ca870ea15ca3" -->
### Finding Rules

```
Current location → layer_N_group → layer_N_03_sub_layers → sub_layer_N_04_rules
                 → Also check parent layers for inherited rules
```

**Example**:
```
/project/feature_a/
  → /project/feature_a/layer_2_group/layer_2_03_sub_layers/sub_layer_2_04_rules/
  → /project/layer_1_group/layer_1_03_sub_layers/sub_layer_1_04_rules/
  → /layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/  ← Universal rules
```

<!-- section_id: "739ca02f-950b-4e1d-8e3f-99e5c541ca06" -->
### Finding Knowledge

```
Current location → layer_N_group → layer_N_03_sub_layers → sub_layer_N_02_knowledge_system
```

Check 0INDEX.md for available knowledge areas.

<!-- section_id: "2bd9586f-7e65-4a80-85ca-c298fb6cfd1e" -->
### Finding Current Work

```
Current location → layer_N_group → layer_N_99_stages → stage_N_XX_current
```

Or check `stage_N_10_current_product/` for deliverables.

<!-- section_id: "de002d5c-b4aa-4f78-af08-835f01e1ba4a" -->
### Finding Proposals

```
Current location → layer_N_group → layer_N_00_layer_registry → proposals
```

Check `proposals/0INDEX.md` for active, staging, and archived proposals.

<!-- section_id: "f8325258-b431-4aff-be2e-0cae41fc71c0" -->
### Finding Setup-Specific Content

```
Current location → layer_N_group → layer_N_03_sub_layers
                 → sub_layer_N_05+_setup_dependant_hierarchy
                 → Navigate by: OS → Environment → Tool
```

**Example path for Linux + Local + Cursor**:
```
sub_layer_0_04+_setup_dependant/
  → sub_layer_0_05_operating_systems/
    → sub_layer_0_05_linux_ubuntu/
      → sub_layer_0_06_environments/
        → sub_layer_0_06_local/
          → sub_layer_0_07_coding_apps/
            → sub_layer_0_07_cursor/
```

---

<!-- section_id: "59a78125-c9c4-4530-8579-95450ed5fa6d" -->
## Navigation by Intent

<!-- section_id: "1f9161aa-c6ed-49dd-9a9b-21db41cd3ea3" -->
### "I need to understand this project"

1. Read `0AGNOSTIC.md` - Identity and scope
2. Read `0INDEX.md` - Structure overview
3. Check `layer_N_99_stages/` - Current work status
4. Check `layer_N_00_layer_registry/proposals/` - Active proposals

<!-- section_id: "e4734e85-dabc-4fd8-b59a-e3fb83618668" -->
### "I need to find a specific rule"

1. Start at current entity's rules: `sub_layer_N_04_rules/`
2. Check universal rules: `layer_0/.../sub_layer_0_02_rules/`
3. Use grep if needed: `grep -r "rule_keyword" --include="*.md"`

<!-- section_id: "fc4e033b-57ae-4e12-b70d-24041809b8a6" -->
### "I need to create something new"

1. Read `entity_lifecycle/INSTANTIATION_GUIDE.md`
2. Check templates: `.0agnostic/templates/`
3. Find similar existing entity for reference
4. Follow the instantiation checklist

<!-- section_id: "dbb52b63-f20a-4e6a-b956-4e15dd3e6cc0" -->
### "I need to update something"

1. Read `entity_lifecycle/MAINTENANCE_GUIDE.md`
2. Check for modification protocols in rules
3. Update indexes after changes
4. Regenerate tool files if needed

<!-- section_id: "702704f2-c560-46cd-960c-d0780186a727" -->
### "I need to find research on a topic"

1. Check research layer: `layer_-1_research/`
2. Look in relevant project's `stage_02_research/outputs/`
3. Check `by_topic/` folders
4. Check `cross_cutting/` for multi-topic research

---

<!-- section_id: "0873fea3-90a1-4158-8ff8-db29773b0d4a" -->
## Hierarchy Navigation

When encountering a `_hierarchy` folder:

<!-- section_id: "41e7e82e-84a7-4ef5-98db-6521390df51f" -->
### Step 1: Identify the Branching Factor

```
sub_layer_0_04+_setup_dependant/
  └── sub_layer_0_05_operating_systems/   ← Branch by OS
```

<!-- section_id: "2f7bac40-d07b-4a53-bd8e-f259363a8438" -->
### Step 2: Select Your Branch

Based on current context (OS, environment, tool, etc.):
```
I'm on Linux → sub_layer_0_05_linux_ubuntu/
```

<!-- section_id: "456b0d59-9ef4-467f-93b1-353617c81e80" -->
### Step 3: Continue Down Relevant Path Only

Don't load all branches - only follow your path:
```
sub_layer_0_05_linux_ubuntu/
  → sub_layer_0_06_environments/
    → sub_layer_0_06_local/     ← My environment
```

---

<!-- section_id: "68b19073-82bb-419a-aa1a-b2e951c42bf7" -->
## Quick Reference: Where Things Live

| Looking for... | Location Pattern |
|----------------|------------------|
| Universal rules | `layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/` |
| Project rules | `<project>/layer_1_group/layer_1_03_sub_layers/sub_layer_1_04_rules/` |
| Knowledge | `<entity>/layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Knowledge | `<entity>/layer_N_group/layer_N_03_sub_layers/sub_layer_N_01_knowledge_system/` |
| Current work | `<entity>/layer_N_group/layer_N_99_stages/stage_N_06_development/` |
| Proposals | `<entity>/layer_N_group/layer_N_00_layer_registry/proposals/` |
| Features | `<project>/layer_2_group/layer_2_features/` |
| Research | `layer_-1_research/<project>/` |
| Templates | `<entity>/.0agnostic/templates/` |
| Session logs | `<entity>/.0agnostic/episodic/sessions/` |

---

<!-- section_id: "fff7688f-e79a-4a6b-9616-04df6074fff3" -->
## Navigation Commands

<!-- section_id: "8a5e371d-62f5-47ad-8bbf-1f9e5be165b6" -->
### Using Indexes
```bash
# Find all index files
find . -name "0INDEX.md" -type f

# Find all agnostic files
find . -name "0AGNOSTIC.md" -type f
```

<!-- section_id: "b1be950a-e815-4efe-9199-123813198610" -->
### Using Grep for Content
```bash
# Find files mentioning a topic
grep -r "authentication" --include="*.md" -l

# Find rules about something
grep -r "rule" layer_*/layer_*_03_sub_layers/sub_layer_*_04_rules/
```

<!-- section_id: "6bf9dbb9-a4a0-4492-8c9a-73f9d4c2970e" -->
### Using Directory Listing
```bash
# See structure at a glance
ls -la layer_*/
ls -la layer_*_group/layer_*_03_sub_layers/
```

---

*See INDEX_SYSTEM.md for details on the indexing system*
