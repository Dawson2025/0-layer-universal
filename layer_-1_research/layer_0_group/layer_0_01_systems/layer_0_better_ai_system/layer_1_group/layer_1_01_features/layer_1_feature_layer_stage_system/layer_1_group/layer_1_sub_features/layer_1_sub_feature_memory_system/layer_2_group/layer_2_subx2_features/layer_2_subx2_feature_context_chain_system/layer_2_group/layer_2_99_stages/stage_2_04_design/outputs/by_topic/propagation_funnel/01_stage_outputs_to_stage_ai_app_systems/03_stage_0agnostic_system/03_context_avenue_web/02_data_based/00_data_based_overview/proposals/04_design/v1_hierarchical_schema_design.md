---
resource_id: "01dfacf5-0ae5-41c5-b78f-30007989e4b7"
resource_type: "output"
resource_name: "v1_hierarchical_schema_design"
---
# Context Avenue Database Schema — Proposal v1

<!-- section_id: "e8823eea-5a57-486b-9802-18f4595aca38" -->
## Improved Hierarchical Architecture

This proposal redesigns the avenues.db schema to support multi-dimensional analysis of context delivery approaches.

---

<!-- section_id: "7a0622f1-593f-4bc0-a690-4cc3f8156cef" -->
## Natural Hierarchy

```
CONTEXT AVENUES (ROOT)
│
├── FILE_BASED_AVENUES
│   ├── Integration Summaries
│   ├── Skills
│   ├── Auto Memory
│   └── [others]
│
└── DATA_BASED_AVENUES
    │
    ├── KNOWLEDGE_GRAPH
    │   ├── Supported Operations
    │   │   ├── Query
    │   │   │   ├── Operation Speeds
    │   │   │   │   ├── Retrieval Speed
    │   │   │   │   └── Read Speed
    │   │   │   └── Operation Qualities
    │   │   │       └── [Quality metrics]
    │   │   ├── Insert
    │   │   ├── Update
    │   │   └── Delete
    │   │
    │   └── Capability Rankings
    │       ├── Reasoning (rank: X)
    │       ├── Comprehensiveness (rank: X)
    │       ├── Cost (rank: X)
    │       └── Scalability (rank: X)
    │
    ├── SHIMI (Semantic Hierarchical Memory Index)
    │   ├── Supported Operations
    │   │   ├── Query
    │   │   │   ├── Operation Speeds
    │   │   │   └── Operation Qualities
    │   │   ├── Insert
    │   │   ├── Update
    │   │   └── Delete
    │   │
    │   └── Capability Rankings
    │       ├── Reasoning (rank: X)
    │       ├── Comprehensiveness (rank: X)
    │       ├── Cost (rank: X)
    │       └── Scalability (rank: X)
    │
    ├── RELATIONAL_TABLES
    │   ├── Supported Operations
    │   │   ├── Query
    │   │   │   ├── Operation Speeds
    │   │   │   └── Operation Qualities
    │   │   ├── Insert
    │   │   ├── Update
    │   │   └── Delete
    │   │
    │   └── Capability Rankings
    │       ├── Reasoning (rank: X)
    │       ├── Comprehensiveness (rank: X)
    │       ├── Cost (rank: X)
    │       └── Scalability (rank: X)
    │
    └── VECTOR_DATABASES
        ├── Supported Operations
        │   ├── Query
        │   │   ├── Operation Speeds
        │   │   └── Operation Qualities
        │   ├── Insert
        │   ├── Update
        │   └── Delete
        │
        └── Capability Rankings
            ├── Reasoning (rank: X)
            ├── Comprehensiveness (rank: X)
            ├── Cost (rank: X)
            └── Scalability (rank: X)
```

---

<!-- section_id: "21dbf75e-c114-4821-91eb-b83366bba85c" -->
## Natural Relationships 

<!-- section_id: "32b21f20-0661-4b9b-a1a3-101347765340" -->
### Vertical Relationships (Drill-down)

- **Avenues** → **Operations** → **Speeds/Qualities**
- Allows deep exploration of specific avenue capabilities

<!-- section_id: "de5344d8-90e1-46ee-97fe-9d54bdc63855" -->
### Horizontal Relationships (Comparison)

- Compare avenues across capabilities
- Compare operations across speeds
- Aggregate rankings by capability type

---

<!-- section_id: "f42d3a63-a2e3-4cee-8709-189d629cb4ee" -->
## Key Design Insights

1. **Hierarchical Navigation**: Drill down from avenue types → operations → speeds/qualities
2. **Cross-sectional Views**: Slice by capability (e.g., "rank all data-based avenues by reasoning")
3. **Operation-centric Analysis**: "Which avenues support fast Query operations?"
4. **Capability Comparison**: "Compare Vector Databases vs Relational Tables on Cost vs Scalability"

---

<!-- section_id: "76dcf36c-4ec1-44ab-8a60-72aaaa6e953d" -->
## Supported Query Patterns

This schema naturally supports:

- **By Reasoning**: "Show me data-based avenues ranked by reasoning capability (highest → lowest)"
- **By Usage**: "Show me avenues ranked by usage frequency (highest → lowest)"
- **By Cost**: "Show me avenues ranked by cost (lowest → highest)"
- **By Scalability**: "Show me avenues ranked by scalability (highest → lowest)"
- **By Operation Type**: "What are the fastest Query operations across all avenues?"
- **By Capability**: "How do all data-based avenue types compare on this specific capability?"

---

<!-- section_id: "911a4344-78b2-448b-b64c-2a636c264b5e" -->
## Data Types Included

<!-- section_id: "44c0a39e-bd55-469c-a9f0-3a515102ad78" -->
### Avenue Categories

- File-based avenues (Integration Summaries, Skills, Auto Memory)
- Data-based avenues (Knowledge Graph, SHIMI, Relational Tables, Vector Databases)

<!-- section_id: "0179927c-c888-48ae-bf4f-18e966fb4f8d" -->
### Operations

- Query
- Insert
- Update
- Delete
- [Extensible for other operations]

<!-- section_id: "71270dbe-3608-48d0-bfda-9f2538b58d36" -->
### Operation Metrics

- **Operation Speeds**: Retrieval Speed, Read Speed, Write Speed, [others]
- **Operation Qualities**: [Quality metrics for operations]

<!-- section_id: "7f68daf2-ece9-4f43-ba74-0cd59bdec9c0" -->
### Core Capabilities

- Reasoning
- Comprehensiveness
- Cost
- Scalability
- [Extensible for other capabilities]

---

<!-- section_id: "992aba3f-e8cd-4fe7-8341-84b51dc529cd" -->
## Next Steps

This proposal is ready for:

1. Schema implementation in SQL
2. Data migration from current avenues.db
3. View creation for different sorted perspectives
4. Testing and validation
