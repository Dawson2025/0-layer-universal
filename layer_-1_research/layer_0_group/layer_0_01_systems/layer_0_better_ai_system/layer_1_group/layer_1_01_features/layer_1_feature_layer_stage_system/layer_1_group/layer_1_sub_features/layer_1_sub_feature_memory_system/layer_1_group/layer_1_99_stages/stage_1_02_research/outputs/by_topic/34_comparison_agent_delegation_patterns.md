---
resource_id: "8da4050f-8535-4758-9b9a-75eb5b136a9d"
resource_type: "output"
resource_name: "34_comparison_agent_delegation_patterns"
---
# Comparison: Agent Delegation Patterns -- User's System vs Multi-Agent Frameworks

## Purpose

Compare the user's layer-stage delegation system with established multi-agent frameworks (AutoGen, CrewAI, LangGraph, OASIS, ATLAS) across delegation architecture, memory sharing, context transfer, and orchestration patterns. Identify where the user's system excels, where it falls short, and what hybrid improvements could bridge the gaps.

---

## 1. Overview of User's System

The user's agent delegation system is a **hierarchical manager-to-stage-agent architecture** organized across layers and stages:

- **Layer-stage hierarchy**: Manager agents delegate to stage agents (stages 01-11: request_gathering through archives). Each stage is a self-contained unit with its own identity, methodology, and success criteria defined in a `0AGNOSTIC.md` file.
- **Manager isolation**: Managers do not carry operational knowledge. They delegate to stage agents and read stage reports (`outputs/reports/stage_report.md`) for async status updates, without loading full stage context.
- **Three-tier knowledge**: Pointers (`0AGNOSTIC.md`) point to distilled summaries (`.0agnostic/01_knowledge/`) which point to full stage outputs. This prevents context overload.
- **Handoff documents**: Located at `.0agnostic/05_handoff_documents/` with directional subdirs (`01_incoming/{from_above,from_below}`, `02_outgoing/{to_above,to_below}`), these carry structured context between layers.
- **GAB/AALang agent definitions**: JSON-LD graphs define agent modes, actors, personas, and constraints. Entity-level uses a 5-mode-13-actor pattern (ReceiveMode, ResearchMode, DesignMode, ImplementMode, ReviewMode). Stage-level uses a simpler 3-mode-7-actor pattern (ReceiveMode, ExecuteMode, ReportMode).
- **File-system-as-structure**: The directory hierarchy IS the delegation structure. Paths encode layer, feature, sub-feature, and stage relationships.
- **Scope boundary rule**: When agents hit layer or stage boundaries, they decide: do it yourself (small/coupled), delegate (significant, agent exists), or instantiate (significant, no agent).

---

## 2. Overview of Alternative Approaches

### AutoGen (Microsoft)

AutoGen uses a **GroupChat** pattern where multiple agents share a conversation history. A GroupChatManager routes messages based on role-based specialization. Agents include admin, planner, developer, executor, and QA roles. Memory is shared through the message list -- all agents see the full conversation. Teachable agents can persist user instructions across sessions. Context is flat and cumulative rather than hierarchical.

### CrewAI

CrewAI organizes agents into **crews** with defined tasks. It has a built-in `Memory` class with configurable weights (recency, semantic, importance) and decay rates. Memory types include short-term (RAG), long-term (SQLite3), entity memory (RAG), contextual memory, and user memory. All crew members share memory through a scope hierarchy. Task results flow sequentially -- completed task outputs become available to subsequent tasks. Delegation is task-based, not stage-based.

### LangGraph

LangGraph models agent orchestration as a **state machine graph**. Nodes are agents or functions; edges encode transitions with conditional logic. State is the shared context accessible by all nodes. Checkpointing enables resumption and human-in-the-loop interrupts. Cross-thread memory stores allow sharing context across conversation threads. The graph structure explicitly defines the execution flow rather than relying on free-form delegation.

### OASIS (AWS)

