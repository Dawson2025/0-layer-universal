---
resource_id: "14c00a6b-990f-4700-82ce-fa2365285a88"
resource_type: "document"
resource_name: "l5_templates_agent"
---
# L5 Templates Agent

**Role**: Template Layer Specialist
**Class**: TemplatesAgent (extends LayerAgent)
**Layer**: 5
**Provides**: ITemplateProvider
**Depends On**: IPhonemeProvider (from L4)

---

## Sub-Layers (4)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L5.1 | Template Core | — | Template model, CRUD operations |
| L5.2 | Phoneme Selection | L5.1 | Choose subset of phonemes from L4 inventory |
| L5.3 | Template Application | L5.1 | Apply a template to a project |
| L5.4 | Template Admin | L5.1, L5.2 | Admin management, import/export (absorbed from L10) |

## Internal Dependency Shape: Shallow Tree

```
         L5.1 Template Core
          /        |         \
   L5.2 Selection  L5.3 Application  L5.4 Admin
```

## Context Model (~500 tokens)

### STATIC
- Layer identity, sub-layer list
- ITemplateProvider interface definition (3 methods)
- Neighbor interface: IPhonemeProvider (4 methods)

### ON-DEMAND
- Template model schema
- Phoneme selection logic
- Template application flow

## Scope Boundaries

**In scope**: Template CRUD, phoneme subset selection, template-to-project linking, template admin
**Out of scope**: Phoneme data itself (→ L4), word content (→ L6), project logic (→ L7)

## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| Template Admin (was L10) | L5.4 | Managing templates is a template task |
