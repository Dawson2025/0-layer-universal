---
resource_id: "419adc6b-1150-42df-8c51-176e7b8ad6c5"
resource_type: "readme
document"
resource_name: "README"
---
# 0.01 Universal Setup File Tree (Traversable Hierarchy)

This folder is the **traversable universal setup documentation file tree**. It is organized so you can always navigate through the complete setup hierarchy:

- See `HIERARCHY_SYSTEM_OVERVIEW.md` for the current hierarchy rules and traversal pattern.

`Operating System → Environment → Coding App → AI App → {MCP Servers, AI Models, Universal Tools, Protocols, Agent Setup}`

## Canonical Tree

```text
0.01_universal_setup_file_tree_0/
└── 0.05_operating_systems/
    ├── _shared/                                    # Cross-OS defaults and documentation
    │   └── 0.06_environments/
    │       ├── _shared/                            # Cross-environment defaults
    │       │   └── 0.07_coding_apps/
    │       │       ├── _shared/                    # Cross-coding-app defaults
    │       │       │   └── 0.09_ai_apps/
    │       │       │       ├── _shared/            # Cross-AI-app defaults
    │       │       │       │   └── 0.10_mcp_servers_and_apis_and_secrets/
    │       │       │       │       ├── _shared/    # Cross-MCP-server defaults
    │       │       │       │       │   └── 0.11_ai_models/
    │       │       │       │       │       ├── _shared/           # Cross-model defaults
    │       │       │       │       │       │   └── 0.12_universal_tools/
    │       │       │       │       │       │       ├── _shared/   # Cross-tool defaults
    │       │       │       │       │       │       │   └── 0.13_protocols/
    │       │       │       │       │       │       │       ├── _shared/          # Cross-protocol defaults
    │       │       │       │       │       │       │       │   └── 0.14_agent_setup/
    │       │       │       │       │       │       │       │       └── general_setup_and_config/
    │       │       │       │       │       │       │       └── <protocol>/
    │       │       │       │       │       │       │           └── general_setup_and_config/
    │       │       │       │       │       │       └── <tool>/
    │       │       │       │       │       │           └── general_setup_and_config/
    │       │       │       │       │       └── <ai_model>/
    │       │       │       │       │           └── general_setup_and_config/
    │       │       │       │       ├── _mcp_core/              # Cross-server MCP issues
    │       │       │       │       │   └── general_setup_and_config/
    │       │       │       │       └── <mcp_server>/
    │       │       │       │           └── general_setup_and_config/
    │       │       │       └── <ai_app>/                       # Specific AI app setup
    │       │       │           └── 0.10_mcp_servers_and_apis_and_secrets/
    │       │       │               └── (same structure)
    │       │       └── <coding_app>/                           # Specific coding app setup
    │       │           └── 0.09_ai_apps/
    │       │               └── (same structure)
    │       └── <environment>/                                  # Specific environment setup
    │           └── 0.07_coding_apps/
    │               └── (same structure)
    └── <os>/                                                   # OS-specific overrides and notes
        └── 0.06_environments/
            └── (same structure)
```

## How To Use This Tree

### Quick Navigation

1. **Start at your OS**: `0.05_operating_systems/<os>/README.md`
   - Linux/Ubuntu: `0.05_operating_systems/linux_ubuntu/`
   - macOS: `0.05_operating_systems/macos/`
   - Windows: `0.05_operating_systems/windows/`
   - WSL: `0.05_operating_systems/wsl/`

2. **Navigate to environment**: `0.06_environments/<environment>/README.md`
   - Development: `0.06_environments/development/`
   - Production: `0.06_environments/production/`
   - Testing: `0.06_environments/testing/`

3. **Navigate to coding app**: `0.07_coding_apps/<coding_app>/README.md`
   - VS Code: `0.07_coding_apps/vscode/`
   - Cursor: `0.07_coding_apps/cursor/`
   - Vim: `0.07_coding_apps/vim/`
   - Emacs: `0.07_coding_apps/emacs/`

