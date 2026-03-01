# Need: Chain Validation Enhancement

**Branch**: [03_knowledge_retrieval](../)
**Question**: "Is the context chain intact, and are all references valid?"
**Version**: 1.0.0

---

## Definition

Upgrade the existing `chain-validate` skill to validate against the knowledge graph (need_02_knowledge_graph). Currently validates file existence; should validate typed relationships, detect broken references, and flag staleness.

---

## Why This Matters

- Current validation only checks "does this file exist?" -- misses relationship integrity
- Broken cross-references silently fail (agent follows link to nothing)
- With a knowledge graph, validation can check the entire relationship web, not just individual files

---

## Acceptance Criteria

- [ ] Validation runs against the knowledge graph
- [ ] Broken edges are detected and reported
- [ ] Cross-tier references are checked
- [ ] Unified report covers integrity + validity + staleness
- [ ] Integrates with existing chain-validate skill

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

## User Stories

See [user_stories/](./user_stories/) for individual stories.
