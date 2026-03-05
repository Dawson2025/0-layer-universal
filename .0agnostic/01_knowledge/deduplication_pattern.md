---
resource_id: "383f63b4-75d8-41c7-8f5b-385bad92e7b2"
resource_type: "knowledge"
resource_name: "deduplication_pattern"
---
# Deduplication Pattern & Naming Convention

## Overview

The codebase uses a **single-source-of-truth pattern** to eliminate duplicate documentation across multiple locations. This document defines:

1. **Canonical Files** — authoritative versions at root `.0agnostic/`
2. **Pointer Files** — lightweight references to canonical sources
3. **Naming conventions** to distinguish them
4. **Maintenance procedures** to keep the pattern intact

---

## Canonical Files (Tier 0)

### What They Are
- Complete, authoritative versions of documentation
- Located at `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/`
- Organized by category: `01_knowledge/`, `02_rules/`, `03_protocols/`
- The ONLY place where content should be edited

### Naming Convention
**No special prefix.** Canonical files use their natural names:
```
.0agnostic/01_knowledge/entity_lifecycle/INSTANTIATION_GUIDE.md      ← Canonical
.0agnostic/02_rules/context_scope_boundaries.md                      ← Canonical
.0agnostic/03_protocols/stage_report_protocol.md                     ← Canonical
```

### Key Rules
1. **Edit here first** — When updating any documentation, always edit the canonical version
2. **Full content** — Canonical files contain complete, detailed information
3. **Never edit research copies** — If you find duplicates in research subdirectories, they should be pointers (see below)

---

## Pointer Files (Tier 1)

### What They Are
- Lightweight reference files in research subdirectories
- Point users to the canonical source
- Prevent duplication and maintenance burden
- Typically 7-10 lines (header + link + footer)

### Naming Convention
**Same name as canonical.** Pointer files use identical names to their canonical sources:
```
layer_-1_research/.../context_chain_system/.0agnostic/03_protocols/stage_report_protocol.md
                                                                      ↑
                                                    POINTER (same name as canonical)
```

### Standard Format
```markdown
# [Title]

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL [FILENAME].md]([path_to_canonical])**

---

[1-2 sentences explaining what this documentation covers and why it's unified]

This pointer file directs you to the current production definition.
```

### Example
```markdown
# Context Scope Boundaries

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL CONTEXT_SCOPE_BOUNDARIES.md](../../../../../../../../../../../.0agnostic/02_rules/context_scope_boundaries.md)**

---

All context scope boundary rules are maintained in a single location to prevent inconsistency.

This pointer file directs you to the current production definition.
```

### Key Rules
1. **Never edit pointers** — They should only redirect
2. **Calculate relative paths carefully** — Use relative paths from pointer location to canonical location
3. **Keep pointers under 15 lines** — They're summaries, not full content

---

## How to Identify Which is Which

### Canonical File Checklist
- ✓ Location: `/code/0_layer_universal/.0agnostic/`
- ✓ Contains: Multiple paragraphs, detailed rules, or substantial content
- ✓ Line count: 30+ lines
- ✓ No redirect links

### Pointer File Checklist
- ✓ Location: `layer_-1_research/` or nested research subdirectories
- ✓ Contains: Header + redirect link + footer only
- ✓ Line count: 7-10 lines
- ✓ First non-comment line: "This file has been replaced..."

---

## When to Create a Pointer

**Rule: Create a pointer whenever:**

1. You find documentation with the same name in both:
   - Root `.0agnostic/` (canonical)
   - A research subdirectory (potential duplicate)

2. The content is substantively identical or overlapping

3. The research version is NOT entity-specific (not unique to that entity)

### Example: Should This Be a Pointer?

**YES - make a pointer:**
- Found `LAYERS_EXPLAINED.md` at both root and in `layer_2_subx2_feature_entities/.0agnostic/01_knowledge/`
- Content is identical
- No entity-specific customization

