---
resource_id: "fff53527-996a-42aa-98fb-6e8712177051"
resource_type: "output"
resource_name: "09_rag_and_knowledge_graphs"
---
# RAG and Knowledge Graph Memory Systems

## Overview

Retrieval-Augmented Generation (RAG) and knowledge graphs as memory architectures for AI agents. These represent the most widely deployed forms of external memory in production systems.

---

## 1. RAG as Memory

### Core Concept
RAG augments LLM generation with retrieved external knowledge, effectively giving the model access to a vast external memory without modifying its parameters.

### Architecture
```
Query → Retriever (search external store) → Retrieved documents → LLM (generate with context)
```

### Components
1. **Document Store**: External knowledge base (vector DB, document DB)
2. **Embedding Model**: Converts text to dense vector representations
3. **Retriever**: Finds relevant documents via similarity search
4. **Generator**: LLM that produces output conditioned on retrieved context

### As Memory System
| Memory Property | RAG Implementation |
|-----------------|-------------------|
| Storage | Vector embeddings in external database |
| Encoding | Chunking + embedding model |
| Retrieval | Semantic similarity search (cosine, dot product) |
| Capacity | Theoretically unlimited (external storage) |
| Persistence | Persistent in database |
| Update | Re-embed modified documents |

### Limitations as Memory
- Flat structure: no hierarchy or organization
- Retrieval based on surface similarity, not deep understanding
- No temporal reasoning (unless explicitly indexed)
- Susceptible to semantic drift (lexically similar but semantically irrelevant results)
- No built-in consolidation or forgetting

---

## 2. Agentic RAG

### Evolution from Traditional RAG
Traditional RAG uses static, linear retrieval pipelines. Agentic RAG embeds autonomous AI agents into the RAG pipeline for dynamic, adaptive memory access.

### Key Capabilities
- **Reflection**: Agent evaluates retrieval quality and re-queries if insufficient
- **Planning**: Agent decomposes complex queries into sub-queries
- **Tool use**: Agent selects appropriate retrieval tools per sub-query
- **Multi-agent collaboration**: Specialized agents for different knowledge domains

### Architecture Patterns
1. **Single-agent RAG**: One agent manages retrieval + generation
2. **Multi-agent RAG**: Specialized retriever agents + generator agent
3. **Hierarchical RAG**: Manager agent delegates to domain-specific retriever agents

### As Memory System
- More intelligent memory access than vanilla RAG
- Self-correcting retrieval (checks and refines results)
- Multi-strategy retrieval (vector search, keyword, graph traversal)
- Adaptive: chooses retrieval strategy based on query type

---

## 3. Knowledge Graph Memory

### Core Concept
Structured representation of entities and their relationships, enabling symbolic reasoning and precise querying.

### Structure
```
(Entity A) --[Relationship]--> (Entity B)
  |                              |
[Attributes]                [Attributes]
```

### As Memory System
| Memory Property | Knowledge Graph Implementation |
|-----------------|-------------------------------|
| Storage | Graph database (Neo4j, Amazon Neptune, etc.) |
| Encoding | Entity extraction + relationship identification |
| Retrieval | Graph traversal, SPARQL/Cypher queries |
| Capacity | Scales with graph size |
| Reasoning | Multi-hop relationship queries |
| Update | Add/modify/delete nodes and edges |

### Advantages Over Vector-Based Memory
- **Explicit relationships**: Not just similarity but typed connections
- **Multi-hop reasoning**: "Who is the manager of the person who wrote document X?"
- **Interpretability**: Graph structure is human-readable
- **Precise queries**: Exact entity and relationship matching
- **Temporal**: Edges can have temporal attributes

### Challenges
- Construction cost: Entity/relationship extraction is expensive and error-prone
- Schema rigidity: Pre-defined relationship types may not cover all cases
- Scalability: Large graphs become slow to traverse
- Maintenance: Keeping graph current as knowledge changes

---

## 4. Graph RAG (Graph-Based Retrieval-Augmented Generation)

### Core Concept
Extends RAG by using knowledge graphs as the retrieval source instead of (or alongside) vector stores.

