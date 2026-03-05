---
resource_id: "9359c2c2-9265-43b8-8fb1-081b2196e2e5"
resource_type: "output"
resource_name: "01_cognitive_science_foundations"
---
# Cognitive Science Foundations of AI Agent Memory

## Overview

Modern AI agent memory systems draw heavily from cognitive science theories of human memory. This file maps classical cognitive architectures and human memory types to their AI agent implementations.

---

## 1. Human Memory Types (Cognitive Science)

### Sensory Memory
- **Duration**: Milliseconds to seconds
- **Function**: Brief registration of sensory input before processing
- **Subtypes**: Iconic (visual), echoic (auditory), haptic (touch)
- **AI Analog**: Raw input buffers, unprocessed token streams, initial perception layers

### Short-Term / Working Memory
- **Duration**: Seconds to minutes
- **Capacity**: ~7 +/- 2 items (Miller's Law)
- **Function**: Active manipulation of currently relevant information
- **AI Analog**: Context window, attention mechanism, active prompt context
- **Key Theory**: Baddeley's multi-component model (central executive, phonological loop, visuospatial sketchpad, episodic buffer)

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

### Prospective Memory
- **Content**: Intentions, planned future actions
- **Properties**: Time-based or event-based triggers
- **AI Analog**: Task queues, scheduled actions, goal stacks

### Metamemory
- **Content**: Knowledge about one's own memory capabilities
- **Properties**: Self-monitoring, confidence calibration
- **AI Analog**: Self-reflection mechanisms, uncertainty estimation

---

## 2. Classical Cognitive Architectures

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

## 4. Key Principles from Cognitive Science Applied to AI

### Complementary Learning Systems Theory
- Fast learning system (hippocampus) + slow learning system (neocortex)
- AI analog: External memory (fast, specific) + parametric memory (slow, general)
- Sleep/replay consolidation: periodic transfer from episodic to semantic

### Levels of Processing (Craik & Lockhart)
- Deeper processing = better retention
- AI analog: Raw storage < summarization < reflection < abstraction

### Decay and Interference
- Memories fade without rehearsal (temporal decay)
- New information can interfere with old (retroactive interference)
- AI implementations: recency weighting, importance scoring, forgetting mechanisms

### Chunking and Schema Formation
- Grouping information into meaningful units
- AI analog: Summarization, entity extraction, knowledge graph construction

### Emotional/Salience Tagging
- Emotionally significant events remembered better
- AI analog: Importance scoring, salience-based retention

---

## 5. Neural Encoding of Relationship Types

For a deep dive into how the brain encodes different types of relationships between concepts (cause-effect, category membership, part-whole, etc.) and how this compares to vector embeddings and knowledge graphs, see `15_vectors_graphs_and_neurology.md`.

**Key findings**:
- The hippocampus handles **relational encoding** — storing individual relationships with their predicate-argument structure ("A is heavier than B" as structured data, not just "A and B are linked")
- The rostrolateral prefrontal cortex (RLPFC) handles **relational integration** — combining multiple relationships to generate new inferences (transitive inference: if A>B and B>C, then A>C)
- The PFC has an **anterior-posterior gradient**: posterior regions handle concrete relationships (push→falls), anterior regions handle abstract ones (analogies, formal logic)
- Relationship types are not labeled explicitly like knowledge graph edges — they're encoded implicitly by **which neural circuit processes them** (causal→lateral PFC, categorical→temporal cortex, spatial→parietal cortex, sequential→basal ganglia)

---

## Sources

- [SOAR Cognitive Architecture (Wikipedia)](https://en.wikipedia.org/wiki/Soar_(cognitive_architecture))
- [Analysis and Comparison of ACT-R and SOAR (arXiv:2201.09305)](https://arxiv.org/abs/2201.09305)
- [Introduction to the SOAR Cognitive Architecture (arXiv:2205.03854)](https://arxiv.org/pdf/2205.03854)
- [LIDA Cognitive Architecture (Wikipedia)](https://en.wikipedia.org/wiki/LIDA_(cognitive_architecture))
- [Comparing SOAR, ACT-R, CLARION, and DUAL](https://roboticsbiz.com/comparing-four-cognitive-architectures-soar-act-r-clarion-and-dual/)
- [Cognitive Architectures and Agents (Purdue)](https://ccn.psych.purdue.edu/papers/cogArch_agent-springer.pdf)
- [Cognitive Architecture in AI (Sema4)](https://sema4.ai/learning-center/cognitive-architecture-ai/)
