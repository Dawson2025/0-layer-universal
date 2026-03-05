---
resource_id: "2c419e13-3343-4c2f-bd4e-3cad02cff529"
resource_type: "readme
document"
resource_name: "README"
---
# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "e528d158-2506-4248-8486-3e22d7d79060" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "df7927b9-2967-439a-bac7-e033cb1011c8" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "0ea3c288-5726-4316-8ce0-68894f43b6b8" -->
## Quick Reference

<!-- section_id: "008fe1d2-bb08-4d83-bb68-dd5992ed6297" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "f4492437-1a7d-4864-b481-25b8fccf2b4d" -->
### Log Location in Layer/Stage Structure

```
<layer_N>/<N.99_stages>/<stage_M>/ai_agent_system/logs/
  ├── manager.log          # Manager decisions and handoff creation
  ├── workers/
  │   ├── codex.log       # Worker execution logs
  │   ├── gemini.log      # Worker execution logs
  │   └── claude.log      # Worker execution logs
  ├── handoffs/
  │   ├── incoming.log    # Received handoffs
  │   └── outgoing.log    # Created handoffs
  └── metrics.jsonl       # Structured metrics
```

<!-- section_id: "c9444d7b-1fbb-4901-a4ed-66b12daff8a4" -->
### Structured Logging Format

All log entries MUST include:

```json
{
  "timestamp": "2025-12-24T10:30:45.123Z",
  "level": "INFO",
  "logger": "supervisor.task_executor",
  "message": "Task completed successfully",
  "context": {
    "task_id": "task-L2-auth-impl-20251224-103045",
    "layer": 2,
    "stage": "implementation",
    "tool": "codex",
    "model": "codestral",
    "handoff_id": "handoff-20251224-102030"
  },
  "metadata": {
    "duration_ms": 12450,
    "tokens_used": 2340,
    "cost_usd": 0.0234,
    "files_modified": 3,
    "retry_count": 0
  },
  "trace_id": "trace-L1-auth-system",
  "span_id": "span-impl-login-component"
}
```

---

<!-- section_id: "e2155b1c-ca0f-466b-b38a-21cf5fdc3b6d" -->
## Layer-Specific Logging Requirements

<!-- section_id: "67d5e75f-84fd-4198-86d5-f795dc612051" -->
### Layer 0 (Universal) - L0 Manager

**Responsibilities**:
- Log all user requests and initial handoff creation
- Track cross-layer handoff propagation
- Monitor system-wide budget and resource usage
- Audit all L0 → L1 delegations

**Key Events**:
```json
{
  "event": "request.received",
  "layer": 0,
  "stage": "request_gathering",
  "request_summary": "Implement authentication system",
  "estimated_complexity": "high",
  "initial_budget": 10.00
}
```

<!-- section_id: "7952015e-6198-4895-b746-b7d1ae156f58" -->
### Layer 1 (Project) - L1 Manager

**Responsibilities**:
- Log project-level planning decisions
- Track L1 → L2 feature delegation
- Monitor project budget allocation
- Audit tool selection for features

**Key Events**:
```json
{
  "event": "feature.delegated",
  "layer": 1,
  "stage": "planning",
  "feature": "login-component",
  "delegated_to_layer": 2,
  "allocated_budget": 2.50,
  "selected_tool": "codex"
}
```

<!-- section_id: "9f905c94-6276-487e-9a1e-35aaba79cea6" -->
### Layer 2 (Features) - L2 Manager

**Responsibilities**:
- Log feature implementation decisions
- Track L2 → L3 component delegation
- Monitor feature-level quality metrics
- Audit component integration

**Key Events**:
```json
{
  "event": "component.created",
  "layer": 2,
  "stage": "implementation",
  "component": "LoginForm",
  "files_created": ["LoginForm.tsx", "LoginForm.test.tsx"],
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85
  }
}
```

<!-- section_id: "43e85556-3930-44a0-b56e-c894064f4eb9" -->
### Layer 3 (Components) - L3 Workers

**Responsibilities**:
- Log all file operations (create, modify, delete)
- Track code quality metrics
- Monitor test execution and results
- Audit all tool usage

**Key Events**:
```json
{
  "event": "file.written",
  "layer": 3,
  "stage": "implementation",
  "file_path": "src/components/LoginForm.tsx",
  "lines_added": 120,
  "tool": "write_file",
  "verified": true
}
```

---

<!-- section_id: "0b9eb7ac-f0f3-4d25-b406-cc8cc4452278" -->
## Handoff Logging

