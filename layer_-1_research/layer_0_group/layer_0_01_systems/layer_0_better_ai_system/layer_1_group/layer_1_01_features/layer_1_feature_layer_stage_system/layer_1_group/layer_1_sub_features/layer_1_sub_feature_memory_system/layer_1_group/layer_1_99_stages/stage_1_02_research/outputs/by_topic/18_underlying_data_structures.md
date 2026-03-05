---
resource_id: "4007e213-a850-4b33-b863-61f159b1428b"
resource_type: "output"
resource_name: "18_underlying_data_structures"
---
# Underlying Data Structures for AI Agent Memory Systems

<!-- section_id: "bbe3aab6-bc0b-49c8-9c52-605e82c86a5d" -->
## Purpose

Memory types like "episodic," "semantic," "short-term," and "long-term" describe *what* is stored and *how long* it lasts. This document covers the **actual data structures** underneath — the technical building blocks that these memory types are implemented on top of.

The relationship: **Memory type** (episodic, semantic, etc.) is built on top of a **data structure** (vector store, key-value map, etc.), which is stored in a **storage backend** (database, file system, model weights, etc.).

---

<!-- section_id: "d0fe51d1-ea3a-493f-bfd3-969e561d61b9" -->
## 1. Raw Message List (Array / Queue)

<!-- section_id: "18109644-309a-46be-8731-4c89b34b53ca" -->
### What It Is
A simple ordered list of messages: `[msg1, msg2, msg3, ...]`. The most basic data structure possible — just an array that grows as the conversation continues.

<!-- section_id: "feb12108-240c-4a67-b8fd-f74865566c6b" -->
### How It Works
- Messages are appended in order
- The entire list is injected into the LLM's context window
- No processing, no transformation, no indexing
- Retrieval = "load everything"

<!-- section_id: "c289e5d8-2a11-498f-9abe-b69420293beb" -->
### Technical Details
- Data structure: Array, List, or Deque
- Storage: In-memory (session-scoped) or persisted to database rows
- Time complexity: O(1) append, O(n) to load everything
- Space: Grows linearly with conversation length

<!-- section_id: "07be3945-793b-48fe-b024-0c56ae2eac2b" -->
### Used By
- LangChain `ConversationBufferMemory`
- Any basic chatbot's conversation history
- Raw chat logs / transcripts

<!-- section_id: "f76d3ddc-f377-494c-8ecb-bf215ac9b420" -->
### Which Memory Types Use This
- **Short-term / working memory** (current conversation context)
- **Episodic memory** (raw session transcripts)

<!-- section_id: "0677a087-9dd7-454c-abc8-6c8ecb24b335" -->
### Strengths
- Zero information loss — every word preserved
- Simplest possible implementation
- No extraction errors

<!-- section_id: "4f8cf633-8cbc-4761-a9ce-24b01fa91851" -->
### Weaknesses
- Overflows context window in long conversations
- Cost grows linearly (every token loaded = money)
- No selectivity — loads irrelevant information alongside relevant

<!-- section_id: "fe21dbfa-a680-4610-b32a-d7caff7e7179" -->
### Brain Analogy
- Closest to **sensory memory buffer** — brief, unprocessed, everything captured before being selectively encoded

---

<!-- section_id: "0ab92792-ba7c-433c-b8d0-f9e5df5d3784" -->
## 2. Sliding Window (Circular Buffer / Bounded Array)

<!-- section_id: "bd461622-0e5a-419c-b197-48157a297019" -->
### What It Is
A fixed-size list that drops the oldest entries when full. Only the most recent K messages are kept.

<!-- section_id: "c3039506-7c54-4f2d-bdb1-a93592dc92b7" -->
### How It Works
- New messages push in at one end
- When the buffer reaches size K, the oldest message is evicted (FIFO — first in, first out)
- Only the window contents are injected into context

<!-- section_id: "ee23b6c2-8c87-49c7-b15e-74cbf86dac8f" -->
### Technical Details
- Data structure: Deque with maxlen, or circular buffer (ring buffer)
- Storage: In-memory
- Time complexity: O(1) append and evict, O(K) to load window
- Space: Fixed at K items regardless of conversation length

<!-- section_id: "3b135a10-ae39-45a4-9cd7-e3b332da9bde" -->
### Used By
- LangChain `ConversationBufferWindowMemory(k=N)`
- Any framework with `max_turns` or `max_tokens` parameter

<!-- section_id: "f812113e-c4a7-412e-9339-ea97394c66ac" -->
### Which Memory Types Use This
- **Short-term / working memory** with bounded capacity
- Mirrors Miller's Law (~7 items in human working memory)

<!-- section_id: "926fc556-90c3-4b60-a8c1-7a1b7534f78f" -->
### Strengths
- Fixed, predictable token cost
- Simple, no LLM calls needed for management
- Good for task-focused agents where only recent context matters

<!-- section_id: "af8da5f3-538e-430f-98fc-36dd31f80ef3" -->
### Weaknesses
- Hard boundary — information outside the window is completely gone (not summarized, just deleted)
- Users who reference something said 50 turns ago will get no recall
- No importance-based retention — an important early message is treated the same as trivial chatter

<!-- section_id: "0fe4a3b8-a7fe-4f04-bc10-a9aca47aab22" -->
### Brain Analogy
- Closest to **working memory** — limited capacity, recency-biased, items fall out when capacity is exceeded

---

<!-- section_id: "3455736d-c594-4fa1-b6d7-7fabade59bb6" -->
## 3. Key-Value Store (Hash Map / Dictionary)

<!-- section_id: "72750562-978a-42fc-aff6-65fabc28d0f7" -->
### What It Is
A lookup table mapping keys to values. The most common structure for entity memory.

```
{
  "Alice": "Senior engineer at Acme Corp, prefers Python, working on Project X",
  "Project X": "Due March 2026, uses React + FastAPI, Alice is lead",
  "user_preferences": "Dark mode, concise answers, no emojis"
}
```

