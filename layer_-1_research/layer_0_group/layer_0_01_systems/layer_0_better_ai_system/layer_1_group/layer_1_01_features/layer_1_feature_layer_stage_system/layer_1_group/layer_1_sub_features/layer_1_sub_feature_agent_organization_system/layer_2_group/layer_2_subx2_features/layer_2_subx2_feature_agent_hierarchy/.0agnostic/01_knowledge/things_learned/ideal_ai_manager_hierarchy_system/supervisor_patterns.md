---
resource_id: "6e54505f-724a-4ca8-b6bb-5c93afd65a18"
resource_type: "knowledge"
resource_name: "supervisor_patterns"
---
## Supervisor Patterns and Implementation

This document provides concrete patterns and examples for implementing supervisors in the AI manager hierarchy system.

Supervisors are the "process schedulers" that orchestrate managers and workers across layers and stages.

It builds on:
- `architecture.md` (supervisor responsibilities)
- `framework_orchestration.md` (framework-based supervisors)

---

## 1. Supervisor Core Responsibilities

A supervisor must:

1. **Discover Tasks**: Detect new work from handoffs or external triggers
2. **Plan Execution**: Determine which agents, tools, and resources to use
3. **Spawn Workers**: Launch manager/worker processes
4. **Monitor Progress**: Track running tasks, collect outputs
5. **Handle Failures**: Retry, escalate, or fail gracefully
6. **Aggregate Results**: Combine outputs into final handoffs

---

## 2. Supervisor Architecture Patterns

### 2.1 Pattern 1: Simple File-Watching Supervisor

**Use Case:** Lightweight, single-machine development

**Architecture:**
```
┌─────────────────────────────────────┐
│  File Watcher (inotify/fswatch)    │
│  - Watches hand_off_documents/     │
│  - Triggers on new incoming.json   │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Task Dispatcher                    │
│  - Reads handoff                    │
│  - Applies policy mapping           │
│  - Selects tool & model             │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Process Manager                    │
│  - Spawns CLI processes             │
│  - Monitors exit codes              │
│  - Collects outputs                 │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Result Aggregator                  │
│  - Writes outgoing handoffs         │
│  - Updates status                   │
│  - Triggers next stage              │
└─────────────────────────────────────┘
```

