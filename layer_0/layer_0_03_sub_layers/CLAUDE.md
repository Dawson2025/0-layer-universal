# layer_0_03_sub_layers

## Role

**Sub_layers Manager** - Manages universal sub_layers (content types that apply to all projects).

## Responsibilities

- Manage universal prompts, knowledge, principles, rules, and setup content
- Delegate tasks to appropriate sub_layer
- Aggregate results from sub_layers
- Handle escalations from sub_layers
- Maintain sub_layer registry

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from layer_0
2. Check `hand_off_documents/incoming/from_below/` for results/escalations from sub_layers
3. Process pending work or delegate to appropriate sub_layer

## Primary AI System

**sub_layer_0_01_ai_system** contains AALang - the primary way agents work within our layer-stage system. It is used at every layer, stage, sub_layer, and sub_stage throughout the entire framework.

## Children (Universal Sub_layers)

| Number | Name | Purpose |
|--------|------|---------|
| 00 | sub_layer_registry | Sub_layer definitions and metadata (data only) |
| 01 | ai_system | **PRIMARY AI SYSTEM** - AALang: how agents work at all levels (submodule: Dawson2025/AALang-Gab, fork of yenrab/AALang-Gab, **use dawson branch**) |
| 02 | knowledge_system | Domain knowledge, reference materials |
| 03 | principles | Guiding principles for decisions |
| 04 | rules | Universal rules (modification protocol, commit rule, etc.) |
| 05 | protocols | Session init protocols, context protocols |
| 06+ | setup_dependant_hierarchy | OS/tool specific configuration |

## Navigation

- **Parent**: `../` (layer_0)
- **Registry**: `layer_0_00_sub_layer_registry/`

## Key Content

| Sub_layer | Key Files |
|-----------|-----------|
| ai_system | AALang language and gab compiler |
| protocols | `universal_init_prompt.md` |
| rules | `AI_CONTEXT_MODIFICATION_PROTOCOL.md`, `AI_CONTEXT_COMMIT_PUSH_RULE.md`, `safety_governance.md` |
| principles | Guiding principles documentation |