<!-- section_id: "dac5af25-0498-4520-909c-287ebfa2b72a" -->
### Incoming Handoff

When a manager/worker receives a handoff:

```json
{
  "event": "handoff.received",
  "handoff_id": "handoff-20251224-102030",
  "layer": 2,
  "stage": "implementation",
  "from": {
    "layer": 1,
    "stage": "planning"
  },
  "task": "Implement login form component",
  "constraints": ["TypeScript", "React", "Accessibility"],
  "artifacts": ["design-spec.md", "wireframes.png"]
}
```

<!-- section_id: "25f84d5b-e55a-42ef-812c-ed9e74c26375" -->
### Outgoing Handoff

When a manager/worker creates a handoff:

```json
{
  "event": "handoff.created",
  "handoff_id": "handoff-20251224-103045",
  "layer": 2,
  "stage": "implementation",
  "to": {
    "layer": 1,
    "stage": "review"
  },
  "status": "completed",
  "results": {
    "files_created": 3,
    "tests_passed": true,
    "quality_score": 0.92
  },
  "artifacts": ["LoginForm.tsx", "test-results.json"]
}
```

---

<!-- section_id: "e756297e-3c6c-405d-92e1-cf7e8a0c4805" -->
## Manager/Worker Pattern Observability

<!-- section_id: "9014a19f-0e32-47ef-abe0-9d6d5c4217de" -->
### Manager Spawning Workers

```json
{
  "event": "worker.spawned",
  "manager": {
    "layer": 2,
    "stage": "implementation"
  },
  "worker": {
    "worker_id": "worker-codex-20251224-103045",
    "tool": "codex",
    "model": "codestral",
    "task_id": "task-L3-login-impl",
    "estimated_cost": 0.50
  },
  "parallel_count": 3,
  "parallel_group": "login-components"
}
```

<!-- section_id: "3885136b-a8a0-43db-98ed-b63ed19710cd" -->
### Worker Reporting Results

```json
{
  "event": "worker.completed",
  "worker_id": "worker-codex-20251224-103045",
  "task_id": "task-L3-login-impl",
  "status": "success",
  "duration_ms": 8500,
  "tokens": {"input": 1200, "output": 850, "total": 2050},
  "cost_usd": 0.0205,
  "artifacts": {
    "files_created": ["LoginForm.tsx"],
    "files_modified": ["index.ts"]
  }
}
```

---

<!-- section_id: "53f31fb8-f118-4907-9bd2-1fe34cd52797" -->
## Metrics Collection

<!-- section_id: "4c892307-b331-4965-a3ea-27b520ec6f73" -->
### Cost Tracking

Track costs at every layer/stage boundary:

```json
{
  "metric": "cost",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 2,
  "stage": "implementation",
  "tool": "codex",
  "model": "codestral",
  "cost_usd": 0.0205,
  "budget_remaining": {
    "daily": 45.50,
    "task_limit": 1.95
  }
}
```

<!-- section_id: "4ea788cd-fd60-4e1b-8369-a69452337358" -->
### Quality Metrics

Track code quality per component:

```json
{
  "metric": "quality",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 3,
  "component": "LoginForm",
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85,
    "complexity_score": 12,
    "type_errors": 0
  }
}
```

<!-- section_id: "61405b0d-33ff-4e2c-ac5e-1b66c650c940" -->
### Performance Metrics

Track task execution performance:

```json
{
  "metric": "performance",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 2,
  "stage": "implementation",
  "task_duration_ms": 8500,
  "parallel_workers": 3,
  "total_cost_usd": 0.62
}
```

---

<!-- section_id: "ac720678-de04-4ab5-9009-827553d76ba0" -->
## Distributed Tracing

<!-- section_id: "0d3aaaff-e8a8-48da-86f6-0436834043af" -->
### Trace Hierarchy

Traces show the full workflow from L0 to L3+:

```
trace-L1-auth-system (5m 32s, $4.50)
├─ span-L1-request (45s, $0.50) [gemini-pro-2]
├─ span-L1-instructions (1m 20s, $0.80) [gemini-pro-2]
├─ span-L1-planning (2m 10s, $1.20) [claude-sonnet-4.5]
└─ span-L2-implementation (1m 17s, $2.00)
   ├─ span-L3-login-impl (25s, $0.20) [codestral]
   ├─ span-L3-reset-impl (30s, $0.25) [codestral]
   └─ span-L3-testing (22s, $0.15) [starcoder2]
```

