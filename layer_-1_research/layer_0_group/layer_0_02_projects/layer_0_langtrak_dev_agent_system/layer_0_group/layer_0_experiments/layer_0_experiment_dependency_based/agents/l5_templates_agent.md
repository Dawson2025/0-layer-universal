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

<!-- section_id: "64bf4e2d-0b59-40bb-bdb9-928acc12f49f" -->
## Sub-Layers (4)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L5.1 | Template Core | — | Template model, CRUD operations |
| L5.2 | Phoneme Selection | L5.1 | Choose subset of phonemes from L4 inventory |
| L5.3 | Template Application | L5.1 | Apply a template to a project |
| L5.4 | Template Admin | L5.1, L5.2 | Admin management, import/export (absorbed from L10) |

<!-- section_id: "e4950e8d-d901-466f-9e3e-7d93132195ea" -->
## Internal Dependency Shape: Shallow Tree

```
         L5.1 Template Core
          /        |         \
   L5.2 Selection  L5.3 Application  L5.4 Admin
```

<!-- section_id: "a37b01d0-b6fe-4065-854d-85dfa91cad76" -->
## Context Model (~500 tokens)

<!-- section_id: "52d3c712-3b32-4b5a-9a49-27c641b085da" -->
### STATIC
- Layer identity, sub-layer list
- ITemplateProvider interface definition (3 methods)
- Neighbor interface: IPhonemeProvider (4 methods)

<!-- section_id: "f9e647b3-a21e-4825-ae2c-c90126111392" -->
### ON-DEMAND
- Template model schema
- Phoneme selection logic
- Template application flow

<!-- section_id: "7a8880e4-fda4-491f-8df7-18e6f58433e0" -->
## Scope Boundaries

**In scope**: Template CRUD, phoneme subset selection, template-to-project linking, template admin
**Out of scope**: Phoneme data itself (→ L4), word content (→ L6), project logic (→ L7)

<!-- section_id: "8ad16b76-220d-4625-8e32-4381e794e7e0" -->
## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| Template Admin (was L10) | L5.4 | Managing templates is a template task |
