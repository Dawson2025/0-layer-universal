---
resource_id: "568a9df1-044e-4c59-b975-cbf3851f107d"
resource_type: "knowledge"
resource_name: "production_deployment"
---
## Production Deployment Guide

This document provides guidance for deploying the AI manager hierarchy system to production environments.

It covers:
- Deployment architectures
- Scaling considerations
- Reliability and fault tolerance
- Operational best practices

---

## 1. Deployment Architectures

### 1.1 Single-Machine Development

**Architecture:**
- Supervisor, managers, and workers on one machine
- File-based handoffs in local filesystem
- SQLite for task tracking

**Pros:**
- Simple setup
- Easy debugging
- Low cost

**Cons:**
- No horizontal scaling
- Single point of failure
- Limited throughput

**Use Cases:**
- Development and testing
- Personal projects
- Small teams

### 1.2 Distributed Production

**Architecture:**
```
┌─────────────────────────────────────────┐
│  Load Balancer (HAProxy/nginx)         │
└───────────┬─────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│  Supervisor Cluster (N replicas)        │
│  - Leader election (etcd/Consul)        │
│  - Shared state (PostgreSQL/Redis)      │
└───────────┬─────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│  Task Queue (RabbitMQ/Redis/SQS)       │
│  - Priority queues per layer            │
│  - Dead letter queues for failures      │
└───────────┬─────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│  Worker Pool (Auto-scaling)             │
│  - Kubernetes pods or ECS tasks         │
│  - Scale based on queue depth           │
└───────────┬─────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────┐
│  Shared Storage (S3/GCS/Azure Blob)    │
│  - Handoff documents                    │
│  - Code artifacts                       │
│  - Logs and traces                      │
└─────────────────────────────────────────┘
```

**Pros:**
- Horizontal scaling
- High availability
- Geographic distribution

**Cons:**
- Complex setup
- Higher cost
- Network latency

**Use Cases:**
- Production deployments
- Large organizations
- High-volume workloads

### 1.3 Hybrid Cloud/Local

**Architecture:**
- L0-L2 managers in cloud (always available)
- L3-L4 workers on-premise or cloud
- Sensitive data stays local

**Use Cases:**
- Privacy/compliance requirements
- Cost optimization (cheap local GPUs)
- Low-latency requirements

---

## 2. Scaling Guidelines

### 2.1 Recommended Limits

**Layer Depth:**
- **Development**: L0-L3 (4 layers)
- **Production**: L0-L4 (5 layers)
- **Maximum**: L0-L5 (6 layers)

**Reasoning:**
- Deeper hierarchies increase latency and complexity
- Diminishing returns beyond 5-6 layers
- Context pollution risk in very deep hierarchies

**Scaling Dimensions:**

| Metric | Small | Medium | Large | Enterprise |
|--------|-------|--------|-------|------------|
| Tasks/day | <100 | 100-1000 | 1K-10K | >10K |
| Concurrent workers | 2-4 | 10-20 | 50-100 | 100+ |
| Supervisor replicas | 1 | 2-3 | 3-5 | 5+ |
| Queue throughput | 10/min | 100/min | 1K/min | 10K/min |
| Storage (handoffs) | 1GB | 10GB | 100GB | 1TB+ |

### 2.2 Auto-Scaling Policies

**Worker Auto-Scaling:**
```yaml
# Kubernetes HPA example
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: worker-pool
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-worker
  minReplicas: 2
  maxReplicas: 50
  metrics:
    - type: External
      external:
        metric:
          name: queue_depth
        target:
          type: AverageValue
          averageValue: "10"  # Scale when >10 tasks per worker

    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70

  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # Wait 5min before scaling down
      policies:
        - type: Percent
          value: 50  # Scale down by 50% at most
          periodSeconds: 60

    scaleUp:
      stabilizationWindowSeconds: 0  # Scale up immediately
      policies:
        - type: Pods
          value: 4  # Add up to 4 pods at once
          periodSeconds: 60
```

**Cost-Based Scaling:**
```python
class CostAwareScaler:
    """Scale workers based on cost and demand."""

    def should_scale_up(self, queue_depth, current_workers, budget):
        # Don't scale if near budget limit
        if get_daily_spend() > budget * 0.9:
            return False

        # Scale based on queue depth and current capacity
        tasks_per_worker = queue_depth / max(current_workers, 1)

        if tasks_per_worker > 10:  # Overwhelmed
            return True

        return False

    def should_scale_down(self, queue_depth, current_workers):
        # Only scale down if significantly underutilized
        tasks_per_worker = queue_depth / max(current_workers, 1)

        if tasks_per_worker < 2 and current_workers > 2:
            return True

        return False
```

