---
resource_id: "8561a693-d84e-4e82-98fb-7817d27f8984"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Sub*2 Projects

This folder contains nested sub-projects (subx2 projects) within this sub-project.

Each subx2-project follows the standard sub-project template structure (`2_sub_project_template`).

<!-- section_id: "f06b8824-1be4-4592-9220-0e8680b7bdb0" -->
## Naming Convention

```
layer_3_subx2_project_<name>/
```

<!-- section_id: "245287d2-8f9e-493c-8303-533f37e578f9" -->
## When to Create a Sub*2-Project

Create a subx2-project when you have a nested project within a sub-project that:
- Has its own distinct scope and lifecycle
- Warrants its own Git repository (submodule)
- Contains multiple features/components of its own

<!-- section_id: "985ee9ef-91d8-4a09-9ea9-604772c43b2d" -->
## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Project inside a project = **subproject** (subx1)
- Project inside a subproject = **subx2 project** (subx2)
- Project inside a subx2 project = **subx3 project** (subx3)

The `*2` notation indicates two levels of nesting (project → subproject → subx2 project).
