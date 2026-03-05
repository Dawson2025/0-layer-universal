---
resource_id: "4ef2ab87-f31e-4b44-9494-e90ae9ea03fe"
resource_type: "document"
resource_name: "CODEX_SETUP_README"
---
# OpenAI Codex CLI Setup Guide

<!-- section_id: "ade4e5c1-ada9-4a7f-98bf-513a6a88cfff" -->
## ✅ Installation Complete!

The OpenAI Codex CLI has been successfully installed in your Cursor environment.

<!-- section_id: "80c16bcb-85bb-450b-928e-3ae4024c39b1" -->
## 🚀 Quick Start

<!-- section_id: "81712946-2ec0-430d-aaaf-0423c73fc53c" -->
### 1. Set up your API Key

Before using Codex CLI, you need to set up your OpenAI API key:

1. Get your API key from: https://platform.openai.com/settings/organization/api-keys
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

<!-- section_id: "9e57d074-2958-4ec9-9b7f-f7389589c535" -->
### 2. Load the Codex Environment

To use Codex CLI in any terminal session, run:

```bash
source .codex_alias
```

This will:
- Load Node.js v22.19.0
- Make the `codex` command available
- Show version information

<!-- section_id: "4e71752f-256c-4541-9e08-c5ca996ff9d6" -->
### 3. Using Codex CLI

Once the environment is loaded and API key is set:

```bash
# Get help
codex --help

# Example usage (replace with actual commands from the help)
codex generate "function to sort an array"
```

<!-- section_id: "ee37d021-2e17-4c8f-a0a7-a1280c02636c" -->
## 📁 Files Created

- `setup_codex.sh` - Setup script to verify installation
- `.codex_alias` - Environment setup for shell sessions
- `CODEX_SETUP_README.md` - This documentation

<!-- section_id: "44e0a4f4-089c-41bc-bf1d-4c1b70361539" -->
## 🔧 Technical Details

- **Node.js Version**: v22.19.0 (installed via nvm)
- **npm Version**: v10.9.3
- **Codex CLI Version**: 0.30.0
- **Installation Method**: nvm + npm global install

<!-- section_id: "f93285ba-7a6c-4963-898e-062b6f1a6ac7" -->
## 🛠️ Troubleshooting

1. **Command not found**: Run `source .codex_alias` first
2. **API key errors**: Ensure `OPENAI_API_KEY` is set correctly
3. **Permission errors**: The setup script should handle permissions automatically

<!-- section_id: "7b3fb62a-241a-41da-acd9-21bfb2c7c1f1" -->
## 💡 Tips

- Add `source /home/runner/workspace/.codex_alias` to your `~/.bashrc` for automatic loading
- The Codex CLI will check for your API key automatically when running commands
