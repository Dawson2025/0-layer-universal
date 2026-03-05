---
resource_id: "88b322eb-bc51-45e8-b753-b278cb392970"
resource_type: "knowledge"
resource_name: "observability_and_logging"
---
<!-- section_id: "350949a8-7bf1-4b81-a0d1-1e3999e261e7" -->
## Observability and Logging Framework

This document defines structured logging, monitoring, and observability patterns for the AI manager hierarchy system.

It ensures the system is:
- **Auditable**: Full trace of decisions and actions
- **Debuggable**: Easy to identify failures and bottlenecks
- **Analyzable**: Data-driven optimization of policies and workflows

---

<!-- section_id: "132bbd43-fa46-4766-8c52-a5710afffb57" -->
## 1. Logging Levels and Contexts

<!-- section_id: "77176b3f-e456-4b83-8935-a350d06b352c" -->
### 1.1 Log Levels

Following standard severity hierarchy:

- **DEBUG**: Detailed diagnostic information (handoff contents, API calls, decision logic)
- **INFO**: General operational events (task started, completed, stage transitions)
- **WARNING**: Potentially problematic situations (retries, escalations, budget warnings)
- **ERROR**: Failures that require attention (task failures, API errors)
- **CRITICAL**: System-level failures (supervisor crashes, data corruption)

<!-- section_id: "85effd3d-e685-4dc1-b086-458364e3b8a0" -->
### 1.2 Contextual Logging

Every log entry includes:

```json
{
  "timestamp": "2025-01-15T10:30:45.123Z",
  "level": "INFO",
  "logger": "supervisor.task_executor",
  "message": "Task completed successfully",
  "context": {
    "task_id": "task-L2-auth-impl-20250115-103045",
    "layer": 2,
    "stage": "implementation",
    "tool": "codex",
    "model": "codestral",
    "handoff_id": "handoff-20250115-102030"
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

<!-- section_id: "b325f809-8d93-424d-8147-aa05461c16de" -->
## 2. Structured Logging Schema

<!-- section_id: "a825106d-b7ce-4326-bc82-db398ec329d7" -->
### 2.1 Task Lifecycle Events

**Task Started:**
```json
{
  "event": "task.started",
  "task_id": "task-L3-login-impl",
  "layer": 3,
  "stage": "implementation",
  "tool": "codex",
  "model": "codestral",
  "handoff": {
    "id": "handoff-login-20250115",
    "task": "Implement login form component",
    "constraints": ["TypeScript", "React", "Accessibility"]
  },
  "estimated_cost": 0.05,
  "priority": "normal"
}
```

**Task Completed:**
```json
{
  "event": "task.completed",
  "task_id": "task-L3-login-impl",
  "status": "success",
  "duration_ms": 8500,
  "tokens": {"input": 1200, "output": 850, "total": 2050},
  "cost_usd": 0.0205,
  "artifacts": {
    "files_created": ["LoginForm.tsx", "LoginForm.test.tsx"],
    "files_modified": ["index.ts"],
    "lines_added": 120,
    "lines_deleted": 5
  },
  "quality_metrics": {
    "lint_errors": 0,
    "test_coverage": 0.85,
    "complexity_score": 12
  }
}
```

**Task Failed:**
```json
{
  "event": "task.failed",
  "task_id": "task-L3-login-impl",
  "error": {
    "type": "ValidationError",
    "message": "TypeScript compilation failed",
    "details": "Cannot find module 'react-hook-form'",
    "stack_trace": "..."
  },
  "retry_count": 1,
  "will_retry": true,
  "next_retry_at": "2025-01-15T10:32:00Z"
}
```

<!-- section_id: "ba0702d7-ee8b-40e5-a64e-403a71155d5c" -->
### 2.2 Agent Interaction Events

**Agent Spawned:**
```json
{
  "event": "agent.spawned",
  "agent_id": "agent-codex-20250115-103045",
  "tool": "codex",
  "model": "codestral",
  "parent_task_id": "task-L3-login-impl",
  "process_id": 12345,
  "command": "codex --model codestral execute-handoff handoff-login-20250115"
}
```

**Agent Message:**
```json
{
  "event": "agent.message",
  "agent_id": "agent-codex-20250115-103045",
  "role": "assistant",
  "content_preview": "I'll implement the login form component...",
  "content_length": 1250,
  "tokens": 320,
  "tool_calls": [
    {"tool": "write_file", "args": {"path": "LoginForm.tsx"}}
  ]
}
```

**Agent Tool Use:**
```json
{
  "event": "agent.tool_use",
  "agent_id": "agent-codex-20250115-103045",
  "tool": "write_file",
  "args": {"path": "LoginForm.tsx", "content_length": 2400},
  "result": "success",
  "duration_ms": 150
}
```

<!-- section_id: "31549b00-6892-49ee-8e64-55efcc73b48e" -->
### 2.3 Supervisor Events

**Supervisor Started:**
```json
{
  "event": "supervisor.started",
  "supervisor_id": "supervisor-main",
  "root_dir": "/workspace",
  "policy_version": "1.2.0",
  "watched_layers": [0, 1, 2, 3],
  "worker_count": 4
}
```

**Policy Applied:**
```json
{
  "event": "supervisor.policy_applied",
  "task_id": "task-L2-auth-plan",
  "layer": 2,
  "stage": "planning",
  "selected_tool": "claude-code",
  "selected_model": "claude-sonnet-4.5",
  "reason": "Layer 2 planning requires deep reasoning",
  "alternatives_considered": ["gemini-pro-2", "gpt-4-turbo"]
}
```

**Budget Check:**
```json
{
  "event": "supervisor.budget_check",
  "layer": 3,
  "stage": "implementation",
  "estimated_cost": 0.50,
  "remaining_budget": {
    "daily": 45.50,
    "task_limit": 2.00
  },
  "approved": true
}
```

---

<!-- section_id: "ef7e4480-f061-41b2-a0d5-f13fa754486e" -->
## 3. Log Storage and Retention

<!-- section_id: "55b0e79c-ff44-4cee-a231-0950cebeb72a" -->
### 3.1 Storage Backends

**Local Files (Development):**
```python
import logging
from logging.handlers import RotatingFileHandler

