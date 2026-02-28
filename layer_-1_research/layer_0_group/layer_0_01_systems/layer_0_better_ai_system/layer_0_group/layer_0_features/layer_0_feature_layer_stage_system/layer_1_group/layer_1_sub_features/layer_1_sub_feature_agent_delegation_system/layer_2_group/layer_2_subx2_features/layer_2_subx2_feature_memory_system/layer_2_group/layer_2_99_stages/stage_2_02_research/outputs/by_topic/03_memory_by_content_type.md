# Memory Types by Content / Function

## Overview

Memory systems categorized by what kind of information they store and what purpose they serve, regardless of duration or storage mechanism.

---

## 1. Factual / Semantic Memory

### What It Stores
- Objective facts about the world
- Definitions, concepts, relationships
- Domain knowledge, encyclopedic information
- Decontextualized general knowledge

### How It Works
- Stored as structured facts, knowledge graph triples, or embedded in model weights
- Retrieved by topical relevance rather than temporal context
- Updated through knowledge editing or external database modification

### AI Implementations
- **Parametric knowledge**: Facts encoded in LLM weights during pretraining
- **Knowledge graphs**: Entity-relationship triples (e.g., Neo4j, Amazon Neptune)
- **RAG document stores**: Indexed factual documents for retrieval
- **LangChain ConversationKGMemory**: Extracts and maintains a knowledge graph from conversations
- **Wikipedia/knowledge base integrations**: External factual sources

### Retrieval Patterns
- Entity-based queries ("What do we know about X?")
- Relationship traversal ("How are X and Y connected?")
- Semantic similarity search

---

## 2. Episodic Memory

### What It Stores
- Specific past events and interactions
- Temporal and contextual metadata (when, where, who)
- Sequential experience records
- "What happened" rather than "what is true"

### How It Works
- Records of specific episodes with timestamps
- Preserves temporal ordering and causal relationships
- Can be replayed, reflected upon, or summarized

### AI Implementations
- **Conversation history logs**: Raw chat transcripts with timestamps
- **SOAR EPMEM**: Automatic snapshots of working memory in temporal stream
- **Trajectory preservation**: Complete action-observation sequences
- **MemGPT Recall Memory**: Searchable interaction history
- **Reflexion episodic buffer**: Past trial results for self-improvement

### Retrieval Patterns
- Temporal queries ("What happened yesterday?")
- Cue-based retrieval ("Similar to when we discussed X")
- Recency-weighted access

---

## 3. Procedural Memory

### What It Stores
- "How-to" knowledge and skills
- Action sequences and tool-use patterns
- Problem-solving strategies
- Workflow templates

### How It Works
- Encoded as production rules (SOAR), action policies, or tool-use patterns
- Often implicit - shapes behavior without explicit recall
- Learned through experience and reinforcement

### AI Implementations
- **SOAR production rules**: IF-THEN condition-action pairs
- **ACT-R production memory**: Utility-weighted production rules
- **Tool-use patterns**: Learned sequences of API/tool calls
- **Code generation templates**: Learned coding patterns
- **ReAct patterns**: Reasoning + Acting sequences
- **Memp, ToolMem**: Papers on procedural memory for tool learning

### Retrieval Patterns
- Triggered by matching conditions (not explicit queries)
- Automatic activation when relevant context appears
- Skill transfer to novel but similar situations

---

## 4. Entity Memory

### What It Stores
- Information about specific named entities (people, places, organizations, concepts)
- Attributes, properties, and relationships of entities
- Evolving summaries that update as new information arrives

### How It Works
- Extracts named entities from conversations
- Maintains per-entity summaries that grow over time
- Links entities to their attributes and relationships

### AI Implementations
- **LangChain ConversationEntityMemory**: Extracts entities using LLM, builds evolving summaries, swappable entity store (in-memory, Redis, SQLite)
- **CrewAI Entity Memory** (legacy): RAG-based entity tracking for people, places, concepts
- **Knowledge graph entities**: Nodes in structured graphs
- **Mem0 entity tracking**: Entity-aware memory extraction

