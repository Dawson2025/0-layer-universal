---
resource_id: "2e5fd3c1-cd7d-4e24-85fc-015429d49713"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Chain Validation Enhancement

**Branch**: [03_knowledge_retrieval](../)
**Question**: "Is the context chain intact, and are all references valid?"
**Version**: 1.0.0

---

<!-- section_id: "e3264b7a-3d57-4fe6-97a4-b9bbd0f61ba1" -->
## Definition

Upgrade the existing `chain-validate` skill to validate against the knowledge graph (need_02_knowledge_graph). Currently validates file existence; should validate typed relationships, detect broken references, and flag staleness.

---

<!-- section_id: "78aefbe8-83af-4fa3-9c88-9ca68aa02b58" -->
## Why This Matters

- Current validation only checks "does this file exist?" -- misses relationship integrity
- Broken cross-references silently fail (agent follows link to nothing)
- With a knowledge graph, validation can check the entire relationship web, not just individual files

---

<!-- section_id: "2d06c889-8afe-4a33-b055-4d0e3918c584" -->
## Acceptance Criteria

- [ ] Validation runs against the knowledge graph
- [ ] Broken edges are detected and reported
- [ ] Cross-tier references are checked
- [ ] Unified report covers integrity + validity + staleness
- [ ] Integrates with existing chain-validate skill

---

<!-- section_id: "454e914c-48e0-4cdc-9272-a3cff461f2ce" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

<!-- section_id: "4c4aa00e-72ce-4e8f-9a84-9994adbab1c4" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.