# Structured JSON logs
json_handler = RotatingFileHandler(
    "logs/supervisor.jsonl",
    maxBytes=100_000_000,  # 100MB
    backupCount=10
)
json_handler.setFormatter(JsonFormatter())

# Human-readable logs
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)

logger = logging.getLogger("supervisor")
logger.addHandler(json_handler)
logger.addHandler(console_handler)
```

**Cloud Logging (Production):**
```python
# Google Cloud Logging
from google.cloud import logging as cloud_logging

client = cloud_logging.Client()
logger = client.logger("ai-manager-supervisor")

def log_event(event_type, **kwargs):
    logger.log_struct({
        "event": event_type,
        **kwargs
    }, severity="INFO")

# AWS CloudWatch
import boto3

logs_client = boto3.client('logs')

def log_to_cloudwatch(log_group, log_stream, event):
    logs_client.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[{
            'timestamp': int(time.time() * 1000),
            'message': json.dumps(event)
        }]
    )
```

<!-- section_id: "58867177-5d06-4e02-96ed-5a55575767a6" -->
### 3.2 Retention Policy

```yaml
retention:
  # Hot storage (queryable, indexed)
  hot:
    duration: 7 days
    storage: elasticsearch
    indices: ["task-*", "agent-*", "supervisor-*"]

  # Warm storage (archived, slower queries)
  warm:
    duration: 90 days
    storage: s3
    compression: gzip

  # Cold storage (compliance, long-term)
  cold:
    duration: 1 year
    storage: glacier
    encryption: required

  # Aggregated metrics (permanent)
  metrics:
    duration: forever
    storage: timescaledb
    rollup: daily
```

---

<!-- section_id: "256c1cf1-8746-4c98-9c3d-56f9b4a99842" -->
## 4. Distributed Tracing

<!-- section_id: "67a03b41-ae35-4f3a-b890-f0d739d70603" -->
### 4.1 OpenTelemetry Integration

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger import JaegerExporter

# Setup tracer
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Export to Jaeger
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Trace task execution
def execute_task_with_tracing(task_id, layer, stage, handoff):
    with tracer.start_as_current_span(
        f"task.{layer}.{stage}",
        attributes={
            "task.id": task_id,
            "task.layer": layer,
            "task.stage": stage,
            "handoff.id": handoff["id"]
        }
    ) as span:
        try:
            result = execute_task(task_id, layer, stage, handoff)
            span.set_attribute("task.status", "success")
            span.set_attribute("task.cost", result["cost"])
            return result
        except Exception as e:
            span.set_attribute("task.status", "failed")
            span.record_exception(e)
            raise
```

