<!-- derived_from: "d39b1b99-83b0-4e73-96b4-22fd8b03e835" -->
# Agent Instructions - Linux Ubuntu Environment

**OS Variant**: Linux Ubuntu (Native)
**Layer**: 1 (Project)
**Stage**: stage_1.01_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## Ubuntu-Specific Context for Worker Agents at Layer 1 (Project)

This context builds on Layer 0 Universal Ubuntu context and adds project-level execution patterns.

### Project-Level Command Execution
- Execute commands from project root: `/home/dawson/code/<project>/`
- Use relative paths within project structure
- Scripts use bash shebang: `#!/bin/bash`
- Check exit codes: `$?` for error handling

### Dependency Installation
- System dependencies: `sudo apt update && sudo apt install <packages>`
- Node.js: `npm install` (use nvm for version management)
- Python: `pip3 install -r requirements.txt` (use venv for isolation)
- Build tools: `sudo apt install build-essential`

### Development Server Operations
- Start servers: `npm start`, `python3 manage.py runserver`, etc.
- Bind to `localhost` or `0.0.0.0` as appropriate
- Use standard ports (3000, 8000, 5000, etc.)
- Check port availability: `lsof -i :<port>`

### Build and Test Commands
- Build: `npm run build`, `make`, `python3 setup.py build`
- Test: `npm test`, `pytest`, `make test`
- Lint: `npm run lint`, `pylint`, `shellcheck`
- All tools are Linux-native (no emulation overhead)

### File Management at Project Level
- Use LF line endings exclusively
- Set permissions appropriately: `chmod +x scripts/*.sh`
- Watch for file descriptor limits on large projects
- Use `.gitignore` to exclude build artifacts

### Environment Variables
- Define in `.env` file (project root)
- Load with `source .env` or via application framework
- System-wide: add to `~/.bashrc` or `~/.profile`
- Systemd services: use `Environment=` directive

### Process Management
- Background tasks: `<command> &`
- Process monitoring: `ps aux | grep <name>`
- Service management: `systemctl --user <start|stop|status> <service>`

---

## Integration Notes

This context file:
- Inherits from Layer 0 Universal Ubuntu agent context
- Is overridden by Layer 2 (Feature) and Layer 3 (Component) Ubuntu contexts
- Provides project-level execution patterns for worker agents

---

## Future Extensions

Add project-level Ubuntu-specific:
- Project build scripts and automation
- Database initialization patterns
- Development environment setup automation
- Testing and CI/CD command patterns
