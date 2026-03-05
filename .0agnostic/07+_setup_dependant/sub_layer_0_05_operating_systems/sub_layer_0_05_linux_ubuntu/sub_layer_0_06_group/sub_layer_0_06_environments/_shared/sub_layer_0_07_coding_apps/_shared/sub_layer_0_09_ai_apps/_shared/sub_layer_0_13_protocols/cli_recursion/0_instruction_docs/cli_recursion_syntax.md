---
resource_id: "8004bc89-bad4-4a57-95d6-7c166a054945"
resource_type: "document"
resource_name: "cli_recursion_syntax"
---
# CLI Recursion Syntax and Patterns

<!-- section_id: "bda7005f-bf7d-447e-ab7b-6a936a49cd12" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "7b5b7201-166a-4a52-88d0-81d05bce9f8d" -->
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

<!-- section_id: "91ac1832-66d7-4e6e-b2fe-00008289b428" -->
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

<!-- section_id: "92b3bffd-d819-4d94-a0ef-cf1103eca02e" -->
## Claude Code Recursion Syntax

<!-- section_id: "cb6a5e89-587a-4dcd-b7c6-7425b5cbe06d" -->
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

<!-- section_id: "38a530a4-329e-496a-ae59-1480bbd43390" -->
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

<!-- section_id: "956999ab-f3cc-42e9-bf7d-fadd08c82fa0" -->
## Handoff-Based Recursion

<!-- section_id: "275be660-d7fa-4af9-bd0b-4359c2c99a7c" -->
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

<!-- section_id: "7568866d-c0f5-4759-8c1f-2c0b150ac47b" -->
## Multi-Layer Examples

<!-- section_id: "40b5216f-2d57-4c92-8fee-e40df7b73d98" -->
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

<!-- section_id: "4b039d8a-400c-42f0-8081-3bdc637b0fc0" -->
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

<!-- section_id: "d17a82dc-bdb6-4089-92da-362f1ff906b4" -->
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

<!-- section_id: "c5c2bcff-4d49-4882-bb92-98afd25eb5ad" -->
## Tool Selection Patterns

<!-- section_id: "187863b0-7106-4a30-b89b-cdd9b1971271" -->
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

<!-- section_id: "be7f45c2-7581-480a-bae2-6780f13b617e" -->
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

<!-- section_id: "e49942a0-e42a-437a-bcc2-317d8c26095c" -->
## Wrapper Scripts

<!-- section_id: "b4f486db-a5a2-4048-9b11-19c32ec79d09" -->
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

<!-- section_id: "73e2d1d6-e6c3-4a05-b104-06e613235de0" -->
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

<!-- section_id: "ba5e3899-16d9-4907-9766-f13f5b3a522c" -->
## OS-Specific Adaptations

<!-- section_id: "00bb8952-ddb0-4f89-8086-0fc3a2e58bc4" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "cd0de995-3356-428b-b3bb-f0bc01617322" -->
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

<!-- section_id: "899c7007-a0d5-43b4-bb1e-e15a3c3dfa1c" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "fe373cf1-8483-4019-abe6-832ff99e2378" -->
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

<!-- section_id: "556e4cfc-99d8-4848-a46f-6df1da37ddc2" -->
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

<!-- section_id: "6b392aab-15bc-4225-a69b-0a8370c33760" -->
## Legacy Universal Protocols Source

# CLI Recursion Syntax and Patterns

<!-- section_id: "efdae942-30ad-49c5-aa16-5409a899dd9f" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "f230f5a3-0cbe-4095-aa1a-fdbbdcbd91e5" -->
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

<!-- section_id: "b124f27a-c2a3-4f86-aeeb-db862e98a36b" -->
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

<!-- section_id: "7031a58f-2c23-4bef-a132-f9f6fa0b999f" -->
## Claude Code Recursion Syntax

<!-- section_id: "aa42cbbe-98f4-42c5-91be-64ffbbd9f84f" -->
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

<!-- section_id: "07cc1aef-57e7-46a1-8acc-b9d55ca98ea2" -->
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

<!-- section_id: "d73d1546-7a43-4bf5-a05b-9763eaa0081e" -->
## Handoff-Based Recursion

<!-- section_id: "c24cc7c8-24d6-4432-9a1f-e5373537988e" -->
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

<!-- section_id: "57f7c4e4-6052-48d4-b45a-566adaee04d7" -->
## Multi-Layer Examples

<!-- section_id: "aa8dd0c4-2d99-4e68-823c-db8a32c3bd5e" -->
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

<!-- section_id: "0a8072ec-5cb6-42fa-bc89-739c86096c64" -->
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

<!-- section_id: "81553fb1-62d0-40ff-8f4a-5619c5b1d715" -->
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

