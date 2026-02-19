# Need: Chain Validation Enhancement

**Branch**: [03_knowledge_retrieval](../)
**Question**: "Is the context chain intact, and are all references valid?"
**Version**: 1.0.0

---

## Definition

Upgrade the existing `chain-validate` skill to validate against the knowledge graph (need_02_knowledge_graph). Currently validates file existence; should validate typed relationships, detect broken references, and flag staleness.

---

## Why This Matters

- Current validation only checks "does this file exist?" — misses relationship integrity
- Broken cross-references silently fail (agent follows link to nothing)
- With a knowledge graph, validation can check the entire relationship web, not just individual files

---

## Requirements

### Graph-Based Validation
- MUST validate every node in the knowledge graph against the file system
- MUST validate every edge (source and target both exist and are correctly typed)
- MUST report: orphaned nodes, missing nodes, broken edges, type mismatches

### Reference Validation
- MUST validate cross-tier references (knowledge file → stage output)
- MUST detect moved, renamed, or deleted targets
- SHOULD detect changed section headers (reference points to section that was renamed)

### Staleness Integration
- SHOULD integrate staleness detection (need_02_staleness_detection) into validation report
- SHOULD produce a unified health report: chain integrity + reference validity + staleness

---

## Acceptance Criteria

- [ ] Validation runs against the knowledge graph
- [ ] Broken edges are detected and reported
- [ ] Cross-tier references are checked
- [ ] Unified report covers integrity + validity + staleness
- [ ] Integrates with existing chain-validate skill

---

## User Stories

See [user_stories.md](./user_stories.md)
