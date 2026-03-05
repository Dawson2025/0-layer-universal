---
resource_id: "1dde8666-d08e-491f-a615-51353fee8276"
resource_type: "document"
resource_name: "framework_orchestration_overview"
---
# Framework Orchestration Overview

<!-- section_id: "45e8b2a9-7923-445d-a237-8a11f7b7b536" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "36c8f70b-1966-49ac-bd29-c5d81bfbe1a0" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "ede566a7-a9cd-4e3d-b0df-6d8c3f5c8527" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "59da1380-4f5a-4883-ae62-70bd1f51b33c" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "906934db-d9c4-44ef-9b49-7ccf05a0c6b5" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "9a6d62dd-c351-4b92-a5c0-4c9d88e1db4d" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "4bec0515-4b75-4ecb-83af-d7bbb25f8b0d" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "f5abc943-9c73-4ac5-92b2-c5f336e92872" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "56ec0491-c30c-4cf2-abe1-84cf1845245a" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "23d3e9f8-0fc8-4371-97eb-37ed9f0968e5" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "2bbae0e8-8238-4051-b99b-c1e70cc9b87c" -->
## Framework Summary

<!-- section_id: "b8b38581-4336-433e-a406-3f9323f2fa6a" -->
### LangGraph
**Best For**: Deterministic workflows with explicit state control, checkpointing, and complex conditional logic.

**Strengths**:
- Graph-based state machine control
- Excellent auditability and debugging
- Checkpointing and human-in-the-loop support
- Strong tool integration via LangChain ecosystem

**Use Cases**:
- L0-L2 managers requiring explicit control flow
- Workflows with conditional branching and cycles (plan → implement → test → fix)
- Production systems requiring reliability and observability

**Key Pattern**: Define state machine nodes for each stage/operation, edges for transitions, and use checkpointing for resumability.

<!-- section_id: "16782d9e-8df2-4664-ae4b-eae3ca5b430f" -->
### AutoGen
**Best For**: Dialogue-heavy exploration, negotiation, and conversational multi-agent patterns.

**Strengths**:
- Conversational multi-agent interactions
- Easy to prototype agent collaborations
- Built-in code execution and tool use
- Good for exploratory workflows

**Use Cases**:
- L1/L2 request and instructions stages (dialogue-heavy)
- Rapid prototyping of new agent patterns
- Workflows where agents need to negotiate solutions

**Key Pattern**: Define specialized agents (project manager, requirements analyst, etc.) that converse via GroupChat, then extract structured handoffs from conversation.

<!-- section_id: "cd061eef-de2b-42ea-8aa9-cd8fcba35e83" -->
### CrewAI
**Best For**: Role-based team abstractions with clear task delegation patterns.

**Strengths**:
- Natural "team" metaphor (designer, developer, tester)
- Task assignment and dependency management
- Sequential and parallel task execution
- Intuitive for feature-level work

**Use Cases**:
- L2 feature managers with clear role separation
- Workflows mimicking human team structures
- Parallel execution of independent subtasks

**Key Pattern**: Define role-based agents (UI designer, backend developer, QA engineer), assign tasks with dependencies, execute crew in sequential or parallel mode.

<!-- section_id: "66f1f0fe-0f68-4ee4-8627-04ff5ddd7085" -->
### MetaGPT
**Best For**: Opinionated "software team in a box" with standardized artifacts (PRDs, design docs, code).

**Strengths**:
- Prescriptive software engineering roles (PM, architect, engineer)
- Structured document outputs
- Comprehensive end-to-end feature development
- Batteries-included approach

**Use Cases**:
- L1/L2 managers for greenfield feature development
- Projects wanting standardized documentation outputs
- Teams preferring opinionated structure over flexibility

**Key Pattern**: Hire pre-defined roles (ProductManager, Architect, Engineer), run project with task description, extract standardized artifacts.

---

<!-- section_id: "4b12b169-627e-457a-aa4c-4c7d0a3a6651" -->
## Integration Checklist

When integrating a framework into the hierarchy, ensure:

- [ ] **Handoff Compatibility**: Can it read/write JSON handoffs per the canonical schema?
- [ ] **Context Loading**: Can it load cascading CLAUDE.md/AGENTS.md/GEMINI.md files?
- [ ] **Tool Integration**: Can it call external CLIs (codex, gemini, claude-code)?
- [ ] **State Persistence**: Does it preserve handoff state across runs?
- [ ] **Error Handling**: Can it report failures in handoff format?
- [ ] **Parallel Execution**: Does it support concurrent worker spawning?
- [ ] **Observability**: Can you inspect agent interactions and decisions?

---

<!-- section_id: "70630b32-3eee-4999-ba91-c1548b63d211" -->
## Minimal Integration Examples

<!-- section_id: "99ef21d2-ba6d-44f8-9858-a13d2ca0bb54" -->
### LangGraph as L1 Manager

```python
from langgraph.graph import StateGraph
from typing import TypedDict
import json

class L1ManagerState(TypedDict):
    handoff: dict  # Incoming handoff from L0
    subtasks: list[dict]  # Decomposed tasks for L2
    results: list[dict]  # Aggregated results from L2
    status: str

def read_handoff(state: L1ManagerState):
    # Read incoming.json from L1 handoff directory
    with open("layer_1_project/1.01_manager_handoff_documents/1.00_to_universal/incoming.json") as f:
        state["handoff"] = json.load(f)
    return state

def decompose_tasks(state: L1ManagerState):
    # Use LLM to decompose into L2 feature subtasks
    # Load layer context from CLAUDE.md
    state["subtasks"] = llm_decompose(state["handoff"])
    return state

def spawn_l2_workers(state: L1ManagerState):
    # Launch L2 feature managers (via CLI or framework)
    results = []
    for task in state["subtasks"]:
        result = spawn_l2_manager(task)  # CLI call to claude-code or codex
        results.append(result)
    state["results"] = results
    state["status"] = "completed"
    return state

# Build graph
workflow = StateGraph(L1ManagerState)
workflow.add_node("read", read_handoff)
workflow.add_node("decompose", decompose_tasks)
workflow.add_node("spawn", spawn_l2_workers)
workflow.add_edge("read", "decompose")
workflow.add_edge("decompose", "spawn")
workflow.set_entry_point("read")

# Execute
result = workflow.invoke({})
```

<!-- section_id: "2962b274-b340-4fd5-8c0b-17763408d34c" -->
### CrewAI as L2 Feature Manager

```python
from crewai import Agent, Task, Crew
import json

# Load incoming handoff
with open("layer_2_auth/2.01_manager_handoff_documents/incoming.json") as f:
    handoff = json.load(f)

# Define role-based agents
ui_designer = Agent(
    role="UI/UX Designer",
    goal="Design authentication UI components",
    backstory="Expert in user experience and interface design",
    tools=[read_file, web_search]
)

backend_dev = Agent(
    role="Backend Developer",
    goal="Implement authentication backend logic",
    backstory="Full-stack developer with security expertise",
    tools=[codex_cli, read_file, write_file]
)

qa_engineer = Agent(
    role="QA Engineer",
    goal="Test authentication flows and security",
    backstory="Security-focused QA specialist",
    tools=[run_tests, codex_cli]
)

# Define tasks from handoff
design_task = Task(
    description=f"{handoff['task']} - Design UI components",
    agent=ui_designer
)

implement_task = Task(
    description=f"{handoff['task']} - Implement backend",
    agent=backend_dev,
    context=[design_task]  # Depends on design
)

test_task = Task(
    description=f"{handoff['task']} - Test and verify",
    agent=qa_engineer,
    context=[implement_task]
)

# Execute crew
crew = Crew(
    agents=[ui_designer, backend_dev, qa_engineer],
    tasks=[design_task, implement_task, test_task],
    process="sequential"
)

result = crew.kickoff()

# Write outgoing handoff
outgoing = {
    "schemaVersion": "1.0.0",
    "id": handoff["id"] + "-result",
    "status": "completed",
    "results": result,
    "artifacts": {"design": "...", "code": "...", "tests": "..."}
}

with open("layer_2_auth/2.01_manager_handoff_documents/outgoing.json", "w") as f:
    json.dump(outgoing, f, indent=2)
```

---

<!-- section_id: "08afa3b8-9b96-4f9e-bfe6-2ac8743b3ee4" -->
## Hybrid Patterns

Frameworks can be mixed within the hierarchy:

**Pattern 1: LangGraph Supervisor + CrewAI Features**
- L0: LangGraph supervisor managing overall workflow
- L1: LangGraph project managers
- L2: CrewAI "teams" for each feature
- L3: Direct CLI calls (codex, claude-code) as workers

**Pattern 2: AutoGen Planning + LangGraph Execution**
- Request/Instructions: AutoGen for dialogue
- Planning: AutoGen for collaborative planning
- Implementation onward: LangGraph for deterministic execution

**Pattern 3: Framework-Free Supervisor + Framework Workers**
- Supervisor: Simple Python/shell scripts watching handoffs
- L1/L2 Managers: Framework-based (LangGraph, CrewAI, etc.)
- L3/L4 Workers: Direct CLI tools (codex, gemini, claude-code)

---

<!-- section_id: "b272bb90-9a56-442c-b8fd-8d2af46a4a76" -->
## When to Skip Frameworks

You may not need a framework at all if:
- Work is straightforward and decomposable
- Simple shell scripts or Python can coordinate CLI calls
- You want minimal dependencies
- Handoff protocol is sufficient for coordination

**Example**: L2 feature manager that:
1. Reads incoming handoff
2. Decomposes into 3 component tasks
3. Spawns 3 Codex workers via `subprocess.run(["codex", ...])`
4. Waits for all to complete
5. Aggregates outgoing handoffs
6. Writes L2 outgoing handoff

No framework needed - just handoffs and CLI calls.

---

<!-- section_id: "69368f6f-3bb7-4c62-8c65-376dac2d9c07" -->
## Migration Path

If starting from scratch or migrating existing workflows:

**Phase 1: Manual CLI Orchestration** (Week 1-2)
- Use shell scripts to chain claude-code, codex, gemini
- Handoffs as simple JSON files
- Manual supervision

**Phase 2: Prototype with AutoGen/CrewAI** (Week 3-4)
- Implement L1/L2 managers with AutoGen or CrewAI
- Keep L3 workers as direct CLI calls
- Test multi-agent patterns

**Phase 3: Formalize with LangGraph** (Week 5-8)
- Convert successful patterns to LangGraph for production
- Add checkpointing, error recovery, monitoring
- Scale to more layers and parallel workers

**Phase 4: Hybrid Optimization** (Ongoing)
- Use frameworks where they excel
- Direct CLI calls for simple workers
- Continuous improvement based on metrics

---

<!-- section_id: "e74eb539-9495-4f40-be2a-4bb2337a65ce" -->
## Related Documentation

