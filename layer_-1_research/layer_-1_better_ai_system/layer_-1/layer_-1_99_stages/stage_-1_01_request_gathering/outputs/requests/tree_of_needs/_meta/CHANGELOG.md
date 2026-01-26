# Changelog: Tree of Needs

All notable changes to the Tree of Needs structure.

Format based on [Keep a Changelog](https://keepachangelog.com/).

---

## [1.4.0] - 2026-01-26

### Changed
- **Structure is now a DAG** (Directed Acyclic Graph), not strict tree
  - Some needs can have multiple parents (shared needs)
  - `multimodal` now belongs to BOTH 01_capable AND 05_engaging
  - Primary location: 05_engaging/need_01_multimodal
  - Cross-reference: 01_capable/need_04_multimodal → points to primary
- Updated documentation to explain DAG structure
- Added ⟷ symbol to indicate shared needs

### Added
- Shared needs documentation in DEPENDENCIES.md
- Cross-reference requirements.md pattern for shared needs

---

## [1.3.0] - 2026-01-26

### Added
- New branch: `05_engaging` - "Is working with AI enjoyable?"
  - Focuses on engagement, interactivity, and user experience
  - Contains needs related to making AI collaboration enjoyable

### Moved
- `need_04_multimodal` moved from 01_capable to 05_engaging (as need_01_multimodal)
  - Better fit: multimodal is about engagement, not core capability
  - Updated version to 1.1.0

### Changed
- 01_capable branch now has 3 needs (was 4)
- New 05_engaging branch has 1 need
- Total branches increased to 5 (was 4)
- Total needs remains 15
- Updated tree structure diagrams

---

## [1.2.0] - 2026-01-26

### Added
- `need_04_multimodal` in 01_capable branch
  - Voice input support (speech-to-text via Vibe Typer)
  - Voice output support (text-to-speech)
  - Visual output support (diagrams, charts)
  - Rich interaction (mixed modes, interactive elements)

- `need_05_cross_platform` in 02_continuous branch
  - Works across macOS, Linux, Windows, WSL
  - Configuration portability between machines
  - Single-command bootstrap on new machines
  - Machine-specific adaptations

### Changed
- 01_capable branch now has 4 needs (was 3)
- 02_continuous branch now has 5 needs (was 4)
- Total needs increased to 15 (was 13)
- Updated all structure documentation

---

## [1.1.0] - 2026-01-26

### Added
- `need_04_evolvable` in 02_continuous branch
  - Captures requirement that system must evolve with AI technology
  - Concrete expression of Principle P1 (Future-Proof)
  - Requirements for technology abstraction, modular architecture, forward compatibility

### Changed
- 02_continuous branch now has 4 needs (was 3)
- Total needs increased to 13 (was 12)
- Updated DEPENDENCIES.md with evolvable need relationships
- Updated implementation priority (now 13 items)

---

## [1.0.0] - 2026-01-26

### Added
- Initial Tree of Needs structure
- Root need: `00_seamless_ai_collaboration`
- Four branches: `01_capable`, `02_continuous`, `03_trustworthy`, `04_observable`
- 12 needs total (3 per branch)

#### 01_capable branch
- `need_01_persistent_knowledge` - Hierarchical system prompts, referenced resources
- `need_02_scalable_context` - Agent delegation, progressive disclosure
- `need_03_discoverable` - Layer-stage structure, registries, self-describing prompts

#### 02_continuous branch
- `need_01_tool_portable` - Agnostic source of truth, tool-specific derivations
- `need_02_session_resilient` - Handoff documents, cross-tool continuity
- `need_03_failure_recoverable` - Idempotent setup, rollback capability

#### 03_trustworthy branch
- `need_01_rule_compliant` - Rule hierarchy, conflict resolution, rule registry
- `need_02_predictable` - Consistent behavior, version tracking
- `need_03_bounded` - Scope definitions, permission model

#### 04_observable branch
- `need_01_transparent` - State visibility, decision transparency
- `need_02_debuggable` - Validation suite, error diagnosis
- `need_03_auditable` - Change tracking, audit trails

### Integrated
- Consolidated from 8 original requests (request_01 through request_08)
- Legacy request content integrated into appropriate needs
- Legacy folders removed after integration

### Meta
- Added `_meta/EXTENSION_GUIDE.md` - How to extend the structure
- Added `_meta/DEPENDENCIES.md` - Need dependency map
- Added `_meta/CHANGELOG.md` - This file
- Added `_meta/VERSION.md` - Versioning policy

---

## Template for Future Entries

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New needs, branches, or features

### Changed
- Modifications to existing needs

### Deprecated
- Needs marked for future removal

### Removed
- Needs removed from the tree

### Fixed
- Corrections to requirements or structure

### Security
- Security-related changes (if applicable)
```

---

## Version History Summary

| Version | Date | Summary |
|---------|------|---------|
| 1.4.0 | 2026-01-26 | Converted to DAG - multimodal shared between capable & engaging |
| 1.3.0 | 2026-01-26 | Added 05_engaging branch, moved multimodal there |
| 1.2.0 | 2026-01-26 | Added multimodal + cross_platform (15 needs total) |
| 1.1.0 | 2026-01-26 | Added need_04_evolvable (13 needs total) |
| 1.0.0 | 2026-01-26 | Initial release with 4 branches, 12 needs |
