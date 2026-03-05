---
resource_id: "d4c459a7-9c2b-4393-b1a9-3f486d0f1017"
resource_type: "output"
resource_name: "DEPENDENCIES"
---
# Need Dependencies

How needs relate to and depend on each other.

---

<!-- section_id: "cc5f7a2a-7a43-4164-8b10-b9fd3c52e6a5" -->
## Structure: DAG (Not Strict Tree)

While called "Tree of Needs," the structure is a **Directed Acyclic Graph (DAG)**. Currently no shared needs, but the structure supports them.

---

<!-- section_id: "83e1524e-b21b-4f71-9ab4-c7a02a310e03" -->
## Dependency Types

| Type | Symbol | Meaning |
|------|--------|---------|
| **Enables** | `→` | Must be satisfied before the other can work |
| **Enhances** | `~>` | Makes the other more effective (not required) |
| **Related** | `<->` | Share concepts, should be considered together |

---

<!-- section_id: "d9b95191-d511-48bd-b470-a5b73c4bb84f" -->
## Cross-Branch Dependencies

<!-- section_id: "f5a78b8e-a230-4a65-b2be-6e0ef51a64c1" -->
### 01_knowledge_organization → 02_knowledge_lifecycle
- `consolidation_process` needs `three_tier_architecture` (must know tiers before distilling between them)
- `consolidation_process` needs `reference_format` (references from knowledge → stage outputs)
- `staleness_detection` needs `reference_format` (must parse references to check sources)

<!-- section_id: "6ed73fa6-04dc-40f3-844e-918579c5b43b" -->
### 01_knowledge_organization → 03_knowledge_retrieval
- `scored_retrieval` needs `three_tier_architecture` (scores content across tiers)
- `chain_validation` needs `knowledge_graph` (validates against the graph)

<!-- section_id: "9ed70671-a10c-4531-87da-3fc805590809" -->
### 02_knowledge_lifecycle → 03_knowledge_retrieval
- `chain_validation` ~> `staleness_detection` (staleness is one dimension of chain health)

---

<!-- section_id: "a17576a6-db9f-4735-94ad-b6563b625d9e" -->
## Intra-Branch Dependencies

<!-- section_id: "fc8f4858-5be2-4144-8cfc-98b76d00411a" -->
### 01_knowledge_organization (internal)
```
three_tier_architecture
        │
        ├──→ knowledge_graph (graph represents relationships between tiered entities)
        │
        └──→ reference_format (references connect tiers)
```

<!-- section_id: "21dba1bf-cca8-44ce-95ff-08f02d476275" -->
### 02_knowledge_lifecycle (internal)
```
consolidation_process
        │
        └──~> staleness_detection (staleness = consolidation hasn't happened recently enough)
```

<!-- section_id: "50dacd62-ec1d-4194-b48d-afccb30029e6" -->
### 03_knowledge_retrieval (internal)
```
scored_retrieval <-> chain_validation (related but independent)
```

---

<!-- section_id: "cf12bda0-6ec1-4bd1-80f5-e9c0cea1fc43" -->
## Implementation Priority

Based on dependencies:

<!-- section_id: "4b0263e2-b17d-4f77-ba33-f99d27a751de" -->
### Phase 1: Foundation (01_knowledge_organization)
1. `need_01_three_tier_architecture` — define tier boundaries
2. `need_03_reference_format` — define how tiers reference each other
3. `need_02_knowledge_graph` — formalize entity relationships

<!-- section_id: "864e7e95-00c2-4db8-91db-03829b6c341d" -->
### Phase 2: Lifecycle (02_knowledge_lifecycle)
4. `need_01_consolidation_process` — distill research into knowledge
5. `need_02_staleness_detection` — detect drift

<!-- section_id: "3cbebc7d-96f7-453c-b644-0b14bf819765" -->
### Phase 3: Retrieval (03_knowledge_retrieval)
6. `need_02_chain_validation` — validate against graph
7. `need_01_scored_retrieval` — rank context by relevance
