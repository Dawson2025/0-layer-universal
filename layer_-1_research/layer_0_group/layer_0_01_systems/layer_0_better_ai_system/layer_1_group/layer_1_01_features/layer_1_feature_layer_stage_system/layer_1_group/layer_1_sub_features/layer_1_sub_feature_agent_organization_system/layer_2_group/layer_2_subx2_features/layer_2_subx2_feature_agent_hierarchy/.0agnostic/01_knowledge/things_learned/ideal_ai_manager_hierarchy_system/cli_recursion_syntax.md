---
resource_id: "a925638a-d113-415a-94eb-eddfc2985c83"
resource_type: "knowledge"
resource_name: "cli_recursion_syntax"
---
## CLI Recursion Syntax and Patterns

This document provides concrete examples of using CLI recursion to create deep agent hierarchies.

It covers:
- Claude Code recursive delegation syntax
- Handoff-based recursion patterns
- Multi-level manager chains
- Practical examples

---

## 1. Core Concept

**CLI Recursion** allows agents to spawn other agents by invoking CLI commands, creating arbitrary depth hierarchies without framework-specific APIs.

**Key Pattern:**
```
L0 Manager (claude-code)
  → spawns L1 Manager (claude-code in subdirectory)
    → spawns L2 Manager (claude-code in subdirectory)
      → spawns L3 Workers (codex)
```

Each invocation:
1. Loads appropriate layer context (CLAUDE.md, AGENTS.md)
2. Reads incoming handoff
3. Executes work
4. Writes outgoing handoff
5. Optionally spawns deeper agents

---

## 2. Claude Code Recursion Syntax

### 2.1 Basic Recursive Call

```bash
# L0 manager spawning L1 manager
cd /workspace/layer_2_ecommerce

claude-code \
  --working-dir "layer_2_ecommerce" \
  --allowed "B(cla:*)" \
  process-handoff handoff-20250115.json
```

**Flags Explained:**
- `--working-dir`: Sets working directory (loads CLAUDE.md from there)
- `--allowed "B(cla:*)`: Allows subprocess to call "claude" binary (recursive permission)

### 2.2 Permission Patterns

**Allow Specific Tools:**
```bash
# Allow subprocess to call claude-code and codex
claude-code --allowed "B(cla:*,codex:*)" process-handoff handoff.json
```

**Full Recursion:**
```bash
# Allow subprocess to call any binary (use with caution)
claude-code --allowed "B(*)" process-handoff handoff.json
```

**Read-Only:**
```bash
# No subprocess binary execution allowed
claude-code process-handoff handoff.json
```

### 2.3 Handoff-Based Recursion

```bash
#!/bin/bash
# L1 manager script

# Read incoming handoff
HANDOFF=$(cat layer_2_ecommerce/manager_handoff_documents/incoming.json)
TASK=$(echo "$HANDOFF" | jq -r '.task')

echo "L1 Manager processing: $TASK"

# Decompose into L2 features
FEATURES=$(echo "$HANDOFF" | jq -r '.features[]')

# Spawn L2 manager for each feature
for FEATURE in $FEATURES; do
  echo "Spawning L2 manager for feature: $FEATURE"

  # Create L2 handoff
  cat > "layer_2_$FEATURE/manager_handoff_documents/incoming.json" <<EOF
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-$FEATURE",
  "layer": 2,
  "parent_id": "$(echo "$HANDOFF" | jq -r '.id')",
  "task": "Implement $FEATURE feature",
  "constraints": $(echo "$HANDOFF" | jq -r '.constraints')
}
EOF

  # Spawn L2 manager in background
  (
    cd "layer_2_$FEATURE"
    claude-code \
      --allowed "B(cla:*,codex:*)" \
      process-handoff manager_handoff_documents/incoming.json
  ) &
done

# Wait for all L2 managers
wait

echo "All L2 managers completed"
```

---

## 3. Multi-Layer Example: Full Hierarchy

### 3.1 L0 → L1 Delegation

