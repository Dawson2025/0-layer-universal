# layer_0_feature_ai_context_system

## Overview
Research feature focused on improving context gathering and management for AI agents. Addresses how agents discover, load, and use context from the layer-stage hierarchy.

## Status
**Progress**: ~5% (Research)
**Current Stage**: 02_research

## Purpose
Research and design improvements to context systems:
- Context gathering rule consistency
- Context loading optimization
- Context scope definitions
- Agent context handoff

## Problems Being Addressed

### From AI System Audit

#### Major Issues
1. **Context Gathering Rules Scattered** (MAJOR)
   - Rules exist in multiple places:
     - `layer_0_01_ai_manager_system/agnostic/context_gathering_rules.md`
     - `layer_2_feature_context_gathering/` (in layer_stage_system)
     - Inline in various READMEs
   - No single authoritative source

2. **Agnostic/Specific Pattern Incomplete** (MAJOR)
   - `layer_0_01_ai_manager_system/` has agnostic/ and specific/
   - No clear guidance on when to use which
   - specific/ is deeply nested but sparse

3. **Multiple CLAUDE.md Entry Points** (affects context)
   - Agents don't know which CLAUDE.md to read first
   - No defined chain for context loading

#### Minor Issues
4. **Context Gathering Skill Implementation**
   - `.claude/skills/context-gathering` exists
   - References old `0_context` structure
   - No bridge to new system

5. **Layer Navigation Unclear**
   - `layer_navigation.md` exists but not comprehensive
   - Vertical chain rules defined but horizontal unclear

### Specific Context Problems
1. No context priority system (which context overrides which)
2. No context caching or optimization
3. No context scope boundaries clearly defined
4. Stage-specific context not well integrated

## Research Areas
1. **Context Discovery**
   - How agents find relevant context
   - Context chain definition
   - Automatic vs manual context loading

2. **Context Priority**
   - Conflict resolution between contexts
   - Override rules
   - Inheritance patterns

3. **Context Optimization**
   - Minimal context loading
   - Context caching
   - Lazy loading patterns

4. **Context Handoff**
   - How context passes between agents
   - Context serialization
   - Context compression

## Structure
```
layer_0_feature_ai_context_system/
├── CLAUDE.md
├── layer_0/
│   ├── layer_0_03_sub_layers/
│   │   └── sub_layer_0_02_knowledge_system/
│   │       ├── overview/
│   │       └── things_learned/
│   └── layer_0_99_stages/
│       └── stage_0_02_research/
│           └── outputs/
└── layer_1/
    └── layer_1_features/
```

## Related Features
- `better_layer_stage_system` - Framework structure
- `ai_manager_hierarchy_system` - Manager/worker context needs
- `ai_documentation_system` - Documentation as context source
