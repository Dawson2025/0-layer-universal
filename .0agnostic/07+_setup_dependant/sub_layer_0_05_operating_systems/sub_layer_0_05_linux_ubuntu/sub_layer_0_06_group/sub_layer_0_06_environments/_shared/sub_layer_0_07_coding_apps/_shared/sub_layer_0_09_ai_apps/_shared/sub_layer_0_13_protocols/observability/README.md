---
resource_id: "ad8afecb-ebb7-4b27-973d-21070b59cfd7"
resource_type: "readme_document"
resource_name: "README"
---
# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "40671a50-bd7d-49b5-bced-9bd8e8341fea" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "460647ee-34cd-4298-b3e2-a30dd20ee53d" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "7951c140-d49f-4025-bfc9-92456af9bc97" -->
## Quick Reference

<!-- section_id: "cd8f1a4b-3750-4f94-bd73-d6b04130b2ba" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "b25d3e5c-6427-4a6f-b197-7b841e5aab35" -->
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

<!-- section_id: "c4248870-e8e1-4034-9bae-3695f19a6487" -->
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

<!-- section_id: "1c56e953-30a7-4c45-8e28-9331f898b81a" -->
## Layer-Specific Logging Requirements

<!-- section_id: "a95f95c1-82f8-4210-b074-41b69a1e3f00" -->
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

<!-- section_id: "550c3001-8e60-41fb-b587-99678e023ca0" -->
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

<!-- section_id: "60250bcb-5fc0-4f18-8adf-21aea4936e79" -->
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

<!-- section_id: "15ede768-8d2c-4fa6-8d9a-09404db63381" -->
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

<!-- section_id: "0a0e762e-5b27-4c3e-936d-8e9188d39129" -->
## Handoff Logging

<!-- section_id: "373a7b54-1a56-4bc3-9712-9420aa6044d1" -->
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

<!-- section_id: "abad7f1b-9563-4dcf-ab9d-c38d1fad566a" -->
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

<!-- section_id: "df2782fa-b27c-4401-88f6-1167025f0ccf" -->
## Manager/Worker Pattern Observability

<!-- section_id: "6d47e038-a022-452c-8594-568536d56b13" -->
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

<!-- section_id: "ba60a67c-ceff-43e7-bd3c-8b8f4bcb0564" -->
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

<!-- section_id: "dc379269-3874-407f-8d96-487536c22807" -->
## Metrics Collection

<!-- section_id: "54fa682c-0040-44c0-9c96-783ee01ae655" -->
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

<!-- section_id: "dc9eb0ae-0955-4fb2-9430-b000473bfc30" -->
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

<!-- section_id: "cd899f3e-a3ec-4af5-b8d9-27c647fa35d9" -->
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

<!-- section_id: "0d4ca56e-61f8-48d3-830c-b70ceb6a3e8b" -->
## Distributed Tracing

<!-- section_id: "1a5b8717-b100-4fac-81e8-51aa71fcdb0d" -->
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

<!-- section_id: "4edf6901-441a-4e38-ba1b-5b986d7e204f" -->
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

<!-- section_id: "7784a8eb-a9a6-4468-a08a-912529a8f43f" -->
## Log Storage Strategy

<!-- section_id: "cf3dccb4-a943-404e-99cf-675c2f708098" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "d8df57e0-7efa-405e-bfe5-93ca3a61f24a" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "12f426ae-98ff-48ea-aca8-c6d6215ecb41" -->
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

<!-- section_id: "45b42772-695d-418c-97e9-162d3448f1d7" -->
## Examples

<!-- section_id: "f097995a-f708-4a43-aac7-4c7b8c037bdc" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "c9c0463e-2978-4345-9360-b75c1d4de237" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "45e07417-4b56-416a-ac9d-f0c88d32d614" -->
## Integration Points

<!-- section_id: "51d5ca40-858d-43a4-b789-abb432fc82c5" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "9e04299a-413d-4d50-bf94-8ddaa6275672" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "4af43e11-d987-400f-af52-4a6fb328b0b1" -->
## Tools and Libraries

<!-- section_id: "533a4226-f783-4f12-8bff-5fe2a4d8bda3" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "12a51d04-9d8b-49f9-ac6a-fd8cc9bb178e" -->
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

