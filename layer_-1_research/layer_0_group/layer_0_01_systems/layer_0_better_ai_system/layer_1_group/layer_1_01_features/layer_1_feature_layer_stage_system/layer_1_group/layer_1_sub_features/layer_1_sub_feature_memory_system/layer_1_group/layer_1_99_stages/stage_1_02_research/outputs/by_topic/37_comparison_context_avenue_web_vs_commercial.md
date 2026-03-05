---
resource_id: "85b11e39-11a7-43e0-8d09-fcb2e4f206b7"
resource_type: "output"
resource_name: "37_comparison_context_avenue_web_vs_commercial"
---
# Comparison: 8-Avenue Context Web vs Commercial Knowledge Organization Systems

<!-- section_id: "058c43e5-540b-41e1-bde6-50fb882ab178" -->
## Purpose

This document compares the user's **context avenue web** (8 numbered avenues for organizing AI agent knowledge, from 01_aalang through 08_hooks) combined with the `.0agnostic/` knowledge/rules/protocols structure, against how commercial AI agent systems organize their knowledge: Mem0's flat vector pool, LangChain's tools/chains/retrievers, CrewAI's tools/memory/tasks, RAG's chunking/embedding/retrieval pipeline, and AutoGen's agent configurations. The comparison focuses on a key architectural question: the user's system uses **explicit typing** (8 categories of context source, ordered by comprehensiveness) while commercial systems use **implicit organization** (everything is a vector, a tool, or a prompt). Where does each approach excel, and where could vector search augment the avenue web without replacing it?

---

<!-- section_id: "d1e92982-2f25-4e3f-adc2-550ca59c1a5a" -->
## 1. User's System Architecture: The Context Avenue Web

<!-- section_id: "7e6e6771-d296-40f1-b53a-3beccbb31cf8" -->
### The 8-Avenue Structure

The context avenue web lives at `.0agnostic/06_context_avenue_web/` and provides 8 distinct categories of context source, ordered from most comprehensive (full agent graphs) to most fragmented (event-triggered scripts):

| Avenue | Name | What It Contains | Comprehensiveness |
|--------|------|------------------|-------------------|
| 00 | Registry | Index of all avenues and their contents | Meta (index only) |
| 01 | AALang | `.gab.jsonld` files -- full agent graphs with modes, actors, personas, constraints | Highest -- complete agent definition |
| 02 | AALang Markdown Integration | `.integration.md` files -- human-readable summaries of agent graphs | High -- agent summary |
| 03 | Auto Memory | Claude Code auto-memory (`MEMORY.md` + topic files) | Medium -- operational learnings |
| 04 | @import References | External file imports referenced from context files | Medium -- cross-file links |
| 05 | Skills | `SKILL.md` files with WHEN/WHEN NOT conditions + instructions | Medium -- task-specific guidance |
| 06 | Agents | Agent configuration files (lightweight stubs, `.agent.jsonld`) | Medium-Low -- agent identity only |
| 07 | Path-Specific Rules | `.claude/rules/` files triggered by directory matching | Low -- triggered rules |
| 08 | Hooks | Shell commands triggered by events (pre-commit, post-save) | Lowest -- event scripts |

<!-- section_id: "a5adc1ac-b298-4278-9ad8-eab1ac2d3ab9" -->
### The Broader .0agnostic/ Structure

The avenue web is one of 7 top-level categories:

