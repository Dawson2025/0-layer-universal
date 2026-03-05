---
resource_id: "fa3350ee-71b3-4b0b-8d3a-226e664a3b0f"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102106-IF2WOGZ"
---
# 0.01 Universal Setup File Tree (Traversable Hierarchy)

This folder is the **traversable universal setup documentation file tree**. It is organized so you can always navigate through the complete setup hierarchy:

- See `HIERARCHY_SYSTEM_OVERVIEW.md` for the current hierarchy rules and traversal pattern.

`Operating System → Environment → Coding App → AI App → {MCP Servers, AI Models, Universal Tools, Protocols, Agent Setup}`

<!-- section_id: "51721d68-c5e9-4734-a165-c6c00ad16681" -->
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

<!-- section_id: "fc2bcfde-eeed-4a6d-ab32-024153e3e95f" -->
## How To Use This Tree

<!-- section_id: "75a58c4b-d86a-462a-ae98-d1c607dcedcc" -->
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

<!-- section_id: "f0062c19-b4e1-40c1-ac3c-7c0a96b3e185" -->
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

<!-- section_id: "0f75234d-2ef5-4706-b1df-403f17ff8f4d" -->
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

<!-- section_id: "1ec07373-db6f-4bbb-a973-95801155e0c0" -->
## Documentation Placement Guidelines

<!-- section_id: "1db671b1-62e6-45fa-99ac-264358c94ab2" -->
### Where to place OS-specific setup docs:
- `0.05_operating_systems/<os>/README.md` - OS installation, system requirements

<!-- section_id: "22c647f4-b27c-4f90-ba75-ed7e1c802a51" -->
### Where to place environment-specific setup docs:
- `0.06_environments/<environment>/README.md` - Environment variables, configuration

<!-- section_id: "973d8601-29de-4e93-87bd-c7717f514abf" -->
### Where to place coding app setup docs:
- `0.07_coding_apps/<coding_app>/README.md` - IDE installation, extensions, settings

<!-- section_id: "c3e2da76-78d1-4a7e-b317-5bd7d54bd221" -->
### Where to place AI app setup docs:
- `0.09_ai_apps/<ai_app>/README.md` - AI tool installation, authentication, configuration

<!-- section_id: "4656e4c5-93d4-46f5-8015-e82e5cd2d2bb" -->
### Where to place MCP server setup docs:
- `0.10_mcp_servers_and_apis_and_secrets/<mcp_server>/general_setup_and_config/` - MCP server installation, configuration, issues

<!-- section_id: "9215e5aa-e011-47de-8d99-280a79064c04" -->
### Where to place AI model setup docs:
- `0.11_ai_models/<ai_model>/general_setup_and_config/` - Model access, API keys, rate limits

<!-- section_id: "1d43a80a-677b-4e06-b396-c5789650ec7a" -->
### Where to place universal tool setup docs:
- `0.12_universal_tools/<tool>/general_setup_and_config/` - Tool installation, usage, issues

<!-- section_id: "033fc8c8-ad4a-43c9-8b4a-8837ce3540ca" -->
### Where to place protocol setup docs:
- `0.13_protocols/<protocol>/general_setup_and_config/` - Protocol rules, conventions, best practices

<!-- section_id: "a64caec6-36ea-4202-8306-d8790f39883d" -->
### Where to place agent setup docs:
- `0.14_agent_setup/general_setup_and_config/` - Agent configuration, registration, deployment

<!-- section_id: "31efbf88-b2af-4c30-88c3-98ea5ba2a7bb" -->
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

<!-- section_id: "40f7e517-5e19-4c72-bfe9-70bc3596ef04" -->
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

<!-- section_id: "b913ab9c-7866-42c7-aae1-b9c45fd464bd" -->
## Legacy sub_layer_0_06_coding_app_setup Source

# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "8d3664ea-53b4-41bc-aa11-4f8ea2d9f02b" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "10cd54df-35fe-4fff-8824-d45c72f06ca9" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "f5240c54-1830-4fb8-bef5-253b1e4e4f7d" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.

---

<!-- section_id: "65af4683-ce8e-4f21-8783-82984cbd38b0" -->
## Legacy sub_layer_0_07_environment_setup Source

# Sub Layer 0.06: Environment Setup

**Purpose**: Environment-level setup that is not OS-specific and not tied to a single coding/AI application (e.g., Git/GitHub auth patterns, credentials, cross-app environment rules).

