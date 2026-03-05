---
resource_id: "2433c06d-d579-468a-85fe-9896208a9e08"
resource_type: "document"
resource_name: "AI_MANAGER_HIERARCHY_DEPLOYMENT"
---
# AI Manager Hierarchy System - Deployment Overview

**Document Type**: Deployment Guide
**Scope**: All Deployment Environments (Development, Staging, Production)
**Related**: `DEPLOYMENT_GUIDE.md` (application-specific deployment)

---

<!-- section_id: "efe2febc-40b5-4cff-8442-6d32261d4bf1" -->
## Purpose

This document provides deployment guidance specific to the **AI Manager Hierarchy System** (Agent OS). It clarifies how the layer/stage architecture maps to deployed services, background workers, and infrastructure components.

<!-- section_id: "d05b3465-3843-4252-b41a-c6ed7e0e66ae" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/production_deployment.md`
- **Status**: Normative (refer to source for authoritative details)

For application-specific deployment (Flask, Node.js, etc.), see:
- **Application Deployment**: `../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "e16f8223-df3d-45fc-a0c8-959d3591652b" -->
## Quick Reference

<!-- section_id: "940653f7-8841-4f7a-a996-4b9966d3e1eb" -->
### Deployment Patterns by Environment

| Environment | Architecture | Layers | Workers | Cost |
|------------|--------------|--------|---------|------|
| Development | Single-machine | L0-L3 | Local processes | $0-10/day |
| Staging | Distributed (small) | L0-L3 | 2-5 workers | $10-50/day |
| Production | Distributed (scaled) | L0-L4+ | 10-50+ workers | $50-500+/day |

<!-- section_id: "6d7e86a9-9659-4b24-b148-1f86fe5f84d4" -->
### Component Mapping

```
AI Manager Hierarchy → Deployment Services

Layer 0 Manager → Supervisor Service (1-3 replicas)
Layer 1 Managers → Queue + Workers (project-level)
Layer 2 Managers → Queue + Workers (feature-level)
Layer 3 Workers → Worker Pool (component-level)
Handoffs → S3/GCS/Filesystem Storage
Logs → Centralized Logging (ELK/Loki)
Metrics → Prometheus + Grafana
```

---

<!-- section_id: "5cc2432e-ed70-4df9-b63f-73e8eccfe7f1" -->
## Deployment Architectures

<!-- section_id: "fd7f384b-a004-422b-9741-aa64005e04cc" -->
### Pattern 1: Single-Machine Development

**Best For**: Local development, testing, small personal projects

**Architecture**:
```
┌─────────────────────────────────────┐
│  Developer Machine / WSL            │
│  ┌───────────────────────────────┐  │
│  │  Supervisor (Python Process)  │  │
│  └───────────┬───────────────────┘  │
│              │                       │
│  ┌───────────▼───────────────────┐  │
│  │  File-based Task Queue        │  │
│  │  (<workspace>/queues/)        │  │
│  └───────────┬───────────────────┘  │
│              │                       │
│  ┌───────────▼───────────────────┐  │
│  │  Worker Processes (2-4)       │  │
│  │  - codex (subprocess)         │  │
│  │  - gemini (API calls)         │  │
│  │  - claude (API calls)         │  │
│  └───────────────────────────────┘  │
│                                     │
│  Storage: Local Filesystem          │
│  Database: SQLite                   │
│  Logs: Local files                  │
└─────────────────────────────────────┘
```

**Characteristics**:
- Supervisor runs as local Python process
- Workers spawn as subprocesses or API calls
- Handoffs stored in `<workspace>/layer_N/N.01_manager_handoff_documents/`
- Task state in SQLite database
- Logs in `<workspace>/logs/`

**Deployment Steps**:
```bash
# 1. Install dependencies
cd <workspace>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Configure environment
cp .env.example .env
# Edit .env with API keys and budget limits

# 3. Start supervisor
python supervisor/main.py --mode=development

# 4. Monitor logs
tail -f logs/supervisor.log
```

**Pros**:
- Simple setup, easy debugging
- No infrastructure costs
- Fast iteration

**Cons**:
- No horizontal scaling
- Single point of failure
- Limited throughput

---

<!-- section_id: "bd97bcf8-b2d6-4fb9-a83a-2d024fe9892a" -->
### Pattern 2: Distributed Staging

**Best For**: Testing production deployment patterns, team collaboration

