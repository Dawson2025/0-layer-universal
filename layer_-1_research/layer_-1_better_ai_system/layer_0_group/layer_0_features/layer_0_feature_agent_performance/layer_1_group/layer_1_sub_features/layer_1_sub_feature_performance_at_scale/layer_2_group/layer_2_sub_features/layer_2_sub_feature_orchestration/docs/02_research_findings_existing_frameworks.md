# Research Findings: Existing Multi-Agent Frameworks

**Layer**: -1 (Research)
**Feature**: layer_0_feature_multi_agent_orchestration
**Stage**: 02_research
**Date**: 2026-02-06
**Status**: Complete

---

## Key Discoveries

### 1. ReDel Toolkit - Recursive Multi-Agent Systems

**Source**: [arxiv.org/html/2408.02248v1](https://arxiv.org/html/2408.02248v1)

ReDel is a fully-featured open-source toolkit that enables recursive multi-agent systems where a root agent can dynamically spawn child agents.

#### Key Features:
- **DelegateOne**: Blocks parent until all children return (parallel execution)
- **DelegateWait**: Parent continues while children work asynchronously
- **Event-driven logging**: Captures every interaction for debugging
- **Interactive replay**: Re-execute portions of workflows

#### Performance:
- Outperforms single-agent GPT-4o on FanOutQA (information aggregation)
- Improves over state-of-the-art on TravelPlanner
- Advantage grows as task complexity increases

**Relevance to Our Design**: DelegateOne and DelegateWait patterns map directly to our needs. We can implement both synchronous and asynchronous spawning.

---

### 2. Daytona - Unlimited Recursion Depth

**Source**: [daytona.io/docs/en/recursive-language-models](https://www.daytona.io/docs/en/recursive-language-models)

Daytona extends recursive agents to support **unlimited recursion depth** with isolated sandboxes.

#### Architecture:
- Each agent runs in isolated sandbox with fresh repository clone
- Agents can call `rlm_query()` to spawn single child
- Agents can call `rlm_query_batched()` for parallel spawning
- Results propagate back up through hierarchy

#### Real-World Example (scikit-learn):
- Root agent spawned 25 depth-1 agents in parallel
- Some depth-1 agents spawned depth-2 agents for large modules
- Total: 40 agents, 3 hierarchy levels
- Completed in ~5 minutes

#### Safeguards:
| Safeguard | Purpose |
|-----------|---------|
| Maximum recursion depth | Prevent infinite depth |
| Total sandbox count | Limit resource usage |
| Maximum iterations per agent | Prevent infinite loops |
| Global timeout | Time-bound execution |
| Result truncation limits | Manage output size |

**Relevance to Our Design**: This proves unlimited recursion is viable with proper safeguards. We should implement similar controls.

---

### 3. CLI-Based AI Tools Landscape

| Tool | Spawnable? | Notes |
|------|------------|-------|
| **Claude Code** | Yes | `claude` command, `--print` flag, ranks #3 on Terminal Bench |
| **Gemini CLI** | Yes | 1000 free requests/day, 1M token context |
| **Codex CLI** | Yes | Lightweight, ranks #19 on Terminal Bench |
| **Aider** | Yes | Git-native, supports local models |

#### Key Insight:
> "Unlike other multi-agent frameworks that require custom runtimes, CLI AI tools are already designed to be invoked from terminals. This means any AI agent with bash access can spawn other AI agents natively."

**Relevance to Our Design**: We can spawn any of these tools via bash. No custom runtime needed.

---

### 4. Communication Protocols

#### Model Context Protocol (MCP)

**Source**: Anthropic, late 2024

- Standardizes how agents discover and call external tools
- OpenAPI/JSON schemas for tool definitions
- November 2025 update added **Tasks primitive** for async operations
- OAuth 2.1 for authorization

**Key Feature**: Tasks primitive enables long-running async operations - critical for multi-agent workflows.

#### Agent Communication Protocol (ACP)

**Source**: IBM Research

- Focus on semantic richness and intent modeling
- Structured messages encapsulate intention, task parameters, context
- Requires shared ontologies (best for same-team development)

#### Agent2Agent Protocol (A2A)

**Source**: Google (with Microsoft)

- Targets cross-platform interoperability
- Agents advertise capabilities via "agent cards"
- Cryptographic signing for trust

**Relevance to Our Design**:
- Use MCP patterns for tool integration
- Use file-based hand_off_documents for simplicity (no shared ontology required)
- A2A patterns for future cross-organization collaboration

---

### 5. Hierarchical Coordination Patterns

#### Three-Tier Hierarchy (Manager-Specialist-Worker)

```
┌─────────────────────────────────────────┐
│  MANAGER (Strategic Orchestrator)       │
│  • Decompose high-level objectives      │
│  • Route to specialists                 │
│  • Monitor progress, handle exceptions  │
│  • Synthesize results                   │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┴────────────┐
    ▼                         ▼
┌───────────────┐     ┌───────────────┐
│  SPECIALIST   │     │  SPECIALIST   │
│  (Domain      │     │  (Domain      │
│   Expert)     │     │   Expert)     │
└───────┬───────┘     └───────┬───────┘
        │                     │
    ┌───┴───┐             ┌───┴───┐
    ▼       ▼             ▼       ▼
┌───────┐ ┌───────┐   ┌───────┐ ┌───────┐
│WORKER │ │WORKER │   │WORKER │ │WORKER │
│       │ │       │   │       │ │       │
└───────┘ └───────┘   └───────┘ └───────┘
```

**Benefits**:
- As task complexity increases, generalist performance degrades
- Hierarchical delegation distributes work across specialized agents
- Prevents context window overflow

#### Two-Tier (Supervisor-Worker)

- Simpler communication paths
- Easy horizontal scaling
- Lower latency
- Better for parallelizable tasks

**Relevance to Our Design**: Start with two-tier (supervisor-worker), evolve to three-tier as needed.

---

### 6. Context Management Strategies

#### The Problem:
- Multi-agent systems consume ~15x more tokens than simple chat
- Every token for history depletes budget for new information
- Context windows are hard limits

#### Solutions:

| Strategy | Description |
|----------|-------------|
| **Selective Context Injection** | Include only relevant info per step |
| **Progressive Disclosure** | Reveal details only when needed |
| **Tiered Action Spaces** | Load only core tools initially |
| **Memory Offloading** | Store history in external DB, retrieve via semantic search |
| **Context Compression** | Embeddings + vector DB for dense storage |

**Relevance to Our Design**:
- Pass minimal task-specific context to children
- Use hand_off_documents for state rather than passing full context
- Children can request more context if needed

---

### 7. Safeguards and Failure Prevention

#### Known Failure Modes:
- **Premature termination**: Agents stop before completing multi-step reasoning
- **Undercommitment anomalies**: Agents continuously delegate, creating infinite recursion
- **Neural howlround**: Agents trapped in infinite self-optimization loops

#### Defense-in-Depth Architecture:

| Layer | Controls |
|-------|----------|
| **Design** | Threat modeling, least-privilege, safe tool integration |
| **Runtime** | Recursion depth limits, timeouts, token budgets |
| **Monitoring** | Real-time behavioral monitoring, anomaly detection |
| **Recovery** | Circuit breakers, automatic rollbacks, safe modes |

#### Key Safeguards for Our Design:

1. **Hard Limits**:
   - Max recursion depth (default: 5)
   - Max concurrent agents (default: 3)
   - Global timeout (default: 10 minutes)
   - Token budget per agent

2. **Semantic Safeguards**:
   - Detect repeated delegation with identical instructions
   - Detect children returning results parent ignores
   - Detect circular dependencies

3. **Circuit Breakers**:
   - Stop routing to failing agents
   - Retry with exponential backoff
   - Escalate to human if repeated failures

---

### 8. Industry Predictions

> "Gartner predicts that 40% of enterprise applications will integrate task-specific AI agents by end of 2026, up from less than 5% in 2025."

> "Multi-agent systems consume approximately 15 times more tokens than simple chat interactions."

> "Only 6% of organizations have advanced AI security strategies despite 40% planning agent deployments."

---

## Conclusions for Our Design

### What to Adopt:

1. **ReDel patterns**: DelegateOne (sync) and DelegateWait (async) spawning
2. **Daytona safeguards**: Depth limits, timeouts, iteration limits
3. **File-based communication**: Already have hand_off_documents
4. **Supervisor-Worker hierarchy**: Simple, effective starting point
5. **Minimal context passing**: Task + essentials only

### What to Avoid:

1. Complex ontologies (ACP) - overkill for our use case
2. Full context passing - too expensive
3. Flat peer-to-peer - harder to coordinate
4. Single-agent-does-all - doesn't scale

### Novel Contribution:

Our approach is unique in combining:
- **AALang/GAB patterns** (4-mode-13-actor) for agent definition
- **CLI AI tools** (Claude Code, Codex, Gemini) for execution
- **Layer-stage hand_off_documents** for communication
- **Recursive spawning** with proper safeguards

No existing framework combines these elements.

---

## Sources

- [ReDel Toolkit](https://arxiv.org/html/2408.02248v1)
- [Daytona Recursive LMs](https://www.daytona.io/docs/en/recursive-language-models)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Hierarchical Agent Systems](https://www.ruh.ai/blogs/hierarchical-agent-systems)
- [Multi-Agent Context Engineering](https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering)
- [Anthropic Multi-Agent Research](https://www.anthropic.com/engineering/multi-agent-research-system)
- [AI CLI Tools Comparison](https://tessl.io/blog/choosing-the-right-ai-cli/)
- [Agent Security Framework](https://zbrain.ai/architecting-resilient-ai-agents/)

---

*Research Findings - Layer -1 (Research)*
*Feature: Multi-Agent Orchestration*
*Created: 2026-02-06*
