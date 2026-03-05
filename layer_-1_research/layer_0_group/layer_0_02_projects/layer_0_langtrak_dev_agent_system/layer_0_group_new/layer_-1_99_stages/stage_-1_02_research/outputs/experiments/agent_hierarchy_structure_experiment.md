---
resource_id: "0cc815b8-baea-45b5-8b9a-b03991cc1a48"
resource_type: "output"
resource_name: "agent_hierarchy_structure_experiment"
---
# Agent Hierarchy Structure Experiment

**Status**: DESIGN — Experiment framework defined, trials not yet started
**Date**: 2026-02-26
**Goal**: Find the best agent delegation structure for developing LangTrak by testing several approaches and measuring performance

---

<!-- section_id: "f2a0eeff-8086-43a8-aa07-0ffb920ca6f1" -->
## Hypothesis

Different agent hierarchy structures will produce significantly different outcomes when applied to LangTrak development tasks. The optimal structure will enable agents to:
1. Correctly identify what needs to be done (requirement understanding)
2. Debug issues effectively (root cause identification speed)
3. Implement features completely (feature coverage)
4. Satisfy all requirements and design constraints (design compliance)
5. Coordinate without excessive context overhead (efficiency)

---

<!-- section_id: "29803f70-0ce3-465b-b966-33db2f05bd88" -->
## LangTrak Architecture (Constant Across All Trials)

All trials work with the same LangTrak codebase and feature set:

**10-Layer Feature Hierarchy:**
- L2: Infrastructure (Database, Auth, Firebase, Storage Manager, App)
- L3: Users (Profiles, Sessions)
- L4: Full Phoneme System (Inventory, Groups, Types, Frequency Tracking)
- L5: Phoneme Templates (Subset Selection, View/Filter of Full System)
- L6: Language Content (Words, Syllables, Positions)
- L7: Projects (Containers for Content, Storage Type, Variants)
- L8: Teams (Collaboration, Invites, Project Sharing)
- L9: Enhancements (TTS, Video, Suggestions) — cross-cutting
- L10: Admin (Phoneme Management, DB Tools, Dashboard) — cross-cutting
- L11: Orchestration (Firebase Sync, Universal + AI Coordination) — cross-cutting

**Known Issues** (from stage 08 criticism): 5 multisyllable test failures, 2 admin auth routing issues, 1 template application failure, 8 Firebase emulator tests, dual DB path design, 13+ TODO/FIXME files

**Test Suite**: 228/249 pass (91.6%), 16 feature modules, Flask 2.3.2

---

<!-- section_id: "42a3a97c-c8c0-44a9-bd86-e8f71f85403e" -->
## Trial Structures

<!-- section_id: "8d33aca6-7dbb-432c-801a-a2788ed38040" -->
### Trial A: One Agent Per Layer (10 Specialists)

**Structure**: Each of the 10 layers gets its own dedicated agent. Agents communicate only with direct neighbors (up/down in the dependency chain). Cross-cutting layers (L9-L11) communicate with specific layers they affect.

```
Manager Agent
├── L2 Infrastructure Agent
├── L3 Users Agent
├── L4 Phoneme System Agent
├── L5 Templates Agent
├── L6 Language Content Agent
├── L7 Projects Agent
├── L8 Teams Agent
├── L9 Enhancements Agent (cross-cuts L4, L6)
├── L10 Admin Agent (cross-cuts L2, L4, L5, L7)
└── L11 Orchestration Agent (cross-cuts L2, L7)
```

**Context model**: Each agent gets own STATIC + neighbor interfaces (2-3 lines per neighbor) + on-demand access to any layer
**Communication**: Relay chain (request passes through each layer to reach its destination)
**Delegation**: Manager delegates to specific layer agents based on task keywords

**Predicted strengths**: Clear ownership, minimal context per agent, good for isolated feature work
**Predicted weaknesses**: Slow for cross-layer tasks, relay overhead, manager must know which layer handles what

<!-- section_id: "b27e425a-186f-4967-9a83-6b8ba1d238d4" -->
### Trial B: Domain Cluster Agents (3 Clusters + Manager)

**Structure**: Group related layers into domain clusters. Each cluster agent handles multiple related layers.

```
Manager Agent
├── Foundation Cluster Agent (L2 Infrastructure + L3 Users)
├── Phoneme Domain Agent (L4 System + L5 Templates + L6 Content)
├── Collaboration Domain Agent (L7 Projects + L8 Teams)
└── Cross-Cutting Agent (L9 Enhancements + L10 Admin + L11 Orchestration)
```

**Context model**: Each cluster agent gets STATIC for all layers in its cluster + interfaces to other clusters
**Communication**: Direct between clusters (no relay chain)
**Delegation**: Manager delegates based on domain, not individual layer