4. **Navigate to AI app**: `0.09_ai_apps/<ai_app>/README.md`
   - Claude Code CLI: `0.09_ai_apps/claude_code_cli/`
   - Cursor Agent: `0.09_ai_apps/cursor_agent/`
   - Codex CLI: `0.09_ai_apps/codex_cli/`

5. **Navigate to MCP server**: `0.10_mcp_servers_and_apis_and_secrets/<mcp_server>/general_setup_and_config/`
   - Browser MCP: `0.10_mcp_servers_and_apis_and_secrets/browser-mcp/`
   - Playwright MCP: `0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/`
   - Core issues: `0.10_mcp_servers_and_apis_and_secrets/_mcp_core/`

6. **Navigate to AI model**: `0.11_ai_models/<ai_model>/general_setup_and_config/`
   - Claude Sonnet: `0.11_ai_models/claude-sonnet/`
   - Claude Opus: `0.11_ai_models/claude-opus/`
   - GPT-4: `0.11_ai_models/gpt-4/`

7. **Navigate to universal tools**: `0.12_universal_tools/<tool>/general_setup_and_config/`
   - Git: `0.12_universal_tools/git/`
   - Docker: `0.12_universal_tools/docker/`
   - NPM: `0.12_universal_tools/npm/`

8. **Navigate to protocols**: `0.13_protocols/<protocol>/general_setup_and_config/`
   - Terminal Protocol: `0.13_protocols/terminal_protocol/`
   - Browser Protocol: `0.13_protocols/browser_protocol/`
   - Git Protocol: `0.13_protocols/git_protocol/`

9. **Navigate to agent setup**: `0.14_agent_setup/general_setup_and_config/`
   - Manager agents
   - Stage agents
   - Testing agents

### Using _shared Folders

Use `_shared/` folders when guidance applies across multiple options at that level:

- `0.05_operating_systems/_shared/` - Setup that works on all OSes
- `0.06_environments/_shared/` - Setup that works in all environments
- `0.07_coding_apps/_shared/` - Setup that works with all coding apps
- `0.09_ai_apps/_shared/` - Setup that works with all AI apps
- `0.10_mcp_servers_and_apis_and_secrets/_shared/` - Setup that works with all MCP servers
- `0.11_ai_models/_shared/` - Setup that works with all AI models
- `0.12_universal_tools/_shared/` - Setup that works with all tools
- `0.13_protocols/_shared/` - Setup that works with all protocols

### Finding Setup Documentation

**Scenario 1**: Setting up Claude Code CLI on Linux Ubuntu with Playwright MCP
```
Path: 0.05_operating_systems/linux_ubuntu/
      → 0.06_environments/development/
      → 0.07_coding_apps/_shared/
      → 0.09_ai_apps/claude_code_cli/
      → 0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
      → general_setup_and_config/
```

**Scenario 2**: Setting up universal Git tool for all environments
```
Path: 0.05_operating_systems/_shared/
      → 0.06_environments/_shared/
      → 0.07_coding_apps/_shared/
      → 0.09_ai_apps/_shared/
      → 0.10_mcp_servers_and_apis_and_secrets/_shared/
      → 0.11_ai_models/_shared/
      → 0.12_universal_tools/git/
      → general_setup_and_config/
```

**Scenario 3**: Setting up Cursor Agent with Browser MCP on macOS
```
Path: 0.05_operating_systems/macos/
      → 0.06_environments/development/
      → 0.07_coding_apps/cursor/
      → 0.09_ai_apps/cursor_agent/
      → 0.10_mcp_servers_and_apis_and_secrets/browser-mcp/
      → general_setup_and_config/
```

## Documentation Placement Guidelines

### Where to place OS-specific setup docs:
- `0.05_operating_systems/<os>/README.md` - OS installation, system requirements

### Where to place environment-specific setup docs:
- `0.06_environments/<environment>/README.md` - Environment variables, configuration

### Where to place coding app setup docs:
- `0.07_coding_apps/<coding_app>/README.md` - IDE installation, extensions, settings

### Where to place AI app setup docs:
- `0.09_ai_apps/<ai_app>/README.md` - AI tool installation, authentication, configuration

### Where to place MCP server setup docs:
- `0.10_mcp_servers_and_apis_and_secrets/<mcp_server>/general_setup_and_config/` - MCP server installation, configuration, issues