**Within 0_ai_context**:
- **AI Framework Docs**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/`
  - `framework-comparison.md` - Comparison of Spec Kit, BMAD Method, and other frameworks
  - `integration-guide.md` - Integration with existing tools
  - `tool-selection-guide.md` - Decision framework for tool selection
- **CLI Recursion**: `sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
- **Handoff Schema**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Normative Specification**:
- **Framework Orchestration (Detailed)**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`
- **Architecture**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Supervisor Patterns**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

---

<!-- section_id: "ce12bdb6-071a-4049-9ad3-303b5b25c31d" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.

---

<!-- section_id: "74386233-0c9f-4637-b23b-11d5a5ff2715" -->
## Legacy Universal Protocols Source

# Framework Orchestration Overview

<!-- section_id: "aa73733f-043f-4f4a-9521-21d491162fac" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "74c09662-3a3c-4c38-bb5f-2990f03d9a75" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "72e52ee2-0a94-4d81-9a13-b68453516a4d" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "9b205d69-7a9e-4798-878d-bca6171e9719" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "a6c30db0-7ec6-42dc-8cff-2153e9e22835" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "07e2f403-ce74-43ce-a543-7fd5496660a2" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "04fc8227-185f-4339-a45f-b9f4475133ad" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "f6c9d968-f3d2-40b7-a0fd-3d3fac49b53e" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "08d7a63b-1788-496f-80ec-fd875ba5a1fb" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "e97e0063-bef0-4fc3-9561-71b0ad99a9b3" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "9c07ea22-7409-4e1a-aa34-870f28d22b9a" -->
## Framework Summary

<!-- section_id: "cd63e2ab-3600-4809-a1ce-cc34fe52d814" -->
### LangGraph
**Best For**: Deterministic workflows with explicit state control, checkpointing, and complex conditional logic.

**Strengths**:
- Graph-based state machine control
- Excellent auditability and debugging
- Checkpointing and human-in-the-loop support
- Strong tool integration via LangChain ecosystem

**Use Cases**:
- L0-L2 managers requiring explicit control flow
- Workflows with conditional branching and cycles (plan → implement → test → fix)
- Production systems requiring reliability and observability

**Key Pattern**: Define state machine nodes for each stage/operation, edges for transitions, and use checkpointing for resumability.

<!-- section_id: "679a758d-2892-4000-aa79-3805baa613bf" -->
### AutoGen
**Best For**: Dialogue-heavy exploration, negotiation, and conversational multi-agent patterns.

**Strengths**:
- Conversational multi-agent interactions
- Easy to prototype agent collaborations
- Built-in code execution and tool use
- Good for exploratory workflows

**Use Cases**:
- L1/L2 request and instructions stages (dialogue-heavy)
- Rapid prototyping of new agent patterns
- Workflows where agents need to negotiate solutions

**Key Pattern**: Define specialized agents (project manager, requirements analyst, etc.) that converse via GroupChat, then extract structured handoffs from conversation.

<!-- section_id: "35386703-32d5-4782-99ff-cde3fcc0a266" -->
### CrewAI
**Best For**: Role-based team abstractions with clear task delegation patterns.

**Strengths**:
- Natural "team" metaphor (designer, developer, tester)
- Task assignment and dependency management
- Sequential and parallel task execution
- Intuitive for feature-level work

**Use Cases**:
- L2 feature managers with clear role separation
- Workflows mimicking human team structures
- Parallel execution of independent subtasks

**Key Pattern**: Define role-based agents (UI designer, backend developer, QA engineer), assign tasks with dependencies, execute crew in sequential or parallel mode.

<!-- section_id: "42179a1f-bb70-41f7-be59-5c7ca39e0a91" -->
### MetaGPT
**Best For**: Opinionated "software team in a box" with standardized artifacts (PRDs, design docs, code).

**Strengths**:
- Prescriptive software engineering roles (PM, architect, engineer)
- Structured document outputs
- Comprehensive end-to-end feature development
- Batteries-included approach

**Use Cases**:
- L1/L2 managers for greenfield feature development
- Projects wanting standardized documentation outputs
- Teams preferring opinionated structure over flexibility

**Key Pattern**: Hire pre-defined roles (ProductManager, Architect, Engineer), run project with task description, extract standardized artifacts.

---

<!-- section_id: "3c9ab616-4225-4825-baeb-8d2d66584e44" -->
## Integration Checklist

When integrating a framework into the hierarchy, ensure:

- [ ] **Handoff Compatibility**: Can it read/write JSON handoffs per the canonical schema?
- [ ] **Context Loading**: Can it load cascading CLAUDE.md/AGENTS.md/GEMINI.md files?
- [ ] **Tool Integration**: Can it call external CLIs (codex, gemini, claude-code)?
- [ ] **State Persistence**: Does it preserve handoff state across runs?
- [ ] **Error Handling**: Can it report failures in handoff format?
- [ ] **Parallel Execution**: Does it support concurrent worker spawning?
- [ ] **Observability**: Can you inspect agent interactions and decisions?

---

<!-- section_id: "46c23aea-a72d-43ac-8422-663cc533b941" -->
## Minimal Integration Examples

<!-- section_id: "25ebbe9a-12c9-4e09-9985-de64834eb310" -->
### LangGraph as L1 Manager

```python
from langgraph.graph import StateGraph
from typing import TypedDict
import json

class L1ManagerState(TypedDict):
    handoff: dict  # Incoming handoff from L0
    subtasks: list[dict]  # Decomposed tasks for L2
    results: list[dict]  # Aggregated results from L2
    status: str

def read_handoff(state: L1ManagerState):
    # Read incoming.json from L1 handoff directory
    with open("layer_1_project/1.01_manager_handoff_documents/1.00_to_universal/incoming.json") as f:
        state["handoff"] = json.load(f)
    return state

def decompose_tasks(state: L1ManagerState):
    # Use LLM to decompose into L2 feature subtasks
    # Load layer context from CLAUDE.md
    state["subtasks"] = llm_decompose(state["handoff"])
    return state

