---
resource_id: "2e78fa96-b04b-432b-9aba-02a6c5aa24a1"
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

<!-- section_id: "739bf361-ef65-405c-b55e-1ca86c032703" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "401bc223-eb14-47bb-97b6-b76a647555ab" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "fee4a072-eed5-401f-bf09-6ae45c82baea" -->
## Quick Reference

<!-- section_id: "ebbc12e3-ee89-4c5f-a4b8-9b8734e15765" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "11e28b27-2b9b-4e3c-84de-435b99596811" -->
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

<!-- section_id: "ca64f3e1-58d6-4f40-a83a-980d92bc9306" -->
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

<!-- section_id: "89c139d8-f095-4085-a1e3-525382ed6e29" -->
## Layer-Specific Logging Requirements

<!-- section_id: "854d8269-8e20-4e5b-835a-ec35e70610d6" -->
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

<!-- section_id: "991ccb41-dbf2-4b97-83d5-5159f588687b" -->
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

<!-- section_id: "43b08464-32a5-441f-b515-4f0151be4207" -->
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

<!-- section_id: "3d8c992b-6423-45bc-888a-24d66bcbfec4" -->
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

<!-- section_id: "0d64b9fc-26d3-4e3c-b93b-7a19fcf0fe91" -->
## Handoff Logging

<!-- section_id: "0169fc05-efa2-4079-9fad-9b5c106d0668" -->
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

<!-- section_id: "8bdcaae6-1abe-4fdf-97db-fd462f4d6fee" -->
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

<!-- section_id: "7e208f68-a3c7-4234-8a7c-95cf473ef612" -->
## Manager/Worker Pattern Observability

<!-- section_id: "714393e6-1053-441a-b351-4720cebd730b" -->
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

<!-- section_id: "a1c044b3-6ef3-4cbe-824d-bf06caeecc5b" -->
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

<!-- section_id: "e6903750-c72d-452b-ab8f-e4b3c801c9ed" -->
## Metrics Collection

<!-- section_id: "8477b62b-ef02-45ab-b769-1a28c8b52aa3" -->
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

<!-- section_id: "270fa3c1-ef99-44b9-a204-12b6988593ad" -->
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

<!-- section_id: "0aab952a-22cd-469e-8680-9b38c309d640" -->
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

<!-- section_id: "548e6835-61af-403a-9d89-226d623d004f" -->
## Distributed Tracing

<!-- section_id: "a409787f-332a-4920-9a63-a74dc4b5fff9" -->
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

<!-- section_id: "7afb5186-3b3f-4190-9418-c4d1d317b9ab" -->
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

<!-- section_id: "4b9d7d35-1882-48a2-a908-b00809fd761d" -->
## Log Storage Strategy

<!-- section_id: "a80d7560-53b1-456e-a90b-c41cf0acae33" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "07fa33d7-dc2b-476d-adb0-572b08525619" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "0c6cda1a-7f18-495b-89fb-1c51c07a0c37" -->
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

<!-- section_id: "2814a8e6-224e-4fe2-87cb-08e6e87798c0" -->
## Examples

<!-- section_id: "3c5b2019-b477-46c2-afeb-05072aa5005e" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "8dc52cd9-c00c-4582-aca4-8d02d04841d1" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "5596c2a3-b355-4ccc-8b46-9bb33d8505f0" -->
## Integration Points

<!-- section_id: "1c6e8fae-5406-4c14-b22f-dd0714e4caca" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "cefb05c8-46e0-471f-bac7-8ebf58e22dcd" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "5f2c91f5-b853-4d5a-9e7b-21d45e8b4867" -->
## Tools and Libraries

<!-- section_id: "2e0447be-201b-494f-a577-b80970fbe34d" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "a4929d42-0bf4-4f30-bbbd-038efd781351" -->
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

<!-- section_id: "34468c80-8810-47ee-9942-0b99e6df893e" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "ad9d3b53-2aa0-46a3-b55f-a3821f2006ea" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active

---

<!-- section_id: "22823406-af28-44a7-8f53-1c5a8b64e6bd" -->
## Legacy Universal Protocols Source

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "314b982c-1194-4c1f-8373-c6c3b3fbb779" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "b642b495-b9e7-4777-8777-75f60347a587" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "50a72385-1f78-4ae9-8690-caf33767b862" -->
## Quick Reference

<!-- section_id: "efe01f5b-d9c3-455d-adbf-c86b9216f85b" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "00fdbf9f-8f2d-4284-94ef-fe54433e80f4" -->
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

<!-- section_id: "776902b9-2682-4f60-a8af-25a7d8c98b21" -->
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

<!-- section_id: "0485531b-8f67-4b26-8fd5-6144fce6348d" -->
## Layer-Specific Logging Requirements

<!-- section_id: "6570172e-d8ee-41f7-acdd-7df9894d224a" -->
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

