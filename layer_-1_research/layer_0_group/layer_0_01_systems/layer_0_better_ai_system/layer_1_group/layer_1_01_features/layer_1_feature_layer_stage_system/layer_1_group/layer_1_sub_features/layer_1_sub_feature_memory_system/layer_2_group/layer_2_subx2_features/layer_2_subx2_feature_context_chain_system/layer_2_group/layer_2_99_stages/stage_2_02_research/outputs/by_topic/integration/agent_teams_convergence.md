---
resource_id: "bb07baf9-3746-4193-ae63-a8a74acc7db3"
resource_type: "output"
resource_name: "agent_teams_convergence"
---
# Agent Teams + Layer-Stage Convergence

## The Two Systems

### Claude Code Agent Teams

**What it provides**:
- Live multi-agent orchestration with a team lead and teammates
- User can enter any agent and interact with it directly
- Shared task lists for coordination
- Message passing between agents (DMs, broadcasts, shutdown requests)
- Team lead delegates, monitors, and aggregates work

**What it lacks**:
- Persistence — agents are terminated when the team is deleted
- Reusability — agent context is lost after the session
- Pre-configured roles — agents start fresh each time with no pre-built context
- Cross-session continuity — no hand-off mechanism between team sessions

### Layer-Stage System

**What it provides**:
- Persistent agent context at every layer (CLAUDE.md, orchestrator.jsonld, status.json)
- Pre-configured roles — each layer already has management instructions and context
- Hand-off documents for cross-session IPC
- Hierarchical delegation (parent ↔ child layers)
- Reusable context that survives indefinitely in the file system
- AALang agent definitions that formally specify behavior

**What it lacks**:
- Live interactivity — can't "enter" a running layer agent and talk to it
- Multi-agent concurrency — agents run sequentially, not in parallel teams
- Real-time task coordination — task lists are file-based, not live
- Dynamic team formation — structure is pre-defined, not created on-the-fly

---

## The Convergence Goal

Combine both systems so that:

1. **Agent Teams uses layer-stage context as its foundation**
   - When a team is created, each agent loads its layer's CLAUDE.md and orchestrator.jsonld
   - Agents start with pre-configured knowledge, not blank slates

2. **Layer-stage system persists Agent Teams' work**
   - When the team completes, results are written to hand-off documents
   - Status.json files are updated with progress
   - Next team session picks up where the previous one left off

3. **Users can interact with any layer agent live**
   - Agent Teams' interactivity model applied to layer agents
   - Enter module_03's agent and ask questions while module_01's agent works in parallel

4. **AALang orchestrators drive team coordination**
   - The layer_0_orchestrator.gab.jsonld defines the coordination pattern
   - Agent Teams uses this pattern instead of ad-hoc coordination
   - Safeguards (max recursion, circuit breaker) are enforced

---

## How It Could Work

### Team Creation from Layer Structure

```
User: "Create a team to work on the ML assignments"

System reads layer structure:
├── Layer 5: Assignments Manager (team lead)
├── Layer 6: Module 01 Manager (teammate)
├── Layer 6: Module 02 Manager (teammate)
└── Layer 6: Module 03 Manager (teammate)

Team is created with:
- Team lead → loads layer_4/CLAUDE.md + orchestrator
- Module 01 agent → loads module_01/CLAUDE.md + orchestrator
- Module 02 agent → loads module_02/CLAUDE.md + orchestrator
- Module 03 agent → loads module_03/CLAUDE.md + orchestrator

Each agent starts with full context from its layer.
```

### Session Persistence via Hand-Off Documents

```
During team session:
├── Module 01 completes its work
│   └── Writes results to layer_6_module_01/hand_off_documents/outgoing/to_above/
├── Module 02 hits a blocker
│   └── Writes escalation to layer_6_module_02/hand_off_documents/outgoing/to_above/
└── Module 03 is in progress
    └── Updates layer_6_module_03/status_6.json

Team session ends. Agents terminated.

Next team session starts:
├── Module 01 agent reads hand_off_documents → knows work is done
├── Module 02 agent reads hand_off_documents → knows there's a blocker to resolve
└── Module 03 agent reads status_6.json → resumes from where it stopped
```

### AALang Orchestrator as Team Coordinator

Instead of Agent Teams' default coordination, the team lead uses the AALang orchestrator pattern:

```
Team Lead (loads layer_0_orchestrator.gab.jsonld):
├── Receive Mode: Parse the user's request
├── Delegation Mode: Assign tasks to module agents (max 3 concurrent)
├── Monitoring Mode: Track progress, handle failures (circuit breaker)
├── Aggregation Mode: Collect results from all modules
└── Report Mode: Deliver final result to user
```

---

## Implementation Considerations

### What Claude Code Agent Teams Supports Today

Based on the current Agent Teams API:
- `TeamCreate` — creates a team with a task list
- `Task` tool with `team_name` — spawns teammates
- `TaskCreate/TaskUpdate/TaskList` — shared task management
- `SendMessage` — inter-agent messaging (DM, broadcast, shutdown)
- Teammates go idle between turns and can be re-activated

### What We'd Need to Build

1. **Layer-aware team creation**: A script or skill that reads the layer structure and creates a team with agents pre-loaded with their layer context

2. **Context injection**: When spawning a teammate via the Task tool, include the layer's CLAUDE.md path so the agent loads it on start

3. **Hand-off document bridge**: After a team session, a script that extracts task results and writes them to the appropriate hand_off_documents directories

4. **Status sync**: A script that reads Agent Teams task list status and syncs it to status.json files in the layer structure

5. **Orchestrator integration**: A way to make the team lead follow the AALang orchestrator pattern instead of ad-hoc coordination

### What Might Not Be Possible (Yet)

- **Persistent agent instances**: Agent Teams terminates agents when the team is deleted. We can persist context via files, but we can't keep the actual agent process alive.

- **Live layer jumping**: Entering a specific layer's agent mid-execution might require Agent Teams to support addressing agents by their layer identity, not just team name.

- **Cross-team communication**: If multiple teams run in parallel (e.g., school team and research team), there's no built-in mechanism for cross-team messaging.

---

## Phased Implementation

### Phase 1: Manual Bridge
- Manually create teams that correspond to layer structure
- Include layer CLAUDE.md paths in agent prompts
- After team session, manually write hand-off documents
- Test whether layer context actually improves agent behavior

### Phase 2: Automated Scripts
- Build scripts that create teams from layer structure
- Build scripts that sync task results to hand-off documents
- Build scripts that sync status between Agent Teams and status.json
- Create skills that automate the bridge

### Phase 3: AALang-Driven Teams
- Team lead loads and follows the AALang orchestrator pattern
- Skill router determines which agents to spawn and when
- Full integration: Agent Teams is the runtime, layer-stage is the persistence layer, AALang is the behavior specification

---

## Open Questions

1. **Can Agent Teams agents read arbitrary files on startup?** If we include a CLAUDE.md path in the agent prompt, does Claude Code's CLAUDE.md chain traversal kick in for that agent?

2. **Can we customize the team lead's coordination strategy?** Or is it always the default Agent Teams behavior?

3. **Is there a way to prevent team deletion?** Or at minimum, export team state before deletion?

4. **Can teammates be spawned with different subagent_types that load different CLAUDE.md chains?** This would allow each layer agent to have its own context chain.

5. **What happens if we create a team that maps 1:1 to a layer hierarchy?** Does the overhead of Agent Teams outweigh the benefit of live interactivity?

---

*Research feature: layer_0_feature_aalang_integration/agent_teams_convergence*
*Last updated: 2026-02-07*
