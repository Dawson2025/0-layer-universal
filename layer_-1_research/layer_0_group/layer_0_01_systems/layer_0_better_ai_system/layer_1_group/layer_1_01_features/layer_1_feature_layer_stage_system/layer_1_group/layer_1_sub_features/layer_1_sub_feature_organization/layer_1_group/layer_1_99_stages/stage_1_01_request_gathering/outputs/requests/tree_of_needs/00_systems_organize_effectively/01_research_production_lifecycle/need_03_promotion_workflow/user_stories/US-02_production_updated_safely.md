---
resource_id: "110d6311-add4-4765-bc6b-453054f97c23"
resource_type: "output"
resource_name: "US-02_production_updated_safely"
---
# Production Updated Safely

**As a** production manager responsible for system stability,
**I want** promoted content to go through validation and approval before entering production,
**So that** production stability is maintained and any issues from promotion can be identified and rolled back.

## Acceptance Criteria

**Scenario 1: Promotion requires explicit approval**
- **Given** a researcher has prepared a finding for promotion,
- **When** they submit it through the promotion protocol,
- **Then** the protocol requires a review step where the production manager (or designated reviewer) approves the change before it modifies any production files.

**Scenario 2: Rollback is possible after promotion**
- **Given** a finding has been promoted to production and an issue is discovered afterward,
- **When** the production manager initiates a rollback,
- **Then** the promotion history (tracked in the research knowledge index) identifies exactly what was changed, when, and from which research source — enabling targeted reversal without affecting unrelated production content.

**Scenario 3: Promotion history is auditable**
- **Given** multiple findings have been promoted over time,
- **When** I review the research knowledge index (`RESEARCH_KNOWLEDGE_INDEX.md`),
- **Then** each promotion entry includes: research source path, promotion date, target production path, status (promoted/reverted), and a one-line summary of what was promoted.
