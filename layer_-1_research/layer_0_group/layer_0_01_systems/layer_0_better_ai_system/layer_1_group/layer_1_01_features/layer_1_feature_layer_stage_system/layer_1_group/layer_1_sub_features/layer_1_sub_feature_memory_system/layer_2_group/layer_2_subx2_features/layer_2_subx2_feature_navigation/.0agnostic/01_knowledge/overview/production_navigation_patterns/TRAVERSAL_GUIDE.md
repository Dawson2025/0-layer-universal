---
resource_id: "91c59563-2d88-4a6e-ae12-646b308ee3cb"
resource_type: "knowledge"
resource_name: "TRAVERSAL_GUIDE"
---
# System Traversal Guide

<!-- section_id: "51af1f77-bce3-4c6a-8974-14ca5f0fa2af" -->
## Overview

This guide explains how AI agents should navigate the layer-stage system to find content, understand context, and locate resources.

<!-- section_id: "9f6ac1bf-2d63-4129-832b-45f338c81f76" -->
## Navigation Principles

<!-- section_id: "8086dd56-d61d-442a-aa16-dbe096251a7f" -->
### 1. Start with Indexes

Every significant folder has an index file:
- `0INDEX.md` - Contents and navigation
- `0AGNOSTIC.md` - Identity and triggers

**Always read the index first** before exploring contents.

<!-- section_id: "a52dd369-88ca-4fc4-b62c-d4a81eb0f481" -->
### 2. Use the Cascade

Context flows down through layers:
```
layer_0 (universal) → layer_1 (project) → layer_2 (feature)
```

To understand full context, trace back up to parents.

<!-- section_id: "e20c8eea-b7be-43e7-8538-07329f130018" -->
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

<!-- section_id: "f14d677f-24bb-4cba-84c8-bdb655a88e39" -->
## Common Navigation Patterns

<!-- section_id: "78272db9-e6eb-43b4-9cc0-855653d96be9" -->
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
  → /layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/  ← Universal rules
```

<!-- section_id: "12c480d0-12f2-4caa-ae74-637df6767cbd" -->
### Finding Knowledge

```
Current location → layer_N_group → layer_N_03_sub_layers → sub_layer_N_02_knowledge_system
```

Check 0INDEX.md for available knowledge areas.

<!-- section_id: "c112e5a5-0a3f-4343-bab6-3ef9f760aaa0" -->
### Finding Current Work

```
Current location → layer_N_group → layer_N_99_stages → stage_N_XX_current
```

Or check `stage_N_10_current_product/` for deliverables.

<!-- section_id: "8e3ff2f0-fe76-4e2e-b213-2a9bb12d9ef7" -->
### Finding Proposals

```
Current location → layer_N_group → layer_N_00_layer_registry → proposals
```

Check `proposals/0INDEX.md` for active, staging, and archived proposals.

<!-- section_id: "542b5611-a024-451c-ae57-cfc30c84c2e8" -->
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

<!-- section_id: "7f73275b-c3c4-483e-9860-4bfdc1247898" -->
## Navigation by Intent

<!-- section_id: "d9bb8a72-e3d3-49bd-b6b1-6de1de6b559c" -->
### "I need to understand this project"

1. Read `0AGNOSTIC.md` - Identity and scope
2. Read `0INDEX.md` - Structure overview
3. Check `layer_N_99_stages/` - Current work status
4. Check `layer_N_00_layer_registry/proposals/` - Active proposals

<!-- section_id: "4b6646b0-8ede-4c0e-b65c-316afd77acdd" -->
### "I need to find a specific rule"

1. Start at current entity's rules: `sub_layer_N_04_rules/`
2. Check universal rules: `layer_0/.../sub_layer_0_04_rules/`
3. Use grep if needed: `grep -r "rule_keyword" --include="*.md"`

<!-- section_id: "6d582bec-d4ce-487f-9bc4-afb3bb81b882" -->
### "I need to create something new"

1. Read `entity_lifecycle/INSTANTIATION_GUIDE.md`
2. Check templates: `.0agnostic/templates/`
3. Find similar existing entity for reference
4. Follow the instantiation checklist

<!-- section_id: "fb594e60-e4a1-4c63-b879-2e4c73d512fe" -->
### "I need to update something"

1. Read `entity_lifecycle/MAINTENANCE_GUIDE.md`
2. Check for modification protocols in rules
3. Update indexes after changes
4. Regenerate tool files if needed

<!-- section_id: "da3ac2b7-5205-4eb8-a15c-b883e27a3bab" -->
### "I need to find research on a topic"

1. Check research layer: `layer_-1_research/`
2. Look in relevant project's `stage_02_research/outputs/`
3. Check `by_topic/` folders
4. Check `cross_cutting/` for multi-topic research

---

<!-- section_id: "2f9976c4-1d70-4443-9933-8ac7009f05f7" -->
## Hierarchy Navigation

When encountering a `_hierarchy` folder:

<!-- section_id: "46a721bd-91b8-46af-ac28-950da260f94d" -->
### Step 1: Identify the Branching Factor

```
sub_layer_0_05+_setup_dependant_hierarchy/
  └── sub_layer_0_05_operating_systems/   ← Branch by OS
