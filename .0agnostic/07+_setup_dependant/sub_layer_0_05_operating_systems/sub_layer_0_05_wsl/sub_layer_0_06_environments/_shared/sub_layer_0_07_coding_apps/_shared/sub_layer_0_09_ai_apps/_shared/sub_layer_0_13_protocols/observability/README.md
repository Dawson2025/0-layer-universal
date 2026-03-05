---
resource_id: "3dc79a05-a949-4397-8104-0981f889c09b"
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

<!-- section_id: "b6f99141-ef65-4087-83a6-acaef311fdb7" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "9de75751-e030-4915-8e42-b81830a6a1c8" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "83469d70-d323-4834-8486-b13fdce39a4a" -->
## Quick Reference

<!-- section_id: "9ebe0145-3f98-40e2-8ce5-c2d525f40b6e" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "5d3a7fbd-0422-41bb-b8b5-f26c81282123" -->
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

<!-- section_id: "8ac2face-5fc1-4903-aaf3-202410c0fa38" -->
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

<!-- section_id: "b5f9bffd-db26-4072-93a6-23ed51dc050e" -->
## Layer-Specific Logging Requirements

<!-- section_id: "e3f6addb-1056-4c21-a661-426d5bafd1ca" -->
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

<!-- section_id: "b220dd7f-3933-4495-9fae-4a35768338b6" -->
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

<!-- section_id: "a00195f2-1ad3-407a-8a2b-27061738023a" -->
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

<!-- section_id: "7d232129-131e-482a-b509-d3e791da3c30" -->
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

<!-- section_id: "1fed578a-aad7-4fcf-98a3-246423dae665" -->
## Handoff Logging

<!-- section_id: "1c9f6fc2-dc5f-4af4-9e5e-97e786b70c50" -->
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

<!-- section_id: "476ffc7a-ac2a-4e6f-b5a4-af209b4630a8" -->
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

<!-- section_id: "7bc6d814-0eb5-4acf-9753-9b45b13e5e71" -->
## Manager/Worker Pattern Observability

<!-- section_id: "46803797-0207-45ae-83c6-fb6d241dbaab" -->
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

<!-- section_id: "a0ae016d-62e8-4df4-824e-bb2719d746f2" -->
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

<!-- section_id: "ffbc2b4e-1666-4409-882f-82d9947f0818" -->
## Metrics Collection

<!-- section_id: "a4788220-bf28-42ea-ba3d-ba388ec8a6a8" -->
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

<!-- section_id: "6495fad2-aa79-481a-82ee-ebeca826b737" -->
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

<!-- section_id: "1b4798d7-4e01-4952-b3c9-5581d30feb3d" -->
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

<!-- section_id: "9df381d9-3cd1-4564-9b5e-c76cc544803b" -->
## Distributed Tracing

<!-- section_id: "1b138361-93d8-4cf4-b25d-8bf7d83a995d" -->
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

<!-- section_id: "abf62699-187c-4082-9df3-c7dbe9e3c383" -->
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

<!-- section_id: "a00d7698-9fb0-4966-b2e1-92ee9bf7dba5" -->
## Log Storage Strategy

<!-- section_id: "53105756-6212-467f-8157-b22040bcbc68" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "dac24cae-f47b-4973-bca3-4145c6dd5e8e" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "2feadd8f-8a54-426e-92a8-530767f8fada" -->
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

<!-- section_id: "859637ca-679b-4d5b-b3fa-a276880bedac" -->
## Examples

<!-- section_id: "dc15974f-e8ac-4e41-a620-a359210c8d0d" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "2d68e456-c02d-4595-a607-36525f2dedb4" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "4f30d4a7-eab4-4098-8f40-dfa084546fa8" -->
## Integration Points

<!-- section_id: "0b8e1e9d-6d13-4b19-b8a0-00f9fba4ce62" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "473c1e72-9a3b-404a-859e-c2d004910cc8" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "9d415ef4-1b87-4430-aca2-236cd7dd9b62" -->
## Tools and Libraries

