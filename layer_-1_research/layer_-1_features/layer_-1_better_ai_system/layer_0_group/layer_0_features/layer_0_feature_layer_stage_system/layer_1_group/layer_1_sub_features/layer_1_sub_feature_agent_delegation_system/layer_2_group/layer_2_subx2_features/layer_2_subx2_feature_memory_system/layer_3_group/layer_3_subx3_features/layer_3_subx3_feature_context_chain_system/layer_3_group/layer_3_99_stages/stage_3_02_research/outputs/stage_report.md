# Stage Report: 02_research

## Status
active

## Last Updated
2026-02-22

## Summary
Extensive research into context chain architecture, avenue web design, and AALang integration. 25+ research files organized by topic. New findings (2026-02-22): context chain discovery temperatures, .1merge hot injection mechanism, user-level chain extension, and real-world validation via skill discovery chain testing.

## Key Outputs
- `outputs/by_topic/README.md`: Full research index (the master table of contents)
- 6 topic areas: vision, problem analysis, obstacles, design, architecture decisions, **discovery**
- Key decisions: three-layer redundancy model, .0agnostic/ as canonical filesystem, 8-avenue web
- `outputs/by_topic/architecture/selective_jsonld_navigation.md`: Proven jq-based JSON-LD navigation (2-5% file loads)
- `outputs/by_topic/verification/verification_results.md`: What was verified true/false
- `outputs/by_topic/three_tier_knowledge_architecture.md`: Reference to parent-level research on three-tier pattern

## Findings
- Three-layer redundancy (jq-first + skills + .integration.md) is the approved approach
- 8 avenues provide independent context delivery with "any-one-fires" resilience
- Static chain was 717 lines (target <400) — lean static context is critical
- Selective JSON-LD loading proven effective (load 2-5% per query)
- .0agnostic/ internal structure designed and validated
- **New (2026-02-22)**: Discovery temperature model — Hot (CLAUDE.md, always loaded), Warm (path-specific rules, on directory entry), Cold (dynamic rules/skills, on trigger/demand)
- **New (2026-02-22)**: .1merge `2_additions/` tier serves as the mechanism for tool-specific hot context injection — content in `tool_additions.md` appears in the generated CLAUDE.md but NOT in AGENTS.md/GEMINI.md/OPENAI.md
- **New (2026-02-22)**: Context chain extends beyond the repo to user-level via `~/.0agnostic/` and `user-level-sync.sh`
- **New (2026-02-22)**: React-rendered pages (Perplexity) require React fiber traversal for link extraction — standard DOM queries return ~0 external URLs. This validated the need for tool-specific dynamic rules

## Open Items
- Agent context model for stage delegation (design phase needed)
- Knowledge graph formalization not yet implemented
- Scored retrieval system not yet designed
- Discovery temperature model needs formal documentation as a research finding

## Handoff
- **Ready for next stage**: yes for current scope
- **Next stage**: 04_design (architecture decisions for next features)
- **What next stage needs to know**: all major architecture decisions are made; discovery temperature model and .1merge injection are new patterns to formalize in design; user-level chain extension is a new architectural element
