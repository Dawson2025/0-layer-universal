---
resource_id: "0cfef7ea-848e-430b-8fe6-d9de17322099"
resource_type: "output"
resource_name: "US-01_student_gets_personalized_entity"
---
# Student Gets Personalized Entity

**As a** student enrolling in a school system powered by AI,
**I want** my own instance entity that inherits the school system's production patterns,
**So that** the AI knows my specific knowledge gaps, learning goals, and progress without mixing my data with other students'.

<!-- section_id: "3b8a0916-f54a-4e8b-8af1-104c5749a937" -->
## Acceptance Criteria

**Scenario 1: Instance is created with student identity**
- **Given** a new student ("Alice") enrolls in the school system,
- **When** her instance entity is created (e.g., `instances/alice/`),
- **Then** the instance has a `0AGNOSTIC.md` with Alice's identity (name, enrolled courses, goals), a `.0agnostic/` directory for her resources, and a reference back to the school system's production template.

**Scenario 2: Instance inherits production patterns via context chain**
- **Given** Alice's instance entity exists,
- **When** the AI agent loads context for Alice's instance,
- **Then** the context chain includes both Alice's instance-specific content AND the school system's production patterns — inheriting methodology, stage structure, and knowledge organization from the template without duplicating files.

**Scenario 3: Instance data is isolated from other students**
- **Given** both Alice and Bob have instance entities,
- **When** Alice's AI agent updates her knowledge state (e.g., marks "linear algebra" as mastered),
- **Then** Bob's instance remains unchanged — his knowledge state, goals, and progress are completely independent of Alice's modifications.
