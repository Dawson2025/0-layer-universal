---
resource_id: "476f732e-f534-4b30-a207-b48d01551c67"
resource_type: "output"
resource_name: "08_multi_agent_memory"
---
# Multi-Agent Memory Systems

<!-- section_id: "6e035417-fdad-403a-a506-e32b6e04f339" -->
## Overview

How memory is shared, coordinated, and synchronized across multiple AI agents working together. This is a rapidly growing research area as multi-agent systems become more prevalent.

---

<!-- section_id: "18c28966-9af2-4bbc-9b6d-ad45e7f49cec" -->
## 1. Memory Sharing Paradigms

<!-- section_id: "7d57ca0f-84c2-4d35-ba0a-884feff75e8a" -->
### Private Memory (No Sharing)
- Each agent maintains fully isolated memory
- No cross-agent information flow
- Simplest but limits collaboration

<!-- section_id: "c6910937-a9a1-44ea-b822-588da155775b" -->
### Shared Memory Pool
- Central memory store accessible by all agents
- Publish/subscribe patterns for updates
- Enables "joint attention" and immediate global knowledge
- Risk: information overload, lack of access control

<!-- section_id: "81998eb1-18c1-4e85-b77d-d84216f25c6e" -->
### Selective Sharing (Access-Controlled)
- Agents share specific memory subsets with specific peers
- Fine-grained access control through collaborative memory access graphs
- Granular permissions: read, write, subscribe per agent per memory scope
- Preserves privacy while enabling collaboration

<!-- section_id: "45b0a1d1-9a7a-4a11-a798-5f958ca46251" -->
### Blackboard Architecture
- Shared workspace where agents post and read information
- Agents contribute independently to a common knowledge structure
- Coordinator or priority system manages conflicts
- Classic AI architecture adapted for LLM agents

---

<!-- section_id: "fbb86b26-9471-4943-889f-734754da5cb0" -->
## 2. Memory Coordination Patterns

<!-- section_id: "2d558396-4643-426a-845f-115ba95f15aa" -->
### Cumulative Memory
- Each agent adds to a shared growing memory
- No deduplication or conflict resolution
- Simple but can become noisy

<!-- section_id: "f75a15ab-26b5-4d18-b204-5955c28491b7" -->
### Reflective/Summarized Memory
- Shared summaries rather than raw data
- Agents periodically consolidate and share insights
- Reduces bandwidth and noise

<!-- section_id: "df7b3582-cfca-49ee-8e26-196b2364aeac" -->
### Structured Memory with Access Control
- Role-based access to different memory regions
- Manager agents have broader access than worker agents
- Sensitive information compartmentalized

<!-- section_id: "7b859b43-7215-4dee-a0f9-1ca53f6ad090" -->
### Modular Multi-Component Systems
- Different memory components for different purposes
- Shared task memory + private agent memory + team knowledge base
- Each component independently managed

---

<!-- section_id: "375210ca-8db0-44c8-be08-cc46e3f7942a" -->
## 3. Framework Implementations

<!-- section_id: "0771a645-4e0c-493f-aa32-eb1d59500a91" -->
### AutoGen / AG2
- **Group chat memory**: Shared message history across all agents in a group
- **Selective context**: Agents can be configured to see only relevant messages
- **Teachable agents**: Memory that persists user instructions across sessions

<!-- section_id: "7387a14a-8448-4447-ba21-8bf3d7b5fae6" -->
### CrewAI
- **Unified Memory**: Shared across crew members via scope hierarchy
- **Hierarchical scopes**: Memory organized as filesystem-like tree; scope determines visibility
- **Task-level sharing**: Results from completed tasks available to subsequent tasks

<!-- section_id: "5e2b9c34-5c79-4191-9985-d80122902467" -->
### LangGraph
- **State-based sharing**: Graph state accessible by all nodes (agents)
- **Checkpointing**: State snapshots for resumption and coordination
- **Cross-thread memory**: Shared memory store across different conversation threads

<!-- section_id: "313cdc3a-7e82-44c0-b5a2-d5f79bde2b01" -->
### Letta (MemGPT)
- **Multi-agent memory**: Agents can modify each other's core memory blocks
- **Shared archival memory**: Common knowledge base across agents
- **Tool-based access**: Memory operations as function calls, shareable across agents

<!-- section_id: "46067dc1-eeef-49d8-82ce-901b968b4399" -->
### SHIMI (Decentralized)
- **Local memory trees**: Each agent maintains own semantic tree
- **Asynchronous synchronization**: Partial sync via Merkle-DAG + Bloom filters + CRDT
- **No central coordinator**: Peer-to-peer memory sharing
- **Eventual consistency**: CRDT merge operations ensure convergence

---