<!-- section_id: "a818d9d9-d8a9-443b-94c7-7eb8c28688e3" -->
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

<!-- section_id: "e5309b9e-5bd0-40e7-945d-9d0cafbb4fb3" -->
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

<!-- section_id: "293b2146-244a-4231-a68d-cb61179166a1" -->
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

<!-- section_id: "ede524c6-4dab-463b-98de-64d7306af6d1" -->
## Handoff Logging

<!-- section_id: "1a8b4976-b63c-46c1-836a-abdf35da1f1f" -->
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

<!-- section_id: "291b3731-0a86-4bcf-9aae-51978a52ca8c" -->
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

<!-- section_id: "51a63098-d7ef-4f0a-88dc-00b418dc68a3" -->
## Manager/Worker Pattern Observability

<!-- section_id: "c17e8f16-fe5e-4f00-ad30-700c393120f6" -->
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

<!-- section_id: "e0aca1ee-3fb2-435c-8ac0-9d96aec36605" -->
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

<!-- section_id: "b5729ee2-7605-47d4-8845-cb6bac3e8e9b" -->
## Metrics Collection

<!-- section_id: "6aa60d5c-34ef-4944-8d3c-d8529aa27106" -->
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

<!-- section_id: "6238c804-9838-4daf-b0f0-5a1bfca444b0" -->
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

<!-- section_id: "255ef6b6-3792-40f7-a165-a5b9865928c1" -->
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

<!-- section_id: "0b4cb8ef-de49-4519-bdc5-ca293527e71e" -->
## Distributed Tracing

<!-- section_id: "8a085d28-65af-460c-b4ae-cbaa2d8fbf4b" -->
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

<!-- section_id: "adf7e167-a869-4019-bcf9-35225389867b" -->
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

<!-- section_id: "f47c0f9c-dca7-42ac-8127-60557810ad20" -->
## Log Storage Strategy

<!-- section_id: "bed4a1b3-a2c6-498a-b59e-0787808c03f7" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "fc1b6829-8660-40e1-b7b7-f8f9c9fb6dc4" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "9ec4941a-d608-42b0-872c-93be6d3d7fec" -->
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

<!-- section_id: "39cfcdab-4bb0-4647-9e1a-dd71065503c3" -->
## Examples

<!-- section_id: "8c5617cf-dba6-44ab-ac62-25488e570d95" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "cf6c8282-2522-42b1-a409-e5db9435afda" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "6b5f285b-89de-402d-aab7-2edeea234d51" -->
## Integration Points

<!-- section_id: "aead0718-06a5-46b8-ab16-9b346506e0ee" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "165c31ae-8d7f-4142-a0db-bd25eb3cf7d0" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "69c7e2d2-3ded-4927-82ce-a8b7d6841f50" -->
## Tools and Libraries

<!-- section_id: "009ba26e-7977-4aa5-939e-6e870f79e950" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "6c0945c3-f348-4285-8473-7ec7f0e46a2d" -->
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

<!-- section_id: "cfd2e94c-bce3-48df-8419-5740dda1f978" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "29a8d97b-cad9-48e2-9a82-5c940ba65c60" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active


---