**Architecture**:
```
┌─────────────────────────────────────────────┐
│  Load Balancer (nginx/HAProxy)             │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  Supervisor Cluster (2-3 replicas)          │
│  - Leader election (Consul/etcd)            │
│  - Shared state (PostgreSQL)                │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  Task Queue (Redis/RabbitMQ)                │
│  - Priority queues per layer                │
│  - Dead letter queue for failures           │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  Worker Pool (5-10 workers)                 │
│  - Kubernetes pods / Docker containers      │
│  - Auto-scale on queue depth                │
└─────────────┬───────────────────────────────┘
              │
┌─────────────▼───────────────────────────────┐
│  Shared Storage (S3/GCS)                    │
│  - Handoff documents                        │
│  - Code artifacts                           │
│  - Logs (centralized)                       │
└─────────────────────────────────────────────┘
```

**Characteristics**:
- Multiple supervisor replicas with leader election
- Centralized task queue (Redis/RabbitMQ)
- Worker pool scales based on queue depth
- Handoffs stored in cloud storage (S3/GCS)
- Centralized logging (ELK stack, Loki)
- Metrics collection (Prometheus)

**Deployment Steps**:
```bash
# 1. Deploy infrastructure (Terraform/CloudFormation)
cd infrastructure/staging
terraform init
terraform apply

# 2. Deploy supervisor cluster
kubectl apply -f k8s/supervisor-deployment.yaml

# 3. Deploy worker pool
kubectl apply -f k8s/worker-deployment.yaml

# 4. Configure monitoring
kubectl apply -f k8s/monitoring/

# 5. Verify deployment
kubectl get pods -n ai-manager
curl https://staging.example.com/health
```

**Pros**:
- High availability
- Horizontal scaling
- Mirrors production architecture

**Cons**:
- More complex setup
- Higher costs
- Requires infrastructure expertise

---

<!-- section_id: "397ad280-ed43-44df-805b-e66949cbc029" -->
### Pattern 3: Production at Scale

**Best For**: Production workloads, high-volume processing, enterprise deployments

**Architecture**: See normative specification Section 1.2 for full distributed production architecture diagram.

**Key Components**:

1. **Supervisor Cluster** (3-5 replicas)
   - Leader election via Consul/etcd
   - Shared state in PostgreSQL
   - Health checks and auto-restart
   - Geographic distribution

2. **Task Queue** (Redis Cluster or RabbitMQ)
   - Priority queues per layer (L0 highest priority)
   - Dead letter queues for failed tasks
   - Message persistence
   - At-least-once delivery guarantees

3. **Worker Pool** (10-100+ workers)
   - Kubernetes HPA or ECS auto-scaling
   - Spot/preemptible instances for cost savings
   - Stateless design (no local state)
   - Graceful shutdown on scale-down

4. **Storage** (S3/GCS/Azure Blob)
   - Handoff documents
   - Code artifacts
   - Logs (hot tier)
   - Metrics (time-series database)

5. **Observability Stack**
   - Metrics: Prometheus + Grafana
   - Logs: ELK Stack (Elasticsearch, Logstash, Kibana) or Loki
   - Traces: Jaeger or Zipkin
   - Alerts: Alertmanager + PagerDuty

**Deployment Steps**: See normative specification Section 5 for complete checklist and blue-green deployment procedure.

---

<!-- section_id: "64679a12-1e8d-4610-ac75-ee91d6649d1d" -->
## Layer-to-Service Mapping

<!-- section_id: "9bc4f1c8-8407-4fba-9d0c-33b6e4da059c" -->
### How Layers Map to Deployed Services

```yaml
Layer 0 (Universal Manager):
  service: supervisor-main
  replicas: 3
  role: Orchestrate all L1 managers
  responsibilities:
    - Discover new user requests
    - Create L0 → L1 handoffs
    - Monitor all downstream tasks
    - Enforce budget limits
    - Generate reports

Layer 1 (Project Manager):
  service: manager-worker-L1
  replicas: 2-5
  role: Project-level planning and coordination
  responsibilities:
    - Read L0 → L1 handoffs
    - Create project plans
    - Spawn L2 feature managers
    - Aggregate feature results

Layer 2 (Feature Manager):
  service: manager-worker-L2
  replicas: 5-20
  role: Feature implementation
  responsibilities:
    - Read L1 → L2 handoffs
    - Implement features
    - Spawn L3 component workers
    - Aggregate component results

Layer 3 (Component Worker):
  service: worker-pool-L3
  replicas: 10-50
  role: Component implementation
  responsibilities:
    - Read L2 → L3 handoffs
    - Implement components
    - Run tests
    - Report results

Layer 4+ (Sub-component Worker):
  service: worker-pool-L4
  replicas: 5-20
  role: Fine-grained implementation
  responsibilities:
    - Implement sub-components
    - Unit-level testing
```

