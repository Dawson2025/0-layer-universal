# Multi-Agent Memory Systems

## Overview

How memory is shared, coordinated, and synchronized across multiple AI agents working together. This is a rapidly growing research area as multi-agent systems become more prevalent.

---

## 1. Memory Sharing Paradigms

### Private Memory (No Sharing)
- Each agent maintains fully isolated memory
- No cross-agent information flow
- Simplest but limits collaboration

### Shared Memory Pool
- Central memory store accessible by all agents
- Publish/subscribe patterns for updates
- Enables "joint attention" and immediate global knowledge
- Risk: information overload, lack of access control

### Selective Sharing (Access-Controlled)
- Agents share specific memory subsets with specific peers
- Fine-grained access control through collaborative memory access graphs
- Granular permissions: read, write, subscribe per agent per memory scope
- Preserves privacy while enabling collaboration

### Blackboard Architecture
- Shared workspace where agents post and read information
- Agents contribute independently to a common knowledge structure
- Coordinator or priority system manages conflicts
- Classic AI architecture adapted for LLM agents

---

## 2. Memory Coordination Patterns

### Cumulative Memory
- Each agent adds to a shared growing memory
- No deduplication or conflict resolution
- Simple but can become noisy

### Reflective/Summarized Memory
- Shared summaries rather than raw data
- Agents periodically consolidate and share insights
- Reduces bandwidth and noise

### Structured Memory with Access Control
- Role-based access to different memory regions
- Manager agents have broader access than worker agents
- Sensitive information compartmentalized

### Modular Multi-Component Systems
- Different memory components for different purposes
- Shared task memory + private agent memory + team knowledge base
- Each component independently managed

---

## 3. Framework Implementations

### AutoGen / AG2
- **Group chat memory**: Shared message history across all agents in a group
- **Selective context**: Agents can be configured to see only relevant messages
- **Teachable agents**: Memory that persists user instructions across sessions

### CrewAI
- **Unified Memory**: Shared across crew members via scope hierarchy
- **Hierarchical scopes**: Memory organized as filesystem-like tree; scope determines visibility
- **Task-level sharing**: Results from completed tasks available to subsequent tasks

### LangGraph
- **State-based sharing**: Graph state accessible by all nodes (agents)
- **Checkpointing**: State snapshots for resumption and coordination
- **Cross-thread memory**: Shared memory store across different conversation threads

### Letta (MemGPT)
- **Multi-agent memory**: Agents can modify each other's core memory blocks
- **Shared archival memory**: Common knowledge base across agents
- **Tool-based access**: Memory operations as function calls, shareable across agents

### SHIMI (Decentralized)
- **Local memory trees**: Each agent maintains own semantic tree
- **Asynchronous synchronization**: Partial sync via Merkle-DAG + Bloom filters + CRDT
- **No central coordinator**: Peer-to-peer memory sharing
- **Eventual consistency**: CRDT merge operations ensure convergence

---

## 4. Key Research Challenges

### Synchronization
- Keeping distributed memories consistent across agents
- Real-time vs. eventual consistency trade-offs
- Bandwidth costs of synchronization
- SHIMI's approach: >90% bandwidth savings via partial sync

### Conflict Resolution
- Multiple agents updating the same memory simultaneously
- Strategies: last-writer-wins, merge, CRDT, version vectors
- Semantic conflicts (contradictory facts) vs. structural conflicts (data format)

### Privacy and Access Control
- Not all information should be shared with all agents
- Role-based access control for memory regions
- Privacy-preserving memory sharing (differential privacy, federated approaches)

### Scalability
- Memory coordination overhead grows with agent count
- Hierarchical architectures to reduce communication
- Agent clustering for localized sharing

### Memory Auditing
- Tracking provenance of shared memories
- Accountability: who contributed what information
- Versioning and rollback for shared memory

---

## 5. Multi-Agent Memory Patterns

### Hub-and-Spoke
- Central coordinator manages shared memory
- Agents communicate through central hub
- Simple coordination but single point of failure
- Example: CrewAI crew with manager agent

### Peer-to-Peer
- Agents share directly with each other
- No central coordinator needed
- More complex but more resilient
- Example: SHIMI decentralized memory

### Hierarchical
- Memory organized in layers matching organizational hierarchy
- Team-level, project-level, organization-level memory
- Agents access memory at their level and above
- Example: Layer-stage system with layer 0 (universal) → layer 1 (project)

### Publish-Subscribe
- Agents publish memory updates to topics
- Other agents subscribe to relevant topics
- Decouples producers from consumers
- Enables selective information flow

---

## 6. Emerging Research Directions

### RL-Driven Memory Management
- Reinforcement learning to optimize what to share and when
- Learning memory coordination policies from experience

### Cross-Agent Memory Transfer
- Transferring learned memories from experienced to new agents
- Knowledge distillation for memory

### Hierarchical Memory Architectures for Teams
- Multi-level memory matching team structure
- Automatic promotion of local insights to team-level memory

### Memory-Based Agent Specialization
- Agents develop specialized memories based on their roles
- Selective memory sharing based on task requirements

### MemIndex: Event-Based Distributed Memory
- Agentic event-based distributed memory management for multi-agent systems
- Published in ACM Transactions on Autonomous and Adaptive Systems

---

## Sources

- [Memory in LLM-based Multi-agent Systems: Mechanisms, Challenges, and Collective (TechRxiv)](https://www.techrxiv.org/users/1007269/articles/1367390/)
- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [SHIMI: Decentralizing AI Memory (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- [MemIndex: Agentic Event-based Distributed Memory (ACM TAAS)](https://dl.acm.org/doi/10.1145/3774946)
- [Multi-Agent Systems and Workflow Survey (ResearchGate)](https://www.researchgate.net/publication/395128299)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
- [Memory Mechanisms in LLM Agents (Emergent Mind)](https://www.emergentmind.com/topics/memory-mechanisms-in-llm-based-agents)
