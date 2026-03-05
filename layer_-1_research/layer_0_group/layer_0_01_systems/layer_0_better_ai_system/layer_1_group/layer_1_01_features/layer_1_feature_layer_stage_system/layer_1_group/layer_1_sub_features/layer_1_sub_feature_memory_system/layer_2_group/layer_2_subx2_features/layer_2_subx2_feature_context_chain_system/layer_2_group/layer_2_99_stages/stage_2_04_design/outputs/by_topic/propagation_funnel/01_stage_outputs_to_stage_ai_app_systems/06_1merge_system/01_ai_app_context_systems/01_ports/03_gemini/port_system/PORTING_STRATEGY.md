---
resource_id: "3453ff95-f208-48a9-bf61-adcadb4f7003"
resource_type: "output"
resource_name: "PORTING_STRATEGY"
---
# Gemini — Porting Strategy for 0AGNOSTIC.md and .0agnostic/ System

**Date**: 2026-02-27
**Focus**: How to port both the 0AGNOSTIC.md file AND .0agnostic/ directory structure into Gemini's native system

---

## Overview

Porting to Gemini means mapping two things:

1. **0AGNOSTIC.md file** (identity, triggers, resources) → Gemini's **system instructions** and **configuration**
2. **.0agnostic/ directory** (rules, knowledge, protocols, skills) → Gemini's **runtime strategy** (session management, error handling, cost tracking, file organization)

Gemini has no native `.0agnostic/` equivalent — you must manually implement these patterns in your application code and configuration.

---

## Part 1: Porting 0AGNOSTIC.md → System Instructions & Configuration

### Step 1: Extract STATIC Context

Read the STATIC section of your 0AGNOSTIC.md:

```markdown
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──
## Identity
[Your identity: role, scope, parent, children]

# ── Current Status ──
## Current Status
[Substantive status: phase, key findings, readiness]
```

### Step 2: Map to Gemini System Instructions

The STATIC section becomes your **system instruction**:

```python
system_instruction = """
# Identity
[Your identity from 0AGNOSTIC.md]

## Role
[Your role: expert developer, researcher, code reviewer, etc.]

## Scope
[What you can and should do: domains, responsibilities]

## Parent Context
[Brief reference to parent entity]

## Current Status
[Phase, key findings, what's ready]

## Key Behaviors
[What you DO and what you DON'T DO]

## Triggers
[When this context applies, what actions to take]

## Key Concepts
[Domain vocabulary, important patterns]
"""
```

### Example: Identity Porting

**From 0AGNOSTIC.md (STATIC)**:
```markdown
## Identity

You are an expert Python data analyst.
- **Role**: Build and optimize data processing pipelines
- **Scope**: Python, pandas, numpy, data ETL
- **Parent**: data_systems entity
- **Children**: None

## Key Behaviors

### What You DO
- Optimize pandas operations for large datasets
- Suggest efficient algorithms
- Use type hints consistently

### What You DON'T DO
- Use data in unsafe ways (SQL injection-like patterns)
- Ignore performance implications
```

**To Gemini system instruction**:
```python
system_instruction = """
You are an expert Python data analyst.

## Role
Build and optimize data processing pipelines. Provide clear explanations for why you recommend specific approaches.

## Scope
Python, pandas, numpy, data ETL, performance optimization. You do NOT handle business logic outside data processing.

## Key Behaviors

### DO:
- Optimize pandas operations for large datasets
- Suggest efficient algorithms with justifications
- Use type hints consistently
- Include docstrings with example usage

### DON'T:
- Use data unsafely (SQL injection-like patterns)
- Ignore performance implications
- Over-engineer simple solutions
"""
```

### Step 3: Porting Triggers

STATIC triggers become **application-level conditional logic**:

**From 0AGNOSTIC.md**:
```markdown
## Triggers

| Situation | Action |
|-----------|--------|
| User asks about data | Load dashboard skill |
| Working with pandas | Load optimization protocol |
| Debugging performance | Load profiling knowledge |
```

