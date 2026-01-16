# Phase 6: Ops, Safety, and Deployment - Quick Reference

**Last Updated**: 2025-12-24
**Status**: Active
**Phase**: 6 of 7 (Integration of Ideal AI Manager Hierarchy System)

---

## What Was Added in Phase 6?

Phase 6 added **operational, safety, and deployment guidance** for the AI Manager Hierarchy System:

1. **Observability & Logging Protocol** - How to log, monitor, and trace AI work
2. **Safety, Permissions, and Governance Rules** - Security boundaries and approval gates
3. **AI Manager Hierarchy Deployment** - How to deploy the Agent OS to production

---

## Quick Links

### Observability & Logging

**Location**: `sub_layer_0.13_universal_protocols/observability/README.md`

**Use When**:
- Setting up logging for manager/worker systems
- Debugging multi-layer workflows
- Tracking costs and quality metrics
- Creating audit trails

**Key Topics**:
- Log levels and structured formats
- Where logs live in layer/stage structure
- Handoff logging (incoming/outgoing)
- Manager/worker observability
- Distributed tracing

### Safety, Permissions, and Governance

**Location**: `sub_layer_0.04_universal_rules/safety_governance.md`

**Use When**:
- Understanding what permissions each layer has
- Requesting human approval for sensitive operations
- Enforcing budget limits
- Implementing security boundaries

**Key Topics**:
- Permission levels by layer (L0=System Manager, L3=Sandboxed Write)
- Filesystem, network, command execution boundaries
- Human-in-the-loop approval gates
- Budget governance and resource quotas
- Escalation patterns

### AI Manager Hierarchy Deployment

**Location**: `sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`

**Use When**:
- Deploying supervisor and worker services
- Scaling from development to production
- Setting up distributed task queues
- Configuring monitoring and observability infrastructure

**Key Topics**:
- Deployment architectures (single-machine, distributed staging, production)
- Layer-to-service mapping (L0=Supervisor, L1-L3=Workers)
- Environment-specific configuration
- Scaling strategy and auto-scaling
- Reliability and fault tolerance

---

## How These Integrate

```
User Request
    ↓
Layer 0 Manager (follows safety rules, logs everything)
    ↓
Creates L0→L1 Handoff (logged with trace_id)
    ↓
Layer 1 Manager (budget check, permission check)
    ↓
Spawns Workers (logged, monitored)
    ↓
Workers Execute (within safety boundaries)
    ↓
Results Logged (cost, quality, duration)
    ↓
Deployed Services (supervisor, workers, queues)
```

**Observability**: Provides logging/metrics at every step
**Safety**: Enforces permissions and budget at every layer
**Deployment**: Maps logical layers to deployed services

---

## Common Use Cases

### "How do I log a handoff?"

See: `observability/README.md` → Section "Handoff Logging"

Example:
```json
{
  "event": "handoff.received",
  "handoff_id": "handoff-20251224-102030",
  "layer": 2,
  "from": {"layer": 1, "stage": "planning"},
  "task": "Implement login component"
}
```

### "What permissions does Layer 3 have?"

See: `safety_governance.md` → Section "Permission Levels by Layer" → "Layer 3"

Answer:
- **Allowed**: Create/modify files in `src/components/<component>/`
- **Requires Approval**: Any file outside component directory
- **Prohibited**: Network access, arbitrary commands, git push

### "How do I deploy to production?"

See: `deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md` → Section "Pattern 3: Production at Scale"

Steps:
1. Deploy supervisor cluster (3-5 replicas)
2. Set up task queue (RabbitMQ/Redis)
3. Deploy worker pool (auto-scaling)
4. Configure observability stack
5. Set up budget limits

### "When do I need human approval?"

See: `safety_governance.md` → Section "Human-in-the-Loop Approval Gates"

Always requires approval:
- Delete directory
- Modify security policy
- Change budget limits
- Git push to main/master/production
- Deploy to production
- Install unknown dependency

---

## For Managers

**Layer 0 Managers**:
- Read: All three documents
- Focus: System-wide observability, budget governance, production deployment

**Layer 1 Managers**:
- Read: Safety (permissions), Observability (project-level logging)
- Focus: Project budget, feature delegation, approval gates

**Layer 2 Managers**:
- Read: Safety (L2 permissions), Observability (feature logging)
- Focus: Component delegation, quality metrics

**Layer 3 Workers**:
- Read: Safety (L3 sandboxing), Observability (file operation logging)
- Focus: Stay within component boundaries, log all actions

---

## For Humans

**Developers**:
- Start with deployment guide → "Single-Machine Development"
- Learn observability basics (where logs are, how to read them)
- Understand safety boundaries (what agents can/can't do)

**DevOps/SRE**:
- Start with deployment guide → "Production at Scale"
- Set up monitoring stack (Prometheus, Grafana, ELK/Loki)
- Configure budget limits and alerts
- Implement approval workflows

**Security Teams**:
- Start with safety_governance.md
- Review permission model and approval gates
- Validate compliance requirements
- Configure audit logging

---

## Relationship to Ideal Hierarchy

All Phase 6 documents are **derived from** the normative ideal hierarchy specifications:

| Phase 6 Document | Normative Source |
|------------------|------------------|
| Observability Protocol | `.../-1_research/.../observability_and_logging.md` |
| Safety & Governance Rules | `.../-1_research/.../safety_and_governance.md` |
| Deployment Overview | `.../-1_research/.../production_deployment.md` |

When in doubt, **refer to the normative source** for authoritative details.

---

## Related Documentation

**Previous Phases**:
- Phase 1: Navigation and overview (MASTER_DOCUMENTATION_INDEX, SYSTEM_OVERVIEW, USAGE_GUIDE)
- Phase 2: Framework alignment (0.01_layer_stage_framework)
- Phase 3: Manager/worker standardization (handoff_schema.md, layer READMEs)
- Phase 4: OS/tool variants (os/<os-id>/ directories)
- Phase 5: Orchestration and CLI recursion (cli_recursion, framework_orchestration)

**Complementary Docs**:
- Handoff Schema: `layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- Git Commit Rule: `sub_layer_0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- Layer Context Header: `sub_layer_0.04_universal_rules/LAYER_CONTEXT_HEADER_PROTOCOL.md`

---

## Next Phase

**Phase 7**: Rollout and Migration Strategy

Will define how to:
- Test these new docs with a pilot project
- Iterate based on real usage
- Roll out across all projects and features
- Measure success and adapt

---

## Questions?

- **Can't find something?**: Check `MASTER_DOCUMENTATION_INDEX.md` or `SYSTEM_OVERVIEW.md`
- **Need more detail?**: Refer to the normative specs in `-1_research/.../ideal_ai_manager_hierarchy_system/`
- **Found an issue?**: Document it and update the relevant README

---

**Status**: Phase 6 is COMPLETE ✅