<!-- section_id: "738c1bdc-0db3-444f-b77a-ef91ee89ede1" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`

# Observability and Logging Protocol

**Protocol Type**: Universal
**Scope**: All Layers (L0-L3+)
**OS Applicability**: All (WSL, Linux, macOS, Windows)
**Tool Applicability**: All AI tools and managers

---

<!-- section_id: "153847c1-1678-4955-90ec-e4fba09151c5" -->
## Purpose

This protocol defines structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. It ensures the system is auditable, debuggable, and analyzable across all layers and stages.

<!-- section_id: "512b65da-bbd8-4ec5-beee-2455aa47a0ff" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Status**: Normative (refer to source for authoritative details)

---

<!-- section_id: "550b6596-fbd7-4c82-8d4e-af2d232253bd" -->
## Quick Reference

<!-- section_id: "09e15c99-44c6-41e4-8633-f918966022ff" -->
### Log Levels

- **DEBUG**: Handoff contents, API calls, decision logic
- **INFO**: Task started/completed, stage transitions
- **WARNING**: Retries, escalations, budget warnings
- **ERROR**: Task failures, API errors
- **CRITICAL**: System failures, data corruption

<!-- section_id: "5fdc8aa1-ec35-4371-943c-b5c43f933ffd" -->
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

<!-- section_id: "bcc1031b-2057-4f63-a6de-588caf394dd2" -->
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

<!-- section_id: "780eeb66-5670-49d5-bd87-495d886294ff" -->
## Layer-Specific Logging Requirements

<!-- section_id: "ab8d7203-a572-4d42-922b-553a39cde032" -->
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

<!-- section_id: "62e5ca39-a1ee-49ee-ad27-505686026cfb" -->
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

<!-- section_id: "420056e6-d56d-42c6-bdd3-c6e1f70315ab" -->
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

<!-- section_id: "4d2e9dc4-e360-4aa0-a04f-47377683298b" -->
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

<!-- section_id: "93645ebf-d89f-4ba4-94cb-5f7c6932f52d" -->
## Handoff Logging

<!-- section_id: "2333b5c4-2975-43db-824f-90698b35c4f8" -->
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

<!-- section_id: "e9f14eb6-7e98-4e90-bb44-8b90b3c089a6" -->
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

<!-- section_id: "f8720cce-cf88-487f-a59d-4c6b1db09ce4" -->
## Manager/Worker Pattern Observability

<!-- section_id: "c4f967eb-3cd2-4101-b8cf-ae42888bde79" -->
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

<!-- section_id: "e1d48e55-0c7d-4648-ae1a-2f23e5688b44" -->
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

<!-- section_id: "bf7154bb-6166-4d8c-acc0-16d923ce05a1" -->
## Metrics Collection

<!-- section_id: "eacdeba4-663e-4458-b6ae-20c8a7c3078e" -->
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

<!-- section_id: "a645e815-4ebf-4b64-a134-07080a1ed627" -->
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

<!-- section_id: "0ee831c9-50cf-43b1-84a5-95c13612a2eb" -->
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

<!-- section_id: "fe06a798-9277-4e33-96c5-a14eb1a5506f" -->
## Distributed Tracing

<!-- section_id: "5de7332c-dcda-4601-85a7-b7070d870c6a" -->
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

<!-- section_id: "a92f9727-5276-4b0c-8c07-b2622b704892" -->
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

<!-- section_id: "e8cbfbdf-2477-4c06-bf5b-fac2187adb76" -->
## Log Storage Strategy

<!-- section_id: "0f3bbf83-27e8-47e4-9380-3fe456416b1d" -->
### Development Environment

- **Location**: `<layer>/logs/*.log` files in project directory
- **Format**: Human-readable text with structured JSON for metrics
- **Retention**: 7 days
- **Tools**: `tail -f`, `grep`, `jq` for analysis

<!-- section_id: "bab22843-563a-4de4-a111-7adc6c2343ca" -->
### Production Environment

- **Location**: Centralized logging service (see deployment guide)
- **Format**: Structured JSON (JSONL)
- **Retention**: See normative spec for tiered retention policy
- **Tools**: Elasticsearch/Kibana, Grafana, Jaeger for tracing

---

<!-- section_id: "525ac256-d1c9-4294-8d9b-e27eff810427" -->
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

<!-- section_id: "24c2b28f-8bc1-4692-863d-062eba3b1e4a" -->
## Examples

<!-- section_id: "af51cc83-4e95-4f7e-ac77-45b6372f2fc7" -->
### Full Task Lifecycle

See the normative specification (`observability_and_logging.md`) Section 2.1 for complete JSON schemas of:

- Task Started
- Task Completed
- Task Failed
- Agent Spawned
- Agent Message
- Agent Tool Use

<!-- section_id: "9ef50f70-06ee-4317-b50c-1eba45451d61" -->
### Supervisor Events

See the normative specification Section 2.3 for:

- Supervisor Started
- Policy Applied
- Budget Check

---

<!-- section_id: "4292dcc7-55da-44a7-a8a1-08fe21bd54ca" -->
## Integration Points

<!-- section_id: "4c0c5cf7-244f-40c5-abeb-9322938f0295" -->
### With Safety & Governance

Observability logs feed into safety/governance systems:

- Budget violations trigger alerts
- Permission violations are audited
- Human approvals are logged with full context

See: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

<!-- section_id: "b733a81e-cdd7-494c-9d10-dbf9c52c4baf" -->
### With Deployment

Production deployments require observability infrastructure:

- Log aggregation and storage
- Metrics collection and visualization
- Distributed tracing setup

See: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "26b43b4a-7937-43e6-a7a1-761cb2417551" -->
## Tools and Libraries

<!-- section_id: "f30626d2-c25b-480d-9e1e-4c093c9261b8" -->
### Recommended Stack

- **Logging**: Python `logging` module with JSON formatter
- **Metrics**: Prometheus client libraries
- **Tracing**: OpenTelemetry SDK
- **Visualization**: Grafana dashboards

<!-- section_id: "ede7b22e-d69c-4979-b95f-075dd1a86320" -->
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

<!-- section_id: "3808fa5e-e4cf-46b7-8291-478e2478a630" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/observability_and_logging.md`
- **Handoff Schema**: `layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- **Safety & Governance**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- **Deployment Guide**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/.../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "509a0fe6-c9e3-48ba-9e96-4fddc747c1f7" -->
## Compliance

This protocol follows the **Protocol Writing Standard**:

- See: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/protocol_writing_standard/`

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active
