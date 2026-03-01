# Cursor Agent CLI — Porting Strategy for 0AGNOSTIC.md and .0agnostic/ System

**Date**: 2026-02-27
**Focus**: How to port both the 0AGNOSTIC.md file AND .0agnostic/ directory structure into Cursor Agent CLI

---

## Overview

Porting to Cursor Agent CLI is different from other tools because **Agent CLI doesn't have native 0AGNOSTIC.md support**. Instead, you implement the system through:

1. **0AGNOSTIC.md → Task Definitions** (what tasks to delegate)
2. **.0agnostic/ → Application Code + Configuration** (how agents execute tasks)

Unlike Claude Code or Cursor IDE, Agent CLI has **no built-in context loading** — you write code that manages context.

---

## Part 1: Porting 0AGNOSTIC.md → Task Definitions

### Step 1: Extract Identity & Scope

**From 0AGNOSTIC.md**:
```markdown
## Identity
You are an expert Python developer.
- **Role**: Build and optimize data processing pipelines
- **Scope**: Python, pandas, numpy, refactoring, performance optimization
```

**To Agent Task Definitions**:
```bash
# Ideal task: Clear scope, specific deliverable
cursor agent "Refactor src/etl.py to use async/await. \
  Replace all Promise chains with async/await syntax. \
  Keep all error handling intact. \
  Tests must pass."

# Bad task: Vague scope
cursor agent "Improve the data processing code"

# Better: Specific scope with context
cursor agent "Optimize pandas operations in src/pipelines/load.py. \
  Current: iterrows() loop (slow). \
  Target: Vectorized operations. \
  Verify: Run benchmarks in tests/perf_test.py"
```

**Key Principle**: Agent tasks must be **specific, bounded, and verifiable**. Vague tasks fail.

### Step 2: Map Triggers to Task Types

**From 0AGNOSTIC.md TRIGGERS**:
```markdown
## Triggers

| Situation | Action |
|-----------|--------|
| User asks to refactor | Delegate to agent |
| Performance issue | Delegate to agent |
| Bug needs fixing | Delegate to agent |
```

**To Agent Task Types**:

```python
def should_delegate_to_agent(user_request):
    """Determine if task should be delegated to Agent."""

    refactoring_triggers = [
        "refactor", "clean up", "reorganize", "restructure"
    ]
    optimization_triggers = [
        "optimize", "performance", "slow", "bottleneck"
    ]
    bug_triggers = [
        "fix", "bug", "broken", "error"
    ]

    request_lower = user_request.lower()

    if any(trigger in request_lower for trigger in refactoring_triggers):
        return ("refactoring", extract_scope(user_request))
    elif any(trigger in request_lower for trigger in optimization_triggers):
        return ("optimization", extract_scope(user_request))
    elif any(trigger in request_lower for trigger in bug_triggers):
        return ("bug_fix", extract_scope(user_request))

    return None  # Don't delegate

def extract_scope(user_request):
    """Extract specific files, functions, or scope."""
    # Parse user request to find files mentioned
    # Example: "Refactor src/auth.py" → ["src/auth.py"]
    pass
```

### Step 3: Create Task Context from 0AGNOSTIC.md

Every agent task needs context. Extract from 0AGNOSTIC.md:

```python
class TaskContext:
    """Context for agent execution from 0AGNOSTIC.md."""

    def __init__(self):
        # From STATIC section
        self.identity = """
You are an expert Python developer specializing in data pipelines.
- Optimize for performance
- Write clear, documented code
- Follow project conventions
"""

        # From TRIGGERS
        self.triggers = {
            "refactoring": "Use vectorization patterns",
            "optimization": "Profile before optimizing",
            "bug_fix": "Add test case first, then fix",
        }

        # From KEY BEHAVIORS
        self.do = [
            "Optimize pandas with vectorization",
            "Use type hints",
            "Test thoroughly"
        ]
        self.dont = [
            "Use unsafe operations",
            "Ignore performance",
            "Skip documentation"
        ]

        # From CURRENT STATUS
        self.current_status = """
Project is in active data optimization phase.
Current bottleneck: String operations in pipeline.
Recent achievement: 50% query optimization.
"""

def create_agent_prompt(task_description, task_type):
    """Create agent prompt with context from 0AGNOSTIC.md."""

    context = TaskContext()

    prompt = f"""
{context.identity}

## Task Type: {task_type}
Context for this type: {context.triggers.get(task_type, '')}

## Your Task
{task_description}

## Project Status
{context.current_status}

## Key Guidelines
DO:
{chr(10).join('- ' + item for item in context.do)}

DON'T:
{chr(10).join('- ' + item for item in context.dont)}

## Success Criteria
- All tests passing
- Performance improved or maintained
- Code follows project conventions
"""

    return prompt
```

---

## Part 2: Porting .0agnostic/ → Application Code + Configuration

The `.0agnostic/` directory becomes **application code** that Agent CLI calls. You write the code; Agent CLI executes it.

### Mapping .0agnostic/ Directories

| .0agnostic/ Directory | Agent CLI Port | Implementation |
|----------------------|----------------|-----------------|
| `01_knowledge/` | Python docstrings + comments | Document knowledge in code |
| `02_rules/static/` | Application validation code | Enforce rules before/after agent |
| `02_rules/dynamic/` | Task routing logic | Select appropriate agent behavior |
| `03_protocols/` | Python functions implementing protocol | Step-by-step procedures as code |
| `04_episodic_memory/` | Local session storage | Save session history to JSON/DB |
| `05_handoff_documents/` | State serialization | Save/load agent state |
| `06_context_avenue_web/skills/` | Reusable Python functions | Skills as importable modules |
| `07+_setup_dependant/` | config.json + environment | Agent configuration |

### Detailed Implementation

#### 01_knowledge/ → Python Docstrings + Code Comments

**From .0agnostic/01_knowledge/optimization_patterns.md**:
```markdown
# Optimization Patterns

## Vectorization Pattern
Use pandas vectorization instead of loops.

```python
# Bad
for idx, row in df.iterrows():
    df.loc[idx, 'result'] = process(row)

# Good
df['result'] = df.apply(process, axis=1)
```
```

**To Python Code**:
```python
"""
Optimization module — knowledge from .0agnostic/01_knowledge/

Key Pattern: Vectorization
Use pandas vectorization instead of loops for performance.
"""

def vectorize_operations(df, operation):
    """
    Apply operation using vectorization (fast).

    From: .0agnostic/01_knowledge/optimization_patterns.md

    Args:
        df: Pandas DataFrame
        operation: Function to apply

    Returns:
        DataFrame with operation applied

    Example:
        >>> df['result'] = vectorize_operations(df, lambda row: row['a'] + row['b'])
    """
    return df.apply(operation, axis=1)

def loop_operations(df, operation):
    """
    Apply operation using loop (slow).

    BAD PATTERN - Use vectorize_operations instead!

    From: .0agnostic/01_knowledge/optimization_patterns.md
    """
    for idx, row in df.iterrows():
        df.loc[idx, 'result'] = operation(row)
    return df
```

#### 02_rules/static/ → Validation Code

**From .0agnostic/02_rules/static/data_validation.md**:
```
"All inputs must be validated before processing"
```