<!-- section_id: "098dc312-48c9-43ba-98d2-c64a6b786d69" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "cd78c6d6-8b03-4c4f-9835-0de421dd34fd" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active

---

<!-- section_id: "15c729b1-ca65-449b-91e8-be350fb734e4" -->
## Legacy Universal Protocols Source

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "cbb1f188-807e-4ab8-9725-27975e7092c3" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "698d6e46-3c8c-4557-82fa-523b9576031e" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "0447302c-a8ba-490b-a557-149afc217f41" -->
## Quick Reference

<!-- section_id: "b3c4ea18-3023-4981-aa6c-59f94dbd4718" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "f854d3e6-3363-43c6-957a-bdb1a7645abc" -->
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

<!-- section_id: "c42902fe-8c89-4ba2-bc1a-83f03a96690a" -->
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

<!-- section_id: "585323ec-8601-4abe-9f58-84cf1df53b1a" -->
## Layer-Specific Logging Requirements

<!-- section_id: "bef2fc6e-fbd2-4f66-8fed-aa96bcd5025c" -->
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

<!-- section_id: "e7de82b1-685f-4d6a-a54d-471fef430209" -->
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

<!-- section_id: "b685b1a8-989f-4efc-8ba5-eb12d938274a" -->
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

<!-- section_id: "b61e494f-6eeb-4d76-8870-e29d38723b8c" -->
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

<!-- section_id: "6a2155d0-2e34-4e4c-86e8-681049208113" -->
## Handoff Logging

<!-- section_id: "ec416e3c-b8f7-4c65-ae36-f1b218ec4085" -->
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

<!-- section_id: "86cc01e5-3edc-4c11-96c8-c96abed40a51" -->
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

<!-- section_id: "74e6f63d-b776-4820-9ee8-656b6dc4f4bf" -->
## Manager/Worker Pattern Observability

<!-- section_id: "934cd29c-6c15-4b54-94b3-39b1b3dd3d95" -->
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

<!-- section_id: "ee57dc10-a745-4844-a2d3-4da73d941fd2" -->
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

<!-- section_id: "0f30f4b9-0123-41b8-a54c-f2fcd195c9dd" -->
## Metrics Collection

<!-- section_id: "04b1699e-f915-44e7-aeb0-84e0f6a48127" -->
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

<!-- section_id: "6ba8018e-7cfc-4228-b2ec-f71aefb782f5" -->
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

<!-- section_id: "40e1fc35-ae7c-4f30-86bb-f72d6c9f8fd8" -->
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

<!-- section_id: "f73345f2-f141-4ba5-b4da-303d7515baee" -->
## Distributed Tracing

<!-- section_id: "b4c64f9b-bab6-427d-8990-093570bc8edd" -->
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

<!-- section_id: "eabfc545-3944-4855-b49f-59b205a4f7a7" -->
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

<!-- section_id: "89efd04a-5097-4b24-b9fe-70fd031ab714" -->
## Log Storage Strategy

<!-- section_id: "b224baef-cfad-43e2-9d7e-a93784264c29" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "71eaee00-7ba5-4585-adaf-da6c7d9d5f8f" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "90d10a85-f761-4f94-8967-8f3a8697aba5" -->
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

<!-- section_id: "110d2697-ab93-4f50-962d-714443c8f861" -->
## Examples

<!-- section_id: "221ad1a3-b701-4c75-9e3c-d0f961ec7ba0" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "fb385e5a-c795-4dfb-a8c0-9f6dba72b39b" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "6ddc2ead-3747-40c8-a4b6-a81b24ad1685" -->
## Integration Points

<!-- section_id: "8c5e0fd6-25ad-45e1-a597-13e7f81fafb8" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "bb9f5b89-7a3f-49ea-b680-ec2f07862501" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "74659158-22f7-4797-8f31-76b186c2d752" -->
## Tools and Libraries

<!-- section_id: "6340ac3d-823a-458b-b248-11a0d864655a" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "de0553f6-4f82-4888-afe9-55b6a1000d19" -->
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

