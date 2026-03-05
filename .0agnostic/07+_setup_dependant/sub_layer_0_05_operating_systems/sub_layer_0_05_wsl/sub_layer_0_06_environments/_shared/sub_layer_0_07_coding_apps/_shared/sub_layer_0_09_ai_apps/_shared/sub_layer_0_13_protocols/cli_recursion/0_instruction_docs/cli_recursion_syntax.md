---
resource_id: "0e2a5bec-1712-4383-a05e-fef9b8fe38f5"
resource_type: "document"
resource_name: "cli_recursion_syntax"
---
# CLI Recursion Syntax and Patterns

<!-- section_id: "049b1eb6-46b0-482d-88f4-6d176cd5424b" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "0f55bbcd-9ae1-42ba-bd6b-9bf1dbabdf6c" -->
## Overview

This document provides concrete CLI recursion patterns for creating deep agent hierarchies. CLI recursion allows agents to spawn other agents by invoking CLI commands, enabling arbitrary depth hierarchies without framework-specific APIs.

**Current Environment**:
- **OS**: WSL (Windows Subsystem for Linux), Linux Ubuntu
- **Shell**: bash
- **CLI Tools**: Claude Code, Codex CLI, Gemini CLI
- **Working Directory**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/`

For the normative specification with additional patterns and examples, see:
- **Normative Spec**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`

---

<!-- section_id: "b3dd6801-fe9a-415a-9d61-f95b7a208140" -->
## Core Concept

**CLI Recursion Pattern**:
```
L0 Manager (claude-code)
  → spawns L1 Manager (claude-code in L1 directory)
    → spawns L2 Manager (claude-code in L2 directory)
      → spawns L3 Workers (codex, gemini, claude-code)
```

Each invocation:
1. Loads appropriate layer context (CLAUDE.md, AGENTS.md, GEMINI.md)
2. Reads incoming handoff from `*/manager_handoff_documents/incoming.json` or `*/hand_off_documents/incoming.json`
3. Executes work
4. Writes outgoing handoff
5. Optionally spawns deeper agents

---

<!-- section_id: "b5e160f0-ea9d-4a1c-a25d-0c166dac2a53" -->
## Claude Code Recursion Syntax

<!-- section_id: "e1e4440b-dc55-4fbd-9e3b-03ecd0b337c2" -->
### Basic Recursive Call

```bash
# L0 manager spawning L1 manager
cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1_project

claude-code \
  --working-dir "/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1_project" \
  --allowed "B(cla:*)" \
  process-handoff 1.01_manager_handoff_documents/1.00_to_universal/incoming.json
```

**Flags Explained**:
- `--working-dir`: Sets working directory (loads CLAUDE.md from there)
- `--allowed "B(cla:*)`: Allows subprocess to call "claude" binary (enables recursive calls)
- `process-handoff`: Command to process a handoff file

<!-- section_id: "16a5db32-761f-4e62-bc06-5127027db0d0" -->
### Permission Patterns

**Allow Specific Tools**:
```bash
# Allow subprocess to call claude-code and codex
claude-code \
  --working-dir "/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_2_features" \
  --allowed "B(cla:*,codex:*)" \
  process-handoff 2.01_manager_handoff_documents/incoming.json
```

**Full Recursion** (use with caution):
```bash
# Allow subprocess to call any binary
claude-code \
  --working-dir "/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1_project" \
  --allowed "B(*)" \
  process-handoff 1.01_manager_handoff_documents/incoming.json
```

**Read-Only** (no subprocess execution):
```bash
# No subprocess binary execution allowed
claude-code \
  --working-dir "/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_3_components" \
  process-handoff 3.01_manager_handoff_documents/incoming.json
```

---

<!-- section_id: "2401df9a-5770-464d-9068-90cd052faad1" -->
## Handoff-Based Recursion

<!-- section_id: "8e8b6d89-8cc5-41ca-be42-06400dbdda3a" -->
### Bash Script Example: L1 Manager

```bash
#!/bin/bash
# L1 manager script: layer_1_project/scripts/process_handoff.sh

# Path to L1 layer
L1_DIR="/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1_project"

# Read incoming handoff
HANDOFF_FILE="$L1_DIR/1.01_manager_handoff_documents/1.00_to_universal/incoming.json"
HANDOFF=$(cat "$HANDOFF_FILE")
TASK=$(echo "$HANDOFF" | jq -r '.task')

echo "L1 Manager processing: $TASK"

# Decompose into L2 features
FEATURES=$(echo "$HANDOFF" | jq -r '.features[]')

# Spawn L2 manager for each feature
for FEATURE in $FEATURES; do
  echo "Spawning L2 manager for feature: $FEATURE"

  L2_DIR="/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_2_features/$FEATURE"

  # Create L2 handoff
  cat > "$L2_DIR/2.01_manager_handoff_documents/incoming.json" <<EOF
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-$FEATURE-$(date +%s)",
  "layer": 2,
  "parent_id": "$(echo "$HANDOFF" | jq -r '.id')",
  "task": "Implement $FEATURE feature",
  "constraints": $(echo "$HANDOFF" | jq -r '.constraints')
}
EOF

  # Spawn L2 manager in background (parallel execution)
  (
    cd "$L2_DIR"
    claude-code \
      --working-dir "$L2_DIR" \
      --allowed "B(cla:*,codex:*)" \
      process-handoff 2.01_manager_handoff_documents/incoming.json
  ) &
done

# Wait for all L2 managers
wait

echo "All L2 managers completed"

# Aggregate results into L1 outgoing handoff
# (Implementation would collect L2 outgoing handoffs and synthesize L1 result)
```

---

<!-- section_id: "fa626d98-f0da-4b36-add5-5613002ede09" -->
## Multi-Layer Examples

<!-- section_id: "260ee462-fa64-42d6-a192-51b483656973" -->
### L0 → L1 Delegation (Python)

```python
#!/usr/bin/env python3
# L0 universal manager: layer_0/scripts/spawn_l1.py

import subprocess
import json
from pathlib import Path

BASE_DIR = Path("/home/dawson/dawson-workspace/code/0_layer_universal/0_context")

def spawn_l1_project_manager(project_name, task, constraints):
    """Spawn L1 manager for specific project."""

    l1_dir = BASE_DIR / "layer_1_project" / project_name
    handoff_path = l1_dir / "1.01_manager_handoff_documents" / "1.00_to_universal" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l0-to-{project_name}",
        "layer": 1,
        "task": task,
        "constraints": constraints,
        "project": project_name
    }

    # Write handoff
    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Spawn L1 manager
    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", str(l1_dir),
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", str(handoff_path)
        ],
        capture_output=True,
        text=True,
        cwd=str(l1_dir)
    )

    return result

# Example usage
if __name__ == "__main__":
    # Load universal request
    l0_handoff_path = BASE_DIR / "layer_0" / "0.01_manager_handoff_documents" / "incoming.json"
    with open(l0_handoff_path) as f:
        universal_request = json.load(f)

    # Decompose to projects (simplified example)
    projects = {
        "ecommerce": "Build product catalog and shopping cart",
        "math-automation": "Automate homework processing and grading"
    }

    # Spawn L1 for each project
    for project_name, project_task in projects.items():
        print(f"Spawning L1 manager for project: {project_name}")
        result = spawn_l1_project_manager(
            project_name,
            project_task,
            universal_request.get("constraints", [])
        )
        print(f"L1 {project_name} completed with status: {result.returncode}")
```

<!-- section_id: "0c23cbb5-d1fe-4740-9704-a2ff0d82f719" -->
### L1 → L2 Delegation (Python)