<!-- section_id: "e5a533ac-3c5f-4cb8-9765-c463398532ec" -->
### How It Works
- Entities or topics are keys
- Values are text summaries, fact lists, or structured data
- Lookup is by exact key match (O(1))
- Values get updated/overwritten as new information arrives

<!-- section_id: "7c1a47f1-5e9f-454a-a464-6bb7ea44af81" -->
### Technical Details
- Data structure: Hash map / dictionary / associative array
- Storage: In-memory dict, Redis, SQLite, DynamoDB, or any KV store
- Time complexity: O(1) lookup, O(1) insert/update
- Space: Grows with number of distinct entities

<!-- section_id: "2e9c7196-a593-4dca-a41f-b4c8720c32f0" -->
### Used By
- LangChain `ConversationEntityMemory` with swappable store (in-memory, Redis, SQLite)
- Mem0's key-value component (alongside vector + graph)
- MemGPT/Letta core memory blocks (`human` block, `persona` block)
- User preference stores

<!-- section_id: "4977a71c-9bc3-4d14-b686-de616a6ce10d" -->
### Which Memory Types Use This
- **Entity memory** (per-entity fact storage)
- **Profile / persona memory** (user and agent identity)
- **Core memory** (always-in-context editable blocks)
- **Factual / semantic memory** (simple fact lookup)

<!-- section_id: "53b8fed1-48e5-403e-9f5e-385055377b64" -->
### Strengths
- Extremely fast lookup (O(1))
- Simple to implement and understand
- Human-readable and editable
- Easy to update specific entries without affecting others

<!-- section_id: "62a2a62b-319c-4e76-9671-809fd079e1ca" -->
### Weaknesses
- No similarity search — you must know the exact key
- No relationship modeling between entities (flat structure)
- Values can become stale or contradictory without maintenance
- Entity extraction (determining what keys to create) relies on LLM and can introduce errors

<!-- section_id: "cab66f74-98c1-4bab-b044-d1b74a71efd2" -->
### Brain Analogy
- Closest to **semantic memory for specific entities** — "I know that Alice is an engineer" without remembering when or how you learned it

---

<!-- section_id: "7e24685d-e1e2-465f-9aad-857fb19ef48a" -->
## 4. Vector Store (Embedding Database)

<!-- section_id: "a00971dd-8447-4064-b1ce-9f889e68f712" -->
### What It Is
A collection of dense vector representations (embeddings) with an index for similarity search. Covered in depth in `15_vectors_graphs_and_neurology.md`.

<!-- section_id: "795b3320-805c-47b7-9b8e-cb81d21158c9" -->
### How It Works
- Text chunks are converted to vectors (arrays of floats) by an embedding model
- Vectors are stored with their original text and metadata
- Retrieval = embed the query, find the N nearest vectors by cosine similarity or dot product

<!-- section_id: "abec7e83-a88a-4784-b531-2e3ff2034ddf" -->
### Technical Details
- Data structure: Arrays of float32/float16 vectors + approximate nearest neighbor (ANN) index (HNSW, IVF, etc.)
- Storage: Specialized vector databases (Pinecone, Qdrant, Weaviate, ChromaDB, FAISS, Milvus, pgvector)
- Time complexity: O(log n) to O(n) for search depending on index type; O(1) insert
- Space: ~1-4KB per vector (depends on dimensionality, typically 384-1536 dims)
- Vectors are opaque (not human-readable)

<!-- section_id: "32aecc4e-8067-43ca-944f-2bf327515d61" -->
### Used By
- RAG systems (the dominant AI memory pattern)
- LangChain `VectorStoreRetrieverMemory`
- Mem0's vector component
- CrewAI's LanceDB-backed memory

<!-- section_id: "a58a4ee7-7a12-41b6-b847-5427e1a3bd4d" -->
### Which Memory Types Use This
- **Long-term semantic memory** (large knowledge bases)
- **Episodic memory** (searchable interaction history)
- **Contextual memory** (finding relevant background context)

<!-- section_id: "c3691652-89ef-461a-a85d-9a93689a2d87" -->
### Strengths
- Scales to millions of memories
- Semantic search (finds conceptually related content, not just keyword matches)
- No need to know exact queries — fuzzy matching works

<!-- section_id: "81b2808f-8a31-44bc-bd22-216f40c24036" -->
### Weaknesses
- No relationship types (only "similar" / "not similar")
- No multi-hop reasoning
- Embedding quality determines retrieval quality
- Binary blobs — not human-readable, not git-friendly
- Model-specific — embeddings from one model can't be used with another

<!-- section_id: "1607bf1c-87f7-4f91-b0f5-907a398cefb3" -->
### Brain Analogy
- Loosely like **distributed representations** — similar concepts have overlapping neural activation patterns. But the brain does associative activation through learned pathways, not nearest-neighbor search.

<!-- section_id: "fc99d070-f3bb-4433-95aa-290911f49e05" -->
### Full Coverage
- See `15_vectors_graphs_and_neurology.md` → Sections 1 and 4 for deep comparison with knowledge graphs and neurology

---

<!-- section_id: "3700a390-c0f6-4d3d-bdb5-9b3c9c4f43ca" -->
## 5. Knowledge Graph (Graph Database)

<!-- section_id: "0bbc5257-bbf5-4361-979b-8c019f9e92de" -->
### What It Is
Entities as nodes, relationships as typed directed edges. Covered in depth in `15_vectors_graphs_and_neurology.md`.

<!-- section_id: "850c7743-ad4c-4847-a091-08500f8db219" -->
### How It Works
- Entities (nodes) have labels and properties
- Relationships (edges) have types, directions, and properties
- Retrieval = graph traversal via query languages (Cypher, SPARQL, Gremlin)

