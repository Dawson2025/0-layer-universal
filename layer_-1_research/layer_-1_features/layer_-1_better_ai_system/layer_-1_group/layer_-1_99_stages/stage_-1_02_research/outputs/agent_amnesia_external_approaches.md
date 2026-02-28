# External Approaches to Solving Agent Amnesia in AI Systems

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Date**: 2026-01-30
**Purpose**: Comprehensive research on multi-agent AI frameworks and their approaches to agent identity persistence, memory systems, and context management.

---

## Executive Summary

This document synthesizes research from major AI frameworks (LangGraph/LangChain, AutoGen, CrewAI, OpenAI, Anthropic) and academic literature on solving the "agent amnesia" problem - the tendency of LLM-based agents to lose context, forget their identity, and fail to maintain coherent state across sessions.

**Key Finding**: The field has converged on a **three-layer memory architecture** (immediate context, episodic memory, semantic memory) as the foundation for amnesia-resistant agent systems. Production-grade solutions require **explicit architectural structure** rather than implicit optimization - agents need deliberate context engineering, not just larger context windows.

---

## Table of Contents

1. [The Agent Amnesia Problem](#1-the-agent-amnesia-problem)
2. [Framework Approaches](#2-framework-approaches)
   - [LangGraph/LangChain](#21-langgraphlangchain)
   - [Microsoft AutoGen](#22-microsoft-autogen)
   - [CrewAI](#23-crewai)
   - [OpenAI Agents SDK](#24-openai-agents-sdk)
   - [Anthropic Patterns](#25-anthropic-patterns)
3. [Memory Architecture Patterns](#3-memory-architecture-patterns)
4. [System Prompt Hierarchies](#4-system-prompt-hierarchies)
5. [Self-Referential Agent Patterns](#5-self-referential-agent-patterns)
6. [Academic Research](#6-academic-research)
7. [Implementation Patterns](#7-implementation-patterns)
8. [Recommendations for Our System](#8-recommendations-for-our-system)

---

## 1. The Agent Amnesia Problem

### 1.1 Definition

Agent amnesia is the architectural problem where AI agents:
- Lose context between sessions
- Forget file locations, function names, and prior work
- Fail to maintain coherent understanding across extended interactions
- Cannot recall their own role, capabilities, and constraints

Research analyzing 1,600+ agent execution traces found that **context-related failures accounted for 41.8% of all agent failures** - the largest category of system design issues.

### 1.2 Manifestations

| Scenario | Symptom |
|----------|---------|
| Conversational | Treats each message as isolated despite history |
| Coding | Loses track of file structure, rewrites existing code |
| Multi-agent | Coordination fails, shared state ignored |
| Long-running | Cannot maintain strategy across days/weeks |

### 1.3 Root Cause

The problem is NOT storage capacity - it's **coherence maintenance**. Agents forget not because there's insufficient memory but because they lack structural means to maintain coherent understanding across time.

---

## 2. Framework Approaches

### 2.1 LangGraph/LangChain

**Philosophy**: Explicit graph-based state management with layered memory architecture.

#### Key Patterns

**1. Dual Memory System**
- **Short-term memory**: Thread-scoped checkpoints saved at each execution step
- **Long-term memory**: Namespace-scoped memory stores for cross-session persistence

```python
# LangGraph Memory Store Pattern
def pre_model_hook(state, config: RunnableConfig, *, store: BaseStore):
    """Retrieve relevant memories before model invocation"""
    user_id = config["configurable"]["user_id"]
    namespace = (user_id, "memories")

    # Search for memories relevant to current message
    messages = state.get("messages", [])
    if messages and isinstance(messages[-1], HumanMessage):
        query = messages[-1].content
        relevant_memories = store.search(namespace, query=query, limit=5)

        memory_text = "\n".join([
            f"- {m.value['memory']}" for m in relevant_memories
        ])

        if memory_text:
            state["relevant_memories"] = memory_text

    return state
```

**2. Checkpointing Architecture**
- Snapshots capture complete state at each "super-step"
- Organized into threads with unique `thread_id`
- Enables human-in-the-loop, failure recovery, time-travel debugging
- DynamoDB/S3 integration for production (auto-offloads >350KB payloads)

**3. Supervisor Pattern**
- Hierarchical agents where specialists report to supervisors
- Each supervisor sees specialists as tools
- Message history controlled via `output_mode` parameter

#### Strengths
- Explicit state management makes debugging straightforward
- Built-in persistence rather than optional extension
- Graph visualization of context flow

### 2.2 Microsoft AutoGen

**Philosophy**: Event-driven, actor-model concurrency with distributed state.

#### Key Patterns

**1. Conversable Agents**
- Agents communicate through message passing
- Each maintains own message history
- Auto-reply functions determine responses

```python
# AutoGen Event-Driven Pattern
class Orchestrator:
    async def run_agent_workflow(self, input_data):
        state = WorkflowState(status="START", data=input_data)

        emit(StateEvent(type="MODEL_INVOKED", state=state))
        model_response = await self.model.call(input_data)

        if model_response.tool_calls:
            for tool_call in model_response.tool_calls:
                emit(StateEvent(type="TOOL_INVOKED", tool=tool_call.name))
                result = await self.execute_tool(tool_call)

        emit(StateEvent(type="FINISHED", result=result))
        return result
```

**2. Event-Driven State**
- Every state transition is an event (MODEL_INVOKED, TOOL_INVOKED, etc.)
- Events can be persisted, logged, analyzed
- Resume by replaying events or checkpointing

**3. Dynamic Conversation Patterns**
- Topology evolves based on message content
- Agents can spawn helper agents mid-conversation
- Group chat patterns for multi-agent collaboration

#### Memory Extensions
- ListMemory: Simple chronological storage
- ChromaDBVectorMemory: Semantic search via embeddings
- Memory as optional extension (not built-in)

#### Strengths
- Distributed systems thinking
- Asynchronous by design
- Flexible memory backends

### 2.3 CrewAI

**Philosophy**: Role-based agents with structured, crew-level memory.

#### Key Patterns

**1. Agent Definition**
```python
analyst = Agent(
    role="Data Analyst",
    goal="Analyze and remember complex data patterns",
    backstory="Expert data analyst with 10 years experience",
    memory=True,
    verbose=True
)
```

Each agent has:
- **Role**: Primary function
- **Goal**: What agent tries to accomplish
- **Backstory**: Expertise and experience context

**2. Three-Part Memory System**
| Memory Type | Storage | Purpose |
|-------------|---------|---------|
| Short-term | RAG | Immediate context, recent interactions |
| Long-term | SQLite3 | Persistent across sessions |
| Entity | RAG | Track specific people/orgs/concepts |

**3. Crew-Level Memory Sharing**
- Memory shared across agents within a crew
- Separation between different crews
- Automatic context summarization when limits approached

#### Strengths
- Predictable agent behavior through explicit role definition
- Built-in memory management at crew level
- Automatic context window management

### 2.4 OpenAI Agents SDK

**Philosophy**: Session-based simplicity with automatic history management.

#### Key Patterns

**1. Session Abstraction**
```python
session = SQLiteSession("conversation_123")

# First turn
result = await Runner.run(agent, "What city is the Golden Gate Bridge in?", session=session)

# Second turn - automatically has full history
result = await Runner.run(agent, "What state is it in?", session=session)
```

**2. Compaction Sessions**
- `OpenAIResponsesCompactionSession` auto-summarizes older turns
- Recent turns in full detail, older turns compressed
- Preserves context while managing tokens

**3. Handoff Pattern**
```python
agent_a = Agent(
    name="GeneralAgent",
    instructions="If the user asks about billing, hand off to BillingAgent",
    handoffs=[billing_agent]
)
```
- Explicit delegation between specialists
- Full context transfer on handoff
- Receiving agent gets complete history

#### Strengths
- Simple developer experience
- Automatic history management
- Clean handoff semantics

### 2.5 Anthropic Patterns

**Philosophy**: Advanced tool use, programmatic orchestration, and context engineering.

#### Key Patterns

**1. Tool Search Pattern**
Problem: 50+ tools consume ~72,000 tokens before work begins

Solution: Load tools on-demand
```python
tools = [
    {"type": "tool_search_tool_regex", "name": "tool_search_tool_regex"},  # Always available
    {"name": "github.createPullRequest", "defer_loading": False},  # Frequently used
    {"name": "slack.sendMessage", "defer_loading": True}  # Load on demand
]
```
Reduces context from ~77,000 to <10,000 tokens.

**2. Programmatic Tool Calling**
Instead of N+1 model invocations for N steps:
```python
code = """
team = get_team_members('engineering')
expenses_data = []
for member in team:
    expenses = get_expenses(member['id'])
    expenses_data.extend(expenses)

total = sum(e['amount'] for e in expenses_data)
return {'total': total, 'breakdown': analyze_expenses(expenses_data)}
"""
```
Code orchestrates tools, only final results return to model context.

**3. Tool Use Examples**
Not just JSON schemas but concrete usage demonstrations:
```
Critical bugs: full contact info + escalation with tight SLAs
Feature requests: reporter but no contact/escalation
Internal tasks: title only
```
Improved accuracy from 72% to 90% on complex parameter handling.

**4. Claude Code Harness Architecture**
Production patterns from Claude Code:
- Master agent loop (single-threaded, deterministic)
- TODO lists persisted and injected into system prompt
- h2A async queue for real-time steering
- Mandatory verification before task completion

#### Model Context Protocol (MCP)

Open standard for LLM-external system communication:
- **Resources**: File-like data (API responses, documents)
- **Tools**: Executable functions (user approval required)
- **Prompts**: Pre-written templates

Enables dynamic context injection from external systems.

---

## 3. Memory Architecture Patterns

### 3.1 The Three-Layer Convergence

All major frameworks converge on:

| Layer | Scope | Purpose | Implementation |
|-------|-------|---------|----------------|
| **Immediate** | Current session | Conversation history | Messages list |
| **Episodic** | Cross-session | Specific completed tasks | Vector DB + metadata |
| **Semantic** | Global | General facts, patterns | Knowledge graphs |

### 3.2 Academic Memory Dimensions

Research categorizes memory across:

**Forms**:
- Token-level: Explicit text in context
- Parametric: Encoded in model weights (fine-tuning)
- Latent: Vector embeddings

**Functions**:
- Factual: World knowledge, grounding
- Experiential: Past actions, learned patterns
- Working: Current task execution

**Dynamics**:
- Formation: What merits storage
- Evolution: Updating based on new info
- Retrieval: Finding relevant memories

### 3.3 Key Research Papers (2024-2025)

| Paper | Key Innovation |
|-------|----------------|
| **MIRIX** (2025) | Multi-level core/episodic/semantic/procedural hierarchy; 26% improvement, 91% lower latency |
| **A-Mem** (2025) | Zettelkasten-inspired dynamic linking; 2x better multi-hop reasoning |
| **Memory OS** (2025) | STM/MTM/LPM hierarchy for sequential decision-making |
| **Git Context Controller** (2025) | Version-controlled memory with commit/branch/merge |
| **MemGPT** (2023) | OS-inspired memory paging; baseline for newer work |

### 3.4 Strategic Forgetting

Counter-intuitive finding: **Effective memory requires sophisticated forgetting**.

MemGPT research shows:
- Cognitive triage (LLM evaluates information value)
- Important facts prioritized, transient content summarized/deleted
- Reduces context pollution that degrades reasoning

---

## 4. System Prompt Hierarchies

### 4.1 Layered Context Stack

Modern agents use modular context layers:

```
1. System Instructions (role, capabilities, constraints) - Static
2. Long-term Memory (user preferences, learned patterns) - Retrieved
3. Retrieved Documents (search results, project docs) - Dynamic
4. Tool Definitions (available functions) - Filtered
5. Conversation History (recent turns) - Compressed
6. Current Task (user request) - Last position (recency bias)
```

### 4.2 Context Engineering Strategies

From Anthropic's research:

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Write** | Store info in working memory/state | Scratchpads, intermediate results |
| **Select** | Pull relevant info from larger stores | RAG, semantic search |
| **Compress** | Summarize while preserving essentials | Long conversations |
| **Isolate** | Partition across agents/components | Specialized workers |

### 4.3 Sliding Window Compression

```
Turns 1-5: Full verbatim detail
Turns 6-20: Lightly summarized
Turns 21-50: Heavily summarized
```

Maintains recent context in detail, older context in compressed form.

---

## 5. Self-Referential Agent Patterns

### 5.1 The Self-Blindness Problem

Traditional agents lack awareness of:
- Their own tool availability
- Knowledge boundaries
- Context window consumption
- Their own constraints

### 5.2 Gödel Agent (Microsoft Research)

Self-modifying framework where agents:
1. Execute current policy
2. Evaluate own performance
3. Generate improvements to own prompting strategy
4. Modify self

```python
class SelfImprovingAgent:
    async def execute_with_improvement(self, task):
        result = await self.execute(task)
        performance = self.evaluate_performance(result, task)

        if performance < threshold:
            improved_policy = await self.llm.generate_improvement(
                task=task,
                current_policy=self.policy,
                performance_feedback=performance
            )
            self.policy = improved_policy

        return result
```

### 5.3 Claude's Context Awareness

Claude 4.x models incorporate:
- Tracking of remaining context window
- Adaptive behavior as limits approach
- Can proactively summarize before running out

Prompt pattern:
```
If you are using Claude in an agent harness that compacts context
or allows saving context to external files, we suggest adding this
information to your prompt so Claude can behave accordingly.
```

### 5.4 Reflexion Pattern

```python
class ReflectiveAgent:
    async def execute_with_reflection(self, task):
        initial_response = await self.generate_response(task)

        reflection = await self.llm.generate(f"""
        Review this response: {initial_response}

        1. Is it accurate and truthful?
        2. Does it fully address the task?
        3. What are you uncertain about?
        4. How could this be improved?
        """)

        if "improvement" in reflection.lower():
            return await self.generate_response(
                task,
                context=f"Previous: {initial_response}\nFeedback: {reflection}"
            )

        return initial_response
```

---

## 6. Academic Research

### 6.1 Memory Agent Competencies (MemoryAgentBench)

Four essential competencies for memory agents:
1. **Accurate retrieval**: Find specific info from long conversations
2. **Test-time learning**: Improve through interaction
3. **Long-range understanding**: Span many turns
4. **Conflict resolution**: Handle contradictory memories

### 6.2 Key Findings

1. **Context-related failures are #1** (41.8% of all failures)
2. **Larger context windows are insufficient** - processing degradation occurs
3. **Hierarchical memory outperforms flat** (10-26% improvement)
4. **Strategic forgetting improves performance**
5. **Multiple memory types essential** (semantic + episodic + procedural)

### 6.3 Unified Database Approaches

Modern pattern: PostgreSQL with specialized extensions
- Hypertables for time-series conversation history
- pgvector for semantic similarity search
- Standard tables for structured state

Benefits:
- Single transaction for consistent snapshots
- Hybrid RAG (vector + keyword + temporal)
- One backup strategy protects all memory

---

## 7. Implementation Patterns

### 7.1 Single-Agent Execution Loop

Universal pattern across all frameworks:
```python
async def run_agent(task: str):
    messages = [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": task}
    ]

    while True:
        response = await client.chat.completions.create(
            model=model_id, messages=messages, tools=tool_schemas
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if not assistant_message.tool_calls:
            return assistant_message.content  # Final response

        for tool_call in assistant_message.tool_calls:
            result = await execute_tool(tool_call)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
```

### 7.2 Multi-Agent Patterns

| Pattern | Description | Best For |
|---------|-------------|----------|
| Sequential Pipeline | Output chains to next agent | Clear stage dependencies |
| Supervisor/Dispatcher | Routes to specialists | Request classification |
| Hierarchical Decomposition | Recursive problem breakdown | Complex, divide-and-conquer |
| Agents-as-Tools | Specialists as callable functions | Clear hierarchy |
| Parallel Fan-Out | Simultaneous independent work | Code review, analysis |

### 7.3 Cross-Session Memory Integration

```python
async def begin_new_session(project_id: str, new_task: str):
    # Retrieve relevant episodic memories
    relevant_episodes = await memory_store.search(
        namespace=(project_id, "episodes"),
        query=new_task,
        limit=5
    )

    # Extract relationships between episodes
    context = await extract_episode_relationships(relevant_episodes)

    # Inject into system prompt
    system_with_context = f"""
    {base_instructions}

    Prior work on this project:
    {context}
    """

    return await agent.run(new_task, system_prompt=system_with_context)
```

---

## 8. Recommendations for Our System

Based on this research, recommendations for the layer-stage framework:

### 8.1 Adopt Three-Layer Memory

```
Layer 1: Immediate Context
- Current session CLAUDE.md chain
- Active stage state
- Recent tool outputs

Layer 2: Episodic Memory
- Session handoff documents
- Completed work summaries
- Decision rationale

Layer 3: Semantic Memory
- Universal rules (layer_0)
- Project knowledge bases
- Learned patterns
```

### 8.2 Implement Explicit Context Traversal

Already in CLAUDE.md rules - formalize as mandatory pre-task routine:
1. Read CLAUDE.md chain from root to working directory
2. Identify current layer and stage
3. Load relevant sub_layer content
4. Read status.json for current state

### 8.3 Add Self-Referential Prompting

Include in system prompts:
```markdown
## Self-Awareness Context

You are operating in the layer-stage framework:
- Current Layer: {layer}
- Current Stage: {stage}
- Available Tools: {tool_list}
- Context Window Status: {remaining_tokens}
- Session History: {compressed_history}

If approaching context limits, use handoff_documents to persist
critical state before compaction.
```

### 8.4 Enhance Handoff Documents

Current handoff_documents can serve as episodic memory:
- Add structured metadata (timestamp, layer, stage, outcome)
- Enable semantic search across handoffs
- Link related handoffs for context continuity

### 8.5 Consider Graph Memory

For complex projects, track relationships:
```
Feature A --depends-on--> Component B
Decision X --supersedes--> Decision Y
Agent Session 1 --handed-off-to--> Agent Session 2
```

### 8.6 Implement Verification Gates

From Claude Code patterns:
- Agents must verify task completion before marking done
- Automatic tests where possible
- Human review checkpoints for critical paths

---

## Sources

### Official Documentation
- [LangGraph Memory Documentation](https://docs.langchain.com/oss/python/langgraph/memory)
- [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [AutoGen Documentation](https://microsoft.github.io/autogen/stable/)
- [CrewAI Agents](https://docs.crewai.com/en/concepts/agents)
- [CrewAI Memory](https://docs.crewai.com/en/concepts/memory)
- [OpenAI Agents SDK Sessions](https://openai.github.io/openai-agents-python/sessions/)
- [OpenAI Agents SDK Handoffs](https://openai.github.io/openai-agents-python/handoffs/)
- [Anthropic Advanced Tool Use](https://www.anthropic.com/engineering/advanced-tool-use)
- [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Model Context Protocol](https://modelcontextprotocol.io)

### Academic Papers
- [A Survey on the Memory Mechanism of LLM-based Agents](https://arxiv.org/abs/2512.13564) (2024-2025)
- [A-Mem: Agentic Memory for LLM Agents](https://arxiv.org/html/2502.12110v1) (2025)
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (2023)
- [MIRIX: Multi-Agent Memory System](https://www.emergentmind.com/topics/persistent-memory-for-llm-agents) (2025)
- [Gödel Agent: Self-Modifying Framework](https://arxiv.org/html/2410.04444v1) (2024)
- [MemoryAgentBench](https://arxiv.org/html/2507.05257v1) (2025)

### Industry Articles
- [AWS: Build Durable AI Agents with LangGraph and DynamoDB](https://aws.amazon.com/blogs/database/build-durable-ai-agents-with-langgraph-and-amazon-dynamodb/)
- [Claude Code Behind the Scenes](https://blog.promptlayer.com/claude-code-behind-the-scenes-of-the-master-agent-loop/)
- [The Discipline Layer: Harnesses as Missing Piece](https://www.getmaxim.ai/blog/the-discipline-layer-harnesses-as-the-missing-piece-in-autonomous-coding/)
- [Building AI Agents with Persistent Memory](https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach)
- [Vector Databases for Agentic AI](https://www.getmonetizely.com/articles/how-do-vector-databases-power-agentic-ais-memory-and-knowledge-systems)