---

## 3. Reliability and Fault Tolerance

### 3.1 Failure Modes and Mitigations

**Supervisor Failure:**
- **Problem**: Supervisor crashes, tasks orphaned
- **Mitigation**:
  - Multiple supervisor replicas with leader election
  - Health checks and auto-restart
  - Task state persisted to database

**Worker Failure:**
- **Problem**: Worker crashes mid-task
- **Mitigation**:
  - Task timeouts trigger retries
  - Idempotent task design
  - Failed tasks go to dead letter queue

**Model API Failure:**
- **Problem**: Claude/OpenAI/Gemini API down
- **Mitigation**:
  - Automatic fallback to alternative models
  - Circuit breakers prevent cascading failures
  - Queue tasks for retry when service returns

**Network Partition:**
- **Problem**: Workers can't reach queue/storage
- **Mitigation**:
  - Local caching of handoffs
  - Graceful degradation (work on cached tasks)
  - Reconciliation when partition heals

### 3.2 High Availability Configuration

**Supervisor Cluster:**
```python
from consul import Consul

class SupervisorCluster:
    """Supervisor cluster with leader election."""

    def __init__(self, consul_host, supervisor_id):
        self.consul = Consul(host=consul_host)
        self.supervisor_id = supervisor_id
        self.session_id = None
        self.is_leader = False

    def start(self):
        """Start supervisor and compete for leadership."""
        # Create session
        self.session_id = self.consul.session.create(
            name=f"supervisor-{self.supervisor_id}",
            ttl=30  # 30 second TTL
        )

        # Try to acquire leadership
        while True:
            self.try_acquire_leadership()

            if self.is_leader:
                self.run_as_leader()
            else:
                self.run_as_follower()

            time.sleep(10)

    def try_acquire_leadership(self):
        """Attempt to become leader."""
        acquired = self.consul.kv.put(
            "supervisor/leader",
            self.supervisor_id,
            acquire=self.session_id
        )

        self.is_leader = acquired

        # Renew session
        self.consul.session.renew(self.session_id)

    def run_as_leader(self):
        """Main supervisor loop (only leader executes)."""
        # Discover and schedule tasks
        new_tasks = self.discover_tasks()
        for task in new_tasks:
            self.schedule_task(task)

        # Monitor running tasks
        self.check_running_tasks()

    def run_as_follower(self):
        """Standby mode (ready to take over if leader fails)."""
        # Health check leader
        leader_id = self.consul.kv.get("supervisor/leader")[1]["Value"]

        if not leader_id:
            # Leader died, try to acquire
            self.try_acquire_leadership()
```

**Stateless Workers:**
```python
class StatelessWorker:
    """Worker that stores no local state."""

    def process_task(self, task_message):
        """Process task from queue."""

        try:
            # Download handoff from S3
            handoff = self.download_handoff(task_message["handoff_id"])

            # Execute task
            result = self.execute(handoff)

            # Upload result to S3
            self.upload_result(result)

            # Acknowledge message (remove from queue)
            self.queue.ack(task_message)

        except Exception as e:
            # Don't ack - message goes back to queue
            # After N failures, goes to dead letter queue
            self.log_error(e, task_message)
            raise
```

---

## 4. Observability in Production

### 4.1 Monitoring Stack

**Recommended Stack:**
- **Metrics**: Prometheus + Grafana
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana) or Loki
- **Traces**: Jaeger or Zipkin
- **Alerts**: Alertmanager or PagerDuty

**Key Dashboards:**
1. **Overview Dashboard**
   - Task throughput (tasks/min)
   - Success/failure rates
   - Current spend vs budget
   - Active workers

2. **Layer/Stage Dashboard**
   - Performance by layer and stage
   - Bottleneck identification
   - Cost per layer/stage

3. **Worker Health Dashboard**
   - Worker utilization
   - Queue depths
   - Error rates by worker

4. **Cost Dashboard**
   - Spend trends
   - Cost per model
   - Budget burn rate

### 4.2 Alerting Rules

