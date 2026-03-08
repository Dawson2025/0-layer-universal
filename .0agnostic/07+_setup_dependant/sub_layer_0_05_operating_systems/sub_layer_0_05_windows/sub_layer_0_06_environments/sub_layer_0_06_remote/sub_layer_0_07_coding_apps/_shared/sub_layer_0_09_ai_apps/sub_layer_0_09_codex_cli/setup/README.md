---
resource_id: "73e19fa1-5fe7-4103-b127-e49f0320be0e"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.09: AI Apps & Tools Setup

**Purpose:** This sub-layer contains documentation and setup instructions for AI applications and tools used across all projects.

**Location in Layer System:**
- Universal Layer: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`
- Referenced in: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`

---

<!-- section_id: "14e924b2-3ddc-4f3a-8050-6da9781a4fb7" -->
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

<!-- section_id: "da669be8-526c-47db-aeaf-6239e5023387" -->
## 📚 Related Documentation

<!-- section_id: "72fbf711-663f-4a89-a7ed-33aba553ab3c" -->
### Universal Context Entry Points
- **Universal Init Prompt:** `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
- **System Overview:** `0_context/SYSTEM_OVERVIEW.md`
- **Usage Guide:** `0_context/USAGE_GUIDE.md`
- **Master Index:** `0_context/MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "411e296c-267d-44a0-8a1c-d32385dafe34" -->
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

<!-- section_id: "33f61290-46ee-45d6-8515-5402fa00d87c" -->
### Universal Rules & Protocols
- **Terminal Protocol:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- **Git Commit Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- **Context Update Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

---

<!-- section_id: "56273a4e-3040-4821-a650-e745a1eae44e" -->
## 🔧 AI Apps & Tools Covered

This sub-layer documents:
- AI application installations and configurations
- CLI tools for AI services (OpenAI Codex, Claude Code, Google Gemini, etc.)
- Authentication and API key management
- Tool-specific setup instructions
- Integration patterns and best practices

<!-- section_id: "21654903-89f7-42f7-ad3c-7b48c1d6e6a8" -->
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

<!-- section_id: "ee3908d7-41d7-4354-803d-b4a2b3904b79" -->
### Claude Code CLI

**Documentation Location**:
- Main README: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md`
- Quick Start: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/QUICK_START.md`
- What Actually Works: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/WHAT_ACTUALLY_WORKS.md`

**Important Note**: Claude Code uses CLI-based MCP configuration (not config files). See MCP setup in `sub_layer_0_10_mcp_servers_and_tools_setup` for details.

<!-- section_id: "fbc455d3-0be3-4816-b80b-416a63719ab2" -->
### Google Gemini CLI

**Example Installation**:
```bash
npm install -g @google/gemini-cli
gemini login
gemini  # Start interactive CLI
```

<!-- section_id: "5da75cf9-f51e-4062-925c-91110d2839ee" -->
### Installation Checklist

When setting up a new development environment:

- [ ] Node.js and npm installed (via nvm recommended)
- [ ] OpenAI Codex CLI installed and configured
- [ ] Claude Code CLI installed (if using)
- [ ] API keys configured for respective tools
- [ ] MCP servers configured (see `sub_layer_0_10_mcp_servers_and_tools_setup`)

<!-- section_id: "1cce3fd9-619e-4e0a-bcef-5e4503edfe19" -->
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

<!-- section_id: "67427371-ffa5-4315-8d5c-5085b5825c53" -->
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

<!-- section_id: "01ada33a-d4c5-4fa3-b00f-acdafcaf236a" -->
## 📝 Documentation Structure

<!-- section_id: "e49a0f7c-fc2a-4337-bcc4-4287adc677f1" -->
### Current Status
- This README provides the entry point and navigation
- Additional documentation should be added as needed
- Keep mappings up to date if paths change

<!-- section_id: "6fcb4e60-40dc-40e0-b09b-ae70533d9191" -->
### Adding New Documentation
When adding new AI app or tool documentation:
1. Create appropriate subdirectories if needed (following trickle-down pattern)
2. Follow the universal documentation structure
3. Update this README with references
4. Ensure paths are relative to the universal context root (`<universal_context_root>/0_context/`)
5. Update the Master Documentation Index if needed
6. Follow the context update rule: `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

<!-- section_id: "15072ff5-a1d1-4ae8-80c2-ab438f281c4a" -->
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

<!-- section_id: "71f81bc8-e899-472c-97cd-3031b401c48a" -->
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

<!-- section_id: "5706713d-255d-4e6b-bfc3-6efaf404758c" -->
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

<!-- section_id: "1fe7006b-3b9e-43ec-90b9-f4c881a3ad1f" -->
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