<!-- section_id: "ef7f106e-5a7a-4aec-b191-481bb9030466" -->
### Service Communication

```
Supervisor (L0) → Task Queue → Manager Workers (L1)
                            → Manager Workers (L2)
                            → Component Workers (L3)
                            → Sub-component Workers (L4)

All services read/write:
  - Handoff storage (S3/GCS)
  - Shared database (PostgreSQL)
  - Metrics (Prometheus)
  - Logs (centralized logging)
```

---

<!-- section_id: "493c490a-c110-451e-b649-b90f8ce6c70e" -->
## Environment-Specific Configuration

<!-- section_id: "c3d4df0b-3545-4718-b1b3-599d8f3a84b1" -->
### Development Environment

**Configuration** (`config/development.yaml`):
```yaml
environment: development

supervisor:
  mode: single_machine
  workers: 4
  poll_interval: 10  # seconds

storage:
  type: filesystem
  handoffs_dir: ./handoffs
  artifacts_dir: ./artifacts

database:
  type: sqlite
  path: ./data/tasks.db

logging:
  level: DEBUG
  output: file
  path: ./logs/supervisor.log

budget:
  daily_limit: 10.00
  enforce: false  # Warnings only
```

**Tools**:
- Local AI tool binaries (codex, claude-code)
- API calls to cloud services (OpenAI, Anthropic, Google)

<!-- section_id: "91467891-7758-44f6-869c-fb83325cd2cb" -->
### Staging Environment

**Configuration** (`config/staging.yaml`):
```yaml
environment: staging

supervisor:
  mode: distributed
  replicas: 2
  leader_election:
    backend: consul
    endpoint: consul.staging.internal

storage:
  type: s3
  bucket: ai-manager-staging
  region: us-east-1

database:
  type: postgresql
  host: postgres.staging.internal
  database: ai_manager_staging

queue:
  type: redis
  endpoint: redis.staging.internal

logging:
  level: INFO
  output: elasticsearch
  endpoint: elasticsearch.staging.internal

monitoring:
  prometheus: prometheus.staging.internal
  grafana: grafana.staging.internal

budget:
  daily_limit: 50.00
  enforce: true
  alert_threshold: 0.8
```

<!-- section_id: "25063e93-2e9a-4afd-a954-e95980bc39e6" -->
### Production Environment

**Configuration** (`config/production.yaml`):
```yaml
environment: production

supervisor:
  mode: distributed
  replicas: 5
  leader_election:
    backend: consul
    endpoint: consul.prod.internal
  high_availability: true

storage:
  type: s3
  bucket: ai-manager-production
  region: us-east-1
  encryption: AES256

database:
  type: postgresql
  host: postgres-primary.prod.internal
  read_replicas:
    - postgres-replica-1.prod.internal
    - postgres-replica-2.prod.internal
  database: ai_manager_production
  ssl_mode: require

queue:
  type: rabbitmq
  cluster:
    - rabbitmq-1.prod.internal
    - rabbitmq-2.prod.internal
    - rabbitmq-3.prod.internal
  vhost: /ai-manager

logging:
  level: WARNING
  output: elasticsearch
  endpoint: elasticsearch.prod.internal
  retention_days: 90

monitoring:
  prometheus: prometheus.prod.internal
  grafana: grafana.prod.internal
  alertmanager: alertmanager.prod.internal
  pagerduty_key: ${PAGERDUTY_KEY}

budget:
  daily_limit: 500.00
  enforce: true
  alert_threshold: 0.9
  emergency_stop_threshold: 1.1

security:
  tls_enabled: true
  api_auth_required: true
  audit_all_actions: true
```

---

<!-- section_id: "d8e60fb1-c22a-48c0-a364-d5ae323531ef" -->
## Scaling Strategy

<!-- section_id: "3cfb77cd-e3b2-4c3f-8e9f-a744fd767dd1" -->
### Vertical Scaling (Per-Service)

**Supervisor**:
- Start: 1 replica (dev)
- Staging: 2-3 replicas
- Production: 3-5 replicas
- Scale trigger: Leadership failover, high load

