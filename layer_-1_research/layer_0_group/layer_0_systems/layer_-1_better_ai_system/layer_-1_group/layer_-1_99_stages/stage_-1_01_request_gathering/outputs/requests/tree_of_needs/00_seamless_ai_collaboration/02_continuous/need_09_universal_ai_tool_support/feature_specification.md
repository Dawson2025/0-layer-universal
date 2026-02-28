# Feature Request: Universal AI Tool Integration & Access

**Status**: Under Request Gathering
**Priority**: HIGH (Depends on: Feature: Full System Resilience)
**Related**: `need_01_tool_portable`, `need_02_session_resilient`
**Project**: better_ai_system

---

## Overview

Enable multiple AI tools and CLIs to access and use the 0_layer_universal AI system universally:

**No matter:**
- Which AI tool is being used (Claude Code, Copilot, Gemini, etc.)
- Where the tool is running (local machine, remote, container)
- What state the computer is in (normal, recovery, degraded, corrupted)
- Which machine it's running on (Ubuntu, Windows WSL, macOS, VPS)
- Whether the system is online or offline

**Result**: Any supported AI tool can access universal rules, skills, memories, and knowledge from the system.

---

## Supported AI Tools

### Currently Using
- ✓ **Claude Code CLI** - Primary tool, reads CLAUDE.md hierarchy

### Want to Support
- [ ] **GitHub Copilot CLI** (GitHub/OpenAI)
- [ ] **Google Gemini CLI** (Google)
- [ ] **OpenCode CLI** / **Azure CLI** (Microsoft)
- [ ] **clawdbot** (Discord bot for Claude)
- [ ] **Other AI tools** (Perplexity, Anthropic APIs, etc.)

### Future Support
- [ ] **Web-based AI interfaces** (if system hosted)
- [ ] **Mobile AI assistants** (if applicable)
- [ ] **Custom AI agents** (built on system)

---

## What Is It?

A standardized access layer allowing **any AI tool** to:

1. **Discover** the AI system location and structure
2. **Load** universal rules regardless of tool type
3. **Access** skills, prompts, and knowledge bases
4. **Query** memories and session state
5. **Respect** rules and constraints
6. **Continue** work across tool changes
7. **Sync** changes back to central system

---

## Why?

### Current Limitation
- System is tightly coupled to Claude Code
- If Claude Code becomes unavailable, can't use system
- Switching tools loses context

### Requirements Driving This
From Tree of Needs:
- `need_01_tool_portable`: "Can I switch tools?"
  - **Answer**: Yes, if tools support access layer
- `need_02_session_resilient`: "Can I pick up where I left off?"
  - **Answer**: Yes, if tool can access hand-off documents

### Strategic Value
- **Not locked to one vendor**: Claude Code, Copilot, Gemini all supported
- **Flexibility**: Choose tool based on task, not habit
- **Resilience**: If Claude Code fails, use alternative
- **Future-proof**: New tools can be added
- **Tool evolution**: When better tools appear, use them

### Real-World Scenario

**Today:**
```
You: "I want to use Copilot instead of Claude Code"
System: "Sorry, Copilot doesn't understand CLAUDE.md"
You: Stuck using Claude Code or losing context
```

**With This Feature:**
```
You: "I want to use Copilot instead of Claude Code"
System: "Sure, here are your universal rules [from access layer]"
Copilot: Reads rules, loads context, continues work
You: Seamlessly switch tools
```

---

## Scope: 4 Components

### Component 1: Discovery Protocol
**How AI tools find the system**

```
Tool starts → Looks in standard locations:
├── ~/.claude/              (User home)
├── /etc/claude/            (System-wide)
├── /opt/claude/            (System tools)
├── Environment variables   (CLAUDE_SYSTEM_PATH)
├── Git config             (claude.system)
└── Syncthing folders      (synced machines)

Tool finds: Config file pointing to system location
```

### Component 2: Unified Data Access Interface
**How tools read rules, skills, memories**

```
Tool API:
├── get_universal_rules()          → Layer 0 rules
├── get_project_context(project_id) → Layer 1 data
├── get_research_context()          → Layer -1 data
├── get_skills(skill_type)         → Available skills
├── query_memories(query)          → Search memories
├── get_hand_off_documents()       → Session state
└── report_completion()            → Write status back
```