<!-- section_id: "af919387-dd05-4ac6-be59-f0a915324803" -->
### Technical Details
- Data structure: Adjacency lists or adjacency matrices with typed edges
- Storage: Graph databases (Neo4j, Amazon Neptune, ArangoDB, FalkorDB)
- Time complexity: O(V + E) for traversal; pattern matching varies
- Space: Nodes + edges + properties

<!-- section_id: "94ac5daa-6891-4e38-9915-568ecbe650ef" -->
### Used By
- Mem0 (graph component)
- Zep (temporal knowledge graph)
- LangChain `ConversationKGMemory`
- Microsoft GraphRAG

<!-- section_id: "8710052e-8434-4aea-b048-3c445178d54c" -->
### Which Memory Types Use This
- **Semantic / factual memory** (structured world knowledge)
- **Entity memory** (entity relationships)
- **Temporal memory** (event sequences with temporal edges)

<!-- section_id: "f1a8726d-0808-4b68-84dd-6c7587ca07a8" -->
### Strengths
- Explicit typed relationships (cause-effect, part-whole, etc.)
- Multi-hop reasoning ("who manages the person who wrote document X?")
- Human-readable and explainable
- Precise queries

<!-- section_id: "0bf70211-bb41-4b9e-81e6-d4faea387035" -->
### Weaknesses
- Expensive to build (entity/relationship extraction is error-prone)
- Schema must be designed upfront (or dynamically, which adds complexity)
- No fuzzy/semantic matching (can't find "similar" things, only connected things)
- Graph traversal can be slow on very large graphs

<!-- section_id: "65bf851c-62c8-4c52-b558-c6dcbb775956" -->
### Brain Analogy
- Closest to **semantic memory in temporal cortex** — structured, declarative knowledge with explicit relationships. See `15_vectors_graphs_and_neurology.md` for full comparison.

<!-- section_id: "242a21ca-2a5e-4b2e-8061-c8027c53a388" -->
### Full Coverage
- See `15_vectors_graphs_and_neurology.md` → Sections 2, 3, and 4
- See `09_rag_and_knowledge_graphs.md` → Sections 3-6

---

<!-- section_id: "50b703ba-9f71-4d3a-b720-03b17fe4b5cf" -->
## 6. LLM-Generated Summary (Compressed Text)

<!-- section_id: "6fe4b8f5-6c3e-46c7-86af-67aca0eb6366" -->
### What It Is
A single text string (or short document) that replaces a larger body of content. The LLM itself performs the compression by summarizing.

<!-- section_id: "c7a57006-c470-4530-9236-e7ad6bcb95ff" -->
### How It Works
- After N messages (or on a schedule), the LLM is asked: "Summarize this conversation so far"
- The summary replaces the raw messages in context
- Some implementations keep a hybrid: recent messages raw + older messages summarized
- Summaries can be recursive (summary of summaries)

<!-- section_id: "8e2b800c-1cfb-4d8d-8e38-e8bd882672bc" -->
### Technical Details
- Data structure: A single text string, periodically regenerated
- Storage: In-memory string, or persisted as a text file / database entry
- Time complexity: O(1) to load (it's just one string); O(n) to generate (LLM must read all content)
- Space: Roughly constant regardless of conversation length (summary stays a similar size)
- Requires an LLM call to produce — adds latency and cost

<!-- section_id: "7e957925-9c2a-46df-b39d-624b66bd3eee" -->
### Used By
- LangChain `ConversationSummaryMemory`
- LangChain `ConversationSummaryBufferMemory` (hybrid: summary + recent window)
- MemoryOS MTM segments (summarized topic clusters)
- Any system with "rolling summaries"

<!-- section_id: "ac2f460c-4326-4333-8fda-4c8fb4cf7ef6" -->
### Which Memory Types Use This
- **Long-term memory** (compressed history)
- **Medium-term memory** (summarized recent sessions)
- **Consolidated memory** (merging multiple sources)

<!-- section_id: "26eac4fa-16e0-4824-8c13-aa47cb046777" -->
### Strengths
- Bounded token cost regardless of conversation length
- Captures the gist of long interactions
- Human-readable output

<!-- section_id: "c2b9a23d-3069-41df-834d-61988b536fb6" -->
### Weaknesses
- **Lossy compression** — details are permanently lost
- **Summarization errors** — LLM can misrepresent, omit, or hallucinate during summarization
- **Compounds over time** — summary of a summary of a summary degrades quality
- Latency — requires an LLM call to produce
- Not suitable for exact-wording-matters contexts (legal, compliance)

<!-- section_id: "d55221ad-f433-47da-86c0-c57d809ecf95" -->
### Brain Analogy
- Closest to **memory consolidation** — the brain's progressive summarization where raw episodic memories gradually become abstract semantic knowledge, losing specific details but retaining the gist. Sleep replay compresses sequences similarly.

---

<!-- section_id: "48d9990a-5b8b-458e-ad94-8748e060196e" -->
## 7. Relational Database (SQL Tables)

<!-- section_id: "2649e97f-09c0-4258-a6cf-a192d1648f2f" -->
### What It Is
Structured tables with rows (records) and columns (attributes), queried via SQL.

```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    content TEXT,
    source VARCHAR(50),
    importance FLOAT,
    entity VARCHAR(100),
    memory_type VARCHAR(20)
);
```

<!-- section_id: "df889ef9-312d-4458-a530-93cd005bc763" -->
### How It Works
- Each memory is a row with structured attributes
- Columns provide indexable metadata (timestamp, importance, source, type)
- SQL queries for filtered retrieval: `SELECT * FROM memories WHERE entity='Alice' AND importance > 0.7 ORDER BY timestamp DESC`
- JOINs can connect related tables (memories → entities → relationships)

<!-- section_id: "f44f9303-2270-4242-9ea1-7fa04a7b097d" -->
### Technical Details
- Data structure: B-tree indexed tables
- Storage: PostgreSQL, SQLite, MySQL
- Time complexity: O(log n) for indexed queries, O(n) for full scans
- Space: Efficient for structured data with fixed schemas

<!-- section_id: "984975f3-777e-4afe-807d-82c42dfbd18a" -->
### Used By
- LangChain entity stores (SQLite option)
- Custom memory systems needing complex filtered queries
- Logging and audit trail systems
- Any production system that needs ACID transactions

<!-- section_id: "f5f6379e-d13a-4384-967a-3852c6fbe247" -->
### Which Memory Types Use This
- **Episodic memory** (timestamped event records)
- **Entity memory** (structured entity attributes)
- **Metadata-heavy memory** (when you need to query by importance, source, timestamp, etc.)

<!-- section_id: "23ae8990-86b0-4d10-8299-cff068d52d50" -->
### Strengths
- Rich querying (filter by any combination of attributes)
- ACID transactions (reliable, consistent)
- Mature tooling, widely understood
- Good for temporal queries (WHERE timestamp BETWEEN ...)

<!-- section_id: "c3bd1d53-0cd9-4654-80da-36a606f1596d" -->
### Weaknesses
- Fixed schema — adding new attributes requires migrations
- No semantic search (keyword only, unless combined with vector extension like pgvector)
- No relationship traversal (JOINs are flat, not graph-native)

<!-- section_id: "a48718ff-5276-46f1-908a-892d2b1de7ee" -->
### Brain Analogy
- Not a natural brain analog — the brain doesn't store information in tabular form. Closest to a **structured external memory aid** like a spreadsheet or ledger.

---

<!-- section_id: "a5be2460-a274-4608-9600-2fa8a072db24" -->
## 8. Document Store (JSON/BSON Documents)

<!-- section_id: "efba923f-e6f1-44c1-b695-c360aea5cda9" -->
### What It Is
A collection of self-contained documents with flexible schemas. Each memory is a JSON-like document that can have different fields.

```json
{
  "id": "mem_001",
  "content": "Alice prefers Python for backend work",
  "metadata": {
    "timestamp": "2026-02-17T10:30:00Z",
    "source": "conversation",
    "confidence": 0.9,
    "tags": ["preference", "technology", "Alice"]
  },
  "embedding": [0.82, -0.14, ...]
}
```

<!-- section_id: "791654bf-3a50-450f-81fb-135550d82188" -->
### How It Works
- Each memory is a self-contained document
- Documents in the same collection can have different fields (schema-flexible)
- Queries filter by any field or nested field
- Can combine with text search and (in some engines) vector search

<!-- section_id: "60253393-b26a-477e-8c5a-a0bba4ba8139" -->
### Technical Details
- Data structure: B-tree indexed documents (JSON/BSON)
- Storage: MongoDB, CouchDB, Elasticsearch, Firebase
- Time complexity: O(log n) for indexed queries
- Space: Variable per document (flexible schema)

<!-- section_id: "013c9549-ae4c-4c2e-809e-8e8daa71845b" -->
### Used By
- Mem0 internal storage
- Custom memory systems needing flexible schemas
- Systems that store heterogeneous memory types (some have embeddings, some have entity lists, some have raw text)

<!-- section_id: "77f38308-2de8-413d-9cb8-4c8cd9553bbf" -->
### Which Memory Types Use This
- **Any memory type** where entries have varying structures
- **Mixed-type memory stores** (one collection for episodic, entity, and factual memories with different fields)

<!-- section_id: "453b2762-d9a7-4fee-8250-5e8d0aefba94" -->
### Strengths
- Schema flexibility — different memories can have different structures
- Easy to evolve over time (add fields without migrations)
- Good for heterogeneous memory (mix of types in one store)
- Native JSON — easy to work with in code

<!-- section_id: "0c4aba0e-b54d-46b9-8d9a-f404aedef4dd" -->
### Weaknesses
- No relationship modeling (flat documents)
- No native semantic search (unless the DB supports vector extensions)
- Can become a "dumping ground" without discipline

<!-- section_id: "7840f8fc-5ce3-4e2f-a72c-a7cc5bff8e85" -->
### Brain Analogy
- Not a natural brain analog. Closest to **a filing cabinet where each folder can contain different types of documents**.

---

<!-- section_id: "e3f5b4c2-46ca-49dd-9d3d-bde6e49762e4" -->
## 9. Plain Text Files (Markdown / JSON on Disk)

<!-- section_id: "4cc0549d-817d-4dd1-9c94-71c63c05c4f2" -->
### What It Is
Memory stored as human-readable files in a directory structure. Our framework's primary approach.

```
memory/
  episodic/
    2026-02-17_session.md
    2026-02-18_session.md
  entities/
    alice.md
    project_x.md
  learnings/
    gotcha_jq_comments.md
```

<!-- section_id: "888a926e-f1cc-443e-857a-c93899e33b0a" -->
### How It Works
- Each memory is a file (Markdown for human-readable, JSON for structured)
- Directory structure provides organization and scoping
- Files can have YAML frontmatter for metadata
- Retrieval = read relevant files (by name, path, or grep search)
- Git provides versioning, history, and collaboration for free

<!-- section_id: "54f3171e-3d6e-4018-8fc4-ce4d8b0469eb" -->
### Technical Details
- Data structure: Files + directory tree (a hierarchical namespace)
- Storage: Local filesystem, synced via git or file sync tools
- Time complexity: O(1) to read a specific file; O(n) to search across files
- Space: Minimal overhead — just the text

<!-- section_id: "22ecd479-4f52-48e1-98f5-f558908f6015" -->
### Used By
- Letta filesystem baseline (74% LoCoMo with just file tools + GPT-4o mini)
- Our layer-stage framework (CLAUDE.md chain, episodic directories, 0AGNOSTIC.md)
- Claude Code auto-memory (`~/.claude/projects/*/memory/`)
- Any tool-agnostic memory system

<!-- section_id: "001e2d5a-6134-4a99-85a7-ad9af3848721" -->
### Which Memory Types Use This
- **All of them** — any memory type can be stored as files
- Particularly good for: episodic memory (session logs), semantic memory (knowledge files), profile memory (identity files), procedural memory (skill files)

<!-- section_id: "3cfe2b2a-a91a-4011-86b9-3e734b38a765" -->
### Strengths
- **Human-readable and editable** — the user can read, write, and audit memories directly
- **Tool-agnostic** — any AI tool can read files (Claude, Gemini, Cursor, etc.)
- **Git-friendly** — version history, diffs, merges, branching all come free
- **Simple** — no database to set up, no API to learn
- **The baseline to beat** — if a fancy system doesn't outperform files + a good LLM, it's over-engineered

<!-- section_id: "3364c5d4-6fd0-447c-8035-9593a5768ae6" -->
### Weaknesses
- **No semantic search** (only filename and grep-based retrieval)
- **Doesn't scale to millions of entries** (file system slows down)
- **No built-in indexing** (must maintain indexes manually)
- **Retrieval depends on good naming and organization** — badly organized files = bad retrieval

<!-- section_id: "512afb87-7974-4662-bbf4-69f1990cb8d1" -->
### Brain Analogy
- Closest to **external memory aids** — notebooks, journals, diaries. Not a brain structure, but an augmentation of memory that the brain can interact with.

---

<!-- section_id: "4d9d6d8d-39ce-474f-9f32-a5267bfc20b8" -->
## 10. KV Cache (Attention Key-Value Cache)

<!-- section_id: "d469ffb8-555e-4ad2-bdf0-530cde377e56" -->
### What It Is
The key and value matrices computed during the LLM's self-attention mechanism, cached to avoid recomputation. This is the model's **latent working memory** — it exists only during inference and is not normally persisted.

<!-- section_id: "7cc8de9e-ae09-4e32-b350-7da58f32fdc4" -->
### How It Works
- As the LLM processes each token, every attention layer computes key (K) and value (V) vectors
- These are cached so that when generating the next token, previous tokens don't need to be reprocessed
- The KV cache grows with each token generated
- When context window is full, the cache must be managed (dropped, compressed, or evicted)

<!-- section_id: "ec30e276-6d76-471c-bb45-2f1a6206b69f" -->
### Technical Details
- Data structure: Tensors (3D arrays of floats) — one K matrix and one V matrix per attention layer per attention head
- Storage: GPU memory (VRAM) during inference
- Size: Grows linearly with sequence length × number of layers × hidden dimension
- For a 200K context model, KV cache can consume many GB of VRAM

<!-- section_id: "44a40a2f-a58a-4cc8-b7ea-0db25da2b45c" -->
### KV Cache Management Strategies
| Strategy | How | Trade-off |
|---|---|---|
| **Dropping** | Remove cache entries for less important tokens | Loses information but frees memory |
| **Compression** | Low-rank approximation or quantization of cached values | Reduces memory with some quality loss |
| **Selective loading** | Only load relevant KV pairs via approximate nearest neighbor | Faster but may miss relevant context |
| **Offloading** | Move to CPU RAM or disk, reload when needed | Slower but retains all information |

<!-- section_id: "7d613793-c93e-453c-936b-2c3c78ce79d2" -->
### Used By
- Every LLM during inference (this is always happening under the hood)
- MemOS manipulates KV cache directly (freezing, selective loading, priority eviction)
- Memory3 injects external knowledge as KV pairs into attention layers

<!-- section_id: "6b2e4f2e-1c2f-4297-ad97-b0fe925cab4c" -->
### Which Memory Types Use This
- **Working memory** — the active context the model is currently processing
- **Latent memory** — hidden state representations that encode meaning in a non-human-readable form

<!-- section_id: "41070a20-7236-4cbe-b172-63602221d7d9" -->
### Strengths
- Zero additional infrastructure — it's built into the model
- Fastest possible "retrieval" — information is already in the attention computation
- Rich representation — captures nuanced contextual meaning

<!-- section_id: "8088738c-6638-4dce-93cf-c33617589e23" -->
### Weaknesses
- **Not persistent** — destroyed when the session ends (unless explicitly saved)
- **Not human-readable** — opaque tensors, no way to inspect what's stored
- **Not transferable** — KV cache from one model can't be used by another
- **Memory-hungry** — consumes significant GPU VRAM
- **No selective access** — everything in the cache influences everything else through attention

<!-- section_id: "af22b77b-443b-4f4a-8e2d-fed3dcf2a5c9" -->
### Brain Analogy
- Closest to **active neural firing patterns** — the dynamic, fleeting state of neurons currently active in working memory. Just as neural firing patterns are lost when you stop thinking about something (unless consolidated to long-term storage), KV cache is lost when the session ends.

---

<!-- section_id: "9384dfdf-83e7-4124-ba76-849b06397f88" -->
## 11. Model Parameters (Neural Network Weights)

<!-- section_id: "e517de0e-b9d3-4cfd-ba23-6badcae532d7" -->
### What It Is
The billions of floating-point numbers that make up the LLM's neural network. Everything the model "knows" from pretraining is encoded here — distributed across layers, not localized to specific parameters.

<!-- section_id: "e4f2aaf2-76ff-4f74-98dd-06094de918e4" -->
### How It Works
- During pretraining, the model processes trillions of tokens
- Statistical patterns from this training data get encoded as weight values
- When you ask a question, the weights produce the answer through forward passes
- The knowledge is distributed — no single weight stores a specific fact

<!-- section_id: "668f2c45-8d0b-4370-98b7-5f26420f35cf" -->
### How to Modify It (Adding New Memories to Parametric Storage)
| Method | How | When to Use |
|---|---|---|
| **Fine-tuning** | Train on new data, adjust all weights | Large-scale knowledge updates |
| **LoRA adapters** | Train small additional weight matrices that layer on top | Efficient task-specific adaptation |
| **Knowledge editing (ROME, MEMIT)** | Surgically modify specific weights to change specific facts | Correcting individual facts ("The president of X is now Y") |
| **Continual learning** | Ongoing training on new data without forgetting old | Keeping model up-to-date over time |
| **Machine unlearning** | Removing specific knowledge from weights | Privacy, compliance, removing harmful content |

<!-- section_id: "8e4138bc-237c-4f8a-b4e0-838d18a6eaf0" -->
### Technical Details
- Data structure: Multi-dimensional tensors (weight matrices) organized into layers
- Storage: Model checkpoint files (often 10-100+ GB)
- Access: Forward pass through the entire network
- Not directly queryable — you can't ask "what do you know about X?" and get a reliable answer

<!-- section_id: "8160b96d-2288-4184-9012-b2bd572a31b8" -->
### Used By
- Every LLM (this IS the model)
- Fine-tuned domain models
- LoRA adapters for task-specific customization

<!-- section_id: "e07d9848-2d0e-4163-a93b-595b7f8e285e" -->
### Which Memory Types Use This
- **Long-term semantic memory** — general world knowledge from pretraining
- **Procedural memory** — learned patterns for how to respond, reason, use tools

<!-- section_id: "7e46f7d1-5874-42d2-ac28-6880c3a9de88" -->
### Strengths
- Instant retrieval — no database lookup, knowledge flows through the forward pass
- Massive capacity — billions of parameters can store enormous amounts of knowledge
- Generalizes — can answer novel questions by combining stored patterns

<!-- section_id: "58f1bd0a-b314-445b-8a28-ad67df482fa0" -->
### Weaknesses
- **Opaque** — cannot inspect, audit, or verify what's stored
- **Expensive to update** — fine-tuning requires compute and data
- **Catastrophic forgetting** — updating can overwrite existing knowledge
- **Hallucination** — the model can generate plausible-sounding but false information
- **Stale** — knowledge is frozen at training cutoff (unless updated)

<!-- section_id: "a8952f92-c68a-4a65-87cd-ac536512180a" -->
### Brain Analogy
- Closest to **synaptic weights** — the strength of connections between neurons, shaped by lifetime of experience (training). Just as you can't open someone's brain and read out "what they know about trees," you can't inspect model weights for specific facts.

---

<!-- section_id: "08cbeeae-f6d3-4970-aaee-2266e3641a2e" -->
## 12. Semantic Tree (Hierarchical Tree Structure)

<!-- section_id: "ca56c413-8d71-4806-ae6f-6cc073bd41be" -->
### What It Is
A tree data structure where nodes represent semantic categories at different levels of abstraction, and memories are stored as leaves. SHIMI is the primary implementation.

```
Root
├── Science
│   ├── Biology
│   │   ├── Botany
│   │   │   ├── "Oak trees produce acorns"
│   │   │   └── "Photosynthesis requires sunlight"
│   │   └── Zoology
│   └── Physics
├── People
│   ├── Colleagues
│   └── Family
└── Projects
    ├── Project X
    └── Project Y
```

<!-- section_id: "ac114d14-303c-47b9-a89d-c4e772959bdd" -->
### How It Works
- New memories are classified by an LLM into the appropriate branch
- Retrieval descends from root, choosing the most relevant branch at each level
- Like a library's Dewey Decimal system — narrow down level by level
- Each node stores a summary of its children for efficient traversal

<!-- section_id: "a4e36fdd-521c-4aac-b44f-467b3fed9c16" -->
### Technical Details
- Data structure: N-ary tree with LLM-classified node routing
- Storage: Tree nodes can be in-memory, database-backed, or file-based
- Time complexity: O(log n) retrieval (descend tree) vs O(n) for flat search
- Decentralized sync possible via Merkle-DAG + Bloom filters + CRDT (SHIMI)

<!-- section_id: "a15b75d2-dea5-4aba-9a16-8233a4e67e9a" -->
### Used By
- SHIMI (Semantic Hierarchical Memory Index)
- Custom semantic organization systems

<!-- section_id: "35072528-3596-41dd-8a4a-bfd2c0dd43e1" -->
### Which Memory Types Use This
- **Long-term semantic memory** (organized knowledge at scale)
- **Multi-agent shared memory** (SHIMI supports decentralized peer-to-peer sync)

<!-- section_id: "5accc8ea-d058-4ddf-9aa6-ae097750be6d" -->
### Strengths
- **Sublinear retrieval** — O(log n) vs O(n) for flat vector search
- **Explainable** — you can trace exactly why something was retrieved (show the path)
- **Hierarchical organization** — natural for knowledge that has categorical structure
- **Benchmark results** — 90% top-1 accuracy vs 65% for flat RAG

<!-- section_id: "eeb6a574-b78c-414f-b5e4-7609227c7771" -->
### Weaknesses
- Tree restructuring is expensive when knowledge doesn't fit the current hierarchy
- LLM classification at each node adds latency
- Requires well-defined categories — messy, overlapping knowledge is hard to tree-ify
- Not suitable for small memory sets (tree overhead not justified)

<!-- section_id: "1328899e-c0a0-45ca-9293-d8f083aa0113" -->
### Brain Analogy
- Closest to **categorical organization in temporal cortex** — the brain organizes concepts hierarchically (animal → mammal → dog → Labrador). Category-specific brain injuries (e.g., losing knowledge of living things but not tools) suggest hierarchical storage.

---

<!-- section_id: "ca7b3ee1-0cb4-4582-85ea-676368009229" -->
## 13. Scored List / Priority Queue (Composite Scoring)

<!-- section_id: "63538713-47be-468f-b6a0-22c644bc6e63" -->
### What It Is
A single flat list of memories where each entry has a composite score calculated from multiple factors. Retrieval simply sorts by score and returns the top K.

<!-- section_id: "3a4dc26a-8ca1-4c12-afbe-e8a534071c8c" -->
### How It Works
```
score = (recency_weight × recency_score) +
        (semantic_weight × semantic_similarity) +
        (importance_weight × importance_score)
```
- Each memory has attributes: creation time, embedding, importance rating
- At retrieval time, all three factors are computed and combined
- Top-scoring entries are returned
- Weights are tunable (more recency-biased vs more relevance-biased)

<!-- section_id: "18e50891-9d53-4a64-b331-0668b13d9f62" -->
### Technical Details
- Data structure: List/array with per-entry metadata, sorted on demand
- Storage: Any database that can store the fields (often LanceDB, SQLite, or in-memory)
- Time complexity: O(n) to score all entries, O(n log n) to sort, or use a heap for O(n log K) top-K
- CrewAI default: `recency_half_life_days = 30`

<!-- section_id: "7cb4e7fe-0bf3-4483-ac8c-9f8a4c5d79d4" -->
### Used By
- CrewAI's unified Memory class
- Generative Agents (recency × relevance × importance)
- Any system that combines multiple retrieval signals

<!-- section_id: "5370f568-b8ca-4386-9552-244b59ebf4b1" -->
### Which Memory Types Use This
- **Unified memory** (single store replacing multiple memory types)
- **Experiential memory** (where recency, relevance, and importance all matter)

<!-- section_id: "0e4f8757-2c6a-44c4-9bc6-9fbeeb71a7a0" -->
### Strengths
- Simple — one store, one scoring function, one API
- Adaptive — weights can be tuned for different use cases
- Balances multiple factors without maintaining separate systems

<!-- section_id: "a4e2c071-4f30-4b25-ba23-7d125af30e52" -->
### Weaknesses
- Scoring function quality determines system quality — bad weights = bad retrieval
- Harder to debug than separate stores (why was this retrieved? which factor dominated?)
- Doesn't support fundamentally different query types (temporal vs semantic vs structural)

<!-- section_id: "9a12e5a8-9d7d-44e1-bb55-a522996f0e8d" -->
### Brain Analogy
- Loosely like **memory retrieval competition** — in ACT-R, memories compete for activation based on base-level activation (recency/frequency) + spreading activation (relevance) + noise. The highest-activation memory "wins" retrieval.

---

<!-- section_id: "ea4dd62a-7b7b-4641-ad52-fd176b81fb49" -->
## 14. Stack (LIFO — Last In, First Out)

<!-- section_id: "2c8c22a8-dbac-4e3a-a170-13daef9d165f" -->
### What It Is
A data structure where the last item added is the first one retrieved. Used for goal management and nested reasoning.

<!-- section_id: "41b4aac4-643e-46a5-84c6-ad942c17eadb" -->
### How It Works
- Push a goal onto the stack → it becomes the current focus
- Completing or abandoning a goal → pop it, return to the previous one
- Supports nesting: main_goal → sub_goal → sub_sub_goal

<!-- section_id: "861b27a3-79fb-4728-bcf6-9eb5bedd86c7" -->
### Technical Details
- Data structure: Stack (array with push/pop at one end)
- Storage: In-memory
- Time complexity: O(1) push, O(1) pop
- Space: Proportional to nesting depth

<!-- section_id: "d9c44663-7ce8-4284-a6bc-22daa04a9fdb" -->
### Used By
- SOAR's goal stack (central to its decision cycle)
- Agent planning systems with goal decomposition
- Chain-of-thought reasoning with nested sub-problems

<!-- section_id: "9e9be94c-faec-4fbb-ae99-0cf9c634ff49" -->
### Which Memory Types Use This
- **Working memory / task state** (current goals and subgoals)
- **Prospective memory** (planned future actions)

<!-- section_id: "f5d155f9-75a1-4c38-810f-feca38643a0c" -->
### Strengths
- Natural for hierarchical task decomposition
- Ensures you return to the parent goal after completing a subgoal
- Simple, well-understood data structure

<!-- section_id: "f5cb0743-cd62-4920-98e6-6c4836dc699f" -->
### Weaknesses
- Only tracks the current path — no history of completed or abandoned goals
- Strictly LIFO — can't easily switch to a sibling goal without unwinding

<!-- section_id: "b529d878-a705-45e5-8b32-6f67fc73bef8" -->
### Brain Analogy
- Loosely like **the prefrontal cortex's goal maintenance system** — maintaining the current goal hierarchy, with the ability to push subgoals and return to the parent goal.

---

<!-- section_id: "d9281a56-c8d7-48c2-8b6c-73682453cf94" -->
## 15. Production Rule Database (IF-THEN Rule Sets)

<!-- section_id: "8f90d7e5-c9d1-4d09-81e8-d4a722cfa5b7" -->
### What It Is
A collection of condition-action pairs that encode procedural knowledge — "how to do things" rather than "what things are."

```
Rule 1: IF (goal = navigate) AND (obstacle = detected) → THEN (turn left)
Rule 2: IF (goal = answer_question) AND (confidence < 0.5) → THEN (search_web)
Rule 3: IF (user_said = "thank you") → THEN (respond_politely, close_task)
```

<!-- section_id: "81a69ce1-ca8b-4361-8d03-e1a2777f1c9c" -->
### How It Works
- Each rule has a condition (pattern to match against current state) and an action (what to do)
- Rules are tested against working memory
- Matching rules compete for activation (utility-based selection)
- Selected rules fire, modifying working memory or producing actions
- New rules can be learned through experience (chunking in SOAR)

<!-- section_id: "878f7f92-cc97-4574-96eb-9db76b4a58e9" -->
### Technical Details
- Data structure: Set of (condition, action, utility) tuples
- Storage: Rule database (custom format, often in-memory)
- Matching: Pattern matching against current state (can be expensive for large rule sets)
- Learning: Utility values updated through reinforcement; new rules created through chunking

<!-- section_id: "ba8e64bd-7f85-48e2-8306-439f223bbf67" -->
### Used By
- SOAR procedural memory
- ACT-R production memory
- Expert systems
- ReAct-style agent patterns (implicitly — the LLM's learned patterns function as soft production rules)

<!-- section_id: "4a203455-b070-432b-979f-2be966dca547" -->
### Which Memory Types Use This
- **Procedural memory** (skills, habits, how-to knowledge)
- **Policy memory** (decision-making rules)

<!-- section_id: "ad7582de-279a-40ca-8ba6-ba9df53aa65c" -->
### Strengths
- Interpretable — you can read and understand each rule
- Learnable — new rules emerge from experience
- Fast execution once matched
- Supports complex conditional behavior

<!-- section_id: "a8f8f602-8b6c-4148-94d3-ef1222cc86e3" -->
### Weaknesses
- Rule sets can become unmanageable at scale (thousands of rules)
- Rule conflicts require resolution mechanisms
- Brittle — slight variations in conditions can prevent matching
- Hard to cover all cases (combinatorial explosion)

<!-- section_id: "67aa5a98-6b00-4e94-89be-4a942512e756" -->
### Brain Analogy
- Closest to **procedural memory in the basal ganglia** — automatic, habitual responses triggered by specific conditions. Like how you don't think about the steps of riding a bike — the procedure fires automatically when the conditions match.

---

<!-- section_id: "331f79dc-d4de-43ed-ba7c-aa97056477f8" -->
## 16. Activation-State Snapshots (Serialized Tensors)

<!-- section_id: "fb076186-8689-4dc1-846b-5e20bc8e89f0" -->
### What It Is
A saved copy of the LLM's internal hidden states at a specific point in processing. Like a save-state in a video game — you can reload the model's exact internal state later.

<!-- section_id: "93d383a4-1e7c-405f-adfe-2c4ed94d2a2a" -->
### How It Works
- At a chosen point during inference, the model's KV cache and/or hidden layer activations are serialized (saved to disk)
- Later, these states can be loaded back, restoring the model to exactly where it was
- No need to re-process the entire context — just load the snapshot and continue

<!-- section_id: "b2f86787-47e5-441a-b0db-74c92ecf8588" -->
### Technical Details
- Data structure: Serialized tensors (multi-dimensional float arrays)
- Storage: Disk files, typically in model-specific formats
- Size: Can be very large (GB) depending on model size and context length
- Requires the exact same model architecture to reload

<!-- section_id: "564356ae-37f3-430f-a546-4075248ce78c" -->
### Used By
- MemOS's "activation memory" (MemCube abstraction)
- Memory3 (injecting knowledge as KV pairs)
- Prompt caching systems (Anthropic's prompt caching, etc.)
- Checkpoint/resume systems for long-running tasks

<!-- section_id: "7b7cd78d-42fe-42b2-8874-9a2c53353322" -->
### Which Memory Types Use This
- **Latent memory** (hidden state representations)
- **Working memory snapshots** (saving and restoring processing state)

<!-- section_id: "73d0415d-7e3b-4cdb-b966-a12f3fb643a6" -->
### Strengths
- **Instant context restoration** — no reprocessing needed
- **Preserves nuance** — captures the full internal state, including subtleties lost in text summaries
- Enables "memory transplants" between sessions

<!-- section_id: "35e9e5e1-0dbe-485b-8eef-099d9cb04718" -->
### Weaknesses
- **Model-locked** — snapshots only work with the exact same model
- **Opaque** — can't inspect or edit what's in the snapshot
- **Large** — significant storage requirements
- **Fragile** — model updates invalidate all saved snapshots

<!-- section_id: "a62b7ff9-381b-4be8-a8d0-1147b954597c" -->
### Brain Analogy
- Loosely like **state-dependent memory** — the phenomenon where you remember things better when you're in the same mental/physical state as when you learned them. Restoring the model's hidden states recreates the "mental state" it was in.

---

<!-- section_id: "651d66ae-60cc-4020-9c3e-5972a15d9be0" -->
## Summary: Which Memory Types Use Which Data Structures

| Memory Type | Typical Data Structures |
|---|---|
| **Conversation buffer (short-term)** | Raw message list, sliding window |
| **Working memory / scratchpad** | KV cache, stack, in-memory variables |
| **Entity memory** | Key-value store, knowledge graph |
| **Episodic memory** | Raw message list, relational DB, files, document store |
| **Semantic / factual memory** | Vector store, knowledge graph, key-value store, files |
| **Procedural memory** | Production rules, model parameters |
| **Summary memory** | LLM-generated summary (compressed text) |
| **Profile / persona memory** | Key-value store, files |
| **Reflection memory** | Vector store, files, document store |
| **Hierarchical / tiered memory** | Multiple data structures in tiers (window → scored list → vector store → files) |
| **Unified / scored memory** | Scored list / priority queue |
| **Shared / collaborative memory** | Files, document store, knowledge graph |
| **Latent memory** | KV cache, activation snapshots |
| **Parametric memory** | Model parameters (weights) |

---

<!-- section_id: "98374450-942f-4212-b8c1-d8a9d036ebbe" -->
## Sources

- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Rethinking Memory in AI: Taxonomy, Operations, Topics (arXiv:2505.00675)](https://arxiv.org/html/2505.00675v2)
- [MemOS: A Memory OS for AI System (arXiv:2507.03724)](https://arxiv.org/abs/2507.03724)
- [Mem0: Building Production-Ready AI Agents (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413)
- [Comparing File Systems and Databases for AI Agent Memory (Oracle)](https://blogs.oracle.com/developers/comparing-file-systems-and-databases-for-effective-ai-agent-memory-management)
- [AI Agents: Memory Systems and Graph Database Integration (FalkorDB)](https://www.falkordb.com/blog/ai-agents-memory-systems/)
- [SHIMI: Semantic Hierarchical Memory Index (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- All related research docs in this directory (see `00_overview_and_taxonomy.md` for index)