### Architecture
```
Query → Graph Query Builder → Knowledge Graph Traversal → Subgraph Extraction → LLM Generation
```

### Key Approaches
- **Microsoft GraphRAG**: Community detection + hierarchical summarization of knowledge graphs
- **LightRAG**: Lightweight graph-based RAG
- **HippoRAG**: Inspired by hippocampal memory indexing theory

### As Memory System
- Combines structured reasoning (graph) with generative capability (LLM)
- Multi-hop memory access across entity relationships
- Community-level summarization for high-level understanding
- Entity-level detail for specific queries

---

## 5. Hybrid Memory: Vector + Graph

### Why Hybrid?
Neither vector stores nor knowledge graphs alone cover all memory needs:
- **Vector stores**: Good for semantic similarity, poor for precise relationships
- **Knowledge graphs**: Good for structured queries, poor for fuzzy semantic matching

### Implementations
- **Mem0**: Hybrid datastore combining vector + graph + key-value
- **Zep**: Temporal knowledge graph with embedding-based augmentation
- **LangChain**: ConversationKGMemory (graph) + VectorStoreRetrieverMemory (vector) can be combined

### Architecture
```
Query → [Vector Retrieval] + [Graph Traversal] → Fusion/Ranking → Context for LLM
```

---

## 6. Storage Backend Technologies

### Vector Databases
| Database | Key Features |
|----------|-------------|
| **Pinecone** | Managed, serverless, metadata filtering |
| **Weaviate** | Open-source, hybrid search (vector + keyword) |
| **ChromaDB** | Lightweight, in-process, good for prototyping |
| **FAISS** | Facebook's library, high-performance, in-memory |
| **Qdrant** | Open-source, filtering, payload storage |
| **Milvus** | Distributed, scalable, GPU-accelerated |
| **pgvector** | PostgreSQL extension, familiar SQL interface |

### Graph Databases
| Database | Key Features |
|----------|-------------|
| **Neo4j** | Most popular, Cypher query language, mature ecosystem |
| **Amazon Neptune** | Managed, supports property graph + RDF |
| **ArangoDB** | Multi-model (graph + document + KV) |
| **TigerGraph** | Distributed, GSQL query language |

### Hybrid / Multi-Model
| Database | Key Features |
|----------|-------------|
| **LanceDB** | Embedded, multimodal, used by CrewAI |
| **Mem0 stack** | Vector (any) + Graph (Neo4j/Neptune) + KV |

---

## 7. Retrieval Strategies

### Dense Retrieval
- Encode query and documents as dense vectors
- Cosine similarity or dot product for matching
- Best for semantic/conceptual matching
- Models: sentence-transformers, OpenAI embeddings, Cohere embed

### Sparse Retrieval
- Traditional keyword-based matching (BM25, TF-IDF)
- Best for exact term matching
- Complement to dense retrieval

### Hybrid Retrieval
- Combine dense + sparse scores
- Reciprocal rank fusion or weighted combination
- Best overall performance in most benchmarks

### Re-Ranking
- Initial broad retrieval → re-rank with cross-encoder model
- Better precision at cost of additional compute
- Models: Cohere rerank, cross-encoder models

### Graph-Augmented Retrieval
- Vector retrieval to find seed entities → graph traversal for context
- Combines similarity matching with relational reasoning

---

## 8. Neurological Comparison

For a deep comparison of how vector embeddings and knowledge graphs map to human brain neurology — including how the brain encodes different relationship types (cause-effect, category membership, part-whole, temporal sequences) through distinct neural circuits rather than explicit labels — see `15_vectors_graphs_and_neurology.md`.

---

## Sources

- [Agentic Retrieval-Augmented Generation Survey (arXiv:2501.09136)](https://arxiv.org/abs/2501.09136)
- [Graph Retrieval-Augmented Generation Survey (ACM TOIS)](https://dl.acm.org/doi/10.1145/3777378)
- [RAG Survey (GitHub)](https://github.com/hymie122/RAG-Survey)
- [Retrieval-Augmented Generation (Wikipedia)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
- [Graph-Based Agentic RAG Survey (Academia)](https://www.academia.edu/144313989/)
- [Mem0: Building Production-Ready AI Agents (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413)