<!-- section_id: "2fc7fa72-9fdf-457e-ab5f-9832819a3bdd" -->
### Trace Propagation

Every handoff carries trace context:

```json
{
  "handoff_id": "handoff-20251224-102030",
  "trace_context": {
    "trace_id": "trace-L1-auth-system",
    "parent_span_id": "span-L1-planning",
    "span_id": "span-L2-implementation"
  }
}
```

---

<!-- section_id: "f081d144-e13f-44b0-9c4c-75197b5eafa2" -->
## Log Storage Strategy

<!-- section_id: "1e2db6aa-1e27-42c4-a727-cde10fd262e4" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "1d003078-e95a-4901-8097-4fa407b26c3a" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "a88c7577-260b-42a1-9cc3-89cc308d6d2c" -->
## Audit Trail Requirements

All manager decisions and worker actions MUST be logged with:

1. **Timestamp**: ISO 8601 format with millisecond precision
2. **Agent Identity**: Layer, stage, tool, model
3. **Action Type**: read/write/execute/delegate/escalate
4. **Resource**: File path, API endpoint, handoff ID
5. **Outcome**: success/failure with error details
6. **Cost**: Estimated and actual cost in USD
7. **Approver**: If human approval was required

---

<!-- section_id: "0b8211b2-61b7-4866-be97-b89ea48b3707" -->
## Examples

<!-- section_id: "bbba0718-515a-4351-ba42-e8e65cb64c2b" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "369f22bf-6f31-4465-8fb1-654da2e916b4" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "4fef8cdb-e0d3-4bab-ae17-b738d33cbeba" -->
## Integration Points

<!-- section_id: "081a459f-3728-4461-bb51-688268894293" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "5acdeb81-a1fe-4a8f-81df-129c832c0846" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "4d386702-c7e0-44a2-9efd-ce0ae005a60f" -->
## Tools and Libraries

<!-- section_id: "cff25fd7-56cc-4b62-ae91-97e2b6c049c7" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "c61b08bb-756a-4b30-865d-c503e61c382c" -->
### Example Configuration

```python
import logging
import json
from datetime import datetime

class StructuredLogger:
    """Structured logger for AI Manager Hierarchy."""

    def __init__(self, layer, stage, tool=None):
        self.layer = layer
        self.stage = stage
        self.tool = tool
        self.logger = logging.getLogger(f"L{layer}.{stage}")

    def log_event(self, event_type, **kwargs):
        """Log a structured event."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": "INFO",
            "event": event_type,
            "context": {
                "layer": self.layer,
                "stage": self.stage,
                "tool": self.tool
            },
            **kwargs
        }
        self.logger.info(json.dumps(entry))

# Usage
logger = StructuredLogger(layer=2, stage="implementation", tool="codex")
logger.log_event("task.started", task_id="task-L2-auth-impl", estimated_cost=0.50)
```

---

<!-- section_id: "d5526dc4-ff51-4e8c-9adb-fedd48ed1259" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "d6b435b5-aabc-4db2-909b-01df1ccc6d9d" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active

---

<!-- section_id: "e4f5bdcf-6d26-47f1-a207-38ee29cb3f75" -->
## Legacy Universal Protocols Source

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "4e16e188-cc39-4c11-b8eb-1db74c77ccdd" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "1c1c77e1-10e4-40f9-9f0c-c88b0b226c49" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "55463995-a327-431e-9c9f-cadb7a1abf3d" -->
## Quick Reference

<!-- section_id: "f1f63fc0-7f32-4c16-9141-93fdd3821a40" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "49cda3f8-05c5-4ec9-ada4-11ff3c9b69ce" -->
### Log Location in Layer/Stage Structure

```
<layer_N>/<N.99_stages>/<stage_M>/ai_agent_system/logs/
  ├── manager.log          # Manager decisions and handoff creation
  ├── workers/
  │   ├── codex.log       # Worker execution logs
  │   ├── gemini.log      # Worker execution logs
  │   └── claude.log      # Worker execution logs
  ├── handoffs/
  │   ├── incoming.log    # Received handoffs
  │   └── outgoing.log    # Created handoffs
  └── metrics.jsonl       # Structured metrics
```

<!-- section_id: "f0ab4319-ec74-43fd-9380-0d51d8558fc8" -->
### Structured Logging Format

All log entries MUST include:

