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

<!-- section_id: "d509ff7f-aac4-4a2e-a3ff-50fcbeeac3b8" -->
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

<!-- section_id: "79e5c839-5666-44a0-abfd-9b8c86599e9d" -->
## How To Use This Tree

<!-- section_id: "8b36a4c2-1fe5-4ce0-b36e-25960ae6f59e" -->
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

<!-- section_id: "1273bf95-3132-4fb3-8bd7-59f3b3e38f99" -->
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

<!-- section_id: "ca0c9ebe-fa52-4d55-8bc0-0cc0fb939939" -->
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

<!-- section_id: "890455b2-fff4-4a91-b544-64e253dda68d" -->
## Documentation Placement Guidelines

<!-- section_id: "3e55ff89-81e6-4703-a872-b55df8fc729c" -->
### Where to place OS-specific setup docs:
- `0.05_operating_systems/<os>/README.md` - OS installation, system requirements

<!-- section_id: "a3802c2a-9761-405c-95f9-d2b08ae22f61" -->
### Where to place environment-specific setup docs:
- `0.06_environments/<environment>/README.md` - Environment variables, configuration

<!-- section_id: "1ac93f19-3804-4bef-8750-643706e315fd" -->
### Where to place coding app setup docs:
- `0.07_coding_apps/<coding_app>/README.md` - IDE installation, extensions, settings

<!-- section_id: "1e00d1bd-0587-4528-adc6-d9e5c4268234" -->
### Where to place AI app setup docs:
- `0.09_ai_apps/<ai_app>/README.md` - AI tool installation, authentication, configuration

<!-- section_id: "a8342bb4-0a03-4c45-9c79-dbbcb37d1f52" -->
### Where to place MCP server setup docs:
- `0.10_mcp_servers_and_apis_and_secrets/<mcp_server>/general_setup_and_config/` - MCP server installation, configuration, issues

<!-- section_id: "1e007751-1fcb-4e69-b011-c71dc2e272df" -->
### Where to place AI model setup docs:
- `0.11_ai_models/<ai_model>/general_setup_and_config/` - Model access, API keys, rate limits

<!-- section_id: "3ed347d8-ba59-44fa-9c1f-c0bec02db16f" -->
### Where to place universal tool setup docs:
- `0.12_universal_tools/<tool>/general_setup_and_config/` - Tool installation, usage, issues

<!-- section_id: "02235e0a-e164-4de6-b0c2-4c2cd096d8fe" -->
### Where to place protocol setup docs:
- `0.13_protocols/<protocol>/general_setup_and_config/` - Protocol rules, conventions, best practices

<!-- section_id: "2bd0a625-919f-4cba-b220-5b91260ecbcc" -->
### Where to place agent setup docs:
- `0.14_agent_setup/general_setup_and_config/` - Agent configuration, registration, deployment

<!-- section_id: "a9fcf7ce-e97b-41f3-b4d5-32dab7cbc955" -->
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

<!-- section_id: "6758dd97-6e7b-46ee-88eb-26676fe6c731" -->
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

<!-- section_id: "959b6faf-568a-4856-88f9-d4988e1364a8" -->
## Legacy sub_layer_0_06_coding_app_setup Source

# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "3d1e8e79-ca2d-4737-9835-f50d9f79928f" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "29fb5967-ef5b-4c97-bcff-6b56fe4e37de" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "af099db0-0a94-4761-973d-39e2c28f1bdf" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.

---

<!-- section_id: "fc2ecb17-5a1b-43b7-ae0e-ff6dfa23a734" -->
## Legacy sub_layer_0_07_environment_setup Source

# Sub Layer 0.06: Environment Setup

**Purpose**: Environment-level setup that is not OS-specific and not tied to a single coding/AI application (e.g., Git/GitHub auth patterns, credentials, cross-app environment rules).

<!-- section_id: "ffb4a5c4-26db-4b26-8bf9-c42cda35f37e" -->
## Included Topics

- Git and GitHub authentication (PATs, SSO/SAML, credential storage patterns)
- Cross-tool environment conventions (paths, permissions, shells)

<!-- section_id: "35a7a8b5-ca1b-4b5b-b90a-5e89c3d4028d" -->
## Documentation

- **GitHub SSO (PAT) Setup**: `trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`