def spawn_l2_workers(state: L1ManagerState):
    # Launch L2 feature managers (via CLI or framework)
    results = []
    for task in state["subtasks"]:
        result = spawn_l2_manager(task)  # CLI call to claude-code or codex
        results.append(result)
    state["results"] = results
    state["status"] = "completed"
    return state

# Build graph
workflow = StateGraph(L1ManagerState)
workflow.add_node("read", read_handoff)
workflow.add_node("decompose", decompose_tasks)
workflow.add_node("spawn", spawn_l2_workers)
workflow.add_edge("read", "decompose")
workflow.add_edge("decompose", "spawn")
workflow.set_entry_point("read")

# Execute
result = workflow.invoke({})
```

<!-- section_id: "978fc25a-46d5-4ba5-8b62-4cc88830fd0b" -->
### CrewAI as L2 Feature Manager

```python
from crewai import Agent, Task, Crew
import json

# Load incoming handoff
with open("layer_2_auth/2.01_manager_handoff_documents/incoming.json") as f:
    handoff = json.load(f)

# Define role-based agents
ui_designer = Agent(
    role="UI/UX Designer",
    goal="Design authentication UI components",
    backstory="Expert in user experience and interface design",
    tools=[read_file, web_search]
)

backend_dev = Agent(
    role="Backend Developer",
    goal="Implement authentication backend logic",
    backstory="Full-stack developer with security expertise",
    tools=[codex_cli, read_file, write_file]
)

qa_engineer = Agent(
    role="QA Engineer",
    goal="Test authentication flows and security",
    backstory="Security-focused QA specialist",
    tools=[run_tests, codex_cli]
)

# Define tasks from handoff
design_task = Task(
    description=f"{handoff['task']} - Design UI components",
    agent=ui_designer
)

implement_task = Task(
    description=f"{handoff['task']} - Implement backend",
    agent=backend_dev,
    context=[design_task]  # Depends on design
)

test_task = Task(
    description=f"{handoff['task']} - Test and verify",
    agent=qa_engineer,
    context=[implement_task]
)

# Execute crew
crew = Crew(
    agents=[ui_designer, backend_dev, qa_engineer],
    tasks=[design_task, implement_task, test_task],
    process="sequential"
)

result = crew.kickoff()

# Write outgoing handoff
outgoing = {
    "schemaVersion": "1.0.0",
    "id": handoff["id"] + "-result",
    "status": "completed",
    "results": result,
    "artifacts": {"design": "...", "code": "...", "tests": "..."}
}

with open("layer_2_auth/2.01_manager_handoff_documents/outgoing.json", "w") as f:
    json.dump(outgoing, f, indent=2)
```

---

<!-- section_id: "be7a121d-4811-4be6-9e9a-b0571c68851e" -->
## Hybrid Patterns

Frameworks can be mixed within the hierarchy:

**Pattern 1: LangGraph Supervisor + CrewAI Features**
- L0: LangGraph supervisor managing overall workflow
- L1: LangGraph project managers
- L2: CrewAI "teams" for each feature
- L3: Direct CLI calls (codex, claude-code) as workers

**Pattern 2: AutoGen Planning + LangGraph Execution**
- Request/Instructions: AutoGen for dialogue
- Planning: AutoGen for collaborative planning
- Implementation onward: LangGraph for deterministic execution

**Pattern 3: Framework-Free Supervisor + Framework Workers**
- Supervisor: Simple Python/shell scripts watching handoffs
- L1/L2 Managers: Framework-based (LangGraph, CrewAI, etc.)
- L3/L4 Workers: Direct CLI tools (codex, gemini, claude-code)

---

<!-- section_id: "ad990e1a-775f-47f4-806e-6e4653707580" -->
## When to Skip Frameworks

You may not need a framework at all if:
- Work is straightforward and decomposable
- Simple shell scripts or Python can coordinate CLI calls
- You want minimal dependencies
- Handoff protocol is sufficient for coordination

**Example**: L2 feature manager that:
1. Reads incoming handoff
2. Decomposes into 3 component tasks
3. Spawns 3 Codex workers via `subprocess.run(["codex", ...])`
4. Waits for all to complete
5. Aggregates outgoing handoffs
6. Writes L2 outgoing handoff

No framework needed - just handoffs and CLI calls.

---

<!-- section_id: "908308f0-bbb4-48b2-af2f-7ea2668db803" -->
## Migration Path

If starting from scratch or migrating existing workflows:

**Phase 1: Manual CLI Orchestration** (Week 1-2)
- Use shell scripts to chain claude-code, codex, gemini
- Handoffs as simple JSON files
- Manual supervision

**Phase 2: Prototype with AutoGen/CrewAI** (Week 3-4)
- Implement L1/L2 managers with AutoGen or CrewAI
- Keep L3 workers as direct CLI calls
- Test multi-agent patterns

**Phase 3: Formalize with LangGraph** (Week 5-8)
- Convert successful patterns to LangGraph for production
- Add checkpointing, error recovery, monitoring
- Scale to more layers and parallel workers

**Phase 4: Hybrid Optimization** (Ongoing)
- Use frameworks where they excel
- Direct CLI calls for simple workers
- Continuous improvement based on metrics

---

<!-- section_id: "05838d6f-3df3-44d4-9b4b-dc260288fa1f" -->
## Related Documentation

**Within 0_ai_context**:
- **AI Framework Docs**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/`
  - `framework-comparison.md` - Comparison of Spec Kit, BMAD Method, and other frameworks
  - `integration-guide.md` - Integration with existing tools
  - `tool-selection-guide.md` - Decision framework for tool selection