```json
{
  "timestamp": "2025-12-24T10:30:45.123Z",
  "level": "INFO",
  "logger": "supervisor.task_executor",
  "message": "Task completed successfully",
  "context": {
    "task_id": "task-L2-auth-impl-20251224-103045",
    "layer": 2,
    "stage": "implementation",
    "tool": "codex",
    "model": "codestral",
    "handoff_id": "handoff-20251224-102030"
  },
  "metadata": {
    "duration_ms": 12450,
    "tokens_used": 2340,
    "cost_usd": 0.0234,
    "files_modified": 3,
    "retry_count": 0
  },
  "trace_id": "trace-L1-auth-system",
  "span_id": "span-impl-login-component"
}
```

---

<!-- section_id: "591f9d20-342a-4436-8132-f5d9aa2a4619" -->
## Layer-Specific Logging Requirements

<!-- section_id: "844a7da6-0ce4-41d0-940b-dcb2b882f560" -->
### Layer 0 (Universal) - L0 Manager

**Responsibilities**:
- Log all user requests and initial handoff creation
- Track cross-layer handoff propagation
- Monitor system-wide budget and resource usage
- Audit all L0 → L1 delegations

**Key Events**:
```json
{
  "event": "request.received",
  "layer": 0,
  "stage": "request_gathering",
  "request_summary": "Implement authentication system",
  "estimated_complexity": "high",
  "initial_budget": 10.00
}
```

<!-- section_id: "497467bf-f851-4be6-9a82-61be627a6ddb" -->
### Layer 1 (Project) - L1 Manager

**Responsibilities**:
- Log project-level planning decisions
- Track L1 → L2 feature delegation
- Monitor project budget allocation
- Audit tool selection for features

**Key Events**:
```json
{
  "event": "feature.delegated",
  "layer": 1,
  "stage": "planning",
  "feature": "login-component",
  "delegated_to_layer": 2,
  "allocated_budget": 2.50,
  "selected_tool": "codex"
}
```

<!-- section_id: "55e99982-0aa1-446e-8f0f-74a05c52889e" -->
### Layer 2 (Features) - L2 Manager

**Responsibilities**:
- Log feature implementation decisions
- Track L2 → L3 component delegation
- Monitor feature-level quality metrics
- Audit component integration

**Key Events**:
```json
{
  "event": "component.created",
  "layer": 2,
  "stage": "implementation",
  "component": "LoginForm",
  "files_created": ["LoginForm.tsx", "LoginForm.test.tsx"],
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85
  }
}
```

<!-- section_id: "fbf8ec8b-1da9-4c4b-a7ad-c75fa8ffd0af" -->
### Layer 3 (Components) - L3 Workers

**Responsibilities**:
- Log all file operations (create, modify, delete)
- Track code quality metrics
- Monitor test execution and results
- Audit all tool usage

**Key Events**:
```json
{
  "event": "file.written",
  "layer": 3,
  "stage": "implementation",
  "file_path": "src/components/LoginForm.tsx",
  "lines_added": 120,
  "tool": "write_file",
  "verified": true
}
```

---

<!-- section_id: "362b9a62-c9d6-440e-88ab-badb6f53420e" -->
## Handoff Logging

<!-- section_id: "4e4b98ea-43bb-4b02-8ef4-e6690e99f3c8" -->
### Incoming Handoff

When a manager/worker receives a handoff:

```json
{
  "event": "handoff.received",
  "handoff_id": "handoff-20251224-102030",
  "layer": 2,
  "stage": "implementation",
  "from": {
    "layer": 1,
    "stage": "planning"
  },
  "task": "Implement login form component",
  "constraints": ["TypeScript", "React", "Accessibility"],
  "artifacts": ["design-spec.md", "wireframes.png"]
}
```

<!-- section_id: "6402bcf1-39b0-44f8-a236-a404da9942c6" -->
### Outgoing Handoff

When a manager/worker creates a handoff:

```json
{
  "event": "handoff.created",
  "handoff_id": "handoff-20251224-103045",
  "layer": 2,
  "stage": "implementation",
  "to": {
    "layer": 1,
    "stage": "review"
  },
  "status": "completed",
  "results": {
    "files_created": 3,
    "tests_passed": true,
    "quality_score": 0.92
  },
  "artifacts": ["LoginForm.tsx", "test-results.json"]
}
```

---

<!-- section_id: "d69213a8-8195-41d6-abe3-344efdfa1b73" -->
## Manager/Worker Pattern Observability

<!-- section_id: "c50f1e9a-4073-474d-ad5a-4cc16de0f756" -->
### Manager Spawning Workers

