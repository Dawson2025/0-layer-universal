---
resource_id: "56669cab-4f1c-4bb5-8924-3f7c88e2f8b8"
resource_type: "output"
resource_name: "14_memory_types_best_for_guide"
---
# Memory Types: What Each Is Best For

<!-- section_id: "185665c7-650d-4b37-8aff-be9fefdf4a2d" -->
## Purpose

A practical decision guide. For each memory type, this file answers: **when should you use it, when should you NOT, and what's the best implementation?**

---

<!-- section_id: "beebc8f3-ac90-4d69-97cb-ca79404701db" -->
## 1. Conversation Buffer Memory

<!-- section_id: "d2a265f1-f689-4aff-b739-f3e4bec656df" -->
### Best For
- **Short conversations** (< 20 turns) where every word matters
- **Customer support bots** that need full conversation fidelity
- **Debugging/auditing** where complete transcript is needed
- **Prototyping** — simplest possible memory, good starting point

<!-- section_id: "8134857d-d57e-4cd5-b659-aeaf7b916d9b" -->
### Not For
- Long conversations (token overflow)
- Cross-session use (buffer is ephemeral)
- Multi-user systems (no isolation mechanism)

<!-- section_id: "6eebafcb-105e-4d7b-837b-b78b44a90a74" -->
### Best Implementation
- LangChain `ConversationBufferMemory` (simplest)
- Raw message list in any framework

<!-- section_id: "2191331b-c200-4d82-b0bf-c33b1b95d83e" -->
### Key Metric
- Cost grows linearly with conversation length

---

<!-- section_id: "282894fb-34b2-4899-a643-d31cf8473438" -->
## 2. Sliding Window Memory

<!-- section_id: "025111a5-65cb-4417-801d-755023ab4e4a" -->
### Best For
- **Medium-length conversations** where only recent context matters
- **Task-focused agents** where older context becomes irrelevant
- **Cost-constrained** applications — bounded token budget

<!-- section_id: "5f4fb1e7-8315-4134-9e7d-cd275a116fc8" -->
### Not For
- Conversations where early context matters later (users reference things said 50 turns ago)
- Knowledge accumulation (everything outside the window is lost)

<!-- section_id: "082af9ea-15ca-4e38-960a-b7db7c12f61e" -->
### Best Implementation
- LangChain `ConversationBufferWindowMemory` with tuned K
- Any framework with a `max_turns` or `max_tokens` parameter

<!-- section_id: "c595caff-733e-4c1d-875e-d84971a7b4fa" -->
### Key Metric
- Fixed token cost regardless of conversation length (window size)

---

<!-- section_id: "bfeae4ba-cf09-4aa1-a938-f7f9c1c0d01f" -->
## 3. Summary Memory

<!-- section_id: "5a016099-2cad-40bb-8912-16edf9c65964" -->
### Best For
- **Very long conversations** where gist matters more than detail
- **Token-constrained environments** — summary stays roughly constant size
- **Multi-session recaps** — "last time we discussed..."

<!-- section_id: "2ca37631-9f87-4532-b8fc-40e6eed0e71a" -->
### Not For
- Conversations where exact wording matters (legal, compliance)
- High-accuracy applications (summarization introduces error)
- Low-latency requirements (LLM call per summarization)

<!-- section_id: "8fee228f-4989-48ad-803c-394cec6f0bc7" -->
### Best Implementation
- LangChain `ConversationSummaryBufferMemory` (hybrid: recent raw + old summarized)
- Custom: periodic summarization with rolling window

<!-- section_id: "4e772e75-d698-4066-9246-ff00afff4aa1" -->
### Key Metric
- Summary quality determines system quality — bad summarization = corrupted memory

---

<!-- section_id: "0db1a363-7d75-475d-be8d-6eed9c6ce0b5" -->
## 4. Vector Store / Semantic Memory

<!-- section_id: "e89ecfca-a19e-4046-8509-4f4c4d63cada" -->
### Best For
- **Large knowledge bases** — thousands of documents or memories
- **"Find relevant context"** problems — when you don't know which memory matters
- **Long-term recall** — searching across months of interaction history
- **Domain-specific knowledge** — product docs, FAQs, documentation