---

<!-- section_id: "75ca1542-c05f-46a0-b1a4-a8c8016a3056" -->
## Legacy sub_layer_0_08_apps_browsers_extensions_setup Source

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

<!-- section_id: "f9fbec2d-97c2-477d-8be7-873c303701e6" -->
## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.

---

<!-- section_id: "22eabda8-7ca8-4d21-ac46-a961e337102d" -->
## Legacy sub_layer_0_09_ai_apps_tools_setup Source

# Sub Layer 0.09: AI Apps & Tools Setup

**Purpose:** This sub-layer contains documentation and setup instructions for AI applications and tools used across all projects.

**Location in Layer System:**
- Universal Layer: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`
- Referenced in: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`

---

<!-- section_id: "0fe9f5a2-73f3-4b04-9178-2cf747378a7b" -->
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

<!-- section_id: "8628b558-e057-4695-809c-fcadf522d3bf" -->
## 📚 Related Documentation

<!-- section_id: "fc9950d8-0d00-45b6-bde7-41895635532a" -->
### Universal Context Entry Points
- **Universal Init Prompt:** `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
- **System Overview:** `0_context/SYSTEM_OVERVIEW.md`
- **Usage Guide:** `0_context/USAGE_GUIDE.md`
- **Master Index:** `0_context/MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "ec5ae6c7-7eef-4a2c-9f57-49610bf4ec01" -->
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

<!-- section_id: "adda288e-f000-478f-a26a-852f440acaaa" -->
### Universal Rules & Protocols
- **Terminal Protocol:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- **Git Commit Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- **Context Update Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

---

<!-- section_id: "2d76bda3-978f-45fa-b552-c3822904155f" -->
## 🔧 AI Apps & Tools Covered

This sub-layer documents:
- AI application installations and configurations
- CLI tools for AI services (OpenAI Codex, Claude Code, Google Gemini, etc.)
- Authentication and API key management
- Tool-specific setup instructions
- Integration patterns and best practices

<!-- section_id: "1c84d39b-45ab-4127-90f1-eb3b2533e721" -->
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

<!-- section_id: "63b247cd-ac79-480b-9bc7-2f14c5456066" -->
### Claude Code CLI

**Documentation Location**:
- Main README: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md`
- Quick Start: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/QUICK_START.md`
- What Actually Works: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/WHAT_ACTUALLY_WORKS.md`

**Important Note**: Claude Code uses CLI-based MCP configuration (not config files). See MCP setup in `sub_layer_0_10_mcp_servers_and_tools_setup` for details.

<!-- section_id: "f612bd5e-4e7b-4a37-837d-def13343f8e6" -->
### Google Gemini CLI

**Example Installation**:
```bash
npm install -g @google/gemini-cli
gemini login
gemini  # Start interactive CLI
```

<!-- section_id: "b87fc538-445f-4b49-aa1f-77039f992f4e" -->
### Installation Checklist

When setting up a new development environment:

- [ ] Node.js and npm installed (via nvm recommended)
- [ ] OpenAI Codex CLI installed and configured
- [ ] Claude Code CLI installed (if using)
- [ ] API keys configured for respective tools
- [ ] MCP servers configured (see `sub_layer_0_10_mcp_servers_and_tools_setup`)

<!-- section_id: "56a204e2-ae88-42b9-b069-b0edb8da3b08" -->
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

<!-- section_id: "8135dae7-817b-4fd8-a63b-843e5d619f47" -->
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

<!-- section_id: "91b18bf3-e97d-4955-955f-6e9b23dbe3df" -->
## 📝 Documentation Structure

<!-- section_id: "d575f640-ecab-429e-98d7-f2e3ce493912" -->
### Current Status
- This README provides the entry point and navigation
- Additional documentation should be added as needed
- Keep mappings up to date if paths change

<!-- section_id: "546cf352-0a4f-4516-8b9e-5e9a03e0fc1f" -->
### Adding New Documentation
When adding new AI app or tool documentation:
1. Create appropriate subdirectories if needed (following trickle-down pattern)
2. Follow the universal documentation structure
3. Update this README with references
4. Ensure paths are relative to the universal context root (`<universal_context_root>/0_context/`)
5. Update the Master Documentation Index if needed
6. Follow the context update rule: `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

