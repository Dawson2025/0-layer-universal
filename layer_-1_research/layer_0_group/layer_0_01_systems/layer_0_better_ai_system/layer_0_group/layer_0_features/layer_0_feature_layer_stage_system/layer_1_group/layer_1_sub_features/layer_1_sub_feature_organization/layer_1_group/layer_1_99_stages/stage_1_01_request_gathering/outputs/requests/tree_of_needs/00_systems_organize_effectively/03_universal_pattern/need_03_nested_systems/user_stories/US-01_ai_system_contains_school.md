# AI System Contains School as Sub-System

**As an** AI system architect,
**I want to** organize the school system as a sub-system entity within the broader AI system,
**So that** education capabilities are a coherent, self-contained domain that inherits universal context from its parent while maintaining its own internal structure.

## Acceptance Criteria

**Scenario 1: School system is a child entity of the AI system**
- **Given** the AI system exists as the root entity,
- **When** I inspect its children,
- **Then** the school system appears as a child entity (e.g., `layer_1_project_school/`) with its own `0AGNOSTIC.md`, `.0agnostic/`, and full entity structure — nested within the AI system's hierarchy.

**Scenario 2: School system inherits universal context**
- **Given** the AI system's `layer_0/` defines universal rules (e.g., file change reporting, commit protocols),
- **When** the school system's agents load their context chain,
- **Then** the universal rules from the parent AI system are included in the chain — the school system does not need to re-define them.

**Scenario 3: School system maintains its own domain context**
- **Given** the school system has domain-specific concepts (knowledge graphs, student models, course structures),
- **When** I inspect the school system's `.0agnostic/01_knowledge/`,
- **Then** it contains education-specific knowledge that does not exist in the parent AI system — the school system adds domain context on top of what it inherits.