<!-- section_id: "86d46657-9e1d-475e-82f4-3438940a0290" -->
### Not For
- Small memory sets (< 100 items — just use full context)
- When temporal ordering matters more than semantic relevance
- When exact keyword matching is needed (use keyword search instead)
- Highly structured data (use a database or knowledge graph)

<!-- section_id: "19eeae0b-c24a-4917-b29f-329988eb6f9e" -->
### Best Implementation
- Pinecone, Qdrant, or Weaviate for production
- ChromaDB or FAISS for prototyping
- LangChain `VectorStoreRetrieverMemory` for quick integration

<!-- section_id: "c1fe6608-3d27-4530-8ea9-4d6e12c918e0" -->
### Key Metric
- Retrieval precision@K — are the top K results actually relevant?

---

<!-- section_id: "5d181f61-9992-476d-a974-9f7354a8b729" -->
## 5. Entity Memory

<!-- section_id: "d9ca3b51-b127-4330-87b7-f34305d48ffe" -->
### Best For
- **Tracking people, organizations, concepts** mentioned in conversation
- **CRM-like agents** that need to remember facts about specific entities
- **Multi-entity interactions** — remembering who said what about whom
- **Evolving knowledge** — entity attributes that change over time

<!-- section_id: "23043b0b-e13f-49be-ab52-07b87a7ea490" -->
### Not For
- Conversations with few or no named entities
- Use cases where entity extraction errors are unacceptable (medical, legal)
- Simple Q&A where entity tracking adds no value

<!-- section_id: "819d2284-a93b-4a5e-8214-494049fdad8e" -->
### Best Implementation
- LangChain `ConversationEntityMemory` with swappable store (Redis, SQLite)
- Mem0 with entity extraction enabled
- Custom entity store with LLM-based extraction

<!-- section_id: "3f02a7f3-8906-40c5-ad9d-a6a02062b5bf" -->
### Key Metric
- Entity extraction accuracy — wrong entities = corrupted knowledge

---

<!-- section_id: "950fd830-07d8-4fdd-a5b2-9ae4e816f994" -->
## 6. Knowledge Graph Memory

<!-- section_id: "d7674ce3-93a5-4d04-b085-b59e52103f03" -->
### Best For
- **Complex relationships** — "who manages whom", "which component depends on which"
- **Multi-hop reasoning** — questions requiring traversal across connections
- **Structured domain knowledge** — ontologies, taxonomies, org charts
- **Explainable retrieval** — showing WHY something was recalled (graph path)

<!-- section_id: "87cedeab-2d64-4680-8a4a-14901806f918" -->
### Not For
- Simple factual lookup (overkill)
- Rapidly changing knowledge (graph updates are expensive)
- Fuzzy/ambiguous information (graphs need clear structure)
- Prototyping (high setup cost)

<!-- section_id: "a6865468-07a0-42fc-9d4c-6f7bc595d124" -->
### Best Implementation
- Neo4j for production knowledge graphs
- LangChain `ConversationKGMemory` for conversation-derived graphs
- Mem0 hybrid (graph + vector) for combining strengths
- Zep for temporal knowledge graphs

<!-- section_id: "4929a2d1-d4ab-4c71-828e-b6b52e1252ba" -->
### Key Metric
- Graph completeness and accuracy — missing edges = missed connections

---

<!-- section_id: "2a40a52c-b78f-45d8-906c-1ca9aa22886d" -->
## 7. Episodic Memory (Session/Experience Records)

<!-- section_id: "833ac041-5f74-4d4a-9992-809973eb2338" -->
### Best For
- **Multi-session agents** that need to resume where they left off
- **Learning from experience** — agents that improve over time
- **Audit trails** — tracking what happened when
- **Temporal queries** — "what did we do last week?"
- **Our layer-stage framework** — session continuity is critical

<!-- section_id: "59a5f0b1-084c-409c-8eb1-9acfb52a4051" -->
### Not For
- Single-session use cases
- Agents that don't benefit from past experience
- Privacy-sensitive contexts where history must be minimized