<!-- section_id: "b77e141f-5d03-423d-b787-9f29232f6d8f" -->
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

<!-- section_id: "59e1e7bc-3df8-47c3-8bf1-cf840acfb204" -->
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

<!-- section_id: "55b35ab9-6a7d-464c-95ca-c9440d2b67e0" -->
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

<!-- section_id: "c2b901f8-82a3-46ff-94ff-35e18c1c05a1" -->
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

<!-- section_id: "69b9c790-49a8-48a4-a004-4370ebb26c0a" -->
## Legacy sub_layer_0_11_ai_models Source

# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

<!-- section_id: "7a5f2b6a-70bb-4242-85a6-346f2735079f" -->
## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

<!-- section_id: "f11d1fe2-c0b6-4523-8567-b3d51ec92cf3" -->
## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

<!-- section_id: "9ca5ced5-4467-43ab-bea1-7c17f49a7f27" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

<!-- section_id: "b8e02ae8-3e5b-470b-80c2-0e6e931da06d" -->
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

<!-- section_id: "4274956a-5f55-4e43-9e21-c3007bc6c04b" -->
## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

---

<!-- section_id: "776ed38b-4e1f-4a4a-a1ac-e287fe6ff648" -->
## Legacy sub_layer_0_12_universal_tools Source

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

<!-- section_id: "e9451eac-f74b-4148-af6b-abfbd4ba574d" -->
## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

<!-- section_id: "452d8fee-8d50-48a3-a2c6-158cf77eef9c" -->
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

<!-- section_id: "bda75f59-df0d-478e-95ed-e2b420a91d2c" -->
## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

<!-- section_id: "d777df60-0372-4062-a996-e80fc934ff9f" -->
## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "d0ec008b-2f31-4cbe-be2c-8aefe6d4d50e" -->
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

<!-- section_id: "91730726-9aa5-41bd-a4cd-182270261f28" -->
### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/0.99_stages/stage_0_01_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

<!-- section_id: "ccbaf269-a8a3-4d49-9d7f-908055250b14" -->
### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

<!-- section_id: "a64c7f04-2cee-4180-a06a-e812880a8f66" -->
## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

<!-- section_id: "c388f112-442e-406a-ad3b-655e5d0eb8ce" -->
## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

<!-- section_id: "a98fdec3-3ac0-49ab-8778-7be856351eeb" -->
### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

<!-- section_id: "d9a7ba10-11db-4c60-ae66-edc1b5c6618f" -->
### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

<!-- section_id: "306923c2-a935-4dd5-a25c-ea9958866785" -->
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

<!-- section_id: "841f70c3-6128-4bce-861a-8f43ae6d800a" -->
## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

---

<!-- section_id: "82b1a46f-4bd9-40db-b177-587fff285000" -->
## Legacy sub_layer_0_13_universal_protocols Source

# Universal Protocols

This sub-layer contains standard operating procedures (SOPs) and protocols that apply across all projects and features, ensuring consistent and high-quality execution of tasks.

It is organized as a **workflow feature**, following the same pattern described in the layer/stage framework:

- `0_instruction_docs/` – protocol definitions and standards (what the protocols are).
- `0.03_workflow_creation/` – manager system + stages for designing/maintaining protocol workflows.
- `0.04_workflows/` – concrete protocol workflows (how the protocols are applied step-by-step).
- `0.05_results/` – aggregated results, metrics, and retrospectives from running those workflows.

<!-- section_id: "eeb804a2-f00c-40cb-88eb-db50c16947c6" -->
## Protocols

<!-- section_id: "82ccb1ff-0587-4d82-8f1b-1c18e3c2be0b" -->
### 1. Verification
- **Small Batch Protocol**: `small_batch_verification/0_instruction_docs/small_batch_verification_protocol.md` - Guidelines for iterative testing and verification.

<!-- section_id: "1aa20080-2aaf-4105-84db-1835c8eb9003" -->
### 2. Research File Documentation & Organization
- **File Documentation Protocol**: `file_documentation_and_organization/0_instruction_docs/file_documentation_and_organization_protocol.md` - Steps for turning large raw files (e.g., chat transcripts, research logs) into structured `chat_history`, `things_learned`, and `overview` docs that are easy for agents to use.

