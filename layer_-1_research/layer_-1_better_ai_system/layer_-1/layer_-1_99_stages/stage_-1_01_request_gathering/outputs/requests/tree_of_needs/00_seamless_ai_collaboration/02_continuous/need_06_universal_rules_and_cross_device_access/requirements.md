# Need: Universal Rules and Cross-Device AI System Access

**Branch**: [02_continuous](../)
**Question**: "How does AI access and respect universal rules across all contexts, users, machines, and emergency scenarios?"

---

## Definition

The AI system should maintain consistent universal rules and provide seamless access to the AI infrastructure regardless of:
- Which user account is logged in
- Which area of the filesystem is being accessed
- The computer's operational state (normal, emergency/recovery mode)
- Which physical machine is being used
- Network connectivity status

---

## Why This Matters

- **Rule Consistency**: Universal principles should apply everywhere, not just some places
- **User Independence**: Any user on any machine should be able to work with the AI system
- **Robustness**: System should work even when the computer is in emergency/recovery mode
- **Seamless Multi-Device**: Work on laptop today, desktop tomorrow, with same context
- **Accessibility**: AI system shouldn't be locked to one account or location
- **Reliability**: Core rules should be accessible even if normal filesystem or permissions are corrupted

---

## Requirements

### Universal Rules Across All Accounts

- MUST define universal AI rules that apply to ANY user on the system
- MUST store universal rules in a location accessible to all user accounts
- MUST load universal rules regardless of which user is logged in
- MUST ensure universal rules supersede user-specific rules when there's conflict
- MUST prevent any user from accidentally or intentionally disabling universal rules
- SHOULD log when users access or invoke universal rules (for auditing)

### Universal Rules Across Filesystem

- MUST have universal AI rules available at `/` level (root filesystem)
- MUST have universal rules in FHS-compliant locations (`/etc/`, `/opt/`, etc.)
- MUST load universal rules regardless of current working directory
- MUST ensure AI respects universal rules whether in `/home/`, `/opt/`, `/etc/`, or emergency environments
- MUST make universal rules immutable during normal operation (require sudo to change)
- MUST not require user to navigate to specific directory to access rules

### Universal Rules in Emergency/Recovery Mode

- MUST preserve universal rules even if main filesystem is damaged
- MUST store rules in recoverable locations (backup partitions, read-only if possible)
- MUST have universal rules accessible in Ubuntu recovery/advanced options mode
- MUST have universal rules available even if system can't fully boot
- MUST support recovery mode access with minimal dependencies
- SHOULD have emergency-mode-specific behavior that still respects core rules

### Universal Rules Across Machines

- MUST define machine-agnostic universal rules (apply to all machines)
- MUST support machine-specific rule overrides when needed
- MUST synchronize core rules across multiple machines (laptops, desktops, VPS, etc.)
- MUST handle cases where machines diverge (new rules added on one machine)
- MUST have conflict resolution when different machines have conflicting rules
- SHOULD use version control or sync mechanism for rule distribution

### Cross-Device AI System Access

- MUST make the AI system accessible from any machine the user owns
- MUST synchronize the AI system configuration across devices
- MUST provide remote access to skills, prompts, and memories from other machines
- MUST handle authentication/authorization for cross-device access
- MUST support offline operation with later sync when devices connect
- MUST maintain consistency of AI system state across devices

### Skills and Memories Access Across Devices

- MUST enable AI tools on any machine to access skills from the central AI system
- MUST enable AI tools to access memories/learnings from sessions on other machines
- MUST support querying shared memories from any connected device
- MUST handle conflicts when same skill/memory is modified on multiple devices
- MUST preserve decision history and learnings regardless of which machine was used
- SHOULD prioritize syncing of critical rules and memories

### Location of Universal Rules

- MUST place universal rules in FHS-compliant locations:
  - `/etc/claude/` or `/etc/ai-system/` for system config
  - `/opt/claude/` or `/opt/ai-system/` for system-wide AI tool
  - `/root/.claude/` for root-level (emergency) access
- MUST have redundant copies in recoverable locations
- MUST make rules readable by all users but modifiable only by sudo/admin
- MUST support both system-wide install and user-specific overrides

