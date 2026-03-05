---
resource_id: "5d5abf6d-a765-47c9-a88f-86321401b1a6"
resource_type: "document"
resource_name: "framework_orchestration_overview"
---
# Framework Orchestration Overview

<!-- section_id: "5abbbaf3-32b5-4500-9344-ba5872dde9e0" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "5d3cecad-a3ec-4d84-b8ec-ebf39a8a6c56" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "85b33885-7307-4c3c-81c8-7e593eaf724b" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "5eacf6c9-b031-45b1-ae38-17e5b60ba3cf" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "8f43316f-9b63-498d-9d4a-a8376d45fab1" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "6acaf207-2112-4024-a727-11449eacd48a" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "ee1e9d48-9aee-4be2-8316-9e3ffb6859d7" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "4f2b5bb8-159d-4212-a6da-ae4a139cc383" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "b8509972-a8ce-4d26-abd2-d4dabfbc30b8" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "a0bd2cf9-890a-4f99-be3a-1e8b60c44d4f" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "5704fe81-d5eb-4828-9a12-8b72b4a80a66" -->
## Framework Summary

<!-- section_id: "48fdca77-f014-475f-94fb-953f87c59eb6" -->
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

<!-- section_id: "ede14c63-3e34-495f-ab95-11499092c8d9" -->
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

<!-- section_id: "ed3f2e37-a93c-4e77-9391-521f3757c7c3" -->
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

<!-- section_id: "75ef73d5-1736-4edf-9932-6cba7f10f967" -->
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

<!-- section_id: "917908d3-2613-4948-a64a-5e9fb97fcf5b" -->
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

<!-- section_id: "e263db09-1ffd-42a2-bb14-7d3a74bb5d66" -->
## Minimal Integration Examples

<!-- section_id: "ef2ec7f5-e669-4593-8c3d-278a863a376a" -->
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

<!-- section_id: "34a1ef95-2ec3-4842-a0fa-055cf864c56a" -->
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

<!-- section_id: "b4318218-023a-496f-b380-8b99b758169d" -->
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

<!-- section_id: "ba905f26-f334-4ad7-a66d-060a1444b719" -->
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

<!-- section_id: "b54eef68-9de0-4cdc-a581-f1d48acfa794" -->
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

<!-- section_id: "4dda6282-87c6-4482-8706-13413a3a6ea1" -->
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

<!-- section_id: "82e78dd9-d936-4590-92da-6c38354e392a" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.

---

<!-- section_id: "8efd60b2-8a62-40c0-b957-01b53b05e167" -->
## Legacy Universal Protocols Source

# Framework Orchestration Overview

<!-- section_id: "7872ea26-8d8c-4229-a6f5-2168f8d53dc6" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "bf1e3c96-db73-4e0e-88a9-4db5fd317c04" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "76e41ac0-a1e8-4232-8cf6-de4d3c307166" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "c1e3ed25-ef3d-48fe-8f71-6bb5ed633997" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "d99d8c78-8f0d-449b-82ea-6a97aa341aa3" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "00491f0b-f07d-4e23-b149-6c34e2d84f26" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "c0431e89-3af5-428f-b19b-4a90c915fba2" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "269d43e4-3eac-4bdb-b05f-ac380e1d09b1" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "4a487447-6203-4e7a-a90c-cbcd087c3589" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "cf3557ef-af8f-425e-9806-db5d46bae634" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "ccc2bc7f-cb0b-4131-b1ad-85d3cb37ba1f" -->
## Framework Summary

<!-- section_id: "46d7c09f-26b8-42ba-85eb-c02eef5eb305" -->
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

<!-- section_id: "2663452b-fb4f-4687-a591-6c956782619f" -->
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

<!-- section_id: "e57f9a44-ecb5-4493-b1fb-28a48a5201f3" -->
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

<!-- section_id: "3cbab04f-a964-4b14-b944-effaa5f530ae" -->
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

<!-- section_id: "d7d128de-6431-476e-b01f-74846288a518" -->
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

<!-- section_id: "a2c2613e-ce98-433b-a2c9-a8078069cd52" -->
## Minimal Integration Examples

<!-- section_id: "5ec76cfb-80fc-4bf7-8562-cb2fc8bf2ca0" -->
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

<!-- section_id: "40a84e87-ff36-4d30-bb18-3a6b457c72fb" -->
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

<!-- section_id: "bc7abea8-270b-4247-942c-5c922fa854e3" -->
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

<!-- section_id: "21684573-9005-4fc1-b1f2-6ef15a44cb13" -->
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

<!-- section_id: "0d9e0f09-60a7-438f-90aa-dcddfd9163b5" -->
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

<!-- section_id: "95e24c26-90ad-49d3-a268-db38c0fed4ad" -->
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

<!-- section_id: "c5f322aa-f5d1-4a22-80c6-0d8538336851" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.


---

<!-- section_id: "4fbee334-3c5d-47eb-a086-6caaced62741" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`

# Framework Orchestration Overview

<!-- section_id: "ce47e7c0-59ef-4a05-8051-4c1374ff6a78" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "638739ba-e9e3-4e58-b7ce-dfd5b84e021b" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "c7d5c60e-443e-46fd-bf2a-6f7ef110386a" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "fa66cc43-2de7-4a53-9242-94ca1204a76d" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "538e8c24-1a6d-45dc-b5f7-4685120d9845" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "12df9447-f5fe-4f16-aeda-8334f646751c" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "a4b9bbd0-a145-4a5e-8ede-82b22808ec2c" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "4554d421-8133-4953-9e5e-30bdf84d7856" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "054d1f89-9a86-4c7a-b156-8c5930a93e50" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "982ae777-53c1-4505-ad98-2127e2a597ac" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "1dfae37f-d58f-4486-a559-1fb8033948f5" -->
## Framework Summary

<!-- section_id: "b2e1d356-4618-4ea2-acd8-41ec46e3f295" -->
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

<!-- section_id: "902acee6-bafd-4c09-a1b8-d029bcce1614" -->
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

<!-- section_id: "20fc0984-5e7b-4a7b-90a4-84d02b43c69f" -->
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

<!-- section_id: "49818dc4-5cf1-4918-954f-169b93ec9a99" -->
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

<!-- section_id: "10d2fefb-b0bd-47e6-be9f-b308ba87e66e" -->
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

<!-- section_id: "aa188405-15a2-4726-87eb-4af0aa17ef15" -->
## Minimal Integration Examples

<!-- section_id: "36c8e794-86f6-406e-91eb-8124cd595d2b" -->
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

<!-- section_id: "e4b7e444-0285-4761-a3a8-5a01ed86b44a" -->
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

<!-- section_id: "6f16d44e-1e90-4b90-9897-8df12f747127" -->
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

<!-- section_id: "f50114df-1c3a-4f18-b338-2a68d940fa48" -->
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

<!-- section_id: "1a590258-c9e7-4b9e-89c3-c7cbc525dac8" -->
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

<!-- section_id: "ede523a3-7652-44b8-8ac3-48a8563772be" -->
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

<!-- section_id: "b2d99902-99c4-4b63-8003-a3c088c137bf" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.