- **CLI Recursion**: `sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
- **Handoff Schema**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Normative Specification**:
- **Framework Orchestration (Detailed)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`
- **Architecture**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Supervisor Patterns**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

---

<!-- section_id: "e660a69d-bec0-441a-ad0b-456a06070a58" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.


---

<!-- section_id: "4924fca7-0274-485e-a561-e42241129bab" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`

# Framework Orchestration Overview

<!-- section_id: "0e6bd31b-f633-487a-84f6-cca4b481c963" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "db4e245d-faab-46a6-b26c-8ff3a48433ff" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "28676cee-b96c-42f5-b137-94c13ffb0bfa" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "1666f415-b8d7-45df-9a4c-4d66f06639de" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "cdf292f1-c2c1-44ce-bc65-786ff5f06107" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "edb25547-8cce-4712-8874-f2c4ed051ec9" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "6e640e98-7bbd-48c9-abc7-cb4b2ab5b749" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "17c84e28-7ec7-4bf8-9334-9670813f94d9" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "258342ab-7676-4718-baa9-08d8fe849570" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "9a5dab92-512c-47e4-b2fa-a6bb96855998" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "eac3d735-d8b0-4fbc-8cf4-d7d122abf05b" -->
## Framework Summary

<!-- section_id: "f9e26e3e-8761-4364-895a-8d03b27ac5d8" -->
### LangGraph
**Best For**: Deterministic workflows with explicit state control, checkpointing, and complex conditional logic.

**Strengths**:
- Graph-based state machine control
- Excellent auditability and debugging
- Checkpointing and human-in-the-loop support
- Strong tool integration via LangChain ecosystem

**Use Cases**:
- L0-L2 managers requiring explicit control flow
- Workflows with conditional branching and cycles (plan → implement → test → fix)
- Production systems requiring reliability and observability

**Key Pattern**: Define state machine nodes for each stage/operation, edges for transitions, and use checkpointing for resumability.

<!-- section_id: "afab28db-3e86-43d5-9031-cb7a4ed4af4b" -->
### AutoGen
**Best For**: Dialogue-heavy exploration, negotiation, and conversational multi-agent patterns.

**Strengths**:
- Conversational multi-agent interactions
- Easy to prototype agent collaborations
- Built-in code execution and tool use
- Good for exploratory workflows

**Use Cases**:
- L1/L2 request and instructions stages (dialogue-heavy)
- Rapid prototyping of new agent patterns
- Workflows where agents need to negotiate solutions

**Key Pattern**: Define specialized agents (project manager, requirements analyst, etc.) that converse via GroupChat, then extract structured handoffs from conversation.

<!-- section_id: "d0347459-3ca8-4306-b16c-4b97c26b5b9d" -->
### CrewAI
**Best For**: Role-based team abstractions with clear task delegation patterns.

**Strengths**:
- Natural "team" metaphor (designer, developer, tester)
- Task assignment and dependency management
- Sequential and parallel task execution
- Intuitive for feature-level work

**Use Cases**:
- L2 feature managers with clear role separation
- Workflows mimicking human team structures
- Parallel execution of independent subtasks

**Key Pattern**: Define role-based agents (UI designer, backend developer, QA engineer), assign tasks with dependencies, execute crew in sequential or parallel mode.

<!-- section_id: "be3e0d6d-4017-443c-b120-86a6b8ae2be1" -->
### MetaGPT
**Best For**: Opinionated "software team in a box" with standardized artifacts (PRDs, design docs, code).

**Strengths**:
- Prescriptive software engineering roles (PM, architect, engineer)
- Structured document outputs
- Comprehensive end-to-end feature development
- Batteries-included approach

**Use Cases**:
- L1/L2 managers for greenfield feature development
- Projects wanting standardized documentation outputs
- Teams preferring opinionated structure over flexibility

**Key Pattern**: Hire pre-defined roles (ProductManager, Architect, Engineer), run project with task description, extract standardized artifacts.

---

<!-- section_id: "2b2124a5-43a9-4c75-a9ad-11e89dc9f106" -->
## Integration Checklist

When integrating a framework into the hierarchy, ensure:

- [ ] **Handoff Compatibility**: Can it read/write JSON handoffs per the canonical schema?
- [ ] **Context Loading**: Can it load cascading CLAUDE.md/AGENTS.md/GEMINI.md files?
- [ ] **Tool Integration**: Can it call external CLIs (codex, gemini, claude-code)?
- [ ] **State Persistence**: Does it preserve handoff state across runs?
- [ ] **Error Handling**: Can it report failures in handoff format?
- [ ] **Parallel Execution**: Does it support concurrent worker spawning?
- [ ] **Observability**: Can you inspect agent interactions and decisions?

---

<!-- section_id: "16f0288f-5e94-4de5-a3d0-a2f963a9cc03" -->
## Minimal Integration Examples

<!-- section_id: "53fcb8fa-2ec6-463c-8b60-ffb4efe0dddf" -->
### LangGraph as L1 Manager

```python
from langgraph.graph import StateGraph
from typing import TypedDict
import json