<!-- section_id: "351f04d6-aaa3-43e5-a495-ecc6276ab08c" -->
## Included Topics

- Git and GitHub authentication (PATs, SSO/SAML, credential storage patterns)
- Cross-tool environment conventions (paths, permissions, shells)

<!-- section_id: "674e8985-3f77-4f8f-90b2-fbbfcc865b99" -->
## Documentation

- **GitHub SSO (PAT) Setup**: `trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`

---

<!-- section_id: "5a3e3f2a-5a95-4a75-a756-78730e92d34c" -->
## Legacy sub_layer_0_08_apps_browsers_extensions_setup Source

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

<!-- section_id: "2b60829c-a577-4970-908f-8bae6d07b2a8" -->
## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.

---

<!-- section_id: "bc26fae8-4d62-4387-933c-b49a072a9b3c" -->
## Legacy sub_layer_0_09_ai_apps_tools_setup Source

# Sub Layer 0.09: AI Apps & Tools Setup

**Purpose:** This sub-layer contains documentation and setup instructions for AI applications and tools used across all projects.

**Location in Layer System:**
- Universal Layer: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`
- Referenced in: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`

---

<!-- section_id: "a8b85c5f-0154-4a1d-921f-999d6e5590bc" -->
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

<!-- section_id: "34545efe-c18d-4023-8ec3-884dba975676" -->
## 📚 Related Documentation

<!-- section_id: "2a2ab409-a7fd-464b-a2c6-a13a3bf61b64" -->
### Universal Context Entry Points
- **Universal Init Prompt:** `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
- **System Overview:** `0_context/SYSTEM_OVERVIEW.md`
- **Usage Guide:** `0_context/USAGE_GUIDE.md`
- **Master Index:** `0_context/MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "7b6af581-f625-4671-af8a-f5f5b3ac3ded" -->
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

<!-- section_id: "5f0720cb-a40b-41c0-8257-8fac22a15c22" -->
### Universal Rules & Protocols
- **Terminal Protocol:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- **Git Commit Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- **Context Update Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

---

<!-- section_id: "62d0e478-f18b-41b2-b492-ce266cb69a0b" -->
## 🔧 AI Apps & Tools Covered

This sub-layer documents:
- AI application installations and configurations
- CLI tools for AI services (OpenAI Codex, Claude Code, Google Gemini, etc.)
- Authentication and API key management
- Tool-specific setup instructions
- Integration patterns and best practices

<!-- section_id: "a5d80f33-2e9d-4e89-832b-1a8e807c5243" -->
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

<!-- section_id: "adb564c1-1b30-412e-8136-18ef18c81052" -->
### Claude Code CLI

**Documentation Location**:
- Main README: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md`
- Quick Start: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/QUICK_START.md`
- What Actually Works: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/WHAT_ACTUALLY_WORKS.md`

**Important Note**: Claude Code uses CLI-based MCP configuration (not config files). See MCP setup in `sub_layer_0_10_mcp_servers_and_tools_setup` for details.

<!-- section_id: "97f48540-d25c-4aa2-8f97-fb1d8e036cd4" -->
### Google Gemini CLI

**Example Installation**:
```bash
npm install -g @google/gemini-cli
gemini login
gemini  # Start interactive CLI
```

<!-- section_id: "9fc8b95d-460a-4a33-b04f-95f8cbee5ed4" -->
### Installation Checklist

When setting up a new development environment:

- [ ] Node.js and npm installed (via nvm recommended)
- [ ] OpenAI Codex CLI installed and configured
- [ ] Claude Code CLI installed (if using)
- [ ] API keys configured for respective tools
- [ ] MCP servers configured (see `sub_layer_0_10_mcp_servers_and_tools_setup`)

<!-- section_id: "1225d49a-5b3d-420e-9805-114fb69c25d2" -->
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

<!-- section_id: "e9b7da20-3458-4fa4-952b-5f5559fca9e9" -->
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

<!-- section_id: "79ce5817-981a-4c46-84fb-ded8dd717b72" -->
## 📝 Documentation Structure

<!-- section_id: "6760ed60-d176-4087-a180-35a1cdb6e2a0" -->
### Current Status
- This README provides the entry point and navigation
- Additional documentation should be added as needed
- Keep mappings up to date if paths change

<!-- section_id: "10964930-7346-4a5f-a655-cd932505404e" -->
### Adding New Documentation
When adding new AI app or tool documentation:
1. Create appropriate subdirectories if needed (following trickle-down pattern)
2. Follow the universal documentation structure
3. Update this README with references
4. Ensure paths are relative to the universal context root (`<universal_context_root>/0_context/`)
5. Update the Master Documentation Index if needed
6. Follow the context update rule: `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