### Where to place AI model setup docs:
- `0.11_ai_models/<ai_model>/general_setup_and_config/` - Model access, API keys, rate limits

### Where to place universal tool setup docs:
- `0.12_universal_tools/<tool>/general_setup_and_config/` - Tool installation, usage, issues

### Where to place protocol setup docs:
- `0.13_protocols/<protocol>/general_setup_and_config/` - Protocol rules, conventions, best practices

### Where to place agent setup docs:
- `0.14_agent_setup/general_setup_and_config/` - Agent configuration, registration, deployment

## Relationship to Other Sublayers

This file tree serves as a **navigational index** that points to detailed documentation in the individual setup sublayers:

- **sub_layer_0_05_os_setup** - Detailed OS setup documentation
- **sub_layer_0_06_environment_setup** - Detailed environment setup documentation
- **sub_layer_0_07_coding_app_setup** - Detailed coding app setup documentation
- **sub_layer_0_08_apps_browsers_extensions_setup** - Detailed browser/extension setup documentation
- **sub_layer_0_09_ai_apps_tools_setup** - Detailed AI app setup documentation
- **sub_layer_0_10_mcp_servers_and_tools_setup** - Detailed MCP server setup documentation
- **sub_layer_0_11_ai_models** - Detailed AI model access documentation
- **sub_layer_0_12_universal_tools** - Detailed universal tool documentation
- **sub_layer_0_13_universal_protocols** - Detailed protocol documentation
- **sub_layer_0_14_agent_setup** - Detailed agent setup documentation

## Notes

- Use symlinks or references to avoid duplicating content from the detailed sublayers
- Each `general_setup_and_config/` folder should contain:
  - Setup instructions specific to that combination of choices
  - Known issues and fixes for that combination
  - Configuration examples
  - Links to detailed documentation in the respective sublayers
- The `_mcp_core/` pseudo-server stores issues that apply across multiple MCP servers
- Always start navigation from the most general level (OS) and work down to specifics

---

## Legacy sub_layer_0_06_coding_app_setup Source

# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.

---

## Legacy sub_layer_0_07_environment_setup Source

# Sub Layer 0.06: Environment Setup

**Purpose**: Environment-level setup that is not OS-specific and not tied to a single coding/AI application (e.g., Git/GitHub auth patterns, credentials, cross-app environment rules).

## Included Topics

- Git and GitHub authentication (PATs, SSO/SAML, credential storage patterns)
- Cross-tool environment conventions (paths, permissions, shells)

## Documentation

- **GitHub SSO (PAT) Setup**: `trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`

---

## Legacy sub_layer_0_08_apps_browsers_extensions_setup Source

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.

---

## Legacy sub_layer_0_09_ai_apps_tools_setup Source

# Sub Layer 0.09: AI Apps & Tools Setup

**Purpose:** This sub-layer contains documentation and setup instructions for AI applications and tools used across all projects.

**Location in Layer System:**
- Universal Layer: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`
- Referenced in: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`

---

## 🚀 Session Initialization

**Before working with AI apps and tools, follow the universal initialization protocol:**

1. **Read the Universal Init Prompt:**
   - Path: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
   - This provides the complete navigation hub and initialization checklist

2. **Sync Repositories:**
   ```bash
   # From each relevant repo (universal + any project/assignment):
   git pull
   git status
   ```

3. **Read Master Documentation Index:**
   - Path: `0_context/MASTER_DOCUMENTATION_INDEX.md`
   - This is your map of the entire universal documentation system

---

## 📚 Related Documentation

### Universal Context Entry Points
- **Universal Init Prompt:** `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
- **System Overview:** `0_context/SYSTEM_OVERVIEW.md`
- **Usage Guide:** `0_context/USAGE_GUIDE.md`
- **Master Index:** `0_context/MASTER_DOCUMENTATION_INDEX.md`

### Related Sub-Layers
- **Sub Layer 0.05:** OS Setup
  - Path: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/`
  - System-level prerequisites and setup