<!-- section_id: "841fec14-19e9-46bf-96fe-6e8205f0522f" -->
### 4.2 Trace Visualization

Traces show full workflow from L0 to L4:

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

---

<!-- section_id: "89cde335-21f2-4f3c-aaba-68eb34f1ad83" -->
## 5. Metrics and Monitoring

<!-- section_id: "00146473-5fc3-44aa-a48e-0df07c8513e3" -->
### 5.1 Key Metrics

**Task Metrics:**
- Task success rate (by layer, stage, tool, model)
- Task duration (p50, p95, p99)
- Task retry rate
- Task escalation rate

**Cost Metrics:**
- Total spend (daily, weekly, monthly)
- Cost per task (by layer, stage)
- Cost per line of code
- Budget utilization percentage

**Quality Metrics:**
- Code quality scores (linting, coverage, complexity)
- Test pass rate
- Human review approval rate
- Revision/rework rate

**Performance Metrics:**
- Throughput (tasks per hour)
- Latency (time to first response)
- Worker utilization
- Queue depth

<!-- section_id: "471580ea-c27b-4f68-9fea-141b22142fa3" -->
### 5.2 Metrics Collection

```python
from prometheus_client import Counter, Histogram, Gauge

# Counters
tasks_total = Counter(
    'tasks_total',
    'Total number of tasks',
    ['layer', 'stage', 'status']
)

tokens_total = Counter(
    'tokens_total',
    'Total tokens consumed',
    ['model', 'direction']  # direction: input/output
)

cost_total = Counter(
    'cost_usd_total',
    'Total cost in USD',
    ['layer', 'stage', 'model']
)

# Histograms
task_duration = Histogram(
    'task_duration_seconds',
    'Task execution duration',
    ['layer', 'stage'],
    buckets=[1, 5, 10, 30, 60, 300, 600]
)

# Gauges
active_tasks = Gauge(
    'active_tasks',
    'Number of currently running tasks',
    ['layer']
)

budget_remaining = Gauge(
    'budget_remaining_usd',
    'Remaining budget',
    ['layer', 'period']  # period: daily/weekly/monthly
)

# Usage
def execute_task_with_metrics(task_id, layer, stage, tool, model):
    active_tasks.labels(layer=layer).inc()
    start = time.time()

    try:
        result = execute_task(task_id, layer, stage, tool, model)

        # Record success
        tasks_total.labels(layer=layer, stage=stage, status='success').inc()
        tokens_total.labels(model=model, direction='input').inc(result['tokens_in'])
        tokens_total.labels(model=model, direction='output').inc(result['tokens_out'])
        cost_total.labels(layer=layer, stage=stage, model=model).inc(result['cost'])

        return result

    except Exception as e:
        # Record failure
        tasks_total.labels(layer=layer, stage=stage, status='failed').inc()
        raise

    finally:
        # Record duration
        duration = time.time() - start
        task_duration.labels(layer=layer, stage=stage).observe(duration)
        active_tasks.labels(layer=layer).dec()
```

<!-- section_id: "c024baec-b5f1-48c1-9be5-5349b6650e21" -->
### 5.3 Alerting Rules

```yaml
alerts:
  - name: HighTaskFailureRate
    condition: task_failure_rate > 0.2
    window: 1h
    severity: warning
    action: notify_team

  - name: BudgetExceeded
    condition: daily_spend > daily_budget * 0.9
    severity: critical
    action: throttle_tasks

  - name: TaskTimeout
    condition: task_duration > task_timeout
    severity: warning
    action: escalate_to_human

  - name: SupervisorDown
    condition: supervisor_heartbeat_missing > 5m
    severity: critical
    action: restart_supervisor
```

---

<!-- section_id: "89af67a2-0565-4691-82c7-4ef82081d754" -->
## 6. Audit Trail

<!-- section_id: "256c8899-8915-4704-ba3b-77882b1787c6" -->
### 6.1 Immutable Audit Log

Every decision and action is logged:

