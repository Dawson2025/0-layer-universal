---
resource_id: "da88d95b-03f4-4de9-91ee-f6f97ea2ddd2"
resource_type: "document"
resource_name: "cli_recursion_syntax"
---
# CLI Recursion Syntax and Patterns

<!-- section_id: "b819361f-4cb1-4e97-93fd-bd80595bfc9d" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "faee53de-c54c-4f9f-9ce8-2dde17c1ff87" -->
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

<!-- section_id: "d6ff221d-2072-4138-a38e-29d97385213b" -->
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

<!-- section_id: "e52138e4-47bf-4671-add5-5e57de67fb15" -->
## Claude Code Recursion Syntax

<!-- section_id: "4286babe-b307-4a44-9811-104a5c40ffb5" -->
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

<!-- section_id: "a97e9fdf-73db-419a-b0dd-4f7459addd91" -->
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

<!-- section_id: "acc24a48-29a7-4ed8-b79e-5f718c9022eb" -->
## Handoff-Based Recursion

<!-- section_id: "46d0e4ff-737d-4013-b176-d7ee25ec1459" -->
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

<!-- section_id: "5cd5c753-fbd1-407f-8f5d-95597ef5621a" -->
## Multi-Layer Examples

<!-- section_id: "27e2dc0e-09f0-4638-bef6-241032eeb491" -->
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

<!-- section_id: "6b9eef51-ff5e-4a25-a7e2-7f08962d7254" -->
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

<!-- section_id: "fe42de95-adbb-42a1-a620-a6af8e22fb58" -->
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

<!-- section_id: "efdb8c62-6cb8-4135-bf85-787f7e4e3137" -->
## Tool Selection Patterns

<!-- section_id: "f2226d0d-9ab4-43f5-9d34-6fb0308c88b2" -->
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

<!-- section_id: "77598c60-0289-462e-8f68-20dfedd469e8" -->
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

<!-- section_id: "b8499ef2-a077-4dc6-b54d-9f1e0c7fc96d" -->
## Wrapper Scripts

<!-- section_id: "35d28b99-bb31-4712-88a4-1bf65059b6e7" -->
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

<!-- section_id: "5af4bd78-5cd4-4bd4-a703-e1e5bb36bc5a" -->
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

<!-- section_id: "01e70804-d6bd-46b6-948e-4f8dca6d5442" -->
## OS-Specific Adaptations

<!-- section_id: "91311449-8a63-4881-9d0e-55116eea4973" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "2a4b042c-2eca-43f5-9997-f3dc7db6ac6b" -->
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

<!-- section_id: "e0126802-6ddf-44b4-9356-2b13b52dc235" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "e09b475f-4da7-4c00-81cd-cff6227190cc" -->
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

<!-- section_id: "20748bb1-e179-4677-bcc0-5575d88ec14a" -->
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

<!-- section_id: "ed52f0c0-ae63-43b6-a14c-1380d75c7c87" -->
## Legacy Universal Protocols Source

# CLI Recursion Syntax and Patterns

<!-- section_id: "a3a7c14f-dca9-4a31-a345-29705d1ab50a" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "37d095ea-b1db-45c6-b8d2-6c9a1bc0c385" -->
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

<!-- section_id: "ac546a8a-03ea-4fcc-adde-8125cf3833cc" -->
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

<!-- section_id: "4aabc530-f2a8-4cb0-a9be-fba1e99bb491" -->
## Claude Code Recursion Syntax

<!-- section_id: "2f4d9d9a-4ef4-49aa-9fc9-54f8db6c0e51" -->
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

<!-- section_id: "f6b345d5-7b06-47ef-895f-a7a3c1049c49" -->
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

<!-- section_id: "d811c837-2a23-48fc-aed7-c1d95dfa1a4b" -->
## Handoff-Based Recursion

<!-- section_id: "755a0f5b-071f-4b22-8fa4-bf961460ff32" -->
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

<!-- section_id: "89527404-d93b-4818-a719-0f30e2cc3a2b" -->
## Multi-Layer Examples

<!-- section_id: "663d800f-9f5d-45d5-bd1b-52e28705448a" -->
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