- **Sub Layer 0.06:** Environment Setup
  - Path: `layer_0/0.02_sub_layers/sub_layer_0_06_environment_setup/`
  - Git/GitHub auth, credentials, and cross-app environment conventions
- **Sub Layer 0.07:** Coding App Setup
  - Path: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/`
  - IDE and editor setup
- **Sub Layer 0.10:** MCP Servers and Tools Setup
  - Path: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
  - For Model Context Protocol servers and tools
  - **Note**: MCP setup requires AI apps/tools to be installed first (this sub-layer)
- **Sub Layer 0.11:** AI Models
  - Path: `layer_0/0.02_sub_layers/sub_layer_0_11_ai_models/`
  - AI model configuration and usage
- **Sub Layer 0.12:** Universal Tools
  - Path: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/`
  - Contains Claude Code configuration documentation

### Universal Rules & Protocols
- **Terminal Protocol:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- **Git Commit Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- **Context Update Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

---

## 🔧 AI Apps & Tools Covered

This sub-layer documents:
- AI application installations and configurations
- CLI tools for AI services (OpenAI Codex, Claude Code, Google Gemini, etc.)
- Authentication and API key management
- Tool-specific setup instructions
- Integration patterns and best practices

### OpenAI Codex CLI

**Status**: ✅ Installed (v0.64.0)

**Installation**:
```bash
npm install -g @openai/codex
```

**Verification**:
```bash
which codex && codex --version
# Output: /home/dawson/.nvm/versions/node/v22.21.1/bin/codex
#         codex-cli 0.64.0
```

**First-time Setup**:
1. Run `codex` to start interactive terminal UI
2. Authenticate with your ChatGPT Plus/Pro/Business account or provide API key
3. Optional: Set environment variable: `export OPENAI_API_KEY='your-api-key-here'`

**Usage**:
```bash
# Get help
codex --help

# Start interactive terminal
codex

# Update to latest version
npm install -g @openai/codex@latest
```

**Documentation**:
- Official: https://developers.openai.com/codex/cli
- Setup guide: `../../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/setup/CODEX_SETUP_README.md`

**Platform Support**:
- ✅ macOS and Linux (officially supported)
- ⚠️ Windows (experimental; recommended to use WSL)

### Claude Code CLI

**Documentation Location**:
- Main README: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md`
- Quick Start: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/QUICK_START.md`
- What Actually Works: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/WHAT_ACTUALLY_WORKS.md`

**Important Note**: Claude Code uses CLI-based MCP configuration (not config files). See MCP setup in `sub_layer_0_10_mcp_servers_and_tools_setup` for details.

### Google Gemini CLI

**Example Installation**:
```bash
npm install -g @google/gemini-cli
gemini login
gemini  # Start interactive CLI
```

### Installation Checklist

When setting up a new development environment:

- [ ] Node.js and npm installed (via nvm recommended)
- [ ] OpenAI Codex CLI installed and configured
- [ ] Claude Code CLI installed (if using)
- [ ] API keys configured for respective tools
- [ ] MCP servers configured (see `sub_layer_0_10_mcp_servers_and_tools_setup`)

### Quick Verification Commands

```bash
# Check Node.js
node --version && npm --version

# Check Codex CLI
which codex && codex --version

# Check Claude Code (if installed)
which claude && claude --version

# Check Gemini CLI (if installed)
which gemini && gemini --version
```

### Environment Variables

Common environment variables for AI tools:

```bash
# OpenAI API Key (for Codex and other OpenAI tools)
export OPENAI_API_KEY='your-api-key-here'

# Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

---

## 📝 Documentation Structure

### Current Status
- This README provides the entry point and navigation
- Additional documentation should be added as needed
- Keep mappings up to date if paths change