```python
#!/usr/bin/env python3
# L1 project manager: layer_1_project/scripts/spawn_l2.py

import subprocess
import json
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

BASE_DIR = Path("/home/dawson/dawson-workspace/code/0_layer_universal/0_context")
L1_DIR = BASE_DIR / "layer_1_project"

def spawn_l2_feature_manager(feature_name, task, constraints):
    """Spawn L2 manager for specific feature."""

    l2_dir = BASE_DIR / "layer_2_features" / feature_name
    handoff_path = l2_dir / "2.01_manager_handoff_documents" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l1-to-{feature_name}",
        "layer": 2,
        "task": task,
        "constraints": constraints,
        "feature": feature_name
    }

    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", str(l2_dir),
            "--allowed", "B(cla:*,codex:*)",
            "--output-style", "feature-manager",  # Optional persona
            "process-handoff", str(handoff_path)
        ],
        capture_output=True,
        text=True,
        cwd=str(l2_dir)
    )

    return result

# Example usage with parallel execution
if __name__ == "__main__":
    # Load L1 request
    l1_handoff_path = L1_DIR / "1.01_manager_handoff_documents" / "1.00_to_universal" / "incoming.json"
    with open(l1_handoff_path) as f:
        project_request = json.load(f)

    # Decompose to features
    features = {
        "auth-system": "Implement user authentication and authorization",
        "shopping-cart": "Build shopping cart with persistent storage",
        "payment-integration": "Integrate Stripe payment processing"
    }

    # Spawn L2 for each feature (in parallel)
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(
                spawn_l2_feature_manager,
                feature_name,
                feature_task,
                project_request.get("constraints", [])
            )
            for feature_name, feature_task in features.items()
        ]

        results = [f.result() for f in futures]

    print(f"All {len(results)} L2 feature managers completed")
```

<!-- section_id: "08a8857e-e571-4dd6-970c-5411ddaca890" -->
### L2 → L3 Delegation (Workers)

```python
#!/usr/bin/env python3
# L2 feature manager: layer_2_features/scripts/spawn_l3.py

import subprocess
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = Path("/home/dawson/dawson-workspace/code/0_layer_universal/0_context")

def spawn_l3_component_worker(component_name, task, tool="codex"):
    """Spawn L3 worker for component implementation."""

    l3_dir = BASE_DIR / "layer_3_components" / component_name
    handoff_path = l3_dir / "hand_off_documents" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l2-to-{component_name}",
        "layer": 3,
        "stage": "implementation",
        "task": task,
        "component": component_name
    }

    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Use codex for L3 implementation (cheaper, faster)
    if tool == "codex":
        agents_md = l3_dir / "AGENTS.md"
        result = subprocess.run(
            [
                "codex",
                "--model", "codestral",
                "--agents-md", str(agents_md),
                "execute-handoff", str(handoff_path)
            ],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout for leaf workers
            cwd=str(l3_dir)
        )
    else:
        # Fallback to Claude for complex components
        result = subprocess.run(
            [
                "claude-code",
                "--working-dir", str(l3_dir),
                "--model", "claude-haiku",
                "process-handoff", str(handoff_path)
            ],
            capture_output=True,
            text=True,
            cwd=str(l3_dir)
        )

    return result

# Example usage
if __name__ == "__main__":
    # Load L2 feature request
    l2_handoff_path = BASE_DIR / "layer_2_features" / "auth-system" / "2.01_manager_handoff_documents" / "incoming.json"
    with open(l2_handoff_path) as f:
        feature_request = json.load(f)

    # Decompose to components
    components = {
        "login-form": "Implement login form UI component",
        "password-reset": "Build password reset flow",
        "session-manager": "Create session management module",
        "auth-api": "Implement authentication API endpoints"
    }

    # Spawn L3 workers (in parallel)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(spawn_l3_component_worker, comp_name, comp_task)
            for comp_name, comp_task in components.items()
        ]

        results = [f.result() for f in futures]

    print(f"All {len(results)} L3 component workers completed")
```

---

<!-- section_id: "b5d440ac-860e-4c46-a60a-880f97d002c8" -->
## Tool Selection Patterns

<!-- section_id: "9e266e9d-382e-44b4-bdf1-2114d70cab82" -->
### Dynamic Tool Selection

```python
def spawn_agent_smart(layer, stage, task, handoff_path):
    """Intelligently select tool based on task characteristics."""

    # Estimate complexity (simplified)
    complexity = estimate_complexity(task)  # Returns 0.0-1.0

    # Select tool based on policy
    if layer <= 2 or complexity > 0.7:
        # Use Claude for managers and complex tasks
        tool = "claude-code"
        model = "claude-sonnet-4.5" if complexity > 0.8 else "claude-haiku"
    elif stage in ["request", "instructions", "planning"]:
        # Use Gemini for planning/reasoning stages
        tool = "gemini"
        model = "gemini-pro-2"
    else:
        # Use Codex for implementation
        tool = "codex"
        model = "codestral"

    # Build command
    if tool == "claude-code":
        cmd = [
            "claude-code",
            "--working-dir", get_layer_dir(layer),
            "--model", model,
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", str(handoff_path)
        ]
    elif tool == "codex":
        cmd = [
            "codex",
            "--model", model,
            "--agents-md", get_agents_md_path(layer),
            "execute-handoff", str(handoff_path)
        ]
    elif tool == "gemini":
        cmd = [
            "gemini",
            "--model", model,
            "--system-file", get_gemini_md_path(layer),
            "process", str(handoff_path)
        ]

    return subprocess.run(cmd, capture_output=True, text=True)
```

<!-- section_id: "14916c40-9fa5-4265-bb95-2d021e17a1e6" -->
### Retry with Escalation

```python
def execute_with_retry_escalation(layer, stage, task, handoff_path, max_retries=3):
    """Execute task, escalating to more powerful tools on failure."""

    # Tool tiers (cheapest to most capable)
    tiers = [
        {"tool": "codex", "model": "codestral"},
        {"tool": "claude-code", "model": "claude-haiku"},
        {"tool": "claude-code", "model": "claude-sonnet-4.5"}
    ]

    for attempt, tier in enumerate(tiers[:max_retries]):
        print(f"Attempt {attempt + 1} with {tier['tool']} ({tier['model']})")

        # Execute
        result = spawn_agent_with_tool(
            layer, stage, task, handoff_path,
            tier["tool"], tier["model"]
        )

        # Check result
        if result.returncode == 0:
            return result

        print(f"Attempt {attempt + 1} failed, escalating...")

    # All attempts failed
    raise RuntimeError(f"Task failed after {max_retries} attempts")
```

---

<!-- section_id: "4a5f9b7d-fd83-45ad-9688-ff8506dfdd1b" -->
## Wrapper Scripts

<!-- section_id: "137438e1-dbcc-404a-ae27-c8d125b28b5b" -->
### Generic Agent Launcher (Bash)