<!-- section_id: "b59ca188-64b6-4824-8134-ae6d786da564" -->
### 3. Protocol Writing Standard
- **Protocol Writing Standard**: `protocol_writing_standard/0_instruction_docs/protocol_writing_standard.md` - Standard format and conventions for writing protocol documents, including OS/tool specificity conventions.

<!-- section_id: "0fd7be11-9994-440a-ab73-58fec42956cf" -->
### 4. Memory Handling
- **Memory Handling Protocol**: `memory_handling/0_instruction_docs/memory_handling_protocol.md` - Guidelines for handling "remember this" requests and long-term memory storage.

<!-- section_id: "c2ade216-b9fa-40d5-914b-dcf40c0b5ce0" -->
### 5. Reordering Operations
- **Reordering Operations Protocol**: `reordering_operations/0_instruction_docs/reordering_operations_protocol.md` - Step-by-step guide for reordering numbered items (sub-layers, stages, etc.) in the context system, including required context loading and registry regeneration steps.

<!-- section_id: "b0bad6cd-fd78-4667-be2f-d6c389dc5618" -->
### 6. Framework Orchestration
- **Framework Orchestration Overview**: `framework_orchestration/0_instruction_docs/framework_orchestration_overview.md` - Guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the AI Manager Hierarchy System. Explains when to use framework-based orchestration vs. simple handoff-based coordination, with minimal integration examples.

<!-- section_id: "f1419717-f243-4110-b77d-bba6ac92adc5" -->
### 7. CLI Recursion
- **CLI Recursion Syntax**: `cli_recursion/0_instruction_docs/cli_recursion_syntax.md` - Concrete CLI recursion patterns for creating deep agent hierarchies where managers spawn workers via CLI commands. Includes OS-adapted examples for WSL/Ubuntu with Claude Code, Codex CLI, and Gemini CLI.

<!-- section_id: "c6b6fef7-f9c5-4fbe-af3b-112a3cd20d08" -->
### 8. Observability and Logging
- **Observability Protocol**: `observability/README.md` - Structured logging, monitoring, and observability patterns for the AI Manager Hierarchy System. Defines log levels, structured formats, layer-specific requirements, handoff logging, manager/worker observability, metrics collection, distributed tracing, and audit trail requirements.

Over time, each protocol in `0_instruction_docs/` can be backed by:

- One or more **workflow definitions** in `0.03_workflow_creation/` and `0.04_workflows/`.
- Recorded **results and refinements** in `0.05_results/`.

This lets universal protocols evolve as first-class workflows, not just static documents.

---

<!-- section_id: "a3e4ac19-cbcd-45c6-9ada-9042ff4a4a66" -->
## Legacy sub_layer_0_14_agent_setup Source

# sub_layer_0_13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

<!-- section_id: "11e30e25-b24d-4e4c-b787-d26512b0bf4a" -->
## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0_09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0_10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0_11): Which AI models are available and approved for use

<!-- section_id: "c2db363f-9669-440e-a703-df3d0aea1668" -->
## Agent Configuration Features

<!-- section_id: "d7c779db-7e81-4ee3-bc84-5e5a473e519c" -->
### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

<!-- section_id: "12845894-54b9-4563-8fa7-31ac6eb65c11" -->
### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

<!-- section_id: "bf1a4431-83ac-42c4-b4da-2e763b98bd66" -->
### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

<!-- section_id: "82cf19b7-ab14-4814-8d2a-4ba04854d29c" -->
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

<!-- section_id: "8339d9ad-3d83-4b26-a3f7-502a7c67db2d" -->
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

<!-- section_id: "eb054a4a-2c50-4d4c-8aee-0db723c2124b" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0_11_ai_models` - Agents require models to function
  - `sub_layer_0_12_universal_tools` - Agents use universal tools for capabilities
- **Provides to**: All layers that need configured agents for work

<!-- section_id: "370e5c29-62c9-47a4-b3c9-52d2e26aa7b4" -->
## Key Concepts

<!-- section_id: "2b12af68-42ea-412d-92d5-2932f1dbaf91" -->
### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

<!-- section_id: "e2198dfa-684f-4680-a115-293d413e6b7f" -->
### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

<!-- section_id: "4d54e332-9b9c-4eac-8296-5c8260aae823" -->
## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