<!-- section_id: "a86b437a-0bd3-43b6-a21c-40656743ab7e" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "f5d86e93-2c72-4f4c-bf5a-d53d69bf5762" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active


---

<!-- section_id: "9a5cfb76-c251-4db2-95a5-c5ccffdb828b" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "8321af15-61c5-4955-a2ff-83fc11e56b45" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "980c5a1a-a5a7-40f3-bd70-d2dc9c08d981" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "92f59a75-c579-46a7-a01f-b11d3359df25" -->
## Quick Reference

<!-- section_id: "02cd8b75-3533-442e-887c-69988f3fa8b8" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "ba4928b9-5f69-4b47-8fc6-5486ba69f483" -->
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

<!-- section_id: "6a35d60c-834f-4ebd-af75-fe28ab18a32e" -->
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

<!-- section_id: "c5b58dc0-4733-442b-a634-cab94c5642c2" -->
## Layer-Specific Logging Requirements

<!-- section_id: "854827bc-a9f7-4474-91ac-9bd8763c79cd" -->
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

<!-- section_id: "9c99af2c-5d27-4e8e-a7cc-16470ff30975" -->
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

<!-- section_id: "c50bec3f-5de9-4757-84cc-dc450bdb5728" -->
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

<!-- section_id: "b6010dfb-0964-48af-b584-f81d4a02d317" -->
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

<!-- section_id: "27eca1e8-1bdd-4de6-ae97-2d711b158787" -->
## Handoff Logging

<!-- section_id: "d0617577-0d90-4579-9938-1b9ced5f0520" -->
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

<!-- section_id: "855329d9-8040-47a9-9452-86beae0e7937" -->
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

<!-- section_id: "2ce61fa5-d76d-4155-af1e-d9f72fc55707" -->
## Manager/Worker Pattern Observability

<!-- section_id: "579dbe4f-c89f-4ecd-800b-6ef8df108483" -->
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

<!-- section_id: "640f5afb-d84b-4bad-87a2-f9e15bd19400" -->
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

<!-- section_id: "d29c380d-c85d-4526-b2d0-c83407daed63" -->
## Metrics Collection

<!-- section_id: "e12eedc4-344b-4fb6-b4f8-73384c8b4aac" -->
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

<!-- section_id: "53f6ecbd-128d-4a27-8b62-b9c51ea64418" -->
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

<!-- section_id: "ea02624e-fcea-4722-834a-ff4c2b6d9f1a" -->
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

<!-- section_id: "6d8bf7f8-aa84-4720-9a22-ff0c04f4b092" -->
## Distributed Tracing

<!-- section_id: "340a9e0a-d5b6-4ac6-a6a8-5cf3a00c71b0" -->
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

<!-- section_id: "29826583-7fa1-4836-a408-c195e07d4297" -->
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

<!-- section_id: "fc4edeb5-ed38-4fd4-a411-f8e1c433ae78" -->
## Log Storage Strategy

<!-- section_id: "dea83ab1-5a65-460f-8e1a-a45f7c8a1a19" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "b39928e3-485f-43a4-a8ff-4ef72ecb0327" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "6000217c-256e-413b-bfdd-2a7bd47fc2af" -->
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

<!-- section_id: "2e449923-18e1-4451-9fa8-58c2652d6d45" -->
## Examples

<!-- section_id: "fabcd9c3-449d-47db-8d14-9fd55f1ab639" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "f9f47549-a72a-4e6f-9e69-e0f181877b4e" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "5ba93a95-0a4d-4848-9f26-96b449940d56" -->
## Integration Points

<!-- section_id: "b6912d1c-2938-4f35-879a-7e6d252d1d20" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "cb59c94b-431b-49cd-b942-c7df9e35c517" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "ba002723-2fd0-4395-ba58-984d3036eb9e" -->
## Tools and Libraries

<!-- section_id: "af67cbcb-126c-4fc5-bc9d-26c8cc6cdad0" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "22ad3e01-3937-4436-910d-d6ea236877c3" -->
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

<!-- section_id: "2ceecc17-1b9f-45f7-8123-c24385b3ac9f" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "fb90b368-b8d7-4dc2-96f2-0a8e6e881fb2" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active