```bash
#!/bin/bash
# launch_agent.sh - Generic agent launcher for WSL/Ubuntu

LAYER=$1
STAGE=$2
HANDOFF=$3
TOOL=${4:-auto}  # auto, claude, codex, gemini

BASE_DIR="/home/dawson/dawson-workspace/code/0_layer_universal/0_context"

# Auto-select tool if not specified
if [ "$TOOL" = "auto" ]; then
  if [ "$LAYER" -le 2 ] || [ "$STAGE" = "criticism" ]; then
    TOOL="claude"
  elif [ "$STAGE" = "request" ] || [ "$STAGE" = "instructions" ] || [ "$STAGE" = "planning" ]; then
    TOOL="gemini"
  else
    TOOL="codex"
  fi
fi

# Determine working directory
if [ "$LAYER" = "0" ]; then
  WORK_DIR="$BASE_DIR/layer_0"
elif [ "$LAYER" = "1" ]; then
  WORK_DIR="$BASE_DIR/layer_1_project"
elif [ "$LAYER" = "2" ]; then
  WORK_DIR="$BASE_DIR/layer_2_features"
elif [ "$LAYER" = "3" ]; then
  WORK_DIR="$BASE_DIR/layer_3_components"
else
  echo "Error: Unknown layer $LAYER"
  exit 1
fi

# Launch appropriate tool
case $TOOL in
  claude)
    claude-code \
      --working-dir "$WORK_DIR" \
      --allowed "B(cla:*,codex:*,gemini:*)" \
      process-handoff "$HANDOFF"
    ;;

  codex)
    codex \
      --model codestral \
      --agents-md "$WORK_DIR/AGENTS.md" \
      execute-handoff "$HANDOFF"
    ;;

  gemini)
    gemini \
      --model gemini-pro-2 \
      --system-file "$WORK_DIR/GEMINI.md" \
      process "$HANDOFF"
    ;;

  *)
    echo "Error: Unknown tool $TOOL"
    exit 1
    ;;
esac
```

**Usage**:
```bash
# Let script choose tool
./launch_agent.sh 2 implementation layer_2_features/auth-system/2.01_manager_handoff_documents/incoming.json

# Force specific tool
./launch_agent.sh 2 implementation layer_2_features/auth-system/2.01_manager_handoff_documents/incoming.json claude
```

<!-- section_id: "e72a3365-9ce2-4201-aaa4-2c04527ad292" -->
### Parallel Launcher (Bash)

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
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    echo "Warning: Agent PID $PID failed with status $STATUS"
  fi
done

echo "All agents completed"
```

**Usage**:
```bash
./parallel_launch.sh 3 implementation \
  layer_3_components/login-form/hand_off_documents/incoming.json \
  layer_3_components/password-reset/hand_off_documents/incoming.json \
  layer_3_components/session-manager/hand_off_documents/incoming.json
```

---

<!-- section_id: "8cf1c0f3-d96a-446c-8e7f-b9a55024a06f" -->
## OS-Specific Adaptations

<!-- section_id: "bc04c0f7-edb0-4b78-87c8-c92d689fd08f" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "56b9f9e9-bd11-4251-8746-85374d26bb8c" -->
### Windows (PowerShell)
```powershell
# PowerShell equivalent of bash launcher
param(
    [int]$Layer,
    [string]$Stage,
    [string]$Handoff,
    [string]$Tool = "auto"
)

$BaseDir = "C:\Users\YourName\code\0_ai_context\0_context"

# Auto-select tool
if ($Tool -eq "auto") {
    if ($Layer -le 2 -or $Stage -eq "criticism") {
        $Tool = "claude"
    } elseif ($Stage -eq "request" -or $Stage -eq "instructions") {
        $Tool = "gemini"
    } else {
        $Tool = "codex"
    }
}

# Launch tool
switch ($Tool) {
    "claude" {
        & claude-code --working-dir "$BaseDir\layer_$Layer" `
                      --allowed "B(cla:*,codex:*,gemini:*)" `
                      process-handoff "$Handoff"
    }
    "codex" {
        & codex --model codestral `
                --agents-md "$BaseDir\layer_$Layer\AGENTS.md" `
                execute-handoff "$Handoff"
    }
    "gemini" {
        & gemini --model gemini-pro-2 `
                 --system-file "$BaseDir\layer_$Layer\GEMINI.md" `
                 process "$Handoff"
    }
}
```

<!-- section_id: "870f8169-5dc3-48a8-9bbe-63b3e7804dd6" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "13cbf76e-854a-4678-901d-0f0ea4248ef7" -->
## Related Documentation

**Within 0_ai_context**:
- **Framework Orchestration**: `sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`
- **Handoff Schema**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **OS Variants (Quartets)**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`
- **Tool Context Systems**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md`

**Normative Specification**:
- **CLI Recursion (Detailed)**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`
- **Architecture**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Parallel Execution**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md`

---

<!-- section_id: "48ffdc62-9894-485d-8a3f-1d01253aa39b" -->
## Summary

CLI recursion enables deep agent hierarchies:

1. **Explicit Commands**: Use `claude-code --allowed "B(...)"` to enable recursion
2. **Handoff-Driven**: Each level reads incoming, processes, writes outgoing
3. **Tool Selection**: Use different tools at different layers (Claude for managers, Codex for workers, Gemini for planning)
4. **Parallel Execution**: Spawn multiple agents concurrently via background processes
5. **Error Handling**: Retry with escalation to more powerful models
6. **OS Adaptation**: Adjust paths and shell syntax for target OS (WSL, Windows, macOS)

This pattern is framework-agnostic and works with any CLI-based agent tool that can:
- Accept a working directory
- Load context files (CLAUDE.md, AGENTS.md, GEMINI.md)
- Read/write handoff files
- Optionally spawn subprocesses

---

<!-- section_id: "c706a558-1c06-45b8-8b99-79e4ecd2cf62" -->
## Legacy Universal Protocols Source

# CLI Recursion Syntax and Patterns

<!-- section_id: "fbc8187f-4c79-497b-8ab2-d2efe15b0c1e" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "4fae6b50-dd4b-4ef9-b2b8-dfc875dc1599" -->
## Overview

This document provides concrete CLI recursion patterns for creating deep agent hierarchies. CLI recursion allows agents to spawn other agents by invoking CLI commands, enabling arbitrary depth hierarchies without framework-specific APIs.

**Current Environment**:
- **OS**: WSL (Windows Subsystem for Linux), Linux Ubuntu
- **Shell**: bash
- **CLI Tools**: Claude Code, Codex CLI, Gemini CLI
- **Working Directory**: `/home/dawson/code/0_layer_universal/0_context/`

For the normative specification with additional patterns and examples, see:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`

---

<!-- section_id: "46963b88-99a3-4320-9102-6f3560f0a445" -->
## Core Concept

**CLI Recursion Pattern**:
```
L0 Manager (claude-code)
  → spawns L1 Manager (claude-code in L1 directory)
    → spawns L2 Manager (claude-code in L2 directory)
      → spawns L3 Workers (codex, gemini, claude-code)
```

Each invocation:
1. Loads appropriate layer context (CLAUDE.md, AGENTS.md, GEMINI.md)
2. Reads incoming handoff from `*/manager_handoff_documents/incoming.json` or `*/hand_off_documents/incoming.json`
3. Executes work
4. Writes outgoing handoff
5. Optionally spawns deeper agents

---

<!-- section_id: "8582c505-bdec-446a-900f-df5eaac3078c" -->
## Claude Code Recursion Syntax

<!-- section_id: "5eda9b55-fbd2-46f2-9e6d-083bc891474a" -->
### Basic Recursive Call

```bash
# L0 manager spawning L1 manager
cd /home/dawson/code/0_layer_universal/0_context/layer_1_project

claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_1_project" \
  --allowed "B(cla:*)" \
  process-handoff 1.01_manager_handoff_documents/1.00_to_universal/incoming.json
```

**Flags Explained**:
- `--working-dir`: Sets working directory (loads CLAUDE.md from there)
- `--allowed "B(cla:*)`: Allows subprocess to call "claude" binary (enables recursive calls)
- `process-handoff`: Command to process a handoff file

