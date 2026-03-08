---
resource_id: "d74b10b9-6dbc-4e2c-b1d2-8202636aaa2e"
resource_type: "readme_document"
resource_name: "README"
---
# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "8cd0b660-b649-44c0-a3ca-652c1e180b99" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "af8c34ae-2c4e-4aac-9bcb-0937ad7ac025" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "826940c0-7063-4576-aa5d-63cf26540c4e" -->
## Quick Reference

<!-- section_id: "1a7e10c2-3292-406a-860f-c78ffb5e9044" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "bc07296a-8201-4df6-82bb-5bc71545ff0e" -->
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

<!-- section_id: "ebe4b9fd-3e43-47b9-a7dd-6cb88db2f032" -->
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

<!-- section_id: "6c61cf6a-d9fc-4f6e-9624-d99304c3835a" -->
## Layer-Specific Logging Requirements

<!-- section_id: "4ab2cfd1-37a4-4c95-bf70-aaf4e2613445" -->
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

<!-- section_id: "24252eb9-24f9-4565-a381-85ff925d97e4" -->
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

<!-- section_id: "14004058-d099-4f02-bb86-68f6fcf791c6" -->
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

<!-- section_id: "02727c20-85f3-4393-94aa-b62ff85e4a85" -->
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

<!-- section_id: "b7ed35ea-920d-437a-b029-123dd8dc42a0" -->
## Handoff Logging

<!-- section_id: "d28e9abf-fbfc-4dd2-84d1-3c382a0ca17c" -->
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

<!-- section_id: "96bf3269-bbb7-46ac-a70f-30888f1bdf8f" -->
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

<!-- section_id: "e9e8f3c0-e556-45ec-9845-677eb61e0bb7" -->
## Manager/Worker Pattern Observability

<!-- section_id: "3b50c033-9829-465d-b7e5-a14d20e8f3b2" -->
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

<!-- section_id: "b4eaa6c9-3045-496a-bda9-44b87bc2a1a6" -->
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

<!-- section_id: "ed38e3c4-b643-4da1-ae2b-26d630fb68af" -->
## Metrics Collection

<!-- section_id: "23b4e8f5-0482-4c07-9ce2-c54aea196937" -->
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

<!-- section_id: "d553dde9-930a-4fcd-b68f-442862f1561b" -->
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

<!-- section_id: "61386735-086a-4eed-9399-30e345dd84dc" -->
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

<!-- section_id: "0916db3a-e3bf-49bc-acb5-a45292b87c18" -->
## Distributed Tracing

<!-- section_id: "e7197feb-9292-4b66-a82e-67410f154fee" -->
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

<!-- section_id: "1f7ba97a-d377-4bfc-8b37-90a24e066f6a" -->
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

<!-- section_id: "2b07354a-8ca0-46ad-b3ae-5f8184b3accd" -->
## Log Storage Strategy

<!-- section_id: "2e049eb4-b7c1-4400-9a2b-488914902203" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "9a0e2ee2-67aa-45c2-b9d5-1101750c8105" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "a2c9c129-22fb-4587-8079-0b725d48d615" -->
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

<!-- section_id: "b8b5daa2-2611-4f47-aaed-02d8b5b72ea9" -->
## Examples

<!-- section_id: "915a2f6a-aa6a-4d6b-8694-c88e3ac5884e" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "772e60c7-ea45-4a26-9aeb-452d44b9d547" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "4df7811c-213c-44f1-8835-c2754f784167" -->
## Integration Points

<!-- section_id: "6ea6f47c-0d82-4735-8d1b-32e1e180556e" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "82b98599-fd87-43e7-9b37-7d65504e9f49" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "83154805-fed1-436e-bcc8-68526ff79c5a" -->
## Tools and Libraries

<!-- section_id: "86c7891f-1ab1-48e5-95ff-1e7a76f41bff" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "db892072-2c8e-417a-8045-6c7c615e3f5c" -->
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

<!-- section_id: "5e648b81-1445-4833-be27-709c84655338" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "484774ca-ca73-4db8-ad2e-85f5d72d2f03" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active