```python
#!/usr/bin/env python3
# L0 universal manager

import subprocess
import json

def spawn_l1_project_manager(project_name, task):
    """Spawn L1 manager for specific project."""

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l0-to-{project_name}",
        "layer": 1,
        "task": task,
        "constraints": load_l0_constraints(),
        "project": project_name
    }

    # Write handoff
    handoff_path = f"layer_2_{project_name}/manager_handoff_documents/incoming.json"
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Spawn L1 manager
    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", f"layer_2_{project_name}",
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", handoff_path
        ],
        capture_output=True
    )

    return result

# Process universal request
universal_request = load_handoff("layer_0_group/incoming.json")

# Decompose to projects
projects = decompose_to_projects(universal_request)

# Spawn L1 for each project
for project_name, project_task in projects.items():
    spawn_l1_project_manager(project_name, project_task)
```

### 3.2 L1 → L2 Delegation

```python
#!/usr/bin/env python3
# L1 project manager

def spawn_l2_feature_manager(feature_name, task):
    """Spawn L2 manager for specific feature."""

    # Load L1 context
    l1_context = load_context("layer_2_ecommerce/CLAUDE.md")

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l1-to-{feature_name}",
        "layer": 2,
        "task": task,
        "constraints": l1_context["constraints"],
        "feature": feature_name
    }

    handoff_path = f"layer_2_{feature_name}/manager_handoff_documents/incoming.json"
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", f"layer_2_{feature_name}",
            "--allowed", "B(cla:*,codex:*)",
            "--output-style", "feature-manager",  # Use persona
            "process-handoff", handoff_path
        ],
        capture_output=True
    )

    return result

# Process project-level request
project_request = load_handoff("layer_2_ecommerce/manager_handoff_documents/incoming.json")

# Decompose to features
features = decompose_to_features(project_request)

# Spawn L2 for each feature (in parallel)
with ProcessPoolExecutor() as executor:
    futures = [
        executor.submit(spawn_l2_feature_manager, feature_name, feature_task)
        for feature_name, feature_task in features.items()
    ]

    results = [f.result() for f in futures]
```

### 3.3 L2 → L3 Delegation (Workers)

```python
#!/usr/bin/env python3
# L2 feature manager

def spawn_l3_component_worker(component_name, task, tool="codex"):
    """Spawn L3 worker for component implementation."""

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l2-to-{component_name}",
        "layer": 3,
        "stage": "implementation",
        "task": task,
        "component": component_name
    }

    handoff_path = f"layer_4_{component_name}/hand_off_documents/incoming.json"
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Use codex for L3 implementation (cheaper, faster)
    if tool == "codex":
        result = subprocess.run(
            [
                "codex",
                "--model", "codestral",
                "--agents-md", f"layer_4_{component_name}/AGENTS.md",
                "execute-handoff", handoff_path
            ],
            capture_output=True,
            timeout=300  # 5 minute timeout for leaf workers
        )
    else:
        # Fallback to Claude for complex components
        result = subprocess.run(
            [
                "claude-code",
                "--working-dir", f"layer_4_{component_name}",
                "--model", "claude-haiku",
                "process-handoff", handoff_path
            ],
            capture_output=True
        )

    return result

# Process feature-level request
feature_request = load_handoff("layer_2_auth/manager_handoff_documents/incoming.json")

# Decompose to components
components = decompose_to_components(feature_request)

# Spawn L3 workers (in parallel)
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [
        executor.submit(spawn_l3_component_worker, comp_name, comp_task)
        for comp_name, comp_task in components.items()
    ]

    results = [f.result() for f in futures]
```

---

## 4. Advanced Patterns

### 4.1 Dynamic Tool Selection

```python
def spawn_agent_smart(layer, stage, task, handoff):
    """Intelligently select tool based on task characteristics."""

    # Estimate complexity
    complexity = estimate_complexity(task)

    # Select tool based on policy
    if layer <= 2 or complexity > 0.7:
        tool = "claude-code"
        model = "claude-sonnet-4.5" if complexity > 0.8 else "claude-haiku"
    elif stage in ["request", "instructions", "planning"]:
        tool = "gemini"
        model = "gemini-pro-2"
    else:
        tool = "codex"
        model = "codestral"

    # Build command
    if tool == "claude-code":
        cmd = [
            "claude-code",
            "--working-dir", f"layer_{layer}",
            "--model", model,
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", handoff
        ]
    elif tool == "codex":
        cmd = [
            "codex",
            "--model", model,
            "--agents-md", f"layer_{layer}/AGENTS.md",
            "execute-handoff", handoff
        ]
    elif tool == "gemini":
        cmd = [
            "gemini",
            "--model", model,
            "--system-file", f"layer_{layer}/GEMINI.md",
            "process", handoff
        ]

    return subprocess.run(cmd, capture_output=True)
```

