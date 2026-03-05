---
resource_id: "c53a9c92-9f5d-44a4-a6e5-97dbb55878ea"
resource_type: "index
document"
resource_name: "0INDEX"
---
# Proposals Index

<!-- section_id: "c87d64d2-350f-4064-85aa-d8034ce09f16" -->
## Structure

```
proposals/
├── active/           # Currently active proposals (production)
├── staging/
│   ├── stage_experimental/   # Testing on limited scope
│   │   └── stage_01-11/      # Full workflow per proposal
│   ├── stage_testing/        # Expanded scope testing
│   │   └── stage_01-11/
│   └── stage_rollout/        # Gradual production rollout
│       └── stage_01-11/
└── archived/         # Historical/superseded proposals
```

<!-- section_id: "1fa83536-f7df-4d7c-8338-3157aa74d5ce" -->
## Staging Workflow

```
Draft → Experimental (01-11) → Testing (01-11) → Rollout (01-11) → Active
```

Each proposal progresses through full 01-11 stages at each level before graduating.

---

<!-- section_id: "a8dc13c4-d91e-4a68-b231-9be32045a1ed" -->
## Active Proposals

| Proposal | Description | Since |
|----------|-------------|-------|
| [v6 AI-Friendly Output Organization](active/proposal_ai_friendly_output_organization_v6.md) | Main architecture with _group naming, .0agnostic, staged proposals | 2026-02-03 |

---

<!-- section_id: "f1d09361-e408-4be5-87ad-97e31ff3ad13" -->
## Staging

<!-- section_id: "64397808-9d4f-412b-aeb6-38ea425f42e0" -->
### Experimental (Limited Scope)

| Proposal | Stage | Description |
|----------|-------|-------------|
| [Cleanup & Staged Proposals v1](staging/stage_experimental/stage_02_research/proposal_cleanup_and_staged_proposals_v1.md) | 02_research | Cleanup _content→_group, relocate orphans, add staging |

<!-- section_id: "31f8eb79-d8fa-4d59-bdd7-fa9f061c7650" -->
### Testing (Expanded Scope)

_No proposals currently in testing_

<!-- section_id: "873a833d-ce8c-424b-91aa-7dcea66706e6" -->
### Rollout (Gradual Deployment)

_No proposals currently in rollout_

---

<!-- section_id: "8f5c9909-436f-4541-888e-a91c52fd775e" -->
## Archived

| Proposal | Superseded By | Date |
|----------|---------------|------|
| [v1](archived/proposal_ai_friendly_output_organization.md) | v2 | 2026-01 |
| [v2](archived/proposal_ai_friendly_output_organization_v2.md) | v3 | 2026-01 |
| [v3](archived/proposal_ai_friendly_output_organization_v3.md) | v4 | 2026-01 |
| [v4](archived/proposal_ai_friendly_output_organization_v4.md) | v5 | 2026-02 |
| [v5](archived/proposal_ai_friendly_output_organization_v5.md) | v6 | 2026-02 |

---

<!-- section_id: "ae206926-5e40-428a-9bf9-d5c9fd297799" -->
## Proposal Metadata Template

```yaml
---
proposal_id: <unique_id>
status: experimental | testing | rollout | active | archived
applies_to:
  layers: [-1, 0, 1]        # Which layers
  stages: [02, 03, 04]      # Which stages
  features: [feature_name]  # Which features (optional)
rollout_percentage: 10%     # For gradual rollouts
parent_proposal: <id>       # What it's based on
experiment_start: YYYY-MM-DD
experiment_end: YYYY-MM-DD
---
```

---

*Index for proposal staging and tracking*