<!-- section_id: "40a2d840-0a4b-4c0a-b2d0-129ba4b7e9fd" -->
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

<!-- section_id: "9f6217e1-bd15-4ed5-acab-b96cd5dae92c" -->
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

<!-- section_id: "152b334b-ec90-4d36-a35b-4e5b32286c16" -->
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

<!-- section_id: "0eb46c4a-fb04-4e10-9c06-9eca01c83607" -->
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

<!-- section_id: "76f1438a-96c6-4bf6-86ed-1b1a876afd50" -->
## Legacy sub_layer_0_11_ai_models Source

# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

<!-- section_id: "7ecea540-e942-4263-8fec-a66cb809f0b7" -->
## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

<!-- section_id: "78958ff3-6d4c-40ba-b41a-8c7d16a2af0f" -->
## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

<!-- section_id: "757abb7d-0efa-4cb4-bda6-4cd299f5271e" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

<!-- section_id: "2f5efa1e-03e5-4f7c-bf63-6f8e000d887a" -->
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

<!-- section_id: "3260a0b8-3107-49b8-969a-86681b111ede" -->
## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

---

<!-- section_id: "e894ee5f-222d-4d10-be44-6eefdf7f1540" -->
## Legacy sub_layer_0_12_universal_tools Source

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

<!-- section_id: "4c029d17-209f-4735-ab9c-fc100ca6eb67" -->
## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

<!-- section_id: "81ecc737-ee08-426b-8650-40ff0afdcf47" -->
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

<!-- section_id: "396782d8-f2ad-4122-8b58-83a2c227a877" -->
## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

<!-- section_id: "9e7050de-cbd8-438b-bb64-095d26d41a39" -->
## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "6558c3a6-7955-4e3f-aa4d-343f93ab98f7" -->
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

<!-- section_id: "582432b5-47ec-47bd-ad81-681c678eb114" -->
### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/0.99_stages/stage_0_01_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

<!-- section_id: "a7470a85-92ad-403b-8b11-c3fac769d173" -->
### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

<!-- section_id: "b4e3baed-5d0b-427d-885c-3071f51e29e0" -->
## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

<!-- section_id: "3f89d5d7-4e4e-44ff-8b17-70580112da48" -->
## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

<!-- section_id: "53d88ccb-6015-4e28-b618-1fd544634a7f" -->
### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

<!-- section_id: "612e61f2-bcc0-43d0-8b89-53c6718e067f" -->
### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

<!-- section_id: "a37233f3-aecc-4e2c-b475-0d01e8304d88" -->
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

<!-- section_id: "4fe3b35b-f9fa-4800-b034-a6d12763ed36" -->
## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

---

<!-- section_id: "b0418d0c-8631-41d3-8344-3e3cadac2165" -->
## Legacy sub_layer_0_13_universal_protocols Source

# Universal Protocols

This sub-layer contains standard operating procedures (SOPs) and protocols that apply across all projects and features, ensuring consistent and high-quality execution of tasks.

It is organized as a **workflow feature**, following the same pattern described in the layer/stage framework:

- `0_instruction_docs/` – protocol definitions and standards (what the protocols are).
- `0.03_workflow_creation/` – manager system + stages for designing/maintaining protocol workflows.
- `0.04_workflows/` – concrete protocol workflows (how the protocols are applied step-by-step).
- `0.05_results/` – aggregated results, metrics, and retrospectives from running those workflows.

<!-- section_id: "560305b2-aed8-4cdc-9911-344261cba998" -->
## Protocols

<!-- section_id: "eb0c5b8b-8faa-424b-991b-e2862510875d" -->
### 1. Verification
- **Small Batch Protocol**: `small_batch_verification/0_instruction_docs/small_batch_verification_protocol.md` - Guidelines for iterative testing and verification.

<!-- section_id: "b7a09f0b-cba9-4a34-8bae-01f73df03dc3" -->
### 2. Research File Documentation & Organization
- **File Documentation Protocol**: `file_documentation_and_organization/0_instruction_docs/file_documentation_and_organization_protocol.md` - Steps for turning large raw files (e.g., chat transcripts, research logs) into structured `chat_history`, `things_learned`, and `overview` docs that are easy for agents to use.

