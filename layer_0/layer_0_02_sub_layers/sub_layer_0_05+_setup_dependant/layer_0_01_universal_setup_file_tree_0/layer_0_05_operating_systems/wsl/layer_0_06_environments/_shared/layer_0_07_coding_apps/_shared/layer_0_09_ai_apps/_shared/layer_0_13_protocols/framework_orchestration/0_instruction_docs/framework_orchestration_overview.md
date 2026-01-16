# Framework Orchestration Overview

## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

## When to Use Framework Orchestration vs. Simple Handoffs

### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

## Framework Summary

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

## Minimal Integration Examples

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

## Related Documentation

**Within 0_ai_context**:
- **AI Framework Docs**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/`
  - `framework-comparison.md` - Comparison of Spec Kit, BMAD Method, and other frameworks
  - `integration-guide.md` - Integration with existing tools
  - `tool-selection-guide.md` - Decision framework for tool selection
- **CLI Recursion**: `sub_layer_0.13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
- **Handoff Schema**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Normative Specification**:
- **Framework Orchestration (Detailed)**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`
- **Architecture**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Supervisor Patterns**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

---

## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.

---

## Legacy Universal Protocols Source

# Framework Orchestration Overview

## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

## When to Use Framework Orchestration vs. Simple Handoffs

### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

## Framework Summary

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

## Minimal Integration Examples

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

## Related Documentation

**Within 0_ai_context**:
- **AI Framework Docs**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/`
  - `framework-comparison.md` - Comparison of Spec Kit, BMAD Method, and other frameworks
  - `integration-guide.md` - Integration with existing tools
  - `tool-selection-guide.md` - Decision framework for tool selection
- **CLI Recursion**: `sub_layer_0.13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
- **Handoff Schema**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Normative Specification**:
- **Framework Orchestration (Detailed)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`
- **Architecture**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Supervisor Patterns**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

---

## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.


---

## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0.13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`

# Framework Orchestration Overview

## Applicability
**When to use:** When integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) into the AI Manager Hierarchy System.
**Where to use:** L0-L2 managers, supervisors, and complex stage orchestration where framework-based coordination provides value over simple handoff-based coordination.
**Scope:** OS: universal; Tools: universal (applies to any framework that can read/write handoff files and spawn CLI tools).

---

## Overview

This document provides guidance on integrating multi-agent orchestration frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. It explains when to use framework-based orchestration versus simple handoff-based coordination, and how to maintain compatibility with the hierarchy's handoff protocol.

For detailed integration patterns, examples, and framework-specific guidance, see the normative specification:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`

---

## When to Use Framework Orchestration vs. Simple Handoffs

### Use Simple Handoff-Based Coordination When:
- Work is clearly decomposable into independent tasks
- Manager-worker relationships are straightforward (single manager, multiple workers)
- Sequential stage execution is sufficient
- You want minimal dependencies and maximum simplicity
- L3/L4 component-level work with well-defined boundaries

**Example**: L3 component implementation where a manager decomposes a feature into 5 independent components, spawns Codex workers for each via CLI, waits for completion, and aggregates results.

### Use Framework Orchestration When:
- Complex conditional logic or branching workflows (e.g., plan → implement → test → fix loop)
- Need explicit state management and checkpointing
- Dialogue-heavy stages requiring multi-turn agent negotiation
- Want declarative workflow visualization and debugging
- L0-L2 managers requiring sophisticated coordination patterns

**Example**: L1 project manager using LangGraph to orchestrate a plan → design → implement → test → criticize → fix cycle with conditional retry logic and explicit state transitions.

---

## Framework Roles in the Hierarchy

Frameworks can serve multiple roles:

### 1. Supervisors (L0)
Top-level orchestrators managing the entire workflow across layers.
- **Recommended**: LangGraph (for deterministic control) or custom Python/shell scripts
- **Role**: Watch handoff directories, apply tool policies, spawn layer managers, aggregate results

### 2. Layer Managers (L1/L2)
Coordinating work within specific layers.
- **L1 Project Managers**: LangGraph (complex workflows), AutoGen (dialogue-heavy), or MetaGPT (opinionated structure)
- **L2 Feature Managers**: CrewAI (natural team abstraction) or LangGraph (control-heavy)

### 3. Specialized Workers (L2/L3)
Teams of agents handling complex, multi-step tasks.
- **Recommended**: CrewAI (role-based teams) or AutoGen (exploratory dialogue)
- **Role**: Execute feature-level work that requires specialized agent collaboration

### 4. Simple Workers (L3/L4)
Leaf execution via direct CLI calls.
- **Recommended**: Direct CLI invocation (codex, claude-code, gemini)
- **No framework needed**: Handoff in → execute → handoff out

---

## Framework Summary

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

## Minimal Integration Examples

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

## Related Documentation

**Within 0_ai_context**:
- **AI Framework Docs**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/`
  - `framework-comparison.md` - Comparison of Spec Kit, BMAD Method, and other frameworks
  - `integration-guide.md` - Integration with existing tools
  - `tool-selection-guide.md` - Decision framework for tool selection
- **CLI Recursion**: `sub_layer_0.13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
- **Handoff Schema**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Normative Specification**:
- **Framework Orchestration (Detailed)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/framework_orchestration.md`
- **Architecture**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Supervisor Patterns**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

---

## Summary

**Key Takeaways**:
1. **Frameworks are optional** - The hierarchy works with simple CLI orchestration
2. **Frameworks are composable** - Mix and match based on layer/stage needs
3. **Handoff protocol is king** - Any framework must respect the handoff abstraction
4. **Choose based on complexity** - Simple tasks don't need frameworks; complex workflows benefit from them
5. **Start simple, add complexity** - Begin with CLI orchestration, add frameworks where needed

The handoff protocol ensures you can swap frameworks or remove them entirely without rewriting the system.
