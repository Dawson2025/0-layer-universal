---
resource_id: "0bbf43ea-ea15-4ab1-9628-c84acf960ac5"
resource_type: "output"
resource_name: "US-01_developer_creates_research_entity"
---
# Developer Creates Research Entity

**As a** developer setting up a new experimental project,
**I want to** create a research entity under `layer_-1_research/` with a complete stage lifecycle,
**So that** I have an isolated, structured workspace where I can explore ideas without risking production stability.

<!-- section_id: "1f531924-b827-4d5f-95db-bdbbc059e330" -->
## Acceptance Criteria

**Scenario 1: Entity scaffolding is complete**
- **Given** I run the entity creation process targeting `layer_-1_research/`,
- **When** the entity is created,
- **Then** it contains a `0AGNOSTIC.md` with a research-specific identity, a `.0agnostic/` directory with all numbered subdirectories (01-07+), and a `layer_N_99_stages/` directory with all 11 stages (01 through 11).

**Scenario 2: Research entity is isolated from production**
- **Given** a research entity exists at `layer_-1_research/my_experiment/`,
- **When** I modify files within that entity (add stages, write outputs, change 0AGNOSTIC.md),
- **Then** no files outside `layer_-1_research/my_experiment/` are modified, and production entities continue to load their own unmodified context.

**Scenario 3: Entity follows the canonical structure**
- **Given** I inspect the newly created research entity,
- **When** I compare it against the entity structure reference (`entity_structure.md`),
- **Then** every required directory and file from the reference exists in the entity, including `.1merge/`, tool directories (`.claude/`, `.cursor/`, `.github/`), and the stage container with `00_layer_registry`.
