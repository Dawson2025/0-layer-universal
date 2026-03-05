---
resource_id: "48034299-8385-4f95-ae06-ffc605567746"
resource_type: "output"
resource_name: "US-03_production_unaffected"
---
# Production Unaffected by Research

**As a** production system relying on stable, validated patterns,
**I want** research entity changes to be fully isolated from production content,
**So that** no experimental work — whether successful or failed — can accidentally break the stable patterns that agents and users depend on.

## Acceptance Criteria

**Scenario 1: Research modifications stay within research boundaries**
- **Given** a researcher modifies a `0AGNOSTIC.md` file inside `layer_-1_research/my_experiment/`,
- **When** a production agent loads context from `layer_0/` or `layer_1/`,
- **Then** the production agent's context chain contains zero references to `layer_-1_research/` content, and no production files have been modified.

**Scenario 2: Research can read but not write production**
- **Given** a research entity needs to reference production patterns (e.g., reading `entity_structure.md`),
- **When** the research agent reads production files,
- **Then** the production files remain unchanged, and the research entity stores any derived content in its own `outputs/` directory.

**Scenario 3: Failed experiments have no side effects**
- **Given** a research experiment produces invalid or broken output (e.g., malformed 0AGNOSTIC.md, incorrect directory structure),
- **When** the experiment is abandoned or deleted,
- **Then** no production entities, no sibling research entities, and no shared infrastructure files are affected.
