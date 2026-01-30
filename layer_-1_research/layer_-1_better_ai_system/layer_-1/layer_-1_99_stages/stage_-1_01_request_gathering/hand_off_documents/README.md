# Hand Off Documents

This directory manages context transfer between stages.

## Structure

```
hand_off_documents/
├── README.md           # This file
├── incoming/           # Documents received from previous stage
│   └── README.md       # Incoming context specifications
└── outgoing/           # Documents prepared for next stage
    └── README.md       # Outgoing context specifications
```

## Stage Context

| Direction | Stage | Description |
|-----------|-------|-------------|
| **Incoming From** | (Project Initiation) | Initial project scope and goals |
| **Outgoing To** | stage_-1_02_research | Documented requests and requirements |

## Handoff Flow

```
┌─────────────────────┐
│ Project Initiation  │
│ (External/Manual)   │
└──────────┬──────────┘
           │
           ▼
┌──────────────────────────────────────┐
│  incoming/                           │
│  - Initial scope                     │
│  - Stakeholder input                 │
│  - Problem statements                │
└──────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│  stage_-1_01_request_gathering       │
│  (THIS STAGE)                        │
│  - Document requests                 │
│  - Define requirements               │
│  - Create specifications             │
└──────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│  outgoing/                           │
│  - All requests documented           │
│  - Requirements consolidated         │
│  - Dependencies mapped               │
│  - Open questions for research       │
└──────────────────────────────────────┘
           │
           ▼
┌─────────────────────┐
│ stage_-1_02_research│
│ (NEXT STAGE)        │
└─────────────────────┘
```

## Document Naming Convention

```
incoming/
  YYYYMMDD_from_<source>_<description>.md

outgoing/
  YYYYMMDD_to_<destination>_<description>.md
```

Examples:
- `incoming/20260125_from_initiation_project_scope.md`
- `outgoing/20260126_to_research_handoff.md`