```json
{
  "event": "worker.spawned",
  "manager": {
    "layer": 2,
    "stage": "implementation"
  },
  "worker": {
    "worker_id": "worker-codex-20251224-103045",
    "tool": "codex",
    "model": "codestral",
    "task_id": "task-L3-login-impl",
    "estimated_cost": 0.50
  },
  "parallel_count": 3,
  "parallel_group": "login-components"
}
```

<!-- section_id: "778d4cdf-5d2e-423d-b274-59b3d93ede8a" -->
### Worker Reporting Results

```json
{
  "event": "worker.completed",
  "worker_id": "worker-codex-20251224-103045",
  "task_id": "task-L3-login-impl",
  "status": "success",
  "duration_ms": 8500,
  "tokens": {"input": 1200, "output": 850, "total": 2050},
  "cost_usd": 0.0205,
  "artifacts": {
    "files_created": ["LoginForm.tsx"],
    "files_modified": ["index.ts"]
  }
}
```

---

<!-- section_id: "4a373079-835f-43aa-b1ae-f77c82d294ef" -->
## Metrics Collection

<!-- section_id: "d9d799e4-c9d0-4f0f-b3f7-3b15c04808ae" -->
### Cost Tracking

Track costs at every layer/stage boundary:

```json
{
  "metric": "cost",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 2,
  "stage": "implementation",
  "tool": "codex",
  "model": "codestral",
  "cost_usd": 0.0205,
  "budget_remaining": {
    "daily": 45.50,
    "task_limit": 1.95
  }
}
```

<!-- section_id: "a44fa48a-24c6-4c4a-9276-e1ddff724d8c" -->
### Quality Metrics

Track code quality per component:

```json
{
  "metric": "quality",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 3,
  "component": "LoginForm",
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85,
    "complexity_score": 12,
    "type_errors": 0
  }
}
```

<!-- section_id: "5cafd834-1d4a-40ae-acb7-5ea74214da23" -->
### Performance Metrics

Track task execution performance:

```json
{
  "metric": "performance",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 2,
  "stage": "implementation",
  "task_duration_ms": 8500,
  "parallel_workers": 3,
  "total_cost_usd": 0.62
}
```

---

<!-- section_id: "3ed24d21-5bea-43f8-8224-a23691af688d" -->
## Distributed Tracing

<!-- section_id: "e44b8bdf-01e4-475a-b95e-9ef0badd0559" -->
### Trace Hierarchy

Traces show the full workflow from L0 to L3+:

```
trace-L1-auth-system (5m 32s, $4.50)
├─ span-L1-request (45s, $0.50) [gemini-pro-2]
├─ span-L1-instructions (1m 20s, $0.80) [gemini-pro-2]
├─ span-L1-planning (2m 10s, $1.20) [claude-sonnet-4.5]
└─ span-L2-implementation (1m 17s, $2.00)
   ├─ span-L3-login-impl (25s, $0.20) [codestral]
   ├─ span-L3-reset-impl (30s, $0.25) [codestral]
   └─ span-L3-testing (22s, $0.15) [starcoder2]
```

<!-- section_id: "7cf92257-0a96-4ff5-8cec-742106a28d03" -->
### Trace Propagation

Every handoff carries trace context:

```json
{
  "handoff_id": "handoff-20251224-102030",
  "trace_context": {
    "trace_id": "trace-L1-auth-system",
    "parent_span_id": "span-L1-planning",
    "span_id": "span-L2-implementation"
  }
}
```

---

<!-- section_id: "3334216b-643e-4643-b230-107582fb823f" -->
## Log Storage Strategy

<!-- section_id: "ecc4a65d-91da-4741-a5ec-801d295fded2" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "665f7ef3-b864-44a3-803b-bfbcddb7094b" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "8395e8fb-0b07-428e-903c-a58eae46c367" -->
## Audit Trail Requirements

All manager decisions and worker actions MUST be logged with:

1. **Timestamp**: ISO 8601 format with millisecond precision
2. **Agent Identity**: Layer, stage, tool, model
3. **Action Type**: read/write/execute/delegate/escalate
4. **Resource**: File path, API endpoint, handoff ID
5. **Outcome**: success/failure with error details
6. **Cost**: Estimated and actual cost in USD
7. **Approver**: If human approval was required

---

<!-- section_id: "b72de49b-5547-428e-8ff8-2eef9dba6b0a" -->
## Examples

<!-- section_id: "181a32fb-bba2-4c67-9fdc-91d5d1525fd2" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "8467a198-5fed-45c4-b5bb-6548ffb52652" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "fef88d9c-e0b9-40eb-a7a2-1031561d70a7" -->
## Integration Points

