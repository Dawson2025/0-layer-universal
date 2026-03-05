---
resource_id: "d624498d-75e3-479d-93fc-d0da07927bed"
resource_type: "readme
output"
resource_name: "README"
---
# Branch: Delegation Model

**Parent**: [00_agents_delegate_effectively](../)

---

## Core Question

> "How do managers delegate without carrying operational knowledge?"

---

## Description

Managers read pointers, delegate to stage agents, read stage reports. They don't carry methodology. This branch defines the mechanics of that delegation: how work is handed off, how status flows back, and what each agent type knows.

The three failure modes without a clear delegation model:
1. **Manager carries everything** -- context window overflow, blurred responsibilities
2. **Stage agents lack identity** -- no 0AGNOSTIC.md, so agents don't know their scope or methodology
3. **No async status** -- manager must load all stage details to know what happened

---

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_stage_delegation](./need_01_stage_delegation/) | "How does a manager hand off work to a stage agent?" | Define the manager-to-stage-agent delegation pattern |
| [need_02_stage_reports](./need_02_stage_reports/) | "How does a manager know what happened without loading stage details?" | Stage report protocol and content requirements |
| [need_03_agent_context_model](./need_03_agent_context_model/) | "What does each agent type know in its static vs dynamic context?" | Context models for managers, stage agents, sub-feature agents |

---

## Key Insight

Delegation is an information design problem, not a workflow problem. The question is not "what steps does the manager follow?" but "what information does the manager need, and what information does the stage agent need?" When the information boundaries are clear, the delegation pattern follows naturally.
