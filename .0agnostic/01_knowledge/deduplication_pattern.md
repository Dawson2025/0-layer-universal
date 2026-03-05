---
resource_id: "383f63b4-75d8-41c7-8f5b-385bad92e7b2"
resource_type: "knowledge"
resource_name: "deduplication_pattern"
---
# Deduplication Pattern & Naming Convention

<!-- section_id: "ee0b52e8-5a85-41eb-ac5c-280fa50e7e98" -->
## Overview

The codebase uses a **single-source-of-truth pattern** to eliminate duplicate documentation across multiple locations. This document defines:

1. **Canonical Files** — authoritative versions at root `.0agnostic/`
2. **Pointer Files** — lightweight references to canonical sources
3. **Naming conventions** to distinguish them
4. **Maintenance procedures** to keep the pattern intact

---

<!-- section_id: "c60fabdb-8edd-4453-a598-4627ef37a285" -->
## Canonical Files (Tier 0)

<!-- section_id: "cd20f54e-114a-459a-a6d8-10861651aa0f" -->
### What They Are
- Complete, authoritative versions of documentation
- Located at `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/`
- Organized by category: `01_knowledge/`, `02_rules/`, `03_protocols/`
- The ONLY place where content should be edited

<!-- section_id: "877ea479-c518-45a3-8922-d9df6c2b0ec6" -->
### Naming Convention
**No special prefix.** Canonical files use their natural names:
```
.0agnostic/01_knowledge/entity_lifecycle/INSTANTIATION_GUIDE.md      ← Canonical
.0agnostic/02_rules/context_scope_boundaries.md                      ← Canonical
.0agnostic/03_protocols/stage_report_protocol.md                     ← Canonical
```

<!-- section_id: "8c607b56-d447-4c2a-9bfa-d13201820a4b" -->
### Key Rules
1. **Edit here first** — When updating any documentation, always edit the canonical version
2. **Full content** — Canonical files contain complete, detailed information
3. **Never edit research copies** — If you find duplicates in research subdirectories, they should be pointers (see below)

---

<!-- section_id: "79262fc0-194d-46f4-a130-4a8eb2e0ccca" -->
## Pointer Files (Tier 1)

<!-- section_id: "803564e9-288d-4bb9-8e69-70d70444dfef" -->
### What They Are
- Lightweight reference files in research subdirectories
- Point users to the canonical source
- Prevent duplication and maintenance burden
- Typically 7-10 lines (header + link + footer)

<!-- section_id: "f99c32db-24b6-45e9-8221-3b8b06bb67ef" -->
### Naming Convention
**Same name as canonical.** Pointer files use identical names to their canonical sources:
```
layer_-1_research/.../context_chain_system/.0agnostic/03_protocols/stage_report_protocol.md
                                                                      ↑
                                                    POINTER (same name as canonical)
```

<!-- section_id: "991a3f32-6bab-4cbe-b1ec-fc41b51bb73e" -->
### Standard Format
```markdown
# [Title]

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL [FILENAME].md]([path_to_canonical])**

---

[1-2 sentences explaining what this documentation covers and why it's unified]

This pointer file directs you to the current production definition.
```

<!-- section_id: "3206972b-a8ff-41c3-b841-a8f4a81cb1e4" -->
### Example
```markdown
# Context Scope Boundaries

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL CONTEXT_SCOPE_BOUNDARIES.md](../../../../../../../../../../../.0agnostic/02_rules/context_scope_boundaries.md)**

---

All context scope boundary rules are maintained in a single location to prevent inconsistency.

This pointer file directs you to the current production definition.
```

<!-- section_id: "0c0a49d7-6445-49cf-968c-61aab31545d4" -->
### Key Rules
1. **Never edit pointers** — They should only redirect
2. **Calculate relative paths carefully** — Use relative paths from pointer location to canonical location
3. **Keep pointers under 15 lines** — They're summaries, not full content

---

<!-- section_id: "5f59fb77-9071-44a3-89d7-f1484a9b1cd7" -->
## How to Identify Which is Which

<!-- section_id: "290f10aa-296a-4f23-a47f-25441fbefb70" -->
### Canonical File Checklist
- ✓ Location: `/code/0_layer_universal/.0agnostic/`
- ✓ Contains: Multiple paragraphs, detailed rules, or substantial content
- ✓ Line count: 30+ lines
- ✓ No redirect links