<!-- section_id: "a72cd017-a882-4151-969e-92b4f6a96988" -->
### Best Implementation
- MemGPT/Letta recall memory for automated logging
- Markdown session files in episodic directories (tool-agnostic, our approach)
- Custom: auto-generate session summaries at session boundaries

<!-- section_id: "02ff349e-6126-4e31-be24-43c4fb867f92" -->
### Key Metric
- Session continuity score — can the agent accurately recall last session's state?

---

<!-- section_id: "06ec4876-3c06-465f-8eb7-0ac4fe4d83bb" -->
## 8. Reflection Memory (Self-Improvement)

<!-- section_id: "593255f9-a0df-4812-afc8-b2efd0a0da51" -->
### Best For
- **Agents that attempt tasks repeatedly** — coding agents, debugging, iterative problem-solving
- **Self-improving systems** — agents that should get better over time
- **Error-prone tasks** — where learning from mistakes has high value
- **Benchmarks / competitions** — where marginal improvement matters

<!-- section_id: "78ccacb0-6e82-4f91-9321-3bb85feaccaf" -->
### Not For
- One-shot tasks (no opportunity to apply reflections)
- Tasks where the agent already performs at ceiling
- Cost-sensitive environments (reflection requires extra LLM calls)
- WebShop-style navigation (Reflexion showed no improvement here)

<!-- section_id: "d53d9c34-eb40-4363-b787-7730041e6023" -->
### Best Implementation
- Reflexion framework for task-level self-improvement
- Generative Agents reflection mechanism for broader insight generation
- Custom: periodic "what did I learn?" prompt → store insights

<!-- section_id: "88cc343c-8c52-498d-ab24-6b8c463a3f22" -->
### Key Metric
- Task accuracy improvement across trials — does reflection actually help?
- Reflexion results: +24pts on HumanEval, +22pts on AlfWorld, +20pts on HotPotQA, +0 on WebShop

---

<!-- section_id: "6e0a1dad-c36c-41e4-b062-5977e4af9d20" -->
## 9. Core / Editable Memory (Agent Self-Knowledge)

<!-- section_id: "5fa3d2fb-2c66-4bab-acc6-c10ce2fe9df3" -->
### Best For
- **Persistent agents with identity** — agents that maintain character/persona
- **User preference tracking** — remembering how users like to interact
- **Agent customization** — adapting behavior to specific contexts
- **Our framework** — `0AGNOSTIC.md` identity sections serve this role

<!-- section_id: "8a360a4e-a77d-4c6e-b5bf-8f945070d54d" -->
### Not For
- Generic assistants with no persistent identity
- Multi-user systems where one user shouldn't affect another's experience
- Compliance-heavy environments where self-modification is risky

<!-- section_id: "c82960b3-16d0-40fc-a69b-ed0497c37302" -->
### Best Implementation
- MemGPT core memory blocks (agent-editable, always in context)
- CLAUDE.md files with identity sections (our approach, static)
- Mem0 user profiles (managed externally)

<!-- section_id: "dc30ebbe-ee4d-4b34-9ead-355e8e44b1e1" -->
### Key Metric
- Identity consistency — does the agent maintain coherent behavior across sessions?

---

<!-- section_id: "b5d2e29b-f084-46f5-9dc9-5df19957dcdc" -->
## 10. Hierarchical / Tiered Memory (OS-Inspired)

<!-- section_id: "22e1a1d3-00d0-4b4a-91d0-c5eb9b643766" -->
### Best For
- **Long-running agents** with months of interaction history
- **Automated lifecycle management** — don't want manual memory curation
- **Bounded resource usage** — each tier has capacity limits
- **Production systems** that need predictable memory behavior