**Implementation (Python):**
```python
#!/usr/bin/env python3
import os
import json
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HandoffWatcher(FileSystemEventHandler):
    def __init__(self, supervisor):
        self.supervisor = supervisor

    def on_created(self, event):
        if event.src_path.endswith('/incoming.json'):
            self.supervisor.process_handoff(event.src_path)

class SimpleSupervisor:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.running_tasks = {}

    def start(self):
        """Start watching for handoff files."""
        observer = Observer()
        handler = HandoffWatcher(self)

        # Watch all layer directories
        for layer_dir in find_layer_directories(self.root_dir):
            observer.schedule(handler, layer_dir, recursive=True)

        observer.start()
        print(f"Supervisor started, watching {self.root_dir}")

        try:
            while True:
                time.sleep(1)
                self.check_running_tasks()
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def process_handoff(self, handoff_path):
        """Process a new handoff file."""
        try:
            with open(handoff_path) as f:
                handoff = json.load(f)

            # Extract layer and stage from path
            layer, stage = parse_path(handoff_path)

            # Select appropriate tool and model
            tool_config = self.select_tool(layer, stage, handoff)

            # Spawn agent process
            task_id = self.spawn_agent(layer, stage, tool_config, handoff)

            print(f"Started task {task_id}: {layer}/{stage}")

        except Exception as e:
            print(f"Error processing {handoff_path}: {e}")
            self.write_error_handoff(handoff_path, str(e))

    def select_tool(self, layer, stage, handoff):
        """Apply policy to select tool and model."""
        # Simple policy - can be replaced with sophisticated routing
        if layer == 0 or stage in ["criticism", "fixing"]:
            return {"tool": "claude-code", "model": "claude-sonnet-4.5"}
        elif stage in ["request", "instructions", "planning"]:
            return {"tool": "gemini", "model": "gemini-pro-2"}
        elif layer >= 3 and stage == "implementation":
            return {"tool": "codex", "model": "codestral"}
        else:
            return {"tool": "claude-code", "model": "claude-haiku"}

    def spawn_agent(self, layer, stage, tool_config, handoff):
        """Launch agent process."""
        task_id = generate_task_id()

        # Build command
        cmd = self.build_command(layer, stage, tool_config, handoff)

        # Start process in background
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=get_stage_directory(layer, stage)
        )

        # Track running task
        self.running_tasks[task_id] = {
            "process": process,
            "layer": layer,
            "stage": stage,
            "handoff": handoff,
            "started_at": time.time()
        }

        return task_id

    def build_command(self, layer, stage, tool_config, handoff):
        """Construct CLI command for agent."""
        tool = tool_config["tool"]
        model = tool_config["model"]

        if tool == "claude-code":
            return [
                "claude-code",
                "--model", model,
                "--system-prompt-file", f"layer_{layer}/ai_agent_system/CLAUDE.md",
                "process-handoff", handoff["id"]
            ]
        elif tool == "codex":
            return [
                "codex",
                "--model", model,
                "--agents-md", f"layer_{layer}/ai_agent_system/AGENTS.md",
                "execute-handoff", handoff["id"]
            ]
        elif tool == "gemini":
            return [
                "gemini",
                "--model", model,
                "--system-file", f"layer_{layer}/ai_agent_system/GEMINI.md",
                "process", handoff["id"]
            ]

    def check_running_tasks(self):
        """Check status of running tasks."""
        for task_id, task in list(self.running_tasks.items()):
            process = task["process"]

            # Check if process finished
            if process.poll() is not None:
                stdout, stderr = process.communicate()

                if process.returncode == 0:
                    print(f"Task {task_id} completed successfully")
                    self.handle_success(task_id, task, stdout)
                else:
                    print(f"Task {task_id} failed with code {process.returncode}")
                    self.handle_failure(task_id, task, stderr)

                del self.running_tasks[task_id]

            # Check for timeout
            elif time.time() - task["started_at"] > 600:  # 10 min timeout
                print(f"Task {task_id} timed out, killing")
                process.kill()
                self.handle_timeout(task_id, task)
                del self.running_tasks[task_id]

    def handle_success(self, task_id, task, stdout):
        """Handle successful task completion."""
        # Trigger next stage if applicable
        next_stage = get_next_stage(task["stage"])
        if next_stage:
            # Copy outgoing to next stage's incoming
            copy_handoff(
                f"{task['layer']}/{task['stage']}/hand_off_documents/outgoing.json",
                f"{task['layer']}/{next_stage}/hand_off_documents/incoming.json"
            )

    def handle_failure(self, task_id, task, stderr):
        """Handle task failure."""
        # Write failure handoff
        failure_handoff = {
            "schemaVersion": "1.0.0",
            "status": "failed",
            "error": stderr.decode(),
            "originalHandoff": task["handoff"]
        }

        write_handoff(
            f"{task['layer']}/{task['stage']}/hand_off_documents/outgoing.json",
            failure_handoff
        )

        # Decide: retry, escalate, or fail
        retry_count = task["handoff"].get("retry_count", 0)
        if retry_count < 3:
            # Retry with higher-tier model
            print(f"Retrying task {task_id} (attempt {retry_count + 1})")
            task["handoff"]["retry_count"] = retry_count + 1
            self.process_handoff(
                f"{task['layer']}/{task['stage']}/hand_off_documents/incoming.json"
            )
        else:
            # Escalate to human or higher layer
            escalate_to_human(task)

    def handle_timeout(self, task_id, task):
        """Handle task timeout."""
        print(f"Task {task_id} exceeded timeout, escalating")
        escalate_to_human(task, reason="timeout")

if __name__ == "__main__":
    supervisor = SimpleSupervisor(root_dir="/path/to/workspace")
    supervisor.start()
```

