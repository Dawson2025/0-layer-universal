---
resource_id: "28fba7c2-92c8-4d34-9768-05c2e25ef31e"
resource_type: "protocol"
resource_name: "agent_delegation_update_protocol"
---
# Agent Delegation Update Protocol

When you need to change agent delegation patterns (Principle 8, Scope Boundary Rule, stage guides, delegation principles, etc.), follow this protocol.

## Step 1: Traverse to ADS

Recognize this is delegation-related work. It is out-of-scope for most entities.

**Path**: `layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/`

Read the entity's `0AGNOSTIC.md` to orient yourself.

## Step 2: Identify the Appropriate Stage

| Type of Work | Stage | Output Location |
|--------------|-------|-----------------|
| New requirement or gap identified | 01 request_gathering | `outputs/requests/tree_of_needs/` |
| Investigating how delegation should work | 02 research | `outputs/by_topic/` |
| Designing new patterns or rules | 04 design | `outputs/design_decisions/` |
| Implementing universal artifacts | 06 development | Root `.0agnostic/` (universal) |
| Testing delegation in working examples | 07 testing | `outputs/test_results/` |

Navigate to the stage directory and read its `0AGNOSTIC.md` for methodology and current state.

## Step 3: Produce Stage Outputs

Work in the stage's `outputs/` directory:
- **Research** -> `outputs/by_topic/{topic_name}/README.md`
- **Design** -> `outputs/design_decisions/{decision_name}.md`
- **Development** -> Produce universal artifacts at root `.0agnostic/` (stage guides, principles, rules, protocols)

Follow the stage's methodology as defined in its 0AGNOSTIC.md.

## Step 4: Update Stage Context

Update the stage's:
1. `0AGNOSTIC.md` Current Status section (the pointer-tier summary)
2. Stage report at `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`

## Step 5: Propagate Through Consolidation Funnel

The consolidation funnel ensures changes flow from stage outputs to the entity's source of truth:

```
Stage outputs (in outputs/)
    -> Stage report (.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md)
    -> Entity stages_report (.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stages_report.md)
    -> Entity layer_report (.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md)
    -> Entity 0AGNOSTIC.md (Current Status section)
```

Update each level to reflect the new work. The entity 0AGNOSTIC.md is the MOST consolidated document (comes LAST in the funnel, not first).

## Step 6: Update Universal Artifacts (if Development)

If you produced changes in stage 06 (development) that modify universal artifacts, those artifacts live at root `.0agnostic/`:

| Artifact | Location |
|----------|----------|
| Stage guides | `01_knowledge/layer_stage_system/stage_guides/` |
| Delegation principles | `01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Static rules | `02_rules/static/` |
| Dynamic rules | `02_rules/dynamic/` |
| Stage report protocol | `03_protocols/stage_report_protocol.md` |

After modifying root `.0agnostic/` content, run `agnostic-sync.sh` and commit with `[AI Context]` prefix.

## Step 7: Commit and Push

Commit all changes with the `[AI Context]` prefix:
```bash
git add [specific files]
git commit -m "[AI Context] description of delegation change"
git push
```

## When to Skip This Protocol

- **Trivial fixes** (typos, formatting) in universal artifacts can be made directly at root `.0agnostic/` without full stage work
- **Using delegation patterns** (applying Principle 8, following stage guides) does NOT require updating them here
- Only changes to the **patterns themselves** (new principles, modified rules, changed stage guides) need this protocol
