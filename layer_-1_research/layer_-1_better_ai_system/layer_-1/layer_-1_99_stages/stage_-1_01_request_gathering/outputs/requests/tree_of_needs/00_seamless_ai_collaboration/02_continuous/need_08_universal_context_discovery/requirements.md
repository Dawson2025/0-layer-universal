# Need: Universal Context Discovery (CLAUDE.md & .claude/ Everywhere)

**Branch**: [02_continuous](../)
**Question**: "Can AI tools find and load context files from any location on any computer in any system state?"
**Related Needs**: need_06_universal_rules_and_cross_device_access, need_01_tool_portable, need_02_session_resilient
**Related Feature**: feature_universal_context_hierarchy.md

---

## Definition

AI tools must be able to discover and load CLAUDE.md and .claude/ context files from **any starting location on the filesystem, in any system state, on any machine**, enabling seamless context availability without requiring users to navigate to specific directories or maintain perfect directory structures.

---

## Why This Matters

- **Accessibility**: Users shouldn't need to know where context files are located
- **Portability**: Context discoverable from any directory, any filesystem
- **Resilience**: Context available even if normal filesystem paths corrupted
- **Recovery**: Tools work the same way in recovery mode as normal operation
- **Cross-Machine**: Same discovery works on laptop, desktop, workstation, or VPS
- **New Sessions**: New AI sessions automatically find complete context without setup
- **Tool Agnostic**: Discovery works for any AI tool, not just Claude Code

---

## Requirements

### Discovery Protocol - Standard Search Paths

- MUST support discovery from current directory and walk UP directory tree
- MUST support discovery from home directory (~/.claude/)
- MUST support discovery from system locations (/etc/claude/, /opt/claude/)
- MUST support discovery from recovery partition (/mnt/recovery/etc/claude/)
- MUST support discovery from environment variables ($CLAUDE_SYSTEM_PATH)
- MUST support discovery from git config (git config claude.systemPath)
- MUST load ALL found CLAUDE.md files in cascade order
- MUST merge .claude/ folders from multiple locations into complete context

### Discovery from Any Starting Location

- MUST work if started from deep nested directory (e.g., /home/dawson/a/b/c/d/e/project/)
- MUST work if started from /tmp or /var or any system location
- MUST work if started from root directory (/)
- MUST work if started from a directory outside normal project structure
- MUST not fail if CLAUDE.md not in exact parent directories
- MUST have sensible fallback behavior if no context found

### Discovery in Different System States

- MUST work in normal operation
- MUST work in recovery/emergency mode with minimal filesystem
- MUST work if main filesystem is read-only or corrupted
- MUST work if boot process is interrupted
- MUST work with degraded filesystem (some partitions unavailable)
- MUST have offline access to pre-cached context

### Context Cascade & Merging

- MUST load context from multiple levels:
  - Current directory walk
  - User home directory
  - System-wide locations
  - Recovery partition
  - Network locations
- MUST merge CLAUDE.md files into complete context hierarchy
- MUST have clear precedence when same configuration appears at multiple levels
- MUST handle conflicts: local overrides system-wide, but not vice versa
- MUST preserve .claude/ folder hierarchy when merging

### System-Wide Context Locations

- MUST create and maintain /etc/claude/CLAUDE.md (system context)
- MUST create and maintain /opt/claude/CLAUDE.md (tool-specific context)
- MUST create and maintain /root/.claude/ (emergency/root access)
- MUST ensure proper permissions: readable by all users, writable only by admin
- MUST make locations FHS-compliant and well-documented

### Recovery Partition Context

- MUST store full CLAUDE.md + .claude/ on recovery partition
- MUST compress Layer 0/1/-1 context into tar.gz archives on recovery
- MUST make recovery context read-only and immutable
- MUST ensure recovery context is discoverable by tools in recovery mode
- MUST sync recovery context weekly with primary system

### Multi-Location Synchronization

- MUST define synchronization strategy across 5 tiers:
  - Tier 1: Fast access (local Syncthing-synced)
  - Tier 2: Recovery partition (immutable copies)
  - Tier 3: External backups (USB write-protected, Cloud versioned)
  - Tier 4: Live boot USB (pre-cached full system)
  - Tier 5: Network recovery (NFS accessible)
- MUST automatically sync context changes to all tiers
- MUST verify checksums after each sync
- MUST detect and resolve sync conflicts
- MUST maintain version history for recovery

### Context Loader Implementation

- MUST provide discovery implementation in multiple languages:
  - Bash script: load_claude_context.sh
  - Python library: context_loader.py
  - Available to any AI tool regardless of implementation language
- MUST make loader available in public repository for tools to use
- MUST document loader API for tool developers
- MUST support both CLI invocation and library inclusion

### Context Validation & Health Checks

- MUST verify context files exist and are readable
- MUST validate CLAUDE.md YAML/Markdown syntax
- MUST check for corruption in context files
- MUST detect stale context (not recently synced)
- MUST warn if critical context missing
- MUST have fallback behavior for degraded contexts

### Tool Integration

- MUST allow Claude Code CLI to use discovery protocol
- MUST allow other AI tools to use discovery protocol
- MUST provide adapter layer for tool-specific context formats
- MUST maintain backward compatibility with existing tools
- MUST not require tools to be modified to use discovery

---

## Acceptance Criteria

