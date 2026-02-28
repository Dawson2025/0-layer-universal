## Framework Orchestration Guide

This document provides detailed guidance on using multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) within the AI manager hierarchy system.

It builds on the generic architecture described in:
- `summary/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`
- `architecture.md`
- `tools_and_context_systems.md`

---

## 1. Overview: Frameworks as Orchestrators

Multi-agent frameworks can serve multiple roles in the hierarchy:

- **Supervisors**: Top-level orchestrators managing the entire workflow
- **Layer Managers**: Coordinating work within specific layers (L1/L2)
- **Specialized Workers**: Teams of agents handling complex, multi-step tasks

The key requirement: frameworks must respect the **Tool Interface** and **Handoff Protocol**.

---

## 2. Framework Comparison Matrix

### 2.1 LangGraph

**Strengths:**
- Explicit state machine control with graph-based workflows
- Excellent for deterministic, auditable agent flows
- Strong tool integration via LangChain ecosystem
- Checkpointing and human-in-the-loop support

**Best Suited For:**
- L0–L2 managers requiring explicit control flow
- Supervisors managing complex DAGs of tasks
- Workflows with conditional branching and cycles (e.g., plan → implement → test → fix loop)

**Integration Pattern:**
```python
# LangGraph as L1 Manager
from langgraph.graph import StateGraph

class L1ManagerState(TypedDict):
    handoff: dict  # Incoming handoff from L0
    subtasks: list[dict]  # Decomposed tasks for L2
    results: list[dict]  # Aggregated results from L2
    status: str

def read_handoff(state: L1ManagerState):
    # Read incoming.json from filesystem
    state["handoff"] = json.load(open("incoming.json"))
    return state

def decompose_tasks(state: L1ManagerState):
    # Use LLM to decompose into L2 subtasks
    state["subtasks"] = llm.decompose(state["handoff"])
    return state

def spawn_l2_workers(state: L1ManagerState):
    # Launch L2 agents (Claude, Codex, etc.)
    results = []
    for task in state["subtasks"]:
        result = spawn_agent(layer=2, task=task)
        results.append(result)
    state["results"] = results
    return state

# Build graph
workflow = StateGraph(L1ManagerState)
workflow.add_node("read", read_handoff)
workflow.add_node("decompose", decompose_tasks)
workflow.add_node("spawn", spawn_l2_workers)
workflow.add_edge("read", "decompose")
workflow.add_edge("decompose", "spawn")
```

**When to Use:**
- Need explicit control over agent interaction patterns
- Require checkpointing/resumability
- Want to visualize and audit workflow execution

### 2.2 AutoGen

**Strengths:**
- Conversational multi-agent patterns
- Easy to prototype agent interactions
- Built-in support for code execution and tool use
- Good for exploratory, dialogue-heavy workflows

**Best Suited For:**
- L1/L2 request and instructions stages (dialogue-heavy)
- Rapid prototyping of new agent patterns
- Workflows where agents need to negotiate and debate solutions

**Integration Pattern:**
```python
# AutoGen as Request/Instructions Stage
from autogen import AssistantAgent, UserProxyAgent, GroupChat

# Define agents
project_manager = AssistantAgent(
    name="ProjectManager",
    system_message=load_context("L1", "CLAUDE.md"),
    llm_config={"model": "claude-sonnet-4.5"}
)

requirements_analyst = AssistantAgent(
    name="RequirementsAnalyst",
    system_message=load_context("L1/instructions", "CLAUDE.md"),
    llm_config={"model": "claude-sonnet-4.5"}
)

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    code_execution_config=False
)

# Group chat for clarification
groupchat = GroupChat(
    agents=[project_manager, requirements_analyst, user_proxy],
    messages=[],
    max_round=20
)

# Run conversation, then extract handoff
manager.run(groupchat)
handoff = extract_handoff_from_chat(groupchat.messages)
write_handoff("outgoing.json", handoff)
```

