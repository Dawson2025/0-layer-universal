---
resource_id: "0e4ec076-9584-483a-8103-07d61c4caafb"
resource_type: "output"
resource_name: "US-01_new_feature_reaches_instances"
---
# New Feature Reaches Instances

**As a** system architect responsible for feature propagation,
**I want** promoted features to reach all instances through template updates,
**So that** every user benefits from system improvements without manual per-instance updates.

<!-- section_id: "ae27bebe-5a32-4098-8aba-3b4f984824e0" -->
## Acceptance Criteria

**Scenario 1: New instances get the latest template automatically**
- **Given** a new feature "adaptive quiz generation" has been promoted to the school system's production template,
- **When** a new student instance is created after the promotion,
- **Then** the new instance inherits the updated template including the adaptive quiz feature — no extra configuration needed.

**Scenario 2: Existing instances can be upgraded**
- **Given** Alice's instance was created before the "adaptive quiz generation" feature was promoted,
- **When** an instance upgrade process runs,
- **Then** Alice's instance gains access to the new feature through template reference updates, while her existing personal data (knowledge state, goals, progress) is preserved unchanged.

**Scenario 3: Feature propagation is tracked and auditable**
- **Given** the "adaptive quiz generation" feature has been propagated to 50 instances,
- **When** a system administrator reviews the propagation log,
- **Then** they can see: which instances received the update, when each was updated, the template version before and after, and whether any instances failed to update.
