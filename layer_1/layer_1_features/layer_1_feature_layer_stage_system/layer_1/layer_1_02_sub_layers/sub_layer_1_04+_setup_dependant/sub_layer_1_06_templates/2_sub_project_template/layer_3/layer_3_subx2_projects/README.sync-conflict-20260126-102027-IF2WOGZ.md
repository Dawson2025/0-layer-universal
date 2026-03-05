---
resource_id: "13c432ac-d555-431c-98de-43275fc1244b"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102027-IF2WOGZ"
---
# Sub*2 Projects

This folder contains nested sub-projects (subx2 projects) within this sub-project.

Each subx2-project follows the standard sub-project template structure (`2_sub_project_template`).

<!-- section_id: "9413b187-ae17-4169-a962-aea0847ea43a" -->
## Naming Convention

```
layer_3_subx2_project_<name>/
```

<!-- section_id: "c91a3831-3ec2-4d66-835d-b25eb5a3b856" -->
## When to Create a Sub*2-Project

Create a subx2-project when you have a nested project within a sub-project that:
- Has its own distinct scope and lifecycle
- Warrants its own Git repository (submodule)
- Contains multiple features/components of its own

<!-- section_id: "6ee9c427-e60f-4f1e-acfd-4357b6de2c51" -->
## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Project inside a project = **subproject** (subx1)
- Project inside a subproject = **subx2 project** (subx2)
- Project inside a subx2 project = **subx3 project** (subx3)

The `*2` notation indicates two levels of nesting (project → subproject → subx2 project).