### Component 3: Tool Adapter Plugins
**How each tool integrates**

```
For Claude Code:
├── CLAUDE.md reader        (already has)
├── agnostic.md reader      (already has)
└── Hand-off document reader (already has)

For GitHub Copilot:
├── .copilot/config.json    → Points to system
├── Rule loader             → Reads Layer 0
├── Skill provider          → Provides context
└── Hand-off adapter        → Reads state

For Google Gemini:
├── gemini.config.json      → Points to system
├── Rule loader
├── Skill provider
└── Hand-off adapter

For clawdbot:
├── Discord config
├── Rule loader
├── Skill provider
└── Hand-off adapter
```

### Component 4: Cross-Tool State Synchronization
**How work continues across tools**

```
Scenario: Start task in Claude Code, continue in Copilot

Claude Code:
1. Reads Layer 0, 1, -1
2. Does work
3. Writes hand-off document to:
   hand_off_documents/outgoing/tool_state/

Copilot:
1. Reads Layer 0, 1, -1
2. Reads hand-off document (gets context)
3. Continues exact work
4. Writes completion back

Syncthing: Syncs both writes across machines
```

---

## Implementation Phases

### Phase 1: Discovery & Access Protocol
- Define standard locations for AI system
- Create unified access API
- Document discovery mechanism

### Phase 2: Claude Code Enhancement
- Add tool identifier to Hand-off documents
- Enhanced state preservation
- Cross-tool compatibility mode

### Phase 3: Tool Adapters
- Build adapters for Copilot, Gemini, etc.
- Plugin architecture for new tools
- Standardized configuration

### Phase 4: Testing & Validation
- Test tool switching
- Verify context preservation
- Cross-machine tool switching

---

## Architecture: How Tools Access System

```
Any AI Tool
    ↓
Discovery Protocol
    ├── Check ~/.claude/config.json
    ├── Check env var CLAUDE_SYSTEM_PATH
    └── Find system location
    ↓
Unified Access API
    ├── Load universal rules (Layer 0)
    ├── Load context (Layer 1 or -1)
    ├── Load skills/prompts
    └── Read previous hand-off documents
    ↓
Tool-Specific Adapter
    ├── Convert to tool's format
    ├── Apply tool-specific rules
    └── Setup tool environment
    ↓
Tool Executes
    ├── Reads from access layer
    ├── Respects universal rules
    ├── Uses skills/memories
    └── Writes completions
    ↓
State Synchronization
    ├── Write hand-off documents
    ├── Syncthing syncs to other machines
    └── Other tools can read state
```

---

## Success Criteria

### Phase 1 Complete
- [ ] Standard locations defined
- [ ] Access API documented
- [ ] Discovery protocol working
- [ ] Claude Code can use it (backwards compatible)

### Phase 2 Complete
- [ ] Claude Code enhanced
- [ ] Tool identifier in hand-off documents
- [ ] State preservation improved
- [ ] Cross-tool switching works for Claude Code

### Phase 3 Complete
- [ ] Copilot adapter working
- [ ] Gemini adapter working
- [ ] OpenCode adapter working
- [ ] clawdbot adapter working

### Phase 4 Complete
- [ ] Can start task in Claude Code, continue in Copilot
- [ ] Can use any tool, rules enforced
- [ ] Cross-machine tool switching works
- [ ] Context preserved across tool changes

### System Integration Complete
- [ ] All tools honor Layer 0 rules
- [ ] Skill discovery automatic
- [ ] Memory/learning accessible from all tools
- [ ] Tool switching transparent to user

---

## Benefits by Scenario

### Scenario 1: Tool Failure
**Before**: Claude Code crashes → Stuck
**After**: Claude Code crashes → Use Copilot → Continue work immediately

### Scenario 2: Task-Specific Tool Choice
**Before**: Always use Claude Code
**After**: Use best tool for each task
- Complex code? → Use Copilot
- Research? → Use Gemini
- Discord chat? → Use clawdbot
- CLI work? → Use Claude Code

### Scenario 3: System Recovery
**Before**: Lose context during recovery
**After**: Tool doesn't matter, access layer still works
- Boot into recovery USB? → Gemini CLI still works
- Network recovery? → Any tool can use NFS