**When to Use:**
- Stages requiring multi-turn dialogue (request, instructions, planning)
- Prototyping new multi-agent patterns before formalizing
- Need flexible agent-to-agent communication

### 2.3 CrewAI

**Strengths:**
- Role-based agent abstractions (natural "team" metaphor)
- Task assignment and delegation patterns
- Good documentation and examples
- Sequential and parallel task execution

**Best Suited For:**
- L2 feature managers with clear role separation
- Workflows mimicking human team structures (designer, developer, tester)
- Parallel execution of independent subtasks

**Integration Pattern:**
```python
# CrewAI as L2 Feature Manager
from crewai import Agent, Task, Crew

# Define agents with roles
designer = Agent(
    role="UI/UX Designer",
    goal="Design user interfaces and flows",
    backstory="Expert in user experience and interface design",
    tools=[read_file, web_search]
)

developer = Agent(
    role="Software Developer",
    goal="Implement features according to design specs",
    backstory="Full-stack developer with expertise in TypeScript",
    tools=[codex_cli, read_file, write_file]
)

tester = Agent(
    role="QA Engineer",
    goal="Ensure code quality and test coverage",
    backstory="Quality assurance specialist",
    tools=[run_tests, codex_cli]
)

# Define tasks from handoff
handoff = read_handoff("incoming.json")
design_task = Task(
    description=handoff["task"] + " - Design phase",
    agent=designer
)

implement_task = Task(
    description=handoff["task"] + " - Implementation",
    agent=developer,
    context=[design_task]  # Depends on design
)

test_task = Task(
    description=handoff["task"] + " - Testing",
    agent=tester,
    context=[implement_task]
)

# Execute crew
crew = Crew(
    agents=[designer, developer, tester],
    tasks=[design_task, implement_task, test_task],
    process="sequential"  # or "parallel" for independent tasks
)

result = crew.kickoff()
write_handoff("outgoing.json", result)
```

**When to Use:**
- L2/L3 feature/component work with clear role separation
- Need intuitive "team" abstraction
- Want built-in task sequencing and dependencies

### 2.4 MetaGPT

**Strengths:**
- Prescriptive "software team in a box" with defined roles (PM, architect, engineer)
- Structured document outputs (PRDs, design docs, code)
- Good for end-to-end feature development
- Opinionated but comprehensive

**Best Suited For:**
- L1/L2 managers for greenfield feature development
- Projects where standardized software engineering artifacts are desired
- Teams wanting a "batteries-included" approach

**Integration Pattern:**
```python
# MetaGPT as L1 Project Manager
from metagpt.roles import ProductManager, Architect, Engineer
from metagpt.team import Team

# Define team
team = Team()
team.hire([
    ProductManager(),
    Architect(),
    Engineer()
])

# Load handoff and run team
handoff = read_handoff("incoming.json")
team.run_project(handoff["task"])

# Extract artifacts and create outgoing handoff
outgoing = {
    "schemaVersion": "1.0.0",
    "status": "completed",
    "artifacts": {
        "prd": team.get_artifact("prd.md"),
        "architecture": team.get_artifact("architecture.md"),
        "code": team.get_artifact("src/")
    },
    "results": "Feature implemented according to PRD"
}
write_handoff("outgoing.json", outgoing)
```

**When to Use:**
- Prefer opinionated, structured workflows
- Want standardized documentation outputs
- Building greenfield features from scratch

---

## 3. Framework Selection Decision Tree

```
┌─ Need explicit state control & auditability?
│  └─> YES → LangGraph
│
├─ Need dialogue-heavy exploration/negotiation?
│  └─> YES → AutoGen
│
├─ Want natural "team" abstraction with roles?
│  └─> YES → CrewAI
│
└─ Want comprehensive "software team in a box"?
   └─> YES → MetaGPT
```

**General Recommendation:**
1. **Start with AutoGen or CrewAI** for prototyping
   - Quick to set up
   - Flexible patterns
   - Good for exploring agent interactions

