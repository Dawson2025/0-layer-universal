---
resource_id: "9359c2c2-9265-43b8-8fb1-081b2196e2e5"
resource_type: "output"
resource_name: "01_cognitive_science_foundations"
---
# Cognitive Science Foundations of AI Agent Memory

<!-- section_id: "e07b0a74-5ac7-48f5-a1d9-bd4b3cd814b2" -->
## Overview

Modern AI agent memory systems draw heavily from cognitive science theories of human memory. This file maps classical cognitive architectures and human memory types to their AI agent implementations.

---

<!-- section_id: "4b6a3a0e-372e-4d11-87d1-3f02aff48b5b" -->
## 1. Human Memory Types (Cognitive Science)

<!-- section_id: "f02578e0-63bf-44b9-a0d3-c74072ea8cbb" -->
### Sensory Memory
- **Duration**: Milliseconds to seconds
- **Function**: Brief registration of sensory input before processing
- **Subtypes**: Iconic (visual), echoic (auditory), haptic (touch)
- **AI Analog**: Raw input buffers, unprocessed token streams, initial perception layers

<!-- section_id: "71d1c0eb-4670-4f7a-bd26-e8143e35310f" -->
### Short-Term / Working Memory
- **Duration**: Seconds to minutes
- **Capacity**: ~7 +/- 2 items (Miller's Law)
- **Function**: Active manipulation of currently relevant information
- **AI Analog**: Context window, attention mechanism, active prompt context
- **Key Theory**: Baddeley's multi-component model (central executive, phonological loop, visuospatial sketchpad, episodic buffer)

<!-- section_id: "c60fbb66-35eb-470d-a4cc-8d22a9dbf6d1" -->
### Long-Term Memory
Three subtypes:

#### Episodic Memory
- **Content**: Personal experiences, events with spatiotemporal context
- **Properties**: Autobiographical, time-stamped, contextually rich
- **AI Analog**: Conversation logs, interaction histories, experience replays

#### Semantic Memory
- **Content**: General knowledge, facts, concepts, meanings
- **Properties**: Decontextualized, organized by relationships
- **AI Analog**: Knowledge bases, parametric knowledge in weights, knowledge graphs

#### Procedural Memory
- **Content**: Skills, habits, "how-to" knowledge
- **Properties**: Implicit, difficult to verbalize, automatic
- **AI Analog**: Tool-use patterns, learned action sequences, policy networks

<!-- section_id: "b213555f-b0ad-44cb-af68-816b2cc501c7" -->
### Prospective Memory
- **Content**: Intentions, planned future actions
- **Properties**: Time-based or event-based triggers
- **AI Analog**: Task queues, scheduled actions, goal stacks

<!-- section_id: "1b5b453e-4ecf-4ca2-81b0-496786306c9d" -->
### Metamemory
- **Content**: Knowledge about one's own memory capabilities
- **Properties**: Self-monitoring, confidence calibration
- **AI Analog**: Self-reflection mechanisms, uncertainty estimation

---

<!-- section_id: "657437f7-a00b-436b-b751-cd411410bfce" -->
## 2. Classical Cognitive Architectures

<!-- section_id: "0929671f-a12b-48de-bafc-8dd0e3f6ece7" -->
### SOAR (State, Operator, And Result)
**Developed by**: John Laird, Allen Newell, Paul Rosenbloom (1983+)

**Memory Types**:
| Memory | Function | Mechanism |
|--------|----------|-----------|
| **Working Memory** | Active state representation | Current goal, perceptions, intermediate results |
| **Procedural Memory** | Production rules for action selection | IF-THEN rules fired through preference-based selection |
| **Episodic Memory (EPMEM)** | Temporal experience recording | Automatic snapshots of working memory; cue-based retrieval |
| **Semantic Memory (SMEM)** | Long-term factual knowledge | Large-scale fact store; query-based retrieval into working memory |

**Key Features**:
- Continuous decision cycle through goal stack
- Chunking mechanism: automated learning of new production rules
- Episodic memory records working memory snapshots in temporal stream
- Semantic memory designed for very large long-term factual storage
- Reinforcement learning for rule utility

<!-- section_id: "b0d3014e-3e82-4c09-82b2-38b81a1916f7" -->
### ACT-R (Adaptive Control of Thought - Rational)
**Developed by**: John Anderson (1993+)

**Memory Types**:
| Memory | Function | Mechanism |
|--------|----------|-----------|
| **Declarative Memory** | Facts and episodes | Chunk-based storage; activation-based retrieval |
| **Procedural Memory** | Production rules | Condition-action pairs; utility-based selection |
| **Perceptual-Motor Buffers** | Working memory interface | Limited-capacity buffers connecting modules |

**Key Features**:
- Activation-based retrieval (base-level activation + spreading activation)
- Decay mechanism: memories decay logarithmically without rehearsal
- Noise in retrieval: probabilistic, not deterministic
- Utility learning for production rule selection
- Hybrid symbolic-subsymbolic architecture

<!-- section_id: "1c8bc4c5-3259-413d-9863-f6cc6fd8ee6b" -->
### LIDA (Learning Intelligent Distribution Agent)
**Developed by**: Stan Franklin (2006+)

**Memory Types**:
| Memory | Function | Mechanism |
|--------|----------|-----------|
| **Sensory Memory** | Raw perceptual input | Brief registration before processing |
| **Sensory-Motor Memory** | Sensor-action mappings | Direct perception-action links |
| **Perceptual Memory** | Pattern recognition | Implemented as slipnet |
| **Episodic Memory** | Past experiences | Event-specific temporal records |
| **Declarative Memory** | Facts and knowledge | Explicit factual storage |
| **Procedural Memory** | Action selection | Implemented as scheme net |
| **Transient Episodic Memory** | Recent episodes | Working memory bridge to episodic |

**Key Features**:
- Implements Global Workspace Theory (consciousness as broadcast)
- Asynchronous cognitive cycle: perception > attention > action > learning
- Most comprehensive memory type coverage of any cognitive architecture
- Emotional tagging via motivational system

<!-- section_id: "1a7ac64b-dcd3-4d08-93bc-6d8f77264332" -->
### CLARION (Connectionist Learning with Adaptive Rule Induction ON-line)
**Developed by**: Ron Sun (2002+)

**Memory Types**:
| Subsystem | Top Level (Explicit) | Bottom Level (Implicit) |
|-----------|---------------------|------------------------|
| **Action-Centered (ACS)** | Explicit action rules | Neural network action policies |
| **Non-Action-Centered (NCS)** | Declarative knowledge | Implicit associative knowledge |
| **Motivational (MS)** | Explicit goals | Implicit drives |
| **Metacognitive (MCS)** | Explicit monitoring rules | Implicit self-regulation |

**Key Features**:
- Dual-process theory: every subsystem has explicit (top) and implicit (bottom) representations
- Bottom-up learning: implicit knowledge can be extracted into explicit rules
- Top-down learning: explicit rules can be internalized into implicit knowledge
- Unique among architectures in modeling the implicit/explicit distinction

---

<!-- section_id: "eb0a6453-5c37-4a45-8ae6-b8283bf27b5f" -->
## 3. Mapping: Cognitive Types to AI Agent Memory

| Human Memory Type | AI Implementation | Example Frameworks |
|-------------------|-------------------|-------------------|
| Sensory | Input buffers, raw observation logs | Perception modules in embodied agents |
| Working Memory | Context window, attention, scratchpad | LLM context, MemGPT core memory |
| Episodic | Conversation history, experience replay | LangChain ConversationBuffer, Letta recall memory |
| Semantic | Knowledge bases, parametric weights | RAG stores, knowledge graphs, fine-tuned weights |
| Procedural | Tool-use patterns, action policies | ReAct patterns, learned tool chains |
| Prospective | Task queues, goal stacks | Agent planners, SOAR goal stack |
| Metamemory | Self-reflection, confidence scores | Reflexion, self-evaluation loops |

---

<!-- section_id: "b0b00c59-98a8-4ed4-a8c7-2f0f8df5dfeb" -->
## 4. Key Principles from Cognitive Science Applied to AI

<!-- section_id: "58749591-b71d-403e-a7f7-07433d50278a" -->
### Complementary Learning Systems Theory
- Fast learning system (hippocampus) + slow learning system (neocortex)
- AI analog: External memory (fast, specific) + parametric memory (slow, general)
- Sleep/replay consolidation: periodic transfer from episodic to semantic

<!-- section_id: "c29705ff-c43b-45fb-b213-0fec925d4f56" -->
### Levels of Processing (Craik & Lockhart)
- Deeper processing = better retention
- AI analog: Raw storage < summarization < reflection < abstraction

<!-- section_id: "b2ffea44-67eb-45af-96cf-a22cc1de50c3" -->
### Decay and Interference
- Memories fade without rehearsal (temporal decay)
- New information can interfere with old (retroactive interference)
- AI implementations: recency weighting, importance scoring, forgetting mechanisms

<!-- section_id: "3a0db7a5-5857-49ce-95e8-b5f610822536" -->
### Chunking and Schema Formation
- Grouping information into meaningful units
- AI analog: Summarization, entity extraction, knowledge graph construction

<!-- section_id: "259adc41-bf42-405d-8b7a-e1c2e915c9cc" -->
### Emotional/Salience Tagging
- Emotionally significant events remembered better
- AI analog: Importance scoring, salience-based retention

---

<!-- section_id: "a4459cee-37ae-4445-85fb-318a162a9245" -->
## 5. Neural Encoding of Relationship Types

For a deep dive into how the brain encodes different types of relationships between concepts (cause-effect, category membership, part-whole, etc.) and how this compares to vector embeddings and knowledge graphs, see `15_vectors_graphs_and_neurology.md`.

**Key findings**:
- The hippocampus handles **relational encoding** — storing individual relationships with their predicate-argument structure ("A is heavier than B" as structured data, not just "A and B are linked")
- The rostrolateral prefrontal cortex (RLPFC) handles **relational integration** — combining multiple relationships to generate new inferences (transitive inference: if A>B and B>C, then A>C)
- The PFC has an **anterior-posterior gradient**: posterior regions handle concrete relationships (push→falls), anterior regions handle abstract ones (analogies, formal logic)
- Relationship types are not labeled explicitly like knowledge graph edges — they're encoded implicitly by **which neural circuit processes them** (causal→lateral PFC, categorical→temporal cortex, spatial→parietal cortex, sequential→basal ganglia)

---

<!-- section_id: "e5c13c56-2c30-45d5-8c5f-5d6ff799305f" -->
## Sources

- [SOAR Cognitive Architecture (Wikipedia)](https://en.wikipedia.org/wiki/Soar_(cognitive_architecture))
- [Analysis and Comparison of ACT-R and SOAR (arXiv:2201.09305)](https://arxiv.org/abs/2201.09305)
- [Introduction to the SOAR Cognitive Architecture (arXiv:2205.03854)](https://arxiv.org/pdf/2205.03854)
- [LIDA Cognitive Architecture (Wikipedia)](https://en.wikipedia.org/wiki/LIDA_(cognitive_architecture))
- [Comparing SOAR, ACT-R, CLARION, and DUAL](https://roboticsbiz.com/comparing-four-cognitive-architectures-soar-act-r-clarion-and-dual/)
- [Cognitive Architectures and Agents (Purdue)](https://ccn.psych.purdue.edu/papers/cogArch_agent-springer.pdf)
- [Cognitive Architecture in AI (Sema4)](https://sema4.ai/learning-center/cognitive-architecture-ai/)