### Scenario 4: Multi-Machine Work
**Before**: Each machine has different tools, different context
**After**: Same context, any tool, any machine
- Work on laptop with Claude Code
- Continue on desktop with Copilot
- Continue on phone with clawdbot
- All see same rules and memory

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| **Tool API incompatibility** | Define minimal required API, tools implement adapter |
| **Different rule interpretations** | Strict rule specification, validation tests |
| **State synchronization conflicts** | Tool identifier + timestamp in hand-off documents |
| **Tool-specific features incompatible** | Lowest-common-denominator core features, tool-specific extensions |
| **Requires vendor cooperation** | Start with open tools (Claude via API, open adapters) |
| **Complex tool integration** | Plugin architecture, community can build adapters |

---

## Dependencies

### Blocking Dependencies
- ✓ `feature_resilience_system`: Must have resilient access layer first
- ✓ `need_06_universal_rules_and_cross_device_access`: Rules must be accessible universally

### Dependent Features
- Any new tool added after this
- Web-based AI interfaces (depends on access layer)
- Mobile AI assistants (depends on access layer)

---

## Timeline (After Resilience Complete)

```
Week 8-9:  Phase 1 (Discovery & API)
Week 9-10: Phase 2 (Claude Code enhancement)
Week 10-12: Phase 3 (Tool adapters - 4 tools)
Week 12-13: Phase 4 (Testing & validation)
Week 13+:  Documentation & community adapters
```

---

## Related Documents

- [`need_01_tool_portable`](tree_of_needs/01_capable/need_01_tool_portable/): "Can I switch tools?"
- [`need_02_session_resilient`](tree_of_needs/02_continuous/need_02_session_resilient/): "Can I pick up where I left off?"
- [`feature_resilience_system.md`](feature_resilience_system.md): Underlying resilience infrastructure
- [`RESILIENCE_SYSTEM_STAGING_PLAN.md`](../RESILIENCE_SYSTEM_STAGING_PLAN.md): How to document through stages

---

## Questions for Design Phase

1. **Tool Priority**: Which tool should be supported first after Claude Code?
   - GitHub Copilot (most common alternative)?
   - Google Gemini (good research)?
   - clawdbot (Discord integration)?

2. **Vendor Relations**: Should we approach vendors for official support or build independent adapters?

3. **API Specification**: How strict should the access API be? Any tool-specific extensions allowed?

4. **State Sync**: When tool switches, what state needs to be preserved?
   - Current task?
   - Current context?
   - Tool-specific preferences?

5. **Offline Operation**: Should tools work offline, or only when central system accessible?

6. **Authentication**: How should cross-tool authentication work?
   - API keys?
   - OAuth?
   - Session tokens?

---

## Vision: The Ideal End State

```
User (any machine):
  "Start implementing feature X with Claude Code"
    Claude Code reads Layer 0, 1, starts work
    Writes progress to hand-off documents

User (same or different machine):
  "Switch to Gemini for research"
    Gemini reads same Layer 0, 1
    Reads Claude Code's hand-off documents
    Continues work without context loss

User (different machine):
  "Use Copilot to review my code"
    Copilot reads same layers via Syncthing
    Reads hand-off documents from both previous tools
    Provides review based on full context

User (discord):
  "clawdbot, what's the status?"
    clawdbot reads same rules and memories
    Reports status from hand-off documents
    Continues to track across all tools

Throughout: Universal rules enforced, memories accumulated, work continuous
           regardless of tool, machine, or system state
```

---

## Next Steps

1. **Stage 01 (This stage)**: Document requirements ← YOU ARE HERE
2. **Stage 02**: Research tool integration patterns
3. **Stage 03**: Define access API and discovery protocol
4. **Stage 04**: Design tool adapters
5. **Stage 05**: Plan adapter implementation
6. **Stage 06**: Build adapters (Copilot, Gemini, OpenCode, clawdbot)
7. **Stage 07**: Test cross-tool scenarios
8. **Stage 08**: Review and critique
9. **Stage 09**: Fix issues
10. **Stage 10**: Final integrated system
11. **Stage 11**: Archive and future roadmap