### Adding New Documentation
When adding new AI app or tool documentation:
1. Create appropriate subdirectories if needed (following trickle-down pattern)
2. Follow the universal documentation structure
3. Update this README with references
4. Ensure paths are relative to the universal context root (`<universal_context_root>/0_context/`)
5. Update the Master Documentation Index if needed
6. Follow the context update rule: `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

## ⚠️ Linux/Ubuntu-Specific MCP Issues

**CRITICAL**: AI apps and tools on Linux have platform-specific MCP limitations. Read:

- **[Linux/Ubuntu AI Apps MCP Issues](trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md)**: AI app-specific Linux limitations

**Key Issues**:
- Cursor IDE: Playwright MCP tools not exposed on Linux
- Claude Code: Different MCP configuration method
- NVM dependencies require bash wrappers
- Platform-specific configuration patterns needed

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

### Troubleshooting

#### Codex CLI Issues

1. **Command not found**: Ensure Node.js is in PATH and Codex is installed globally
   ```bash
   npm list -g @openai/codex
   npm install -g @openai/codex
   ```

2. **API key errors**: Verify `OPENAI_API_KEY` is set correctly
   ```bash
   echo $OPENAI_API_KEY
   ```

3. **Authentication issues**: Run `codex` interactively to re-authenticate

#### General Issues

- **Permission errors**: May need to use `sudo` for global npm installs (not recommended) or configure npm to use a different directory
- **Version conflicts**: Use nvm to manage Node.js versions per project
- **Node.js not found**: Ensure nvm is loaded: `source ~/.nvm/nvm.sh` or add to `~/.bashrc`

---

## 🔄 Mandatory Sync & Context Update Policy

**At start of every chat/session (before work):**
```bash
# From each relevant repo (universal, project, assignment):
git pull
git status
```

**Before ending every response:**
1. Update context/docs with any new decisions/findings
2. Stage and commit your changes:
   ```bash
   git add .
   git commit -m "<short description>" || true
   ```
3. Push to your fork:
   ```bash
   git push || true
   ```
4. Confirm clean status:
   ```bash
   git status
   ```

---

## 🎯 Path Resolution

**All paths in this documentation are relative to:**
- Universal context root: `<universal_context_root>/0_context/`

**To reference this sub-layer from other locations:**
- From universal context root: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`
- From project context: `../../0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`

---

**Last Updated:** 2025-01-26  
**Version:** 1.1 (Enhanced with Codex CLI documentation and universal init prompt patterns)  
**Based on:** `universal_init_prompt.md` patterns and structure

---

## Legacy sub_layer_0_11_ai_models Source

# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

## ⚠️ Linux/Ubuntu-Specific Model Access Issues

**CRITICAL**: AI model access to MCP tools is limited on Linux. Read:

- **[Linux/Ubuntu Model Access Issues](trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md)**: Model access limitations on Linux

**Key Issues**:
- Some MCP tools unavailable to models on Linux
- Tool naming conventions may differ
- Model fallback strategies need Linux-specific configuration
- Model instructions must account for Linux tool limitations

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

---

## Legacy sub_layer_0_12_universal_tools Source

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

## Structure

```
sub_layer_0_12_universal_tools/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── browser-automation/
        ├── claude-code-config/
        ├── ai-development-frameworks/
        ├── platform-version-control/
        └── ...
```

## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

### Quartet Pattern Overview

Each layer/stage location can have OS-specific context files organized as **quartets** (or N-tuples):

- `CLAUDE.md` - Claude Code specific instructions
- `AGENTS.md` - General agent instructions (Codex CLI, etc.)
- `GEMINI.md` - Gemini CLI specific instructions
- `.cursor/rules/*.mdc` - Cursor IDE rules (future)

These files are organized under `os/<os-id>/` directories where `<os-id>` can be:
- `wsl` - Windows Subsystem for Linux
- `linux_ubuntu` - Native Ubuntu Linux
- `windows` - Native Windows
- `macos` - macOS
- Custom variants as needed

### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/0.99_stages/stage_0_01_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

## ⚠️ Linux/Ubuntu-Specific Tool Access Issues

**CRITICAL**: Universal tools that depend on MCP have Linux-specific limitations. Read:

- **[Linux/Ubuntu Tool Access Issues](trickle_down_0.75_universal_tools/0_instruction_docs/LINUX_UBUNTU_TOOL_ACCESS_ISSUES.md)**: Universal tool access limitations on Linux

**Key Issues**:
- Browser automation tools must use `mcp_browser_*` instead of `mcp_playwright_*`
- Development frameworks need Linux-specific adaptations
- Cross-cutting utilities may require tool name updates
- Tool migration guide available for Playwright → Browser MCP

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

