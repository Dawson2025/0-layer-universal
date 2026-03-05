---
resource_id: "3fb9beba-2c83-4ebb-be97-1b16bf1814c9"
resource_type: "document"
resource_name: "stage_02_instructions"
---
# Stage 01: Instructions

## Purpose
Transform gathered requirements into clear, actionable instructions that define exactly what needs to be done. This stage bridges the gap between stakeholder requirements and technical implementation by creating unambiguous task definitions.

## Entry Criteria
- Requirements document completed from Stage 00
- Scope boundaries defined
- Acceptance criteria established
- All major ambiguities resolved

## Exit Criteria
- Instructions written in clear, actionable language
- All requirements mapped to specific instructions
- Dependencies between instructions identified
- Instructions validated for completeness
- Success metrics defined for each instruction

## Typical Tasks
- Break down requirements into discrete tasks
- Write step-by-step instructions
- Define success criteria for each task
- Identify task dependencies and sequencing
- Create instruction hierarchy (parent/child tasks)
- Validate instructions against original requirements
- Review instructions for clarity and completeness

## Handoffs
- **From Previous**: Requirements document, scope definition, acceptance criteria
- **To Next**: Instruction set, task hierarchy, dependency map, success metrics

## Directory Structure
Each stage directory contains:
- `CLAUDE.md` - Stage-specific context
- `ai_agent_system/` - AI tool configurations
- `hand_off_documents/` - Handoff files
- `docs/` - Stage documentation
- `work/` - Working files

## Key Artifacts
- Instruction document
- Task breakdown structure
- Dependency matrix
- Success criteria definitions
- Priority rankings

## Common Pitfalls
- Instructions too vague or abstract
- Missing edge cases
- Unclear success criteria
- Overlooking dependencies
- Not validating against requirements