```

<!-- section_id: "4e187705-acb6-465d-9594-98384044c45e" -->
### Step 2: Select Your Branch

Based on current context (OS, environment, tool, etc.):
```
I'm on Linux → sub_layer_0_05_linux_ubuntu/
```

<!-- section_id: "caaa056d-7d71-4813-a9ad-8aefe49648d3" -->
### Step 3: Continue Down Relevant Path Only

Don't load all branches - only follow your path:
```
sub_layer_0_05_linux_ubuntu/
  → sub_layer_0_06_environments/
    → sub_layer_0_06_local/     ← My environment
```

---

<!-- section_id: "500e6406-95b5-4aae-9f0e-e2f6947d4702" -->
## Quick Reference: Where Things Live

| Looking for... | Location Pattern |
|----------------|------------------|
| Universal rules | `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/` |
| Project rules | `<project>/layer_1_group/layer_1_03_sub_layers/sub_layer_1_04_rules/` |
| Knowledge | `<entity>/layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Prompts | `<entity>/layer_N_group/layer_N_03_sub_layers/sub_layer_N_01_prompts/` |
| Current work | `<entity>/layer_N_group/layer_N_99_stages/stage_N_06_development/` |
| Proposals | `<entity>/layer_N_group/layer_N_00_layer_registry/proposals/` |
| Features | `<project>/layer_2_group/layer_2_features/` |
| Research | `layer_-1_research/<project>/` |
| Templates | `<entity>/.0agnostic/templates/` |
| Session logs | `<entity>/.0agnostic/episodic/sessions/` |

---

<!-- section_id: "40009083-69cd-43b7-8817-27c05ef54385" -->
## Navigation Commands

<!-- section_id: "bb62bde0-99db-4538-87da-74308227276d" -->
### Using Indexes
```bash
# Find all index files
find . -name "0INDEX.md" -type f

# Find all agnostic files
find . -name "0AGNOSTIC.md" -type f
```

<!-- section_id: "81933bb3-b778-410f-ae2f-58ec4f53dcd2" -->
### Using Grep for Content
```bash
# Find files mentioning a topic
grep -r "authentication" --include="*.md" -l

# Find rules about something
grep -r "rule" layer_*/layer_*_03_sub_layers/sub_layer_*_04_rules/
```

<!-- section_id: "dfa03017-e115-4073-9bad-9f1b51db7488" -->
### Using Directory Listing
```bash
# See structure at a glance
ls -la layer_*/
ls -la layer_*_group/layer_*_03_sub_layers/
```

---

*See INDEX_SYSTEM.md for details on the indexing system*
