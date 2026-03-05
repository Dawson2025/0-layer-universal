---
resource_id: "7044c15e-6351-4295-a849-99f103b6cf7e"
resource_type: "output"
resource_name: "03_memory_by_content_type"
---
# Memory Types by Content / Function

<!-- section_id: "5d1db93f-96d5-41b7-a491-9ecc67bb5415" -->
## Overview

Memory systems categorized by what kind of information they store and what purpose they serve, regardless of duration or storage mechanism.

---

<!-- section_id: "061317b1-2a28-4ca4-b949-807474ac6056" -->
## 1. Factual / Semantic Memory

<!-- section_id: "dd9ca9ae-0a96-4976-8119-24a9c962ae53" -->
### What It Stores
- Objective facts about the world
- Definitions, concepts, relationships
- Domain knowledge, encyclopedic information
- Decontextualized general knowledge

<!-- section_id: "cea4e4c7-3053-4cf1-894b-9eab51d40dea" -->
### How It Works
- Stored as structured facts, knowledge graph triples, or embedded in model weights
- Retrieved by topical relevance rather than temporal context
- Updated through knowledge editing or external database modification

<!-- section_id: "d40272ae-73fd-4c8f-9a79-5fd95416047e" -->
### AI Implementations
- **Parametric knowledge**: Facts encoded in LLM weights during pretraining
- **Knowledge graphs**: Entity-relationship triples (e.g., Neo4j, Amazon Neptune)
- **RAG document stores**: Indexed factual documents for retrieval
- **LangChain ConversationKGMemory**: Extracts and maintains a knowledge graph from conversations
- **Wikipedia/knowledge base integrations**: External factual sources

<!-- section_id: "0528cfba-9691-4b62-912c-aad1f21da736" -->
### Retrieval Patterns
- Entity-based queries ("What do we know about X?")
- Relationship traversal ("How are X and Y connected?")
- Semantic similarity search

---

<!-- section_id: "3fb662ff-bbe0-4ac8-b1b2-1e596f565483" -->
## 2. Episodic Memory

<!-- section_id: "b565be44-3140-4483-8386-6b53f819b693" -->
### What It Stores
- Specific past events and interactions
- Temporal and contextual metadata (when, where, who)
- Sequential experience records
- "What happened" rather than "what is true"

<!-- section_id: "3f5f029a-df1e-4875-b277-8e40ad9ca25b" -->
### How It Works
- Records of specific episodes with timestamps
- Preserves temporal ordering and causal relationships
- Can be replayed, reflected upon, or summarized

<!-- section_id: "24a7ea1b-9c93-4e45-aea0-24ff9419aa2e" -->
### AI Implementations
- **Conversation history logs**: Raw chat transcripts with timestamps
- **SOAR EPMEM**: Automatic snapshots of working memory in temporal stream
- **Trajectory preservation**: Complete action-observation sequences
- **MemGPT Recall Memory**: Searchable interaction history
- **Reflexion episodic buffer**: Past trial results for self-improvement

<!-- section_id: "a9d7577a-2463-4af0-9eae-fae3f8793afd" -->
### Retrieval Patterns
- Temporal queries ("What happened yesterday?")
- Cue-based retrieval ("Similar to when we discussed X")
- Recency-weighted access

---

<!-- section_id: "e247f026-0d21-4568-b6a2-8c4a5a1370be" -->
## 3. Procedural Memory

<!-- section_id: "a8a6a6e1-771b-42b2-936a-cc7f7bd789e8" -->
### What It Stores
- "How-to" knowledge and skills
- Action sequences and tool-use patterns
- Problem-solving strategies
- Workflow templates

<!-- section_id: "23562ae0-6a41-4699-a112-46f108cf42d6" -->
### How It Works
- Encoded as production rules (SOAR), action policies, or tool-use patterns
- Often implicit - shapes behavior without explicit recall
- Learned through experience and reinforcement

