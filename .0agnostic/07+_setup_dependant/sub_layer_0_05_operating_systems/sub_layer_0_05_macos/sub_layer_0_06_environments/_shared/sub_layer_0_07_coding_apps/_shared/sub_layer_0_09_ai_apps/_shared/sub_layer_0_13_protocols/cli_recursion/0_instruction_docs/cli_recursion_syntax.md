---
resource_id: "0031d509-15be-46ca-b39c-dbd0ed0a6270"
resource_type: "document"
resource_name: "cli_recursion_syntax"
---
# CLI Recursion Syntax and Patterns

<!-- section_id: "cae2355a-6fc4-441c-a1a9-9f80756b74d1" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "7733e513-1644-4791-a205-22ec66bd4d1c" -->
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

<!-- section_id: "d456657e-7ecc-4e38-9483-c64ef9d673a8" -->
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

<!-- section_id: "8198abaa-4d7d-450d-bcc7-6f7f0ce06de0" -->
## Claude Code Recursion Syntax

<!-- section_id: "3768d7e9-ab8d-4cfd-8907-656fad01a645" -->
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

<!-- section_id: "1608aee2-b080-43ea-9382-5778f98a15d3" -->
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

<!-- section_id: "242004c6-6b59-45e0-8024-1aad2be5f20b" -->
## Handoff-Based Recursion

<!-- section_id: "f0422354-09f3-4970-b6a4-20603459dba9" -->
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

<!-- section_id: "bb40feea-6cc1-45e9-8d37-bfadabe5d985" -->
## Multi-Layer Examples

<!-- section_id: "cf327ea8-1a89-4a85-b0c5-3f6778b21911" -->
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

<!-- section_id: "18208cd3-b809-4609-8de8-ab23cc534184" -->
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

<!-- section_id: "2623c8cc-0ab4-4f27-8d3c-9283ae74fdd8" -->
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

<!-- section_id: "98ab24fe-1f01-445b-8c49-14c2c04c881d" -->
## Tool Selection Patterns

<!-- section_id: "49a54863-074f-4910-a4da-7d757d1e7bcc" -->
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

<!-- section_id: "1aed5692-d4cb-400d-8854-61d74040211e" -->
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

<!-- section_id: "5e7b7abc-966d-416c-9e43-7824e9253c13" -->
## Wrapper Scripts

<!-- section_id: "9b141ec9-f67f-416b-bc62-a64e417b9398" -->
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

<!-- section_id: "593a5350-bc0c-472d-a342-89b9cd2af5a4" -->
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

<!-- section_id: "2f7ef098-3fe0-4041-8265-e1ac3c5fbdce" -->
## OS-Specific Adaptations

<!-- section_id: "2487bec9-1375-4792-b10b-3f87f1575f6d" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "cc428fc5-0cf8-4edf-b07c-4a9336a7774e" -->
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

<!-- section_id: "cadb1d79-ea7e-4f71-9e28-d8ff62ffa49a" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "cd8cc4d3-64fe-4680-a08e-93b4d2597949" -->
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

<!-- section_id: "7cd431fd-5e46-4320-9311-bd1cb307a52d" -->
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

<!-- section_id: "8d94330f-8937-487e-9f57-6ba704e42ecd" -->
## Legacy Universal Protocols Source

# CLI Recursion Syntax and Patterns

<!-- section_id: "566ef287-5f17-4d9c-9fd3-5ff73fbdf757" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "8c36e2eb-9cf5-4923-a160-8b7d66350d94" -->
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

<!-- section_id: "4c130028-c006-418f-96bd-34dea64f5b7c" -->
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

<!-- section_id: "bd725af7-fa29-46dc-b280-4c90774ce48c" -->
## Claude Code Recursion Syntax

<!-- section_id: "cc077007-7ea7-47f8-b36e-7d8d9acb1072" -->
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

<!-- section_id: "30b698e3-11e7-4842-8929-d1717b40ed2a" -->
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

<!-- section_id: "36d33146-d880-4f02-919b-1acf7f54a588" -->
## Handoff-Based Recursion

<!-- section_id: "80aa13ac-c46d-43fb-a7ee-3f8b49fa1fec" -->
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

<!-- section_id: "cbcba8a6-678d-4f09-b6b5-5092aee774c4" -->
## Multi-Layer Examples

