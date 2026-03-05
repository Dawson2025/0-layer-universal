---
resource_id: "2974f747-b97b-4338-830f-010230620f5f"
resource_type: "output"
resource_name: "DEPENDENCIES"
---
# Dependencies

## Cross-Branch Dependencies

| From | To | Relationship |
|------|-----|-------------|
| Branch 01 (R/P lifecycle) | Branch 02 (instantiation) | Instantiation assumes production exists |
| Branch 01 (R/P lifecycle) | Branch 03 (universal) | Universal pattern generalizes R/P lifecycle |
| Branch 02 need_04 (feature→instance flow) | Branch 01 need_03 (promotion) | Feature promotion feeds instance templates |

## External Dependencies

| Need | Depends On | Location |
|------|-----------|----------|
| Branch 03 need_02 (school example) | School project structure | `layer_1/layer_1_projects/layer_1_project_school/` |
| All needs | Entity structure definition | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` |