<!-- section_id: "0b9ab95c-3bb4-481d-8f95-5336cb8ca8b3" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "e68b8721-773d-44c3-99ac-d7baf4f34ec9" -->
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

<!-- section_id: "a03dd32b-1457-4949-a4d7-cee436ef8b8b" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "78a00355-466a-4776-ae69-17ec60c53975" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active

---

<!-- section_id: "6b9fc836-62bd-44ec-92e5-d5df4d0033aa" -->
## Legacy Universal Protocols Source

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "2f6d0a5a-2af0-4ce7-afae-58676b2dd83a" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "e9813f86-ab48-4f38-8b13-89d881f99148" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "4942a76f-dd37-4e35-a8ab-1b0550a6864d" -->
## Quick Reference

<!-- section_id: "3af60384-bfa4-4159-a88d-7ba9446ab8b8" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "f4b8eb82-8d14-48be-9d59-25ea19b03139" -->
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

<!-- section_id: "baa77e54-a746-4790-b592-da0e5e121c79" -->
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

<!-- section_id: "f20942cc-5b02-473a-9899-3a85a7382573" -->
## Layer-Specific Logging Requirements

<!-- section_id: "d838b2e6-a669-4382-8fde-3c5b63b078bd" -->
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

<!-- section_id: "afe2cd9d-bc87-4636-a55e-db97c5f2e0f4" -->
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

<!-- section_id: "8ae43959-ab8e-4b43-a811-8b86e5c86160" -->
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

<!-- section_id: "0f72f77c-c829-4f5f-92d5-27cc14c9b5d6" -->
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

<!-- section_id: "fbffc3a4-52fb-49c2-ab23-db7997fbbc16" -->
## Handoff Logging

<!-- section_id: "0ec5308c-b757-4834-8a8d-f00342149f70" -->
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

<!-- section_id: "31920795-528b-41b7-88a4-efbc4a417eb2" -->
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

<!-- section_id: "2d673ec0-dd6b-47f2-aeb0-14e9f442e229" -->
## Manager/Worker Pattern Observability

<!-- section_id: "20c0c361-d2c8-4d09-9a3c-b6b5eb908f78" -->
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

<!-- section_id: "5c54440e-cb5b-4db0-adae-45cbf6ec21d4" -->
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

<!-- section_id: "b6f9104e-e61b-4d65-a74a-9356f07b1258" -->
## Metrics Collection

<!-- section_id: "709d2d38-a3ba-411b-a6ae-e7f77b877b98" -->
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

<!-- section_id: "ac0bacb5-e32f-47f5-9179-95b10492c4b0" -->
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

<!-- section_id: "f3cf2e82-542c-4bcd-abf6-330889762013" -->
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

<!-- section_id: "915924d2-ba19-4af6-b108-382dc440da1b" -->
## Distributed Tracing

<!-- section_id: "dbe8b7f8-f59a-4753-be7f-989867c072de" -->
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

<!-- section_id: "e01499ba-a5be-4db0-8487-8a16a4ecc581" -->
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

<!-- section_id: "7af1664c-34fd-497a-b39c-31d15f1d275c" -->
## Log Storage Strategy

<!-- section_id: "81e0fb77-7eda-427c-8452-c2cfda98fd5e" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "84ed2a01-6485-45d7-8de2-406789d41917" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "30c8be04-d558-402e-a695-0a3b76ffe90a" -->
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

<!-- section_id: "390dbb2a-210f-4a86-8345-220e43c0b6e2" -->
## Examples

<!-- section_id: "884a46ec-9109-4f48-94fa-0279eebfd530" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "839e0f81-a0e7-421c-b9f7-622170d9fc2f" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "974e4bde-b48f-4daa-b570-d760bf56ec75" -->
## Integration Points

<!-- section_id: "db0b2eab-2cb1-4e08-a2ef-c0a12c1e8133" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "97fe7ef5-6f64-4194-a97d-085415c44271" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "966a6c19-83fa-4e5d-9947-8502ad6127fd" -->
## Tools and Libraries

<!-- section_id: "582d3d1e-768e-4b39-954a-694f8aa599c1" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "87e30e9f-6927-49e2-9f9c-72386266d262" -->
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

