---
resource_id: "36b4d52f-1f23-45db-9ae8-e41abc0e6fe1"
resource_type: "readme
document"
resource_name: "README"
---
# Experiment: Dependency-Based Agent Hierarchy

**Status**: READY — Structure created, agents defined, awaiting trial execution
**Date**: 2026-02-26
**Trial**: Revised Trial A — Dependency-Based with Absorbed Cross-Cutting

---

## Design

This experiment implements the **dependency-based agent hierarchy** design:
- 7 layers (L2-L8) instead of original 10 (L2-L11)
- Cross-cutting features (L9 Enhancements, L10 Admin, L11 Orchestration) absorbed into domain layers
- 38 sub-layers with internal dependency ordering
- OOP class hierarchy: BaseAgent → LayerAgent → SubLayerAgent + ManagerAgent
- 12 segregated interfaces between layers

**Design documents** (source of truth):
- `../../layer_-1_99_stages/stage_-1_04_design/outputs/design_decisions/dependency_based_structure/dependency_based_agent_hierarchy_design.md`
- `../../layer_-1_99_stages/stage_-1_04_design/outputs/design_decisions/dependency_based_structure/oop_class_hierarchy.md`
- `../../layer_-1_99_stages/stage_-1_04_design/outputs/design_decisions/dependency_based_structure/diagrams/dependency_based_architecture_diagrams.md`

**Research documents**:
- `../../layer_-1_99_stages/stage_-1_02_research/outputs/by_topic/01_hierarchy_structural_ideas.md`
- `../../layer_-1_99_stages/stage_-1_02_research/outputs/by_topic/02_sublayer_dependency_structures.md`
- `../../layer_-1_99_stages/stage_-1_02_research/outputs/by_topic/03_oop_agent_hierarchy_patterns.md`

---

## Agent Hierarchy

```
ManagerAgent (Factory + Mediator)
├── L2 InfrastructureAgent (7 sub-layers: App Factory, Database, Firebase, Storage, Auth, DB Admin, Firebase Sync)
├── L3 UsersAgent (3 sub-layers: User Model, Profiles, Sessions)
├── L4 PhonemeSystemAgent (7 sub-layers: Groups, Types, Phonemes, Frequency, Display, TTS, Admin)
├── L5 TemplatesAgent (4 sub-layers: Core, Selection, Application, Admin)
├── L6 LanguageContentAgent (7 sub-layers: Words, Syllables, Positions, Phoneme Refs, TTS, Suggestions, Video)
├── L7 ProjectsAgent (6 sub-layers: Core, Storage Type, Variants, Content Assoc, Dashboard, Menu)
└── L8 TeamsAgent (4 sub-layers: Team Model, Membership, Invites, Project Sharing)
```

Total: 1 Manager + 7 Layer Agents + 38 Sub-Layer responsibilities = 46 logical units

---

## Inter-Layer Dependency Chain

```
L2 Infrastructure → L3 Users → L4 Phonemes → L5 Templates → L6 Content → L7 Projects → L8 Teams
```

Each arrow = "layer below provides an interface that layer above depends on."

---

## Test Tasks

| ID | Task | Layers Involved | Tests |
|----|------|-----------------|-------|
| T1 | Multisyllable Debug | L6, L4, L7 | Cross-layer debugging, root cause identification |
| T2 | Admin Auth Routing | L2, L4, L7 | Auth + admin feature integration |
| T3 | Template Application | L5, L4, L7 | Template-to-project linking |
| T4 | TTS Phoneme + Word | L4.6, L6.5 | Split TTS (absorbed cross-cutting) |
| T5 | Team Invitation | L8, L7, L3, L2 | Full-chain traversal |
| T6 | Firebase Dual DB | L2.3, L2.4, L2.7, L7.2 | Infrastructure complexity |
| T7 | Full Feature (New) | All layers | End-to-end feature implementation |

---

## Evaluation Metrics

| Metric | Weight | Measures |
|--------|--------|----------|
| Task Completion | 20% | Did the agent(s) produce a correct solution? |
| Context Efficiency | 15% | How many tokens of context were loaded vs needed? |
| Delegation Accuracy | 15% | Did tasks reach the right agent on first try? |
| Cross-Layer Coordination | 15% | How well did multi-layer tasks flow? |
| Error Recovery | 10% | When something went wrong, how fast was recovery? |
| Scope Awareness | 10% | Did agents correctly identify scope boundaries? |
| Communication Overhead | 10% | How many inter-agent messages were needed? |
| Time to Solution | 5% | Wall-clock time to produce solution |

---

## Directory Structure

```
agents/           # Agent context definitions (what each agent knows, can do, interfaces)
interfaces/       # Interface definitions between layers
trial_runs/       # One directory per test task — execution logs, results
results/          # Aggregated metrics and comparison data
```

---

## How to Run a Trial

1. Pick a test task (T1-T7)
2. Set up the agent team using definitions in `agents/`
3. Present the task to the Manager Agent
4. Record: delegation chain, context loaded, messages exchanged, solution produced
5. Evaluate against metrics
6. Log results in `trial_runs/tN_*/` and aggregate in `results/metrics.md`
