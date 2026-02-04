# Need: Universal AI Tool Support (Any Tool Can Access System)

**Branch**: [02_continuous](../)
**Question**: "Can AI tools other than Claude Code (Copilot, Gemini, clawdbot, etc.) access and work with the universal system?"
**Related Needs**: need_01_tool_portable, need_02_session_resilient, need_08_universal_context_discovery
**Related Feature**: feature_universal_ai_tool_access.md

---

## Definition

Enable **any supported AI tool** to discover, load, and use the 0_layer_universal AI system regardless of:
- Which AI tool is being used (Claude Code, Copilot, Gemini, clawdbot, etc.)
- Where the tool is running (local, remote, container)
- What state the system is in (normal, recovery, degraded)
- Which machine the tool is running on
- What programming language or framework the tool uses

---

## Why This Matters

- **Not Locked to One Tool**: Switching tools doesn't mean losing context or functionality
- **Resilience**: If Claude Code fails, use Copilot immediately with same context
- **Flexibility**: Choose best tool for each task instead of being forced to one tool
- **Future-Proof**: New AI tools can be supported when they appear
- **Vendor Independence**: Not dependent on single vendor's tool
- **Cross-Tool Continuation**: Start work in Claude Code, continue in Copilot on same machine or different machine
- **Consistency**: All tools enforce same universal rules and share same memories

---

## Requirements

### Tool Access API

- MUST define unified data access API that any tool can use
- MUST provide methods to:
  - `get_universal_rules()` → Layer 0 (applies to all)
  - `get_project_context(project_id)` → Layer 1 (current project)
  - `get_research_context()` → Layer -1 (research findings)
  - `get_skills(skill_type)` → Available skills library
  - `query_memories(query)` → Search past learnings
  - `get_hand_off_documents()` → Previous session state
  - `report_completion()` → Write status back
- MUST be language-agnostic (implementable in Bash, Python, Go, Node, etc.)
- MUST support synchronous and asynchronous access
- MUST handle errors gracefully with meaningful messages

### Tool Discovery

- MUST allow tools to locate the AI system without configuration
- MUST use universal context discovery protocol (need_08)
- MUST auto-detect tool type and capabilities
- MUST provide tool-specific documentation
- MUST support multiple tools running simultaneously
- MUST maintain tool identity in state/logs

### Tool Adapters

- MUST provide adapter for Claude Code CLI (update/enhance existing)
- MUST provide adapter for GitHub Copilot CLI
- MUST provide adapter for Google Gemini CLI
- MUST provide adapter for OpenCode/Azure CLI
- MUST provide adapter for clawdbot (Discord)
- MUST support custom adapters for community tools
- MUST define adapter interface/API for tool developers
- MUST each adapter converts tool-specific format to/from universal format

### Cross-Tool State Synchronization

- MUST allow work to continue when switching tools:
  - Tool A writes state to hand-off document
  - Tool B reads state and continues exact work
  - Tool C can read state from A or B
- MUST preserve task context across tool changes
- MUST include tool identifier in all hand-off documents
- MUST timestamp all state writes (for ordering)
- MUST handle conflicts when two tools modify state simultaneously
- MUST prevent one tool's operations from breaking another tool's access

### Universal Rules Enforcement

- MUST load universal rules (Layer 0) regardless of tool
- MUST enforce rules consistently across all tools
- MUST prevent any tool from bypassing universal rules
- MUST allow tool-specific rule variations while keeping universal rules intact
- MUST log rule violations for audit trails
- MUST validate tool compliance at integration time

### Skill & Memory Access

- MUST make skills library accessible to all tools
- MUST allow tools to discover available skills
- MUST support tool-specific skill implementations
- MUST maintain shared memory pool accessible to all tools
- MUST allow tools to query memories from other tools' sessions
- MUST handle memory conflicts (same learned fact from different tools)
- MUST accumulate learning across all tools

### Hand-Off Document Format

- MUST define standard hand-off document format (tool-agnostic)
- MUST include:
  - Task description
  - Current state/context
  - Tool that created it
  - Timestamp
  - Session metadata
