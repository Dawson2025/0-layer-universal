---
resource_id: "2fe0f282-4ef6-41a0-9b59-d40d71ef11c0"
resource_type: "document"
resource_name: "02_metadata_patterns"
---
# Metadata-Based Organization Patterns

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

## Pattern 4: Cross-Layer References

Instead of deep nesting, use **pointer documents**:

```
machine_learning/
└── 0AGNOSTIC.md
    references: "See grade_strategy at ../../classes/.0agnostic/..."
```

**Key Insight**: References are *documented*, not *structural*.

---

## Recommended Transition Strategy

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

### Phase 2: Migrate Relationships to Metadata (Parallel)

- Update 0AGNOSTIC.md with explicit parent/child pointers
- Add trigger documentation
- Create cross-reference index
- Update status.json to track relationships

### Phase 3: Validate System

- Run diagram generator on new structure
- Verify all relationships in metadata
- Test trigger-based resource loading

---

## Tools That Work With This Pattern

| Tool | Purpose | Input |
|------|---------|-------|
| Mermaid | Visualize hierarchies | 0AGNOSTIC.md metadata |
| Obsidian | Knowledge graph | 0AGNOSTIC.md + .md files |
| GraphQL | Query relationships | JSON-LD or YAML metadata |
| Custom script | Generate diagrams | Parse 0AGNOSTIC.md files |