**To Gemini Application**:
```python
def select_system_instruction(context):
    """Select system instruction based on user context."""

    if "data analysis" in context:
        return ANALYST_INSTRUCTION
    elif "code review" in context:
        return REVIEWER_INSTRUCTION
    elif "optimization" in context:
        return OPTIMIZER_INSTRUCTION
    else:
        return DEFAULT_INSTRUCTION

# When calling Gemini
selected_instruction = select_system_instruction(user_message)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    system_instruction=selected_instruction,
)
```

### Step 4: Porting Current Status

Include status in system instructions for context:

```python
system_instruction = """
[identity and role...]

## Current Status
**Phase**: Active data analysis | Last Updated: 2026-02-27
Dataset: 500M rows, parquet format. Optimizations: vectorized operations, chunked processing, memory pooling. Known issues: string operations slower than expected.

[rest of instruction...]
"""
```

This helps Gemini understand what's known, what's unknown, and where to focus.

---

## Part 2: Porting .0agnostic/ Directory → Application Implementation

The `.0agnostic/` directory doesn't have a native Gemini equivalent. You must implement these patterns in your application code.

### Mapping .0agnostic/ Directories

| .0agnostic/ Directory | Gemini Port | How |
|----------------------|-----------|-----|
| `01_knowledge/` | Documentation/comments in code + external docs referenced in system instruction | Reference docs in comments, pass relevant context to Gemini |
| `02_rules/static/` | Hardcoded application logic + system instruction constraints | Enforce in code before/after Gemini calls |
| `02_rules/dynamic/` | Conditional application logic + dynamic system instruction selection | Check triggers, select appropriate instruction |
| `03_protocols/` | Documented step-by-step procedures in code comments + implementation | Follow as pseudocode, document in comments |
| `04_episodic_memory/` | Session storage (database, file, in-memory) | Save conversation history locally |
| `05_handoff_documents/` | State serialization between sessions/agents | Save/load session state |
| `06_context_avenue_web/` (skills) | Modular functions/methods in your application | Implement as Python functions or classes |
| `07+_setup_dependant/` | Configuration files, environment variables | Load from config.json or env vars |

### Detailed Porting Strategy

#### 01_knowledge/ → Documentation + Context