<!-- section_id: "998926f4-a3af-4020-a776-7464312c8dc5" -->
### Permission Patterns

**Allow Specific Tools**:
```bash
# Allow subprocess to call claude-code and codex
claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_2_features" \
  --allowed "B(cla:*,codex:*)" \
  process-handoff 2.01_manager_handoff_documents/incoming.json
```

**Full Recursion** (use with caution):
```bash
# Allow subprocess to call any binary
claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_1_project" \
  --allowed "B(*)" \
  process-handoff 1.01_manager_handoff_documents/incoming.json
```

**Read-Only** (no subprocess execution):
```bash
# No subprocess binary execution allowed
claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_3_components" \
  process-handoff 3.01_manager_handoff_documents/incoming.json
```

---

<!-- section_id: "d20d4c3e-ff69-4626-b478-2a90c279eed3" -->
## Handoff-Based Recursion

<!-- section_id: "53bdcf99-68b9-4e6a-8c98-74433a611d13" -->
### Bash Script Example: L1 Manager

```bash
#!/bin/bash
# L1 manager script: layer_1_project/scripts/process_handoff.sh

# Path to L1 layer
L1_DIR="/home/dawson/code/0_layer_universal/0_context/layer_1_project"

# Read incoming handoff
HANDOFF_FILE="$L1_DIR/1.01_manager_handoff_documents/1.00_to_universal/incoming.json"
HANDOFF=$(cat "$HANDOFF_FILE")
TASK=$(echo "$HANDOFF" | jq -r '.task')

echo "L1 Manager processing: $TASK"

# Decompose into L2 features
FEATURES=$(echo "$HANDOFF" | jq -r '.features[]')

# Spawn L2 manager for each feature
for FEATURE in $FEATURES; do
  echo "Spawning L2 manager for feature: $FEATURE"

  L2_DIR="/home/dawson/code/0_layer_universal/0_context/layer_2_features/$FEATURE"

  # Create L2 handoff
  cat > "$L2_DIR/2.01_manager_handoff_documents/incoming.json" <<EOF
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-$FEATURE-$(date +%s)",
  "layer": 2,
  "parent_id": "$(echo "$HANDOFF" | jq -r '.id')",
  "task": "Implement $FEATURE feature",
  "constraints": $(echo "$HANDOFF" | jq -r '.constraints')
}
EOF

  # Spawn L2 manager in background (parallel execution)
  (
    cd "$L2_DIR"
    claude-code \
      --working-dir "$L2_DIR" \
      --allowed "B(cla:*,codex:*)" \
      process-handoff 2.01_manager_handoff_documents/incoming.json
  ) &
done

# Wait for all L2 managers
wait

echo "All L2 managers completed"

# Aggregate results into L1 outgoing handoff
# (Implementation would collect L2 outgoing handoffs and synthesize L1 result)
```

---

<!-- section_id: "e635f317-96c6-42ea-9b3e-f11cf20cfe4e" -->
## Multi-Layer Examples

<!-- section_id: "9c563d65-6994-4850-81f5-de2ace0fe64f" -->
### L0 → L1 Delegation (Python)

```python
#!/usr/bin/env python3
# L0 universal manager: layer_0/scripts/spawn_l1.py

import subprocess
import json
from pathlib import Path

BASE_DIR = Path("/home/dawson/code/0_layer_universal/0_context")

def spawn_l1_project_manager(project_name, task, constraints):
    """Spawn L1 manager for specific project."""

    l1_dir = BASE_DIR / "layer_1_project" / project_name
    handoff_path = l1_dir / "1.01_manager_handoff_documents" / "1.00_to_universal" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l0-to-{project_name}",
        "layer": 1,
        "task": task,
        "constraints": constraints,
        "project": project_name
    }

    # Write handoff
    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Spawn L1 manager
    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", str(l1_dir),
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", str(handoff_path)
        ],
        capture_output=True,
        text=True,
        cwd=str(l1_dir)
    )

    return result

# Example usage
if __name__ == "__main__":
    # Load universal request
    l0_handoff_path = BASE_DIR / "layer_0" / "0.01_manager_handoff_documents" / "incoming.json"
    with open(l0_handoff_path) as f:
        universal_request = json.load(f)

    # Decompose to projects (simplified example)
    projects = {
        "ecommerce": "Build product catalog and shopping cart",
        "math-automation": "Automate homework processing and grading"
    }

    # Spawn L1 for each project
    for project_name, project_task in projects.items():
        print(f"Spawning L1 manager for project: {project_name}")
        result = spawn_l1_project_manager(
            project_name,
            project_task,
            universal_request.get("constraints", [])
        )
        print(f"L1 {project_name} completed with status: {result.returncode}")
```

<!-- section_id: "a3435723-f545-48d4-9f80-1390352f22c9" -->
### L1 → L2 Delegation (Python)

```python
#!/usr/bin/env python3
# L1 project manager: layer_1_project/scripts/spawn_l2.py

import subprocess
import json
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

BASE_DIR = Path("/home/dawson/code/0_layer_universal/0_context")
L1_DIR = BASE_DIR / "layer_1_project"

def spawn_l2_feature_manager(feature_name, task, constraints):
    """Spawn L2 manager for specific feature."""

    l2_dir = BASE_DIR / "layer_2_features" / feature_name
    handoff_path = l2_dir / "2.01_manager_handoff_documents" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l1-to-{feature_name}",
        "layer": 2,
        "task": task,
        "constraints": constraints,
        "feature": feature_name
    }

    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", str(l2_dir),
            "--allowed", "B(cla:*,codex:*)",
            "--output-style", "feature-manager",  # Optional persona
            "process-handoff", str(handoff_path)
        ],
        capture_output=True,
        text=True,
        cwd=str(l2_dir)
    )

    return result

# Example usage with parallel execution
if __name__ == "__main__":
    # Load L1 request
    l1_handoff_path = L1_DIR / "1.01_manager_handoff_documents" / "1.00_to_universal" / "incoming.json"
    with open(l1_handoff_path) as f:
        project_request = json.load(f)

    # Decompose to features
    features = {
        "auth-system": "Implement user authentication and authorization",
        "shopping-cart": "Build shopping cart with persistent storage",
        "payment-integration": "Integrate Stripe payment processing"
    }

    # Spawn L2 for each feature (in parallel)
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(
                spawn_l2_feature_manager,
                feature_name,
                feature_task,
                project_request.get("constraints", [])
            )
            for feature_name, feature_task in features.items()
        ]

        results = [f.result() for f in futures]

    print(f"All {len(results)} L2 feature managers completed")
```

<!-- section_id: "e7e8f4fc-3e0b-4a1b-b315-4fc297209dc1" -->
### L2 → L3 Delegation (Workers)

