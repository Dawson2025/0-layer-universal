---
resource_id: "19b3510c-4e9b-4fff-8ec3-3879b6c6b1a4"
resource_type: "document"
resource_name: "framework_orchestration_overview"
---
# Framework Orchestration Overview

<!-- section_id: "c74c21c5-3045-468f-907c-ea155369cc63" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "539e3291-ead4-4676-9bdd-89d759a5603f" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "379ee244-fe42-4b60-a0d4-966a3fb42f9b" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "eaf7c17e-1c0f-4f6b-ab86-1cc786b3c5b7" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "1af6cea0-9369-4292-a509-ff176984e218" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "71f2ca1e-8492-4c38-95d7-4d9b1ee50dc0" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "186fcdcc-e619-4f5b-8248-92a8bc6c5c25" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "1b83dc67-cf1f-4971-a76c-16fb0da61dd3" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "c6c427d0-e83f-402d-a635-5318c251d50d" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "09cbb88a-9425-4716-a80d-80190ed0de0b" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "a9536d41-97ed-45eb-a806-2263ddad2b15" -->
## Framework Summary

<!-- section_id: "ba73ae4c-6f47-4e27-95a1-955964927f38" -->
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

<!-- section_id: "e1692c08-060a-483c-8c95-d8bb1ceb01f5" -->
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

<!-- section_id: "b2e6e03f-6532-4e1e-aae6-2f19e57bde6f" -->
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

<!-- section_id: "76f6d29d-a323-4040-85fa-5ab1c766ed46" -->
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

<!-- section_id: "d09a4772-948b-42cb-ba7d-afbfe9f59c70" -->
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

<!-- section_id: "280b268f-0d77-4d51-8d8d-0101c125536f" -->
## Minimal Integration Examples

<!-- section_id: "2e408fbe-34ce-45ad-9fd6-e0be65a12b42" -->
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

<!-- section_id: "ab41c11f-f39b-4a7f-befa-22c8a2788c56" -->
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

<!-- section_id: "77de01fb-a675-451c-9075-129953b998bd" -->
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

<!-- section_id: "66ffc4a5-3215-432b-87e9-8d832f32e634" -->
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

<!-- section_id: "eb6ed0c4-ba43-423d-8038-8bf553bd487c" -->
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

<!-- section_id: "53454584-cce9-4330-8243-921ecf4bed4c" -->
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

<!-- section_id: "9e9e95a2-c11e-4166-95b0-706e1cd7e40b" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.

---

<!-- section_id: "09370881-b2d5-445d-87cb-8520baede022" -->
## Legacy Universal Protocols Source

# Framework Orchestration Overview

<!-- section_id: "c259f7c1-35cf-4490-88a3-7fc930429c75" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "8b55eb6f-5a9f-4cb0-8049-7e29113ceea4" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "f225b326-e1dc-46d9-9cac-61fbfac82b0b" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "0352ed5e-8aa8-495b-a0f1-cc845993a85f" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "893cb14b-dd77-4784-a325-3010b911ae0e" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "9707d161-11a7-4a9b-8a87-8aaaa51f8578" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "b76585f5-70d0-4570-8bcf-e1742bdd1fc2" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "ff1e5c52-8399-424f-b5be-9ef965b4692d" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "963159c4-4524-4a45-a51f-0ffc3d2451eb" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "49d5b38b-9fe4-4784-8e67-54ae81b33221" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "7dc9a377-426c-4f32-89a2-09dd4f4784c1" -->
## Framework Summary

<!-- section_id: "7add0802-9fff-4f23-a4df-b104cb3b5ead" -->
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

<!-- section_id: "e5839a27-a6a6-4fac-979c-bbb3bfe4a4e2" -->
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

<!-- section_id: "ae50820b-3bf9-4e1a-9be9-1b4fd2be5951" -->
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

<!-- section_id: "176de004-1eb8-482c-8b75-f6dc0bca32f9" -->
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

<!-- section_id: "a2049ede-0f7f-4b13-87f0-9d37bbe3b6ab" -->
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

<!-- section_id: "f02e0735-4446-41d0-8d28-515865e8e787" -->
## Minimal Integration Examples

<!-- section_id: "34e913ca-8a16-4092-9b41-554092943642" -->
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

<!-- section_id: "ffc80d4b-e559-4b7a-bdca-9ccabc138a03" -->
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

<!-- section_id: "1feca545-0c89-49ad-abc0-69c4e4aa0273" -->
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

<!-- section_id: "fdb01d69-b763-4413-b0ee-485d1934f957" -->
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

<!-- section_id: "553028e9-87ad-40c5-988c-5367704524b5" -->
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

<!-- section_id: "7f09106c-96a2-4173-9cb5-441ff02f8895" -->
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

<!-- section_id: "5f6c4369-e1d1-480a-9485-50f33fa8435d" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.


---

<!-- section_id: "fe7802b5-0025-47f0-8fa0-6a215a973081" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`

# Framework Orchestration Overview

<!-- section_id: "bdc14a1f-30a8-4517-b261-69f5ea83ccb6" -->
## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

<!-- section_id: "7e57bbf2-286d-4e6e-8dcd-8cc5be0a17db" -->
## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

<!-- section_id: "7c2f31a8-4414-40f2-92e3-4b1b137aaf3a" -->
## When to Use Framework Orchestration vs. Simple Handoffs

<!-- section_id: "13d77b2e-6bcd-4986-b84b-60c74079d7b2" -->
### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

<!-- section_id: "09321a9f-a9c3-447a-8846-6bd435db2874" -->
### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

<!-- section_id: "f7fecde9-9a63-423b-9a99-82a6ec8647be" -->
## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

<!-- section_id: "5917682e-8762-4e16-836a-f3d90dd465ad" -->
### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

<!-- section_id: "84a2fb24-b074-45c1-a63e-e2ec550e739a" -->
### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

<!-- section_id: "5448201f-45f5-45a9-9f22-7b1011d7f809" -->
### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

<!-- section_id: "9f7b4737-85a2-422b-9213-36b88175f777" -->
### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

<!-- section_id: "0e1d4ff7-e662-4469-b92e-405925cb457b" -->
## Framework Summary

<!-- section_id: "79a2f411-812b-4355-9afe-05e7470df8a0" -->
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

<!-- section_id: "ba1df510-03a8-4f1d-98e2-036d37d6df5c" -->
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

<!-- section_id: "ddf3fe1c-b349-4037-b8ad-c9dec413b238" -->
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

<!-- section_id: "54955d6f-4761-42c8-959e-e8001e78ab46" -->
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

<!-- section_id: "e5ce2bf5-7c04-41fa-996b-cef66122ad25" -->
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

<!-- section_id: "d96c4784-d111-46ad-b294-db80298d5079" -->
## Minimal Integration Examples

<!-- section_id: "d59af5b4-d3dd-48be-bc54-73e58205f4e9" -->
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

<!-- section_id: "e6eff320-e121-46a7-8cdb-3c62beab9675" -->
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

<!-- section_id: "b616dd3e-b03f-4562-b1ae-a7035a228321" -->
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

<!-- section_id: "16a9948b-d62c-4f30-b26a-2141f2fa5541" -->
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

<!-- section_id: "97602ae8-ddb7-4bae-adc5-4638254e93c7" -->
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

<!-- section_id: "1a7a1a89-9e06-45d4-ac84-ab1cfdcf90ce" -->
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

<!-- section_id: "93dc0848-dd48-42a0-a8cf-62f1b6767dee" -->
## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.
