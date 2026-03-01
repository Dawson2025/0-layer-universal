# Feature Request: Universal Context Hierarchy (CLAUDE.md & .claude/ Everywhere)

**Status**: Under Request Gathering
**Priority**: HIGH (Depends on: Feature: Full System Resilience)
**Related**: `need_06_universal_rules_and_cross_device_access`, `system_context_hierarchy_research.md`
**Project**: better_ai_system

---

## Overview

Make AI system context files (CLAUDE.md, agnostic.md, .claude/ folders) accessible and loadable by AI tools from **every location on the filesystem and every system state**, regardless of:

- Where the computer is in the directory tree
- What machine the user is on
- Whether the system is in recovery mode
- Whether storage is corrupted or degraded
- Whether the system is online or offline
- What AI tool is being used

**Result**: Any AI tool can load complete contextual knowledge from the system from anywhere, always.

---

## What Is It?

A distributed context system ensuring:

```
What You Have:
├── CLAUDE.md files at multiple levels (already done)
│   ├── /home/dawson/CLAUDE.md
│   ├── /home/dawson/dawson-workspace/CLAUDE.md
│   ├── /home/dawson/dawson-workspace/code/CLAUDE.md
│   ├── /home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
│   └── [many more at layer/stage levels]
│
├── agnostic.md files (already done)
│   └── [mirrors of CLAUDE.md structure]
│
├── .claude/ folders at key levels (partially done)
│   ├── ~/.claude/               ← User global
│   └── /home/dawson/.../.claude/ ← Project level
│
└── Other config (settings.json, skills, agents)

What's Missing:
├── Accessible from ALL locations
├── Accessible in ALL system states
├── Cached/replicated to recovery partitions
├── Accessible via multiple paths
└── Tool-agnostic loading mechanism
```

---

## Why?

### Current Limitation
- CLAUDE.md cascade works ONLY if located in correct directory hierarchy
- If filesystem corrupts, context files inaccessible
- If starting from non-standard location, context may be incomplete
- No fallback if standard locations unavailable

### Requirements Driving This
From System Context Hierarchy Research:
- Claude Code loads context from ~/.claude/CLAUDE.md and walks UP tree
- **Problem**: Doesn't walk DOWN (can't access child context)
- **Problem**: No recovery partition fallback
- **Problem**: If main filesystem corrupted, context inaccessible

### Real-World Scenarios

**Scenario 1: Recovery Mode**
```
Normal: /home/dawson/code/project/ → Claude Code loads context
Recovery: System boots to recovery partition, no /home directory
Problem: Where are CLAUDE.md files? Can't find them!
Solution: CLAUDE.md also stored in recovery partition, accessible
```

**Scenario 2: Different Machine**
```
Machine A: Syncthing synced system
Machine B: Joins network, needs to start Claude Code
Problem: Different filesystem paths, can't locate CLAUDE.md
Solution: .stignore file + universal discovery protocol
```

**Scenario 3: Non-Standard Start Location**
```
Start: /home/dawson/dawson-workspace/code/0_layer_universal/layer_0_group/layer_0_04_rules/
Need: Universal rules, project context
Problem: Walking UP from this location gets layer_0 specific, not projects
Solution: Explicit context registry accessible from anywhere
```

---

## Scope: 3 Components

### Component 1: Multi-Location Context Storage
**Ensure CLAUDE.md exists at every strategic location**

```
Current (mostly done):
├── ~/.claude/                      ✓ User global
├── /home/dawson/                  ✓ User root
├── /home/dawson/dawson-workspace/ ✓ Workspace
├── /home/dawson/dawson-workspace/code/ ✓ Code root
├── .../0_layer_universal/         ✓ System root
├── .../layer_0_group/                   ✓ Universal layer
├── .../layer_1/                   ✓ Projects layer
├── .../layer_-1_research/         ✓ Research layer
├── .../layer_0_99_stages/         ✓ Stages container
└── .../stage_-1_XX_*/             ✓ Individual stages

System-Wide (needs to be added):
├── /etc/claude/CLAUDE.md          ← System config
├── /etc/opt/claude/               ← System-wide settings
├── /opt/claude/                   ← System tool location
└── /var/opt/claude/               ← Runtime context
```

### Component 2: Context Discovery & Loading Protocol
**How tools find CLAUDE.md from any location**

