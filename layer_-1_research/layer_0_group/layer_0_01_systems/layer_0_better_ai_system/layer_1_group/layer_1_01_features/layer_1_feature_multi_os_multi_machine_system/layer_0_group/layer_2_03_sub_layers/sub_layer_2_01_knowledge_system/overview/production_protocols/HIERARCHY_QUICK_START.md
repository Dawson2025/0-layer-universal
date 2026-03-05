---
resource_id: "cc46c939-33c9-4c60-b689-540a4d20445e"
resource_type: "document"
resource_name: "HIERARCHY_QUICK_START"
---
# AI Manager Hierarchy - Quick Start Guide

**Reading Time**: 5-10 minutes
**Goal**: Get started with the AI Manager Hierarchy System quickly
**Target Audience**: Agents new to the hierarchy, managers starting a new project

---

<!-- section_id: "1318acfd-5daa-4555-83b6-f7b978de5d5a" -->
## The 3-Minute Version

<!-- section_id: "c6fe5d92-5d65-49d6-b8e7-682d1c635812" -->
### What Is It?

The **AI Manager Hierarchy System** is a coordination framework for multi-agent work. It organizes agents into **layers** (project → feature → component) and **stages** (request → plan → develop → test → deliver), with **managers** delegating to **workers** via **handoff documents**.

<!-- section_id: "e3dfcbf6-ed79-4a3b-9339-b72c612f847a" -->
### Why Use It?

- **Coordination**: Managers and workers have clear roles and boundaries
- **Observability**: All work is logged and traceable
- **Safety**: Permission levels prevent accidents, budget limits prevent overspend
- **Scalability**: Works for solo agents or teams of 100+

<!-- section_id: "5cb568a6-7f85-4314-8992-e1f038c96b34" -->
### How It Works (Visual)

```
L0 (Universal) → L1 (Project) → L2 (Feature) → L3 (Component)
     │               │              │               │
     ↓               ↓              ↓               ↓
 Supervisor    Project Mgr    Feature Mgr    Component Worker
     │               │              │               │
     └───────────────┴──────────────┴───────────────┘
                Handoff Documents
```

<!-- section_id: "0214408d-7267-45a2-880d-ce98df9a817e" -->
### Core Concepts (30 seconds each)

1. **Layers**: Nested work levels (L0: cross-project, L1: project, L2: feature, L3: component)
2. **Stages**: Chronological workflow (request → instructions → planning → research → development → testing → delivery)
3. **Manager/Worker**: Managers delegate via handoffs, workers execute and report back
4. **Handoffs**: JSON documents defining tasks, constraints, artifacts, and status
5. **OS Variants**: Context files (CLAUDE.md, AGENTS.md, GEMINI.md) for each OS (wsl, linux_ubuntu, windows, macos)

---

<!-- section_id: "3e0b3ba7-10f0-489b-ad73-69d636b1549a" -->
## Essential Links (Bookmark These)

<!-- section_id: "d518d517-5303-4b60-8b5a-703d47808be6" -->
### Start Here

1. **MASTER_DOCUMENTATION_INDEX.md**
   - `/home/dawson/code/0_layer_universal/0_context/MASTER_DOCUMENTATION_INDEX.md`
   - Your navigation hub - find anything from here

2. **SYSTEM_OVERVIEW.md**
   - `/home/dawson/code/0_layer_universal/0_context/SYSTEM_OVERVIEW.md`
   - High-level architecture and concepts

3. **USAGE_GUIDE.md**
   - `/home/dawson/code/0_layer_universal/0_context/USAGE_GUIDE.md`
   - How to work with the hierarchy

<!-- section_id: "922392ba-8db9-472a-8c38-f4c08ea78832" -->
### When You Need Details

4. **Layer/Stage Framework**
   - `/home/dawson/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
   - Detailed layer and stage definitions

5. **Handoff Schema**
   - `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
   - JSON schema for handoff documents

