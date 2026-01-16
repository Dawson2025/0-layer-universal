# Agent Instructions - WSL Environment

**OS Variant**: Windows Subsystem for Linux (WSL)
**Layer**: 1 (Project)
**Stage**: stage_1.01_instructions
**Tool Context**: General Agents (Codex CLI, etc.)

---

## Normative Specification

This file implements the OS-specific context pattern defined in:
- `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

Refer to that document for the canonical specification of the OS variant system.

---

## WSL-Specific Context for Worker Agents at Layer 1 (Project)

This context builds on Layer 0 Universal WSL context and adds project-level execution patterns.

### Project-Level Command Execution
- Always execute commands from project root or subdirectories
- Use relative paths within project when possible
- Absolute paths should point to `/home/dawson/code/<project>/`
- Scripts should have bash shebang: `#!/bin/bash`

### Dependency Installation
- Node.js: `npm install` (uses Linux build)
- Python: `pip3 install -r requirements.txt`
- System tools: `sudo apt install <package>`

### Development Server Operations
- Start servers: `npm start`, `python3 -m flask run`, etc.
- Servers bind to `0.0.0.0` or `localhost`
- Port forwarding handled automatically by WSL2
- Access from Windows browser: `http://localhost:<port>`

### Build and Test Commands
- Build: `npm run build`, `make`, `python3 setup.py build`
- Test: `npm test`, `pytest`, `make test`
- All use Linux-native tools and compilers

### File Management at Project Level
- Create files with LF line endings
- Use `.gitattributes` to enforce line ending policy
- Watch for permission issues (should be minimal on native Linux FS)

### Environment Variables
- Set in `.env` file (project root)
- Or in `~/.bashrc` for persistent settings
- Use `export VAR=value` syntax

---

## Integration Notes

This context file:
- Inherits from Layer 0 Universal WSL agent context
- Is overridden by Layer 2 (Feature) and Layer 3 (Component) WSL contexts
- Provides project-level execution patterns for worker agents

---

## Future Extensions

Add project-level WSL-specific:
- Project-specific scripts and commands
- Development workflow patterns
- Testing and CI/CD integration
- Environment variable management
