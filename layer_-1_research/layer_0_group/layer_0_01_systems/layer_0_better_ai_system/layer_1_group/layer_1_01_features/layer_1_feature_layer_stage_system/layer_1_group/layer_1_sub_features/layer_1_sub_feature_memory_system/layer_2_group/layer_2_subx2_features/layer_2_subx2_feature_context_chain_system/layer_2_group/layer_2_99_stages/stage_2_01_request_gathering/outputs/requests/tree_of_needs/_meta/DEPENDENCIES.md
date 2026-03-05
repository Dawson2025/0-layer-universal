---
resource_id: "d4c459a7-9c2b-4393-b1a9-3f486d0f1017"
resource_type: "output"
resource_name: "DEPENDENCIES"
---
# Need Dependencies

How needs relate to and depend on each other.

---

## Structure: DAG (Not Strict Tree)

While called "Tree of Needs," the structure is a **Directed Acyclic Graph (DAG)**. Currently no shared needs, but the structure supports them.

---

## Dependency Types

| Type | Symbol | Meaning |
|------|--------|---------|
| **Enables** | `→` | Must be satisfied before the other can work |
| **Enhances** | `~>` | Makes the other more effective (not required) |
| **Related** | `<->` | Share concepts, should be considered together |

---

## Cross-Branch Dependencies

### 01_knowledge_organization → 02_knowledge_lifecycle
- `consolidation_process` needs `three_tier_architecture` (must know tiers before distilling between them)
- `consolidation_process` needs `reference_format` (references from knowledge → stage outputs)
- `staleness_detection` needs `reference_format` (must parse references to check sources)

### 01_knowledge_organization → 03_knowledge_retrieval
- `scored_retrieval` needs `three_tier_architecture` (scores content across tiers)
- `chain_validation` needs `knowledge_graph` (validates against the graph)

### 02_knowledge_lifecycle → 03_knowledge_retrieval
- `chain_validation` ~> `staleness_detection` (staleness is one dimension of chain health)

---

## Intra-Branch Dependencies

### 01_knowledge_organization (internal)
```
three_tier_architecture
        │
        ├──→ knowledge_graph (graph represents relationships between tiered entities)
        │
        └──→ reference_format (references connect tiers)
```

### 02_knowledge_lifecycle (internal)
```
consolidation_process
        │
        └──~> staleness_detection (staleness = consolidation hasn't happened recently enough)
```

### 03_knowledge_retrieval (internal)
```
scored_retrieval <-> chain_validation (related but independent)
```

---

## Implementation Priority

Based on dependencies:

### Phase 1: Foundation (01_knowledge_organization)
1. `need_01_three_tier_architecture` — define tier boundaries
2. `need_03_reference_format` — define how tiers reference each other
3. `need_02_knowledge_graph` — formalize entity relationships

### Phase 2: Lifecycle (02_knowledge_lifecycle)
4. `need_01_consolidation_process` — distill research into knowledge
5. `need_02_staleness_detection` — detect drift

### Phase 3: Retrieval (03_knowledge_retrieval)
6. `need_02_chain_validation` — validate against graph
7. `need_01_scored_retrieval` — rank context by relevance