**Workers**:
- Start: 2-4 local processes (dev)
- Staging: 5-10 containers
- Production: 10-100+ containers
- Scale trigger: Queue depth, task backlog

<!-- section_id: "431cb85f-8939-459c-9e6d-e689e9a261de" -->
### Horizontal Scaling (Auto-Scaling)

**Kubernetes HPA Example**:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: worker-pool-L3
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-worker-L3
  minReplicas: 10
  maxReplicas: 50
  metrics:
    - type: External
      external:
        metric:
          name: queue_depth_L3
        target:
          type: AverageValue
          averageValue: "10"  # 10 tasks per worker

    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70

  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # Wait 5min
      policies:
        - type: Percent
          value: 50
          periodSeconds: 60

    scaleUp:
      stabilizationWindowSeconds: 0  # Immediate
      policies:
        - type: Pods
          value: 4
          periodSeconds: 60
```

<!-- section_id: "785dd55a-083b-4328-b053-e31431ae685b" -->
### Cost-Based Scaling

- **Peak Hours**: Scale up workers (9am-5pm)
- **Off-Peak**: Scale down to minimum (5pm-9am)
- **Budget Limits**: Throttle or stop when approaching budget
- **Spot Instances**: Use for L3/L4 workers (70-90% cost savings)

---

<!-- section_id: "65e95a1b-1763-4aad-b7dc-6b3e97f0f173" -->
## Deployment Pipeline

<!-- section_id: "1accfe33-7f6e-4383-b778-5fa0bafaad52" -->
### Development → Staging → Production

```mermaid
graph LR
    A[Local Development] --> B{Tests Pass?}
    B -->|Yes| C[Deploy to Staging]
    B -->|No| A
    C --> D{Staging Tests Pass?}
    D -->|Yes| E[Manual Approval]
    D -->|No| A
    E --> F[Deploy to Production]
    F --> G{Production Health?}
    G -->|Healthy| H[Complete]
    G -->|Unhealthy| I[Rollback]
    I --> A
```

<!-- section_id: "f9fe9886-8001-45d6-a96c-0b9cc36cd49f" -->
### Deployment Steps

**1. Pre-Deployment Checklist**:
- [ ] All tests pass (unit, integration, E2E)
- [ ] Security scan completed
- [ ] Load testing completed
- [ ] Rollback plan documented
- [ ] Budget limits configured
- [ ] Monitoring dashboards ready
- [ ] On-call rotation scheduled

**2. Deployment** (Blue-Green):
```bash
# Deploy new version (green)
kubectl apply -f k8s/supervisor-v2.yaml

# Route 10% traffic to new version
kubectl patch service supervisor -p '{"spec":{"selector":{"version":"v2","weight":"10"}}}'

# Monitor for 15 minutes
watch kubectl get pods -l version=v2

# If healthy, route 50% traffic
kubectl patch service supervisor -p '{"spec":{"selector":{"weight":"50"}}}'

# Monitor for 15 minutes

# If healthy, route 100% traffic
kubectl patch service supervisor -p '{"spec":{"selector":{"version":"v2"}}}'

# Retire old version
kubectl delete deployment supervisor-v1
```

**3. Rollback Criteria**:
- Task failure rate > 20%
- API error rate > 10%
- Response time p95 > 60 seconds
- Any critical alert triggered

**4. Post-Deployment**:
- [ ] Verify monitors are green
- [ ] Check logs for errors
- [ ] Validate task execution
- [ ] Monitor cost/usage
- [ ] Document issues
- [ ] Update runbook

---

<!-- section_id: "68a81b2f-ef71-467d-9998-c3c3d6d6afeb" -->
## Reliability and Fault Tolerance

<!-- section_id: "59661acc-5e4a-4043-ad4c-de221e81af73" -->
### Failure Modes and Mitigations

| Failure | Impact | Mitigation |
|---------|--------|------------|
| Supervisor crash | Tasks orphaned | Multiple replicas + leader election |
| Worker crash | Task fails | Timeouts + retries + dead letter queue |
| Model API down | Can't execute | Fallback models + circuit breakers |
| Network partition | Workers isolated | Local caching + reconciliation |
| Database failure | State loss | Read replicas + backups |
| Queue failure | Tasks lost | Message persistence + replication |

<!-- section_id: "81bc570d-bd5f-4cc7-8195-e27169450e1f" -->
### High Availability Configuration

**Supervisor Cluster**: See normative specification Section 3.2 for leader election implementation.

**Stateless Workers**: All workers MUST be stateless:
- No local state storage
- Download handoffs from S3/GCS
- Upload results to S3/GCS
- Acknowledge queue messages only after success

---

<!-- section_id: "2603ebd9-9372-49fc-ae6a-382e23da02b9" -->
## Monitoring and Observability

<!-- section_id: "da1e76f1-3adf-4686-8b92-50229d5443df" -->
### Key Metrics

**System Health**:
- Supervisor uptime and leader status
- Worker pool size and utilization
- Queue depth per layer
- Task throughput (tasks/hour)

**Performance**:
- Task duration (p50, p95, p99) per layer
- End-to-end latency (L0 → L3)
- API response times

**Cost**:
- Daily spend vs budget
- Cost per task per layer
- Cost per line of code
- Budget burn rate

**Quality**:
- Task success rate per layer
- Test pass rate
- Code quality scores
- Human review approval rate

<!-- section_id: "1166b4bf-816d-426b-9811-8a72312afff0" -->
### Dashboards

See observability documentation for dashboard specifications:
- **Reference**: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/`

