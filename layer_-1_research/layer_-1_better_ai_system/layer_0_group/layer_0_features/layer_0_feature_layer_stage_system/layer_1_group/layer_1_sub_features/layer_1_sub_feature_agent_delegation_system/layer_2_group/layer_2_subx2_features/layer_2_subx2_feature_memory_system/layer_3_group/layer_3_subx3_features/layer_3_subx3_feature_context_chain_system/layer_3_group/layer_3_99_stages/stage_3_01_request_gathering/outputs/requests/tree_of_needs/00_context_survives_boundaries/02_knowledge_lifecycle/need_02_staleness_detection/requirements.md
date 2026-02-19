# Need: Staleness Detection

**Branch**: [02_knowledge_lifecycle](../)
**Question**: "How do we know when knowledge files are outdated?"
**Version**: 1.0.0

---

## Definition

A mechanism to detect when distilled knowledge files (Tier 2) have drifted from their source stage outputs (Tier 3). Staleness = the source has changed but the summary hasn't been updated.

---

## Why This Matters

- A stale knowledge file is worse than no knowledge file — it gives agents false confidence
- Stage outputs evolve (new research, revised designs) but knowledge files don't auto-update
- Without detection, staleness is invisible until an agent acts on wrong information

---

## Requirements

### Detection Mechanism
- MUST compare knowledge file timestamps against referenced stage output timestamps
- MUST flag knowledge files whose sources have been modified since last consolidation
- SHOULD detect content drift (source changed substantially, not just minor edits)
- SHOULD integrate into chain-validate skill

### Reporting
- MUST produce a human-readable staleness report
- MUST list: which knowledge file, which source, how stale (time delta)
- SHOULD suggest whether re-consolidation is needed (minor vs major drift)

---

## Acceptance Criteria

- [ ] Staleness check runs and produces a report
- [ ] Stale knowledge files are identified with their source references
- [ ] Report is actionable (developer knows what to update)
- [ ] Integrates with existing validation tooling

---

## User Stories

See [user_stories.md](./user_stories.md)