```python
#!/usr/bin/env python3
# L2 feature manager: layer_2_features/scripts/spawn_l3.py

import subprocess
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = Path("/home/dawson/code/0_layer_universal/0_context")

def spawn_l3_component_worker(component_name, task, tool="codex"):
    """Spawn L3 worker for component implementation."""

    l3_dir = BASE_DIR / "layer_3_components" / component_name
    handoff_path = l3_dir / "hand_off_documents" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l2-to-{component_name}",
        "layer": 3,
        "stage": "implementation",
        "task": task,
        "component": component_name
    }

    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Use codex for L3 implementation (cheaper, faster)
    if tool == "codex":
        agents_md = l3_dir / "AGENTS.md"
        result = subprocess.run(
            [
                "codex",
                "--model", "codestral",
                "--agents-md", str(agents_md),
                "execute-handoff", str(handoff_path)
            ],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout for leaf workers
            cwd=str(l3_dir)
        )
    else:
        # Fallback to Claude for complex components
        result = subprocess.run(
            [
                "claude-code",
                "--working-dir", str(l3_dir),
                "--model", "claude-haiku",
                "process-handoff", str(handoff_path)
            ],
            capture_output=True,
            text=True,
            cwd=str(l3_dir)
        )

    return result

# Example usage
if __name__ == "__main__":
    # Load L2 feature request
    l2_handoff_path = BASE_DIR / "layer_2_features" / "auth-system" / "2.01_manager_handoff_documents" / "incoming.json"
    with open(l2_handoff_path) as f:
        feature_request = json.load(f)

    # Decompose to components
    components = {
        "login-form": "Implement login form UI component",
        "password-reset": "Build password reset flow",
        "session-manager": "Create session management module",
        "auth-api": "Implement authentication API endpoints"
    }

    # Spawn L3 workers (in parallel)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(spawn_l3_component_worker, comp_name, comp_task)
            for comp_name, comp_task in components.items()
        ]

        results = [f.result() for f in futures]

    print(f"All {len(results)} L3 component workers completed")
```

---

<!-- section_id: "4ae0a9a4-7d58-4e69-b5e3-4215ae1c2a43" -->
## Tool Selection Patterns

<!-- section_id: "fb52842c-5bb2-4b31-97a4-42a5cd723ce5" -->
### Dynamic Tool Selection

```python
def spawn_agent_smart(layer, stage, task, handoff_path):
    """Intelligently select tool based on task characteristics."""

    # Estimate complexity (simplified)
    complexity = estimate_complexity(task)  # Returns 0.0-1.0

    # Select tool based on policy
    if layer <= 2 or complexity > 0.7:
        # Use Claude for managers and complex tasks
        tool = "claude-code"
        model = "claude-sonnet-4.5" if complexity > 0.8 else "claude-haiku"
    elif stage in ["request", "instructions", "planning"]:
        # Use Gemini for planning/reasoning stages
        tool = "gemini"
        model = "gemini-pro-2"
    else:
        # Use Codex for implementation
        tool = "codex"
        model = "codestral"

    # Build command
    if tool == "claude-code":
        cmd = [
            "claude-code",
            "--working-dir", get_layer_dir(layer),
            "--model", model,
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", str(handoff_path)
        ]
    elif tool == "codex":
        cmd = [
            "codex",
            "--model", model,
            "--agents-md", get_agents_md_path(layer),
            "execute-handoff", str(handoff_path)
        ]
    elif tool == "gemini":
        cmd = [
            "gemini",
            "--model", model,
            "--system-file", get_gemini_md_path(layer),
            "process", str(handoff_path)
        ]

    return subprocess.run(cmd, capture_output=True, text=True)
```

<!-- section_id: "de6ab1ee-1fee-4e94-b7b6-8835dd759199" -->
### Retry with Escalation

```python
def execute_with_retry_escalation(layer, stage, task, handoff_path, max_retries=3):
    """Execute task, escalating to more powerful tools on failure."""

    # Tool tiers (cheapest to most capable)
    tiers = [
        {"tool": "codex", "model": "codestral"},
        {"tool": "claude-code", "model": "claude-haiku"},
        {"tool": "claude-code", "model": "claude-sonnet-4.5"}
    ]

    for attempt, tier in enumerate(tiers[:max_retries]):
        print(f"Attempt {attempt + 1} with {tier['tool']} ({tier['model']})")

        # Execute
        result = spawn_agent_with_tool(
            layer, stage, task, handoff_path,
            tier["tool"], tier["model"]
        )

        # Check result
        if result.returncode == 0:
            return result

        print(f"Attempt {attempt + 1} failed, escalating...")

    # All attempts failed
    raise RuntimeError(f"Task failed after {max_retries} attempts")
```

---

<!-- section_id: "84e274d7-578c-4bef-8f8d-0c9053130f76" -->
## Wrapper Scripts

<!-- section_id: "319ec0cd-4ed1-4fee-84e1-0f5cc70651db" -->
### Generic Agent Launcher (Bash)

```bash
#!/bin/bash
# launch_agent.sh - Generic agent launcher for WSL/Ubuntu

LAYER=$1
STAGE=$2
HANDOFF=$3
TOOL=${4:-auto}  # auto, claude, codex, gemini

BASE_DIR="/home/dawson/code/0_layer_universal/0_context"

# Auto-select tool if not specified
if [ "$TOOL" = "auto" ]; then
  if [ "$LAYER" -le 2 ] || [ "$STAGE" = "criticism" ]; then
    TOOL="claude"
  elif [ "$STAGE" = "request" ] || [ "$STAGE" = "instructions" ] || [ "$STAGE" = "planning" ]; then
    TOOL="gemini"
  else
    TOOL="codex"
  fi
fi

# Determine working directory
if [ "$LAYER" = "0" ]; then
  WORK_DIR="$BASE_DIR/layer_0"
elif [ "$LAYER" = "1" ]; then
  WORK_DIR="$BASE_DIR/layer_1_project"
elif [ "$LAYER" = "2" ]; then
  WORK_DIR="$BASE_DIR/layer_2_features"
elif [ "$LAYER" = "3" ]; then
  WORK_DIR="$BASE_DIR/layer_3_components"
else
  echo "Error: Unknown layer $LAYER"
  exit 1
fi

# Launch appropriate tool
case $TOOL in
  claude)
    claude-code \
      --working-dir "$WORK_DIR" \
      --allowed "B(cla:*,codex:*,gemini:*)" \
      process-handoff "$HANDOFF"
    ;;

  codex)
    codex \
      --model codestral \
      --agents-md "$WORK_DIR/AGENTS.md" \
      execute-handoff "$HANDOFF"
    ;;

  gemini)
    gemini \
      --model gemini-pro-2 \
      --system-file "$WORK_DIR/GEMINI.md" \
      process "$HANDOFF"
    ;;

  *)
    echo "Error: Unknown tool $TOOL"
    exit 1
    ;;
esac
```

**Usage**:
```bash
# Let script choose tool
./launch_agent.sh 2 implementation layer_2_features/auth-system/2.01_manager_handoff_documents/incoming.json

# Force specific tool
./launch_agent.sh 2 implementation layer_2_features/auth-system/2.01_manager_handoff_documents/incoming.json claude
```

<!-- section_id: "d544531d-3423-4771-bc08-4c4cf539c0ab" -->
### Parallel Launcher (Bash)

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
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    echo "Warning: Agent PID $PID failed with status $STATUS"
  fi
done

echo "All agents completed"
```

**Usage**:
```bash
./parallel_launch.sh 3 implementation \
  layer_3_components/login-form/hand_off_documents/incoming.json \
  layer_3_components/password-reset/hand_off_documents/incoming.json \
  layer_3_components/session-manager/hand_off_documents/incoming.json
```

---

<!-- section_id: "7e24b4d9-013b-4a9a-a2ad-f074040d878e" -->
## OS-Specific Adaptations

<!-- section_id: "94fe7174-12f6-4210-b9ba-41031df18cfe" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "8b0092ed-6cd3-4fca-a622-44db068dc942" -->
### Windows (PowerShell)
```powershell
# PowerShell equivalent of bash launcher
param(
    [int]$Layer,
    [string]$Stage,
    [string]$Handoff,
    [string]$Tool = "auto"
)

$BaseDir = "C:\Users\YourName\code\0_ai_context\0_context"