---

## Legacy sub_layer_0_13_universal_protocols Source

# Universal Protocols

This sub-layer contains standard operating procedures (SOPs) and protocols that apply across all projects and features, ensuring consistent and high-quality execution of tasks.

It is organized as a **workflow feature**, following the same pattern described in the layer/stage framework:

- `0_instruction_docs/` – protocol definitions and standards (what the protocols are).
- `0.03_workflow_creation/` – manager system + stages for designing/maintaining protocol workflows.
- `0.04_workflows/` – concrete protocol workflows (how the protocols are applied step-by-step).
- `0.05_results/` – aggregated results, metrics, and retrospectives from running those workflows.

## Protocols

### 1. Verification
- **Small Batch Protocol**: `small_batch_verification/0_instruction_docs/small_batch_verification_protocol.md` - Guidelines for iterative testing and verification.

### 2. Research File Documentation & Organization
- **File Documentation Protocol**: `file_documentation_and_organization/0_instruction_docs/file_documentation_and_organization_protocol.md` - Steps for turning large raw files (e.g., chat transcripts, research logs) into structured `chat_history`, `things_learned`, and `overview` docs that are easy for agents to use.

### 3. Protocol Writing Standard
- **Protocol Writing Standard**: `protocol_writing_standard/0_instruction_docs/protocol_writing_standard.md` - Standard format and conventions for writing protocol documents, including OS/tool specificity conventions.

### 4. Memory Handling
- **Memory Handling Protocol**: `memory_handling/0_instruction_docs/memory_handling_protocol.md` - Guidelines for handling "remember this" requests and long-term memory storage.

### 5. Reordering Operations
- **Reordering Operations Protocol**: `reordering_operations/0_instruction_docs/reordering_operations_protocol.md` - Step-by-step guide for reordering numbered items (sub-layers, stages, etc.) in the context system, including required context loading and registry regeneration steps.

### 6. Framework Orchestration
- **Framework Orchestration Overview**: `framework_orchestration/0_instruction_docs/framework_orchestration_overview.md` - Guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. Explains when to use framework-based orchestration vs. simple handoff-based coordination, with minimal integration examples.

### 7. CLI Recursion
- **CLI Recursion Syntax**: `cli_recursion/0_instruction_docs/cli_recursion_syntax.md` - Concrete CLI recursion patterns for creating deep agent hierarchies where managers spawn workers via CLI commands. Includes OS-adapted examples for WSL/Ubuntu with Claude Code, Codex CLI, and Gemini CLI.

### 8. Observability and Logging
- **Observability Protocol**: `observability/README.md` - Structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. Defines log levels, structured formats, layer-specific requirements, handoff logging, manager/worker observability, metrics collection, distributed tracing, and audit trail requirements.

Over time, each protocol in `0_instruction_docs/` can be backed by:

- One or more **workflow definitions** in `0.03_workflow_creation/` and `0.04_workflows/`.
- Recorded **results and refinements** in `0.05_results/`.

This lets universal protocols evolve as first-class workflows, not just static documents.

---

## Legacy sub_layer_0_14_agent_setup Source

# sub_layer_0_13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0_09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0_10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0_11): Which AI models are available and approved for use

## Agent Configuration Features

### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

## Structure

```
sub_layer_0_13_agent_setup/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── agent-configs/          # Agent configuration files
        ├── model-fallbacks/        # Model fallback configurations
        ├── app-specific-agents/    # App-specific agent setups
        └── mcp-agent-integration/  # MCP server agent integration
```

## Dependency Chain

Agent setup follows this dependency order:

```
0.08_ai_apps_tools_setup
    ↓
0.10_mcp_servers_and_tools_setup (depends on 0.09)
    ↓
0.11_ai_models
    ↓
0.12_universal_tools
    ↓
0.13_agent_setup (depends on 0.09, 0.10, 0.11, 0.12) ← You are here
```

## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0_11_ai_models` - Agents require models to function
  - `sub_layer_0_12_universal_tools` - Agents use universal tools for capabilities
- **Provides to**: All layers that need configured agents for work

## Key Concepts

### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