<!-- section_id: "0293de3d-5ef1-443f-bfc7-b1d349f90efb" -->
## 4. Key Research Challenges

<!-- section_id: "cf266104-a7bd-4abc-9d42-9a9a51f886bd" -->
### Synchronization
- Keeping distributed memories consistent across agents
- Real-time vs. eventual consistency trade-offs
- Bandwidth costs of synchronization
- SHIMI's approach: >90% bandwidth savings via partial sync

<!-- section_id: "fa74bf76-23cf-4ad4-b438-c78cef41f4e2" -->
### Conflict Resolution
- Multiple agents updating the same memory simultaneously
- Strategies: last-writer-wins, merge, CRDT, version vectors
- Semantic conflicts (contradictory facts) vs. structural conflicts (data format)

<!-- section_id: "d15dc706-5280-4891-a40d-7b806a753dd1" -->
### Privacy and Access Control
- Not all information should be shared with all agents
- Role-based access control for memory regions
- Privacy-preserving memory sharing (differential privacy, federated approaches)

<!-- section_id: "86eafb96-4c87-4fa1-aa51-19a002a2e3e0" -->
### Scalability
- Memory coordination overhead grows with agent count
- Hierarchical architectures to reduce communication
- Agent clustering for localized sharing

<!-- section_id: "ec1c438d-4d00-4e14-a624-b2950e51426d" -->
### Memory Auditing
- Tracking provenance of shared memories
- Accountability: who contributed what information
- Versioning and rollback for shared memory

---

<!-- section_id: "613aceda-b365-4ee3-97a0-e3892349258f" -->
## 5. Multi-Agent Memory Patterns

<!-- section_id: "6aa573ae-be0d-4338-a2a0-b18ef8e001aa" -->
### Hub-and-Spoke
- Central coordinator manages shared memory
- Agents communicate through central hub
- Simple coordination but single point of failure
- Example: CrewAI crew with manager agent

<!-- section_id: "34c61dd2-518a-4287-93d7-a465b46ff81c" -->
### Peer-to-Peer
- Agents share directly with each other
- No central coordinator needed
- More complex but more resilient
- Example: SHIMI decentralized memory

<!-- section_id: "94d579bf-1943-4320-bf86-6c06a634d1fa" -->
### Hierarchical
- Memory organized in layers matching organizational hierarchy
- Team-level, project-level, organization-level memory
- Agents access memory at their level and above
- Example: Layer-stage system with layer 0 (universal) → layer 1 (project)

<!-- section_id: "92b3e96d-5482-480e-af0c-66e444f2dc0f" -->
### Publish-Subscribe
- Agents publish memory updates to topics
- Other agents subscribe to relevant topics
- Decouples producers from consumers
- Enables selective information flow

---

<!-- section_id: "f44fcf91-8ce7-4b44-9f22-0ecc856797c0" -->
## 6. Emerging Research Directions

<!-- section_id: "d3d0ffcc-9b44-49fb-979c-2bef3900094e" -->
### RL-Driven Memory Management
- Reinforcement learning to optimize what to share and when
- Learning memory coordination policies from experience

<!-- section_id: "5e11ff92-e2dd-4a62-a9d3-04896bb37440" -->
### Cross-Agent Memory Transfer
- Transferring learned memories from experienced to new agents
- Knowledge distillation for memory

<!-- section_id: "c69d0426-c1aa-48c3-b24f-9147cfa8f1eb" -->
### Hierarchical Memory Architectures for Teams
- Multi-level memory matching team structure
- Automatic promotion of local insights to team-level memory

<!-- section_id: "ad8142f6-2daa-4e55-83dd-3eca48ae186e" -->
### Memory-Based Agent Specialization
- Agents develop specialized memories based on their roles
- Selective memory sharing based on task requirements

<!-- section_id: "856e0944-7690-4f34-b6b8-081f3a8857c4" -->
### MemIndex: Event-Based Distributed Memory
- Agentic event-based distributed memory management for multi-agent systems
- Published in ACM Transactions on Autonomous and Adaptive Systems

---

<!-- section_id: "897009c8-6897-4508-a742-5b3d123510e6" -->
## Sources

- [Memory in LLM-based Multi-agent Systems: Mechanisms, Challenges, and Collective (TechRxiv)](https://www.techrxiv.org/users/1007269/articles/1367390/)
- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [SHIMI: Decentralizing AI Memory (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- [MemIndex: Agentic Event-based Distributed Memory (ACM TAAS)](https://dl.acm.org/doi/10.1145/3774946)
- [Multi-Agent Systems and Workflow Survey (ResearchGate)](https://www.researchgate.net/publication/395128299)
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory)
- [Memory Mechanisms in LLM Agents (Emergent Mind)](https://www.emergentmind.com/topics/memory-mechanisms-in-llm-based-agents)
