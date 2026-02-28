# Rationale: Why Hierarchical/DAG Structure?

This document explains why the Tree of Needs uses a hierarchical DAG (Directed Acyclic Graph) structure, supported by research on how AI systems process organized information.

---

## TL;DR

Hierarchical structures help LLMs perform **10-30% better** on complex reasoning tasks. Our DAG structure aligns with research-backed best practices for AI knowledge organization.

---

## The Research Question

> Does hierarchical structure in knowledge organization help large language models (LLMs) and AI assistants perform better?

**Answer: Yes, substantially.**

---

## Key Research Findings

### Performance Improvements

| Metric | Improvement |
|--------|-------------|
| Retrieval accuracy | Up to **12%** better top-1 accuracy |
| Search efficiency | **3-4x faster** through intelligent pruning |
| Reasoning tasks | **10-30%** improvement on complex reasoning |
| QuALITY benchmark | **20%** absolute accuracy improvement (RAPTOR + GPT-4) |
| Multi-hop reasoning | **>90% micro-F1** when grounded in knowledge graphs |

### Why Hierarchy Works for LLMs

#### 1. Logarithmic vs Linear Search
- **Flat structure**: Compare query against every item (O(n))
- **Hierarchical**: Navigate tree, progressively narrow search space (O(log n))

#### 2. Multi-Level Abstraction
- LLMs understand both "the forest and the trees"
- High-level summaries for overview, drill down for details
- Different queries need different levels of detail

#### 3. Activates Latent Reasoning Capabilities
- Explicit hierarchy provides "scaffolding" that triggers formal reasoning
- Study showed **3x improvement** (31.5% → 97.3%) when task structure was made explicit
- LLMs have dormant reasoning capabilities that hierarchy activates

#### 4. Context Window Efficiency
- Don't need to load everything at once
- Progressive disclosure: load details on demand
- Reduces "context rot" (performance degradation with long inputs)

#### 5. Reduces Hallucination
- Grounding in structured knowledge reduces fabrication
- Explicit relationships provide verifiable paths
- Answers can be traced back through the hierarchy

---

## Tree vs Graph vs DAG

### Comparison

| Structure | Description | Pros | Cons |
|-----------|-------------|------|------|
| **Tree** | Each node has exactly 1 parent | Simple, efficient O(log n) | Forces artificial single-parent decisions |
| **DAG** | Nodes can have multiple parents, no cycles | Reflects reality, flexible | Slightly more complex |
| **General Graph** | Any connections, can have cycles | Maximum flexibility | Can be confusing, cycles cause issues |

### Why We Chose DAG

Research supports DAGs for knowledge organization because:

1. **Real requirements cross-cut concerns**
   - `multimodal` genuinely belongs to both "capable" AND "engaging"
   - Forcing single-parent loses important relationships

2. **Maintains tree benefits**
   - Still has single root
   - Still flows "downward" (acyclic)
   - Still enables efficient navigation

3. **Better matches human cognition**
   - Humans naturally see concepts belonging to multiple categories
   - AI performs better when structure matches natural organization

---

## How Our Structure Aligns with Best Practices

| Best Practice | Our Implementation |
|---------------|-------------------|
| **Single root** | `00_seamless_ai_collaboration` |
| **Clear branches** | 5 branches answering distinct questions |
| **Multiple abstraction levels** | Root → Branch → Need → Requirements |
| **Shared needs (DAG)** | `multimodal` in both capable & engaging |
| **Self-describing structure** | CLAUDE.md cascade, READMEs at each level |
| **Progressive disclosure** | Navigate down to details as needed |
| **Explicit relationships** | DEPENDENCIES.md maps connections |
| **Consistent terminology** | Standardized naming, ⟷ for shared needs |

---

## Frameworks Referenced

### RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)
- Recursively clusters and summarizes text into tree structure
- Enables retrieval at different abstraction levels
- 20% improvement on QuALITY benchmark

### LATTICE (LLM-Guided Hierarchical Navigation)
- LLM actively navigates semantic hierarchy
- Logarithmic search complexity
- 9% improvement in Recall@100

### Knowledge Graphs + LLMs
- Explicit structure reduces hallucination
- Multi-hop reasoning follows graph edges
- Verifiable reasoning paths

---

## Implications for This Project

### For AI Consuming This Structure

1. **Start at root** - Understand the overall goal
2. **Navigate to relevant branch** - Find the right concern
3. **Drill into specific needs** - Get detailed requirements
4. **Follow cross-references** - Understand shared needs
5. **Check dependencies** - Know implementation order

### For Humans Maintaining This Structure

1. **Keep hierarchy clear** - Don't nest too deep
2. **Use shared needs sparingly** - Only when genuinely multi-parent
3. **Maintain READMEs** - Self-describing at every level
4. **Update DEPENDENCIES.md** - Keep relationships current
5. **Follow EXTENSION_GUIDE.md** - Consistent patterns

---

## Sources

Research compiled via Perplexity (2026-01-26), drawing from:

- HiBench benchmark (hierarchical reasoning evaluation)
- RAPTOR framework (recursive tree retrieval)
- LATTICE framework (LLM-guided navigation)
- Anthropic's context engineering guidelines
- Knowledge graph + LLM integration studies
- Task-Method-Knowledge framework research

Key citations:
- arxiv.org/abs/2401.18059 (RAPTOR)
- arxiv.org/html/2510.13217v1 (LATTICE)
- arxiv.org/html/2503.00912v1 (HiBench)
- anthropic.com/engineering/effective-context-engineering-for-ai-agents

---

## Version

**1.0.0** (2026-01-26) - Initial rationale document
