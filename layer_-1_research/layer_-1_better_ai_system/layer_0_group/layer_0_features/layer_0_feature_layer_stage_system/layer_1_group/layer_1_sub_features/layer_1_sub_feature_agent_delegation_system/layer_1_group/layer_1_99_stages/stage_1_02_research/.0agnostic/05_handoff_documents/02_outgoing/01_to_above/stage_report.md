# Stage Report: 02_research

## Status
active

## Last Updated
2026-02-26

## Summary
Research conducted through both the context_chain_system living laboratory (implicit findings) and 3 formal research topic directories. Topics cover tool context cascading (how AI coding tools handle CLAUDE.md/AGENTS.md/GEMINI.md cascading), multi-agent context patterns (how CrewAI/LangGraph/AutoGen handle shared context), and scope boundary traversal (directional patterns for crossing layer/stage boundaries).

## Key Outputs
- `outputs/by_topic/tool_context_cascading/README.md`: 3 of 4 tools cascade natively (Claude Code, Codex, Gemini CLI); Cursor uses glob targeting. Native cascading is an argument FOR lean content per level.
- `outputs/by_topic/multi_agent_context_patterns/README.md`: All 3 frameworks converge on minimal context + on-demand access. None use full parent cascade.
- `outputs/by_topic/scope_boundary_traversal/README.md`: Scope decisions are directional (up/down/left/right/sideways/multi-location). Communication protocol differs per direction. Universal infrastructure loaded on-demand, positional awareness is compact STATIC.
- Implicit research via context_chain_system (56+ files across 9 topics, 76 PASS tests)
- Child entity research: memory_system (21 files on cognitive science, memory types)

## Findings
- Managers don't need stage methodology — coordinate effectively by reading stage reports alone
- 0AGNOSTIC.md is the right vehicle for stage identity — static context, tool-agnostic, single source of truth
- Two-halves context pattern discovered (operational guidance + current state summary) — formalized as Principle 9
- Stage reports enable async coordination — manager never needs to load stage outputs
- Scope boundary decisions discovered — three-option framework (do it yourself, delegate, instantiate) — formalized as Principle 8
- Scope boundaries span both layers AND stages — single rule covers both dimensions
- Tool context cascading varies by tool — 3/4 cascade natively, Cursor uses glob targeting. Cascading makes lean CLAUDE.md content critical
- Multi-agent frameworks converge on minimal context + on-demand — CrewAI, LangGraph, AutoGen all use this pattern
- Scope boundary traversal is directional — direction determines communication method. Multi-location work escalates to nearest common ancestor

## Open Items
- Context chain system lessons should be documented as a formal research topic
- multi_agent_system child entity not yet explored as a research vehicle

## Handoff
- **Ready for next stage**: yes
- **Next stage**: 04_design (multiple design decisions already created from these findings)
- **Key findings for design**: Minimal context model validated, directional scope boundaries formalized