**Predicted strengths**: Fewer agents to coordinate, domain experts understand related layers together, faster cross-layer work within clusters
**Predicted weaknesses**: More context per agent (cluster-wide), boundary between clusters is still a handoff point, one agent doing too many things

<!-- section_id: "038bd739-2bb1-4897-aaa3-5c57de3bd379" -->
### Trial C: Stage-First Agents (Per-Stage, Layer-Agnostic)

**Structure**: Instead of one agent per layer, one agent per development stage. Each stage agent works across ALL layers but only does its specific phase of work.

```
Manager Agent
├── Requirements Agent (understands what needs to be built across all layers)
├── Research Agent (investigates technical options for any layer)
├── Design Agent (architects solutions spanning any layers)
├── Planning Agent (breaks designs into tasks for any layer)
├── Development Agent (implements code in any layer's modules)
├── Testing Agent (writes and runs tests for any layer)
├── Criticism Agent (reviews work across all layers)
└── Fixing Agent (applies fixes anywhere)
```

**Context model**: Each stage agent gets full LangTrak architecture overview (all layers) + stage-specific methodology
**Communication**: Sequential handoff (requirements → research → design → planning → development → testing)
**Delegation**: Manager routes to stage agents based on task phase, not feature domain

**Predicted strengths**: Mirrors the existing stage-based workflow, natural for sequential development, each agent is a phase expert
**Predicted weaknesses**: Each agent needs broad context (all layers), hard to parallelize across features, no layer-specific deep expertise

<!-- section_id: "ca9f83d9-6abe-42f3-8f5f-8b496bb1b518" -->
### Trial D: Hybrid (Layer Specialists + Stage Coordinators)

**Structure**: Combine layer specialists (for domain knowledge) with stage coordinators (for workflow). Layer agents HAVE the knowledge; stage coordinators MANAGE the workflow.

```
Stage Coordinator (manages workflow phases)
├── Requirements Phase → queries Layer Agents for gaps
├── Design Phase → delegates architecture to Layer Agents
├── Development Phase → assigns implementation to Layer Agents
├── Testing Phase → asks Layer Agents to verify
│
Layer Agents (have domain knowledge):
├── Infrastructure Agent (L2-L3)
├── Phoneme Domain Agent (L4-L5-L6)
├── Projects Agent (L7-L8)
└── Cross-Cutting Agent (L9-L10-L11)
```

**Context model**: Layer agents get domain STATIC; stage coordinators get workflow methodology + layer agent interface summaries
**Communication**: Stage coordinator orchestrates; layer agents execute within their domain
**Delegation**: Two-level: manager → stage coordinator → layer agents

**Predicted strengths**: Best of both worlds (domain expertise + workflow management), supports parallelism (multiple layer agents work concurrently), clear separation of concerns
**Predicted weaknesses**: Most complex structure, coordination overhead between two levels, potential confusion about who decides what

<!-- section_id: "9f2a8622-a4fc-4723-b95a-916b66820e80" -->
### Trial E: Flat Team (No Hierarchy)

**Structure**: All agents are peers. No manager, no hierarchy. Shared task board. Any agent can pick up any task.

```
Shared Task Board
├── Agent 1 (generalist, grabs any available task)
├── Agent 2 (generalist, grabs any available task)
├── Agent 3 (generalist, grabs any available task)
└── Agent 4 (generalist, grabs any available task)
```

**Context model**: Each agent gets full LangTrak overview + reads task-specific context on demand
**Communication**: Via shared task board (no direct agent-to-agent messaging)
**Delegation**: Self-organized — agents claim tasks from the board

**Predicted strengths**: Simple, flexible, no coordination bottleneck, good for parallelism
**Predicted weaknesses**: No specialization, risk of conflicts, each agent needs broad context, no one has deep domain knowledge, hard to maintain consistency

---

<!-- section_id: "3c296c97-fad9-48db-a823-aa0c23b50a5a" -->
## Evaluation Criteria

<!-- section_id: "e3e48748-d207-4849-9122-2a5ac3ea45cc" -->
### Metrics (Scored 1-5 Per Trial)

| Metric | What It Measures | How To Evaluate |
|--------|-----------------|-----------------|
| **Requirement Understanding** | Can agents correctly identify what needs to be done? | Give agents a LangTrak issue. Do they correctly scope it? |
| **Debug Speed** | How quickly do agents find root causes? | Give agents a failing test. How many turns to find the cause? |
| **Feature Completeness** | Do implemented features cover all requirements? | Give agents a feature request. Does the implementation miss anything? |
| **Design Compliance** | Does work follow the architecture design? | Check if implementations respect layer boundaries and interfaces |
| **Context Efficiency** | How much context does each agent load? | Measure total context tokens loaded per task |
| **Coordination Overhead** | How much agent-to-agent messaging is needed? | Count messages between agents to complete a task |
| **Parallelism** | Can multiple things happen simultaneously? | Can agents work on independent features concurrently? |
| **Error Recovery** | How well does the system handle mistakes? | Introduce an error. How does the system detect and fix it? |