# Auto-select tool
if ($Tool -eq "auto") {
    if ($Layer -le 2 -or $Stage -eq "criticism") {
        $Tool = "claude"
    } elseif ($Stage -eq "request" -or $Stage -eq "instructions") {
        $Tool = "gemini"
    } else {
        $Tool = "codex"
    }
}

# Launch tool
switch ($Tool) {
    "claude" {
        & claude-code --working-dir "$BaseDir\layer_$Layer" `
                      --allowed "B(cla:*,codex:*,gemini:*)" `
                      process-handoff "$Handoff"
    }
    "codex" {
        & codex --model codestral `
                --agents-md "$BaseDir\layer_$Layer\AGENTS.md" `
                execute-handoff "$Handoff"
    }
    "gemini" {
        & gemini --model gemini-pro-2 `
                 --system-file "$BaseDir\layer_$Layer\GEMINI.md" `
                 process "$Handoff"
    }
}
```

<!-- section_id: "e541211f-7b3e-4775-b9c6-2574028aab4a" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "e7daa9db-0d89-4264-80e0-b3dff0dab380" -->
## Related Documentation

**Within 0_ai_context**:
- **Framework Orchestration**: `sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`
- **Handoff Schema**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **OS Variants (Quartets)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`
- **Tool Context Systems**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md`

**Normative Specification**:
- **CLI Recursion (Detailed)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`
- **Architecture**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Parallel Execution**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md`

---

<!-- section_id: "99d2ecfd-f3f0-4ab3-975e-109edaeca2a4" -->
## Summary

CLI recursion enables deep agent hierarchies:

1. **Explicit Commands**: Use `claude-code --allowed "B(...)"` to enable recursion
2. **Handoff-Driven**: Each level reads incoming, processes, writes outgoing
3. **Tool Selection**: Use different tools at different layers (Claude for managers, Codex for workers, Gemini for planning)
4. **Parallel Execution**: Spawn multiple agents concurrently via background processes
5. **Error Handling**: Retry with escalation to more powerful models
6. **OS Adaptation**: Adjust paths and shell syntax for target OS (WSL, Windows, macOS)

This pattern is framework-agnostic and works with any CLI-based agent tool that can:
- Accept a working directory
- Load context files (CLAUDE.md, AGENTS.md, GEMINI.md)
- Read/write handoff files
- Optionally spawn subprocesses


---

<!-- section_id: "c22dcfce-5dd3-4c31-94c5-6b242d6ff51b" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`

# CLI Recursion Syntax and Patterns

<!-- section_id: "d85abeeb-f236-4db0-bc70-ae38b10ad866" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "f1a3e043-ba2b-4d9d-90d5-5045b965e8e7" -->
## Overview

This document provides concrete CLI recursion patterns for creating deep agent hierarchies. CLI recursion allows agents to spawn other agents by invoking CLI commands, enabling arbitrary depth hierarchies without framework-specific APIs.

**Current Environment**:
- **OS**: WSL (Windows Subsystem for Linux), Linux Ubuntu
- **Shell**: bash
- **CLI Tools**: Claude Code, Codex CLI, Gemini CLI
- **Working Directory**: `/home/dawson/code/0_layer_universal/0_context/`

For the normative specification with additional patterns and examples, see:
- **Normative Spec**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`

---

<!-- section_id: "de39d81e-e8ae-4f43-9c5f-c2f73e6a130a" -->
## Core Concept

**CLI Recursion Pattern**:
```
L0 Manager (claude-code)
  → spawns L1 Manager (claude-code in L1 directory)
    → spawns L2 Manager (claude-code in L2 directory)
      → spawns L3 Workers (codex, gemini, claude-code)
```

Each invocation:
1. Loads appropriate layer context (CLAUDE.md, AGENTS.md, GEMINI.md)
2. Reads incoming handoff from `*/manager_handoff_documents/incoming.json` or `*/hand_off_documents/incoming.json`
3. Executes work
4. Writes outgoing handoff
5. Optionally spawns deeper agents

---

<!-- section_id: "a30f90d2-a822-42df-a642-bf0ca0bc0846" -->
## Claude Code Recursion Syntax

<!-- section_id: "258f7aaa-5b30-4ad4-8d81-9ad94042d162" -->
### Basic Recursive Call

```bash
# L0 manager spawning L1 manager
cd /home/dawson/code/0_layer_universal/0_context/layer_1_project

claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_1_project" \
  --allowed "B(cla:*)" \
  process-handoff 1.01_manager_handoff_documents/1.00_to_universal/incoming.json
```

**Flags Explained**:
- `--working-dir`: Sets working directory (loads CLAUDE.md from there)
- `--allowed "B(cla:*)`: Allows subprocess to call "claude" binary (enables recursive calls)
- `process-handoff`: Command to process a handoff file

<!-- section_id: "efe68448-788e-43d5-8051-decd8b3c7b56" -->
### Permission Patterns

**Allow Specific Tools**:
```bash
# Allow subprocess to call claude-code and codex
claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_2_features" \
  --allowed "B(cla:*,codex:*)" \
  process-handoff 2.01_manager_handoff_documents/incoming.json
```

**Full Recursion** (use with caution):
```bash
# Allow subprocess to call any binary
claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_1_project" \
  --allowed "B(*)" \
  process-handoff 1.01_manager_handoff_documents/incoming.json
```

**Read-Only** (no subprocess execution):
```bash
# No subprocess binary execution allowed
claude-code \
  --working-dir "/home/dawson/code/0_layer_universal/0_context/layer_3_components" \
  process-handoff 3.01_manager_handoff_documents/incoming.json
```

---

<!-- section_id: "216670b2-6ccb-4ca0-9cea-ca339e1a6c39" -->
## Handoff-Based Recursion

<!-- section_id: "267bfef2-b918-4b7c-9d7d-b7a7fd027bc4" -->
### Bash Script Example: L1 Manager

```bash
#!/bin/bash
# L1 manager script: layer_1_project/scripts/process_handoff.sh

# Path to L1 layer
L1_DIR="/home/dawson/code/0_layer_universal/0_context/layer_1_project"

# Read incoming handoff
HANDOFF_FILE="$L1_DIR/1.01_manager_handoff_documents/1.00_to_universal/incoming.json"
HANDOFF=$(cat "$HANDOFF_FILE")
TASK=$(echo "$HANDOFF" | jq -r '.task')

echo "L1 Manager processing: $TASK"

# Decompose into L2 features
FEATURES=$(echo "$HANDOFF" | jq -r '.features[]')

# Spawn L2 manager for each feature
for FEATURE in $FEATURES; do
  echo "Spawning L2 manager for feature: $FEATURE"

  L2_DIR="/home/dawson/code/0_layer_universal/0_context/layer_2_features/$FEATURE"

  # Create L2 handoff
  cat > "$L2_DIR/2.01_manager_handoff_documents/incoming.json" <<EOF
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-$FEATURE-$(date +%s)",
  "layer": 2,
  "parent_id": "$(echo "$HANDOFF" | jq -r '.id')",
  "task": "Implement $FEATURE feature",
  "constraints": $(echo "$HANDOFF" | jq -r '.constraints')
}
EOF

  # Spawn L2 manager in background (parallel execution)
  (
    cd "$L2_DIR"
    claude-code \
      --working-dir "$L2_DIR" \
      --allowed "B(cla:*,codex:*)" \
      process-handoff 2.01_manager_handoff_documents/incoming.json
  ) &
done

# Wait for all L2 managers
wait

echo "All L2 managers completed"

# Aggregate results into L1 outgoing handoff
# (Implementation would collect L2 outgoing handoffs and synthesize L1 result)
```