```
Tool starts at: /some/random/location/

Discovery Sequence:
1. Check current directory for CLAUDE.md
2. Walk UP directories looking for CLAUDE.md
   /some/random/CLAUDE.md?
   /some/CLAUDE.md?
   /CLAUDE.md?
3. Check standard locations:
   ~/.claude/CLAUDE.md?
   /home/USERNAME/CLAUDE.md?
   /home/USERNAME/workspace/CLAUDE.md?
4. Check system locations:
   /etc/claude/CLAUDE.md?
   /etc/opt/claude/CLAUDE.md?
5. Check environment variables:
   $CLAUDE_SYSTEM_PATH?
   $CLAUDE_CONTEXT_DIR?
6. Check recovery locations:
   /mnt/recovery/etc/claude/CLAUDE.md?
   /mnt/recovery_partition/CLAUDE.md?
7. Fallback: Check git config
   git config --get claude.systemPath?

Load ALL found CLAUDE.md files (context cascades)
```

### Component 3: Resilient Storage & Replication
**Ensure context survives system failures**

```
CLAUDE.md & .claude/ locations:

Tier 1 (Fast Access):
├── ~/.claude/
├── /home/dawson/.../
└── Syncthing synced

Tier 2 (Recovery Partition):
├── /mnt/recovery/etc/claude/
├── /mnt/recovery/.../CLAUDE.md
└── Read-only, immutable

Tier 3 (External Backup):
├── External USB: all CLAUDE.md + .claude/ (write-protected)
└── Cloud: all CLAUDE.md + .claude/ (versioned)

Tier 4 (Live Boot USB):
├── Pre-loaded CLAUDE.md + .claude/ on USB
└── Accessible immediately from boot

Tier 5 (Network Recovery):
├── NFS server with all context
└── Accessible via network boot
```

---

## Implementation Phases

### Phase 1: System-Wide Context Locations
Create CLAUDE.md files at FHS-compliant locations:

```
/etc/claude/CLAUDE.md
├── Role: System-wide context
├── Audience: All users, all tools
├── Content: Universal rules applicable system-wide
└── Permissions: Readable by all, writable by admin

/opt/claude/CLAUDE.md
├── Role: Claude tool system context
├── Audience: All users, Claude tool
└── Location: Near Claude tool installation

/var/opt/claude/.claude/settings.json
├── Role: Runtime configuration
├── Audience: Tools during execution
└── Content: Dynamic configuration

/root/.claude/CLAUDE.md
├── Role: Emergency/recovery context
├── Audience: Root user, recovery mode
└── Content: Critical rules that survive damage
```

### Phase 2: Context Discovery Protocol
Define and implement discovery mechanism:

```
Create: ~/.claude/discovery.json
{
  "system_context_paths": [
    "~/.claude",
    "/etc/claude",
    "/etc/opt/claude",
    "/opt/claude",
    "$CLAUDE_SYSTEM_PATH"
  ],
  "search_order": [
    "local_directory_walk",
    "user_home",
    "system_locations",
    "environment_variables",
    "recovery_partition",
    "git_config"
  ],
  "fallback": "use_layer_0_rules_minimal"
}
```

Implement in: Context loader (any tool, any language)
- Bash script: `load_claude_context.sh`
- Python library: `claude_context.py`
- Go package: `claudiore` or similar
- Available in: Git repo for any tool to use

### Phase 3: Recovery Partition Context
Store full context on recovery partition:

```
Recovery partition contents:

/mnt/recovery/etc/claude/
├── CLAUDE.md (root manager)
├── Layer_0_context.tar.gz (universal rules, compressed)
├── Layer_1_context.tar.gz (projects, compressed)
└── Layer_-1_context.tar.gz (research, compressed)

/mnt/recovery/.claude/
├── settings.json
├── skills/ (essential skills)
├── agents/ (recovery agents)
└── commands/ (recovery commands)

During recovery mode:
Tool mounted at recovery → Reads /mnt/recovery/etc/claude/CLAUDE.md
→ Has full system context in recovery mode
```

### Phase 4: Multi-Location Synchronization
Ensure all locations stay in sync:

```
Synchronization Model:

Primary: /home/dawson/.../.claude/ (Syncthing synced)
  ↓ (Syncthing)
Secondary: Other machines
  ↓ (Git push on changes)
Backup: Git repo
  ↓ (Deployment script)
System: /etc/claude/, /opt/claude/
  ↓ (Deployment script)
Recovery: /mnt/recovery/etc/claude/
  ↓ (Backup script)
External: USB backup, Cloud S3
```

Script: `sync-context-everywhere.sh`
- Runs weekly
- Copies context to all locations
- Verifies checksums
- Updates recovery partition
- Pushes to cloud

---

## Success Criteria

### Phase 1 Complete
- [ ] /etc/claude/CLAUDE.md exists with system context
- [ ] /opt/claude/CLAUDE.md exists with tool context
- [ ] /root/.claude/ exists with emergency context
- [ ] All readable by appropriate users

### Phase 2 Complete
- [ ] Discovery protocol documented
- [ ] Context loader implemented (at least Bash, Python)
- [ ] Tools can discover CLAUDE.md from any location
- [ ] Tests: 10 different start locations all find context

### Phase 3 Complete
- [ ] Recovery partition contains full CLAUDE.md + .claude/
- [ ] Accessible in recovery mode (tested)
- [ ] Immutable (read-only)
- [ ] Tests: Boot recovery, verify context accessible

### Phase 4 Complete
- [ ] Synchronization script created and tested
- [ ] All 5 tiers (fast, recovery, external, USB, network) in sync
- [ ] Runs weekly automatically
- [ ] Tests: Verify all locations have current context

### System Integration Complete
- [ ] Any AI tool can find and load context from anywhere
- [ ] Context available in normal, recovery, and degraded modes
- [ ] Cross-machine context sync works
- [ ] Tool switching preserves context
- [ ] Documentation complete

---

## Architecture Diagram

```
AI Tool Request:
  "Load context for this task"
       ↓
Discovery Protocol:
  Search in order:
  1. Current directory
  2. Walk up tree
  3. Home directory
  4. System locations
  5. Recovery partition
  6. Network locations
       ↓
Context Loader:
  Found CLAUDE.md files aggregate into:
  ├── Universal rules (Layer 0)
  ├── Project context (Layer 1)
  ├── Research context (Layer -1)
  ├── Tool configuration (.claude/)
  └── Skills & agents
       ↓
Cascade Resolution:
  If Layer 1 not found → Use only Layer 0
  If recovery partition → Use read-only copies
  If network → Use NFS mounted copies
  If offline → Use pre-cached copies
       ↓
Tool Uses Context:
  Claude Code: Parse CLAUDE.md
  Copilot: Use access API
  Gemini: Query context database
  clawdbot: Load from Discord config
```

---

## File Structure After Implementation

```
Filesystem Level (Current + New):

~/.claude/                          ← User global
├── CLAUDE.md                       ✓ Already
├── agnostic.md                     ✓ Already
├── discovery.json                  [CREATE]
├── settings.json                   ✓ Already
├── skills/                         ✓ Already
├── agents/                         ✓ Already
└── commands/                       ✓ Already

/home/dawson/CLAUDE.md              ✓ Already
/home/dawson/agnostic.md            ✓ Already
/home/dawson/dawson-workspace/CLAUDE.md ✓ Already
/home/dawson/dawson-workspace/agnostic.md ✓ Already
/home/dawson/dawson-workspace/code/CLAUDE.md ✓ Already
...
(All layer/stage CLAUDE.md files as created)

System Level (New):

/etc/claude/                        [CREATE]
├── CLAUDE.md                       [CREATE]
├── agnostic.md                     [CREATE]
├── universal_rules.yaml            [CREATE]
└── shared_settings.json            [CREATE]

/etc/opt/claude/                    [CREATE]
├── system_config.json              [CREATE]
└── security_policies.yaml          [CREATE]

/opt/claude/                        [CREATE]
├── CLAUDE.md                       [CREATE]
├── .claude/settings.json           [CREATE]
└── README.md                       [CREATE]

/var/opt/claude/                    [CREATE]
├── runtime_state.json              [CREATE]
├── cache/                          [CREATE]
└── logs/                           [CREATE]

/root/.claude/                      [CREATE]
├── CLAUDE.md                       [CREATE]
├── EMERGENCY_RULES.md              [CREATE]
└── settings.json                   [CREATE]

Recovery Partition (New):

/mnt/recovery/etc/claude/           [CREATE]
├── CLAUDE.md                       [CREATE - read-only]
├── Layer_0_context.tar.gz          [CREATE - read-only]
├── Layer_1_context.tar.gz          [CREATE - read-only]
└── Layer_-1_context.tar.gz         [CREATE - read-only]

Scripts (New):

~/scripts/
├── load_claude_context.sh          [CREATE]
├── sync_context_everywhere.sh      [CREATE]
└── validate_context_sync.sh        [CREATE]

Libraries (New):

~/lib/
├── context_loader.py               [CREATE]
└── context_loader.sh               [CREATE]
```