<!-- section_id: "61c79366-ae84-4b35-9659-e6b957c9fd36" -->
### Scoring

Each trial gets scores on all 8 metrics. Final score is weighted:
- Requirement Understanding: 20%
- Debug Speed: 15%
- Feature Completeness: 20%
- Design Compliance: 15%
- Context Efficiency: 10%
- Coordination Overhead: 10%
- Parallelism: 5%
- Error Recovery: 5%

<!-- section_id: "4ed6e920-ebc7-402f-a891-3da90d65f865" -->
### Test Tasks

Each trial must attempt the SAME set of test tasks:

| # | Task | Type | Layers Involved | Difficulty |
|---|------|------|-----------------|------------|
| T1 | Fix multisyllable word creation test failures | Debug | L6, L4, L7 | Medium |
| T2 | Add a new phoneme group type | Feature | L4, L5, L10 | Easy |
| T3 | Implement project variant duplication | Feature | L7, L2, L11 | Medium |
| T4 | Fix admin auth routing exceptions | Debug | L10, L2, L3 | Medium |
| T5 | Design and implement team invitation flow | Feature | L8, L7, L3, L2 | Hard |
| T6 | Add TTS preview for syllables | Feature | L9, L6, L4 | Hard |
| T7 | Resolve dual DB path design | Architecture | L2, all modules | Hard |

---

<!-- section_id: "dfa1c2eb-9a32-468a-b4c2-382d4d4ae4d9" -->
## Trial Execution Protocol

<!-- section_id: "8d7d709f-fb4d-44a8-ba52-73cb02d188aa" -->
### For Each Trial

1. **Setup**: Define agents per the trial structure. Create 0AGNOSTIC.md for each agent with appropriate context model.
2. **Calibration**: Run T1 (debug task) and T2 (easy feature) to validate the structure works at all.
3. **Full run**: Execute all 7 test tasks. Record metrics for each.
4. **Post-mortem**: Analyze where the structure helped and where it hindered. Document failure modes.

<!-- section_id: "7b00b7dc-0243-4075-a434-3487701f5f39" -->
### Recording Format

For each trial + task combination:

```markdown
## Trial [A-E] — Task T[1-7]

**Agents involved**: [which agents participated]
**Turns to complete**: [number of agent turns]
**Context loaded**: [approximate token count]
**Messages between agents**: [count]
**Outcome**: [success/partial/failure]
**Score**: [1-5 per metric]

### What Happened
[Narrative of how agents handled the task]

### What Worked
[Strengths observed]

### What Failed
[Weaknesses observed]
```

---

<!-- section_id: "026295b6-75db-4c6e-bfc6-0967b7e1487e" -->
## Expected Outcomes

Based on LangTrak's specific architecture:

- **Trial A** (per-layer) will likely struggle with cross-cutting tasks (T5, T6, T7) but excel at isolated layer work (T2)
- **Trial B** (domain clusters) should be a strong middle ground — the Phoneme Domain cluster handles T1, T2, T6 internally
- **Trial C** (per-stage) will be natural for sequential workflows but bottleneck on any task needing domain expertise
- **Trial D** (hybrid) is predicted to score highest overall but has the most coordination complexity
- **Trial E** (flat team) will be fastest for simple tasks but may produce inconsistent architecture decisions

The experiment should validate or invalidate these predictions and reveal which structure best matches LangTrak's specific dependency patterns.

---

<!-- section_id: "87a3681c-8e2c-47bb-8c93-49f96dc4486f" -->
## Results

*(To be filled after trials are executed)*

| Trial | ReqUnderstand | DebugSpeed | FeatureComplete | DesignComply | CtxEfficiency | CoordOverhead | Parallelism | ErrorRecovery | **Weighted Total** |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A: Per-Layer | — | — | — | — | — | — | — | — | — |
| B: Domain Clusters | — | — | — | — | — | — | — | — | — |
| C: Per-Stage | — | — | — | — | — | — | — | — | — |
| D: Hybrid | — | — | — | — | — | — | — | — | — |
| E: Flat Team | — | — | — | — | — | — | — | — | — |

---

<!-- section_id: "57cf761a-a8de-4b09-8425-174075f7fa76" -->
## Next Steps

1. Choose 2-3 trials to run first (recommend B, D, E for maximum variation)
2. Create agent 0AGNOSTIC.md files for chosen trial structures
3. Execute calibration tasks (T1, T2) for each
4. Run full task suite
5. Score and compare results
6. Write conclusions and recommendations