**From .0agnostic/01_knowledge/**:
```
01_knowledge/
├── principles/
│   ├── principle_1_clarity.md
│   └── principle_2_performance.md
├── docs/
│   ├── data_format_guide.md
│   └── optimization_patterns.md
└── resources/
    └── templates/
        └── pipeline_template.py
```

**To Gemini App**:
```python
# documents/principles.md (local file)
"""
Principle 1: Code Clarity
All code must be readable. Prefer clear variable names over clever one-liners.

Principle 2: Performance
...
"""

# In your system instruction
system_instruction = """
...

## Principles
1. Code Clarity: All code must be readable
2. Performance: Optimize for user experience
3. Safety: Validate all inputs

See: documents/principles.md
"""

# In your code
class DataPipeline:
    """Build data pipelines following optimization patterns."""

    def process(self, data):
        """Process data following documented patterns.
        See: documents/optimization_patterns.md
        """
        pass
```

**How to use in Gemini**:
- Reference documents in system instruction
- Pass relevant excerpts as context when asking Gemini
- Gemini generates code following documented patterns

#### 02_rules/static/ → Enforced Application Logic

**From .0agnostic/02_rules/static/**:
```
02_rules/static/
├── data_validation.md
│   "All inputs must be validated before processing"
└── error_handling.md
    "All API calls must include retry logic"
```

**To Gemini App**:
```python
class DataProcessor:
    def process(self, data):
        # RULE: Data validation (static rule #1)
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be DataFrame")

        if data.empty:
            raise ValueError("Input cannot be empty")

        # Process
        result = self._do_process(data)

        # RULE: Validate output (static rule #2)
        assert len(result) > 0, "Output validation failed"

        return result

    def _do_process(self, data):
        # When asking Gemini for this implementation,
        # include system instruction:
        # "All code must validate inputs and outputs"
        pass
```

#### 02_rules/dynamic/ → Conditional Application Logic

**From .0agnostic/02_rules/dynamic/**:
```
02_rules/dynamic/
├── content_moderation/
│   "Load when user uploads content"
└── performance_profiling/
    "Load when response time exceeds threshold"
```

**To Gemini App**:
```python
class ContentHandler:
    def handle_user_input(self, data):
        # RULE: Dynamic content moderation (trigger: user_uploads_content)
        if self._is_content_upload(data):
            self._apply_content_moderation(data)

        # Process normally
        return self.process(data)

    def _apply_content_moderation(self, data):
        """Apply moderation rules when triggered."""
        # Load moderation system instruction
        moderation_instruction = """
        You are a content safety reviewer.
        Check for: harmful content, privacy violations, policy breaches.
        Output: safe|unsafe|review_needed
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Review this content: {data}",
            system_instruction=moderation_instruction,
        )

        if "unsafe" in response.text:
            raise ValueError("Content violates policy")
```

#### 03_protocols/ → Documented Procedures

**From .0agnostic/03_protocols/data_processing_protocol.md**:
```markdown
# Data Processing Protocol

## Step 1: Validate Input
- Check type is DataFrame
- Check no null values in key columns
- Check all columns present

## Step 2: Transform
- Apply business logic
- Log transformations

## Step 3: Validate Output
- Check shape is as expected
- Check for new nulls
- Check no data loss
```

**To Gemini App**:
```python
class DataProcessor:
    """Implements data_processing_protocol.md step-by-step."""

    def process(self, data):
        # STEP 1: Validate Input (from protocol)
        self._validate_input(data)

        # STEP 2: Transform
        result = self._transform(data)

        # STEP 3: Validate Output
        self._validate_output(result)

        return result

    def _validate_input(self, data):
        """Step 1: Validate Input.
        From: .0agnostic/03_protocols/data_processing_protocol.md
        """
        assert isinstance(data, pd.DataFrame), "Must be DataFrame"
        # ... rest of step 1 logic

    # When asking Gemini to implement _transform:
    # "Implement step 2 of the data_processing_protocol.
    #  See .0agnostic/03_protocols/data_processing_protocol.md"
```

#### 04_episodic_memory/ → Session Storage

**From .0agnostic/04_episodic_memory/**:
```
04_episodic_memory/sessions/
├── 2026-02-26-session-1.md
└── 2026-02-27-session-2.md
```

**To Gemini App**:
```python
class GeminiSession:
    """Manages conversation history and session state."""

    def __init__(self, session_id):
        self.session_id = session_id
        self.messages = []
        self.created_at = datetime.now()
        self.metadata = {}

    def save_session(self):
        """Save session to episodic memory."""
        session_file = f".0agnostic/04_episodic_memory/sessions/{self.session_id}.md"

        content = f"""# Session {self.session_id}
Created: {self.created_at}
Messages: {len(self.messages)}

## History
{self._format_messages()}

## Metadata
{json.dumps(self.metadata, indent=2)}
"""

        with open(session_file, 'w') as f:
            f.write(content)

    def load_session(self):
        """Load session from episodic memory."""
        session_file = f".0agnostic/04_episodic_memory/sessions/{self.session_id}.md"

        if os.path.exists(session_file):
            with open(session_file, 'r') as f:
                # Parse and restore messages
                pass

    def add_turn(self, user_message, assistant_response):
        """Record a turn in the session."""
        self.messages.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat(),
        })
        self.messages.append({
            "role": "assistant",
            "content": assistant_response,
            "timestamp": datetime.now().isoformat(),
        })
```

#### 05_handoff_documents/ → State Transfer

**From .0agnostic/05_handoff_documents/**:
```
05_handoff_documents/
├── 01_incoming/
│   └── 01_from_above/
│       └── context.md
└── 02_outgoing/
    └── 01_to_above/
        └── session_report.md
```

**To Gemini App**:
```python
class HandoffManager:
    """Manages state transfer between sessions/agents."""

    def create_outgoing_handoff(self, session_state):
        """Create handoff document for next session/agent."""

        report = f"""# Session Handoff Report

## Summary
{session_state.get('summary', '')}

## Key Findings
{session_state.get('findings', '')}

## Next Steps
{session_state.get('next_steps', '')}

## Session State
{json.dumps(session_state, indent=2)}
"""

        output_dir = ".0agnostic/05_handoff_documents/02_outgoing/01_to_above/"
        os.makedirs(output_dir, exist_ok=True)

        with open(f"{output_dir}session_report.md", 'w') as f:
            f.write(report)

    def load_incoming_handoff(self):
        """Load context from previous session/agent."""

        input_dir = ".0agnostic/05_handoff_documents/01_incoming/01_from_above/"

        if os.path.exists(f"{input_dir}context.md"):
            with open(f"{input_dir}context.md", 'r') as f:
                return f.read()

        return None
```

#### 06_context_avenue_web/05_skills/ → Modular Functions

**From .0agnostic/06_context_avenue_web/05_skills/data_validation/SKILL.md**:
```markdown
# Data Validation Skill

When to use: Before processing user data
Inputs: DataFrame, validation rules
Outputs: Boolean (valid/invalid) + error details
```

**To Gemini App**:
```python
class DataValidationSkill:
    """Implements data validation skill."""

    @staticmethod
    def validate(data, rules):
        """Validate data against rules.

        From: .0agnostic/06_context_avenue_web/05_skills/data_validation/
        When: Before processing user data
        """

        errors = []

        for rule_name, rule_func in rules.items():
            if not rule_func(data):
                errors.append(rule_name)

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "details": f"Failed rules: {', '.join(errors)}"
        }

# When asking Gemini to implement validation:
# "Use the data_validation_skill to validate user input.
#  See .0agnostic/06_context_avenue_web/05_skills/data_validation/"

def process_user_data(user_data):
    validation_result = DataValidationSkill.validate(
        user_data,
        rules={
            "is_dataframe": lambda d: isinstance(d, pd.DataFrame),
            "not_empty": lambda d: len(d) > 0,
            "has_required_columns": lambda d: all(col in d.columns for col in REQUIRED_COLUMNS),
        }
    )

    if not validation_result["valid"]:
        raise ValueError(f"Validation failed: {validation_result['details']}")
```

#### 07+_setup_dependant/ → Configuration

**From .0agnostic/07+_setup_dependant/gemini_config.json**:
```json
{
    "model": "gemini-2.5-flash",
    "temperature": 0.7,
    "max_tokens": 2048,
    "cache_strategy": "explicit",
    "budget_limit": 50.0,
    "retry_max_attempts": 3
}
```

**To Gemini App**:
```python
import json

class GeminiConfig:
    """Load configuration from setup_dependant."""

    def __init__(self, config_path=".0agnostic/07+_setup_dependant/gemini_config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    @property
    def model(self):
        return self.config.get("model", "gemini-2.5-flash")

    @property
    def temperature(self):
        return self.config.get("temperature", 0.7)

    @property
    def max_tokens(self):
        return self.config.get("max_tokens", 2048)

    @property
    def budget_limit(self):
        return self.config.get("budget_limit", 50.0)

# Usage
config = GeminiConfig()

response = client.models.generate_content(
    model=config.model,
    contents=user_message,
    system_instruction=system_instruction,
    generation_config={
        "temperature": config.temperature,
        "max_output_tokens": config.max_tokens,
    }
)
```

---

## Part 3: Complete Integration Example

Here's how to integrate everything together:

```python
import json
import os
from datetime import datetime
import anthropic

class GeminiApplication:
    """Complete Gemini application with 0AGNOSTIC.md + .0agnostic/ patterns."""

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.config = self._load_config()
        self.session_manager = SessionManager()
        self.budget = BudgetTracker(self.config["budget_limit"])

        # Load system instructions from 0AGNOSTIC.md
        self.instructions = {
            "analyst": self._load_instruction("analyst"),
            "reviewer": self._load_instruction("reviewer"),
            "default": self._load_instruction("default"),
        }

    def _load_config(self):
        """Load from 07+_setup_dependant/config.json"""
        with open(".0agnostic/07+_setup_dependant/gemini_config.json", 'r') as f:
            return json.load(f)

    def _load_instruction(self, instruction_type):
        """Load system instruction from file.

        Based on 0AGNOSTIC.md STATIC context.
        """
        path = f".0agnostic/06_context_avenue_web/01_file_based/02_aalang_markdown_integration/{instruction_type}.md"

        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()

        # Fallback: generate from 0AGNOSTIC.md
        return self._generate_default_instruction()

    def _generate_default_instruction(self):
        """Generate system instruction from 0AGNOSTIC.md."""

        # This would parse 0AGNOSTIC.md and extract STATIC section
        # For this example, returning a basic instruction
        return """
You are a helpful AI assistant.

## Current Status
Active and ready to help.

## Key Behaviors
- Provide clear, concise answers
- Explain trade-offs
- Admit uncertainty
"""

    def process_request(self, user_message):
        """Process user request with full system integration."""

        # RULE: Dynamic instruction selection (02_rules/dynamic)
        instruction = self._select_instruction(user_message)

        # RULE: Check budget before expensive request (static rule)
        estimated_cost = self._estimate_cost(user_message, instruction)
        if estimated_cost > self.budget.remaining():
            raise BudgetExceeded(f"Not enough budget. Need ${estimated_cost:.2f}")

        # Call Gemini with full context
        response = self.client.models.generate_content(
            model=self.config["model"],
            contents=user_message,
            system_instruction=instruction,
            generation_config={
                "temperature": self.config["temperature"],
                "max_output_tokens": self.config["max_tokens"],
            },
            cache_control={
                "type": "ephemeral",
            } if self.config.get("cache_strategy") == "explicit" else None,
        )

        # RULE: Track usage (dynamic rule)
        cost = self.budget.track_usage(response.usage_metadata)

        # SKILL: Save session (06_context_avenue_web/skills)
        self.session_manager.add_turn(user_message, response.text)

        return response.text

    def _select_instruction(self, user_message):
        """Select instruction based on triggers (02_rules/dynamic)."""

        if "analyze" in user_message.lower():
            return self.instructions["analyst"]
        elif "review" in user_message.lower():
            return self.instructions["reviewer"]
        else:
            return self.instructions["default"]

    def _estimate_cost(self, user_message, instruction):
        """Estimate cost before request."""

        input_tokens = len(user_message.split()) + len(instruction.split())
        output_estimate = self.config["max_tokens"]

        # Simplified: actual cost depends on model and caching
        if self.config["model"] == "gemini-2.5-flash":
            return (input_tokens * 0.075 + output_estimate * 0.30) / 1_000_000
        else:
            return (input_tokens * 3.0 + output_estimate * 12.0) / 1_000_000

    def save_state(self):
        """Save session for continuity (05_handoff_documents)."""
        self.session_manager.save_session()
        self.budget.save_state()


class SessionManager:
    """Manage conversation history (04_episodic_memory)."""

    def __init__(self):
        self.session_id = datetime.now().strftime("%Y-%m-%d-session")
        self.messages = []

    def add_turn(self, user_message, assistant_response):
        """Record a turn."""
        self.messages.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().isoformat(),
        })
        self.messages.append({
            "role": "assistant",
            "content": assistant_response,
            "timestamp": datetime.now().isoformat(),
        })

    def save_session(self):
        """Save to episodic memory (04_episodic_memory/sessions)."""

        session_file = f".0agnostic/04_episodic_memory/sessions/{self.session_id}.md"
        os.makedirs(os.path.dirname(session_file), exist_ok=True)

        content = f"# Session {self.session_id}\n\n"
        for msg in self.messages:
            role = msg["role"].upper()
            timestamp = msg["timestamp"]
            content += f"## {role} ({timestamp})\n{msg['content']}\n\n"

        with open(session_file, 'w') as f:
            f.write(content)


class BudgetTracker:
    """Track API costs (02_rules/dynamic)."""

    def __init__(self, limit):
        self.limit = limit
        self.spent = 0.0

    def track_usage(self, usage_metadata):
        """Record cost from Gemini response."""

        # Simplified cost calculation
        input_cost = usage_metadata.input_tokens * (0.075 / 1_000_000)
        output_cost = usage_metadata.output_tokens * (0.30 / 1_000_000)
        cost = input_cost + output_cost

        self.spent += cost

        if self.spent > self.limit * 0.8:
            print(f"⚠️ WARNING: 80% of budget consumed (${self.spent:.2f})")

        return cost

    def remaining(self):
        """Get remaining budget."""
        return self.limit - self.spent

    def save_state(self):
        """Save budget tracking (05_handoff_documents)."""

        state = {
            "limit": self.limit,
            "spent": self.spent,
            "remaining": self.remaining(),
            "timestamp": datetime.now().isoformat(),
        }

        output_dir = ".0agnostic/05_handoff_documents/02_outgoing/01_to_above/"
        os.makedirs(output_dir, exist_ok=True)

        with open(f"{output_dir}budget_report.json", 'w') as f:
            json.dump(state, f, indent=2)


# Usage
if __name__ == "__main__":
    app = GeminiApplication()

    response = app.process_request("Analyze this dataset: [data]")
    print(response)

    app.save_state()
```

---

## Part 4: Configuration File Template

Create `.0agnostic/07+_setup_dependant/gemini_config.json`:

```json
{
    "gemini": {
        "model": "gemini-2.5-flash",
        "temperature": 0.7,
        "max_tokens": 2048,
        "cache_strategy": "explicit",
        "cache_ttl_minutes": 5,
        "streaming": false
    },
    "budget": {
        "monthly_limit_usd": 50.0,
        "alert_threshold_percent": 80
    },
    "retry": {
        "max_attempts": 3,
        "initial_backoff_seconds": 1,
        "max_backoff_seconds": 32
    },
    "session": {
        "resumption_window_hours": 2,
        "auto_save": true,
        "save_directory": ".0agnostic/04_episodic_memory/sessions/"
    },
    "files": {
        "upload_directory": ".0agnostic/07+_setup_dependant/uploads/",
        "retention_hours": 48,
        "max_size_mb": 100
    }
}
```

---

## Part 5: Migration Checklist

- [ ] Extract STATIC section from 0AGNOSTIC.md
- [ ] Create system_instruction string
- [ ] Map triggers to application conditional logic
- [ ] Create `.0agnostic/07+_setup_dependant/gemini_config.json`
- [ ] Implement configuration loader (`GeminiConfig` class)
- [ ] Implement session manager (episodic memory)
- [ ] Implement budget tracker (cost monitoring)
- [ ] Implement handoff document manager
- [ ] Create protocol implementations as code comments
- [ ] Document rules in code (static + dynamic)
- [ ] Create skills as modular functions
- [ ] Test system instruction loading
- [ ] Test trigger selection logic
- [ ] Test budget enforcement
- [ ] Test session persistence
- [ ] Test cost tracking accuracy
- [ ] Document all mappings in comments

---

## Summary

Porting to Gemini requires:
1. **0AGNOSTIC.md STATIC** → System instruction (what the model knows)
2. **0AGNOSTIC.md DYNAMIC** → Application logic (what the app controls)
3. **02_rules/static/** → Enforced application logic (validation, error handling)
4. **02_rules/dynamic/** → Conditional application logic (trigger-based)
5. **03_protocols/** → Step-by-step procedures in code comments
6. **04_episodic_memory/** → Session storage (local file/database)
7. **05_handoff_documents/** → State serialization (between sessions)
8. **06_context_avenue_web/skills/** → Modular functions (reusable components)
9. **07+_setup_dependant/** → Configuration files (JSON, env vars)

Gemini has no native `.0agnostic/` equivalent — you implement these patterns in your application code using the architecture shown above.

