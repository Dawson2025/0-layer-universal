---
resource_id: "5b97f213-49e9-46f9-bd5c-baab577b1945"
resource_type: "output"
resource_name: "US-01_developer_works_on_feature"
---
# Developer Works on Feature

**As a** developer building a new capability for the system,
**I want to** work on a feature entity that has its own complete stage lifecycle (stages 01-11),
**So that** I can develop the capability from requirements through delivery in an isolated, structured environment without affecting other features.

<!-- section_id: "0ba17396-d507-4c4a-84a7-2deebf83f24b" -->
## Acceptance Criteria

**Scenario 1: Feature entity has all 11 stages**
- **Given** I create or enter a feature entity (e.g., `layer_0_feature_knowledge_graph/`),
- **When** I list the contents of `layer_N_99_stages/`,
- **Then** all 11 stages exist (stage_01 through stage_11), each with at minimum an empty directory ready for use.

**Scenario 2: Feature has its own scoped identity**
- **Given** a feature entity exists,
- **When** I read its `0AGNOSTIC.md`,
- **Then** it contains an Identity section with a specific role, scope, parent reference, and children reference — scoped to this feature only, not the entire system.

**Scenario 3: Feature work is isolated from other features**
- **Given** I am working in `layer_0_feature_A/stage_04/outputs/`,
- **When** I create or modify files,
- **Then** no files in `layer_0_feature_B/` or any other sibling feature are modified, and each feature's stage outputs remain independent.
