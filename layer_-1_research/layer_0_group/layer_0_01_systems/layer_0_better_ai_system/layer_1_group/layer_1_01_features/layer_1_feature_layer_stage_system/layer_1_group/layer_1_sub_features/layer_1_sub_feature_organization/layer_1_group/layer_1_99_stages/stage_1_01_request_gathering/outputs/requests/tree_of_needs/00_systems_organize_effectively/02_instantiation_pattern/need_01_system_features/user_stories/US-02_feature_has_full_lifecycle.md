---
resource_id: "3ec10c05-d858-4a12-bcad-1e0418d3768c"
resource_type: "output"
resource_name: "US-02_feature_has_full_lifecycle"
---
# Feature Has Full Lifecycle

**As a** feature agent responsible for developing a capability,
**I want** my feature entity to support the full stage lifecycle from requirements (01) through archives (11),
**So that** I can systematically progress through research, design, development, testing, and delivery without gaps in the workflow.

<!-- section_id: "1dd4ea86-cc3c-4f4b-bcc1-63286ea3871e" -->
## Acceptance Criteria

**Scenario 1: Stages follow the dependency chain**
- **Given** I have completed stage 01 (request gathering) with a tree of needs,
- **When** I move to stage 04 (design),
- **Then** the design stage's 0AGNOSTIC.md references stage 01 outputs as inputs, and the stage dependency chain (01→02→04→05→06→07→08→09→10→11) is documented in the stages container.

**Scenario 2: Each stage can have its own agent**
- **Given** a stage directory exists (e.g., `stage_01_request_gathering/`),
- **When** I populate it with a `0AGNOSTIC.md`,
- **Then** that file defines a stage-specific agent with its own methodology, delegation contract, inputs, and outputs — operating independently from the entity-level agent.

**Scenario 3: Stage outputs feed into downstream stages**
- **Given** stage 06 (development) has produced artifacts in `outputs/`,
- **When** stage 07 (testing) begins,
- **Then** the testing agent can locate and read the development outputs by following the path references in stage 07's `0AGNOSTIC.md` Inputs section.