class L1ManagerState(TypedDict):
    handoff: dict  # Incoming handoff from L0
    subtasks: list[dict]  # Decomposed tasks for L2
    results: list[dict]  # Aggregated results from L2
    status: str

def read_handoff(state: L1ManagerState):
    # Read incoming.json from L1 handoff directory
    with open("layer_1_project/1.01_manager_handoff_documents/1.00_to_universal/incoming.json") as f:
        state["handoff"] = json.load(f)
    return state

def decompose_tasks(state: L1ManagerState):
    # Use LLM to decompose into L2 feature subtasks
    # Load layer context from CLAUDE.md
    state["subtasks"] = llm_decompose(state["handoff"])
    return state

def spawn_l2_workers(state: L1ManagerState):
    # Launch L2 feature managers (via CLI or framework)
    results = []
    for task in state["subtasks"]:
        result = spawn_l2_manager(task)  # CLI call to claude-code or codex
        results.append(result)
    state["results"] = results
    state["status"] = "completed"
    return state

# Build graph
workflow = StateGraph(L1ManagerState)
workflow.add_node("read", read_handoff)
workflow.add_node("decompose", decompose_tasks)
workflow.add_node("spawn", spawn_l2_workers)
workflow.add_edge("read", "decompose")
workflow.add_edge("decompose", "spawn")
workflow.set_entry_point("read")

# Execute
result = workflow.invoke({})
```

<!-- section_id: "4ded0c69-ee89-416b-8cc9-a8f505564c23" -->
### CrewAI as L2 Feature Manager

```python
from crewai import Agent, Task, Crew
import json

# Load incoming handoff
with open("layer_2_auth/2.01_manager_handoff_documents/incoming.json") as f:
    handoff = json.load(f)

# Define role-based agents
ui_designer = Agent(
    role="UI/UX Designer",
    goal="Design authentication UI components",
    backstory="Expert in user experience and interface design",
    tools=[read_file, web_search]
)

backend_dev = Agent(
    role="Backend Developer",
    goal="Implement authentication backend logic",
    backstory="Full-stack developer with security expertise",
    tools=[codex_cli, read_file, write_file]
)

qa_engineer = Agent(
    role="QA Engineer",
    goal="Test authentication flows and security",
    backstory="Security-focused QA specialist",
    tools=[run_tests, codex_cli]
)