2. **Move to LangGraph** when you need:
   - Production-grade control
   - Complex conditional logic
   - Explicit state management
   - Auditability and debugging

3. **Use MetaGPT** when:
   - You want standardized outputs
   - Building greenfield projects
   - Prefer opinionated structure over flexibility

---

## 4. Hybrid Patterns

Frameworks can be mixed within the hierarchy:

**Example 1: LangGraph Supervisor + CrewAI Features**
- L0: LangGraph supervisor managing overall workflow
- L1: LangGraph project managers
- L2: CrewAI "teams" for each feature
- L3: Direct CLI calls (Claude, Codex) as workers

**Example 2: AutoGen Planning + LangGraph Execution**
- Request/Instructions: AutoGen for dialogue
- Planning: AutoGen for collaborative planning
- Implementation onward: LangGraph for deterministic execution

**Example 3: Framework-Free Supervisor + Framework Workers**
- Supervisor: Simple Python/shell scripts watching handoffs
- L1/L2 Managers: Framework-based (any of the above)
- L3/L4 Workers: Direct CLI tools (Codex, Claude, Gemini)

---

## 5. Integration Checklist

When integrating a framework into the hierarchy:

- [ ] **Handoff Compatibility**: Can it read/write JSON handoffs?
- [ ] **Context Loading**: Can it load cascading CLAUDE.md/AGENTS.md/etc.?
- [ ] **Tool Integration**: Can it call external CLIs (codex, gemini, etc.)?
- [ ] **State Persistence**: Does it preserve handoff state across runs?
- [ ] **Error Handling**: Can it report failures in handoff format?
- [ ] **Parallel Execution**: Does it support concurrent worker spawning?
- [ ] **Observability**: Can you inspect agent interactions and decisions?

---

## 6. Migration Path

If starting from scratch or migrating:

**Phase 1: Manual CLI Orchestration** (Week 1-2)
- Use shell scripts to chain claude-code, codex, gemini
- Handoffs as simple JSON files
- Manual supervision

**Phase 2: AutoGen/CrewAI Prototyping** (Week 3-4)
- Implement L1/L2 managers with AutoGen or CrewAI
- Keep L3 workers as direct CLI calls
- Test multi-agent patterns

**Phase 3: LangGraph Formalization** (Week 5-8)
- Convert successful patterns to LangGraph for production
- Add checkpointing, error recovery, monitoring
- Scale to more layers and parallel workers

**Phase 4: Hybrid Optimization** (Ongoing)
- Use frameworks where they excel
- Direct CLI calls for simple workers
- Continuous improvement based on metrics

---

## 7. Common Pitfalls

### 7.1 Over-Engineering Early
**Problem:** Starting with complex LangGraph workflows before understanding patterns
**Solution:** Prototype with AutoGen/CrewAI first, formalize later

### 7.2 Framework Lock-In
**Problem:** Tightly coupling architecture to framework-specific APIs
**Solution:** Always maintain handoff protocol as abstraction boundary

### 7.3 Ignoring Context Cascading
**Problem:** Frameworks not loading layer-specific CLAUDE.md/AGENTS.md
**Solution:** Build context loaders that merge layer context before agent initialization

### 7.4 Missing Error Boundaries
**Problem:** Framework failures don't produce valid handoffs
**Solution:** Wrap framework calls in error handlers that write failure handoffs

---

## 8. Summary

Multi-agent frameworks are **powerful orchestrators** within the hierarchy, but they are:

- **Optional**: The architecture works without them
- **Composable**: Mix and match based on layer/stage needs
- **Abstracted**: Hidden behind handoff protocol for flexibility

Choose frameworks based on:
- Stage characteristics (dialogue vs deterministic)
- Team familiarity and preferences
- Production requirements (auditability, error handling)
- Cost/complexity tradeoffs

The handoff protocol ensures you can swap frameworks without rewriting the entire system.