<!-- section_id: "2f640936-a73e-4a4b-83a5-e25fc106da9c" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "e525a784-5221-4128-8bbd-f3d1d92f304c" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active


---

<!-- section_id: "a1064562-17fe-4c71-b5aa-c243cc957ee9" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "d3bef984-90bc-46a6-87cf-81a4d37dade2" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "8e9d9658-f5ec-497e-8cae-c9b88d3cb55b" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "ad88b14f-febf-4610-9f75-19bd086f3561" -->
## Quick Reference

<!-- section_id: "ac91fe92-64c1-4950-b818-bbbfe38afecb" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "a52f638b-ab21-491a-a906-5b5f3ce7977d" -->
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

<!-- section_id: "526cd6d7-0e55-42e1-addb-85d276741ba8" -->
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

<!-- section_id: "63d255c0-1395-4f40-8ed1-9059cb523ff4" -->
## Layer-Specific Logging Requirements

<!-- section_id: "489f8c1a-c2b3-402d-a657-7dd77647acbb" -->
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

<!-- section_id: "6bf606fa-5b23-440f-9584-7644339acea7" -->
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

<!-- section_id: "5bec8598-c9d2-4254-afa1-abc72e4bcbce" -->
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

<!-- section_id: "d1607e92-959d-426c-b46e-a19030b58a37" -->
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

<!-- section_id: "3a8a67bd-5230-4b7e-9db5-96b68b622b42" -->
## Handoff Logging

<!-- section_id: "1735781b-7b48-4f85-909b-cb8da0bc8f12" -->
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

<!-- section_id: "9e383f84-647a-4ba7-a6e4-f5ded21e013d" -->
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

<!-- section_id: "c5d96c3b-0b57-4846-b162-41d8c3c75512" -->
## Manager/Worker Pattern Observability

<!-- section_id: "87a709e4-ecb9-4397-938c-409dc269179c" -->
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

<!-- section_id: "f5b8c7cb-7be3-46ee-b0bd-46ff1bae43a2" -->
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

<!-- section_id: "c45c831e-13ad-4dc5-b05e-b7db7de51093" -->
## Metrics Collection

<!-- section_id: "c066e42f-d49f-44e3-ad3a-2132a8e10181" -->
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

<!-- section_id: "9c4d624f-1b5e-4265-8658-163952519387" -->
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

<!-- section_id: "c853c0bf-6cc0-44fd-9f87-b6d6f1782903" -->
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

<!-- section_id: "b94cce30-ce74-4cc5-a934-d87150d0c5aa" -->
## Distributed Tracing

<!-- section_id: "c39bcc8a-d9c3-4f29-a73d-5262d97def50" -->
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

<!-- section_id: "d87ab706-5911-4270-9a5b-1ec4b961e4b0" -->
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

<!-- section_id: "a01e76d6-ca7b-40ef-be8b-d832dbc1035e" -->
## Log Storage Strategy

<!-- section_id: "af7d5759-f148-4c0c-845e-c5220d13c38a" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "ba359f48-a259-4919-920b-78c26d3ec543" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "36334e1e-84d6-4439-ac35-e2c92e5b6531" -->
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

<!-- section_id: "79e2da92-e90c-4f09-942e-895e48e95acf" -->
## Examples

<!-- section_id: "db0c86f2-5618-4863-8602-315319478f05" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "54077b4b-e802-4f8a-809a-862586d548f5" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "40ec89e7-2888-4647-87dd-f6a9ae44b579" -->
## Integration Points

<!-- section_id: "7700663b-8994-4823-a97d-646dd2040465" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "29468e7d-6be8-448f-8671-220e8415e627" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "b9825156-4976-449b-b376-70ae63066198" -->
## Tools and Libraries

<!-- section_id: "7d76c52d-6d9c-4a6d-8198-c1c168493db1" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "39bc4019-556c-486f-868a-89d7c6c83c48" -->
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

<!-- section_id: "d56946e2-ed21-4c9a-b6bb-853d5bfb6ce6" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "86e1e7c9-9e80-4223-9460-15167fdc19bd" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active
