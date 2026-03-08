---
resource_id: "5a21d894-888e-4753-a018-c829fd6f53d3"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Sub-Projects

This folder contains sub-projects (Layer 2) within this project.

Each sub-project follows the standard sub-project template structure (`2_sub_project_template`).

<!-- section_id: "5497af1d-b0fa-47cd-a3d3-29cbd0f8fb1f" -->
## Naming Convention

```
layer_2_sub_project_<name>/
```

<!-- section_id: "816af04d-5703-4627-9f74-901aeaec32bc" -->
## When to Create a Sub-Project

Create a sub-project when you have:
- A nested project that warrants its own scope and lifecycle
- Content that may become its own Git repository (submodule)
- Multiple features/components that logically belong together

<!-- section_id: "ecdaddf2-ced2-4916-b1e6-b9349d47ef11" -->
## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Project inside a project = **sub_project** (same type nesting)
- Feature inside a project = **feature** (different types, no "sub")
- Component inside a project = **component** (different types, no "sub")

Since this is a project inside another project (same types), it uses the "sub" prefix.
