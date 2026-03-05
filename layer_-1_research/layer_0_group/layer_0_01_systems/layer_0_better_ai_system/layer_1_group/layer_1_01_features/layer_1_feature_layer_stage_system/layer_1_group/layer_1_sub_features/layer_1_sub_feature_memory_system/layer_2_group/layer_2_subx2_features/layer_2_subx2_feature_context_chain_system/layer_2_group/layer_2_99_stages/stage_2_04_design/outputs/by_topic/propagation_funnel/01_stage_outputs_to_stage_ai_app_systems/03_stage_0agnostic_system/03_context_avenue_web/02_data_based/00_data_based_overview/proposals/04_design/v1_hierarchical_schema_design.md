---
resource_id: "01dfacf5-0ae5-41c5-b78f-30007989e4b7"
resource_type: "output"
resource_name: "v1_hierarchical_schema_design"
---
# Context Avenue Database Schema — Proposal v1

## Improved Hierarchical Architecture

This proposal redesigns the avenues.db schema to support multi-dimensional analysis of context delivery approaches.

---

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

## Natural Relationships 

### Vertical Relationships (Drill-down)

- **Avenues** → **Operations** → **Speeds/Qualities**
- Allows deep exploration of specific avenue capabilities

### Horizontal Relationships (Comparison)

- Compare avenues across capabilities
- Compare operations across speeds
- Aggregate rankings by capability type

---

## Key Design Insights

1. **Hierarchical Navigation**: Drill down from avenue types → operations → speeds/qualities
2. **Cross-sectional Views**: Slice by capability (e.g., "rank all data-based avenues by reasoning")
3. **Operation-centric Analysis**: "Which avenues support fast Query operations?"
4. **Capability Comparison**: "Compare Vector Databases vs Relational Tables on Cost vs Scalability"

---

## Supported Query Patterns

This schema naturally supports:

- **By Reasoning**: "Show me data-based avenues ranked by reasoning capability (highest → lowest)"
- **By Usage**: "Show me avenues ranked by usage frequency (highest → lowest)"
- **By Cost**: "Show me avenues ranked by cost (lowest → highest)"
- **By Scalability**: "Show me avenues ranked by scalability (highest → lowest)"
- **By Operation Type**: "What are the fastest Query operations across all avenues?"
- **By Capability**: "How do all data-based avenue types compare on this specific capability?"

---

## Data Types Included

### Avenue Categories

- File-based avenues (Integration Summaries, Skills, Auto Memory)
- Data-based avenues (Knowledge Graph, SHIMI, Relational Tables, Vector Databases)

### Operations

- Query
- Insert
- Update
- Delete
- [Extensible for other operations]

### Operation Metrics

- **Operation Speeds**: Retrieval Speed, Read Speed, Write Speed, [others]
- **Operation Qualities**: [Quality metrics for operations]

### Core Capabilities

- Reasoning
- Comprehensiveness
- Cost
- Scalability
- [Extensible for other capabilities]

---

## Next Steps

This proposal is ready for:

1. Schema implementation in SQL
2. Data migration from current avenues.db
3. View creation for different sorted perspectives
4. Testing and validation
