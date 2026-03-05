---
resource_id: "56669cab-4f1c-4bb5-8924-3f7c88e2f8b8"
resource_type: "output"
resource_name: "14_memory_types_best_for_guide"
---
# Memory Types: What Each Is Best For

## Purpose

A practical decision guide. For each memory type, this file answers: **when should you use it, when should you NOT, and what's the best implementation?**

---

## 1. Conversation Buffer Memory

### Best For
- **Short conversations** (< 20 turns) where every word matters
- **Customer support bots** that need full conversation fidelity
- **Debugging/auditing** where complete transcript is needed
- **Prototyping** — simplest possible memory, good starting point

### Not For
- Long conversations (token overflow)
- Cross-session use (buffer is ephemeral)
- Multi-user systems (no isolation mechanism)

### Best Implementation
- LangChain `ConversationBufferMemory` (simplest)
- Raw message list in any framework

### Key Metric
- Cost grows linearly with conversation length

---

## 2. Sliding Window Memory

### Best For
- **Medium-length conversations** where only recent context matters
- **Task-focused agents** where older context becomes irrelevant
- **Cost-constrained** applications — bounded token budget

### Not For
- Conversations where early context matters later (users reference things said 50 turns ago)
- Knowledge accumulation (everything outside the window is lost)

### Best Implementation
- LangChain `ConversationBufferWindowMemory` with tuned K
- Any framework with a `max_turns` or `max_tokens` parameter

### Key Metric
- Fixed token cost regardless of conversation length (window size)

---

## 3. Summary Memory

### Best For
- **Very long conversations** where gist matters more than detail
- **Token-constrained environments** — summary stays roughly constant size
- **Multi-session recaps** — "last time we discussed..."

### Not For
- Conversations where exact wording matters (legal, compliance)
- High-accuracy applications (summarization introduces error)
- Low-latency requirements (LLM call per summarization)

### Best Implementation
- LangChain `ConversationSummaryBufferMemory` (hybrid: recent raw + old summarized)
- Custom: periodic summarization with rolling window

### Key Metric
- Summary quality determines system quality — bad summarization = corrupted memory

---

## 4. Vector Store / Semantic Memory

### Best For
- **Large knowledge bases** — thousands of documents or memories
- **"Find relevant context"** problems — when you don't know which memory matters
- **Long-term recall** — searching across months of interaction history
- **Domain-specific knowledge** — product docs, FAQs, documentation

### Not For
- Small memory sets (< 100 items — just use full context)
- When temporal ordering matters more than semantic relevance
- When exact keyword matching is needed (use keyword search instead)
- Highly structured data (use a database or knowledge graph)

### Best Implementation
- Pinecone, Qdrant, or Weaviate for production
- ChromaDB or FAISS for prototyping
- LangChain `VectorStoreRetrieverMemory` for quick integration

### Key Metric
- Retrieval precision@K — are the top K results actually relevant?

---

## 5. Entity Memory

### Best For
- **Tracking people, organizations, concepts** mentioned in conversation
- **CRM-like agents** that need to remember facts about specific entities
- **Multi-entity interactions** — remembering who said what about whom
- **Evolving knowledge** — entity attributes that change over time

### Not For
- Conversations with few or no named entities
- Use cases where entity extraction errors are unacceptable (medical, legal)
- Simple Q&A where entity tracking adds no value

### Best Implementation
- LangChain `ConversationEntityMemory` with swappable store (Redis, SQLite)
- Mem0 with entity extraction enabled
- Custom entity store with LLM-based extraction

### Key Metric
- Entity extraction accuracy — wrong entities = corrupted knowledge

---

## 6. Knowledge Graph Memory

### Best For
- **Complex relationships** — "who manages whom", "which component depends on which"
- **Multi-hop reasoning** — questions requiring traversal across connections
- **Structured domain knowledge** — ontologies, taxonomies, org charts
- **Explainable retrieval** — showing WHY something was recalled (graph path)

