---
resource_id: "a3bf84b9-f99d-4639-a0c1-dae2c4943029"
resource_type: "document"
resource_name: "framework_orchestration_overview"
---
# Framework Orchestration Overview

<!-- section_id: "e03ea0e5-7ea9-41ad-a94a-9aeb18e43574" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "d7970a1d-08c0-4f99-b59a-441d5c0b9ede" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "8490be0a-d507-4a72-a127-3260383700ec" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "86448e9c-6d93-4c4c-917b-b2a1e63fc5f9" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "177f7a1b-97b4-42d4-b2c1-12a84f7906e8" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "24095e8e-426e-4b38-9621-65bc9915c6a3" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "06097c43-315e-44c1-b91a-73f07c0c7660" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "d90e5d2b-a438-456a-b8b0-12bc61a2bbf8" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "6fdd74fd-5f9e-4c58-bcbb-a3f80f2be117" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "45be8d50-19e8-4c48-ba05-9bf21abc045d" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "3983fd96-cb42-4384-a843-14ec88eaf532" -->
## Framework Summary

<!-- section_id: "72287f89-067c-4ef8-b9ba-b06ccbe3f31d" -->
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

<!-- section_id: "1572b249-33ce-41df-ad6a-6d0ccc74976b" -->
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

<!-- section_id: "383ecbe1-b711-40e9-b9ad-b6afef309182" -->
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

<!-- section_id: "71507925-9a08-417d-84a5-fe1674a0a636" -->
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

<!-- section_id: "d71479ad-d4a5-4593-979a-fed0eb4ddc7f" -->
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

<!-- section_id: "30e42a93-664f-4493-b797-64c782ddb679" -->
## Minimal Integration Examples

<!-- section_id: "d98d767b-175b-450b-b38e-a59c45fb69ec" -->
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

<!-- section_id: "42712f13-15e0-4dd8-b7ab-3d93e377eace" -->
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

<!-- section_id: "69a2fc07-5709-4cc3-89c2-655bccd2f77f" -->
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

<!-- section_id: "8e7515ae-ab45-43c1-bebe-56eac6a0f5e9" -->
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

<!-- section_id: "2b081ae3-b042-47ca-a8b5-bd65b7624e1b" -->
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

<!-- section_id: "d023dbf2-c0ff-487e-a74f-66124048b444" -->
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

<!-- section_id: "32ad096d-f857-4f64-976d-48c59a844c1a" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.

---

<!-- section_id: "146f01b9-d7fb-46d9-8e4c-a5707cdd56e8" -->
## Legacy Universal Protocols Source

# Framework Orchestration Overview

<!-- section_id: "7a0fb203-f83d-4b56-a6cf-8c7014c060c0" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "0db6c959-f06c-48d5-8591-1fd4e657e987" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "8b8ab7b8-bb94-4cbf-9439-a51a0ad327a9" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "f0b11c4f-5b7a-42c4-b311-0985d9d4fe92" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "48859554-ca63-49b7-914e-d200eafe1cf3" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "8d8580e5-1832-4156-9908-8480fb684970" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "355fbc55-ebb6-4189-8587-66c7afae59b3" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "f7570723-119b-4df4-92b6-c2a7948b2658" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "00fe13ea-c47e-4709-94fc-542d4e3fc655" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "87bf06be-d642-4e6b-8e33-d4269619ff34" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "034505cc-e6da-4a70-bed3-5aef0243b0bc" -->
## Framework Summary

<!-- section_id: "2a0de26b-0f18-472b-9520-a71dfaba59f2" -->
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

<!-- section_id: "4554f635-85be-4382-bd9a-c1f82e65ae81" -->
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

<!-- section_id: "e091e8e8-2ab8-4ff1-9f34-f441791f9e19" -->
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

<!-- section_id: "807991ce-1d85-498a-930b-b82c0575287e" -->
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

<!-- section_id: "c25a060e-85ba-418d-9619-15932c7e9613" -->
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

<!-- section_id: "84244047-e8c7-449b-a7ed-8dc55c2bc76d" -->
## Minimal Integration Examples

<!-- section_id: "d22d6153-4e31-4919-99e7-c8c77d6e40c3" -->
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

<!-- section_id: "84b14435-5908-4d47-84e2-2a3bc436acbe" -->
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

<!-- section_id: "bb0a5866-011e-4d0d-ae3f-b4aeebc4822b" -->
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

<!-- section_id: "8fd27b3f-14db-424c-b80d-63371e8eb93a" -->
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

<!-- section_id: "eb0f1742-da30-49b8-84f9-96f127c106d0" -->
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

<!-- section_id: "628a7323-c1aa-4c2b-afd6-6b30e076cc45" -->
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

<!-- section_id: "23bd6505-19d6-45ff-9399-49d1723378f6" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.


---

<!-- section_id: "b4db6764-b8b2-4b9e-a3fb-03060432fac9" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`

# Framework Orchestration Overview

<!-- section_id: "f20b25c4-66f9-41f7-a0b0-696d0513582d" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "e6265dcf-e497-4846-bbc1-32fff77b71e9" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "c219b2d0-061a-4748-ab40-62a2063b3032" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "666fe6a8-a3c8-41f5-9544-99e152e7f9e7" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "7647c1e4-7d1b-40a8-9ab0-9bd742acfb4a" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "e8e76f26-4d9e-4632-bb68-593fb6534042" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "e54c0dcd-9cd2-4452-8764-41a4f219a4ef" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "6bf945ef-b2b4-45c2-9e14-461f37e99901" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "41e177f7-2f62-438b-81a1-bb5deea30ec8" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "9ff70cd7-2a40-4fd9-9478-6510007eff30" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "15857c22-5830-4803-a887-0f14b4966938" -->
## Framework Summary

<!-- section_id: "e837e6ac-a3c3-49b6-baa4-b224a28fb308" -->
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

<!-- section_id: "dae85812-1118-4c2e-b77b-faacaca2dfbc" -->
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

<!-- section_id: "405a6b01-0f3b-4169-b6eb-746a562f84dd" -->
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

<!-- section_id: "7957bcfa-7f0e-4a0e-8f53-f44744bfcd0b" -->
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

<!-- section_id: "4d81f9e0-7866-45f1-a4d8-5e85e2ecbc84" -->
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

<!-- section_id: "e5c2e8ae-5e50-401f-b8b8-5d6cbc7eb4dc" -->
## Minimal Integration Examples

<!-- section_id: "02f8021b-eb89-4fb6-bafe-f1806a697bf6" -->
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

<!-- section_id: "bda9a682-3507-4c5e-8da7-1f7944cd5ecb" -->
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

<!-- section_id: "608ca6f2-fe31-47d3-8abd-0730b588ca3d" -->
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

<!-- section_id: "2a0afec4-2fa0-44b1-820f-067d96f70872" -->
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

<!-- section_id: "1dadff3c-18ed-4c38-8b6b-502d08f43025" -->
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

<!-- section_id: "e46377c6-64b2-4742-8a1a-ca5d76fcca5e" -->
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

<!-- section_id: "95d9803f-bd6f-4d14-9f54-0180dcbda6d3" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.