<!-- section_id: "56ff11b4-19bd-4d20-9158-7dc7c2e51730" -->
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

<!-- section_id: "f236a3f9-79db-4b0f-9fbf-b0f00e504c8d" -->
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

<!-- section_id: "7a4177a1-112e-42cd-a97b-5b9a4409533e" -->
## Tool Selection Patterns

<!-- section_id: "131954ac-f374-43a6-a513-2a47ced574db" -->
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

<!-- section_id: "d8dbf1e4-cd29-4c54-8e49-cfffb268a82e" -->
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

<!-- section_id: "19cba2aa-ab3f-4e9c-b07c-cb547ac23f9d" -->
## Wrapper Scripts

<!-- section_id: "1a875f6c-c4dd-47ad-8922-2730f752e13a" -->
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

<!-- section_id: "03b2322f-87c8-4e85-842e-8862d561a466" -->
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

<!-- section_id: "05abdd41-f6f8-4005-a80b-99f801dbb153" -->
## OS-Specific Adaptations

<!-- section_id: "b0648581-2fab-4b8c-b5af-0157b09ecc3f" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "66f1030b-9d7a-4e5a-a981-a4e67c5ff43c" -->
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

<!-- section_id: "3806472b-4d6c-417a-8d86-c6aac5361507" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "accf0a31-663b-4047-b056-c79e2abec390" -->
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

<!-- section_id: "9eebc113-32a0-483c-925a-24334605d702" -->
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

<!-- section_id: "e18b0ad8-9d82-41cd-897c-125a4b21570c" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`

# CLI Recursion Syntax and Patterns

<!-- section_id: "304ba4e0-8b27-4675-b2d7-6428cc3d2f64" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "757003a4-85c7-4d97-93d4-ec961355ffe9" -->
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

<!-- section_id: "7e08d434-bbd5-4008-ae6e-56991af4e9b3" -->
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

<!-- section_id: "d321d6a7-9837-420f-8476-8e1485c4d574" -->
## Claude Code Recursion Syntax

<!-- section_id: "c3c62815-f389-4029-9653-da8ec2cec4ce" -->
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

<!-- section_id: "3e103533-8881-4edf-a6e7-669d0014b963" -->
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

<!-- section_id: "2b8475a3-85a7-45de-a0ec-a6a75f1228cd" -->
## Handoff-Based Recursion

<!-- section_id: "3e77cc86-c9c2-45b6-b91f-dd4cba852544" -->
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

<!-- section_id: "bb2e6f18-ac78-4f8f-9cd8-a5916201d55b" -->
## Multi-Layer Examples

<!-- section_id: "c8ab3008-f8bd-4873-bb0f-27ec11e4ac84" -->
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

<!-- section_id: "84149ea8-847d-41b7-ab71-898cfd0480fc" -->
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

<!-- section_id: "86d2e65b-c4e1-4c1d-b4fd-582ee3f5ba85" -->
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

<!-- section_id: "c062c55b-ac64-49fb-9961-85a42be81dda" -->
## Tool Selection Patterns

<!-- section_id: "7f168888-da14-4715-aed3-fa79d8972f6c" -->
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

<!-- section_id: "9a733151-7502-4069-9082-9117202596a7" -->
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

<!-- section_id: "f023c99c-b26a-439f-9dc0-585801e313ef" -->
## Wrapper Scripts

<!-- section_id: "62e5c8b3-d68a-4d2b-a024-03fefd649c31" -->
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

<!-- section_id: "d8fd0bae-4e8a-423c-b2a4-2e4aecc32ce2" -->
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

<!-- section_id: "13f7dfdb-a319-43c7-9c4a-032e934556c2" -->
## OS-Specific Adaptations

<!-- section_id: "a6b6ccce-7dd4-4593-91ef-682d61f57cb5" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "ab6ab97b-783c-4336-aa94-5663ad6c2d75" -->
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

<!-- section_id: "650631fa-876e-4eb6-b8b1-bf59b89b8e9f" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "aa1ee528-3a35-4a5d-938e-72066354df6a" -->
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

<!-- section_id: "a4d52a84-54d9-458d-a953-3fedc97f916f" -->
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
