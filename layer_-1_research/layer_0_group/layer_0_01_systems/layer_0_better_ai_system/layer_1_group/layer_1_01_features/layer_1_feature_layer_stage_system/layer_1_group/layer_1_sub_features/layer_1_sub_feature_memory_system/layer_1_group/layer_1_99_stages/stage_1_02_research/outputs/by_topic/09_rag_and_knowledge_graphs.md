---
resource_id: "fff53527-996a-42aa-98fb-6e8712177051"
resource_type: "output"
resource_name: "09_rag_and_knowledge_graphs"
---
# RAG and Knowledge Graph Memory Systems

<!-- section_id: "015a3018-14e2-4e74-9842-89a449739cb3" -->
## Overview

Retrieval-Augmented Generation (RAG) and knowledge graphs as memory architectures for AI agents. These represent the most widely deployed forms of external memory in production systems.

---

<!-- section_id: "f5d84d03-47a5-4ed6-9f44-a684c91906bc" -->
## 1. RAG as Memory

<!-- section_id: "d010d966-fb10-488d-8e04-17d4f7f88bda" -->
### Core Concept
RAG augments LLM generation with retrieved external knowledge, effectively giving the model access to a vast external memory without modifying its parameters.

<!-- section_id: "a23f0f94-1de0-42c8-bbae-bf5bc8616e4a" -->
### Architecture
```
Query → Retriever (search external store) → Retrieved documents → LLM (generate with context)
```

<!-- section_id: "13a25112-99e0-43af-93e3-d0fc77d671fe" -->
### Components
1. **Document Store**: External knowledge base (vector DB, document DB)
2. **Embedding Model**: Converts text to dense vector representations
3. **Retriever**: Finds relevant documents via similarity search
4. **Generator**: LLM that produces output conditioned on retrieved context

<!-- section_id: "e25aab63-0b82-4020-b7d5-09d40d79e4c0" -->
### As Memory System
| Memory Property | RAG Implementation |
|-----------------|-------------------|
| Storage | Vector embeddings in external database |
| Encoding | Chunking + embedding model |
| Retrieval | Semantic similarity search (cosine, dot product) |
| Capacity | Theoretically unlimited (external storage) |
| Persistence | Persistent in database |
| Update | Re-embed modified documents |

<!-- section_id: "7b74df05-d39d-4fe9-92d7-41392ccf3d18" -->
### Limitations as Memory
- Flat structure: no hierarchy or organization
- Retrieval based on surface similarity, not deep understanding
- No temporal reasoning (unless explicitly indexed)
- Susceptible to semantic drift (lexically similar but semantically irrelevant results)
- No built-in consolidation or forgetting

---

<!-- section_id: "5e8804fe-ba4f-4180-80f8-bac0cf1b46a9" -->
## 2. Agentic RAG

<!-- section_id: "45634f80-c362-497a-82a2-48636455b4a6" -->
### Evolution from Traditional RAG
Traditional RAG uses static, linear retrieval pipelines. Agentic RAG embeds autonomous AI agents into the RAG pipeline for dynamic, adaptive memory access.

<!-- section_id: "2dd581ee-0c22-416f-898a-8979679bf222" -->
### Key Capabilities
- **Reflection**: Agent evaluates retrieval quality and re-queries if insufficient
- **Planning**: Agent decomposes complex queries into sub-queries
- **Tool use**: Agent selects appropriate retrieval tools per sub-query
- **Multi-agent collaboration**: Specialized agents for different knowledge domains

<!-- section_id: "a9231120-fc2b-4502-a8df-4c52314b2863" -->
### Architecture Patterns
1. **Single-agent RAG**: One agent manages retrieval + generation
2. **Multi-agent RAG**: Specialized retriever agents + generator agent
3. **Hierarchical RAG**: Manager agent delegates to domain-specific retriever agents

<!-- section_id: "8d71fd11-c61f-44a5-8d1c-796ee915ebe5" -->
### As Memory System
- More intelligent memory access than vanilla RAG
- Self-correcting retrieval (checks and refines results)
- Multi-strategy retrieval (vector search, keyword, graph traversal)
- Adaptive: chooses retrieval strategy based on query type