OASIS is a **production IT incident management** system using LangGraph, Amazon Bedrock, and OpenSearch. It has two specialized agents (monitoring + deployment specialist) coordinated through a state machine. Memory is stored in OpenSearch across three indices: raw event logs (episodic), system metrics (time-series), and agent findings (semantic + procedural). Status transitions track incident lifecycle. Human-in-the-loop approval gates exist for critical actions.

### ATLAS (Academic Task and Learning Agent System)

ATLAS uses **four specialized agents**: coordinator (routes queries using semantic understanding), planner (creates schedules from episodic performance data), notewriter (generates notes based on learning style), and advisor (provides guidance using procedural memory). The coordinator acts as a router rather than a hierarchical manager. Each agent maintains its own memory type specialization.

---

## 3. Comparison Table

| Dimension | User's System | AutoGen | CrewAI | LangGraph | OASIS | ATLAS |
|-----------|--------------|---------|--------|-----------|-------|-------|
| **Delegation model** | Hierarchical manager-to-stage (tree) | Flat GroupChat with manager routing | Task-sequential with crew manager | State machine graph (DAG) | Two-agent state machine | Router-to-specialist (star) |
| **Agent count** | 11 stages per entity + child entities | Variable (typically 3-6) | Variable per crew (2-5 typical) | Variable per graph (2-10 typical) | 2 specialized agents | 4 fixed agents |
| **Manager knowledge** | Isolated -- reads reports only | Full conversation history | Full crew memory | Full graph state | Full incident state | Coordinator sees all queries |
| **Context transfer** | Handoff documents + stage reports (async, file-based) | Shared message list (sync) | Task result chain (sync) | Graph state (sync) | OpenSearch shared store (async) | Function call returns (sync) |
| **Memory architecture** | Three-tier markdown (pointer, distilled, full) | Conversation history + teachable memory | Unified Memory class (5 types, weighted) | Graph state + checkpoints + cross-thread store | OpenSearch (3 index types) | Per-agent type specialization |
| **Agent identity** | GAB JSON-LD with modes, actors, personas, constraints | Role string + system prompt | Role + goal + backstory | Node function definition | Agent configuration | Agent role + tools |
| **Orchestration** | Sequential stages (01-11), parallel within stages via rules | Round-robin or manager-selected | Sequential task chain | Explicit graph edges with conditions | Event-driven state transitions | Coordinator routing |
| **Persistence** | Git-versioned markdown files | In-memory (session) | SQLite3 + RAG | Checkpoints (configurable backend) | OpenSearch + S3 | Custom per-agent |
| **Scalability model** | Add layers/entities (tree growth) | Add agents to group | Add agents/tasks to crew | Add nodes/edges to graph | Fixed architecture | Fixed 4-agent |
| **Human-in-the-loop** | User approval protocols in rules | Optional per-agent | Optional per-task | Interrupt nodes + breakpoints | Approval gates for critical actions | No |
| **Recovery/Resume** | Episodic memory + stage reports + git history | None (session-bound) | None (session-bound) | Checkpoint-based resume | Event log replay | None |

---

## 4. Analysis

### Where User's System Excels

**Separation of concerns through isolation**: The manager never carries operational knowledge, which prevents context bloat at scale. In AutoGen's GroupChat, every agent sees every message -- at 12 rounds with 5 agents, the context grows linearly. The user's system keeps each agent's context bounded by its tier.

**Explicit lifecycle stages**: The 11-stage lifecycle (request_gathering through archives) provides a repeatable process that other frameworks lack. AutoGen and CrewAI define WHAT agents do but not the development lifecycle around them. The user's system codifies the workflow itself.

**Persistence and auditability**: Every decision, output, and handoff is a git-versioned file. No other framework provides this level of auditability out of the box. OASIS comes closest with OpenSearch event logs, but lacks the structural organization.

**Self-describing agents**: GAB JSON-LD agent definitions with modes, actors, personas, and explicit constraints are richer than any other framework's agent identity system. AutoGen agents are a role string. CrewAI adds goal and backstory. The user's system defines behavioral modes with entry/exit criteria and constraint sets.

