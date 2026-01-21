# Sub*2 Projects

This folder contains nested sub-projects (sub*2 projects) within this sub-project.

Each sub*2-project follows the standard sub-project template structure (`2_sub_project_template`).

## Naming Convention

```
layer_3_sub*2_project_<name>/
```

## When to Create a Sub*2-Project

Create a sub*2-project when you have a nested project within a sub-project that:
- Has its own distinct scope and lifecycle
- Warrants its own Git repository (submodule)
- Contains multiple features/components of its own

## Note on "Sub" Prefix

The "sub" prefix indicates nesting within the **same type**:
- Project inside a project = **subproject** (sub*1)
- Project inside a subproject = **sub*2 project** (sub*2)
- Project inside a sub*2 project = **sub*3 project** (sub*3)

The `*2` notation indicates two levels of nesting (project → subproject → sub*2 project).