---

<!-- section_id: "f5deb51b-b34c-4eab-a89e-67b2109bdb08" -->
## Legacy Universal Protocols Source

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "91808d7d-1da6-4aee-adea-60dc13ab3e14" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "f95abc85-a8ef-401d-b87f-bb1d95fd87cc" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "a2303cac-678c-4f3e-ac36-ad95e8d91766" -->
## Quick Reference

<!-- section_id: "d08def55-1b90-4c8a-a827-69a58aac77af" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "93a3c2ca-f949-450e-8532-d8d4b26be13b" -->
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

<!-- section_id: "e3d050a2-e931-4bc4-8af1-9ef0414ad528" -->
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

<!-- section_id: "9b468627-b103-4677-8fdd-e978db212335" -->
## Layer-Specific Logging Requirements

<!-- section_id: "a7f6990e-e7d1-4117-842b-03d33a652610" -->
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

<!-- section_id: "f94e70b4-0814-4546-818a-47bf357e589c" -->
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

<!-- section_id: "d484db67-0088-450d-872e-c5d447fa1af8" -->
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

<!-- section_id: "ff870a0e-f298-4c12-a038-fa943741b9ce" -->
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

<!-- section_id: "43bc4c42-c985-4272-ac2c-63f91c0edfb4" -->
## Handoff Logging

<!-- section_id: "728bf751-876c-4209-ad41-28256f821093" -->
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

<!-- section_id: "408d43ae-6b68-4f8d-b3ac-6b41205259d9" -->
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

<!-- section_id: "7f69a6e5-a5a5-46f4-aff3-770fe265a4be" -->
## Manager/Worker Pattern Observability

<!-- section_id: "8bc465dd-a4cc-4693-8b48-75932520993e" -->
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

<!-- section_id: "d522638f-4a53-4338-bd77-408719c302cf" -->
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

<!-- section_id: "04c7bf1a-f9d0-4ed3-a5f9-97b490706344" -->
## Metrics Collection

<!-- section_id: "01c9b5b6-0f71-43ce-bd6d-41c8cb04e9e6" -->
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

<!-- section_id: "a8b43d54-f523-4ab1-b0e0-03b029699d8e" -->
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

<!-- section_id: "605d86ec-0c2c-4399-9ff9-c1c9a2f690d4" -->
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

<!-- section_id: "dce0cb53-065b-4d68-a330-19fd98e13f94" -->
## Distributed Tracing

<!-- section_id: "014d00ee-d42d-4070-85d3-bca0e937633a" -->
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

<!-- section_id: "cc8befa2-6201-4db1-b3d6-232c161fe5ba" -->
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

<!-- section_id: "0c29c4f0-2310-43b9-899a-318d2c5b0d12" -->
## Log Storage Strategy

<!-- section_id: "c0cf4352-e3b2-461d-b2c0-6805a923988b" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "0e445966-b6cd-4693-ae0d-0bb61db23777" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "0fd5e475-092e-4b23-aada-6c0ad42838c5" -->
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

<!-- section_id: "c7cadae1-e2b0-4296-9a66-3b382b12b652" -->
## Examples

<!-- section_id: "668872a6-b415-42c2-8a47-8ec4c848c240" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "f45819e5-757a-4c66-b902-5df312f2b2f6" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "65d146f0-db44-4207-93aa-78f1b21d4dbc" -->
## Integration Points

<!-- section_id: "cb498da8-0a59-4790-b249-129fcd66fc24" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "8eb5d47d-1fbe-4505-b2ae-733a945344c1" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "f3c84937-d155-473b-8a20-96ea769813c9" -->
## Tools and Libraries

<!-- section_id: "b29c138c-719e-4f9d-8b0d-86a181ba12f6" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "935efa6f-a3b7-4fb7-9bbe-e681c8d3a0c6" -->
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

<!-- section_id: "f2d6ead1-5276-45c2-afff-ed1e703965c6" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "c3b85b1c-0ff7-4094-82f9-dd60be25edf6" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active