**Portability**: The entire system is plain text (markdown + JSON-LD + directory structure). It works with any AI tool, any editor, any platform. Every other framework is code-bound to a specific runtime (Python, LangChain, Bedrock).

**Recursive delegation**: The system supports arbitrary nesting depth (layer 0 > feature > sub-feature > sub-sub-feature, each with stages). Other frameworks are typically flat (one level of agents) or limited to two levels (manager + workers).

### Where User's System Falls Short

**No runtime orchestration**: The user's system defines structure and process but relies on the AI tool (Claude, Cursor) to actually execute delegation. AutoGen, CrewAI, and LangGraph have runtime engines that automatically route messages, manage turns, and handle failures. The user's system is a blueprint that requires a capable executor.

**No shared state or real-time coordination**: Agents communicate through files (stage reports, handoff documents). There is no real-time message passing, no shared memory pool, no event-driven coordination. This makes the system inherently asynchronous, which works for staged workflows but not for real-time multi-agent collaboration.

**Context transfer overhead**: Handoff documents and three-tier knowledge are powerful but require agents to read files, parse markdown, and reconstruct context. In LangGraph, state is just a Python dictionary passed to the next node. In CrewAI, task results are passed directly. The user's system trades speed for portability and persistence.

**No built-in semantic retrieval**: The user's system navigates context through hierarchical file paths and explicit pointers. There is no vector similarity search, no embedding-based retrieval, no fuzzy matching. Finding relevant context requires knowing where it is. AutoGen's teachable agents and CrewAI's entity memory both support semantic search.

**No automatic conflict resolution**: When multiple agents might modify shared state, the user's system relies on the scope boundary rule and human oversight. SHIMI uses CRDTs for automatic conflict resolution. LangGraph uses graph state with defined reducers. The user's system has no equivalent.

**No quantitative benchmarks**: The user's system has 76 PASS tests for context chain validation, but no performance metrics (latency, throughput, recall). Other frameworks publish benchmarks -- pgvector at 471 QPS, Mem0 at 91% latency reduction.

### Potential Hybrid Improvements

**Add semantic retrieval layer**: Augment the file-based navigation with vector embeddings of `0AGNOSTIC.md` and stage report content. An agent could semantically search across all entities and stages rather than traversing the tree manually. This preserves the hierarchical structure while adding fuzzy retrieval as an overlay.

**Runtime orchestration adapter**: Create a LangGraph or CrewAI adapter that maps the layer-stage hierarchy into a state machine or crew definition. The 11-stage lifecycle would map to graph nodes with conditional edges. The `0AGNOSTIC.md` files would define node behavior. This gives the system a runtime engine while keeping the source-of-truth in portable markdown.

**Shared working memory buffer**: Add a lightweight shared memory mechanism (even a single JSON file per entity) where active stage agents can publish status and intermediate results. Other agents could subscribe to updates. This bridges the gap between fully async file-based communication and real-time state sharing.

**Stage report templating with structured data**: Enhance stage reports to include machine-readable sections (JSON or YAML frontmatter) alongside human-readable markdown. This would enable automated status aggregation, progress dashboards, and programmatic health checks without breaking the markdown-first philosophy.

**Checkpoint integration**: Map git commits to LangGraph-style checkpoints. Each commit represents a recoverable state. A checkpoint index could map commit hashes to stage transitions, enabling "resume from stage 04" by checking out the appropriate commit state.

---

## Sources

- AutoGen GroupChat: https://github.com/microsoft/autogen
- CrewAI Memory: https://docs.crewai.com/
- LangGraph: https://github.com/langchain-ai/langgraph
- OASIS: https://github.com/aws-samples/sample-operational-ai-agent
- ATLAS: https://github.com/NirDiamant/GenAI_Agents
- User's agent delegation system: `layer_1_sub_feature_agent_delegation_system/0AGNOSTIC.md`
- User's GAB agent definition: `.0agnostic/06_context_avenue_web/01_aalang/agent_delegation_system.gab.jsonld`
- Multi-agent memory research: `08_multi_agent_memory.md`