### Multi-User Considerations

- MUST apply universal rules to all user accounts (`/home/alice/`, `/home/bob/`, etc.)
- MUST support each user having personal memories while sharing universal rules
- MUST prevent one user's activities from breaking another user's AI access
- MUST audit which user invoked which rule (for accountability)
- MUST handle permissions: universal rules override per-user configs

### Cross-Platform Context

- MUST support same AI system on Linux, Windows (WSL), macOS
- MUST handle different filesystem structures on different OS's
- MUST store universal rules in portable format (not OS-specific paths)
- MUST provide platform-specific access paths but unified rules
- SHOULD abstract OS differences from rule definitions

---

## Acceptance Criteria

- [ ] Universal rules defined and documented
- [ ] Rules stored in `/etc/`, `/opt/`, and recoverable locations
- [ ] All users on system can access universal rules
- [ ] Universal rules load automatically regardless of working directory
- [ ] Emergency/recovery mode has access to universal rules
- [ ] Rules accessible via multiple machines (synced via git or Syncthing)
- [ ] Skills accessible from any machine with proper authentication
- [ ] Memories/learnings queryable across machines
- [ ] Cross-device sync mechanism implemented
- [ ] Conflict resolution tested for multi-device scenarios
- [ ] Universal rules tested in recovery mode
- [ ] Documentation: where rules are, how to access, how to override

---

## Integration Points

This need integrates with and enhances:

- **need_02_session_resilient**: Rules should persist across sessions and machines
- **need_05_cross_platform**: Rules apply across OS platforms
- **need_03_tool_portable**: AI tools portable because rules follow them
- **03_trustworthy/need_01_rule_compliant**: Rules are universally compliant
- **01_capable/need_02_scalable_context**: Shared context across devices

---

## Technical Considerations

### Storage Locations
```
/etc/claude/UNIVERSAL_RULES.md          ← System-wide, readable by all
/etc/claude/settings.json               ← Config for all users
/opt/claude/shared_rules/               ← Shared prompts/skills
~/.claude/PERSONAL_OVERRIDES.md         ← Per-user customizations
/root/.claude/EMERGENCY_RULES.md        ← Root/emergency access
/var/opt/claude/shared_memories/        ← Shared learnings/cache
```

### Multi-Device Sync
```
Device A (laptop)
  ├── Local AI system
  └── Syncs to git repo / Syncthing folder

Device B (desktop)
  ├── Local AI system
  └── Pulls from same repo / folder

Central storage (git, Syncthing, etc.)
  └── Single source of truth for core rules & memories
```

### Access Control
```
Universal Rules
  ├── Readable by: all users
  ├── Writable by: sudo/admin only
  └── Override by: user-specific files (if allowed)

Shared Memories
  ├── Readable by: all users
  ├── Writable by: user who created + admin
  └── Queryable by: all users
```

---

## Open Questions

1. **How to handle rule conflicts across devices?** (Last-write-wins? Merge? Manual conflict resolution?)
2. **Authentication for cross-device access?** (SSH keys? Shared password? Biometric?)
3. **Which rules should be truly universal vs. machine-specific?** (Bootstrap first with core rules, extend later)
4. **How to access AI system in recovery mode?** (Needs testing with actual Ubuntu recovery environment)
5. **Backup strategy for universal rules?** (Should they be on separate partition? Redundant copies?)

---

## Related Needs

- `need_01_tool_portable` - Rules must be portable with the tool
- `need_02_session_resilient` - Rules survive session transitions
- `need_05_cross_platform` - Rules work across platforms
- `03_trustworthy/need_01_rule_compliant` - AI respects rules universally
- `01_capable/need_02_scalable_context` - Shared context across contexts

---

## Related User Requests

**From Dawson (2026-01-27):**
- "Whenever I'm on this computer, no matter which account I'm on, there will be universal rules that apply"
- "No matter which area within the filesystem I am currently in"
- "Even if the computer should have problems, use one of the emergency modes"
- "Regardless of which machine I'm on, certain universal rules apply"
- "Regardless of the machine I'm currently on, AI tools can access my system, traverse through it, use skills and memories"