**NO - keep as is:**
- Found `agent_hierarchy_design.md` only in `layer_3_subx3_feature_agent_hierarchy/.0agnostic/01_knowledge/`
- Unique to this entity
- No canonical version exists at root

---

## Maintenance Workflow

### When You Need to Update Documentation

1. **Identify if it's canonical:**
   - Is it in `.0agnostic/` at root?
   - Is it the authoritative version?

2. **If canonical:** Edit it directly
   - All pointers automatically reference the updated version
   - No other edits needed

3. **If pointer:** Don't edit it
   - Edit the canonical instead
   - Pointers don't need updating

### When You Discover a Duplicate

1. **Read both versions** to understand the difference
2. **Identify the canonical** (usually at root `.0agnostic/`)
3. **Replace the research version** with a pointer
4. **Test the link** by checking the path calculation
5. **Commit** with message: `[AI Context] Replace duplicate [filename] with canonical pointer`

---

## Current Canonical Documents

### Knowledge
- `.0agnostic/01_knowledge/entity_lifecycle/INSTANTIATION_GUIDE.md`
- `.0agnostic/01_knowledge/entity_lifecycle/ENTITY_TYPES.md`
- `.0agnostic/01_knowledge/layer_stage_system/LAYERS_EXPLAINED.md`
- `.0agnostic/01_knowledge/layer_stage_system/STAGES_EXPLAINED.md`
- `.0agnostic/01_knowledge/layer_stage_system/NESTED_DEPTH_NAMING.md`
- `.0agnostic/01_knowledge/layer_stage_system/OVERVIEW.md`
- `.0agnostic/01_knowledge/layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md`
- `.0agnostic/01_knowledge/layer_stage_system/SUB_STAGES_EXPLAINED.md`

### Rules
- `.0agnostic/02_rules/context_scope_boundaries.md`
- `.0agnostic/02_rules/context_priority_rules.md`
- `.0agnostic/02_rules/context_traversal.md`

### Protocols
- `.0agnostic/03_protocols/stage_report_protocol.md`

---

## Path Calculation Quick Reference

### Pattern
```
Source (pointer): layer_-1_research/layer_0_group/.../layer_3_subx3_feature_X/.0agnostic/01_knowledge/file.md
Target (canonical): .0agnostic/02_rules/file.md

Relative path: ../../../../../../../../../../../.0agnostic/02_rules/file.md
```

### Formula
1. Count directories from pointer to root (each level up = `../`)
2. From root, navigate down to `.0agnostic/` path
3. Total: `[ups]/[downs]`

### Example: Calculate Path from context_chain_system

```
layer_-1_research/
  layer_0_group/
    layer_0_01_systems/
      layer_0_better_ai_system/
        layer_0_01_features/
          layer_0_feature_layer_stage_system/
            layer_1_group/
              layer_1_sub_features/
                layer_1_sub_feature_agent_delegation_system/
                  layer_2_group/
                    layer_2_subx2_features/
                      layer_2_subx2_feature_memory_system/
                        layer_3_group/
                          layer_3_subx3_features/
                            layer_3_subx3_feature_context_chain_system/
                              .0agnostic/02_rules/  ← Pointer location

Ups to root: ../../../../../../../../../../../../
Path to target: .0agnostic/02_rules/
Final: ../../../../../../../../../../../../.0agnostic/02_rules/file.md
```

---

## Anti-Patterns: What NOT to Do

❌ **DON'T:** Create multiple "canonical" versions of the same document
- This defeats the purpose of single-source-of-truth

❌ **DON'T:** Create a pointer to another pointer
- Pointers should always point to canonical sources (root `.0agnostic/`)

❌ **DON'T:** Edit a pointer file
- If you need to change content, edit the canonical instead

❌ **DON'T:** Leave duplicate content when you find it
- Always replace with a pointer or document why the duplication is intentional

---

## References

- Deduplication project summary: `.0agnostic/01_knowledge/deduplication_project_summary.md`
- Entity structure (canonical): `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`

---

*Last Updated: 2026-02-28*
