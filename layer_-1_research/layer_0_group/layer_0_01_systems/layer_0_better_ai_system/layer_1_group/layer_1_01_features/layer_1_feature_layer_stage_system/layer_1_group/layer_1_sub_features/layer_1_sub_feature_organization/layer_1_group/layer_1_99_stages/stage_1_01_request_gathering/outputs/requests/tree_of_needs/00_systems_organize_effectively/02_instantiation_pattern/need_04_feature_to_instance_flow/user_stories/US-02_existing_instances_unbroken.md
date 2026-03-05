---
resource_id: "7d440316-043c-499d-b745-9ac11911b8a1"
resource_type: "output"
resource_name: "US-02_existing_instances_unbroken"
---
# Existing Instances Unbroken

**As a** student whose personalized instance has been in use for weeks,
**I want** system improvements to not break my instance or lose my progress,
**So that** I can trust that updates improve my experience without disrupting the work I've already done.

## Acceptance Criteria

**Scenario 1: Instance-specific data survives template updates**
- **Given** Alice has been using her instance for 3 weeks with accumulated knowledge state, completed assessments, and personalized goals,
- **When** the school system pushes a template update that adds a new "career planning" feature,
- **Then** all of Alice's existing data remains intact — her knowledge state, assessment history, and goals are unchanged, and the new feature appears alongside her existing content.

**Scenario 2: Format changes are handled gracefully**
- **Given** a template update changes the structure of the knowledge state file (e.g., adding a new "confidence" field to each topic),
- **When** Alice's instance is upgraded,
- **Then** existing topic entries are preserved with their current data, new entries get the updated format with default values, and no data is lost or corrupted.

**Scenario 3: Failed updates do not corrupt the instance**
- **Given** a template update is applied to Alice's instance but fails partway through (e.g., disk full, interrupted process),
- **When** the instance is accessed after the failure,
- **Then** the instance is in a consistent state — either the update completed fully or it was rolled back to the pre-update state, with no partially-applied changes.