### 2.2 Pattern 2: Queue-Based Supervisor

**Use Case:** Distributed systems, multiple machines, high throughput

**Architecture:**
```
┌─────────────────────────────────────┐
│  Task Queue (Redis/RabbitMQ)       │
│  - Handoffs as messages             │
│  - Priority queues per layer        │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Worker Pool                        │
│  - Multiple workers consume queue   │
│  - Each worker runs on own machine  │
│  - Auto-scaling based on load       │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Result Store (PostgreSQL/S3)      │
│  - Stores completed handoffs        │
│  - Queryable task history           │
└─────────────────────────────────────┘
```

**Implementation (Python + Celery):**
```python
from celery import Celery, group
from celery.exceptions import SoftTimeLimitExceeded
import json

app = Celery('supervisor', broker='redis://localhost:6379/0')

@app.task(bind=True, max_retries=3, time_limit=600)
def process_handoff(self, layer, stage, handoff_data):
    """Process a single handoff task."""
    try:
        # Select tool and model
        tool_config = select_tool(layer, stage, handoff_data)

        # Execute agent
        result = execute_agent(layer, stage, tool_config, handoff_data)

        # Write outgoing handoff
        write_result(layer, stage, result)

        # Trigger next stage
        next_stage = get_next_stage(stage)
        if next_stage:
            process_handoff.delay(layer, next_stage, result)

        return result

    except SoftTimeLimitExceeded:
        # Escalate on timeout
        escalate_task.delay(layer, stage, handoff_data, reason="timeout")

    except Exception as exc:
        # Retry with exponential backoff
        retry_delay = 2 ** self.request.retries
        raise self.retry(exc=exc, countdown=retry_delay)

@app.task
def process_layer_task(layer, handoff_data):
    """Process entire layer by spawning parallel stage tasks."""

    # Decompose into stages
    stages = ["request", "instructions", "planning", "design",
              "implementation", "testing", "criticism", "fixing"]

    # Run stages sequentially (could parallelize some)
    for stage in stages:
        # Check if stage is needed
        if should_run_stage(layer, stage, handoff_data):
            result = process_handoff.delay(layer, stage, handoff_data).get()
            handoff_data = result  # Feed output to next stage

    return handoff_data

@app.task
def process_feature_parallel(layer, feature_handoff):
    """Process feature by parallelizing component work."""

    # Decompose feature into components
    components = decompose_to_components(feature_handoff)

    # Launch parallel component tasks
    job = group(
        process_layer_task.s(layer + 1, comp)
        for comp in components
    )

    # Wait for all components
    results = job.apply_async().get()

    # Aggregate results
    return aggregate_component_results(results)

# Task routing for priority queues
app.conf.task_routes = {
    'process_handoff': {
        'queue': 'layer_{layer}',
        'priority': lambda layer: 10 - layer  # Higher layers = higher priority
    }
}
```

### 2.3 Pattern 3: LangGraph-Based Supervisor

**Use Case:** Complex workflows, explicit state management, auditability

**Implementation:**
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, List

class SupervisorState(TypedDict):
    """State for supervisor workflow."""
    current_layer: int
    current_stage: str
    handoff: dict
    results: List[dict]
    errors: List[dict]
    status: str

def discover_tasks(state: SupervisorState):
    """Discover new handoff files."""
    new_handoffs = scan_for_handoffs()
    if new_handoffs:
        # Process first new handoff
        state["handoff"] = new_handoffs[0]
        state["status"] = "discovered"
    else:
        state["status"] = "idle"
    return state