6. **Layer Manager READMEs**
   - L0: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.00_ai_manager_system/README.md`
   - L1: `/home/dawson/code/0_layer_universal/0_context/layer_1_project/1.00_ai_manager_system/README.md`
   - L2: `/home/dawson/code/0_layer_universal/0_context/layer_2_features/2.00_ai_manager_system/README.md`
   - L3: `/home/dawson/code/0_layer_universal/0_context/layer_3_components/3.00_ai_manager_system/README.md`

<!-- section_id: "e4b1de04-254b-4e8e-91c4-c29d84425acd" -->
### When You're Ready to Adopt

7. **Adoption Checklist**
   - `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/HIERARCHY_ADOPTION_CHECKLIST.md`
   - Step-by-step guide to adopting the hierarchy

8. **Migration Guide**
   - `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/MIGRATION_GUIDE.md`
   - Retrofit existing projects with hierarchy patterns

---

<!-- section_id: "fec131bd-bdcb-4ac0-8575-12a1584bfe14" -->
## Your First Handoff (10-Minute Walkthrough)

<!-- section_id: "11da70ad-c19a-414e-8513-902a40769952" -->
### Scenario: You're a Project Manager (L1)

You receive a request to implement a new feature. Here's how to use the hierarchy:

<!-- section_id: "371a8401-c762-4796-b0cc-960ad6dbd35b" -->
### Step 1: Receive Handoff from L0 Supervisor

**Example Handoff** (from human or L0 supervisor to you):

```json
{
  "schemaVersion": "1.0",
  "id": "handoff_L0_to_L1_web-app_add-user-auth_2025-12-24T10:00:00Z",
  "kind": "vertical",
  "layer": {"from": 0, "to": 1},
  "stage": {"from": "0.00_request_gathering", "to": "0.01_instructions"},
  "from": {"agent_id": "human_instructor", "role": "project_owner"},
  "to": {"agent_id": "L1_web-app_manager", "role": "project_manager"},
  "task": {
    "description": "Add user authentication to web-app project",
    "objectives": ["Implement login/logout", "Hash passwords with bcrypt", "Use session-based auth"]
  },
  "constraints": {
    "budget": "$10.00",
    "deadline": "2025-12-31",
    "scope": "Basic auth only, no OAuth"
  },
  "artifacts": {
    "deliverables": ["Login form", "Session manager", "Password hashing module", "Tests"]
  },
  "status": "pending"
}
```

**Action**: Read the handoff, understand the task, accept it (change status to "in_progress")

<!-- section_id: "419c5d46-7fdc-49e1-a49f-82f177468ac1" -->
### Step 2: Create L2 Handoff for Feature Manager

You break the feature into L2 tasks:

```json
{
  "schemaVersion": "1.0",
  "id": "handoff_L1_to_L2_web-app_user-auth_2025-12-24T10:30:00Z",
  "kind": "vertical",
  "layer": {"from": 1, "to": 2},
  "stage": {"from": "0.02_planning", "to": "0.04_development"},
  "from": {"agent_id": "L1_web-app_manager", "role": "project_manager"},
  "to": {"agent_id": "L2_user-auth_manager", "role": "feature_manager"},
  "task": {
    "description": "Implement user authentication feature",
    "subtasks": [
      {"id": "L3_login-form", "description": "Create login form component"},
      {"id": "L3_session-mgr", "description": "Create session manager"},
      {"id": "L3_password-hash", "description": "Create password hashing module"}
    ]
  },
  "constraints": {
    "budget": "$5.00",
    "deadline": "2025-12-30",
    "scope": "Use Flask-Login library"
  },
  "artifacts": {
    "deliverables": ["Login form (HTML + route)", "Session manager (Python module)", "Password hashing (bcrypt wrapper)"]
  },
  "status": "pending"
}
```

**Action**: Save handoff to `.ai_context/handoffs/outgoing/`, spawn L2 manager

<!-- section_id: "fa7edeea-c944-4aeb-9e09-fbfdf18d030c" -->
### Step 3: L2 Manager Spawns L3 Workers

L2 manager reads your handoff and spawns L3 workers for each component:

**Example: Spawn Codex worker for login form** (simple task, < 5 min)

```bash
codex run --model=codestral \
  --message="$(cat handoff_L2_to_L3_login-form.json)" \
  --output=templates/login.html
```

**Example: Spawn Claude worker for session manager** (complex task, 15-30 min)

```bash
claude-code --allowed=Read,Write,Bash \
  --context="L3 worker: Implement session manager for Flask app" \
  < handoff_L2_to_L3_session-mgr.json