- MUST be readable by any tool (JSON, YAML, or Markdown acceptable)
- MUST support both simple and complex state
- MUST maintain version history for hand-offs
- MUST handle incomplete/partial hand-offs gracefully

### Tool Integration Path

- MUST have low friction for adding new tools
- MUST support both official and community adapters
- MUST provide reference implementation (Claude Code adapter)
- MUST document integration requirements clearly
- MUST test cross-tool compatibility before release
- MUST have versioning strategy for API changes

### Tool Compatibility Matrix

- MUST support:
  - ✓ Claude Code CLI (primary, already works)
  - GitHub Copilot CLI
  - Google Gemini CLI
  - OpenCode/Azure CLI
  - clawdbot (Discord bot)
  - Other AI tools via custom adapters
- MUST handle different tool capabilities gracefully
- MUST document which features work in which tools
- MUST have fallback behavior for unsupported features
- MUST allow incremental capability support

### Cross-Machine Tool Switching

- MUST support seamless switching between:
  - Tool + Machine A → Tool + Machine B (different tool, different machine)
  - Tool A Machine A → Tool B Machine A (different tool, same machine)
  - Tool A Machine A → Tool A Machine B (same tool, different machine)
- MUST maintain context through all combinations
- MUST use Syncthing to sync hand-off documents across machines
- MUST verify data consistency after switching
- MUST log all tool/machine transitions

### Tool Initialization & Bootstrap

- MUST allow tool to bootstrap with minimal configuration
- MUST auto-discover system location using context discovery protocol
- MUST load all required context on first run
- MUST cache context locally for fast startup
- MUST validate cache freshness on each startup
- MUST refresh cache if remote has changes

### API Versioning & Compatibility

- MUST maintain backward compatibility for API changes
- MUST support multiple API versions simultaneously (if major version changes)
- MUST document deprecation clearly before removing features
- MUST provide migration guides for tools switching API versions
- MUST have clear versioning scheme (semantic versioning)

---

## Acceptance Criteria

- [ ] Unified access API documented and published
- [ ] Claude Code CLI enhanced to use access API
- [ ] GitHub Copilot adapter implemented and tested
- [ ] Google Gemini adapter implemented and tested
- [ ] OpenCode/Azure adapter implemented and tested
- [ ] clawdbot adapter implemented and tested
- [ ] Can start task in Claude Code, continue in Copilot
- [ ] Can switch tools mid-task without losing context
- [ ] All tools load same Layer 0 universal rules
- [ ] Hand-off documents created and read by all tools
- [ ] Cross-machine tool switching verified working
- [ ] State synchronization tested: conflicts resolved correctly
- [ ] Tool identity properly logged in all operations
- [ ] Memory sharing tested: one tool's learning accessible to others
- [ ] Skill library accessible from all tools
- [ ] Documentation: How to integrate new AI tool
- [ ] Documentation: How to use system with multiple tools
- [ ] Reference implementation (adapter) provided for tool developers

---

## Integration Points

This need integrates with and enhances:

- **need_01_tool_portable**: Makes tools portable by supporting multiple tools
- **need_02_session_resilient**: State continues across tool changes
- **need_08_universal_context_discovery**: Unified discovery used by all tools
- **need_06_universal_rules_and_cross_device_access**: All tools enforce same rules
- **03_trustworthy/need_01_rule_compliant**: All tools comply with universal rules

---

## Technical Considerations

### Access Flow

```
Any AI Tool
    ↓
Discovery Protocol (need_08)
    ├── Find ~/.claude/config.json
    ├── Check /etc/claude/
    └── Locate system
    ↓
Tool Adapter Layer
    ├── Claude Code: Parse CLAUDE.md natively
    ├── Copilot: Convert to Copilot format
    ├── Gemini: Query via Gemini API
    ├── clawdbot: Load from Discord config
    └── Others: Via custom adapter
    ↓
Unified Access API
    ├── Load universal rules
    ├── Load project context
    ├── Load research context
    ├── Load skills library
    └── Read hand-off documents
    ↓
Tool Executes Work
    ├── Respects universal rules
    ├── Uses shared skills
    ├── Accesses memories
    └── Writes completion
    ↓
State Synchronization
    ├── Write hand-off document
    ├── Syncthing syncs to machines
    └── Other tools can read state
```