def select_agent(state: SupervisorState):
    """Select appropriate agent based on policy."""
    layer = state["current_layer"]
    stage = state["current_stage"]
    handoff = state["handoff"]

    tool_config = apply_policy(layer, stage, handoff)
    state["tool_config"] = tool_config
    state["status"] = "agent_selected"
    return state

def spawn_agent(state: SupervisorState):
    """Spawn agent process."""
    try:
        result = execute_agent(
            state["current_layer"],
            state["current_stage"],
            state["tool_config"],
            state["handoff"]
        )
        state["results"].append(result)
        state["status"] = "completed"
    except Exception as e:
        state["errors"].append({"error": str(e), "stage": state["current_stage"]})
        state["status"] = "failed"

    return state

def should_retry(state: SupervisorState):
    """Decide if we should retry failed task."""
    if state["status"] == "failed":
        retry_count = state["handoff"].get("retry_count", 0)
        return "retry" if retry_count < 3 else "escalate"
    return "next"

def advance_stage(state: SupervisorState):
    """Move to next stage in pipeline."""
    next_stage = get_next_stage(state["current_stage"])
    if next_stage:
        state["current_stage"] = next_stage
        state["handoff"] = state["results"][-1]  # Use last result as input
        state["status"] = "stage_advanced"
    else:
        state["status"] = "workflow_complete"
    return state

# Build supervisor graph
workflow = StateGraph(SupervisorState)

# Add nodes
workflow.add_node("discover", discover_tasks)
workflow.add_node("select", select_agent)
workflow.add_node("execute", spawn_agent)
workflow.add_node("advance", advance_stage)

# Add edges
workflow.set_entry_point("discover")
workflow.add_edge("discover", "select")
workflow.add_edge("select", "execute")
workflow.add_conditional_edges(
    "execute",
    should_retry,
    {
        "retry": "select",  # Retry with potentially different agent
        "escalate": END,    # Escalate to human
        "next": "advance"   # Continue to next stage
    }
)
workflow.add_conditional_edges(
    "advance",
    lambda s: "discover" if s["status"] == "workflow_complete" else "select",
    {
        "discover": "discover",
        "select": "select"
    }
)

# Compile and run
supervisor = workflow.compile()

# Run supervisor loop
while True:
    state = supervisor.invoke(SupervisorState(
        current_layer=1,
        current_stage="request",
        handoff={},
        results=[],
        errors=[],
        status="idle"
    ))
    time.sleep(10)  # Poll interval
```

---

## 3. Failure Handling Patterns

### 3.1 Retry with Escalation

```python
class RetryPolicy:
    """Define retry behavior for different failure modes."""

    def __init__(self):
        self.max_retries = 3
        self.backoff_base = 2  # Exponential backoff

    def should_retry(self, error, attempt):
        """Determine if task should be retried."""

        # Never retry certain errors
        if isinstance(error, (PermissionError, AuthenticationError)):
            return False

        # Retry transient errors
        if isinstance(error, (TimeoutError, NetworkError, RateLimitError)):
            return attempt < self.max_retries

        # Default: retry up to max
        return attempt < self.max_retries

    def get_retry_delay(self, attempt):
        """Calculate delay before next retry."""
        return self.backoff_base ** attempt

    def escalate_tier(self, current_tier, attempt):
        """Escalate to more powerful model on retry."""
        tiers = ["code_specialized", "balanced", "premium"]
        current_idx = tiers.index(current_tier)
        next_idx = min(current_idx + attempt, len(tiers) - 1)
        return tiers[next_idx]

def execute_with_retry(task, layer, stage):
    """Execute task with retry logic."""
    policy = RetryPolicy()
    attempt = 0

    while attempt < policy.max_retries:
        try:
            # Select model tier (escalate on retries)
            tier = policy.escalate_tier("balanced", attempt)
            model = select_model_from_tier(tier)

            # Execute
            result = execute_task(task, model)
            return result

        except Exception as e:
            if not policy.should_retry(e, attempt):
                # Non-retryable error - escalate immediately
                return escalate_to_human(task, error=e)

            # Wait before retry
            delay = policy.get_retry_delay(attempt)
            time.sleep(delay)
            attempt += 1

    # All retries exhausted
    return escalate_to_human(task, error="Max retries exceeded")
