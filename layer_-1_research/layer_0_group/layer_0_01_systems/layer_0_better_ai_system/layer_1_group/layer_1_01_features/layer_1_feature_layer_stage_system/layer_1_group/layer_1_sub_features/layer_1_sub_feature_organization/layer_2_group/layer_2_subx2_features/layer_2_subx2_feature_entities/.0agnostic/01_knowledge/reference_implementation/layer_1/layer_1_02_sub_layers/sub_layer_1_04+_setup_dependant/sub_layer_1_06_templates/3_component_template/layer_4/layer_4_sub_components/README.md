---
resource_id: "5f5e0833-74dc-4823-b3c0-50332fec7c95"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Sub-Components

This folder contains sub-components (Layer 4) within this component.

Each sub-component follows the standard component template structure (`3_component_template`).

<!-- section_id: "f6fdef43-3e4b-44b9-9cfb-baa7437ec8cb" -->
## Naming Convention

```
layer_4_sub_component_<name>/
```

<!-- section_id: "436145b0-2a6a-422b-a190-4d1f4f9e5792" -->
## When to Create a Sub-Component

Create a sub-component when you have:
- Smaller implementation units within the parent component
- Fine-grained breakdowns of complex components
- Specific pieces that warrant their own lifecycle

<!-- section_id: "bf23d91f-df84-4465-8144-5eeecee28123" -->
## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Component inside a project = **component**
- Component inside a component = **sub_component** (same type nesting)

Since this is a component inside another component (same types), it uses the "sub" prefix.
