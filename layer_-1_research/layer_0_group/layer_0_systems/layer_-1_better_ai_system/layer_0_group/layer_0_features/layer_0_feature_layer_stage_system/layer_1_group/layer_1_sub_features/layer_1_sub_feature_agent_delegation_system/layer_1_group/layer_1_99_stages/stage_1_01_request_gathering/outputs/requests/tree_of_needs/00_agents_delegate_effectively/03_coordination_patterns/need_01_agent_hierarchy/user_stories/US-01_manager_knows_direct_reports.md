# US-1: Entity manager knows its direct reports

**Need**: [Agent Hierarchy](../README.md)

---

**As a** user who asks the AI to manage a project with multiple stages and child entities,
**I want** the manager to know exactly which stages and child entities it manages,
**So that** it can delegate to the right agent without me having to explain the project structure.

### What Happens

1. User says "manage this project" or "what can we work on?"
2. Manager reads its 0AGNOSTIC.md and finds a children table and stage overview table
3. Manager knows its direct reports: stages (01-11) and child entities (sub-features)
4. Manager can propose delegation options: "We can work on stage 02 research or the memory system sub-feature"
5. User picks a direction and the manager delegates accordingly

### Acceptance Criteria

- Manager's 0AGNOSTIC.md contains a children table and a stage overview table
- Manager can list all direct reports without reading additional files
- User does not need to explain the project structure to the manager