- [ ] Discovery protocol documented and implemented
- [ ] Discovery works from 10 different start locations
- [ ] Context found from current directory + walk UP
- [ ] Context found from ~/.claude/
- [ ] Context found from /etc/claude/, /opt/claude/
- [ ] Context found from recovery partition (/mnt/recovery/)
- [ ] Context loader available (Bash and Python)
- [ ] Context loader used successfully by multiple tools
- [ ] All 5 tiers in sync and verified
- [ ] Recovery partition context accessible and immutable
- [ ] System-wide locations (/etc/, /opt/, /root/.claude/) created with proper permissions
- [ ] Synchronization script runs weekly automatically
- [ ] Context merge strategy tested: multiple levels resolve correctly
- [ ] Recovery mode tested: context accessible from recovery environment
- [ ] Checksums validate after each sync
- [ ] Documentation: how to add context at new locations
- [ ] Documentation: how AI tools can use discovery protocol

---

## Integration Points

This need integrates with and enhances:

- **need_07_resilient_system_state**: Discovery depends on resilient storage of context
- **need_06_universal_rules_and_cross_device_access**: Rules discoverable everywhere
- **need_01_tool_portable**: Tools portable because context follows them
- **need_02_session_resilient**: Context persists across sessions
- **need_05_cross_platform**: Discovery works across all platforms

---

## Technical Considerations

### Discovery Search Order

```
1. Check current directory: ./CLAUDE.md
2. Walk UP: ../CLAUDE.md, ../../CLAUDE.md, etc.
3. Check home: ~/.claude/CLAUDE.md
4. Check system: /etc/claude/CLAUDE.md
5. Check system: /opt/claude/CLAUDE.md
6. Check environment: $CLAUDE_SYSTEM_PATH/CLAUDE.md
7. Check recovery: /mnt/recovery/etc/claude/CLAUDE.md
8. Check git config: git config --get claude.systemPath
9. Fallback: Minimal Layer 0 rules if nothing found
```

### Context Merge Strategy

```
User Level (~/.claude/)
  ↓ (merged with, overrides)
System Level (/etc/claude/, /opt/claude/)
  ↓ (merged with, overrides)
Recovery Level (/mnt/recovery/etc/claude/)
  ↓ (merged with, fallback)
Minimal Layer 0 (built-in defaults)
```

### File Structure After Implementation

```
~/.claude/                                ← User global
├── CLAUDE.md                              ✓ Already exists
├── discovery.json                         [CREATE]
└── (all other existing files)

/etc/claude/                               [CREATE]
├── CLAUDE.md                              [CREATE]
├── agnostic.md                            [CREATE]
└── shared_settings.json                   [CREATE]

/opt/claude/                               [CREATE]
├── CLAUDE.md                              [CREATE]
├── .claude/settings.json                  [CREATE]
└── README.md                              [CREATE]

/root/.claude/                             [CREATE]
├── CLAUDE.md                              [CREATE]
├── EMERGENCY_RULES.md                     [CREATE]
└── settings.json                          [CREATE]

/mnt/recovery/etc/claude/                  [CREATE]
├── CLAUDE.md                              [CREATE - immutable]
├── Layer_0_context.tar.gz                 [CREATE - immutable]
└── Layer_1_context.tar.gz                 [CREATE - immutable]

Scripts:
├── load_claude_context.sh                 [CREATE]
├── sync_context_everywhere.sh             [CREATE]
└── validate_context_sync.sh               [CREATE]
```

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Multiple contexts with conflicting rules** | Define clear merge precedence, local overrides system |
| **Stale recovery partition context** | Weekly sync script verifies and updates recovery |
| **Tool can't find any context** | Minimal fallback: Layer 0 rules always available |
| **Permission issues on /etc/claude/** | Set proper permissions during initial setup |
| **Context not in sync across tiers** | Weekly validation script checks all copies |

---

## Dependencies

### Blocking Dependencies
- ✓ `need_07_resilient_system_state`: Context must be stored resiliently
- ✓ Phase 0 of resilience: Sync conflicts must be resolved first

### Dependent Features
- `need_09_universal_ai_tool_access`: Needs this discovery to work
- All AI tools accessing system from recovery mode
- Cross-machine context sync with tool switching

---

## Timeline (Parallel with Resilience, Weeks 2-6)

```
Week 2-3:  Phase 1 (System-wide locations) - create /etc/claude/, etc.
Week 3-4:  Phase 2 (Discovery protocol) - implement loaders
Week 4-5:  Phase 3 (Recovery partition) - add context to recovery
Week 5-6:  Phase 4 (Synchronization) - script to sync everywhere
```

---

## Related Documents

- [`feature_universal_context_hierarchy.md`](../../../requests/feature_universal_context_hierarchy.md): Detailed feature specification
- [`system_context_hierarchy_research.md`](../../stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/system_context_hierarchy_research.md): Research findings
- [`need_07_resilient_system_state`](./need_07_resilient_system_state/): Underlying resilience infrastructure
- [`need_06_universal_rules_and_cross_device_access`](./need_06_universal_rules_and_cross_device_access/): Universal rules requirement

---

## Related User Requests

**From Dawson (2026-01-27):**
- "Can CLAUDE.md and .claude/ be accessible from any location on the filesystem?"
- "Should work in recovery mode and if filesystem is corrupted"
- "Should work across multiple machines"
- "Tools shouldn't need to know where context files are located"