---

<!-- section_id: "24cf2c48-c487-4ddc-8553-7d8adc78139c" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "4cdf4968-928b-4470-8205-5c5d6613ff17" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "3884b78c-c1c7-43ba-9111-4a0c513bd2b9" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "10ea9dbc-da8a-4132-9cd7-3565912b29e0" -->
## Quick Reference

<!-- section_id: "2d063c2c-052d-4360-84e1-0f1e91635478" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "b5c27751-ad08-40ec-bb15-05f6492404b6" -->
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

<!-- section_id: "d4f8499d-659e-4aaf-9eb8-8e43f1c5d190" -->
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

<!-- section_id: "ce2144ab-fdb7-4020-a4e5-ac7e17d97213" -->
## Layer-Specific Logging Requirements

<!-- section_id: "b554fe37-3e40-4bdc-ab82-c19bdbb77d0b" -->
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

<!-- section_id: "29ed98f4-80c9-40c4-b254-37acc38c01f4" -->
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

<!-- section_id: "43a920dc-62f6-4e52-91d5-215dc9d94577" -->
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

<!-- section_id: "fd76366c-90e7-4a86-bf29-0260f8691506" -->
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

<!-- section_id: "fbd49909-8bdc-4d9e-8eb7-23d679aadb73" -->
## Handoff Logging

<!-- section_id: "0f648b83-334e-4524-9076-57f31804e355" -->
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

<!-- section_id: "81c4b91d-59ca-44da-a829-f5cbe6da568f" -->
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

<!-- section_id: "8883ed15-7e6d-4784-93a8-edb5674a03b2" -->
## Manager/Worker Pattern Observability

<!-- section_id: "b4657ee2-5fa1-4a7d-8ead-8f371f7e7aee" -->
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

<!-- section_id: "43d840b9-e17c-4329-9a38-a313a591f902" -->
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

<!-- section_id: "fb7f9c98-b8ae-4d4a-a7ba-6390a59bb67d" -->
## Metrics Collection

<!-- section_id: "b558ca4a-cd1e-4e05-b98d-c23455acca8f" -->
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

<!-- section_id: "ee85f821-1c5d-4139-b374-50e172076853" -->
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

<!-- section_id: "ffd93008-5859-4626-8492-bbbb38132065" -->
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

<!-- section_id: "b183b3bf-aee7-47e6-aec3-41cf4ebcc711" -->
## Distributed Tracing

<!-- section_id: "2ed44c2d-e933-425d-8442-ac18c5b0ba9f" -->
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

<!-- section_id: "dc191115-5a49-41e0-be47-ea6be7226696" -->
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

<!-- section_id: "5c5e073e-1820-4abf-a71b-f354b8335a2a" -->
## Log Storage Strategy

<!-- section_id: "9b0e7a20-bd77-48a7-9b2c-15343f59324d" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "2009dad7-4b83-4e7c-88ce-4194b21539b8" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "01ae925f-2c5f-4e25-93ba-33eac78e4f48" -->
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

<!-- section_id: "c6048dd4-1269-491b-9c79-603fe960f17f" -->
## Examples

<!-- section_id: "1d90c3fe-e914-4477-ac0f-f989ac941791" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "ca110d6f-2d62-442d-811d-c977caf9933b" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "994c5506-ecfe-4523-8cb1-8b28ee701026" -->
## Integration Points

<!-- section_id: "ffb00dda-e355-4216-b39c-04426941fdad" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "5d404a85-35f0-4030-b84c-4f8f3fb76a38" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "b866e9b6-0fa0-4fc4-890c-30c1837ad48b" -->
## Tools and Libraries

<!-- section_id: "2c63f31c-0c16-400f-a241-e0a570afea2c" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "ffea6a95-64f1-45a5-a356-2190e68c51e6" -->
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

<!-- section_id: "61b1a3ad-77d9-4308-afd1-a2a16656e337" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "a871a005-c5b8-4c9d-9d54-2770f3ec0981" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active
