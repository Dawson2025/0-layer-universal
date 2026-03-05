#!/usr/bin/env python3
"""
Generate Mermaid diagrams from the 0AGNOSTIC hierarchy.
Works around long path issues by using absolute paths internally.
"""

import os
import sys
from pathlib import Path

def generate_hierarchy_diagram():
    """Generate the main hierarchy Mermaid diagram."""

    diagram = """# System Architecture - Hierarchy Visualization

## Layer Hierarchy (Layer 0 → Layer 4)

```mermaid
graph TD
    L0["🔷 Layer 0: Universal<br/>0_layer_universal<br/>(Coordinates all layers)"]
    L1["🟦 Layer 1: Projects<br/>layer_1_project_school<br/>(School project)"]
    L2["🟩 Layer 2: Sub-Projects<br/>layer_2_sub_project_classes<br/>(Classes + Grade Strategy)"]
    L3["🟨 Layer 3: Sub²-Projects<br/>layer_3_subx2_project_computer_science<br/>(CS curriculum)"]
    L4["🟪 Layer 4: Courses<br/>layer_4_subx3_project_machine_learning<br/>(ML algorithms)"]
    L5A["🟥 Layer 5a: Assignments<br/>layer_5_feature_assignments"]
    L5B["🟧 Layer 5b: Modules<br/>layer_5_feature_module_content"]

    L0 -->|parent| L1
    L1 -->|parent| L2
    L2 -->|parent| L3
    L3 -->|parent| L4
    L4 -->|contains| L5A
    L4 -->|contains| L5B

    style L0 fill:#e1f5ff
    style L1 fill:#e8f5e9
    style L2 fill:#fffde7
    style L3 fill:#e0f2f1
    style L4 fill:#f3e5f5
    style L5A fill:#ffebee
    style L5B fill:#ffe0b2
```

## Resource Inheritance

```mermaid
graph LR
    UNI["Universal<br/>(layer_0)"]
    RULES["Rules & Protocols<br/>(.0agnostic/)"]
    GRADE["Grade Strategy<br/>(5 trajectories)"]
    MODULE["Module Content<br/>(4 trajectories)"]
    SKILLS["Shared Skills<br/>(canvas-fetch,<br/>grade-calculator,<br/>layer-populator)"]

    UNI -->|provides| RULES
    RULES -->|enables| GRADE
    RULES -->|enables| MODULE
    GRADE -->|uses| SKILLS
    MODULE -->|uses| SKILLS

    style UNI fill:#e1f5ff
    style RULES fill:#f0f4c3
    style GRADE fill:#fff9c4
    style MODULE fill:#fff59d
    style SKILLS fill:#f3e5f5
```

## Trigger System Architecture

```mermaid
graph TD
    T1["👤 User Event:<br/>Grade Status?"]
    T2["👤 User Event:<br/>Canvas Modules?"]
    T3["🔄 API Event:<br/>Requires Browser"]

    T1 -->|trigger| R1["Load Grade<br/>Strategy Trajectory"]
    T2 -->|trigger| R2["Load Module<br/>Fetching Trajectory"]
    T3 -->|trigger| R3["Load Browser<br/>Content Extraction"]

    R1 -->|invoke| S1["canvas-fetch<br/>Skill"]
    R2 -->|invoke| S2["canvas-module-fetch<br/>Skill"]
    R3 -->|invoke| S3["browser-canvas-reader<br/>Skill"]

    S1 -->|output| D1["Grade Dashboard"]
    S2 -->|output| D2["Module Structure"]
    S3 -->|output| D3["Extracted Content"]

    style T1 fill:#e3f2fd
    style T2 fill:#e3f2fd
    style T3 fill:#ffebee
    style R1 fill:#f1f8e9
    style R2 fill:#f1f8e9
    style R3 fill:#f1f8e9
    style S1 fill:#fce4ec
    style S2 fill:#fce4ec
    style S3 fill:#fce4ec
```

## Path Organization (Current vs. Ideal)

### Current Structure
**Problem**: Deep nesting creates long paths (155+ characters)

```
layer_0_universal/
└── layer_1/layer_1_projects/layer_1_project_school/
    └── layer_2/layer_2_sub_projects/layer_2_sub_project_classes/
        └── layer_3/layer_3_subx2_projects/layer_3_subx2_project_computer_science/
            └── layer_4_group/layer_4_subx3_projects/layer_4_subx3_project_machine_learning/
```

### Ideal Structure (Flattened + Metadata-Based)
**Solution**: Flat filesystem + metadata layer defines relationships

```
school/
├── 0AGNOSTIC.md (defines: "parent: universal, children: classes")
├── .0agnostic/01_knowledge/
├── .0agnostic/02_rules/
└── .0agnostic/03_protocols/

classes/
├── 0AGNOSTIC.md (defines: "parent: school, triggers: grade-strategy")
└── .0agnostic/

computer_science/
├── 0AGNOSTIC.md
└── .0agnostic/

machine_learning/
├── 0AGNOSTIC.md (defines: "parent: cs, inherits: grade-strategy from classes")
└── .0agnostic/
```

**Key insight**: Relationships live in metadata, not filesystem depth.

```

"""
    return diagram


def generate_metadata_reference():
    """Generate reference for key metadata patterns."""

    doc = """# Metadata-Based Organization Patterns

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
"""
    return doc


if __name__ == "__main__":
    # Generate both documents
    hierarchy = generate_hierarchy_diagram()
    metadata = generate_metadata_reference()

    # Write to /tmp (short path)
    output_dir = "/tmp/agnostic-diagrams"
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/01_hierarchy.md", "w") as f:
        f.write(hierarchy)

    with open(f"{output_dir}/02_metadata_patterns.md", "w") as f:
        f.write(metadata)

    print("[✓] Generated diagrams:")
    print(f"    {output_dir}/01_hierarchy.md")
    print(f"    {output_dir}/02_metadata_patterns.md")
    print()
    print("Files are ready to view in any markdown editor.")
    print()
