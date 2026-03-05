---
resource_id: "195fe9fa-3ff6-4ace-833f-dd22f1e7d129"
resource_type: "knowledge"
resource_name: "STAGE_11_ARCHIVES"
---
# Stage 11: Archives — Universal Guide

## Purpose

Store historical versions, deprecated content, and records of past work. This is the **history stage** — preserve what came before for reference.

## What This Stage IS

The archives stage:
- Holds previous versions of deliverables (before they were superseded in stage 10)
- Preserves deprecated approaches, designs, and implementations
- Maintains a changelog documenting the evolution of the entity
- Provides reference material for understanding why things changed

## What This Stage IS NOT

The archives stage does NOT:
- **Contain active work** — that's stages 01-09
- **Contain current deliverables** — that's stage 10
- **Delete or discard content** — archives preserve, never destroy
- **Organize or clean up old content** — archives store as-is for historical accuracy

This is the **library**, not **the recycle bin**.

## Methodology

```
outputs/
├── CHANGELOG.md                  <- Timeline of what changed and when
├── v1/                           <- First version (complete snapshot or delta)
├── v2/                           <- Second version
├── deprecated/                   <- Approaches that were tried and abandoned
│   └── [topic]/
│       └── README.md             <- Why this was deprecated
└── stage_report.md
```

### Changelog Format

Each entry includes:
- **Date**: When the change happened
- **Version**: Version identifier
- **What changed**: Summary of changes
- **Why**: Rationale for the change
- **Replaced by**: Link to current version (stage 10) or newer archive

### Archive Rules

- Archive BEFORE updating stage 10 (preserve the old version first)
- Include a README.md in deprecated directories explaining why the approach was abandoned
- Don't reorganize archived content — it should reflect the state at the time

## Inputs

- **Stage 10 outputs** — current product being replaced (moves here before update)
- **Stage 04 outputs** — deprecated design decisions
- **Stage 08 outputs** — critique that led to changes

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Historical versions | `outputs/v{N}/` | Snapshot or delta of previous versions |
| Deprecated content | `outputs/deprecated/` | Abandoned approaches with rationale |
| Changelog | `outputs/CHANGELOG.md` | Timeline of evolution |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is up to date when:
1. All superseded versions are archived before replacement
2. CHANGELOG.md reflects the complete history
3. Deprecated content has rationale documented
4. Archives are findable and organized chronologically

## Common Patterns

- **Version snapshots**: Copy the complete state before each major update
- **Delta archives**: For large entities, store only what changed
- **Deprecation notices**: Always explain why something was abandoned — future agents need this context

## Anti-Patterns

- Deleting old versions instead of archiving
- Archiving without changelog entries (lost context)
- Reorganizing archived content (breaks historical accuracy)
- Not archiving before updating stage 10 (version history lost)