# Define tasks from handoff
design_task = Task(
    description=f"{handoff['task']} - Design UI components",
    agent=ui_designer
)

implement_task = Task(
    description=f"{handoff['task']} - Implement backend",
    agent=backend_dev,
    context=[design_task]  # Depends on design
)

test_task = Task(
    description=f"{handoff['task']} - Test and verify",
    agent=qa_engineer,
    context=[implement_task]
)

# Execute crew
crew = Crew(
    agents=[ui_designer, backend_dev, qa_engineer],
    tasks=[design_task, implement_task, test_task],
    process="sequential"
)

result = crew.kickoff()

# Write outgoing handoff
outgoing = {
    "schemaVersion": "1.0.0",
    "id": handoff["id"] + "-result",
    "status": "completed",
    "results": result,
    "artifacts": {"design": "...", "code": "...", "tests": "..."}
}

with open("layer_2_auth/2.01_manager_handoff_documents/outgoing.json", "w") as f:
    json.dump(outgoing, f, indent=2)
```

---

<!-- section_id: "c3725d9b-1f3c-4c77-9fbe-9f868e12d1a9" -->
## Hybrid Patterns

Frameworks can be mixed within the hierarchy:

**Pattern 1: LangGraph Supervisor + CrewAI Features**
- L0: LangGraph supervisor managing overall workflow
- L1: LangGraph project managers
- L2: CrewAI "teams" for each feature
- L3: Direct CLI calls (codex, claude-code) as workers

**Pattern 2: AutoGen Planning + LangGraph Execution**
- Request/Instructions: AutoGen for dialogue
- Planning: AutoGen for collaborative planning
- Implementation onward: LangGraph for deterministic execution

**Pattern 3: Framework-Free Supervisor + Framework Workers**
- Supervisor: Simple Python/shell scripts watching handoffs
- L1/L2 Managers: Framework-based (LangGraph, CrewAI, etc.)
- L3/L4 Workers: Direct CLI tools (codex, gemini, claude-code)

---

<!-- section_id: "f0f8644c-22d8-4722-9c91-b582d208dab1" -->
## When to Skip Frameworks

You may not need a framework at all if:
- Work is straightforward and decomposable
- Simple shell scripts or Python can coordinate CLI calls
- You want minimal dependencies
- Handoff protocol is sufficient for coordination

**Example**: L2 feature manager that:
1. Reads incoming handoff
2. Decomposes into 3 component tasks
3. Spawns 3 Codex workers via `subprocess.run(["codex", ...])`
4. Waits for all to complete
5. Aggregates outgoing handoffs
6. Writes L2 outgoing handoff

No framework needed - just handoffs and CLI calls.

---

<!-- section_id: "393a36c3-c570-4ee5-8f5f-b04454f93764" -->
## Migration Path

If starting from scratch or migrating existing workflows:

**Phase 1: Manual CLI Orchestration** (Week 1-2)
- Use shell scripts to chain claude-code, codex, gemini
- Handoffs as simple JSON files
- Manual supervision

**Phase 2: Prototype with AutoGen/CrewAI** (Week 3-4)
- Implement L1/L2 managers with AutoGen or CrewAI
- Keep L3 workers as direct CLI calls
- Test multi-agent patterns

**Phase 3: Formalize with LangGraph** (Week 5-8)
- Convert successful patterns to LangGraph for production
- Add checkpointing, error recovery, monitoring
- Scale to more layers and parallel workers

**Phase 4: Hybrid Optimization** (Ongoing)
- Use frameworks where they excel
- Direct CLI calls for simple workers
- Continuous improvement based on metrics

---

<!-- section_id: "6331a9ba-27f6-4463-827c-44dedd59f907" -->
## Related Documentation

**Within 0_ai_context**:
- **AI Framework Docs**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/`
  - `framework-comparison.md` - Comparison of Spec Kit, BMAD Method, and other frameworks
  - `integration-guide.md` - Integration with existing tools
  - `tool-selection-guide.md` - Decision framework for tool selection
- **CLI Recursion**: `sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
- **Handoff Schema**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Normative Specification**:
- **Framework Orchestration (Detailed)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`
- **Architecture**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Supervisor Patterns**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

---

<!-- section_id: "baadf910-ca7c-4b15-ab6f-eca7af054856" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.