### Hand-Off Document Example

```json
{
  "version": 1,
  "source_tool": "claude-code",
  "source_machine": "laptop-ubuntu",
  "timestamp": "2026-01-27T14:45:00Z",
  "session_id": "session_abc123",
  "task_description": "Implement resilience feature Phase 1",
  "current_state": {
    "stage": "phase_1_recovery_partition",
    "progress": "Recovery partition created and mounted",
    "next_step": "Copy Layer 0 to recovery partition",
    "blockers": "none"
  },
  "context": {
    "layer_0_accessible": true,
    "layer_1_project": "0_layer_universal",
    "layer_minus1_research": "better_ai_system"
  },
  "tool_specific": {
    "claude_code_session": "session_abc123",
    "last_action": "file_created"
  }
}
```

### Adapter Architecture

```
Tool-Specific Adapter
├── Discover system location
├── Load unified API
├── Convert Tool Format → Universal Format
├── Execute via unified API
├── Convert Universal Format → Tool Format
└── Write state back

Universal API
├── Load layers
├── Query memories
├── Get skills
├── Validate rules
└── Write hand-offs

Unified Format (JSON/YAML)
├── Layer 0 (universal rules)
├── Layer 1 (project context)
├── Layer -1 (research)
├── Skills library
└── Memories database
```

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Tool API incompatibility** | Define minimal required API, accept multiple implementations |
| **Different rule interpretations** | Strict specification + validation tests in each adapter |
| **State sync conflicts** | Tool identifier + timestamp in hand-off, conflict resolution policy |
| **Tool-specific features lost** | Lowest-common-denominator core features + tool-specific extensions |
| **Requires vendor cooperation** | Start with open tools, build independent adapters if needed |
| **Complex integration overhead** | Provide reference implementation and clear interface |

---

## Dependencies

### Blocking Dependencies
- ✓ `need_07_resilient_system_state`: Unified API requires resilient data storage
- ✓ `need_08_universal_context_discovery`: Tools must find system via discovery protocol

### Dependent Features
- Any new AI tool wanting to access the system
- Web-based AI interfaces (if system hosted publicly)
- Mobile AI assistants (if applicable)
- Community-built tool adapters

---

## Timeline (After Resilience & Context Discovery, Weeks 8-13)

```
Week 8-9:  Phase 1 (Discovery & API) - define access interface
Week 9-10: Phase 2 (Claude Code enhancement) - update existing adapter
Week 10-12: Phase 3 (Tool adapters) - build 4 additional adapters
Week 12-13: Phase 4 (Testing & validation) - comprehensive cross-tool testing
```

---

## Implementation Priority

### High Priority (Weeks 10-11)
- GitHub Copilot adapter (most common alternative to Claude Code)
- Core unified API stable and documented

### Medium Priority (Weeks 11-12)
- Google Gemini adapter (good for research tasks)
- OpenCode/Azure adapter (enterprise use case)

### Lower Priority (Weeks 12+)
- clawdbot adapter (Discord integration)
- Community adapters (via open interface)

---

## Related Documents

- [`feature_universal_ai_tool_access.md`](../../../requests/feature_universal_ai_tool_access.md): Detailed feature specification
- [`need_01_tool_portable`](./need_01_tool_portable/): Tool portability requirement
- [`need_02_session_resilient`](./need_02_session_resilient/): Session state requirement
- [`need_08_universal_context_discovery`](./need_08_universal_context_discovery/): Discovery mechanism requirement

---

## Related User Requests

**From Dawson (2026-01-27):**
- "We need to document stuff for getting AI tools like Claude Code CLI, Copilot CLI, Gemini CLI, OpenCode CLI, and clawdbot to work"
- "No matter what's going on in the computer or any location in any machine"
- "Any tool can access system, traverse through it, use skills and memories"
- "If Claude Code becomes unavailable, I can use Copilot immediately with same context"
