# Claude Code Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 1 (Project)
**Stage**: stage_1.01_instructions

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## Ubuntu-Specific Context for Claude Code at Layer 1 (Project)

This context builds on Layer 0 Universal Ubuntu context and adds project-level considerations.

### Project-Level Ubuntu Considerations
- Project files in home directory: `/home/dawson/code/<project>/`
- Native Linux filesystem performance (ext4, btrfs, xfs)
- Full systemd integration available for background services
- Direct hardware access for specialized projects

### Project Dependencies in Ubuntu
- System packages via APT: `apt install <package>`
- Node.js packages via npm (Linux build)
- Python packages via pip3
- Snap packages for isolated applications
- Build dependencies typically in `build-essential`

### Project Execution Environment
- Development servers run on standard Linux ports
- Database services via systemd or Docker
- File watchers use inotify (native Linux)
- Environment variables in `.env` or systemd unit files

### Ubuntu Service Management
- Use systemd for long-running project services
- Unit files in `/etc/systemd/system/` or `~/.config/systemd/user/`
- Service logs via `journalctl`
- Socket activation available for advanced scenarios

### Project-Specific Paths
- Configuration: `~/.config/<project>/` or `/etc/<project>/`
- Logs: `/var/log/<project>/` or `~/.local/share/<project>/logs/`
- Cache: `~/.cache/<project>/`
- Data: `~/.local/share/<project>/`

---

## Integration Notes

This context file:
- Inherits from Layer 0 Universal Ubuntu context
- Is overridden by Layer 2 (Feature) and Layer 3 (Component) Ubuntu contexts
- Works in conjunction with project-level `AGENTS.md` and `GEMINI.md`

---

## Future Extensions

Add project-level Ubuntu-specific:
- Systemd service templates
- Database configuration patterns
- Reverse proxy setup (nginx, Apache)
- Security hardening for production-like development
