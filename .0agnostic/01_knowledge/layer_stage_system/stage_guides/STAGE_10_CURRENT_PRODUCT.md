---
resource_id: "162d78c9-175b-4e90-922a-7f50672c171d"
resource_type: "knowledge"
resource_name: "STAGE_10_CURRENT_PRODUCT"
---
# Stage 10: Current Product — Universal Guide

<!-- section_id: "724a2bbb-cf2d-4501-88ed-edcfc4ea3f04" -->
## Purpose

Hold the final deliverables that are ready for active use. This is the **release stage** — the work product in its current, usable form.

<!-- section_id: "cc42ffbc-d241-4178-835d-edef3896c3b3" -->
## What This Stage IS

The current product stage:
- Contains the final, validated versions of all deliverables
- Serves as the "latest release" — what consumers of this entity should use
- May include deployment instructions, usage guides, or integration notes
- Is the canonical "what's live right now" location

<!-- section_id: "ecde535f-1d11-4b02-8247-5c35dbb761e9" -->
## What This Stage IS NOT

The current product stage does NOT:
- **Contain work in progress** — that lives in stages 01-09
- **Contain historical versions** — that's stage 11 (archives)
- **Contain development artifacts** — runbooks, test scripts, research stay in their stages
- **Contain unvalidated work** — only artifacts that passed testing (stage 07) and criticism (stage 08)

This is **the shelf**, not **the workshop**.

<!-- section_id: "6c66490d-4682-418e-811f-8f5e2e2abda6" -->
## Methodology

```
outputs/
├── README.md                    <- What's here, how to use it, version info
├── [deliverable files]          <- The actual products
└── stage_report.md
```

<!-- section_id: "fd311c59-69a6-4b9b-bda3-d7b18073cf76" -->
### Content Rules

- Only move artifacts here after they pass testing (stage 07) and criticism (stage 08)
- Include a README.md explaining what's available and how to use it
- Version information should be clear (date, version number, or reference to changelog)
- Previous versions go to stage 11 (archives) before updating

<!-- section_id: "14662965-085e-4840-805c-e32da53715a9" -->
### What "Current Product" Means Per Entity Type

| Entity Type | Typical Current Product |
|-------------|----------------------|
| Research feature | Validated findings, proven architectures, working prototypes |
| Production feature | Released code, active configuration, deployed artifacts |
| Knowledge entity | Finalized documentation, approved standards |
| Tool/script | Working, tested version of the tool |

<!-- section_id: "05025bb9-67a5-4d29-b507-c238e2f54985" -->
## Inputs

- **Stage 07 outputs** — confirmed that artifacts pass tests
- **Stage 08 outputs** — confirmed quality is acceptable
- **Stage 09 outputs** — all fixes applied
- **Stage 06 outputs** — the built artifacts themselves

<!-- section_id: "07d4e601-cccb-406f-be11-36d5d4ed442b" -->
## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Current deliverables | `outputs/` | Final versions of all products |
| Usage guide | `outputs/README.md` | How to use what's here |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

<!-- section_id: "f244b629-7c75-4b8d-9e13-fed86da94054" -->
## Success Criteria

This stage is up to date when:
1. All deliverables reflect the latest validated state
2. README.md accurately describes contents
3. Previous versions have been archived (stage 11)
4. No unvalidated work is present

<!-- section_id: "756c00c3-b544-404e-b315-a16db2b42e15" -->
## Exit Protocol

1. Update `outputs/stage_report.md` when products change
2. If archiving: move previous version to stage 11 before replacing

<!-- section_id: "d19284f7-fa03-4155-ac81-51e51a3cd374" -->
## Common Patterns

- **Promotion-based**: Content is promoted here from earlier stages, not created here
- **Versioned snapshots**: Each update creates a new version (old goes to archives)
- **Consumer-facing**: Write README.md for the person using the product, not the person who built it

<!-- section_id: "46f4c8e8-c685-4559-b52f-868016a3cf70" -->
## Anti-Patterns

- Placing work-in-progress here (it must pass 07+08 first)
- Not archiving previous versions before updating
- Missing README.md (consumers can't find what they need)
- Mixing deliverables with development artifacts