<!-- section_id: "19d2945f-7c75-4b6a-8d09-40add6374906" -->
## Tool Selection Patterns

<!-- section_id: "1d03a0c1-4155-4039-85b2-c620b58c855a" -->
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

<!-- section_id: "5a062a7c-27c8-4be4-868d-f9466e0af4e2" -->
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

<!-- section_id: "887e0036-f8b2-4b92-8e5f-8b2259a5183f" -->
## Wrapper Scripts

<!-- section_id: "f701a3dd-e07f-4bbe-a850-65cf061377ba" -->
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

<!-- section_id: "fe2f5255-9026-41e8-9b9e-65fa4ef52096" -->
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

<!-- section_id: "e2708f71-a0d2-463a-85c1-ef259c7338e2" -->
## OS-Specific Adaptations

<!-- section_id: "70eace16-e1fe-4056-b6bf-b45afb0c0f57" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "d9a1f648-9e7a-471c-9a32-8401e7efd761" -->
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

<!-- section_id: "666f4778-d5d9-4a4d-8aa8-6d8d67cb671d" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "6d697e82-bacc-4d78-94d3-acbf24711df7" -->
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

<!-- section_id: "c99b9524-7a28-4583-9420-628d15a90912" -->
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

<!-- section_id: "68f36990-4124-4e80-b1cb-1721b84dafa5" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`

# CLI Recursion Syntax and Patterns

<!-- section_id: "4d70603b-89a2-4613-9885-f7d6d34af9c6" -->
## Applicability
**When to use:** When implementing deep agent hierarchies where managers spawn worker agents via CLI commands.
**Where to use:** L0-L3 managers spawning L1-L4 workers; supervisors orchestrating multi-layer workflows.
**Scope:** OS: wsl | linux_ubuntu (examples adapted for WSL/Ubuntu; patterns apply to all OS variants with appropriate command adjustments); Tools: claude-code, codex, gemini (primary CLI tools in current environment).

---

<!-- section_id: "7d18e7ba-40fa-4393-9cdd-aa07894bad37" -->
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

<!-- section_id: "a3f7f19e-e7c9-4da7-afdf-44170fe49a37" -->
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

<!-- section_id: "3023164b-c81b-48a8-9cf0-5ff6741a1ac4" -->
## Claude Code Recursion Syntax

<!-- section_id: "3c03345b-f499-42a8-9890-aae99eedc348" -->
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

<!-- section_id: "f5c68df1-ed4c-4248-93b2-5b05532576d9" -->
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

<!-- section_id: "48756c18-2802-4e7c-b5bd-455e4e2aebe9" -->
## Handoff-Based Recursion

<!-- section_id: "63ba4e0b-841d-4665-8432-2807f2011a6d" -->
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

<!-- section_id: "5359836e-9ce0-47bc-9557-6d84487623d0" -->
## Multi-Layer Examples

<!-- section_id: "4bbc9239-6837-4f7a-a76e-54a5699dc6f1" -->
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

<!-- section_id: "8cad2c26-036e-44ac-af0d-967c133f4871" -->
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

<!-- section_id: "8ef7f0c7-d881-4914-9bf3-c54e614e5695" -->
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

<!-- section_id: "fbcfa129-462b-4382-8424-257ad47a8dad" -->
## Tool Selection Patterns

<!-- section_id: "21d3bd44-5ccc-4cb0-b4c5-a34c8a1a508b" -->
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

<!-- section_id: "1ec80390-b56e-4b2d-a469-690b6ecd1c8f" -->
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

<!-- section_id: "4b0e20a9-198b-4fee-b02a-6ad047ff48ef" -->
## Wrapper Scripts

<!-- section_id: "fae44399-46b6-4684-8f87-b0946d51a1ca" -->
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

<!-- section_id: "ca2fa3b1-9e34-4995-8c06-c46dace52d22" -->
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

<!-- section_id: "25097438-9f73-4ac9-8f9f-dcf169641c7a" -->
## OS-Specific Adaptations

<!-- section_id: "7614118f-3946-4de4-9670-97246b75a6da" -->
### WSL/Ubuntu (Current Environment)
- Shell: bash
- Path separator: `/`
- Line endings: LF
- Commands work as shown in examples above

<!-- section_id: "9747b412-0a0e-4ae6-b88a-94a20cf9431e" -->
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

<!-- section_id: "30133d1b-c3c2-42f0-8cb6-425bba0fbd3c" -->
### macOS (bash/zsh)
Same as WSL/Ubuntu with potential path adjustments:
```bash
BASE_DIR="/Users/yourname/code/0_layer_universal/0_context"
```

---

<!-- section_id: "0f9597de-6dd5-442a-b4ef-0388569f15e4" -->
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

<!-- section_id: "a01471bb-5d42-4d13-9cbf-fd2700a4848c" -->
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
