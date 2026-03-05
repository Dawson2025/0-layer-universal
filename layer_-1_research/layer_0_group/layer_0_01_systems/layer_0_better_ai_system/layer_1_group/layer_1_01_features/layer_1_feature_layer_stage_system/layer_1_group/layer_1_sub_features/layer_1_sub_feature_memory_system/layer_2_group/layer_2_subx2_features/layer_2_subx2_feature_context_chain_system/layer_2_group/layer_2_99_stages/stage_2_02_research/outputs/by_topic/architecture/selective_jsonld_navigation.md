---
resource_id: "45b60f16-567a-468c-8987-c21defa3c8ab"
resource_type: "output"
resource_name: "selective_jsonld_navigation"
---
# Selective JSON-LD Graph Navigation — Research Findings

## Date: 2026-02-07

## Summary

Agents CAN parse JSON-LD files as a graph and load only the nodes they need. Using `jq` (available on the system), selective navigation reduces context load to **2-3% of the full file**. This directly addresses both Problem 4 (context efficiency) and Problem 3 (skill invocation precision).

---

## Demonstration: `layer_0_orchestrator.gab.jsonld` (701 lines, 28,973 bytes)

### Step 1: Read the Index (2.5% of file)

```bash
jq '."@graph"[]."@id"' layer_0_orchestrator.gab.jsonld
```

Returns 29 node IDs in 717 bytes:
```
"orch:ExecutionInstructions"
"orch:Layer0Orchestrator"
"orch:ReceiveMode"
"orch:ReceivePersona1"
"orch:ReceivePersona2"
"orch:DelegationMode"
... (29 total)
```

### Step 2: Navigate to a Specific Node (2.8%)

```bash
jq '."@graph"[] | select(."@id" == "orch:ReceiveMode")' file.jsonld
```

Returns just that node's full definition (816 bytes), including:
- Purpose
- Constraints (what to do, what not to do)
- Contained personas
- Handoff document paths
- Mode transitions

### Step 3: Filter by Type (1.8%)

```bash
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' file.jsonld
```

Returns just the 5 modes with their purposes (521 bytes).

### Step 4: Get State Actors (~1.4%)

```bash
jq '."@graph"[] | select(.["@id"] | test("StateActor")) | {id: .["@id"], purpose: .purpose}' file.jsonld
```

Returns 5 state actors with purposes (~400 bytes).

---

## Efficiency Comparison

| Loading Strategy | Bytes | Lines | % of Full |
|-----------------|-------|-------|-----------|
| Load entire file | 28,973 | 701 | 100% |
| Load index only | 717 | 29 | 2.5% |
| Load 1 mode + constraints | 816 | ~25 | 2.8% |
| Load all 5 modes (summary) | 521 | ~20 | 1.8% |
| Load all state actors | ~400 | ~15 | 1.4% |
| **Typical selective load** | **~1,500** | **~50** | **~5%** |

A typical interaction (read index + load relevant mode + load relevant state actors) uses about **5% of the full file**.

---

## Three Implementation Approaches

### Approach A: jq via Bash Tool (Available NOW)

The agent uses Bash to call jq queries directly:

```bash
# Skill reads the graph index
jq '."@graph"[]."@id"' /path/to/agent.gab.jsonld

# Skill navigates to the relevant mode
jq '."@graph"[] | select(."@id" == "orch:DelegationMode")' /path/to/agent.gab.jsonld

# Skill gets mode constraints (the trigger conditions)
jq '."@graph"[] | select(."@id" == "orch:DelegationMode") | .constraints' /path/to/agent.gab.jsonld
```

**Pros**: Works today, no setup needed, jq already installed
**Cons**: Agent needs to know jq syntax, Bash tool overhead per query

### Approach B: Custom MCP Server (Needs Building)

A dedicated `aalang-graph` MCP server that exposes clean tools:

```
Tool: aalang_get_index(file_path) → returns list of node IDs and types
Tool: aalang_get_node(file_path, node_id) → returns specific node
Tool: aalang_get_modes(file_path) → returns all modes with purposes
Tool: aalang_get_constraints(file_path, mode_id) → returns mode constraints
Tool: aalang_get_state_actors(file_path) → returns all state actors
```

**Pros**: Clean API, no jq knowledge needed, could cache parsed graphs
**Cons**: Needs development, another MCP server to maintain

### Approach C: Read Tool with Line Offsets (Available NOW)

If JSON-LD files follow a consistent structure, the agent can use the Read tool with `offset` and `limit` to read just sections:

```
Read(file_path, offset=42, limit=30)  # Lines 42-72: ReceiveMode definition
```

**Pros**: No extra tools needed
**Cons**: Fragile (line numbers change), requires knowing the structure beforehand

### Recommended: Start with A (jq), evolve to B (MCP server)

jq works today and proves the concept. If it's valuable, build the MCP server for a cleaner interface.

---

## Application to Problem 3: Skill Invocation

**How selective graph navigation fixes vague skill descriptions:**

Current state — skill description is vague:
```
description: "Use this skill when you need to work through stages properly"
```

With selective JSON-LD navigation, a skill can:
1. Read the stage agent's graph index (find all modes)
2. Identify which mode matches the current task
3. Load that mode's constraints (explicit trigger conditions)
4. Present those constraints to the LLM as precise instructions

Example flow for `/stage-workflow` skill:
```
1. jq '."@graph"[]."@id"' → find relevant stage agent definition
2. jq 'select(."@type" == "gab:Mode") | {id, purpose}' → list available modes
3. Match user's task to a mode (e.g., "doing research" → "ResearchMode")
4. jq 'select(."@id" == "ResearchMode") | .constraints' → get exact constraints
5. Present constraints as instructions: "You MUST: ..., You MUST NOT: ..."
```

The JSON-LD constraints become the precise WHEN/WHEN NOT conditions that the skill was missing.

---

## Application to Problem 4: Context Efficiency

Instead of loading 701 lines of orchestrator definition into static context (via CLAUDE.md), the agent loads:
- **Statically** (CLAUDE.md): 3-line reference to the JSON-LD file (where it is, what it defines)
- **Dynamically** (via skill): 50 lines of targeted graph data (the specific mode/actors needed for THIS task)

**Result**: 95% reduction in context usage for AALang definitions.

---

## Next Steps

1. **Test with real scenarios**: Have an agent use jq to navigate the orchestrator during an actual task
2. **Build jq queries into skills**: The `/context-gathering` and `/stage-workflow` skills could use jq internally
3. **Evaluate MCP server**: If jq approach works well, decide whether a dedicated MCP server is worth building
4. **Create standardized queries**: Document the common jq patterns for each type of JSON-LD file

---

*Research finding: selective JSON-LD graph navigation*
*Validated: 2026-02-07 with live jq tests on layer_0_orchestrator.gab.jsonld*
*Status: PROVEN — jq approach works today, 2-5% context load vs 100%*
