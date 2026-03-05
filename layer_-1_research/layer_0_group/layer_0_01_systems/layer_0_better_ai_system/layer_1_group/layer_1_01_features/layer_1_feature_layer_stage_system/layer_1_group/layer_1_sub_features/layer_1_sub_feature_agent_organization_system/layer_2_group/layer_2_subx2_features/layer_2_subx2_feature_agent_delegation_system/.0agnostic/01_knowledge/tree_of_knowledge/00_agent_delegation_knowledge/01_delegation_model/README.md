---
resource_id: "7c5a1a18-a4c4-467c-8972-95033e26df44"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Branch 01: Delegation Model

**Question**: How do managers delegate to stage agents?

This branch covers the core delegation model — the foundation of how AI agents work across the layer-stage hierarchy. It addresses the mechanics of delegation, communication channels, and what each agent type needs to know.

## Topics

| Topic | Summary | Primary Sources |
|-------|---------|----------------|
| `stage_delegation.md` | How managers delegate work to stage-specialized agents | Stage 04 design decisions, Stage 06 stage guides |
| `stage_reports.md` | The async communication channel between agents and managers | Stage 04 design, Universal protocol |
| `agent_context_model.md` | What each agent type knows in static vs dynamic context | Stage 01 requirements, Stage 04 design |

## Key Insight

Delegation is an **information design problem**. When information boundaries are clear (what the manager knows vs what the stage agent knows), the delegation pattern follows naturally. The manager reads pointers and reports; the stage agent carries methodology and produces outputs.