| Directory | Purpose | Relation to Avenue Web |
|-----------|---------|----------------------|
| **01_knowledge/** | Per-topic knowledge: principles, docs, resources, templates, tools | Raw knowledge the avenues reference |
| **02_rules/** | Static rules (always apply), dynamic rules (triggered), scenario-based | Rule definitions that 07_path_specific_rules deploys |
| **03_protocols/** | Step-by-step procedures (stage reports, research methodology) | Procedural knowledge (like skills but more structured) |
| **04_episodic_memory/** | Session records and change logs | Temporal context |
| **05_handoff_documents/** | Incoming (from_above, from_below) and outgoing (to_above, to_below) | Inter-entity communication |
| **06_context_avenue_web/** | The 8 avenues above | Context delivery mechanisms |
| **07+_setup_dependant/** | Tool-specific setup, environment configs | Infrastructure |

<!-- section_id: "5c67d47d-6d13-48fc-8a3a-cb588d41b446" -->
### Key Design Properties

1. **Explicit typing**: Every piece of context has a designated avenue (agent graphs go in 01, skills go in 05, hooks go in 08). There is no "miscellaneous" bucket.

2. **Comprehensiveness ordering**: Avenue 01 (full agent graphs with modes, constraints, transitions) contains the most context per item; avenue 08 (shell scripts triggered by events) contains the least. An agent wanting maximum understanding reads avenue 01; an agent wanting quick task matching reads avenue 05.

3. **Deterministic lookup**: Finding a skill means looking in `05_skills/`. Finding agent constraints means querying `.gab.jsonld` in `01_aalang/`. No search algorithm needed.

4. **Separation of content from delivery**: Knowledge lives in `01_knowledge/`, rules live in `02_rules/`, protocols live in `03_protocols/`. The avenue web (`06_context_avenue_web/`) is about HOW context reaches the agent, not WHAT the context is.

5. **Agent-agnostic**: The same 8 avenues serve Claude (via CLAUDE.md + .claude/ rules), Gemini (via GEMINI.md), Cursor (via .cursor/), and GPT (via OPENAI.md). The avenue definitions are tool-neutral; only the delivery mechanism changes.

6. **Auditable**: Every piece of context is a file with a path. You can `git log` any avenue to see its history. You can diff two entities' avenue configurations. You can verify that a rule was applied by checking the file exists at the expected path.

---

<!-- section_id: "4a7d1b19-376a-425b-9318-432a956acedb" -->
## 2. Commercial Systems: How They Organize Knowledge

<!-- section_id: "0052b608-0686-4a05-b813-554b314c53f9" -->
### 2.1 Mem0: Flat Vector Pool

**Organization model**: All knowledge is stored as vector embeddings in a single pool, scoped by `user_id`, `session_id`, and `agent_id`. No categories, no types, no hierarchy.

**Knowledge types supported**:
- User preferences and facts
- Conversation-extracted memories
- Session-specific context

**How agents access knowledge**: Embed the current query, find top-k similar vectors, inject into prompt. There is no distinction between "this is a rule" and "this is a fact" and "this is a procedure" -- they are all vectors.

**Organization mechanism**: Tags and metadata fields can be attached to memories, but there is no enforced schema. Organization depends entirely on what the LLM extracts.

<!-- section_id: "bd20cb4d-e25d-4339-88f9-c0f3afcc9dd4" -->
### 2.2 LangChain: Tools + Chains + Retrievers

**Organization model**: Knowledge is organized through three mechanism types:

| Mechanism | What It Is | Closest Avenue Equivalent |
|-----------|-----------|--------------------------|
| **Tools** | Function definitions with descriptions and schemas | 05_skills (WHEN conditions + instructions) |
| **Chains** | Sequences of LLM calls with templates | 03_protocols (step-by-step procedures) |
| **Retrievers** | Vector stores, SQL queries, or API calls that fetch context | No equivalent (user has no retrieval layer) |
| **Memory** (via LangMem) | PostgresStore with namespace-scoped vector memories | 03_auto_memory + 04_episodic_memory (partial) |
| **Agents** | ReAct or function-calling agents that choose tools | 01_aalang + 06_agents (agent definitions) |

**How agents access knowledge**: Through explicit tool calls (agent decides when to search), retriever chains (automatic context injection), or memory tools (store/retrieve by namespace).

**Key difference from avenue web**: LangChain does not separate WHAT knowledge is from HOW it is accessed. A "retriever" is both the knowledge and the access mechanism bundled together.

<!-- section_id: "c97a7c4c-42b3-4888-8de7-5c5947cdb25b" -->
### 2.3 CrewAI: Tools + Memory + Tasks

**Organization model**: Knowledge is split across four mechanisms:

| Mechanism | What It Is | Closest Avenue Equivalent |
|-----------|-----------|--------------------------|
| **Tools** | Python functions agents can call | 05_skills |
| **Memory** | 5 types: Short-Term (RAG), Long-Term (SQLite3), Entity (RAG), Contextual, User | 04_episodic_memory + 03_auto_memory |
| **Tasks** | Structured work units with descriptions, expected output, agents | Stages (01-11) |
| **Knowledge Sources** | Documents loaded into agent context (PDF, TXT, CSV) | 01_knowledge/ docs |

**How agents access knowledge**: Automatic retrieval using weighted formula: recency (0.4) + semantic similarity (0.4) + importance (0.2). All agents in a crew share the same memory instance.

**Key difference from avenue web**: CrewAI's memory is implicit -- agents do not choose what to remember or what type a memory is. The system classifies automatically. The avenue web requires explicit placement.

<!-- section_id: "2b34aa24-01bf-44a0-a4e7-3d467f0cf2ee" -->
### 2.4 RAG (Retrieval-Augmented Generation): Chunk + Embed + Retrieve

**Organization model**: No organization per se. Documents are:
1. **Chunked** into 256-1024 token segments
2. **Embedded** into vector representations
3. **Stored** in a vector database
4. **Retrieved** by similarity to the current query

**How agents access knowledge**: Automatic injection of top-k relevant chunks before each LLM call. The agent does not know where the knowledge came from, only that relevant context appeared in its prompt.

**Key difference from avenue web**: RAG has no concept of knowledge types. A rule chunk, a research finding chunk, and a session log chunk are all treated identically -- they differ only in their vector positions. The avenue web explicitly distinguishes between rules (02), knowledge (01), protocols (03), and skills (05).

<!-- section_id: "b0574953-16fd-405e-8fc0-4eb8959d6d7c" -->
### 2.5 AutoGen: Agent Configurations

**Organization model**: Knowledge is embedded in agent definitions:

| Mechanism | What It Is | Closest Avenue Equivalent |
|-----------|-----------|--------------------------|
| **System messages** | Agent identity and instructions | 0AGNOSTIC.md STATIC section |
| **Function schemas** | Tools the agent can call | 05_skills + 08_hooks |
| **Teachable agents** | Agents that store user corrections in a text DB | 03_auto_memory |
| **Group chat** | Multiple agents share a conversation thread | 05_handoff_documents |
| **Agent configs** | YAML/JSON defining agent roles and tools | 01_aalang + 06_agents |

**How agents access knowledge**: System messages provide identity; tools provide capabilities; group chat provides shared context. There is no persistent memory layer by default -- context exists only within the conversation.

**Key difference from avenue web**: AutoGen's knowledge is conversation-scoped. When the conversation ends, knowledge is lost unless explicitly stored. The avenue web is persistent by design -- every avenue is a file on disk.

---

<!-- section_id: "8f00a716-6677-45e9-8d8e-9560715fd80e" -->
## 3. Comparison Table: Avenue Web vs Commercial Systems

| Dimension | Avenue Web (.0agnostic) | Mem0 | LangChain | CrewAI | RAG | AutoGen |
|-----------|------------------------|------|-----------|--------|-----|---------|
| **Knowledge typing** | 8 explicit categories ordered by comprehensiveness | None (all vectors) | 3 types (tools, chains, retrievers) | 4 types (tools, memory, tasks, knowledge) | None (all chunks) | 3 types (system msg, functions, teachable) |
| **Organization structure** | Hierarchical directories with numbered ordering | Flat pool with tags | Graph of chains and tools | Flat lists per type | Flat vector store | Per-agent config files |
| **Discovery mechanism** | Deterministic path lookup | Semantic similarity | Tool descriptions + similarity | Weighted multi-factor formula | Cosine similarity | Function schema matching |
| **Semantic search** | None | Core feature | Core feature | Core feature | Core feature | None |
| **Type enforcement** | Strict (rules in 02/, skills in 05/, agents in 01/) | None | Loose (any LangChain class) | Medium (type fields) | None | Loose (convention) |
| **Cross-type queries** | Manual (read from different directories) | Automatic (all in one pool) | Via chain composition | Via shared memory | Automatic (all chunks equal) | Via group chat |
| **Persistence** | Full (filesystem + git) | Full (vector DB) | Full (PostgreSQL) | Partial (SQLite3) | Full (vector DB) | Session-only (unless saved) |
| **Auditability** | Full (git history, file diffs, line-by-line) | Low (vector embeddings opaque) | Medium (DB records) | Low (internal stores) | Low (chunks opaque) | Medium (config files) |
| **Human editability** | Full (plain markdown) | None | Low (code/DB) | None | None | Low (config files) |
| **Multi-tool support** | Native (agnostic-sync generates per-tool) | API-only | LangChain ecosystem | CrewAI only | Framework-agnostic | AutoGen only |
| **Agent identity** | Full GAB graphs (modes, actors, personas, states) | None | ReAct agent definitions | Role + backstory + goal | None | System message |
| **Context scoping** | Hierarchical (root cascades to leaf) | Per user/session/agent | Per namespace | Per crew | Per collection | Per conversation |
| **Setup complexity** | Zero external deps (just files) | Medium (vector DB + LLM) | High (Python + PostgreSQL) | Low (pip install) | Medium (vector DB) | Low (pip install) |

---

<!-- section_id: "e3c92bc0-575f-45b5-9ec2-59cecbfb47e3" -->
## 4. Analysis: Where Each Approach Excels

<!-- section_id: "b06e6693-fc70-40f9-9869-c08cb101ee63" -->
### 4.1 Where the Avenue Web is Ahead

**Deterministic, auditable context delivery**

The avenue web provides something no commercial system offers: you can trace exactly which context an agent received and why. If an agent makes a mistake, you check: "Did it load the right .gab.jsonld? Did the SKILL.md WHEN condition match? Was the rule in 02_rules/ applicable?" Every step is a file read with a path. In Mem0, you cannot explain why a particular memory was retrieved beyond "it had high cosine similarity."

**Explicit knowledge typing with comprehensiveness ordering**

The 8 avenues are not arbitrary categories -- they are ordered by how much context each type provides. Avenue 01 (full agent graphs) gives the agent its complete identity, constraints, and transitions. Avenue 05 (skills) gives a specific task procedure. Avenue 08 (hooks) gives a one-line shell command. This ordering lets an agent choose its depth of context loading: read avenue 01 for deep understanding, read avenue 05 for quick task matching. No commercial system provides this graduated context scale.

**Agent-agnostic delivery**

The same knowledge (0AGNOSTIC.md -> .0agnostic/) serves Claude, Gemini, GPT, and Cursor through tool-specific sync. Mem0's API works with any LLM but requires its own SDK. LangChain locks you into its ecosystem. CrewAI locks you into its framework. The avenue web is the only system where changing your AI tool requires zero knowledge reorganization.

**Separation of content from delivery**

`01_knowledge/` holds the knowledge. `02_rules/` holds the rules. `06_context_avenue_web/` holds the delivery mechanisms. This separation means you can change how context is delivered (add a new tool, change the sync format) without touching the knowledge itself. In LangChain, knowledge is embedded inside retriever objects. In CrewAI, memory types are implementation classes. Changing the delivery mechanism means rewriting knowledge access code.

**Full version control**

Every change to any avenue is a git commit with a diff. You can `git blame` a rule to see when it was added and why. You can `git log 05_skills/entity-creation/SKILL.md` to trace skill evolution. Vector databases (Mem0, RAG) have no equivalent history mechanism.

<!-- section_id: "5a4caa85-0012-4933-924e-66e19c25dbde" -->
### 4.2 Where the Avenue Web Falls Behind

**No semantic search across avenues**

This is the single largest gap. An agent looking for "how to handle memory decay" must know that the answer is in `01_knowledge/` or in a specific research document. In Mem0 or RAG, the same query returns relevant content regardless of where it was stored. The avenue web's deterministic lookup requires prior knowledge of the system's structure.

**Manual curation required**

Every piece of knowledge must be explicitly placed in the right avenue by a human. Agent graphs go in 01, skills go in 05, rules go in 02. If a human places a rule in the wrong directory, or forgets to create a skill, the system has no self-correction mechanism. Mem0 automatically extracts and stores memories. CrewAI automatically categorizes context. RAG automatically chunks and embeds documents.

**No relevance scoring**

When an agent reads avenue 05 (skills), it reads ALL skills and manually checks WHEN conditions. There is no relevance score, no ranking, no "this skill is 93% relevant to your current task." CrewAI's weighted formula (recency + similarity + importance) provides exactly this graduated relevance.

**No cross-avenue retrieval**

If the answer to a question spans knowledge (01), a rule (02), and a skill (05), the agent must explicitly read from three different directories. In Mem0 or RAG, all content lives in one pool and a single query returns results from any source type.

**No automatic memory extraction**

After an agent session, no knowledge is automatically added to any avenue. The human must manually update `01_knowledge/`, create rules in `02_rules/`, write skills in `05_skills/`, and log sessions in `04_episodic_memory/`. Mem0, MongoDB AI, and CrewAI all extract and store memories automatically.

**Scale limitations**

The avenue web works well with tens of files per avenue. At hundreds of files per avenue, manual navigation becomes impractical. Vector databases scale to millions of records with sub-200ms retrieval.

<!-- section_id: "30ad6bdc-639f-4b5c-b404-2af394b62655" -->
### 4.3 Where Vector Search Could Augment (Not Replace) the Avenue Web

The critical insight: the avenue web's explicit typing and vector search's semantic discovery are **complementary**, not competing. The recommendation is to add vector search as an overlay that preserves avenue boundaries while enabling cross-avenue discovery.

**Augmentation 1: Intra-avenue semantic search**

Keep the 8-avenue structure. Within each avenue, embed the contents and enable similarity search:

```sql
-- "Find the most relevant skill for this task"
SELECT skill_name, match_score
FROM skills_embeddings
WHERE avenue = '05_skills'
ORDER BY embedding <=> task_embedding
LIMIT 3;
```

This preserves type enforcement (only skills are returned) while adding relevance ranking.

**Augmentation 2: Cross-avenue discovery with type labels**

Allow semantic search across all avenues but return results with their avenue type:

```sql
SELECT content_summary, avenue_type, file_path, match_score
FROM avenue_content_embeddings
ORDER BY embedding <=> query_embedding
LIMIT 10;
-- Returns: "STAGE_REPORT_RULE" (avenue: 02_rules, score: 0.91)
--          "entity-creation" (avenue: 05_skills, score: 0.87)
--          "ReceiveMode constraints" (avenue: 01_aalang, score: 0.82)
```

The agent sees both the relevant content AND its type, letting it decide how to use it (a rule must be followed; a skill can be invoked; an agent graph defines constraints).

**Augmentation 3: Avenue-weighted relevance**

Weight search results by avenue comprehensiveness:

```
effective_score = cosine_similarity * avenue_weight

Avenue weights (configurable):
  01_aalang:     1.0  (most comprehensive)
  02_integration: 0.9
  03_auto_memory: 0.7
  04_imports:    0.6
  05_skills:     0.8  (high utility)
  06_agents:     0.5
  07_rules:      0.9  (high importance)
  08_hooks:      0.3  (least comprehensive)
```

This means a high-similarity match in avenue 01 (full agent graph) outranks a slightly-higher-similarity match in avenue 08 (hook script), reflecting the comprehensiveness ordering.

**Augmentation 4: Bloom filter pre-check per avenue**

Before searching an avenue's embeddings, check a Bloom filter:

```python
for avenue in avenues:
    if avenue.bloom_filter.might_contain(task_keywords):
        results += semantic_search(avenue, query)
    # else: skip this avenue entirely -- save compute
```

This combines the avenue web's deterministic structure with SHIMI's efficient pre-filtering.

---

<!-- section_id: "c2d8d4b1-833d-41d5-a1d5-a16f7bcba9ee" -->
## 5. Detailed Comparison: Knowledge Discovery Workflows

<!-- section_id: "d44968cd-9427-43f8-a009-a35926d8791d" -->
### Workflow: "Agent needs to understand its role"

| System | Steps | Context Quality |
|--------|-------|----------------|
| **Avenue Web** | Read 01_aalang/*.gab.jsonld -> get modes, actors, personas, constraints. Read 02_aalang_markdown_integration/*.integration.md for summary. | Highest -- full agent graph with state machine |
| **Mem0** | Search memories for agent_id. Get flat list of past interactions. | Low -- no structured role definition |
| **LangChain** | Read system message in agent config. | Medium -- text description only |
| **CrewAI** | Read role + backstory + goal fields. | Medium -- structured but shallow |
| **RAG** | Retrieve relevant document chunks. | Low -- fragments without structure |
| **AutoGen** | Read system_message in config. | Medium -- text description only |

<!-- section_id: "90e02f3d-7aa0-42cd-881d-2b5731795894" -->
### Workflow: "Agent needs a procedure for the current task"

| System | Steps | Context Quality |
|--------|-------|----------------|
| **Avenue Web** | Check 05_skills/ WHEN conditions. Read matching SKILL.md. Also check 03_protocols/ for step-by-step procedures. | High -- explicit match with clear instructions |
| **Mem0** | Semantic search for similar past procedures. | Medium -- may find relevant past actions |
| **LangChain** | Agent selects tool by description match. Chain provides sequence. | High -- structured tool selection |
| **CrewAI** | Tool descriptions matched to task. | Medium -- description-based |
| **RAG** | Retrieve chunks about the procedure. | Low -- may get fragments |
| **AutoGen** | Function schema matched by name/description. | Medium -- schema-based |

<!-- section_id: "075daf77-6921-48c5-afcb-f4c43aac075c" -->
### Workflow: "Agent needs to find related work in other parts of the system"

| System | Steps | Context Quality |
|--------|-------|----------------|
| **Avenue Web** | Must know the path. Check 04_@import_references or manually navigate. | Low -- requires prior structural knowledge |
| **Mem0** | Single semantic search finds related memories regardless of location. | High -- location-agnostic |
| **LangChain** | Search across namespace-scoped memories. | Medium -- limited to configured namespaces |
| **CrewAI** | Shared memory across crew finds related context. | Medium -- limited to crew scope |
| **RAG** | Single query across all embedded documents. | High -- location-agnostic |
| **AutoGen** | No cross-agent search. Must be in same group chat. | Low -- conversation-scoped |

---

<!-- section_id: "c8e54587-1369-4784-bc03-2edaac7ee77f" -->
## 6. Recommendations

<!-- section_id: "913538f2-a85e-4dbc-8746-df8423f7ddc7" -->
### Keep the Avenue Web's Strengths

1. **Maintain explicit typing** -- the 8-avenue structure provides clarity that no commercial system matches
2. **Preserve deterministic lookup** -- path-based access is fast, predictable, and debuggable
3. **Keep human editability** -- plain markdown is the system's most distinctive advantage
4. **Retain agent-agnostic delivery** -- the agnostic-sync pipeline is unmatched in the industry

<!-- section_id: "5aa0ec18-c395-4ae0-8e52-4243ada2feca" -->
### Add What It Lacks

1. **Embed all avenue contents** -- generate vector embeddings for every file in every avenue. Store in a pgvector table alongside the files (filesystem remains source of truth). Enable `SELECT * FROM avenue_embeddings WHERE avenue = '05_skills' ORDER BY embedding <=> query LIMIT 3`.

2. **Implement cross-avenue discovery** -- a single search endpoint that queries all 8 avenues, returns results with avenue type labels and comprehensiveness scores. This directly addresses the largest weakness without restructuring anything.

3. **Add automatic extraction** -- a post-session hook (avenue 08) that proposes knowledge additions to the relevant avenues. The human reviews and approves, maintaining curation quality while reducing manual effort.

4. **Add relevance scoring to skills** -- instead of reading all SKILL.md files and checking WHEN conditions sequentially, embed skills and match by similarity. Keep WHEN conditions as a hard filter; use similarity as a soft ranking within matching skills.

5. **Build an avenue index** -- a lightweight registry at `00_context_avenue_web_registry/` that maps concepts to avenues and files. Queryable by keyword or (with embeddings) by semantic similarity. This is the avenue web equivalent of a search index.

<!-- section_id: "cfeb2350-8aa0-4151-9cf3-f4e42e56082f" -->
### Integration Architecture

```
Filesystem (source of truth)        PostgreSQL (queryable index)
================================    ================================
.0agnostic/                         avenue_content_embeddings
  01_knowledge/  ─── embed ──────>    (file_path, avenue_type,
  02_rules/      ─── embed ──────>     content_summary, embedding,
  03_protocols/  ─── embed ──────>     importance_level,
  05_skills/     ─── embed ──────>     bloom_filter_hash)
  06_context_avenue_web/
    01_aalang/    ─── embed ──────>  gab_agent_embeddings
    02_integration/ ─ embed ──────>    (agent_id, mode, embedding)
    05_skills/   ─── embed ──────>  skill_embeddings
    07_rules/    ─── embed ──────>    (skill_name, when_cond, embedding)

agnostic-sync.sh                    sync_to_pgvector.sh
  0AGNOSTIC.md -> CLAUDE.md           .md files -> embeddings
  (deterministic)                     (on-commit hook)
```

The filesystem + git provides: version control, human editing, tool generation, auditability.
The pgvector index provides: semantic search, cross-avenue discovery, relevance scoring.
Neither replaces the other.

---

<!-- section_id: "a0198a48-205b-4359-ae4d-d90fea8e500d" -->
## Sources

- [Mem0 GitHub Repository](https://github.com/mem0ai/mem0) -- flat vector pool memory system
- [LangChain Documentation](https://python.langchain.com/docs/) -- tools, chains, retrievers architecture
- [CrewAI Documentation](https://docs.crewai.com/) -- tools, memory, tasks, knowledge sources
- [AutoGen Documentation](https://microsoft.github.io/autogen/) -- agent configurations and group chat
- [pgvector](https://github.com/pgvector/pgvector) -- PostgreSQL vector similarity extension
- [RAG Survey (arXiv)](https://arxiv.org/) -- retrieval-augmented generation architectures
- Perplexity AI research conversations (Feb 2026) -- commercial system architecture details
- Previous research docs in this series: 32 (context chain comparison), 23 (core AI memory systems), 07 (commercial AI memory)