<!-- section_id: "1ec39e60-97e0-4ca2-8afc-2f3c1a8d521f" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "be6223cc-668f-49e4-a490-4663bcea26d0" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "0114304b-fcf8-443a-802e-745ae0f4f0e3" -->
## Tools and Libraries

<!-- section_id: "a2413ded-f334-449f-9ca2-99a35c40d98f" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "c3945007-0868-474e-b710-4a2ec637b79f" -->
### Example Configuration

```python
import logging
import json
from datetime import datetime

class StructuredLogger:
    """Structured logger for AI Manager Hierarchy."""

    def __init__(self, layer, stage, tool=None):
        self.layer = layer
        self.stage = stage
        self.tool = tool
        self.logger = logging.getLogger(f"L{layer}.{stage}")

    def log_event(self, event_type, **kwargs):
        """Log a structured event."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": "INFO",
            "event": event_type,
            "context": {
                "layer": self.layer,
                "stage": self.stage,
                "tool": self.tool
            },
            **kwargs
        }
        self.logger.info(json.dumps(entry))

# Usage
logger = StructuredLogger(layer=2, stage="implementation", tool="codex")
logger.log_event("task.started", task_id="task-L2-auth-impl", estimated_cost=0.50)
```

---

<!-- section_id: "d8e5d5ca-ebea-464b-939a-8338ad6c5069" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "0d99f0fa-d834-4819-a872-ba94bb787133" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active


---

<!-- section_id: "453f9107-3481-4cc2-a97c-68952f5668ad" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "b72e1b5d-d6cc-4be1-b12a-42b04910fb00" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "5c719b23-c0a3-49b1-9fb8-b79fa78c78f6" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "423e7a4d-d3b7-49c8-a25b-e9dcb1460458" -->
## Quick Reference

<!-- section_id: "cffa54d7-2c22-4b18-8b60-c2660af30f53" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "a0a3ccd2-290a-44f1-bf7c-5ab67561f6e8" -->
### Log Location in Layer/Stage Structure

```
<layer_N>/<N.99_stages>/<stage_M>/ai_agent_system/logs/
  ├── manager.log          # Manager decisions and handoff creation
  ├── workers/
  │   ├── codex.log       # Worker execution logs
  │   ├── gemini.log      # Worker execution logs
  │   └── claude.log      # Worker execution logs
  ├── handoffs/
  │   ├── incoming.log    # Received handoffs
  │   └── outgoing.log    # Created handoffs
  └── metrics.jsonl       # Structured metrics
```

<!-- section_id: "18c5cd72-70c8-4145-b198-e187f6868983" -->
### Structured Logging Format

All log entries MUST include:

```json
{
  "timestamp": "2025-12-24T10:30:45.123Z",
  "level": "INFO",
  "logger": "supervisor.task_executor",
  "message": "Task completed successfully",
  "context": {
    "task_id": "task-L2-auth-impl-20251224-103045",
    "layer": 2,
    "stage": "implementation",
    "tool": "codex",
    "model": "codestral",
    "handoff_id": "handoff-20251224-102030"
  },
  "metadata": {
    "duration_ms": 12450,
    "tokens_used": 2340,
    "cost_usd": 0.0234,
    "files_modified": 3,
    "retry_count": 0
  },
  "trace_id": "trace-L1-auth-system",
  "span_id": "span-impl-login-component"
}
```

---

<!-- section_id: "780c90b1-779b-4424-b531-beb60f90ea01" -->
## Layer-Specific Logging Requirements

<!-- section_id: "74602f12-5120-462e-9e86-d9843375b1f1" -->
### Layer 0 (Universal) - L0 Manager

**Responsibilities**:
- Log all user requests and initial handoff creation
- Track cross-layer handoff propagation
- Monitor system-wide budget and resource usage
- Audit all L0 → L1 delegations

**Key Events**:
```json
{
  "event": "request.received",
  "layer": 0,
  "stage": "request_gathering",
  "request_summary": "Implement authentication system",
  "estimated_complexity": "high",
  "initial_budget": 10.00
}
```

<!-- section_id: "1470c80f-acd6-4f7e-9b36-f8ff3b28ea31" -->
### Layer 1 (Project) - L1 Manager

**Responsibilities**:
- Log project-level planning decisions
- Track L1 → L2 feature delegation
- Monitor project budget allocation
- Audit tool selection for features

