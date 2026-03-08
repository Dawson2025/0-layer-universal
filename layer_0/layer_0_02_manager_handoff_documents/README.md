---
resource_id: "ff8653f0-f4f3-4d00-ae93-2372b42c44af"
resource_type: "readme_document"
resource_name: "README"
---
# Hand Off Documents

Four-directional communication hub for the Root Manager.

<!-- section_id: "cf07968c-b031-447e-9ac4-7462a90edea9" -->
## Structure

```
hand_off_documents/
├── incoming/
│   ├── from_above/      ← User requests and instructions
│   └── from_below/      ← Results/escalations from layers
└── outgoing/
    ├── to_above/        ← Results reported to user
    └── to_below/        ← Tasks delegated to layers
```

<!-- section_id: "25085e88-a5fe-4a2d-b425-af8fc79739cc" -->
## Flow

```
        USER
          │
          ▼
   incoming/from_above/     ← User writes requests here
          │
          ▼
    [Root Manager]          ← Processes, delegates
          │
          ▼
   outgoing/to_below/       ← Tasks to layer_0, layer_1, layer_-1_research
          │
          ▼
      [Layers]              ← Execute work
          │
          ▼
   incoming/from_below/     ← Results return here
          │
          ▼
    [Root Manager]          ← Aggregates results
          │
          ▼
   outgoing/to_above/       ← Final results to user
```

<!-- section_id: "d4b2a024-1f29-46a7-b9d7-0c169dda0e18" -->
## Document Format

```markdown
# YYYYMMDD_brief_description.md

## Metadata
| Field | Value |
|-------|-------|
| From | [source path] |
| To | [target path] |
| Date | YYYY-MM-DD |
| Type | task / result / escalation |

## Content
[Description of handoff]

## Context
[Background information]

## Expected Output (for tasks)
[What receiver should produce]

## Actual Output (for results)
[What was produced]

## Next Steps
[What happens next]
```

<!-- section_id: "8fb9deaa-67f5-4989-b807-3331d0a33dd3" -->
## Usage

- **from_above**: Root manager checks this on session start for user requests
- **from_below**: Root manager checks this for completed work from layers
- **to_above**: Root manager writes final results here for user
- **to_below**: Root manager writes delegated tasks here for layers to pick up
