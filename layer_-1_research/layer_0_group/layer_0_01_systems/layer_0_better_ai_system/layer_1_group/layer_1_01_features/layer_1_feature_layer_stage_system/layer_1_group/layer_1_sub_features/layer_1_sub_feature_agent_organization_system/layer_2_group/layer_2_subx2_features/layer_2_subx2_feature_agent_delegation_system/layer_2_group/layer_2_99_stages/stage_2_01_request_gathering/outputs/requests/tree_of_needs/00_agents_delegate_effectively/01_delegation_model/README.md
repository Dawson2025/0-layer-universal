---
resource_id: "d624498d-75e3-479d-93fc-d0da07927bed"
resource_type: "readme_output"
resource_name: "README"
---
# Branch: Delegation Model

**Parent**: [00_agents_delegate_effectively](../)

---

<!-- section_id: "3e35b442-6d68-4a1b-9af8-ebdabd534b2b" -->
## Core Question

> "How do managers delegate without carrying operational knowledge?"

---

<!-- section_id: "6b39b5ed-e989-4963-abf5-22c0894844d5" -->
## Description

Managers read pointers, delegate to stage agents, read stage reports. They don't carry methodology. This branch defines the mechanics of that delegation: how work is handed off, how status flows back, and what each agent type knows.

The three failure modes without a clear delegation model:
1. **Manager carries everything** -- context window overflow, blurred responsibilities
2. **Stage agents lack identity** -- no 0AGNOSTIC.md, so agents don't know their scope or methodology
3. **No async status** -- manager must load all stage details to know what happened

---

<!-- section_id: "38cfb69b-d735-48f7-b2c2-7a059b8c38ae" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_stage_delegation](./need_01_stage_delegation/) | "How does a manager hand off work to a stage agent?" | Define the manager-to-stage-agent delegation pattern |
| [need_02_stage_reports](./need_02_stage_reports/) | "How does a manager know what happened without loading stage details?" | Stage report protocol and content requirements |
| [need_03_agent_context_model](./need_03_agent_context_model/) | "What does each agent type know in its static vs dynamic context?" | Context models for managers, stage agents, sub-feature agents |

---

<!-- section_id: "302e6578-73cf-4887-b4f0-4b9fa8fab1d2" -->
## Key Insight

Delegation is an information design problem, not a workflow problem. The question is not "what steps does the manager follow?" but "what information does the manager need, and what information does the stage agent need?" When the information boundaries are clear, the delegation pattern follows naturally.
