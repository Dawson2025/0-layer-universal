---
resource_id: "f94e8acd-4b4d-4783-bdea-18506b230cf2"
resource_type: "readme
output"
resource_name: "README"
---
# User Stories — Nested Systems

## Actors

| Actor | Description |
|-------|-------------|
| AI System | Contains sub-systems like the school system |
| School System | Sub-system with its own R/P/I cycle |

## Stories

| ID | Story | Actor |
|----|-------|-------|
| [US-01](US-01_ai_system_contains_school.md) | AI system contains school | AI System |
| [US-02](US-02_school_has_own_rpi_cycle.md) | School has own R/P/I cycle | School System |
