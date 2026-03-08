---
resource_id: "1bfbac1d-7615-4953-9bf1-20a81642648d"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.09: AI Apps & Tools Setup

**Purpose:** This sub-layer contains documentation and setup instructions for AI applications and tools used across all projects.

**Location in Layer System:**
- Universal Layer: `layer_0/0.02_sub_layers/sub_layer_0_09_ai_apps_tools_setup/`
- Referenced in: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`

---

<!-- section_id: "199e16f9-d6d6-474f-89f2-7ce58a0e1c90" -->
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

<!-- section_id: "0a9fcdfa-392b-43f2-8e59-a24df9dab69a" -->
## 📚 Related Documentation

<!-- section_id: "15cbcd46-3991-4096-9745-91345a32700c" -->
### Universal Context Entry Points
- **Universal Init Prompt:** `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md`
- **System Overview:** `0_context/SYSTEM_OVERVIEW.md`
- **Usage Guide:** `0_context/USAGE_GUIDE.md`
- **Master Index:** `0_context/MASTER_DOCUMENTATION_INDEX.md`

<!-- section_id: "e99b4e71-a89e-4a00-aa84-4c2db43afb67" -->
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

<!-- section_id: "68d051f8-4a09-460f-92bf-1b58b2ef60b2" -->
### Universal Rules & Protocols
- **Terminal Protocol:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- **Git Commit Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
- **Context Update Rules:** `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

---

<!-- section_id: "26a5d8dd-080b-44c9-9ab8-bf354e35bee6" -->
## 🔧 AI Apps & Tools Covered

This sub-layer documents:
- AI application installations and configurations
- CLI tools for AI services (OpenAI Codex, Claude Code, Google Gemini, etc.)
- Authentication and API key management
- Tool-specific setup instructions
- Integration patterns and best practices

<!-- section_id: "ffe8dc38-73b1-4df2-9e7a-3ca8f4475178" -->
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

<!-- section_id: "7f9ed02e-1eb5-44a2-9b37-593b321a83f7" -->
### Claude Code CLI

**Documentation Location**:
- Main README: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md`
- Quick Start: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/QUICK_START.md`
- What Actually Works: `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/WHAT_ACTUALLY_WORKS.md`

**Important Note**: Claude Code uses CLI-based MCP configuration (not config files). See MCP setup in `sub_layer_0_10_mcp_servers_and_tools_setup` for details.

<!-- section_id: "100479fa-a098-4b98-8051-53b933e4df4a" -->
### Google Gemini CLI

**Example Installation**:
```bash
npm install -g @google/gemini-cli
gemini login
gemini  # Start interactive CLI
```

<!-- section_id: "7d925a31-1222-4ce9-a3fb-63c3a4b53777" -->
### Installation Checklist

When setting up a new development environment:

- [ ] Node.js and npm installed (via nvm recommended)
- [ ] OpenAI Codex CLI installed and configured
- [ ] Claude Code CLI installed (if using)
- [ ] API keys configured for respective tools
- [ ] MCP servers configured (see `sub_layer_0_10_mcp_servers_and_tools_setup`)

<!-- section_id: "cd6a7732-16bb-418c-9a6c-9b7e1646e04d" -->
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

<!-- section_id: "ddf5f865-5cd7-49c9-8ca6-0246ad69f799" -->
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

<!-- section_id: "76d28839-0928-4ad8-8298-c890458c8104" -->
## 📝 Documentation Structure

<!-- section_id: "3fa0793b-ce32-4c71-9ed4-919f70988aef" -->
### Current Status
- This README provides the entry point and navigation
- Additional documentation should be added as needed
- Keep mappings up to date if paths change

<!-- section_id: "6b6a934f-f936-4f25-b9d1-57e238a491ce" -->
### Adding New Documentation
When adding new AI app or tool documentation:
1. Create appropriate subdirectories if needed (following trickle-down pattern)
2. Follow the universal documentation structure
3. Update this README with references
4. Ensure paths are relative to the universal context root (`<universal_context_root>/0_context/`)
5. Update the Master Documentation Index if needed
6. Follow the context update rule: `layer_0/0.04_universal_rules/trickle_down_0_universal/0_instruction_docs/context_update_rule.md`

<!-- section_id: "b002bdaf-075b-40e8-b35e-3d6671e0e4d5" -->
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

<!-- section_id: "049daa8f-4b84-401e-9268-0b735a0b6690" -->
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

<!-- section_id: "1ae5d8c0-2653-4cb9-be4a-d37a025f30cd" -->
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

<!-- section_id: "91853a8a-5e4f-4aef-8074-100cac588b24" -->
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