**Key Events**:
```json
{
  "event": "feature.delegated",
  "layer": 1,
  "stage": "planning",
  "feature": "login-component",
  "delegated_to_layer": 2,
  "allocated_budget": 2.50,
  "selected_tool": "codex"
}
```

<!-- section_id: "ba6f4abb-3a57-4837-9bb6-8f830283102e" -->
### Layer 2 (Features) - L2 Manager

**Responsibilities**:
- Log feature implementation decisions
- Track L2 → L3 component delegation
- Monitor feature-level quality metrics
- Audit component integration

**Key Events**:
```json
{
  "event": "component.created",
  "layer": 2,
  "stage": "implementation",
  "component": "LoginForm",
  "files_created": ["LoginForm.tsx", "LoginForm.test.tsx"],
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85
  }
}
```

<!-- section_id: "062bc597-04a6-4854-9aa8-6cb226bd00a5" -->
### Layer 3 (Components) - L3 Workers

**Responsibilities**:
- Log all file operations (create, modify, delete)
- Track code quality metrics
- Monitor test execution and results
- Audit all tool usage

**Key Events**:
```json
{
  "event": "file.written",
  "layer": 3,
  "stage": "implementation",
  "file_path": "src/components/LoginForm.tsx",
  "lines_added": 120,
  "tool": "write_file",
  "verified": true
}
```

---

<!-- section_id: "c7537bd8-906a-4623-b79a-5f7b74af4bbd" -->
## Handoff Logging

<!-- section_id: "51c0a204-cd33-448e-bed6-af1b717b9601" -->
### Incoming Handoff

When a manager/worker receives a handoff:

```json
{
  "event": "handoff.received",
  "handoff_id": "handoff-20251224-102030",
  "layer": 2,
  "stage": "implementation",
  "from": {
    "layer": 1,
    "stage": "planning"
  },
  "task": "Implement login form component",
  "constraints": ["TypeScript", "React", "Accessibility"],
  "artifacts": ["design-spec.md", "wireframes.png"]
}
```

<!-- section_id: "2df087b6-f3ea-461e-9272-065784e755f2" -->
### Outgoing Handoff

When a manager/worker creates a handoff:

```json
{
  "event": "handoff.created",
  "handoff_id": "handoff-20251224-103045",
  "layer": 2,
  "stage": "implementation",
  "to": {
    "layer": 1,
    "stage": "review"
  },
  "status": "completed",
  "results": {
    "files_created": 3,
    "tests_passed": true,
    "quality_score": 0.92
  },
  "artifacts": ["LoginForm.tsx", "test-results.json"]
}
```

---

<!-- section_id: "9b6b14d4-e344-4b85-9e66-ed81295fa2b3" -->
## Manager/Worker Pattern Observability

<!-- section_id: "119a78f0-7a2e-441a-af42-9285ea924064" -->
### Manager Spawning Workers

```json
{
  "event": "worker.spawned",
  "manager": {
    "layer": 2,
    "stage": "implementation"
  },
  "worker": {
    "worker_id": "worker-codex-20251224-103045",
    "tool": "codex",
    "model": "codestral",
    "task_id": "task-L3-login-impl",
    "estimated_cost": 0.50
  },
  "parallel_count": 3,
  "parallel_group": "login-components"
}
```

<!-- section_id: "965cf0e6-f197-431a-bf0c-f56da9e20a9a" -->
### Worker Reporting Results

```json
{
  "event": "worker.completed",
  "worker_id": "worker-codex-20251224-103045",
  "task_id": "task-L3-login-impl",
  "status": "success",
  "duration_ms": 8500,
  "tokens": {"input": 1200, "output": 850, "total": 2050},
  "cost_usd": 0.0205,
  "artifacts": {
    "files_created": ["LoginForm.tsx"],
    "files_modified": ["index.ts"]
  }
}
```

---

<!-- section_id: "c8bffec0-f0b6-40c1-b9e5-b8fc4429f137" -->
## Metrics Collection

<!-- section_id: "17742c8b-fc71-483b-96d6-d716ced5bea8" -->
### Cost Tracking

Track costs at every layer/stage boundary:

```json
{
  "metric": "cost",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 2,
  "stage": "implementation",
  "tool": "codex",
  "model": "codestral",
  "cost_usd": 0.0205,
  "budget_remaining": {
    "daily": 45.50,
    "task_limit": 1.95
  }
}
```

<!-- section_id: "5b44d90f-22fb-4e82-b257-41946d2c0493" -->
### Quality Metrics

