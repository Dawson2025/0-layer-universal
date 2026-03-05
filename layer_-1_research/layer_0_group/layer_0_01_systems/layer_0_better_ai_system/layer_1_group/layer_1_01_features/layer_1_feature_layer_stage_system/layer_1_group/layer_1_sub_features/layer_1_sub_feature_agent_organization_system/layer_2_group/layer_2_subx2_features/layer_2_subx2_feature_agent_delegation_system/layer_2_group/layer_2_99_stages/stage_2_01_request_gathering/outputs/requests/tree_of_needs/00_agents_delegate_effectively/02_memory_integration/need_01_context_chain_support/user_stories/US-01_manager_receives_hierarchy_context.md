---
resource_id: "eab815f3-e49a-4d31-8808-452f64cf41e7"
resource_type: "output"
resource_name: "US-01_manager_receives_hierarchy_context"
---
# US-1: Manager receives hierarchy context automatically

**Need**: [Context Chain Support](../README.md)

---

**As a** user who opens a project and expects the AI to know where it is in the hierarchy,
**I want** the manager to automatically receive its identity, children, and parent scope through the context chain,
**So that** the AI can make delegation decisions immediately without me explaining the project structure.

<!-- section_id: "cc20201b-3a9c-4770-b604-215eb5c753a2" -->
### What Happens

1. User opens a project and says "manage this entity"
2. Context chain automatically loads the manager's 0AGNOSTIC.md
3. Manager receives: its own identity, its children list, and its parent's scope
4. Manager knows where it is in the hierarchy and what it can delegate to
5. User can immediately ask "what needs work?" and get an informed answer

<!-- section_id: "75ccdd35-e457-410e-b957-af45c201143c" -->
### Acceptance Criteria

- Manager's static context includes self identity, children list, and parent scope
- No manual file reads are needed for the manager to know its hierarchy position
- User does not need to explain the project structure to the AI