**To Python Code**:
```python
"""
Static rules enforcement for Agent CLI.

From: .0agnostic/02_rules/static/
"""

class DataValidationRule:
    """Enforce: All inputs must be validated."""

    @staticmethod
    def validate_before_processing(df):
        """Validate input DataFrame before any processing."""

        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be DataFrame")

        if df.empty:
            raise ValueError("Input cannot be empty")

        required_columns = ['id', 'value', 'timestamp']
        missing = set(required_columns) - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        if df.isnull().any().any():
            raise ValueError("Input contains null values")

        return True  # Valid

def agent_task_wrapper(task_func):
    """Decorator: Apply static rules before agent execution."""

    def wrapper(*args, **kwargs):
        # Rule 1: Validate inputs
        if 'df' in kwargs:
            DataValidationRule.validate_before_processing(kwargs['df'])

        # Rule 2: Execute task
        result = task_func(*args, **kwargs)

        # Rule 3: Validate output
        if isinstance(result, pd.DataFrame):
            DataValidationRule.validate_before_processing(result)

        return result

    return wrapper
```

#### 02_rules/dynamic/ → Task Routing

**From .0agnostic/02_rules/dynamic/**:
```
"Load optimization context when user asks for performance"
```

**To Python Code**:
```python
"""
Dynamic rules routing for Agent CLI.

From: .0agnostic/02_rules/dynamic/
"""

class DynamicRules:
    """Route tasks based on triggers."""

    @staticmethod
    def should_load_optimization_rules(task_description):
        """Trigger: Load optimization context."""
        triggers = ['optimize', 'performance', 'slow', 'bottleneck']
        return any(t in task_description.lower() for t in triggers)

    @staticmethod
    def should_load_refactoring_rules(task_description):
        """Trigger: Load refactoring context."""
        triggers = ['refactor', 'clean up', 'reorganize']
        return any(t in task_description.lower() for t in triggers)

def select_agent_context(task_description):
    """Dynamically select context based on task."""

    context = ""

    if DynamicRules.should_load_optimization_rules(task_description):
        context += OPTIMIZATION_CONTEXT

    if DynamicRules.should_load_refactoring_rules(task_description):
        context += REFACTORING_CONTEXT

    return context
```

#### 03_protocols/ → Step-by-Step Functions

**From .0agnostic/03_protocols/data_processing_protocol.md**:
```markdown
# Step 1: Validate Input
- Check type is DataFrame

# Step 2: Transform
- Apply business logic

# Step 3: Validate Output
- Check shape as expected
```

**To Python Code**:
```python
"""
Protocols — step-by-step procedures from .0agnostic/03_protocols/
"""

def data_processing_protocol(input_data, transform_func):
    """
    Execute data processing protocol step-by-step.

    From: .0agnostic/03_protocols/data_processing_protocol.md

    Steps:
    1. Validate input
    2. Transform data
    3. Validate output
    """

    # STEP 1: Validate Input
    print("[PROTOCOL] Step 1: Validating input...")
    if not isinstance(input_data, pd.DataFrame):
        raise ValueError("Input must be DataFrame")
    if input_data.empty:
        raise ValueError("Input cannot be empty")

    # STEP 2: Transform
    print("[PROTOCOL] Step 2: Transforming data...")
    try:
        result = transform_func(input_data)
    except Exception as e:
        raise RuntimeError(f"Transform failed: {e}")

    # STEP 3: Validate Output
    print("[PROTOCOL] Step 3: Validating output...")
    if result.empty:
        raise ValueError("Output is empty (data loss)")
    if len(result) != len(input_data):
        raise ValueError("Output size differs from input (data loss)")

    print("[PROTOCOL] All steps completed successfully")
    return result
```

#### 04_episodic_memory/ → Session Storage

**From .0agnostic/04_episodic_memory/sessions/**:
```
sessions/2026-02-27-session.md
"Refactored 15 functions, tests passing"
```

**To Python Code**:
```python
"""
Episodic memory management for Agent CLI.

From: .0agnostic/04_episodic_memory/
"""

class SessionManager:
    """Manage episodic memory (session history)."""

    def __init__(self, session_id):
        self.session_id = session_id
        self.history = []
        self.session_file = f".0agnostic/04_episodic_memory/sessions/{session_id}.md"

    def save_session(self):
        """Save session to episodic memory."""

        content = f"# Session {self.session_id}\n\n"

        for turn in self.history:
            content += f"## Turn {turn['number']}\n"
            content += f"**Task**: {turn['task']}\n"
            content += f"**Result**: {turn['result']}\n"
            content += f"**Status**: {turn['status']}\n\n"

        with open(self.session_file, 'w') as f:
            f.write(content)

    def add_turn(self, task, result, status):
        """Record a turn in the session."""
        turn_number = len(self.history) + 1
        self.history.append({
            "number": turn_number,
            "task": task,
            "result": result,
            "status": status,
        })
```

#### 05_handoff_documents/ → State Serialization

**From .0agnostic/05_handoff_documents/02_outgoing/**:
```
02_outgoing/01_to_above/session_report.md
"Completed tasks, next steps"
```

**To Python Code**:
```python
"""
Handoff document management for Agent CLI.

From: .0agnostic/05_handoff_documents/
"""

class HandoffManager:
    """Create state snapshots for resumption."""

    @staticmethod
    def create_handoff(session_state):
        """Create handoff document."""

        handoff = {
            "session_id": session_state['id'],
            "completed_tasks": session_state['completed'],
            "current_task": session_state['current'],
            "next_steps": session_state['next'],
            "timestamp": datetime.now().isoformat(),
        }

        output_path = ".0agnostic/05_handoff_documents/02_outgoing/01_to_above/session_report.json"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w') as f:
            json.dump(handoff, f, indent=2)

    @staticmethod
    def load_handoff():
        """Load previous handoff document."""

        input_path = ".0agnostic/05_handoff_documents/01_incoming/01_from_above/session_report.json"

        if os.path.exists(input_path):
            with open(input_path, 'r') as f:
                return json.load(f)

        return None
```

#### 07+_setup_dependant/ → Configuration

**From .0agnostic/07+_setup_dependant/agent_config.json**:
```json
{
    "default_model": "claude-opus-4-6",
    "max_retries": 3,
    "approval_mode": "interactive",
    "workspace": "~/.cursor/"
}
```

**To Python Code**:
```python
"""
Agent CLI configuration from .0agnostic/07+_setup_dependant/
"""

import json
import os

class AgentConfig:
    """Load Agent CLI configuration."""

    def __init__(self, config_path=".0agnostic/07+_setup_dependant/agent_config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """Load configuration file."""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return self._default_config()

    def _default_config(self):
        """Return default configuration."""
        return {
            "default_model": "claude-opus-4-6",
            "max_retries": 3,
            "approval_mode": "interactive",
            "workspace": "~/.cursor/",
        }

    @property
    def model(self):
        return self.config.get("default_model", "claude-opus-4-6")

    @property
    def max_retries(self):
        return self.config.get("max_retries", 3)

    @property
    def approval_mode(self):
        return self.config.get("approval_mode", "interactive")
```

---

## Part 3: Complete Agent CLI Integration Example

```python
"""
Complete Cursor Agent CLI integration with 0AGNOSTIC.md and .0agnostic/ patterns.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import json
import os
import subprocess

class CursorAgentIntegration:
    """Integrate Agent CLI with 0AGNOSTIC.md system."""

    def __init__(self):
        self.config = AgentConfig()
        self.session_manager = SessionManager(f"session-{datetime.now().isoformat()}")
        self.handoff_manager = HandoffManager()

    def execute_agent_task(self, task_description: str) -> str:
        """Execute task via Agent CLI with full context."""

        # Load previous context (handoff)
        previous_state = self.handoff_manager.load_handoff()

        # Select dynamic rules based on task
        dynamic_context = DynamicRules.select_context(task_description)

        # Build full prompt with 0AGNOSTIC.md context
        full_prompt = f"""
# Task Context from 0AGNOSTIC.md

{TaskContext().identity}

# Dynamic Context
{dynamic_context}

# Your Task
{task_description}

# Previous Progress
{json.dumps(previous_state) if previous_state else 'None'}
"""

        # Execute via Agent CLI
        print(f"[AGENT] Starting task: {task_description}")
        result = subprocess.run([
            "cursor", "agent",
            f"--model={self.config.model}",
            f"--approval={self.config.approval_mode}",
            full_prompt
        ], capture_output=True, text=True)

        if result.returncode != 0:
            status = "failed"
            result_text = result.stderr
        else:
            status = "success"
            result_text = result.stdout

        # Record in episodic memory
        self.session_manager.add_turn(task_description, result_text, status)

        # Apply static rules validation
        if status == "success":
            try:
                # Validate result followed rules
                self._validate_rules(result_text)
            except Exception as e:
                print(f"[VALIDATION] Failed: {e}")
                status = "needs_review"

        # Save handoff for next session
        self.handoff_manager.create_handoff({
            "id": self.session_manager.session_id,
            "completed": self.session_manager.history,
            "current": task_description,
            "next": self._suggest_next_steps(result_text),
        })

        return result_text

    def _validate_rules(self, result: str):
        """Apply static rules validation to result."""
        # Example: Check that result doesn't violate rules
        if "import" in result.lower() and "hardcoded" in result.lower():
            raise ValueError("Result violates rule: no hardcoded secrets")

    def _suggest_next_steps(self, result: str) -> list:
        """Suggest next steps based on result."""
        # Parse result to suggest follow-up tasks
        return ["Review changes", "Run tests", "Merge"]
```

---

## Part 4: Configuration File Template

Create `.0agnostic/07+_setup_dependant/agent_config.json`:

```json
{
    "agent_cli": {
        "default_model": "claude-opus-4-6",
        "approval_mode": "interactive",
        "max_retries": 3,
        "timeout_seconds": 300,
        "workspace": "~/.cursor/"
    },
    "task_defaults": {
        "require_plan": true,
        "require_approval_for": ["destructive", "database", "security"],
        "auto_approve": ["formatting", "documentation"]
    },
    "mcp_servers": {
        "enabled": ["canvas", "github", "tavily"],
        "disabled": []
    }
}
```

---

## Part 5: Migration Checklist

- [ ] Extract identity from 0AGNOSTIC.md
- [ ] Create TaskContext class from STATIC section
- [ ] Create task routing functions from TRIGGERS
- [ ] Create validation rules from 02_rules/static/
- [ ] Create dynamic routing from 02_rules/dynamic/
- [ ] Create protocol functions from 03_protocols/
- [ ] Create SessionManager from 04_episodic_memory/
- [ ] Create HandoffManager from 05_handoff_documents/
- [ ] Create skill functions from 06_skills/
- [ ] Create AgentConfig from 07+_setup_dependant/
- [ ] Create `.0agnostic/07+_setup_dependant/agent_config.json`
- [ ] Test task execution with context
- [ ] Test session persistence
- [ ] Test handoff document creation/loading
- [ ] Test static rules validation
- [ ] Test dynamic rule routing
- [ ] Create integration test with real Agent CLI
- [ ] Document your agent task patterns (what works, what doesn't)
- [ ] Create agent task templates for common use cases

---

## Summary

Porting to Cursor Agent CLI requires you to:

1. **Extract task definitions** from 0AGNOSTIC.md (what to delegate)
2. **Build application code** that implements .0agnostic/ patterns (how to delegate)
3. **Create configuration** that guides agent execution
4. **Implement validation** to ensure agent results follow your rules
5. **Manage state** across agent sessions (episodic memory + handoff)

Unlike other tools, Agent CLI has **no native context loading** — you write the code that manages context. This gives you **maximum control** but requires more implementation.

The key insight: **Agent tasks must be specific and bounded**. Vague tasks fail. Use the context from 0AGNOSTIC.md to make tasks specific.