Track code quality per component:

```json
{
  "metric": "quality",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 3,
  "component": "LoginForm",
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85,
    "complexity_score": 12,
    "type_errors": 0
  }
}
```

<!-- section_id: "e7ffe806-09ea-4098-a244-657fddbf736b" -->
### Performance Metrics

Track task execution performance:

```json
{
  "metric": "performance",
  "timestamp": "2025-12-24T10:30:45.123Z",
  "layer": 2,
  "stage": "implementation",
  "task_duration_ms": 8500,
  "parallel_workers": 3,
  "total_cost_usd": 0.62
}
```

---

<!-- section_id: "a6b30200-4476-444a-bce9-cbe157baecb8" -->
## Distributed Tracing

<!-- section_id: "f26fcd27-89b9-45d1-af55-6145f352a0d7" -->
### Trace Hierarchy

Traces show the full workflow from L0 to L3+:

```
trace-L1-auth-system (5m 32s, $4.50)
├─ span-L1-request (45s, $0.50) [gemini-pro-2]
├─ span-L1-instructions (1m 20s, $0.80) [gemini-pro-2]
├─ span-L1-planning (2m 10s, $1.20) [claude-sonnet-4.5]
└─ span-L2-implementation (1m 17s, $2.00)
   ├─ span-L3-login-impl (25s, $0.20) [codestral]
   ├─ span-L3-reset-impl (30s, $0.25) [codestral]
   └─ span-L3-testing (22s, $0.15) [starcoder2]
```

<!-- section_id: "3210e1a1-7e13-4d9b-9d9c-d760c8655a17" -->
### Trace Propagation

Every handoff carries trace context:

```json
{
  "handoff_id": "handoff-20251224-102030",
  "trace_context": {
    "trace_id": "trace-L1-auth-system",
    "parent_span_id": "span-L1-planning",
    "span_id": "span-L2-implementation"
  }
}
```

---

<!-- section_id: "615bd6da-c4b3-4dd2-906f-cff5cbb84d98" -->
## Log Storage Strategy

<!-- section_id: "d76e330d-1d79-460d-899b-21a883268256" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "5aec3d84-8d52-4d2b-a624-1415f32af22d" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "b43dd718-2425-46ec-a4da-76ad8017d9c0" -->
## Audit Trail Requirements

All manager decisions and worker actions MUST be logged with:

1. **Timestamp**: ISO 8601 format with millisecond precision
2. **Agent Identity**: Layer, stage, tool, model
3. **Action Type**: read/write/execute/delegate/escalate
4. **Resource**: File path, API endpoint, handoff ID
5. **Outcome**: success/failure with error details
6. **Cost**: Estimated and actual cost in USD
7. **Approver**: If human approval was required

---

<!-- section_id: "5cbab71c-059d-4f1c-b0d8-66b6d2263a43" -->
## Examples

<!-- section_id: "88be66ba-7451-4917-b84c-a34847afd144" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "348624bc-5950-43d7-8cf5-b4d426b65e96" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "3e64022a-1fee-4741-89bb-ae851804ffaa" -->
## Integration Points

<!-- section_id: "5b863fd0-1f49-4fef-a03d-6307d24470cf" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "6ca451bb-9e42-42cb-b2fa-dce9a92a680c" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "c92a96e5-ccd6-4164-ae29-b26951059fd8" -->
## Tools and Libraries

<!-- section_id: "12383d81-cd65-4b42-b056-dc7136302e37" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "498c9525-d245-4623-b333-1e7be9ae5a2d" -->
### Example Configuration

```python
import logging
import json
from datetime import datetime

class StructuredLogger:
    """Structured logger for AI Manager Hierarchy."""

    def __init__(self, layer, stage, tool=None):
        self.layer = layer
        self.stage = stage
        self.tool = tool
        self.logger = logging.getLogger(f"L{layer}.{stage}")

    def log_event(self, event_type, **kwargs):
        """Log a structured event."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": "INFO",
            "event": event_type,
            "context": {
                "layer": self.layer,
                "stage": self.stage,
                "tool": self.tool
            },
            **kwargs
        }
        self.logger.info(json.dumps(entry))

# Usage
logger = StructuredLogger(layer=2, stage="implementation", tool="codex")
logger.log_event("task.started", task_id="task-L2-auth-impl", estimated_cost=0.50)
```

---

<!-- section_id: "c1129c63-7f38-4154-b857-4d0ddd0c7a71" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "c4face91-e021-45bc-bcd4-92f2799484c6" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active