<!-- section_id: "999b8eee-f427-45d4-8e47-a8fba254978a" -->
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

<!-- section_id: "b3629ea5-cd04-4264-a462-798b8afa7570" -->
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

<!-- section_id: "fa32f26f-7c9a-4fdc-8be4-ff6c388db33c" -->
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

<!-- section_id: "4a2af25d-fe34-42a5-a4af-4e5e1239c4cf" -->
## Tool Selection Patterns

<!-- section_id: "5bfe94b1-a402-48f4-bf03-6db892233369" -->
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

<!-- section_id: "f88589d8-ce2c-4d49-9351-691987f7d150" -->
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

<!-- section_id: "9c72ecc6-11d8-4677-a817-310e22c4314c" -->
## Wrapper Scripts

<!-- section_id: "d2976d92-e7cf-4204-a6b6-12b408eae30d" -->
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

<!-- section_id: "fa9dd885-d0d1-4002-aa75-eaffcaf40976" -->
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

<!-- section_id: "c63638a7-c640-4d87-b5d5-de112aa7159d" -->
## OS-Specific Adaptations

<!-- section_id: "466eb034-f4bf-4622-a3f1-46dfe0272bd0" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "64d62ecd-2826-4b47-91d8-95c2c690cb19" -->
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

<!-- section_id: "ee35307b-9842-4fbf-bd75-3e7d8505caf8" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "d0c4a281-22e3-4dbb-82d1-35021e2edcaf" -->
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

<!-- section_id: "51c2890b-92f6-4784-b920-38b6fb459dbe" -->
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

<!-- section_id: "4a5df230-9348-499c-a5db-c05ba70af66f" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`

# CLI Recursion Syntax and Patterns

<!-- section_id: "3585471c-bc12-423c-8ae3-50bb1a3d8ecb" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "7e02739d-c552-4a0b-8017-d7247adb241e" -->
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

<!-- section_id: "2c82a4bf-e37e-473b-9532-40ac570e4048" -->
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

<!-- section_id: "db1cf41d-0a09-4197-be04-fa8c47261b45" -->
## Claude Code Recursion Syntax

<!-- section_id: "50f41b13-9b5a-4bd5-869f-8ba486f4ff53" -->
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

<!-- section_id: "a686d1b2-2102-4d13-839d-9311e1c14460" -->
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

<!-- section_id: "986a527e-638e-462f-a05f-2bb2c1e924ea" -->
## Handoff-Based Recursion

<!-- section_id: "992a909c-110b-4fbb-94a7-c047daef81cf" -->
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

<!-- section_id: "61c0d115-9a30-4a93-aa79-97b0230ca4a1" -->
## Multi-Layer Examples

<!-- section_id: "8564885b-8e95-4655-a5c9-c7e95fe629f2" -->
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

<!-- section_id: "3ab78ae1-df48-408b-88db-6195e9c9f703" -->
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

<!-- section_id: "4c1877c3-09c8-4dfa-ac3a-a3190b711bfd" -->
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

<!-- section_id: "ed149af7-6a39-4643-9c15-9365878635ad" -->
## Tool Selection Patterns

<!-- section_id: "1b3dd6b2-3606-4d08-8497-1b703b5d6b4a" -->
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

<!-- section_id: "bc5bf380-c434-44c9-bac0-8d06a1083371" -->
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

<!-- section_id: "4e223944-11c9-4c1a-b8fd-8ba293eaba59" -->
## Wrapper Scripts

<!-- section_id: "5b8ad1c8-765e-48f2-830b-b1d7ca908a5b" -->
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

<!-- section_id: "5824b1d6-a9f6-4208-b051-70cff3e6e2bc" -->
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

<!-- section_id: "9ca35a76-6719-4724-a432-ee34618e6c03" -->
## OS-Specific Adaptations

<!-- section_id: "5eb7a2f3-e237-4f73-8919-b3f206b13a78" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "67b97595-0588-422d-8613-caf5b551a8f8" -->
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

<!-- section_id: "9464897d-401b-4b0d-9dc2-1ff35cab4327" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "faeadb38-4fbd-4842-94c7-8b41e0c10233" -->
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

<!-- section_id: "bccd0911-5c21-4cda-99be-09c95d263cfc" -->
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