### 4.2 Retry with Escalation

```python
def execute_with_retry_escalation(layer, stage, task, handoff, max_retries=3):
    """Execute task, escalating to more powerful tools on failure."""

    tiers = ["codestral", "claude-haiku", "claude-sonnet-4.5"]

    for attempt, model_tier in enumerate(tiers):
        if attempt >= max_retries:
            break

        print(f"Attempt {attempt + 1} with {model_tier}")

        # Determine tool
        if "claude" in model_tier:
            tool = "claude-code"
        else:
            tool = "codex"

        # Execute
        result = spawn_agent_smart(layer, stage, task, handoff)

        # Check result
        if result.returncode == 0:
            return result

        print(f"Attempt {attempt + 1} failed, escalating...")

    # All attempts failed
    raise RuntimeError(f"Task failed after {max_retries} attempts")
```

### 4.3 Conditional Recursion

```python
def spawn_if_needed(layer, stage, task, handoff):
    """Only spawn deeper agents if task is complex enough."""

    # Simple tasks: handle directly
    if is_simple_task(task):
        return execute_directly(task, handoff)

    # Complex tasks: delegate
    elif should_decompose(task):
        subtasks = decompose(task)

        # Spawn agents for subtasks
        results = []
        for subtask in subtasks:
            result = spawn_agent_smart(layer + 1, stage, subtask, handoff)
            results.append(result)

        # Aggregate
        return aggregate_results(results)

    # Medium tasks: execute with current agent
    else:
        return execute_directly(task, handoff)
```

---

## 5. Wrapper Scripts

### 5.1 Generic Launcher

```bash
#!/bin/bash
# launch_agent.sh - Generic agent launcher

LAYER=$1
STAGE=$2
HANDOFF=$3
TOOL=${4:-auto}  # auto, claude, codex, gemini

# Auto-select tool if not specified
if [ "$TOOL" = "auto" ]; then
  if [ "$LAYER" -le 2 ] || [ "$STAGE" = "criticism" ]; then
    TOOL="claude"
  elif [ "$STAGE" = "request" ] || [ "$STAGE" = "instructions" ]; then
    TOOL="gemini"
  else
    TOOL="codex"
  fi
fi

# Launch appropriate tool
case $TOOL in
  claude)
    claude-code \
      --working-dir "layer_${LAYER}" \
      --allowed "B(cla:*,codex:*,gemini:*)" \
      process-handoff "$HANDOFF"
    ;;

  codex)
    codex \
      --model codestral \
      --agents-md "layer_${LAYER}/AGENTS.md" \
      execute-handoff "$HANDOFF"
    ;;

  gemini)
    gemini \
      --model gemini-pro-2 \
      --system-file "layer_${LAYER}/GEMINI.md" \
      process "$HANDOFF"
    ;;
esac
```

**Usage:**
```bash
# Let script choose tool
./launch_agent.sh 2 implementation handoff.json

# Force specific tool
./launch_agent.sh 2 implementation handoff.json claude
```

### 5.2 Parallel Launcher

```bash
#!/bin/bash
# parallel_launch.sh - Launch multiple agents in parallel

LAYER=$1
STAGE=$2
shift 2
HANDOFFS=("$@")

# Launch each in background
PIDS=()
for HANDOFF in "${HANDOFFS[@]}"; do
  ./launch_agent.sh "$LAYER" "$STAGE" "$HANDOFF" &
  PIDS+=($!)
done

# Wait for all
echo "Waiting for ${#PIDS[@]} agents..."
for PID in "${PIDS[@]}"; do
  wait "$PID"
done

echo "All agents completed"
```

**Usage:**
```bash
./parallel_launch.sh 3 implementation handoff1.json handoff2.json handoff3.json
```

---

## 6. Summary

CLI recursion enables deep hierarchies:

1. **Explicit Commands**: Use `claude-code --allowed "B(...)"` to enable recursion
2. **Handoff-Driven**: Each level reads incoming, processes, writes outgoing
3. **Tool Selection**: Use different tools at different layers (Claude for managers, Codex for workers)
4. **Parallel Execution**: Spawn multiple agents concurrently
5. **Error Handling**: Retry with escalation to more powerful models

This pattern is framework-agnostic and works with any CLI-based agent tool.
