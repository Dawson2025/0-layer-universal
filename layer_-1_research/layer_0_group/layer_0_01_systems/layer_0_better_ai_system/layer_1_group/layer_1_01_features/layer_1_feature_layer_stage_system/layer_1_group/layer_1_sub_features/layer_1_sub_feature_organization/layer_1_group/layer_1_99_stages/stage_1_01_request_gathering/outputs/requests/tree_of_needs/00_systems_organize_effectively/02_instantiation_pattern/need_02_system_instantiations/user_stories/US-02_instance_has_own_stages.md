---
resource_id: "69d2c189-daee-4cce-ae23-57fe9e17c4f1"
resource_type: "output"
resource_name: "US-02_instance_has_own_stages"
---
# Instance Has Own Stages

**As a** system architect designing the instantiation pattern,
**I want** each instance to have its own stage progression,
**So that** per-user work (assessments, learning paths, personalized plans) follows the same structured stage lifecycle as system-level work.

<!-- section_id: "b00ccba5-f4bd-45d9-8e1a-b0ac053dac4e" -->
## Acceptance Criteria

**Scenario 1: Instance has a stage lifecycle**
- **Given** a student instance entity exists (e.g., `instances/alice/`),
- **When** I inspect its directory structure,
- **Then** it contains `layer_N_99_stages/` with all 11 stages — enabling the instance to track per-student work from request gathering through to current product.

**Scenario 2: Stage agents access both instance and system context**
- **Given** an AI agent enters Alice's `stage_01_request_gathering/`,
- **When** the agent loads its context chain,
- **Then** it has access to both Alice's instance-specific data (her goals, knowledge state) AND the school system's production methodology (how to do request gathering) — the stage agent inherits methodology from the system while operating on instance data.

**Scenario 3: Instance stage progress is tracked independently**
- **Given** Alice has completed stages 01 and 02 in her instance,
- **When** Bob's instance is checked,
- **Then** Bob's stage progress is independent — he may be at stage 01 or stage 06, unaffected by Alice's progression.
