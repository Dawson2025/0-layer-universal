# Index: layer_0 (Universal)

## Purpose
Universal content that applies to ALL projects. Rules, prompts, knowledge, and principles defined here are inherited by all layers.

---

## Children

| Name | Type | Keywords | Description |
|------|------|----------|-------------|
| 0AGNOSTIC.md | file | context, identity, navigation, behaviors | Tool-agnostic context (lean, <400 tokens) |
| .0agnostic | dir | rules, prompts, knowledge, agents, detailed | Detailed resources loaded on-demand |
| CLAUDE.md | file | claude, tool-specific, auto-generated | Claude Code context (auto-generated) |
| AGENTS.md | file | autogen, tool-specific, auto-generated | AutoGen context (auto-generated) |
| layer_0_03_sub_layers | dir | sub-layers, prompts, rules, knowledge, principles | Organized content by type |
| layer_0_99_stages | dir | stages, 01-11, workflow | Stage-based workflow (01-11) |
| outputs | dir | outputs, episodic, sessions, memory | Output artifacts and episodic memory |

---

## Sub-Layer Quick Reference

| Sub-Layer | Purpose | When to Read |
|-----------|---------|--------------|
| sub_layer_0_01_prompts | Session initialization prompts | Start of session |
| sub_layer_0_02_knowledge | Domain knowledge base | When context needed |
| sub_layer_0_03_principles | Guiding principles | Design decisions |
| sub_layer_0_04_rules | **Universal rules** | **ALWAYS** |
| sub_layer_0_05+_setup | OS/tool configuration | Environment issues |

---

## Navigation Guide

**Looking for rules?** → `layer_0_03_sub_layers/sub_layer_0_04_rules/`
**Looking for prompts?** → `layer_0_03_sub_layers/sub_layer_0_01_prompts/`
**Looking for session memory?** → `outputs/episodic/`
**Looking for sync scripts?** → `.0agnostic/scripts/`

---

*This index enables automated traversal via /find skill.*

