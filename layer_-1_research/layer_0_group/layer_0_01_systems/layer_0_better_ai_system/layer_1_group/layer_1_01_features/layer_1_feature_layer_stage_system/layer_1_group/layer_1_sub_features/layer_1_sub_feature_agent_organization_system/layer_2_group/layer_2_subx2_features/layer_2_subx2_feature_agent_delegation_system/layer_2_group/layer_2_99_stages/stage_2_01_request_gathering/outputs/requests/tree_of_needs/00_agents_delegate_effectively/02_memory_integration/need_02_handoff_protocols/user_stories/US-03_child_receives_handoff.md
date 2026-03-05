---
resource_id: "4725496e-e335-44c3-af7d-a20a7bedfd60"
resource_type: "output"
resource_name: "US-03_child_receives_handoff"
---
# US-3: Child entity receives handoff from parent

**Need**: [Handoff Protocols](../README.md)

---

**As a** user who creates a new child entity (sub-feature) and expects the AI to understand why it exists,
**I want** the child entity to have an incoming handoff document explaining its purpose and expectations,
**So that** the AI working on the child entity knows its role in the broader hierarchy without me re-explaining the parent context.

<!-- section_id: "c3ea30c2-9498-49d7-aa9d-363f5a075940" -->
### What Happens

1. User creates a new sub-feature entity (e.g., "create a memory system sub-feature")
2. Parent entity manager creates a handoff document for the child
3. Handoff document explains: why the child was created, what is expected, and scope boundaries
4. When the AI starts working on the child entity, it reads the handoff document first
5. Child entity agent understands its purpose without reading the parent's full context

<!-- section_id: "42dcaeb8-f1ad-44bb-8801-8da7814ac331" -->
### Acceptance Criteria

- Incoming handoff document exists and is under 50 lines with clear scope and expectations
- Child entity agent understands its purpose after reading the handoff alone
- User does not need to re-explain the parent project's context to the child agent
