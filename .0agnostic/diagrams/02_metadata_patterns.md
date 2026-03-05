---
resource_id: "2fe0f282-4ef6-41a0-9b59-d40d71ef11c0"
resource_type: "document"
resource_name: "02_metadata_patterns"
---
# Metadata-Based Organization Patterns

<!-- section_id: "9fecb580-c439-4534-9b1c-a857ee53f234" -->
## Pattern 1: Parent-Child Inheritance

**File**: `machine_learning/0AGNOSTIC.md`

```yaml
## Identity
- Role: Course Project Manager
- Parent: ../computer_science/ (or via metadata pointer)
- Children: layer_5_group/
- Inherits: Grade strategies, Canvas integration
```

**Key Insight**: Parent relationship is *declared*, not *structural*.

---

<!-- section_id: "c05db65a-165f-4f25-bcae-7ea49981fb86" -->
## Pattern 2: Trigger-Based Resource Loading

**File**: `.0agnostic/02_rules/module_management_triggers.md`

```yaml
Triggers:
  - Situation: "User asks for course modules"
    Action: "Load canvas_module_fetching_trajectory.md"

  - Situation: "Canvas API returns requires_browser"
    Action: "Load browser_canvas_content_extraction_trajectory.md"

  - Situation: "Working on assignment"
    Action: "Load grade_strategy from parent classes layer"
```

**Key Insight**: Relationships are *implicit in triggers*, not *explicit in paths*.

---

<!-- section_id: "47282dc7-91d1-4e43-8a55-99d4787bd731" -->
## Pattern 3: Shared Skill Parameterization

**File**: `.0agnostic/01_knowledge/shared_skills/canvas-fetch.md`

```yaml
Skill: canvas-fetch
Parameters:
  - course_id (required)
  - include_grades (optional)
  - include_assignments (optional)

Invoked by:
  - Grade strategy trajectory (for MATH 119, CSE 300, etc.)
  - Module content trajectory

Returns: Structured course data
```

**Key Insight**: Skills are *generic*, *parameterized*, and *reusable*.

---

<!-- section_id: "6bdea19f-fbb6-4786-8257-2402b04196fc" -->
## Pattern 4: Cross-Layer References

Instead of deep nesting, use **pointer documents**:

```
machine_learning/
└── 0AGNOSTIC.md
    references: "See grade_strategy at ../../classes/.0agnostic/..."
```

**Key Insight**: References are *documented*, not *structural*.

---

<!-- section_id: "8d2d299c-8d43-47b3-99fc-a6df4d8aee9b" -->
## Recommended Transition Strategy

<!-- section_id: "8e08fa3d-b225-4de8-9398-bfc8b037233c" -->
### Phase 1: Flatten Filesystem (Immediate)

```
Old:
  layer_1/layer_1_projects/layer_1_project_school/
    layer_2/layer_2_sub_projects/layer_2_sub_project_classes/

New:
  school/
  school_classes/
  school_cs/
  school_ml/
```

Paths reduce from **155+ chars** → **30-40 chars**

<!-- section_id: "a1b66f47-4c3e-4cdd-b55f-b55d416e58bf" -->
### Phase 2: Migrate Relationships to Metadata (Parallel)

- Update 0AGNOSTIC.md with explicit parent/child pointers
- Add trigger documentation
- Create cross-reference index
- Update status.json to track relationships

<!-- section_id: "6a78a575-ecb8-4bac-b933-d0c2635b2122" -->
### Phase 3: Validate System

- Run diagram generator on new structure
- Verify all relationships in metadata
- Test trigger-based resource loading

---

<!-- section_id: "16a53cf5-7076-4fe4-9180-493feb943ba5" -->
## Tools That Work With This Pattern

| Tool | Purpose | Input |
|------|---------|-------|
| Mermaid | Visualize hierarchies | 0AGNOSTIC.md metadata |
| Obsidian | Knowledge graph | 0AGNOSTIC.md + .md files |
| GraphQL | Query relationships | JSON-LD or YAML metadata |
| Custom script | Generate diagrams | Parse 0AGNOSTIC.md files |