### Not For
- Simple factual lookup (overkill)
- Rapidly changing knowledge (graph updates are expensive)
- Fuzzy/ambiguous information (graphs need clear structure)
- Prototyping (high setup cost)

### Best Implementation
- Neo4j for production knowledge graphs
- LangChain `ConversationKGMemory` for conversation-derived graphs
- Mem0 hybrid (graph + vector) for combining strengths
- Zep for temporal knowledge graphs

### Key Metric
- Graph completeness and accuracy — missing edges = missed connections

---

## 7. Episodic Memory (Session/Experience Records)

### Best For
- **Multi-session agents** that need to resume where they left off
- **Learning from experience** — agents that improve over time
- **Audit trails** — tracking what happened when
- **Temporal queries** — "what did we do last week?"
- **Our layer-stage framework** — session continuity is critical

### Not For
- Single-session use cases
- Agents that don't benefit from past experience
- Privacy-sensitive contexts where history must be minimized

### Best Implementation
- MemGPT/Letta recall memory for automated logging
- Markdown session files in episodic directories (tool-agnostic, our approach)
- Custom: auto-generate session summaries at session boundaries

### Key Metric
- Session continuity score — can the agent accurately recall last session's state?

---

## 8. Reflection Memory (Self-Improvement)

### Best For
- **Agents that attempt tasks repeatedly** — coding agents, debugging, iterative problem-solving
- **Self-improving systems** — agents that should get better over time
- **Error-prone tasks** — where learning from mistakes has high value
- **Benchmarks / competitions** — where marginal improvement matters

### Not For
- One-shot tasks (no opportunity to apply reflections)
- Tasks where the agent already performs at ceiling
- Cost-sensitive environments (reflection requires extra LLM calls)
- WebShop-style navigation (Reflexion showed no improvement here)

### Best Implementation
- Reflexion framework for task-level self-improvement
- Generative Agents reflection mechanism for broader insight generation
- Custom: periodic "what did I learn?" prompt → store insights

### Key Metric
- Task accuracy improvement across trials — does reflection actually help?
- Reflexion results: +24pts on HumanEval, +22pts on AlfWorld, +20pts on HotPotQA, +0 on WebShop

---

## 9. Core / Editable Memory (Agent Self-Knowledge)

### Best For
- **Persistent agents with identity** — agents that maintain character/persona
- **User preference tracking** — remembering how users like to interact
- **Agent customization** — adapting behavior to specific contexts
- **Our framework** — `0AGNOSTIC.md` identity sections serve this role

### Not For
- Generic assistants with no persistent identity
- Multi-user systems where one user shouldn't affect another's experience
- Compliance-heavy environments where self-modification is risky

### Best Implementation
- MemGPT core memory blocks (agent-editable, always in context)
- CLAUDE.md files with identity sections (our approach, static)
- Mem0 user profiles (managed externally)

### Key Metric
- Identity consistency — does the agent maintain coherent behavior across sessions?

---

## 10. Hierarchical / Tiered Memory (OS-Inspired)

### Best For
- **Long-running agents** with months of interaction history
- **Automated lifecycle management** — don't want manual memory curation
- **Bounded resource usage** — each tier has capacity limits
- **Production systems** that need predictable memory behavior

