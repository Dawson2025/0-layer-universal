# Research: Recursive Multi-Agent Systems with CLI AI Tools

**Layer**: -1 (Research)
**Feature**: layer_0_feature_multi_agent_orchestration
**Stage**: 02_research
**Date**: 2026-02-06
**Status**: In Progress

---

## Executive Summary

This research explores the feasibility and design of a recursive multi-agent system using AALang/GAB patterns where CLI AI tools (Claude Code, Codex, Gemini CLI, etc.) can spawn and coordinate with other AI agents in their own terminal instances, creating unlimited recursive subagent hierarchies.

---

## 1. Problem Statement

### Current Limitation
Single AI agent sessions are limited by:
- Context window size
- Single-threaded execution
- One tool at a time
- No persistent coordination with other agents

### Opportunity
CLI AI tools (Claude Code, Codex, Gemini CLI) can:
- Execute bash commands
- Start new terminal processes
- Write to and read from files
- Potentially spawn other AI CLI tools

### Research Question
**Can we use AALang/GAB patterns to create a framework for recursive multi-agent orchestration where AI agents spawn, coordinate, and aggregate results from unlimited subagents?**

---

## 2. Landscape Analysis

### 2.1 Existing Multi-Agent Frameworks

| Framework | Approach | Limitations |
|-----------|----------|-------------|
| **AutoGen (Microsoft)** | Python-based multi-agent conversations | Requires custom runtime, not CLI-native |
| **CrewAI** | Role-based agent teams | Fixed team structure, not recursive |
| **LangGraph** | Graph-based agent workflows | Complex setup, state management overhead |
| **MetaGPT** | Software company simulation | Domain-specific, not general purpose |
| **Swarm (OpenAI)** | Lightweight agent handoffs | Experimental, limited coordination |

### 2.2 CLI AI Tools Available

| Tool | Spawnable via Bash? | Output Capture | Notes |
|------|---------------------|----------------|-------|
| **Claude Code** | Yes (`claude` command) | Yes | Can use `--print` flag |
| **Codex CLI** | Yes (`codex` command) | Yes | Direct output |
| **Gemini CLI** | Yes (`gemini` command) | Yes | Direct output |
| **Aider** | Yes (`aider` command) | Yes | Git-focused |
| **Continue** | No (IDE extension) | N/A | Not CLI |
| **Cursor** | No (IDE) | N/A | Not CLI |

### 2.3 Key Insight

**Unlike other multi-agent frameworks that require custom runtimes, CLI AI tools are already designed to be invoked from terminals. This means any AI agent with bash access can spawn other AI agents natively.**

---

## 3. Technical Feasibility

### 3.1 Spawning Mechanism

```bash
# Parent agent spawns child agent
claude code --print "Analyze the authentication module" > /tmp/child_result.md

# Or with task file
echo "Analyze authentication module for security issues" > /tmp/task.md
codex "$(cat /tmp/task.md)" > /tmp/result.md
```

### 3.2 Communication Channels