```

<!-- section_id: "83eafe24-e2ff-460c-86db-66772d265a8f" -->
### Step 4: L3 Workers Complete and Report Back

Each worker:
1. Reads handoff
2. Implements component
3. Writes handoff with status "completed" and actual cost

**Example: L3 worker completion**

```json
{
  "schemaVersion": "1.0",
  "id": "handoff_L2_to_L3_login-form_2025-12-24T11:00:00Z",
  "status": "completed",
  "results": {
    "artifacts": ["templates/login.html", "routes/auth.py"],
    "cost": "$0.05",
    "duration": "3 minutes"
  }
}
```

<!-- section_id: "09ba544c-c6ce-472d-aa9c-b594c13e092d" -->
### Step 5: L2 Manager Aggregates and Reports to L1

L2 manager collects all L3 results, aggregates, and reports back to you:

```json
{
  "schemaVersion": "1.0",
  "id": "handoff_L1_to_L2_web-app_user-auth_2025-12-24T10:30:00Z",
  "status": "completed",
  "results": {
    "artifacts": ["Login form (templates/login.html)", "Session manager (auth/session.py)", "Password hashing (auth/hash.py)"],
    "cost": "$4.20",
    "duration": "2 hours",
    "subtask_results": [
      {"id": "L3_login-form", "status": "completed", "cost": "$0.05"},
      {"id": "L3_session-mgr", "status": "completed", "cost": "$2.10"},
      {"id": "L3_password-hash", "status": "completed", "cost": "$2.05"}
    ]
  }
}
```

<!-- section_id: "d3dabef8-c8a5-4589-94db-7ffc405b898a" -->
### Step 6: You Report Back to L0

You aggregate L2 results and report completion to L0 supervisor:

```json
{
  "schemaVersion": "1.0",
  "id": "handoff_L0_to_L1_web-app_add-user-auth_2025-12-24T10:00:00Z",
  "status": "completed",
  "results": {
    "artifacts": ["User authentication feature (login/logout, session management, password hashing)", "Tests passing"],
    "cost": "$4.20",
    "duration": "2 hours"
  }
}
```

**Done!** Feature complete, within budget, fully logged.

---

<!-- section_id: "48b82207-768c-4791-a191-4711d593bf63" -->
## Common Patterns by Use Case

<!-- section_id: "15120979-417a-49be-bcc3-63870dedbde1" -->
### Use Case 1: Solo Agent on Simple Project

**Pattern**: Use L1 only, skip L2/L3

- Create L1 project context
- Document features (optional)
- Execute work directly at L1 (no delegation)
- Log actions (optional)

**Time**: 1-2 hours setup, minimal overhead

---

<!-- section_id: "7727307d-e172-4957-8ae5-a67b8fca4acb" -->
### Use Case 2: Small Team on Medium Project (3-5 features)

**Pattern**: Use L0 → L1 → L2, skip L3

- L0 supervisor coordinates projects
- L1 managers coordinate features
- L2 managers execute components directly (no L3 workers)
- Handoffs for L0→L1 and L1→L2
- Observability logging

**Time**: 3-4 hours setup, moderate overhead

---

<!-- section_id: "48f18b84-1bd8-4954-927b-7a58a71bcbd9" -->
### Use Case 3: Large Team on Complex Project (10+ features)

**Pattern**: Use full hierarchy L0 → L1 → L2 → L3

- L0 supervisor orchestrates multiple projects
- L1 managers coordinate features across projects
- L2 managers delegate to L3 workers
- L3 workers execute atomic components
- Full handoff documents, observability, safety rules
- CLI recursion or framework orchestration

**Time**: 6-8 hours setup, high initial overhead but scales well

---

<!-- section_id: "a3689070-7099-4619-b12e-94ff9a58e0af" -->
## Quick Reference: Roles and Responsibilities

| Layer | Role | Reads | Writes | Spawns | Example |
|-------|------|-------|--------|--------|---------|
| L0 | Supervisor | User requests | L0→L1 handoffs | L1 managers | Human or meta-agent |
| L1 | Project Manager | L0→L1 handoffs | L1→L2 handoffs | L2 managers | Claude Code (project-level) |
| L2 | Feature Manager | L1→L2 handoffs | L2→L3 handoffs | L3 workers | Claude Code (feature-level) |
| L3 | Component Worker | L2→L3 handoffs | L3→L2 results | (None) | Codex, Claude (component-level) |

---

<!-- section_id: "fedd1239-1064-46cc-b6c3-b5289a5d6a69" -->
## Quick Reference: Tools and When to Use Them

| Tool | Best For | Cost | Speed | Spawned By |
|------|----------|------|-------|------------|
| **Claude Sonnet 4.5** | Complex reasoning, managers, deep analysis | $$$$ | Slow | L0, L1, L2 (for complex tasks) |
| **Claude Haiku** | Medium complexity, workers, code implementation | $$ | Medium | L1, L2 (for medium tasks) |
| **Codex (codestral)** | Simple tasks, code generation, atomic components | $ | Fast | L2 (for simple tasks), L3 |
| **Gemini CLI** | Planning, research, architecture decisions | $$$ | Slow | L0, L1 (for planning stage) |

---

<!-- section_id: "2527137f-3ae6-4345-957f-9fa30eec663f" -->
## Quick Reference: Observability and Safety

<!-- section_id: "6c344fed-ff06-4bb7-ad7d-b679293654bf" -->
### Where Do Logs Live?

```
<project-root>/.ai_context/logs/
├── managers/          (L1, L2 manager logs)
├── workers/           (L3 worker logs)
└── handoffs/          (Handoff creation, acceptance, completion)
```

<!-- section_id: "60e6195b-556e-4406-a440-35acbcc07572" -->
### What Gets Logged?

- Manager spawning workers
- Handoff creation, acceptance, completion
- Worker results
- Errors and warnings
- Cost and duration

<!-- section_id: "b46cd05a-83da-4fb2-945a-2e0fbef6b923" -->
### What Are the Budget Limits?

| Layer | Daily Limit | Task Limit | Permission Level |
|-------|-------------|------------|------------------|
| L0 | $15 | $5 per task | System Manager (Level 4) |
| L1 | $10 | $3 per task | Project Manager (Level 3) |
| L2 | $5 | $1 per task | Standard Agent (Level 2) |
| L3 | $2 | $0.25 per task | Sandboxed Write (Level 1) |

---

<!-- section_id: "8d9b91c4-7cad-4b5c-8a6b-d6a5bed1e91c" -->
## Next Steps

<!-- section_id: "44040bf1-9aa6-404f-980b-d298625629e8" -->
### If You're a Manager Starting a New Project

1. Read HIERARCHY_ADOPTION_CHECKLIST.md (30 min)
2. Create L1 project context (1 hour)
3. Create your first handoff (15 min)
4. Spawn a worker and test the flow (30 min)
5. Review logs and iterate (15 min)

**Total**: ~2.5 hours to full adoption

<!-- section_id: "d93c8a8f-9dc8-42ee-93fe-d63955ae6168" -->
### If You're a Worker Joining an Existing Project

1. Find the project's L1 context (5 min)
2. Read the handoff you received (5 min)
3. Check OS-specific context (CLAUDE.md, AGENTS.md, or GEMINI.md) (10 min)
4. Execute your task (varies)
5. Write completion handoff (10 min)

**Total**: ~30 min overhead + task execution time

<!-- section_id: "759b95c6-b4a7-4e9e-bb51-aae0c7f3d819" -->
### If You're Retrofitting an Existing Project

1. Read MIGRATION_GUIDE.md (30 min)
2. Choose migration strategy (10 min)
3. Create project assessment (30 min)
4. Create layer mapping (30 min)
5. Start using hierarchy for new work (ongoing)

**Total**: ~2 hours to start migration

---

<!-- section_id: "9f1fccab-63e2-411c-8762-a9c22411affc" -->
## Troubleshooting (1-Minute Fixes)

**"I can't find the right doc"**
→ Start with MASTER_DOCUMENTATION_INDEX.md, use search

**"Handoff feels too heavy"**
→ Use minimal schema (just task, from, to, status) for simple tasks

**"I don't know my layer"**
→ Ask: "Entire project (L1)? Feature (L2)? Component (L3)?"

**"Worker isn't using hierarchy"**
→ Link to HIERARCHY_ADOPTION_CHECKLIST.md in task instructions

**"Budget limit is too low"**
→ Request increase from supervisor, or escalate task to higher layer

---

<!-- section_id: "1a6111a9-5393-4063-80b7-732beb868186" -->
## Related Documentation

**Essential**:
- Adoption Checklist: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/HIERARCHY_ADOPTION_CHECKLIST.md`
- Migration Guide: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/MIGRATION_GUIDE.md`

**Deep Dive**:
- Master Index: `/home/dawson/code/0_layer_universal/0_context/MASTER_DOCUMENTATION_INDEX.md`
- System Overview: `/home/dawson/code/0_layer_universal/0_context/SYSTEM_OVERVIEW.md`
- Usage Guide: `/home/dawson/code/0_layer_universal/0_context/USAGE_GUIDE.md`

**Operational**:
- Observability: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`
- Safety Rules: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- Deployment: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`

---

**Document Status**: Active
**Version**: 1.0
**Last Updated**: 2025-12-24
**Next Review**: 2026-01-24