<!-- section_id: "9db325bb-4f55-45a9-90c9-41cea9545a90" -->
### Pointer File Checklist
- ✓ Location: `layer_-1_research/` or nested research subdirectories
- ✓ Contains: Header + redirect link + footer only
- ✓ Line count: 7-10 lines
- ✓ First non-comment line: "This file has been replaced..."

---

<!-- section_id: "f0b13878-d1ae-4aea-a775-011fd685eb7e" -->
## When to Create a Pointer

**Rule: Create a pointer whenever:**

1. You find documentation with the same name in both:
   - Root `.0agnostic/` (canonical)
   - A research subdirectory (potential duplicate)

2. The content is substantively identical or overlapping

3. The research version is NOT entity-specific (not unique to that entity)

<!-- section_id: "99dd2e3b-af0c-46e4-bdab-91d3fe282a23" -->
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

<!-- section_id: "93ca5f4c-ebe6-4c68-9a5c-50975e06e9a7" -->
## Maintenance Workflow

<!-- section_id: "7b65de6d-4493-473f-b8cc-483c50668bc0" -->
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

<!-- section_id: "0ce94e22-6804-4095-96b1-19b7c30a4e89" -->
### When You Discover a Duplicate

1. **Read both versions** to understand the difference
2. **Identify the canonical** (usually at root `.0agnostic/`)
3. **Replace the research version** with a pointer
4. **Test the link** by checking the path calculation
5. **Commit** with message: `[AI Context] Replace duplicate [filename] with canonical pointer`

---

<!-- section_id: "56775c06-83f6-46e3-a247-f659d9cde9f8" -->
## Current Canonical Documents

<!-- section_id: "b64245af-5175-4579-a874-4220cfe1a65f" -->
### Knowledge
- `.0agnostic/01_knowledge/entity_lifecycle/INSTANTIATION_GUIDE.md`
- `.0agnostic/01_knowledge/entity_lifecycle/ENTITY_TYPES.md`
- `.0agnostic/01_knowledge/layer_stage_system/LAYERS_EXPLAINED.md`
- `.0agnostic/01_knowledge/layer_stage_system/STAGES_EXPLAINED.md`
- `.0agnostic/01_knowledge/layer_stage_system/NESTED_DEPTH_NAMING.md`
- `.0agnostic/01_knowledge/layer_stage_system/OVERVIEW.md`
- `.0agnostic/01_knowledge/layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md`
- `.0agnostic/01_knowledge/layer_stage_system/SUB_STAGES_EXPLAINED.md`

<!-- section_id: "3b83d4f4-fba9-433f-9d79-e014b9a30a29" -->
### Rules
- `.0agnostic/02_rules/context_scope_boundaries.md`
- `.0agnostic/02_rules/context_priority_rules.md`
- `.0agnostic/02_rules/context_traversal.md`

<!-- section_id: "f9bd98da-bd96-44fc-b0d9-169d790d0d54" -->
### Protocols
- `.0agnostic/03_protocols/stage_report_protocol.md`

---

<!-- section_id: "5f01e4e1-71ed-4d2a-aad9-23f9531c5b6d" -->
## Path Calculation Quick Reference

<!-- section_id: "ba591eb2-d763-43b0-a2df-ef2e2e9dcab3" -->
### Pattern
```
Source (pointer): layer_-1_research/layer_0_group/.../layer_3_subx3_feature_X/.0agnostic/01_knowledge/file.md
Target (canonical): .0agnostic/02_rules/file.md

Relative path: ../../../../../../../../../../../.0agnostic/02_rules/file.md
```

<!-- section_id: "5749d889-4e4c-4924-9999-49fae14c3b43" -->
### Formula
1. Count directories from pointer to root (each level up = `../`)
2. From root, navigate down to `.0agnostic/` path
3. Total: `[ups]/[downs]`

<!-- section_id: "b49a6c22-f10c-4aa2-8d60-ce5273c488e2" -->
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

<!-- section_id: "d2d5866e-dc29-4e2b-85a0-18f0ed3b794e" -->
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

<!-- section_id: "44beafa8-7bfb-4b56-80b0-c8faa6a3ab28" -->
## References

- Deduplication project summary: `.0agnostic/01_knowledge/deduplication_project_summary.md`
- Entity structure (canonical): `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`

---

*Last Updated: 2026-02-28*