---

<!-- section_id: "a6dcab09-e5db-4ae2-bf62-255f87d7e371" -->
## 3. Knowledge Graph Memory

<!-- section_id: "ad669f5c-d3d9-459e-99e9-9c80e92eba07" -->
### Core Concept
Structured representation of entities and their relationships, enabling symbolic reasoning and precise querying.

<!-- section_id: "7c4e95c2-abc6-4a01-8365-1b1c3bd380be" -->
### Structure
```
(Entity A) --[Relationship]--> (Entity B)
  |                              |
[Attributes]                [Attributes]
```

<!-- section_id: "12e9648c-8acf-4055-bb3b-830aca45fcbe" -->
### As Memory System
| Memory Property | Knowledge Graph Implementation |
|-----------------|-------------------------------|
| Storage | Graph database (Neo4j, Amazon Neptune, etc.) |
| Encoding | Entity extraction + relationship identification |
| Retrieval | Graph traversal, SPARQL/Cypher queries |
| Capacity | Scales with graph size |
| Reasoning | Multi-hop relationship queries |
| Update | Add/modify/delete nodes and edges |

<!-- section_id: "b9dd30d5-42ab-4fb2-beb0-335766fc359f" -->
### Advantages Over Vector-Based Memory
- **Explicit relationships**: Not just similarity but typed connections
- **Multi-hop reasoning**: "Who is the manager of the person who wrote document X?"
- **Interpretability**: Graph structure is human-readable
- **Precise queries**: Exact entity and relationship matching
- **Temporal**: Edges can have temporal attributes

<!-- section_id: "4cced5a1-d088-4277-9820-baf464e0cc55" -->
### Challenges
- Construction cost: Entity/relationship extraction is expensive and error-prone
- Schema rigidity: Pre-defined relationship types may not cover all cases
- Scalability: Large graphs become slow to traverse
- Maintenance: Keeping graph current as knowledge changes

---

<!-- section_id: "b5d18831-1173-48d4-b29e-63fa0f70fd5b" -->
## 4. Graph RAG (Graph-Based Retrieval-Augmented Generation)

<!-- section_id: "ba628369-7528-4200-b365-f7ca4d32fc95" -->
### Core Concept
Extends RAG by using knowledge graphs as the retrieval source instead of (or alongside) vector stores.

<!-- section_id: "d52f8e5a-4eeb-4420-990e-b02fdf5d35a6" -->
### Architecture
```
Query → Graph Query Builder → Knowledge Graph Traversal → Subgraph Extraction → LLM Generation
```

<!-- section_id: "d095c3e5-5e4a-4c91-b7ab-92d52d28e274" -->
### Key Approaches
- **Microsoft GraphRAG**: Community detection + hierarchical summarization of knowledge graphs
- **LightRAG**: Lightweight graph-based RAG
- **HippoRAG**: Inspired by hippocampal memory indexing theory

<!-- section_id: "594749ae-8bde-40e4-8af6-b0a4cbc1a96b" -->
### As Memory System
- Combines structured reasoning (graph) with generative capability (LLM)
- Multi-hop memory access across entity relationships
- Community-level summarization for high-level understanding
- Entity-level detail for specific queries

---

<!-- section_id: "e5c6e03a-1f9b-43ba-9d6c-aa4ce9c97c6d" -->
## 5. Hybrid Memory: Vector + Graph

<!-- section_id: "790d06e2-7d14-49c8-ad82-9c7a9abc66aa" -->
### Why Hybrid?
Neither vector stores nor knowledge graphs alone cover all memory needs:
- **Vector stores**: Good for semantic similarity, poor for precise relationships
- **Knowledge graphs**: Good for structured queries, poor for fuzzy semantic matching

