# stage_-1_03_instructions

## Role

**Stage Manager** - Define constraints, guidelines, and implementation instructions.

## Responsibilities

- Create implementation instructions based on approved research
- Define constraints and guidelines
- Document setup guides and TODOs
- Produce instructions ready for design stage

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from stages manager
2. Read approved research from previous stage
3. Create implementation instructions
4. Write results to `hand_off_documents/outgoing/to_above/`

## Outputs

- Implementation instructions
- Setup guides
- Constraints documentation
- Usage guidelines

## Output Structure

```
outputs/
├── 01_instructions_in_progress/  ← Being developed
│   ├── by_need/
│   ├── by_topic/
│   └── synthesis/
└── 02_finished_instructions/     ← Approved, ready for design
    ├── by_need/
    ├── by_topic/
    └── synthesis/
```

## Structure

- `ai_agent_system/` - AI agent configurations for this stage
- `hand_off_documents/` - Four-directional handoffs
- `outputs/` - Instructions deliverables

## Context

- **Layer**: -1
- **Stage**: 03 (instructions)
- **Parent**: `../` (layer_-1_99_stages)