```

### 3.2 Circuit Breaker Pattern

```python
from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"      # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    """Prevent cascading failures by temporarily disabling failing agents."""

    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection."""

        if self.state == CircuitState.OPEN:
            # Check if timeout elapsed
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpen("Circuit breaker is OPEN, agent unavailable")

        try:
            result = func(*args, **kwargs)

            # Success - reset circuit
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.CLOSED
                self.failure_count = 0

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                log_alert(f"Circuit breaker OPEN for {func.__name__}")

            raise e

# Usage
claude_breaker = CircuitBreaker(failure_threshold=5, timeout=300)
codex_breaker = CircuitBreaker(failure_threshold=10, timeout=60)

def execute_with_breaker(task, tool):
    """Execute with appropriate circuit breaker."""
    breakers = {
        "claude-code": claude_breaker,
        "codex": codex_breaker
    }

    breaker = breakers.get(tool, CircuitBreaker())

    try:
        return breaker.call(execute_task, task, tool)
    except CircuitBreakerOpen:
        # Fall back to alternative tool
        return execute_task(task, fallback_tool)
```

---

## 4. Monitoring and Visualization

### 4.1 Real-Time Dashboard

```python
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

class SupervisorMonitor:
    """Provide real-time visibility into supervisor state."""

    def __init__(self, supervisor):
        self.supervisor = supervisor

    @app.route("/")
    def dashboard(self):
        """Render supervisor dashboard."""
        return render_template("dashboard.html")

    @app.route("/api/status")
    def get_status(self):
        """Get current supervisor status."""
        return jsonify({
            "running_tasks": len(self.supervisor.running_tasks),
            "queued_tasks": self.get_queue_depth(),
            "completed_today": self.get_completed_count(),
            "failed_today": self.get_failed_count(),
            "current_spend": self.get_daily_spend()
        })

    @app.route("/api/tasks")
    def get_tasks(self):
        """Get list of running tasks."""
        tasks = []
        for task_id, task in self.supervisor.running_tasks.items():
            tasks.append({
                "id": task_id,
                "layer": task["layer"],
                "stage": task["stage"],
                "started_at": task["started_at"],
                "duration": time.time() - task["started_at"]
            })
        return jsonify(tasks)

    def emit_task_update(self, task_id, event, data):
        """Emit real-time update via WebSocket."""
        socketio.emit("task_update", {
            "task_id": task_id,
            "event": event,
            "data": data
        })
```

### 4.2 Task Dependency Visualization

```python
import graphviz

def visualize_task_graph(handoffs):
    """Generate visualization of task dependencies."""

    dot = graphviz.Digraph(comment='Task Dependency Graph')

    # Add nodes
    for handoff in handoffs:
        dot.node(handoff["id"], f"{handoff['layer']}/{handoff['stage']}")

    # Add edges
    for handoff in handoffs:
        for parent_id in handoff.get("parentIds", []):
            dot.edge(parent_id, handoff["id"])

    # Render
    dot.render('task_graph', format='svg', view=True)
```

---

## 5. Supervisor Selection Guide

| Pattern | Best For | Complexity | Scalability |
|---------|----------|------------|-------------|
| File-Watching | Single machine, dev | Low | Single machine |
| Queue-Based | Distributed, production | Medium | Horizontal scaling |
| LangGraph | Complex workflows, auditing | High | Moderate |

**Recommendation:**
1. Start with **File-Watching** for development and prototyping
2. Move to **Queue-Based** for production with multiple workers
3. Use **LangGraph** when explicit workflow control is critical

All patterns can be combined or evolved incrementally.