<!-- section_id: "65b1c978-0ade-4ef2-90ab-eb187eaf5b52" -->
### Implementations
- **Mem0**: Hybrid datastore combining vector + graph + key-value
- **Zep**: Temporal knowledge graph with embedding-based augmentation
- **LangChain**: ConversationKGMemory (graph) + VectorStoreRetrieverMemory (vector) can be combined

<!-- section_id: "700e8835-efee-41e9-a1ab-099ca78df961" -->
### Architecture
```
Query → [Vector Retrieval] + [Graph Traversal] → Fusion/Ranking → Context for LLM
```

---

<!-- section_id: "97a80187-5c67-41c4-9aee-272962da70b9" -->
## 6. Storage Backend Technologies

<!-- section_id: "1cf6fbfd-5c37-454c-91f4-e515ed474d28" -->
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

<!-- section_id: "dc359706-adce-4b05-a0b3-463226cbe868" -->
### Graph Databases
| Database | Key Features |
|----------|-------------|
| **Neo4j** | Most popular, Cypher query language, mature ecosystem |
| **Amazon Neptune** | Managed, supports property graph + RDF |
| **ArangoDB** | Multi-model (graph + document + KV) |
| **TigerGraph** | Distributed, GSQL query language |

<!-- section_id: "241df4d3-0007-477b-8d6f-2a2834fd760e" -->
### Hybrid / Multi-Model
| Database | Key Features |
|----------|-------------|
| **LanceDB** | Embedded, multimodal, used by CrewAI |
| **Mem0 stack** | Vector (any) + Graph (Neo4j/Neptune) + KV |

---

<!-- section_id: "63bf4f8a-96cb-4ab4-ae5f-637d2c449db6" -->
## 7. Retrieval Strategies

<!-- section_id: "749010de-60c1-44f4-b759-4051379afffc" -->
### Dense Retrieval
- Encode query and documents as dense vectors
- Cosine similarity or dot product for matching
- Best for semantic/conceptual matching
- Models: sentence-transformers, OpenAI embeddings, Cohere embed

<!-- section_id: "f74c0139-6d41-44fc-bfc9-8744e5c60b2f" -->
### Sparse Retrieval
- Traditional keyword-based matching (BM25, TF-IDF)
- Best for exact term matching
- Complement to dense retrieval

<!-- section_id: "8b0ab883-be5c-4c6e-88a2-b6e3bfe7daae" -->
### Hybrid Retrieval
- Combine dense + sparse scores
- Reciprocal rank fusion or weighted combination
- Best overall performance in most benchmarks

<!-- section_id: "76682196-1835-4b94-8ffc-0a1e5cedd678" -->
### Re-Ranking
- Initial broad retrieval → re-rank with cross-encoder model
- Better precision at cost of additional compute
- Models: Cohere rerank, cross-encoder models

<!-- section_id: "f4b98466-8745-4c9d-ae53-5252e948100c" -->
### Graph-Augmented Retrieval
- Vector retrieval to find seed entities → graph traversal for context
- Combines similarity matching with relational reasoning

---

<!-- section_id: "89ddee28-b5cb-49cc-aeed-0523ca294998" -->
## 8. Neurological Comparison

For a deep comparison of how vector embeddings and knowledge graphs map to human brain neurology — including how the brain encodes different relationship types (cause-effect, category membership, part-whole, temporal sequences) through distinct neural circuits rather than explicit labels — see `15_vectors_graphs_and_neurology.md`.

---

<!-- section_id: "226f719d-1ef5-4f49-b4bb-af4a984082cc" -->
## Sources

- [Agentic Retrieval-Augmented Generation Survey (arXiv:2501.09136)](https://arxiv.org/abs/2501.09136)
- [Graph Retrieval-Augmented Generation Survey (ACM TOIS)](https://dl.acm.org/doi/10.1145/3777378)
- [RAG Survey (GitHub)](https://github.com/hymie122/RAG-Survey)
- [Retrieval-Augmented Generation (Wikipedia)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
- [Graph-Based Agentic RAG Survey (Academia)](https://www.academia.edu/144313989/)
- [Mem0: Building Production-Ready AI Agents (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413)