### Retrieval Patterns
- Entity name lookup
- Relationship queries between entities
- Attribute queries about specific entities

---

## 5. Experiential / Reflection Memory

### What It Stores
- Insights derived from past experiences
- Self-reflections on successes and failures
- Abstracted lessons learned
- Meta-knowledge about effective strategies

### How It Works
- Generated through reflection on episodic memories
- Distills raw experience into actionable insights
- Progressive abstraction: episodes → reflections → principles

### AI Implementations
- **Reflexion** (Shinn et al., NeurIPS 2023): Verbal self-reflection stored as context for future trials; linguistic feedback converted to improvement insights
- **SAGE**: Self-evolving reflective memory agents
- **Generative Agents** (Park et al.): Reflection mechanism that synthesizes observations into higher-level insights
- **Experience-level memory**: Trajectory abstraction (the "Experience" stage)

### Retrieval Patterns
- Relevance to current task/problem
- Recency and importance weighting
- Analogical matching to similar past situations

---

## 6. Summary Memory

### What It Stores
- Condensed versions of longer interactions or documents
- Key points extracted from verbose content
- Progressive summaries that update with new information

### How It Works
- LLM-generated summarization of content
- May be recursive (summaries of summaries)
- Trades detail for breadth of coverage

### AI Implementations
- **LangChain ConversationSummaryMemory**: Summarizes conversation history instead of storing verbatim
- **LangChain ConversationSummaryBufferMemory**: Hybrid - summarizes old messages, keeps recent ones raw
- **MemoryOS MTM segments**: Summarized content with metadata per topic cluster
- **Progressive summarization**: Layered compression of information

### Retrieval Patterns
- Summary serves as the retrieval result (no further lookup needed)
- May index into original content for drill-down

---

## 7. Working / Scratchpad Memory

### What It Stores
- Intermediate computation results
- Current reasoning state
- Task-specific temporary data
- Plans and subgoals

### How It Works
- Actively maintained during task execution
- Cleared or archived when task completes
- Supports chain-of-thought reasoning

### AI Implementations
- **Chain-of-thought scratchpads**: Intermediate reasoning steps
- **MemGPT Core Memory**: Agent-editable blocks pinned to context
- **SOAR Working Memory**: Central goal/state representation
- **Agent planning buffers**: Current plan, active subgoals

---

## 8. Persona / Profile Memory

### What It Stores
- User preferences and characteristics
- Agent identity and behavioral parameters
- Role-specific knowledge
- Communication style preferences

### How It Works
- Extracted from interactions over time
- Used to personalize responses and behavior
- May include both static (name, role) and dynamic (evolving preferences) components

### AI Implementations
- **MemoryOS Long-Term Persona Memory**: Static profiles + dynamic knowledge + evolving traits
- **MemGPT Core Memory blocks**: `human` and `persona` blocks for user/agent identity
- **Mem0 user profiles**: Per-user preference tracking
- **Claude Memory**: User preference persistence across conversations

---

## 9. Contextual Memory

### What It Stores
- Background context relevant to current task
- Environmental state and constraints
- Metadata about the interaction setting

### How It Works
- Synthesizes information from other memory types
- Provides situational awareness
- Adapts based on current task requirements

### AI Implementations
- **CrewAI Contextual Memory** (legacy): Combined short-term + long-term + entity for situational context
- **System prompts**: Pre-loaded contextual information
- **CLAUDE.md files**: Project-specific context loaded per directory

---

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

## Sources

- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [LangChain Entity Memory Documentation](https://python.langchain.com/v0.1/docs/modules/memory/types/entity_summary_memory/)
- [LangChain Conversational Memory Types (Pinecone)](https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/)
- [Agent Memory: How to Build Agents that Learn and Remember (Letta)](https://www.letta.com/blog/agent-memory)
- [Memory OS of AI Agent (arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