<!-- section_id: "e30993b9-dbfd-4206-b7c4-2c22a4bd863a" -->
### AI Implementations
- **SOAR production rules**: IF-THEN condition-action pairs
- **ACT-R production memory**: Utility-weighted production rules
- **Tool-use patterns**: Learned sequences of API/tool calls
- **Code generation templates**: Learned coding patterns
- **ReAct patterns**: Reasoning + Acting sequences
- **Memp, ToolMem**: Papers on procedural memory for tool learning

<!-- section_id: "c8c16b5f-93e6-4f61-ba37-fa79479cae59" -->
### Retrieval Patterns
- Triggered by matching conditions (not explicit queries)
- Automatic activation when relevant context appears
- Skill transfer to novel but similar situations

---

<!-- section_id: "0eb673ef-a880-4e57-a34a-d83543dfedea" -->
## 4. Entity Memory

<!-- section_id: "97bb36dc-717f-4dd1-8d4b-8757e108d782" -->
### What It Stores
- Information about specific named entities (people, places, organizations, concepts)
- Attributes, properties, and relationships of entities
- Evolving summaries that update as new information arrives

<!-- section_id: "2d20d4c0-b3d9-4fe0-8c3d-8b878a3ea36d" -->
### How It Works
- Extracts named entities from conversations
- Maintains per-entity summaries that grow over time
- Links entities to their attributes and relationships

<!-- section_id: "d1f79283-5f02-4db9-8f06-e8834780b13b" -->
### AI Implementations
- **LangChain ConversationEntityMemory**: Extracts entities using LLM, builds evolving summaries, swappable entity store (in-memory, Redis, SQLite)
- **CrewAI Entity Memory** (legacy): RAG-based entity tracking for people, places, concepts
- **Knowledge graph entities**: Nodes in structured graphs
- **Mem0 entity tracking**: Entity-aware memory extraction

<!-- section_id: "c10707c9-cdc6-4341-a557-cac0d6dbecd5" -->
### Retrieval Patterns
- Entity name lookup
- Relationship queries between entities
- Attribute queries about specific entities

---

<!-- section_id: "63ec3ca5-266d-4e52-b500-50e56acd8a2f" -->
## 5. Experiential / Reflection Memory

<!-- section_id: "df82cda6-dba4-48a4-8050-262be904299d" -->
### What It Stores
- Insights derived from past experiences
- Self-reflections on successes and failures
- Abstracted lessons learned
- Meta-knowledge about effective strategies

<!-- section_id: "faef1293-6594-4ae6-81ba-dda6b67674a8" -->
### How It Works
- Generated through reflection on episodic memories
- Distills raw experience into actionable insights
- Progressive abstraction: episodes → reflections → principles

<!-- section_id: "352c7fa8-8e2d-49d1-80e3-ff8690f7d6a6" -->
### AI Implementations
- **Reflexion** (Shinn et al., NeurIPS 2023): Verbal self-reflection stored as context for future trials; linguistic feedback converted to improvement insights
- **SAGE**: Self-evolving reflective memory agents
- **Generative Agents** (Park et al.): Reflection mechanism that synthesizes observations into higher-level insights
- **Experience-level memory**: Trajectory abstraction (the "Experience" stage)

<!-- section_id: "7bfd080a-0db9-4f64-bbed-b48af5d327d6" -->
### Retrieval Patterns
- Relevance to current task/problem
- Recency and importance weighting
- Analogical matching to similar past situations

---

<!-- section_id: "b2ac05a1-4985-4c35-ad2a-ad9628dfe8fb" -->
## 6. Summary Memory

<!-- section_id: "6881b2cd-ab66-49b8-984e-3d6f1bc93381" -->
### What It Stores
- Condensed versions of longer interactions or documents
- Key points extracted from verbose content
- Progressive summaries that update with new information

<!-- section_id: "9fdc63f0-046a-4902-bc08-8ec413f0c6a5" -->
### How It Works
- LLM-generated summarization of content
- May be recursive (summaries of summaries)
- Trades detail for breadth of coverage

<!-- section_id: "5652ff2f-d0d8-47cf-a07f-50fbb5cb9422" -->
### AI Implementations
- **LangChain ConversationSummaryMemory**: Summarizes conversation history instead of storing verbatim
- **LangChain ConversationSummaryBufferMemory**: Hybrid - summarizes old messages, keeps recent ones raw
- **MemoryOS MTM segments**: Summarized content with metadata per topic cluster
- **Progressive summarization**: Layered compression of information

