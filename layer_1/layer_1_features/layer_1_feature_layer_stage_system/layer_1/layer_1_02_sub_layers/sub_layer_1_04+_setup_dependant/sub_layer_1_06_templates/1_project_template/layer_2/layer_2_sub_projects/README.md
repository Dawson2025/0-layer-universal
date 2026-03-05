---
resource_id: "c4e73005-f837-43c4-a874-07fa4c4de031"
resource_type: "readme
document"
resource_name: "README"
---
# Sub-Projects

This folder contains sub-projects (Layer 2) within this project.

Each sub-project follows the standard sub-project template structure (`2_sub_project_template`).

<!-- section_id: "6a5dc835-e052-49ab-868e-f7dcbf3f4987" -->
## Naming Convention

```
layer_2_sub_project_<name>/
```

<!-- section_id: "8bd895af-bb1b-49ac-924b-9cf37dd3cfb9" -->
## When to Create a Sub-Project

Create a sub-project when you have:
- A nested project that warrants its own scope and lifecycle
- Content that may become its own Git repository (submodule)
- Multiple features/components that logically belong together

<!-- section_id: "2b60d76f-d508-470f-b8aa-698cc207304b" -->
## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Project inside a project = **sub_project** (same type nesting)
- Feature inside a project = **feature** (different types, no "sub")
- Component inside a project = **component** (different types, no "sub")

Since this is a project inside another project (same types), it uses the "sub" prefix.
