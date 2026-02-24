# Need 03: Auto-Discovery of Update Protocols

**Branch**: 03_knowledge_retrieval
**Status**: new (2026-02-22)
**Priority**: High

---

## Definition

> Agents automatically discover and follow context chain update protocols when modifying `.0agnostic/` content, without the user providing specific instructions or file paths.

---

## Why This Matters

The context chain system has a complete update protocol (`agnostic_update_protocol.md`) that describes the full propagation chain:

```
.0agnostic/ content → 0AGNOSTIC.md references → agnostic-sync.sh → CLAUDE.md → agent reads it
```

**But the protocol itself lives in cold context** — no auto-loaded file references it. A fresh agent won't know it exists unless:
1. They follow the Context Traversal Rule (read `.0agnostic/02_rules/`)
2. They discover and read the protocol file

This creates a systemic failure: agents modify `.0agnostic/` but don't update `0AGNOSTIC.md`, breaking the propagation chain and orphaning content.

**Research evidence**: Discovery gap audit (`stage_3_02_research/outputs/by_topic/05_discovery/discovery_gap_audit.md`) found that `agnostic_update_protocol`, `user-level-sync.sh`, and the propagation chain concept are all absent from hot context.

---

## Acceptance Criteria

- [ ] A fresh agent modifying `.0agnostic/` content automatically knows to update `0AGNOSTIC.md`
- [ ] A fresh agent knows about `user-level-sync.sh` without reading MEMORY.md
- [ ] The propagation chain is described in at least one hot-context file per AI tool
- [ ] Commits with orphaned `.0agnostic/` content are either blocked or warned about before commit
- [ ] Stage report and `0INDEX.md` update expectations are discoverable in hot context
- [ ] The solution works across all AI tool adapters (Claude Code, Cursor, Gemini CLI, Codex)

---

## Research References

| Document | Location | Relevance |
|----------|----------|-----------|
| Discovery gap audit | `stage_3_02_research/outputs/by_topic/05_discovery/discovery_gap_audit.md` | Primary evidence |
| Skill discovery chain test | `stage_3_07_testing/outputs/test_skill_discovery_chain.md` | Proves propagation works when content IS referenced |
| agnostic_update_protocol | `.0agnostic/02_rules/static/agnostic_update_protocol.md` | The protocol that needs to be discoverable |
| Multi-avenue redundancy | `stage_3_02_research/outputs/by_topic/04_design/0agnostic_system/multi_avenue_redundancy.md` | Avenue web design context |

---

## Scope Boundaries

**In scope**:
- Making critical update protocols auto-discoverable
- Tool-specific enforcement mechanisms (hooks, rules, etc.)
- Promoting critical cold-context rules to warm/hot context

**Out of scope**:
- Redesigning the .0agnostic/ system (it works — the problem is discovery, not structure)
- Implementing scored retrieval (need_01) or chain validation (need_02) — those are separate needs
- Knowledge graph formalization (Branch 01)

---

## Relationship to Other Needs

| Need | Relationship |
|------|-------------|
| need_01_scored_retrieval | **Independent** — scored retrieval is about choosing WHAT to load; auto-discovery is about ensuring PROTOCOLS are loaded |
| need_02_chain_validation | **Synergistic** — chain validation could check that hot context references critical rules |
| Branch 02 need_02_staleness_detection | **Related** — orphaned content is a staleness problem |