<!-- section_id: "1f7e45f2-bce5-4304-8c26-2757fd8ff08f" -->
### Not For
- Simple chatbots (overkill)
- Short-lived agents (tiers don't have time to differentiate)
- Highly specialized memory needs (tiers are general-purpose)

<!-- section_id: "a72ba7ad-e2c2-43a7-bfbe-d4e1c4d58d0d" -->
### Best Implementation
- MemoryOS (EMNLP 2025): STM (7 pages) → MTM (200 segments) → LPM (100 entries per category)
- MemOS (MemTensor): MemCube abstraction unifying plaintext + activation + parametric memory
- Custom: simple 2-tier (recent buffer + persistent store) is often sufficient

<!-- section_id: "d5280ef3-2ac4-4fc1-9a31-b8a43cb5b599" -->
### Key Metric
- Tier promotion accuracy — does the right information get promoted to long-term?
- MemOS: 159% improvement in temporal reasoning over OpenAI baseline

---

<!-- section_id: "97aa6a6c-5363-4c06-9427-155f91ab6d5a" -->
## 11. Semantic Hierarchical Memory (Tree-Based)

<!-- section_id: "c05e3636-d114-4f22-9631-94a9db6e49d6" -->
### Best For
- **Large-scale multi-agent systems** needing decentralized memory
- **Explainable retrieval** — trace exactly why something was recalled
- **Domain-specific knowledge** with natural hierarchical structure
- **Sublinear scaling** — query time shouldn't grow linearly with memory size

<!-- section_id: "13f923f6-f86e-40d3-97a0-df0930f1ff6d" -->
### Not For
- Small memory sets (tree overhead not justified)
- Rapidly changing knowledge (tree restructuring has cost)
- Single-agent systems (decentralized sync isn't needed)

<!-- section_id: "4089c73a-16e7-4fa0-baf1-a054c4faa6dd" -->
### Best Implementation
- SHIMI architecture (arXiv:2504.06135)
- Custom semantic tree with LLM-based node classification

<!-- section_id: "54a9b4ea-9bff-4fa7-aa11-03269af42cad" -->
### Key Metric
- Retrieval accuracy: SHIMI 90% vs. flat RAG 65% (top-1)
- Interpretability: SHIMI 4.7/5 vs. RAG 2.1/5

---

<!-- section_id: "0d06998a-5113-42fa-a24a-8d77c6357d7e" -->
## 12. Unified / Scored Memory (Single-Store)

<!-- section_id: "0363573b-8577-4332-b629-1185e454f4a3" -->
### Best For
- **Teams wanting simplicity** — one API instead of multiple memory types
- **Rapid development** — less architecture to design and maintain
- **Adaptive retrieval** — let scoring decide what's relevant rather than manual type selection

<!-- section_id: "97d806e3-51a8-433d-ba0d-02dda6d09522" -->
### Not For
- Systems needing fine-grained control over specific memory behaviors
- Debugging-intensive environments (harder to trace retrieval decisions)
- Cases where different memory types genuinely need different storage backends

<!-- section_id: "81570fab-06a6-4c98-a1a6-e3f6663c08da" -->
### Best Implementation
- CrewAI unified Memory class (LanceDB backend)
- Custom: single store with composite scoring (recency × relevance × importance)

<!-- section_id: "e7b4084d-5862-454f-81b2-15f4bff81ce1" -->
### Key Metric
- Composite score quality — do the weights produce good retrieval ordering?

---

<!-- section_id: "acd1a601-1bbe-4253-a07b-bc07a886d124" -->
## 13. Profile / Persona Memory

<!-- section_id: "21371e90-387e-4188-82d0-a5143f1b1f18" -->
### Best For
- **Personalized assistants** — remembering user preferences across sessions
- **Role-playing agents** — maintaining consistent character
- **Multi-user systems** — per-user customization
- **Our framework** — `0AGNOSTIC.md` identity sections + user-level CLAUDE.md

<!-- section_id: "322288eb-3c3b-4111-88c9-331e8200f3e5" -->
### Not For
- Stateless APIs
- Single-interaction use cases
- Privacy-restricted environments

<!-- section_id: "bb6b2fb5-28f8-4caf-912e-efd44266ac1f" -->
### Best Implementation
- MemoryOS Long-Term Persona Memory: static profiles + dynamic knowledge + evolving traits
- Claude Memory (CLAUDE.md files): simple, transparent, user-editable
- Mem0 user profiles: hybrid storage with active curation

<!-- section_id: "9742df54-4d8a-4a34-81f4-eef88ad4a333" -->
### Key Metric
- Personalization accuracy — does the agent correctly apply stored preferences?

---

<!-- section_id: "b77f0c88-2e74-4550-9153-6852a0d0961f" -->
## 14. Shared / Collaborative Memory

<!-- section_id: "e2835ae2-b238-45ab-8b54-7d47bf8b1776" -->
### Best For
- **Multi-agent teams** — agents working on the same project
- **Knowledge sharing** — one agent's discovery benefits all
- **Task handoffs** — agent B continues where agent A left off
- **Our framework** — team workflows with leader + teammates

<!-- section_id: "cc49f964-da87-4d55-a5de-8b46e7114ccb" -->
### Not For
- Single-agent systems
- Privacy-sensitive contexts where agents shouldn't see each other's data
- Simple sequential workflows (just pass state)

<!-- section_id: "ac96a78b-2686-4e4a-ae0f-2e1c8cec3a11" -->
### Best Implementation
- SHIMI (decentralized, peer-to-peer sync with CRDT)
- CrewAI scoped memory (hierarchical visibility)
- Shared filesystem (simplest — all agents read/write same directory)
- Custom: shared memory directory with file-level locking

<!-- section_id: "349505c5-286b-4b3b-aa9f-2cb14cd9e70b" -->
### Key Metric
- Sync consistency — do all agents have the same view of shared memory?
- Handoff quality — can agent B seamlessly continue agent A's work?

---

<!-- section_id: "d0ae441b-9463-4db3-aed2-d974315b9ed4" -->
## 15. File-Based Memory (The Underrated Baseline)

<!-- section_id: "8e5f7a20-f8c5-41ef-8ef9-e43a907c1e75" -->
### Best For
- **Everything that doesn't need sub-second retrieval**
- **Tool-agnostic systems** — any AI tool can read files
- **Human-in-the-loop** — humans can read, edit, audit memory files
- **Git-tracked projects** — version history is free
- **Our framework** — perfectly aligned with existing infrastructure

<!-- section_id: "36b76a90-19c8-4398-a7b2-391378c7e4dc" -->
### Not For
- Massive scale (millions of memories)
- Sub-100ms retrieval requirements
- Complex relational queries (use a database)

<!-- section_id: "d003e030-00a0-46ac-95f5-7e855d61684f" -->
### Best Implementation
- Markdown files with YAML frontmatter (human-readable + machine-parseable)
- JSON files for structured data
- Directory structure as organization (scoping by path)
- Letta filesystem baseline: scored 74% on LoCoMo with just file tools + GPT-4o mini

<!-- section_id: "de6c1a03-450d-4891-824b-90099b1dfda4" -->
### Key Metric
- This IS the baseline. If your fancy memory system doesn't beat file-based memory, you're over-engineering.

---

<!-- section_id: "2031371a-488c-4ec7-a484-7ecf65198788" -->
## Decision Matrix: Quick Reference

| If you need... | Use | Why |
|----------------|-----|-----|
| Simplest possible | Buffer or file-based | Minimum complexity |
| Long conversations | Summary buffer | Bounded tokens |
| Large knowledge base | Vector store | Scalable similarity search |
| Entity tracking | Entity memory | Structured per-entity facts |
| Relationship reasoning | Knowledge graph | Multi-hop traversal |
| Session continuity | Episodic memory | Resume where you left off |
| Self-improvement | Reflection memory | Learn from mistakes |
| Agent identity | Core/profile memory | Consistent persona |
| Automated lifecycle | Hierarchical tiers | Managed promotion/decay |
| Multi-agent sharing | Shared/collaborative | Cross-agent knowledge |
| Explainable retrieval | SHIMI semantic tree | Traceable paths |
| Tool-agnostic persistence | File-based (Markdown) | Universal readability |
| Maximum benchmark scores | MemOS or Hindsight | SOTA performance |
| Best cost/performance | Files + good LLM | 74% LoCoMo with GPT-4o mini |

---

<!-- section_id: "1b77fec7-95d5-4b56-9396-a94a60f9952f" -->
## Sources

- All benchmark data from `12_benchmarks_and_performance.md`
- System details from `06_dedicated_memory_platforms.md`
- Framework implementations from `05_framework_implementations.md`
- Cognitive foundations from `01_cognitive_science_foundations.md`