<!-- section_id: "e7695869-4002-4965-a024-fa8d0effa5a0" -->
### Retrieval Patterns
- Summary serves as the retrieval result (no further lookup needed)
- May index into original content for drill-down

---

<!-- section_id: "8b66e435-c5a6-4127-9da9-d0ba606c93a4" -->
## 7. Working / Scratchpad Memory

<!-- section_id: "527952cd-20f3-45bd-9644-1de1b8cd2631" -->
### What It Stores
- Intermediate computation results
- Current reasoning state
- Task-specific temporary data
- Plans and subgoals

<!-- section_id: "c0a6c6be-4ba8-4c0c-bbdf-faca71628970" -->
### How It Works
- Actively maintained during task execution
- Cleared or archived when task completes
- Supports chain-of-thought reasoning

<!-- section_id: "0b6b9482-eac8-4594-8f3c-fd66aab0091d" -->
### AI Implementations
- **Chain-of-thought scratchpads**: Intermediate reasoning steps
- **MemGPT Core Memory**: Agent-editable blocks pinned to context
- **SOAR Working Memory**: Central goal/state representation
- **Agent planning buffers**: Current plan, active subgoals

---

<!-- section_id: "d03f1d61-fe23-4194-810f-765dfda12590" -->
## 8. Persona / Profile Memory

<!-- section_id: "45d924dd-9959-40d4-a0f4-8597a87ef5b1" -->
### What It Stores
- User preferences and characteristics
- Agent identity and behavioral parameters
- Role-specific knowledge
- Communication style preferences

<!-- section_id: "b929e22e-5cb4-4590-996f-1dc160f11fe5" -->
### How It Works
- Extracted from interactions over time
- Used to personalize responses and behavior
- May include both static (name, role) and dynamic (evolving preferences) components

<!-- section_id: "5d28ba95-6f1b-4ea1-98e1-172bbd0ab9f8" -->
### AI Implementations
- **MemoryOS Long-Term Persona Memory**: Static profiles + dynamic knowledge + evolving traits
- **MemGPT Core Memory blocks**: `human` and `persona` blocks for user/agent identity
- **Mem0 user profiles**: Per-user preference tracking
- **Claude Memory**: User preference persistence across conversations

---

<!-- section_id: "1e3531a4-6493-40d6-891d-0accac445a31" -->
## 9. Contextual Memory

<!-- section_id: "7995a123-06b7-45ac-a3ef-34029e905555" -->
### What It Stores
- Background context relevant to current task
- Environmental state and constraints
- Metadata about the interaction setting

<!-- section_id: "1fac9a91-77ae-4915-b3c5-780a5f468d47" -->
### How It Works
- Synthesizes information from other memory types
- Provides situational awareness
- Adapts based on current task requirements

<!-- section_id: "209e8409-9a0f-44c0-942d-eaffbf38eae4" -->
### AI Implementations
- **CrewAI Contextual Memory** (legacy): Combined short-term + long-term + entity for situational context
- **System prompts**: Pre-loaded contextual information
- **CLAUDE.md files**: Project-specific context loaded per directory

---

<!-- section_id: "8581cb01-262b-4068-8fa8-e35b85b2e206" -->
## Content Type Relationships

```
Factual (what is) ←→ Episodic (what happened)
       ↓                      ↓
  Entity (who/what)    Experiential (what was learned)
       ↓                      ↓
  Summary (condensed)   Procedural (how to)
       ↓                      ↓
  Profile (who am I)   Working (what now)
```

---

<!-- section_id: "ade9eeef-81a8-4940-9a91-21f4f07b035a" -->
## Sources

- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [LangChain Entity Memory Documentation](https://python.langchain.com/v0.1/docs/modules/memory/types/entity_summary_memory/)
- [LangChain Conversational Memory Types (Pinecone)](https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/)
- [Agent Memory: How to Build Agents that Learn and Remember (Letta)](https://www.letta.com/blog/agent-memory)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