### Not For
- Simple chatbots (overkill)
- Short-lived agents (tiers don't have time to differentiate)
- Highly specialized memory needs (tiers are general-purpose)

### Best Implementation
- MemoryOS (EMNLP 2025): STM (7 pages) → MTM (200 segments) → LPM (100 entries per category)
- MemOS (MemTensor): MemCube abstraction unifying plaintext + activation + parametric memory
- Custom: simple 2-tier (recent buffer + persistent store) is often sufficient

### Key Metric
- Tier promotion accuracy — does the right information get promoted to long-term?
- MemOS: 159% improvement in temporal reasoning over OpenAI baseline

---

## 11. Semantic Hierarchical Memory (Tree-Based)

### Best For
- **Large-scale multi-agent systems** needing decentralized memory
- **Explainable retrieval** — trace exactly why something was recalled
- **Domain-specific knowledge** with natural hierarchical structure
- **Sublinear scaling** — query time shouldn't grow linearly with memory size

### Not For
- Small memory sets (tree overhead not justified)
- Rapidly changing knowledge (tree restructuring has cost)
- Single-agent systems (decentralized sync isn't needed)

### Best Implementation
- SHIMI architecture (arXiv:2504.06135)
- Custom semantic tree with LLM-based node classification

### Key Metric
- Retrieval accuracy: SHIMI 90% vs. flat RAG 65% (top-1)
- Interpretability: SHIMI 4.7/5 vs. RAG 2.1/5

---

## 12. Unified / Scored Memory (Single-Store)

### Best For
- **Teams wanting simplicity** — one API instead of multiple memory types
- **Rapid development** — less architecture to design and maintain
- **Adaptive retrieval** — let scoring decide what's relevant rather than manual type selection

### Not For
- Systems needing fine-grained control over specific memory behaviors
- Debugging-intensive environments (harder to trace retrieval decisions)
- Cases where different memory types genuinely need different storage backends

### Best Implementation
- CrewAI unified Memory class (LanceDB backend)
- Custom: single store with composite scoring (recency × relevance × importance)

### Key Metric
- Composite score quality — do the weights produce good retrieval ordering?

---

## 13. Profile / Persona Memory

### Best For
- **Personalized assistants** — remembering user preferences across sessions
- **Role-playing agents** — maintaining consistent character
- **Multi-user systems** — per-user customization
- **Our framework** — `0AGNOSTIC.md` identity sections + user-level CLAUDE.md

### Not For
- Stateless APIs
- Single-interaction use cases
- Privacy-restricted environments

### Best Implementation
- MemoryOS Long-Term Persona Memory: static profiles + dynamic knowledge + evolving traits
- Claude Memory (CLAUDE.md files): simple, transparent, user-editable
- Mem0 user profiles: hybrid storage with active curation

### Key Metric
- Personalization accuracy — does the agent correctly apply stored preferences?

---

## 14. Shared / Collaborative Memory

### Best For
- **Multi-agent teams** — agents working on the same project
- **Knowledge sharing** — one agent's discovery benefits all
- **Task handoffs** — agent B continues where agent A left off
- **Our framework** — team workflows with leader + teammates

### Not For
- Single-agent systems
- Privacy-sensitive contexts where agents shouldn't see each other's data
- Simple sequential workflows (just pass state)

### Best Implementation
- SHIMI (decentralized, peer-to-peer sync with CRDT)
- CrewAI scoped memory (hierarchical visibility)
- Shared filesystem (simplest — all agents read/write same directory)
- Custom: shared memory directory with file-level locking

### Key Metric
- Sync consistency — do all agents have the same view of shared memory?
- Handoff quality — can agent B seamlessly continue agent A's work?

---

## 15. File-Based Memory (The Underrated Baseline)

### Best For
- **Everything that doesn't need sub-second retrieval**
- **Tool-agnostic systems** — any AI tool can read files
- **Human-in-the-loop** — humans can read, edit, audit memory files
- **Git-tracked projects** — version history is free
- **Our framework** — perfectly aligned with existing infrastructure

### Not For
- Massive scale (millions of memories)
- Sub-100ms retrieval requirements
- Complex relational queries (use a database)

### Best Implementation
- Markdown files with YAML frontmatter (human-readable + machine-parseable)
- JSON files for structured data
- Directory structure as organization (scoping by path)
- Letta filesystem baseline: scored 74% on LoCoMo with just file tools + GPT-4o mini

### Key Metric
- This IS the baseline. If your fancy memory system doesn't beat file-based memory, you're over-engineering.

---

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

## Sources

- All benchmark data from `12_benchmarks_and_performance.md`
- System details from `06_dedicated_memory_platforms.md`
- Framework implementations from `05_framework_implementations.md`
- Cognitive foundations from `01_cognitive_science_foundations.md`
