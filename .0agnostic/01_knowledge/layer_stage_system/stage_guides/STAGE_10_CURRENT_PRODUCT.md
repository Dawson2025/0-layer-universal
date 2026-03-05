---
resource_id: "162d78c9-175b-4e90-922a-7f50672c171d"
resource_type: "knowledge"
resource_name: "STAGE_10_CURRENT_PRODUCT"
---
# Stage 10: Current Product — Universal Guide

## Purpose

Hold the final deliverables that are ready for active use. This is the **release stage** — the work product in its current, usable form.

## What This Stage IS

The current product stage:
- Contains the final, validated versions of all deliverables
- Serves as the "latest release" — what consumers of this entity should use
- May include deployment instructions, usage guides, or integration notes
- Is the canonical "what's live right now" location

## What This Stage IS NOT

The current product stage does NOT:
- **Contain work in progress** — that lives in stages 01-09
- **Contain historical versions** — that's stage 11 (archives)
- **Contain development artifacts** — runbooks, test scripts, research stay in their stages
- **Contain unvalidated work** — only artifacts that passed testing (stage 07) and criticism (stage 08)

This is **the shelf**, not **the workshop**.

## Methodology

```
outputs/
├── README.md                    <- What's here, how to use it, version info
├── [deliverable files]          <- The actual products
└── stage_report.md
```

### Content Rules

- Only move artifacts here after they pass testing (stage 07) and criticism (stage 08)
- Include a README.md explaining what's available and how to use it
- Version information should be clear (date, version number, or reference to changelog)
- Previous versions go to stage 11 (archives) before updating

### What "Current Product" Means Per Entity Type

| Entity Type | Typical Current Product |
|-------------|----------------------|
| Research feature | Validated findings, proven architectures, working prototypes |
| Production feature | Released code, active configuration, deployed artifacts |
| Knowledge entity | Finalized documentation, approved standards |
| Tool/script | Working, tested version of the tool |

## Inputs

- **Stage 07 outputs** — confirmed that artifacts pass tests
- **Stage 08 outputs** — confirmed quality is acceptable
- **Stage 09 outputs** — all fixes applied
- **Stage 06 outputs** — the built artifacts themselves

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Current deliverables | `outputs/` | Final versions of all products |
| Usage guide | `outputs/README.md` | How to use what's here |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is up to date when:
1. All deliverables reflect the latest validated state
2. README.md accurately describes contents
3. Previous versions have been archived (stage 11)
4. No unvalidated work is present

## Exit Protocol

1. Update `outputs/stage_report.md` when products change
2. If archiving: move previous version to stage 11 before replacing

## Common Patterns

- **Promotion-based**: Content is promoted here from earlier stages, not created here
- **Versioned snapshots**: Each update creates a new version (old goes to archives)
- **Consumer-facing**: Write README.md for the person using the product, not the person who built it

## Anti-Patterns

- Placing work-in-progress here (it must pass 07+08 first)
- Not archiving previous versions before updating
- Missing README.md (consumers can't find what they need)
- Mixing deliverables with development artifacts
