---
resource_id: "3f91b3df-ebe8-4da2-ab4c-139c9d598275"
resource_type: "output"
resource_name: "ai_context_filesystem_locations"
---
# AI Context Files Across the Linux Filesystem

**Status**: Active Research
**Date Started**: 2026-01-27
**Related Research**: `system_context_hierarchy_research.md`

---

<!-- section_id: "103b2031-798a-48de-912a-41f72f290d77" -->
## Overview

Research into where CLAUDE.md and .claude/ folders can be placed throughout the Linux filesystem hierarchy, beyond the user's home directory.

<!-- section_id: "bdab4771-fa51-4d10-aea9-a2784aa4ff2a" -->
## Current Implementation

Currently, we've placed context files only in `/home/dawson/` and subdirectories:
```
/home/dawson/CLAUDE.md
/home/dawson/CLAUDE.md
/home/dawson/dawson-workspace/CLAUDE.md
/home/dawson/dawson-workspace/code/CLAUDE.md
/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
└── [and layer directories]
```

**Why**: Personal development, single-user workspace, confined to home directory.

<!-- section_id: "85cd87ac-d27d-464c-803c-6057d8ed2fbd" -->
## Other Beneficial Locations

According to FHS (Filesystem Hierarchy Standard), context files could also go in:

<!-- section_id: "42dc56c1-bda1-4fd5-bbcf-98d84f7d77fd" -->
### `/opt/<package>/` - System-Wide Third-Party Software

**Purpose**: Install AI tools system-wide for sharing across users

**Structure**:
```
/opt/claude/
├── CLAUDE.md                    ← Shared AI context for the tool
├── .claude/
│   ├── settings.json
│   ├── prompts/
│   ├── agents/
│   └── skills/
├── bin/                         ← Executables
├── lib/                         ← Libraries
└── README.md
```

**Use Cases**:
- Claude Code installed as a system-wide service
- Multiple users need access to the same AI tool
- Shared prompts/settings across the organization
- Third-party AI tools bundled by vendor

**Example**: `/opt/anthropic/claude/CLAUDE.md` for enterprise Claude deployment

<!-- section_id: "fe89fdaa-b9c8-4c2d-8ace-7eb091bbd2a4" -->
### `/etc/opt/<package>/` - System Config for /opt Tools

**Purpose**: Persistent, system-wide configuration that survives reboots

**Structure**:
```
/etc/opt/claude/
├── settings.json                ← System-wide settings
├── security.conf                ← Policies
└── shared_prompts.md            ← Org-wide prompts
```

**Use Cases**:
- Configuration readable by services/daemons
- Settings that apply to all users
- Security policies for AI tool usage
- Organization-wide guidelines

**Permissions**: Typically read-only for regular users, writable by admin

<!-- section_id: "28488d6f-aa52-48ba-9873-24ca4524bbbb" -->
### `/var/opt/<package>/` - Runtime Data for /opt Tools

**Purpose**: Dynamic data that changes at runtime, preserved across reboots

**Structure**:
```
/var/opt/claude/
├── cache/                       ← Model cache, session data
├── logs/                        ← Operation logs
├── sessions/                    ← User sessions
└── state/                       ← Current state data
```

**Use Cases**:
- Session logs for auditing
- Cached model outputs
- User state information
- Runtime performance data

**Difference from `/tmp`**: `/var/opt/` persists across reboots; `/tmp/` is cleared

<!-- section_id: "de117bdb-2b35-4494-a76b-33bd3c997508" -->
### `/usr/local/share/` - Local Admin Installs

**Purpose**: Custom documentation and data for tools installed locally

**Structure**:
```
/usr/local/share/claude/
├── CLAUDE.md                    ← Static docs
├── prompts/                     ← Shared prompts
└── templates/                   ← Reusable templates
```

**Use Cases**:
- Static documentation for all users
- Read-only reference materials
- Templates for local projects
- Accessible to everyone on the system

**Similar**: `/usr/local/etc/` for configs, `/usr/local/bin/` for scripts

<!-- section_id: "8c63b6b9-c86a-4433-818a-e3068bef9268" -->
## Decision Matrix: Where to Put Context Files