<!-- section_id: "803cfe8e-a778-4bff-9f42-8605b26bcaea" -->
### Alerts

**Critical**:
- Supervisor cluster down
- Daily budget exceeded by >10%
- Task failure rate > 50%

**Warning**:
- Queue backlog growing
- Worker utilization low
- Budget at 80%

---

<!-- section_id: "581b85a1-15c0-42bb-8dd5-d2529988e0b3" -->
## Cost Optimization

<!-- section_id: "03c1c799-411e-4d11-b24c-aefefd76dfdd" -->
### Production Cost Strategies

1. **Spot/Preemptible Instances** for L3/L4 workers (70-90% savings)
2. **Local Model Hosting** for L3/L4 (Llama, Mistral on-premise)
3. **Smart Caching** of model responses
4. **Task Deduplication** (avoid redundant work)
5. **Off-Peak Scaling** (reduce workers during low-demand periods)

<!-- section_id: "e63b677f-d2f1-4790-9c47-8ac6a72b6649" -->
### Budget Management

See safety/governance documentation:
- **Reference**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

---

<!-- section_id: "d6fe8623-f5b5-464c-b9af-803f0c495473" -->
## Security Considerations

<!-- section_id: "18162b76-bc06-47d5-94bf-f307ebcde872" -->
### Deployment Security

- **Network Isolation**: Workers in private subnets
- **TLS Everywhere**: All service-to-service communication encrypted
- **Secrets Management**: Use HashiCorp Vault or AWS Secrets Manager
- **API Authentication**: JWT tokens for service authentication
- **Audit Logging**: All actions logged to immutable audit trail

<!-- section_id: "c8dd4178-4d8b-44d2-8ca6-bb4ea9374341" -->
### Compliance

See safety/governance documentation for compliance requirements:
- **Reference**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

---

<!-- section_id: "5bd49c3f-dc26-45cf-b30c-e038bb466d41" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/production_deployment.md`
- **Application Deployment**: `../DEPLOYMENT_GUIDE.md` (Flask, Node.js, etc.)
- **Observability**: `../../sub_layer_0_13_universal_protocols/observability/`
- **Safety & Governance**: `../../sub_layer_0_04_universal_rules/safety_governance.md`

---

<!-- section_id: "f6e867a4-2106-4936-a2f3-8d78c10a22a3" -->
## Quick Start Commands

<!-- section_id: "42fe1234-fd96-4ca3-abe5-36028514df37" -->
### Start Development Environment

```bash
# Single-machine development
cd <workspace>
source .venv/bin/activate
python supervisor/main.py --config config/development.yaml
```

<!-- section_id: "49a88186-5c0e-4cf9-ab47-19576220ffe7" -->
### Deploy to Staging

```bash
# Deploy full stack to Kubernetes
kubectl apply -f k8s/staging/

# Verify deployment
kubectl get pods -n ai-manager-staging
```

<!-- section_id: "f42c3413-fe48-4006-a20d-3f38e8589594" -->
### Deploy to Production

```bash
# Review deployment plan
terraform plan -var-file=production.tfvars

# Apply infrastructure changes
terraform apply -var-file=production.tfvars

# Deploy application
kubectl apply -f k8s/production/

# Verify health
curl https://api.example.com/health
```

---

**Last Updated**: 2025-12-24
**Version**: 1.0.0
**Status**: Active
