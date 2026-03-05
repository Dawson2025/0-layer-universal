---
resource_id: "2d000cd7-e548-41fe-a45a-c0858f87a8d0"
resource_type: "output"
resource_name: "US-01_ai_maps_class_knowledge"
---
# AI Maps Class Knowledge

**As an** AI tutor in the school system,
**I want to** access a knowledge graph for each of the student's courses,
**So that** I understand the full landscape of concepts, their prerequisites, and their relationships — enabling me to teach in the right order and identify gaps.

<!-- section_id: "17f18a54-75ef-45ab-9fe3-2d68757dd6e9" -->
## Acceptance Criteria

**Scenario 1: Knowledge graph exists per course**
- **Given** a student is enrolled in "Linear Algebra" and "Machine Learning",
- **When** the AI accesses the school system's production knowledge base,
- **Then** it finds a separate knowledge graph for each course, with nodes representing concepts (e.g., "vectors", "matrices", "gradient descent") and edges representing relationships (prerequisite, builds-on, related-to).

**Scenario 2: Prerequisites are explicitly mapped**
- **Given** the Linear Algebra knowledge graph exists,
- **When** the AI queries the prerequisite chain for "eigenvalue decomposition",
- **Then** it receives an ordered list: "scalar multiplication" → "matrix multiplication" → "determinants" → "eigenvalues" → "eigenvalue decomposition" — making the teaching sequence clear.

**Scenario 3: Cross-course connections are visible**
- **Given** the student is enrolled in both "Linear Algebra" and "Machine Learning",
- **When** the AI looks for connections between the two knowledge graphs,
- **Then** it identifies shared concepts (e.g., "matrix multiplication" appears in both) and cross-dependencies (e.g., Machine Learning's "PCA" requires Linear Algebra's "eigenvalue decomposition").
