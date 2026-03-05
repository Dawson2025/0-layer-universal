---
resource_id: "4ba069cc-1858-43da-846b-f041f57f8d40"
resource_type: "readme
document"
resource_name: "README"
---
# Sub*2 Projects

This folder contains nested sub-projects (subx2 projects) within this sub-project.

Each subx2-project follows the standard sub-project template structure (`2_sub_project_template`).

## Naming Convention

```
layer_3_subx2_project_<name>/
```

## When to Create a Sub*2-Project

Create a subx2-project when you have a nested project within a sub-project that:
- Has its own distinct scope and lifecycle
- Warrants its own Git repository (submodule)
- Contains multiple features/components of its own

## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Project inside a project = **subproject** (subx1)
- Project inside a subproject = **subx2 project** (subx2)
- Project inside a subx2 project = **subx3 project** (subx3)

The `*2` notation indicates two levels of nesting (project → subproject → subx2 project).