---

<!-- section_id: "563b1d46-47a7-407e-833b-71464c0675de" -->
## Multi-Layer Examples

<!-- section_id: "81141a93-94b6-45f5-98e1-a5e22b4d2e8a" -->
### L0 → L1 Delegation (Python)

```python
#!/usr/bin/env python3
# L0 universal manager: layer_0/scripts/spawn_l1.py

import subprocess
import json
from pathlib import Path

BASE_DIR = Path("/home/dawson/code/0_layer_universal/0_context")

def spawn_l1_project_manager(project_name, task, constraints):
    """Spawn L1 manager for specific project."""

    l1_dir = BASE_DIR / "layer_1_project" / project_name
    handoff_path = l1_dir / "1.01_manager_handoff_documents" / "1.00_to_universal" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l0-to-{project_name}",
        "layer": 1,
        "task": task,
        "constraints": constraints,
        "project": project_name
    }

    # Write handoff
    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Spawn L1 manager
    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", str(l1_dir),
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", str(handoff_path)
        ],
        capture_output=True,
        text=True,
        cwd=str(l1_dir)
    )

    return result

# Example usage
if __name__ == "__main__":
    # Load universal request
    l0_handoff_path = BASE_DIR / "layer_0" / "0.01_manager_handoff_documents" / "incoming.json"
    with open(l0_handoff_path) as f:
        universal_request = json.load(f)

    # Decompose to projects (simplified example)
    projects = {
        "ecommerce": "Build product catalog and shopping cart",
        "math-automation": "Automate homework processing and grading"
    }

    # Spawn L1 for each project
    for project_name, project_task in projects.items():
        print(f"Spawning L1 manager for project: {project_name}")
        result = spawn_l1_project_manager(
            project_name,
            project_task,
            universal_request.get("constraints", [])
        )
        print(f"L1 {project_name} completed with status: {result.returncode}")
```

<!-- section_id: "6a987643-a625-45f4-8c07-734e193f7a3d" -->
### L1 → L2 Delegation (Python)

```python
#!/usr/bin/env python3
# L1 project manager: layer_1_project/scripts/spawn_l2.py

import subprocess
import json
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

BASE_DIR = Path("/home/dawson/code/0_layer_universal/0_context")
L1_DIR = BASE_DIR / "layer_1_project"

def spawn_l2_feature_manager(feature_name, task, constraints):
    """Spawn L2 manager for specific feature."""

    l2_dir = BASE_DIR / "layer_2_features" / feature_name
    handoff_path = l2_dir / "2.01_manager_handoff_documents" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l1-to-{feature_name}",
        "layer": 2,
        "task": task,
        "constraints": constraints,
        "feature": feature_name
    }

    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    result = subprocess.run(
        [
            "claude-code",
            "--working-dir", str(l2_dir),
            "--allowed", "B(cla:*,codex:*)",
            "--output-style", "feature-manager",  # Optional persona
            "process-handoff", str(handoff_path)
        ],
        capture_output=True,
        text=True,
        cwd=str(l2_dir)
    )

    return result

# Example usage with parallel execution
if __name__ == "__main__":
    # Load L1 request
    l1_handoff_path = L1_DIR / "1.01_manager_handoff_documents" / "1.00_to_universal" / "incoming.json"
    with open(l1_handoff_path) as f:
        project_request = json.load(f)

    # Decompose to features
    features = {
        "auth-system": "Implement user authentication and authorization",
        "shopping-cart": "Build shopping cart with persistent storage",
        "payment-integration": "Integrate Stripe payment processing"
    }

    # Spawn L2 for each feature (in parallel)
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(
                spawn_l2_feature_manager,
                feature_name,
                feature_task,
                project_request.get("constraints", [])
            )
            for feature_name, feature_task in features.items()
        ]

        results = [f.result() for f in futures]

    print(f"All {len(results)} L2 feature managers completed")
```

<!-- section_id: "995a7828-164a-4910-9147-fb97f8cfe1cf" -->
### L2 → L3 Delegation (Workers)

```python
#!/usr/bin/env python3
# L2 feature manager: layer_2_features/scripts/spawn_l3.py

import subprocess
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = Path("/home/dawson/code/0_layer_universal/0_context")

def spawn_l3_component_worker(component_name, task, tool="codex"):
    """Spawn L3 worker for component implementation."""

    l3_dir = BASE_DIR / "layer_3_components" / component_name
    handoff_path = l3_dir / "hand_off_documents" / "incoming.json"

    handoff = {
        "schemaVersion": "1.0.0",
        "id": f"handoff-l2-to-{component_name}",
        "layer": 3,
        "stage": "implementation",
        "task": task,
        "component": component_name
    }

    handoff_path.parent.mkdir(parents=True, exist_ok=True)
    with open(handoff_path, "w") as f:
        json.dump(handoff, f, indent=2)

    # Use codex for L3 implementation (cheaper, faster)
    if tool == "codex":
        agents_md = l3_dir / "AGENTS.md"
        result = subprocess.run(
            [
                "codex",
                "--model", "codestral",
                "--agents-md", str(agents_md),
                "execute-handoff", str(handoff_path)
            ],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout for leaf workers
            cwd=str(l3_dir)
        )
    else:
        # Fallback to Claude for complex components
        result = subprocess.run(
            [
                "claude-code",
                "--working-dir", str(l3_dir),
                "--model", "claude-haiku",
                "process-handoff", str(handoff_path)
            ],
            capture_output=True,
            text=True,
            cwd=str(l3_dir)
        )

    return result

# Example usage
if __name__ == "__main__":
    # Load L2 feature request
    l2_handoff_path = BASE_DIR / "layer_2_features" / "auth-system" / "2.01_manager_handoff_documents" / "incoming.json"
    with open(l2_handoff_path) as f:
        feature_request = json.load(f)

    # Decompose to components
    components = {
        "login-form": "Implement login form UI component",
        "password-reset": "Build password reset flow",
        "session-manager": "Create session management module",
        "auth-api": "Implement authentication API endpoints"
    }

    # Spawn L3 workers (in parallel)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(spawn_l3_component_worker, comp_name, comp_task)
            for comp_name, comp_task in components.items()
        ]

        results = [f.result() for f in futures]

    print(f"All {len(results)} L3 component workers completed")
```

---

<!-- section_id: "99c768e0-b4d4-4ecf-9780-3a5cf78faa0a" -->
## Tool Selection Patterns

<!-- section_id: "88f03004-666a-43a0-8378-ae971ab5442a" -->
### Dynamic Tool Selection

```python
def spawn_agent_smart(layer, stage, task, handoff_path):
    """Intelligently select tool based on task characteristics."""

    # Estimate complexity (simplified)
    complexity = estimate_complexity(task)  # Returns 0.0-1.0

    # Select tool based on policy
    if layer <= 2 or complexity > 0.7:
        # Use Claude for managers and complex tasks
        tool = "claude-code"
        model = "claude-sonnet-4.5" if complexity > 0.8 else "claude-haiku"
    elif stage in ["request", "instructions", "planning"]:
        # Use Gemini for planning/reasoning stages
        tool = "gemini"
        model = "gemini-pro-2"
    else:
        # Use Codex for implementation
        tool = "codex"
        model = "codestral"

    # Build command
    if tool == "claude-code":
        cmd = [
            "claude-code",
            "--working-dir", get_layer_dir(layer),
            "--model", model,
            "--allowed", "B(cla:*,codex:*,gemini:*)",
            "process-handoff", str(handoff_path)
        ]
    elif tool == "codex":
        cmd = [
            "codex",
            "--model", model,
            "--agents-md", get_agents_md_path(layer),
            "execute-handoff", str(handoff_path)
        ]
    elif tool == "gemini":
        cmd = [
            "gemini",
            "--model", model,
            "--system-file", get_gemini_md_path(layer),
            "process", str(handoff_path)
        ]

    return subprocess.run(cmd, capture_output=True, text=True)
```

