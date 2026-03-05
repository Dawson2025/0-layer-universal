---
resource_id: "d22b8aa6-6025-4a29-907d-fc64729d2f78"
resource_type: "index
document"
resource_name: "0INDEX"
---
# Index: layer_0 (Universal)

<!-- section_id: "867588ca-506f-4f8a-ba78-6ea210a23ec8" -->
## Purpose
Universal content that applies to ALL projects. Rules, prompts, knowledge, and principles defined here are inherited by all layers.

---

<!-- section_id: "4d0664d6-edbb-4929-917f-bf859e03c9ff" -->
## Children

| Name | Type | Keywords | Description |
|------|------|----------|-------------|
| 0AGNOSTIC.md | file | context, identity, navigation, behaviors | Tool-agnostic context (lean, <400 tokens) |
| .0agnostic | dir | rules, prompts, knowledge, agents, detailed | Detailed resources loaded on-demand |
| CLAUDE.md | file | claude, tool-specific, auto-generated | Claude Code context (auto-generated) |
| AGENTS.md | file | autogen, tool-specific, auto-generated | AutoGen context (auto-generated) |
| layer_0_04_sub_layers | dir | sub-layers, prompts, rules, knowledge, principles | Organized content by type |
| layer_0_99_stages | dir | stages, 01-11, workflow | Stage-based workflow (01-11) |
| outputs | dir | outputs, episodic, sessions, memory | Output artifacts and episodic memory |

---

<!-- section_id: "768917ec-bec2-42dc-baac-5ccbdf4679b3" -->
## Sub-Layer Quick Reference

| Sub-Layer | Purpose | When to Read |
|-----------|---------|--------------|
| sub_layer_0_01_knowledge_system | Session initialization prompts | Start of session |
| sub_layer_0_02_knowledge | Domain knowledge base | When context needed |
| sub_layer_0_01_knowledge_system/principles | Guiding principles | Design decisions |
| sub_layer_0_02_rules | **Universal rules** | **ALWAYS** |
| sub_layer_0_05+_setup | OS/tool configuration | Environment issues |

---

<!-- section_id: "664528f8-e54c-4a30-b266-19e760e50f7c" -->
## Navigation Guide

**Looking for rules?** → `layer_0_04_sub_layers/sub_layer_0_02_rules/`
**Looking for prompts?** → `layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/`
**Looking for session memory?** → `.0agnostic/episodic_memory/`
**Looking for sync scripts?** → `.0agnostic/scripts/`

---

*This index enables automated traversal via /find skill.*