| Channel | Pros | Cons |
|---------|------|------|
| **Files** | Simple, persistent, cross-process | Polling required, potential race conditions |
| **Named Pipes** | Real-time, streaming | More complex, OS-dependent |
| **Sockets** | Network-capable, bidirectional | Overhead, security considerations |
| **hand_off_documents/** | Already in layer-stage system | File-based, needs polling |

**Recommendation**: Use file-based communication via `hand_off_documents/` pattern, as it's already established in the layer-stage system.

### 3.3 Coordination Patterns

#### Pattern A: Hierarchical (Tree)
```
Parent Agent
├── Child A
│   ├── Grandchild A1
│   └── Grandchild A2
└── Child B
    └── Grandchild B1
```
- Clear ownership
- Results bubble up
- Risk: Deep recursion

#### Pattern B: Peer Network
```
Agent A ←→ Agent B
   ↕         ↕
Agent C ←→ Agent D
```
- Flexible collaboration
- Complex coordination
- Risk: Deadlocks

#### Pattern C: Hub and Spoke
```
        Agent B
           ↑
Agent A ← Hub → Agent C
           ↓
        Agent D
```
- Centralized coordination
- Simple communication
- Risk: Hub bottleneck

**Recommendation**: Start with **Hierarchical (Pattern A)** as it's simplest and maps well to task decomposition.

---

## 4. AALang/GAB Integration

### 4.1 New Mode: SpawningMode

Following the GAB 4-mode pattern, we can add a SpawningMode to any agent that needs to orchestrate subagents:

```json
{
  "@id": "ctx:SpawningMode",
  "@type": "gab:Mode",
  "purpose": "Spawn and coordinate subagents for complex tasks",
  "contains": ["ctx:SpawningPersona1", "ctx:SpawningPersona2"],
  "constraints": [
    "Evaluate if task requires subagents",
    "Decompose task into subtasks",
    "Select appropriate agent type for each subtask",
    "Spawn agents with clear task definitions",
    "Monitor progress via hand_off_documents",
    "Aggregate results when complete"
  ]
}
```

### 4.2 New State Actor: SpawningStateActor

```json
{
  "@id": "ctx:SpawningStateActor",
  "state": {
    "activeSubagents": [],
    "pendingTasks": [],
    "completedTasks": [],
    "maxDepth": 5,
    "currentDepth": 0,
    "coordinationPattern": "hierarchical"
  }
}
```

### 4.3 Integration with Existing Patterns

| Existing Pattern | Integration Point |
|------------------|-------------------|
| **4-mode workflow** | SpawningMode added as optional mode |
| **State actors** | SpawningStateActor tracks subagents |
| **Message interface** | Inter-agent messages via hand_off_documents |
| **Prohibitions** | Max depth, resource limits |
| **Team Lead (user)** | Can override spawn decisions |

---

## 5. Design Considerations

### 5.1 Task Decomposition

When should an agent spawn subagents?

| Criterion | Spawn? | Example |
|-----------|--------|---------|
| Task too large for context | Yes | "Refactor entire codebase" |
| Task requires parallel work | Yes | "Test on Linux, Mac, Windows" |
| Task requires different expertise | Yes | "Write code AND create docs" |
| Task is simple/atomic | No | "Fix this typo" |
| Task requires human decision | No | "Should we use approach A or B?" |

### 5.2 Agent Selection

Which CLI tool to spawn for which task?

| Task Type | Recommended Agent | Reason |
|-----------|-------------------|--------|
| Code analysis/writing | Claude Code | Strong coding capabilities |
| Quick code edits | Codex | Fast, focused |
| Research/web search | Gemini CLI | Web access |
| Git operations | Aider | Git-native |
| General tasks | Any | Flexible |

### 5.3 Safeguards

| Risk | Mitigation |
|------|------------|
| **Infinite recursion** | Max depth limit (default: 5) |
| **Resource exhaustion** | Max concurrent subagents (default: 3) |
| **Runaway costs** | Token/time budget per agent |
| **Lost results** | Persistent file-based handoffs |
| **Deadlocks** | Timeout per agent (default: 10 min) |
| **Context loss** | Each agent gets task + necessary context |

### 5.4 Result Aggregation

How do parent agents combine results from children?

| Strategy | When to Use |
|----------|-------------|
| **Concatenate** | Independent subtasks (code + docs) |
| **Merge** | Overlapping work (multiple analyses) |
| **Select best** | Competitive approaches |
| **Synthesize** | Need unified answer from diverse inputs |
| **Human review** | Conflicting or uncertain results |

---

## 6. Proposed Architecture

### 6.1 High-Level Design

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  RECURSIVE MULTI-AGENT ORCHESTRATION ARCHITECTURE                               │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────────┐
                              │      User Task      │
                              └──────────┬──────────┘
                                         │
                                         ▼
                    ┌────────────────────────────────────────────┐
                    │           ROOT AGENT (Claude Code)         │
                    │  ┌──────────────────────────────────────┐  │
                    │  │    agent_orchestrator_gab.jsonld     │  │
                    │  │  ────────────────────────────────────│  │
                    │  │  • Reads task                        │  │
                    │  │  • Evaluates: Need subagents?        │  │
                    │  │  • Decomposes into subtasks          │  │
                    │  │  • Spawns appropriate agents         │  │
                    │  │  • Aggregates results                │  │
                    │  └──────────────────────────────────────┘  │
                    └─────────────────┬──────────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
              ▼                       ▼                       ▼
    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
    │  CHILD AGENT 1  │     │  CHILD AGENT 2  │     │  CHILD AGENT 3  │
    │  (Claude Code)  │     │    (Codex)      │     │  (Gemini CLI)   │
    │                 │     │                 │     │                 │
    │  Subtask A      │     │  Subtask B      │     │  Subtask C      │
    └────────┬────────┘     └────────┬────────┘     └────────┬────────┘
             │                       │                       │
             │  May spawn            │  Atomic              │  May spawn
             │  grandchildren        │  (no children)       │  grandchildren
             ▼                       ▼                       ▼
    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
    │  Grandchild A1  │     │    (result)     │     │  Grandchild C1  │
    │  Grandchild A2  │     │                 │     │                 │
    └─────────────────┘     └─────────────────┘     └─────────────────┘

COMMUNICATION:
─────────────
    Parent → Child:   hand_off_documents/outgoing/to_below/{child_id}/task.md
    Child → Parent:   hand_off_documents/incoming/from_below/{child_id}/result.md
    Status:           hand_off_documents/status/{child_id}.json
```

### 6.2 File Structure for Communication

```
{agent_workspace}/
├── hand_off_documents/
│   ├── incoming/
│   │   ├── from_above/           ← Task from parent (or user)
│   │   │   └── task.md
│   │   └── from_below/           ← Results from children
│   │       ├── child_001/
│   │       │   └── result.md
│   │       └── child_002/
│   │           └── result.md
│   ├── outgoing/
│   │   ├── to_above/             ← Results to parent
│   │   │   └── result.md
│   │   └── to_below/             ← Tasks to children
│   │       ├── child_001/
│   │       │   └── task.md
│   │       └── child_002/
│   │           └── task.md
│   └── status/                   ← Agent status tracking
│       ├── self.json
│       ├── child_001.json
│       └── child_002.json
└── .claude/
    └── agent_state.json          ← Agent's internal state
```

### 6.3 Task Message Format

```json
{
  "taskId": "task_001",
  "parentAgent": "root_agent",
  "childAgent": "child_001",
  "task": {
    "description": "Analyze authentication module for security vulnerabilities",
    "context": {
      "codebasePath": "/path/to/code",
      "focusFiles": ["auth.py", "login.py"],
      "constraints": ["max_depth: 2", "timeout: 5m"]
    },
    "expectedOutput": {
      "format": "markdown",
      "sections": ["vulnerabilities", "recommendations", "severity"]
    }
  },
  "metadata": {
    "createdAt": "2026-02-06T11:30:00Z",
    "depth": 1,
    "maxDepth": 5
  }
}
```

### 6.4 Result Message Format

```json
{
  "taskId": "task_001",
  "agentId": "child_001",
  "status": "completed",
  "result": {
    "summary": "Found 3 vulnerabilities in authentication module",
    "content": "## Vulnerabilities\n...",
    "confidence": 0.85,
    "subagentsUsed": 0
  },
  "metadata": {
    "completedAt": "2026-02-06T11:35:00Z",
    "tokensUsed": 15000,
    "duration": "5m"
  }
}
```

---

## 7. Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Create `agent_orchestrator_gab.jsonld` with SpawningMode
- [ ] Define hand_off_documents protocol for multi-agent
- [ ] Implement basic spawn/result patterns
- [ ] Test single-level spawning (parent → children)

### Phase 2: Recursion (Week 3-4)
- [ ] Add depth tracking and limits
- [ ] Implement recursive spawning (children → grandchildren)
- [ ] Add timeout and cancellation
- [ ] Test multi-level hierarchies

### Phase 3: Intelligence (Week 5-6)
- [ ] Task decomposition heuristics
- [ ] Agent selection logic
- [ ] Result aggregation strategies
- [ ] Conflict resolution

### Phase 4: Production (Week 7-8)
- [ ] Error handling and recovery
- [ ] Monitoring and logging
- [ ] Performance optimization
- [ ] Documentation and examples

---

## 8. Open Questions

1. **Context Passing**: How much context should children receive? Full parent context or minimal task-specific?

2. **Agent Identity**: Should children know about their ancestry? Or operate independently?

3. **Tool Heterogeneity**: How do we handle different capabilities across Claude/Codex/Gemini?

4. **Cost Management**: How do we prevent runaway API costs with recursive spawning?

5. **State Synchronization**: If multiple children modify shared resources, how do we handle conflicts?

6. **Human Escalation**: When should subagents escalate to humans vs. parents?

---

## 9. Next Steps

1. **Research existing implementations**: Check if any multi-agent frameworks have tackled recursive CLI spawning
2. **Prototype basic spawning**: Test Claude Code spawning Codex via bash
3. **Design agent_orchestrator_gab.jsonld**: Full AALang specification
4. **Test communication patterns**: Validate hand_off_documents approach

---

## References

- [AALang-Gab Repository](https://github.com/yenrab/AALang-Gab)
- [AutoGen Multi-Agent Framework](https://microsoft.github.io/autogen/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI Swarm](https://github.com/openai/swarm)

---

*Research Document - Layer -1 (Research)*
*Feature: Multi-Agent Orchestration*
*Created: 2026-02-06*