---

## Benefits

### For Users
- AI context accessible from anywhere on system
- No more "CLAUDE.md not found" errors
- Consistent context in recovery mode
- Works offline with pre-cached context

### For Tool Developers
- Standardized way to find/load context
- Works with any CLAUDE.md structure
- Fallback mechanism prevents failures
- Easy to integrate discovery protocol

### For System Resilience
- Context survives filesystem corruption
- Available in recovery mode
- Multi-location redundancy
- Cross-machine accessible

### For AI Tools
- Can focus on work, not finding context
- Automatic context loading
- Graceful degradation
- Tool-agnostic design

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| **Context in sync conflicts** | Phase 0 (sync conflict resolution) completes first |
| **Stale context in recovery** | Weekly sync script verifies currency |
| **Permission issues on /etc/claude/** | Set proper permissions during setup |
| **Tool can't find any context** | Minimal fallback: Layer 0 rules always available |
| **Multiple CLAUDE.md versions conflict** | Merge strategy defined, winner selected by precedence |

---

## Dependencies

### Blocking Dependencies
- ✓ `feature_resilience_system`: Context must be stored resiliently
- ✓ Phase 0: Sync conflicts must be resolved first

### Dependent Features
- `feature_universal_ai_tool_access`: Needs this context hierarchy working
- All AI tools accessing system
- Cross-machine context sync

---

## Timeline (Parallel with Resilience)

```
Week 2-3:  Phase 1 (System-wide locations) - create /etc/claude/, etc.
Week 3-4:  Phase 2 (Discovery protocol) - implement loaders
Week 4-5:  Phase 3 (Recovery partition) - add context to recovery
Week 5-6:  Phase 4 (Synchronization) - script to sync everywhere
Week 6-7:  Testing & validation - verify all 5 tiers in sync
```

---

## Related Documents

- [`system_context_hierarchy_research.md`](../../stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/system_context_hierarchy_research.md): Research findings
- [`ai_context_filesystem_locations.md`](../../stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/ai_context_filesystem_locations.md): Filesystem location research
- [`feature_resilience_system.md`](feature_resilience_system.md): Underlying resilience
- [`feature_universal_ai_tool_access.md`](feature_universal_ai_tool_access.md): Requires this

---

## Vision: The Ideal End State

```
AI Tool (any tool, any location):
  "I need context for this task"

System:
  1. Checks current directory
  2. Walks up directory tree
  3. Checks home directory
  4. Checks /etc/claude/
  5. Checks recovery partition
  6. Checks network

Result:
  CLAUDE.md found (from one of 5 locations)
  ↓
  .claude/ folder loaded
  ↓
  Layer 0, 1, -1 context loaded
  ↓
  Tool has COMPLETE context
  ↓
  Tool can work fully

No matter:
  - What directory tool starts from
  - What machine tool is on
  - Whether main storage corrupted
  - Whether in recovery mode
  - Whether offline (if cached)

Result: Seamless context availability everywhere
```

---

## Next Steps

1. **Stage 01 (This stage)**: Document requirements ← YOU ARE HERE
2. **Stage 02**: Research context distribution patterns
3. **Stage 03**: Define discovery protocol specification
4. **Stage 04**: Design system-wide context architecture
5. **Stage 05**: Plan creation of system-wide locations
6. **Stage 06**: Implement discovery protocol + sync scripts
7. **Stage 07**: Test context access from all locations
8. **Stage 08**: Review and critique
9. **Stage 09**: Fix issues
10. **Stage 10**: Final integrated context system
11. **Stage 11**: Archive and future enhancements