<!-- section_id: "ac86fe76-9ba4-4d2b-b0a1-767110ae03c9" -->
### 3. Protocol Writing Standard
- **Protocol Writing Standard**: `protocol_writing_standard/0_instruction_docs/protocol_writing_standard.md` - Standard format and conventions for writing protocol documents, including OS/tool specificity conventions.

<!-- section_id: "22d5bde5-43f4-4cca-8e0f-2b0d38e5305e" -->
### 4. Memory Handling
- **Memory Handling Protocol**: `memory_handling/0_instruction_docs/memory_handling_protocol.md` - Guidelines for handling "remember this" requests and long-term memory storage.

<!-- section_id: "c766667a-b2db-4f85-af49-ccb85d9068f8" -->
### 5. Reordering Operations
- **Reordering Operations Protocol**: `reordering_operations/0_instruction_docs/reordering_operations_protocol.md` - Step-by-step guide for reordering numbered items (sub-layers, stages, etc.) in the context system, including required context loading and registry regeneration steps.

<!-- section_id: "0aae19a6-6550-4d4d-b8de-ba8453c51a09" -->
### 6. Framework Orchestration
- **Framework Orchestration Overview**: `framework_orchestration/0_instruction_docs/framework_orchestration_overview.md` - Guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. Explains when to use framework-based orchestration vs. simple handoff-based coordination, with minimal integration examples.

<!-- section_id: "3b3a58b1-90d8-4bda-b389-9a0a4d1878ec" -->
### 7. CLI Recursion
- **CLI Recursion Syntax**: `cli_recursion/0_instruction_docs/cli_recursion_syntax.md` - Concrete CLI recursion patterns for creating deep agent hierarchies where managers spawn workers via CLI commands. Includes OS-adapted examples for WSL/Ubuntu with Claude Code, Codex CLI, and Gemini CLI.

<!-- section_id: "71f4e732-add0-4e35-81c1-503b3120cb01" -->
### 8. Observability and Logging
- **Observability Protocol**: `observability/README.md` - Structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. Defines log levels, structured formats, layer-specific requirements, handoff logging, manager/worker observability, metrics collection, distributed tracing, and audit trail requirements.

Over time, each protocol in `0_instruction_docs/` can be backed by:

- One or more **workflow definitions** in `0.03_workflow_creation/` and `0.04_workflows/`.
- Recorded **results and refinements** in `0.05_results/`.

This lets universal protocols evolve as first-class workflows, not just static documents.

---

<!-- section_id: "b45196a1-38bf-4d13-a06d-1d59fe8cfbb7" -->
## Legacy sub_layer_0_14_agent_setup Source

# sub_layer_0_13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

<!-- section_id: "63facd05-393c-4cf0-bf1c-441f0cfd5ec0" -->
## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0_09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0_10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0_11): Which AI models are available and approved for use

<!-- section_id: "3634e29f-1e51-4ec3-bcc7-aa3c4cc97ced" -->
## Agent Configuration Features

<!-- section_id: "d557dd79-c382-4344-b326-27a1c222a727" -->
### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

<!-- section_id: "160616b0-b572-4678-b075-cc1137e4bd4a" -->
### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

<!-- section_id: "74b6f59e-0822-425f-b404-76849a432db8" -->
### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

<!-- section_id: "46b52e7e-00c0-41be-9703-a28d4e4e483e" -->
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

<!-- section_id: "79e31e8d-391b-4313-8b29-c2c8c08cf0bb" -->
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

<!-- section_id: "1c15c0a0-0f72-4d64-802a-d1aac2ecb88d" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0_11_ai_models` - Agents require models to function
  - `sub_layer_0_12_universal_tools` - Agents use universal tools for capabilities
- **Provides to**: All layers that need configured agents for work

<!-- section_id: "4a319a90-1f74-46bf-af8f-238be67f5033" -->
## Key Concepts

<!-- section_id: "534e91de-14b5-48a4-b328-78ca04175180" -->
### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

<!-- section_id: "a09dcde6-d7b4-4e8f-8ef9-9f9f78830427" -->
### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

<!-- section_id: "27748af1-6335-45dd-b8e9-c7d4368fb933" -->
## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
