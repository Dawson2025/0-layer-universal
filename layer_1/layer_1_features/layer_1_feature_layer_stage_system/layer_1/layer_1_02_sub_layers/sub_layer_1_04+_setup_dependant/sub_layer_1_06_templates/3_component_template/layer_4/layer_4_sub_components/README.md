---
resource_id: "40db78c2-846a-4aed-80d7-91bf7a9c5749"
resource_type: "readme_document"
resource_name: "README"
---
# Sub-Components

This folder contains sub-components (Layer 4) within this component.

Each sub-component follows the standard component template structure (`3_component_template`).

<!-- section_id: "c7656492-acc8-426c-9724-8a91b644118e" -->
## Naming Convention

```
layer_4_sub_component_<name>/
```

<!-- section_id: "6f1d666d-b02b-43ac-9172-3c9b7a8555ea" -->
## When to Create a Sub-Component

Create a sub-component when you have:
- Smaller implementation units within the parent component
- Fine-grained breakdowns of complex components
- Specific pieces that warrant their own lifecycle

<!-- section_id: "eb53d7c4-e6f1-46f5-9e09-c0cb83806334" -->
## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Component inside a project = **component**
- Component inside a component = **sub_component** (same type nesting)

Since this is a component inside another component (same types), it uses the "sub" prefix.
