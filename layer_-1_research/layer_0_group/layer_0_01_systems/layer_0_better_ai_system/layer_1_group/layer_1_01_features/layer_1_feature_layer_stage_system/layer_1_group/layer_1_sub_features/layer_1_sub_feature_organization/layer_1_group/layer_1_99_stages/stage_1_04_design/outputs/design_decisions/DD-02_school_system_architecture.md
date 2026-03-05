---
resource_id: "b9ba8555-4095-4351-94c9-9b305a4aee10"
resource_type: "output"
resource_name: "DD-02_school_system_architecture"
---
# DD-02: School System Architecture

**Date**: 2026-02-25
**Status**: accepted
**Addresses**: Branch 02 (Instantiation Pattern), Branch 03 need_02 (School System Example)

---

<!-- section_id: "f10c33ca-5cbd-4635-94f8-356287d62251" -->
## Problem Statement

The school system is the primary concrete example of the R/P/I pattern. It needs a clear architecture showing:
1. What research features are being developed for education
2. What production patterns are validated for teaching
3. How each student gets a personalized instance
4. How the knowledge graph, student model, and career goals map to entity context

<!-- section_id: "b5dc85d6-462e-47c1-ada8-309228210de3" -->
## Proposed Solution: School System as R/P/I Example

<!-- section_id: "fefe8180-d371-4406-9732-33339ac7e591" -->
### System Overview

```
better_ai_system/                                    # Parent system
  layer_-1_research/
    layer_-1_better_school_system/                   # RESEARCH version
      layer_0_group/
        layer_0_features/
          layer_0_feature_knowledge_graph_awareness/  # Research feature
          layer_0_feature_student_modeling/            # Research feature
          layer_0_feature_adaptive_learning/           # Research feature
          layer_0_feature_prerequisite_tracking/       # Research feature
          layer_0_feature_career_alignment/            # Research feature

  layer_1/
    layer_1_projects/
      layer_1_project_school/                         # PRODUCTION version
        .0agnostic/
          01_knowledge/
            knowledge_graph/                          # Validated KG patterns
            student_modeling/                         # Validated modeling patterns
            pedagogy/                                 # Teaching principles
        layer_2_group/
          layer_2_instances/
            layer_2_instance_student_dawson/           # INSTANCE
              0AGNOSTIC.md                            # Student identity + state
              .0agnostic/
                01_knowledge/
                  student_profile/                    # This student's profile
                  knowledge_state/                    # What they know/don't know
                  career_goals/                       # Their career targets
```

<!-- section_id: "babf355d-4f97-4671-bdf9-064f7f3b0b69" -->
### Research Features (layer_-1)

Each research feature investigates one aspect of the school system:

| Feature | What It Researches | Key Outputs |
|---------|-------------------|-------------|
| knowledge_graph_awareness | How to map course content to a concept graph | Graph structure, concept relationships, granularity levels |
| student_modeling | How to track what a student knows/doesn't know | Student model format, confidence levels, misconception detection |
| adaptive_learning | How to adjust content based on student state | Adaptation algorithms, difficulty curves, alternative explanations |
| prerequisite_tracking | How to identify and enforce prerequisites | Prerequisite chains, gap detection, review suggestions |
| career_alignment | How to connect learning to career goals | Goal mapping, relevance scoring, path recommendations |

<!-- section_id: "96e25ea2-df8b-41a6-b613-993c248a10d6" -->
### Production Patterns (layer_1)

Production contains validated patterns promoted from research:

| Knowledge Area | Content | Source Research |
|---------------|---------|----------------|
| knowledge_graph/ | Validated graph structure, concept templates | layer_0_feature_knowledge_graph_awareness |
| student_modeling/ | Student model schema, update protocols | layer_0_feature_student_modeling |
| pedagogy/ | Teaching principles, explanation strategies | layer_0_feature_adaptive_learning |

<!-- section_id: "0b2797a3-cd26-4ec9-b584-c7e5c9a49b84" -->
### Per-Student Instances (layer_2)

Each student gets an instance entity:

```
layer_2_instance_student_name/
  0AGNOSTIC.md              # Student identity
    - Name, enrollment, preferences
    - Current courses
    - Learning style observations
    - Current Status: knowledge state summary
  .0agnostic/
    01_knowledge/
      student_profile/      # Demographics, preferences, accessibility needs
      knowledge_state/      # Per-concept: known, unknown, weak, misconception
      career_goals/         # Target career, required skills, progress
      learning_history/     # Past interactions, assessment results
```

<!-- section_id: "8d2e1d79-bf3d-49c9-a523-6b1279e64b4c" -->
### Entity Context Mapping

| School Concept | Entity Location | How AI Accesses It |
|---------------|----------------|-------------------|
| Course content | Production `.0agnostic/01_knowledge/knowledge_graph/` | Read via context chain |
| What student knows | Instance `.0agnostic/01_knowledge/knowledge_state/` | Read from instance entity |
| Student's goals | Instance `.0agnostic/01_knowledge/career_goals/` | Read from instance entity |
| Teaching methods | Production `.0agnostic/01_knowledge/pedagogy/` | Read via context chain |
| Adaptation rules | Production `.0agnostic/02_rules/` | Inherited through context chain |

<!-- section_id: "9456aecf-8795-4e9f-bb62-8996563b57c8" -->
## Alternatives Considered

<!-- section_id: "e5978f6a-6c85-4b81-b23f-43b8ce8baafe" -->
### Alternative A: Flat Student Files
Store all student data in a single JSON file per student.
- **Rejected**: Doesn't scale. No structured access. Hard for AI to navigate.

<!-- section_id: "b587e838-9ad9-4db3-8c99-5b58123eaf2e" -->
### Alternative B: Database-Backed Instances
Use a database instead of filesystem entities.
- **Rejected**: Breaks the entity structure convention. AI agents work with files, not databases. Loses context chain benefits.

<!-- section_id: "e5ec03f3-31e5-4e35-b601-b72f644bca4c" -->
### Alternative C: Shared Student Model
One student model shared across all features.
- **Rejected**: Different features need different views of the student. Instance context provides a unified store, but features read what they need.

<!-- section_id: "a691ac13-8539-4f67-8489-8de1763516f5" -->
## Trade-offs

| Trade-off | Accepted | Why |
|-----------|----------|-----|
| Many small files per student | Yes | Structured access is worth the file count |
| Instance creation overhead | Yes | Template inheritance minimizes manual setup |
| Knowledge graph maintenance | Yes | Foundation for all other features — must be invested in |

<!-- section_id: "c1642819-6ea8-4922-8597-9fc10fbb0a5f" -->
## Design Constraints

- MUST use existing entity structure (0AGNOSTIC.md, .0agnostic/, etc.)
- MUST inherit from production via context chain (no full content copy)
- MUST keep sensitive student data within the instance entity boundary
- SHOULD support the school submodule structure already in use (`layer_1_project_school`)