```python
class AuditLogger:
    """Immutable audit trail for compliance and debugging."""

    def __init__(self, backend="postgresql"):
        self.backend = backend

    def log_decision(self, decision_type, context, rationale, outcome):
        """Log a decision made by supervisor or agent."""
        entry = {
            "id": generate_uuid(),
            "timestamp": datetime.utcnow().isoformat(),
            "type": decision_type,
            "context": context,
            "rationale": rationale,
            "outcome": outcome,
            "immutable_hash": None  # Computed below
        }

        # Compute hash for integrity
        entry["immutable_hash"] = compute_hash(entry)

        # Store in append-only log
        self.append_to_audit_log(entry)

        return entry

# Usage
audit = AuditLogger()

audit.log_decision(
    decision_type="model_selection",
    context={
        "layer": 2,
        "stage": "implementation",
        "task_id": "task-L2-auth-impl"
    },
    rationale="Task complexity (0.6) and layer (2) match balanced tier policy",
    outcome={
        "selected_model": "claude-haiku",
        "estimated_cost": 0.50
    }
)
```

<!-- section_id: "9159c6ce-0d39-4874-a31f-c42bdbd5233d" -->
### 6.2 Queryable Audit API

```python
@app.route("/api/audit/search")
def search_audit():
    """Search audit trail."""
    filters = {
        "start_time": request.args.get("start"),
        "end_time": request.args.get("end"),
        "decision_type": request.args.get("type"),
        "layer": request.args.get("layer"),
        "task_id": request.args.get("task_id")
    }

    results = audit.search(**filters)
    return jsonify(results)

# Example queries:
# /api/audit/search?type=model_selection&layer=2
# /api/audit/search?task_id=task-L2-auth-impl
# /api/audit/search?start=2025-01-01&end=2025-01-31
```

---

<!-- section_id: "1f08456e-2668-47ed-b01b-57b680710e1b" -->
## 7. Observability Dashboard

<!-- section_id: "e8bfe50b-6ffc-4cd3-8318-fe1567f3fdef" -->
### 7.1 Real-Time Dashboard Components

**Overview Panel:**
- Active tasks by layer/stage
- Success/failure rates (last hour, day, week)
- Current spend vs budget
- Worker utilization

**Task Timeline:**
- Gantt chart of running and recent tasks
- Color-coded by status (running, success, failed, escalated)
- Drill-down to individual task details

**Cost Analysis:**
- Spend by layer/stage/model
- Cost trends over time
- Budget burn rate and projections

**Quality Metrics:**
- Code quality trends
- Test coverage by component
- Human review outcomes

<!-- section_id: "34d888ae-e4cc-4ec8-9a33-109a91db5ccb" -->
### 7.2 Implementation (Grafana Example)

```yaml
# Grafana dashboard JSON
{
  "dashboard": {
    "title": "AI Manager Hierarchy - Supervisor",
    "panels": [
      {
        "title": "Active Tasks by Layer",
        "type": "graph",
        "targets": [
          {
            "expr": "active_tasks{layer=~\".*\"}",
            "legendFormat": "Layer {{layer}}"
          }
        ]
      },
      {
        "title": "Task Success Rate",
        "type": "stat",
        "targets": [
          {
            "expr": "rate(tasks_total{status=\"success\"}[1h]) / rate(tasks_total[1h])",
            "format": "percent"
          }
        ]
      },
      {
        "title": "Daily Spend",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(increase(cost_usd_total[24h]))"
          }
        ],
        "fieldConfig": {
          "max": 500,
          "thresholds": [
            {"value": 0, "color": "green"},
            {"value": 400, "color": "yellow"},
            {"value": 450, "color": "red"}
          ]
        }
      }
    ]
  }
}
```

---

<!-- section_id: "120baca2-23fc-4926-a60f-7655f8512057" -->
## 8. Summary

Comprehensive observability requires:

1. **Structured Logging**: JSON logs with full context
2. **Distributed Tracing**: End-to-end workflow visibility
3. **Metrics Collection**: Prometheus/Grafana for real-time monitoring
4. **Audit Trail**: Immutable record of all decisions
5. **Dashboards**: Real-time visibility for operators
6. **Alerting**: Proactive issue detection

This framework provides the foundation for:
- Debugging complex multi-layer workflows
- Optimizing cost and performance
- Ensuring compliance and auditability
- Continuous improvement based on data