| Scenario | Location | Reason |
|----------|----------|--------|
| Personal development (current) | `/home/username/` | Single user, private, controlled |
| System-wide tool install | `/opt/toolname/` | Shared across users, isolated |
| System config for tool | `/etc/opt/toolname/` | Global settings, security policies |
| Runtime data for tool | `/var/opt/toolname/` | Logs, cache, state |
| Local admin templates | `/usr/local/share/` | Shared reference material |
| **NOT** ephemeral temp | `/tmp/` | Gets deleted on reboot |
| **NOT** system configs | `/etc/` | Only for actual config files |
| **NOT** random locations | `/` or elsewhere | Violates FHS, breaks organization |

<!-- section_id: "8347abd2-da04-4115-b65d-83cbeeab7213" -->
## Comparison: /home/username vs /opt

| Aspect | /home/username/ | /opt/ |
|--------|-----------------|-------|
| Scope | Single user | Multiple users / system-wide |
| Ownership | User-controlled | Admin-controlled |
| Permissions | User's group/other restrictions | Everyone can access |
| Updates | User manages | Admin/vendor manages |
| Isolation | Isolated from other users | Shared infrastructure |
| Multi-device sync | Often synced (Syncthing, iCloud) | System-specific |
| Backup | Usually in backup strategy | Depends on admin |

<!-- section_id: "b1003043-73f6-4eff-ba7e-ec3ddde2d058" -->
## Key Findings

1. **FHS separates concerns clearly**:
   - `/opt/` = binaries and package data
   - `/etc/opt/` = persistent configuration
   - `/var/opt/` = runtime/changing data
   - `/usr/local/` = local customizations

2. **Current implementation is correct**:
   - Using `/home/dawson/` for personal development
   - All context files in home directory hierarchy
   - No need for system-wide locations yet

3. **When to expand**:
   - Sharing Claude with other users on same machine
   - Running Claude as a service/daemon
   - Multi-machine deployments
   - Organizational/enterprise setup

4. **Avoid**:
   - `/tmp/` for persistent context (deleted on reboot)
   - Raw `/etc/` for AI contexts (only for configs)
   - Root `/` for new directories (reserved for system)

<!-- section_id: "c19f6deb-352b-462a-ac0d-5d59ab031854" -->
## Future Scenarios

<!-- section_id: "028676c8-5d3b-4acf-a531-99b43ad8002a" -->
### Scenario 1: Multi-User System
If /home/thomas/ and /home/sarah/ exist and need Claude:

```
/opt/claude/                    ← Shared install
/etc/opt/claude/                ← Shared config
/var/opt/claude/                ← Shared logs/cache
```

Each user could have:
```
/home/thomas/.claude/           ← User-specific overrides
/home/sarah/.claude/            ← User-specific overrides
```

<!-- section_id: "8f0dd9d2-8909-4bdf-bf9d-444584f327d7" -->
### Scenario 2: Containerized Claude
If Claude runs in Docker/container:

```
/opt/claude-container/
├── Dockerfile
├── CLAUDE.md                    ← Container's AI context
├── .claude/
└── shared_config/
```

<!-- section_id: "233ecdac-c006-424a-8ee9-d60f0af839b5" -->
### Scenario 3: Claude as Service
If Claude is a system daemon:

```
/opt/claude-service/            ← Service installation
/etc/opt/claude/                ← Service configuration
/var/opt/claude/                ← Service logs
/var/lib/claude/                ← Service state
```

<!-- section_id: "506eec65-a0f1-4f38-8490-bdb944594ef4" -->
## Documentation Needed

- [ ] Best practices for placing context files by use case
- [ ] Permission model for shared vs private contexts
- [ ] Multi-user context inheritance rules
- [ ] Containerization strategies for context files
- [ ] Migration guide: `/home/` → `/opt/` scenarios

<!-- section_id: "7f1d77da-83ca-44c0-bba8-d116e428f899" -->
## References

- Filesystem Hierarchy Standard (FHS)
- Linux Journal - filesystem layout
- FreeDesktop specifications
- Previous research: `system_context_hierarchy_research.md`

<!-- section_id: "ec3cd2db-5a9f-4697-bc35-d10758fc82b6" -->
## Conclusion

For current personal development: **Use `/home/dawson/` structure (already implemented).**

For future expansion: **Know these locations exist and when they apply.**

The hierarchy we built is correct for a single-user, personal development environment. If requirements change (multi-user, system-wide tool, containerization), these other locations provide the proper FHS-compliant alternatives.