```yaml
alerts:
  critical:
    - name: SupervisorDown
      condition: up{job="supervisor"} == 0
      duration: 5m
      action: page_oncall

    - name: HighTaskFailureRate
      condition: rate(tasks_failed[5m]) / rate(tasks_total[5m]) > 0.5
      duration: 10m
      action: page_oncall

    - name: BudgetExceeded
      condition: daily_spend > daily_budget * 1.1
      duration: 1m
      action: stop_new_tasks

  warning:
    - name: QueueBacklog
      condition: queue_depth > 1000
      duration: 15m
      action: notify_team

    - name: WorkerUtilizationLow
      condition: avg(worker_utilization) < 0.3
      duration: 30m
      action: scale_down_workers

    - name: ApiErrorRate
      condition: rate(api_errors[5m]) > 10
      duration: 10m
      action: activate_circuit_breaker
```

---

## 5. Deployment Checklist

### 5.1 Pre-Deployment

- [ ] Code review and approval
- [ ] All tests pass (unit, integration, E2E)
- [ ] Security scan (dependency vulnerabilities)
- [ ] Load testing completed
- [ ] Rollback plan documented
- [ ] On-call rotation scheduled
- [ ] Budget limits configured
- [ ] Monitoring dashboards ready
- [ ] Alerts configured

### 5.2 Deployment Steps

**Zero-Downtime Deployment:**
1. Deploy new supervisor version (blue-green)
2. Route 10% of traffic to new version
3. Monitor metrics for 15 minutes
4. If healthy, route 50% of traffic
5. Monitor for 15 minutes
6. If healthy, route 100% of traffic
7. Retire old version

**Rollback Criteria:**
- Task failure rate > 20%
- API error rate > 10%
- Response time p95 > 60 seconds
- Any critical alert triggered

### 5.3 Post-Deployment

- [ ] Verify all monitors are green
- [ ] Check logs for errors
- [ ] Validate task execution
- [ ] Monitor cost/usage
- [ ] Document any issues
- [ ] Update runbook if needed

---

## 6. Operational Best Practices

### 6.1 Runbook

**Common Operations:**

**Start Supervisor:**
```bash
# Kubernetes
kubectl apply -f k8s/supervisor.yaml

# Docker Compose
docker-compose up -d supervisor

# Systemd
sudo systemctl start ai-supervisor
```

**Scale Workers:**
```bash
# Kubernetes
kubectl scale deployment ai-worker --replicas=20

# ECS
aws ecs update-service --service ai-worker --desired-count 20
```

**Drain and Restart Worker:**
```bash
# Gracefully stop accepting new tasks
kubectl annotate pod <worker-pod> drain=true

# Wait for current tasks to finish
kubectl wait --for=condition=Ready=false pod/<worker-pod> --timeout=600s

# Delete pod (will be recreated)
kubectl delete pod <worker-pod>
```

**Emergency Budget Stop:**
```bash
# Stop all new task scheduling
kubectl set env deployment/supervisor EMERGENCY_STOP=true

# Drain queues
python scripts/drain_queues.py --reason "budget_exceeded"
```

### 6.2 Incident Response

**Severity Levels:**

**P0 (Critical):**
- Supervisor cluster down
- Data corruption
- Budget exceeded by >50%
- Action: Page on-call immediately

**P1 (High):**
- High task failure rate (>30%)
- Performance degradation
- Action: Notify team, investigate within 1 hour

**P2 (Medium):**
- Moderate failures (10-30%)
- Queue backlog growing
- Action: Investigate during business hours

**P3 (Low):**
- Individual task failures
- Minor performance issues
- Action: Log for review

---

## 7. Cost Optimization

### 7.1 Production Cost Strategies

**Spot/Preemptible Instances:**
```yaml
# Kubernetes node pool with spot instances
nodePool:
  name: ai-workers-spot
  instanceType: n1-standard-4
  preemptible: true
  minNodes: 2
  maxNodes: 50
  diskSizeGb: 100

  taints:
    - key: workload-type
      value: ai-worker
      effect: NoSchedule

tolerations:
  - key: workload-type
    operator: Equal
    value: ai-worker
    effect: NoSchedule
```

**Local Model Hosting:**
- Deploy Llama/Mistral on-premise for L3-L4 workers
- Use cloud APIs for L0-L2 managers only
- Potential 70-90% cost savings

**Smart Caching:**
- Cache model responses for identical handoffs
- Deduplicate similar tasks
- Reuse artifacts across tasks

---

## 8. Summary

Production deployment requires:

1. **Right Architecture**: Choose based on scale and requirements
2. **Scaling Strategy**: Auto-scale workers, maintain headroom
3. **High Availability**: Redundancy at every layer
4. **Comprehensive Monitoring**: Metrics, logs, traces, alerts
5. **Operational Discipline**: Runbooks, incident response, regular drills
6. **Cost Management**: Budgets, spot instances, local models

Start simple (single machine), evolve to distributed as scale demands.
