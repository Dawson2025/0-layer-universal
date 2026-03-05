---
resource_id: "0a656dea-b995-4f32-bfed-1a4404c3b88a"
resource_type: "document"
resource_name: "AI_MANAGER_HIERARCHY_DEPLOYMENT"
---
# AI Manager Hierarchy System - Deployment Overview

**Document Type**: Deployment Guide
**Scope**: All Deployment Environments (Development, Staging, Production)
**Related**: `DEPLOYMENT_GUIDE.md` (application-specific deployment)

---

<!-- section_id: "db7f487e-1d1a-4107-ac09-bd294d8e7529" -->
## Purpose

This document provides deployment guidance specific to the **AI Manager Hierarchy System** (Agent OS). It clarifies how the layer/stage architecture maps to deployed services, background workers, and infrastructure components.

<!-- section_id: "acde2740-d27e-42f3-a420-20bd8de35433" -->
## Normative Specification

This document is a **derived implementation guide** from the canonical specification:

- **Source**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/production_deployment.md`
- **Status**: Normative (refer to source for authoritative details)

For application-specific deployment (Flask, Node.js, etc.), see:
- **Application Deployment**: `../DEPLOYMENT_GUIDE.md`

---

<!-- section_id: "f6b4406d-a522-4993-8ac7-9bf1ec8886c6" -->
## Quick Reference

<!-- section_id: "e32bede3-a53a-479f-8890-a09024f0d325" -->
### Deployment Patterns by Environment

| Environment | Architecture | Layers | Workers | Cost |
|------------|--------------|--------|---------|------|
| Development | Single-machine | L0-L3 | Local processes | $0-10/day |
| Staging | Distributed (small) | L0-L3 | 2-5 workers | $10-50/day |
| Production | Distributed (scaled) | L0-L4+ | 10-50+ workers | $50-500+/day |

<!-- section_id: "196ef733-28fa-4636-ad9a-48de8efdec95" -->
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

<!-- section_id: "5f178fbe-fe50-40aa-a6bd-a4feb213fd33" -->
## Deployment Architectures

<!-- section_id: "4aef3729-a521-4978-b6e4-b633003da37d" -->
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

<!-- section_id: "3b1b329d-cf66-4036-8fe0-30056efb520b" -->
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

<!-- section_id: "8371fdc0-5dac-4d02-b90d-5e834aed3c87" -->
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

<!-- section_id: "c4bdfcbd-5aed-4afb-9f2a-43c103a3f83f" -->
## Layer-to-Service Mapping

<!-- section_id: "8c0e11ee-497c-43a1-8e54-f95ef3515381" -->
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

<!-- section_id: "211af16c-1123-4e83-8dfc-d02eab137cc6" -->
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

<!-- section_id: "73baeccc-9d2e-431a-8ae7-97b7bf910dac" -->
## Environment-Specific Configuration

<!-- section_id: "754eb62a-401a-4499-a424-da2bb6d8b8c7" -->
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

<!-- section_id: "ce14143b-279b-4a93-b91c-fe3b3c2ece01" -->
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

<!-- section_id: "57d99001-f960-4ceb-ab2b-b7f491ef0544" -->
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

<!-- section_id: "9905afc8-53e1-48ca-84be-2be8b2b7f238" -->
## Scaling Strategy

<!-- section_id: "1ead69e8-e848-4e00-ad9c-934e4f467d9e" -->
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

<!-- section_id: "3fc7fb7f-4190-4f1c-b03b-c65f2bcb8a3a" -->
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

<!-- section_id: "6a030393-dad3-43b7-bffc-6a45e5594b8b" -->
### Cost-Based Scaling

- **Peak Hours**: Scale up workers (9am-5pm)
- **Off-Peak**: Scale down to minimum (5pm-9am)
- **Budget Limits**: Throttle or stop when approaching budget
- **Spot Instances**: Use for L3/L4 workers (70-90% cost savings)

---

<!-- section_id: "31a4346a-10ce-4cb4-b7dc-ffbb468bc91b" -->
## Deployment Pipeline

<!-- section_id: "c98c7019-5b2b-4609-a155-213649268ad2" -->
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

<!-- section_id: "feb6e932-d79f-482c-9651-ecc845386300" -->
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

<!-- section_id: "bbb17601-ee25-4e10-8e12-51f0f7ee4c2f" -->
## Reliability and Fault Tolerance

<!-- section_id: "ced46383-e0d2-4037-93a1-bb82861309c6" -->
### Failure Modes and Mitigations

| Failure | Impact | Mitigation |
|---------|--------|------------|
| Supervisor crash | Tasks orphaned | Multiple replicas + leader election |
| Worker crash | Task fails | Timeouts + retries + dead letter queue |
| Model API down | Can't execute | Fallback models + circuit breakers |
| Network partition | Workers isolated | Local caching + reconciliation |
| Database failure | State loss | Read replicas + backups |
| Queue failure | Tasks lost | Message persistence + replication |

<!-- section_id: "5f9d87aa-ee18-432c-9fd4-5a7bfc39a5c2" -->
### High Availability Configuration

**Supervisor Cluster**: See normative specification Section 3.2 for leader election implementation.

**Stateless Workers**: All workers MUST be stateless:
- No local state storage
- Download handoffs from S3/GCS
- Upload results to S3/GCS
- Acknowledge queue messages only after success

---

<!-- section_id: "2a747f85-7627-4caf-bead-63e2657827e1" -->
## Monitoring and Observability

<!-- section_id: "b7810472-ab09-42ff-88bd-4a811374a905" -->
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

<!-- section_id: "7d255c68-0162-4df4-8ed6-f1ca6914ba8b" -->
### Dashboards

See observability documentation for dashboard specifications:
- **Reference**: `layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/`

<!-- section_id: "faa5fb2d-1b86-4aad-9ee1-f2af25bdaf3b" -->
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

<!-- section_id: "c52a93db-52e5-4df5-8daa-01a7aa5e72ec" -->
## Cost Optimization

<!-- section_id: "10ddeae0-94ae-4e2b-9969-48697d23e203" -->
### Production Cost Strategies

1. **Spot/Preemptible Instances** for L3/L4 workers (70-90% savings)
2. **Local Model Hosting** for L3/L4 (Llama, Mistral on-premise)
3. **Smart Caching** of model responses
4. **Task Deduplication** (avoid redundant work)
5. **Off-Peak Scaling** (reduce workers during low-demand periods)

<!-- section_id: "70f6ed74-105d-403c-a487-a9084b6a9135" -->
### Budget Management

See safety/governance documentation:
- **Reference**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

---

<!-- section_id: "0a5593e1-de63-4a3e-8098-09210c4ac16a" -->
## Security Considerations

<!-- section_id: "936d8bc7-2dc1-4e9a-a05d-95c121170e9c" -->
### Deployment Security

- **Network Isolation**: Workers in private subnets
- **TLS Everywhere**: All service-to-service communication encrypted
- **Secrets Management**: Use HashiCorp Vault or AWS Secrets Manager
- **API Authentication**: JWT tokens for service authentication
- **Audit Logging**: All actions logged to immutable audit trail

<!-- section_id: "fcd37e81-c430-421e-924d-3948821cdd93" -->
### Compliance

See safety/governance documentation for compliance requirements:
- **Reference**: `layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`

---

<!-- section_id: "9f605077-ed45-4884-bccc-136ea55b51b7" -->
## References

- **Normative Spec**: `.../-1_research/.../ideal_ai_manager_hierarchy_system/production_deployment.md`
- **Application Deployment**: `../DEPLOYMENT_GUIDE.md` (Flask, Node.js, etc.)
- **Observability**: `../../sub_layer_0_13_universal_protocols/observability/`
- **Safety & Governance**: `../../sub_layer_0_04_universal_rules/safety_governance.md`

---

<!-- section_id: "5cc4d167-04e0-4d43-b271-50d63fcf34aa" -->
## Quick Start Commands

<!-- section_id: "e0452e4a-69c4-4b4d-ad1a-689fecfa6801" -->
### Start Development Environment

```bash
# Single-machine development
cd <workspace>
source .venv/bin/activate
python supervisor/main.py --config config/development.yaml
```

<!-- section_id: "1322dd75-b5cf-4b62-8e28-7d3b411ea086" -->
### Deploy to Staging

```bash
# Deploy full stack to Kubernetes
kubectl apply -f k8s/staging/

# Verify deployment
kubectl get pods -n ai-manager-staging
```

<!-- section_id: "91854494-714b-4e08-b101-18cb6b2a4216" -->
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