<!-- section_id: "0cd70589-4fc1-4069-9a11-235d35fd91ee" -->
### Retry with Escalation

```python
def execute_with_retry_escalation(layer, stage, task, handoff_path, max_retries=3):
    """Execute task, escalating to more powerful tools on failure."""

    # Tool tiers (cheapest to most capable)
    tiers = [
        {"tool": "codex", "model": "codestral"},
        {"tool": "claude-code", "model": "claude-haiku"},
        {"tool": "claude-code", "model": "claude-sonnet-4.5"}
    ]

    for attempt, tier in enumerate(tiers[:max_retries]):
        print(f"Attempt {attempt + 1} with {tier['tool']} ({tier['model']})")

        # Execute
        result = spawn_agent_with_tool(
            layer, stage, task, handoff_path,
            tier["tool"], tier["model"]
        )

        # Check result
        if result.returncode == 0:
            return result

        print(f"Attempt {attempt + 1} failed, escalating...")

    # All attempts failed
    raise RuntimeError(f"Task failed after {max_retries} attempts")
```

---

<!-- section_id: "f92f1a19-d685-441c-ba7b-e4351b59ff8c" -->
## Wrapper Scripts

<!-- section_id: "3950863f-7d89-4e21-bcae-bd3874f04781" -->
### Generic Agent Launcher (Bash)

```bash
#!/bin/bash
# launch_agent.sh - Generic agent launcher for WSL/Ubuntu

LAYER=$1
STAGE=$2
HANDOFF=$3
TOOL=${4:-auto}  # auto, claude, codex, gemini

BASE_DIR="/home/dawson/code/0_layer_universal/0_context"

# Auto-select tool if not specified
if [ "$TOOL" = "auto" ]; then
  if [ "$LAYER" -le 2 ] || [ "$STAGE" = "criticism" ]; then
    TOOL="claude"
  elif [ "$STAGE" = "request" ] || [ "$STAGE" = "instructions" ] || [ "$STAGE" = "planning" ]; then
    TOOL="gemini"
  else
    TOOL="codex"
  fi
fi

# Determine working directory
if [ "$LAYER" = "0" ]; then
  WORK_DIR="$BASE_DIR/layer_0"
elif [ "$LAYER" = "1" ]; then
  WORK_DIR="$BASE_DIR/layer_1_project"
elif [ "$LAYER" = "2" ]; then
  WORK_DIR="$BASE_DIR/layer_2_features"
elif [ "$LAYER" = "3" ]; then
  WORK_DIR="$BASE_DIR/layer_3_components"
else
  echo "Error: Unknown layer $LAYER"
  exit 1
fi

# Launch appropriate tool
case $TOOL in
  claude)
    claude-code \
      --working-dir "$WORK_DIR" \
      --allowed "B(cla:*,codex:*,gemini:*)" \
      process-handoff "$HANDOFF"
    ;;

  codex)
    codex \
      --model codestral \
      --agents-md "$WORK_DIR/AGENTS.md" \
      execute-handoff "$HANDOFF"
    ;;

  gemini)
    gemini \
      --model gemini-pro-2 \
      --system-file "$WORK_DIR/GEMINI.md" \
      process "$HANDOFF"
    ;;

  *)
    echo "Error: Unknown tool $TOOL"
    exit 1
    ;;
esac
```

**Usage**:
```bash
# Let script choose tool
./launch_agent.sh 2 implementation layer_2_features/auth-system/2.01_manager_handoff_documents/incoming.json

# Force specific tool
./launch_agent.sh 2 implementation layer_2_features/auth-system/2.01_manager_handoff_documents/incoming.json claude
```

<!-- section_id: "ff253b55-f965-48b1-87a4-67ddb9cf218d" -->
### Parallel Launcher (Bash)

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
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    echo "Warning: Agent PID $PID failed with status $STATUS"
  fi
done

echo "All agents completed"
```

**Usage**:
```bash
./parallel_launch.sh 3 implementation \
  layer_3_components/login-form/hand_off_documents/incoming.json \
  layer_3_components/password-reset/hand_off_documents/incoming.json \
  layer_3_components/session-manager/hand_off_documents/incoming.json
```

---

<!-- section_id: "e330af66-bfe2-4fd8-bf3f-f3fc168b7281" -->
## OS-Specific Adaptations

<!-- section_id: "09ac1499-ebef-4001-b3ea-35dfa7fb3c1b" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "53343ae9-4066-4d8c-bbcc-6158243e96d8" -->
### Windows (PowerShell)
```powershell
# PowerShell equivalent of bash launcher
param(
    [int]$Layer,
    [string]$Stage,
    [string]$Handoff,
    [string]$Tool = "auto"
)

$BaseDir = "C:\Users\YourName\code\0_ai_context\0_context"

# Auto-select tool
if ($Tool -eq "auto") {
    if ($Layer -le 2 -or $Stage -eq "criticism") {
        $Tool = "claude"
    } elseif ($Stage -eq "request" -or $Stage -eq "instructions") {
        $Tool = "gemini"
    } else {
        $Tool = "codex"
    }
}

# Launch tool
switch ($Tool) {
    "claude" {
        & claude-code --working-dir "$BaseDir\layer_$Layer" `
                      --allowed "B(cla:*,codex:*,gemini:*)" `
                      process-handoff "$Handoff"
    }
    "codex" {
        & codex --model codestral `
                --agents-md "$BaseDir\layer_$Layer\AGENTS.md" `
                execute-handoff "$Handoff"
    }
    "gemini" {
        & gemini --model gemini-pro-2 `
                 --system-file "$BaseDir\layer_$Layer\GEMINI.md" `
                 process "$Handoff"
    }
}
```

<!-- section_id: "7efa144f-7ce3-4595-98ca-a9cb037bda1a" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "b8b64fa9-b136-43f5-b8f6-cc0a8b77e7af" -->
## Related Documentation

**Within 0_ai_context**:
- **Framework Orchestration**: `sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`
- **Handoff Schema**: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **OS Variants (Quartets)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`
- **Tool Context Systems**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md`

**Normative Specification**:
- **CLI Recursion (Detailed)**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/cli_recursion_syntax.md`
- **Architecture**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Parallel Execution**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md`

---

<!-- section_id: "832d6a14-bdb8-4b93-8bce-1cf7e8ae63ca" -->
## Summary

CLI recursion enables deep agent hierarchies:

1. **Explicit Commands**: Use `claude-code --allowed "B(...)"` to enable recursion
2. **Handoff-Driven**: Each level reads incoming, processes, writes outgoing
3. **Tool Selection**: Use different tools at different layers (Claude for managers, Codex for workers, Gemini for planning)
4. **Parallel Execution**: Spawn multiple agents concurrently via background processes
5. **Error Handling**: Retry with escalation to more powerful models
6. **OS Adaptation**: Adjust paths and shell syntax for target OS (WSL, Windows, macOS)

This pattern is framework-agnostic and works with any CLI-based agent tool that can:
- Accept a working directory
- Load context files (CLAUDE.md, AGENTS.md, GEMINI.md)
- Read/write handoff files
- Optionally spawn subprocesses
