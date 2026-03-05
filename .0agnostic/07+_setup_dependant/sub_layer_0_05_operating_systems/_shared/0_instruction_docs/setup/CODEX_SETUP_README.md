---
resource_id: "dc0f1c43-fa01-4d46-aa98-a14e55f2db80"
resource_type: "document"
resource_name: "CODEX_SETUP_README"
---
# OpenAI Codex CLI Setup Guide

<!-- section_id: "e25429c9-6337-4577-96b2-fec9efd9a331" -->
## ✅ Installation Complete!

The OpenAI Codex CLI has been successfully installed in your Cursor environment.

<!-- section_id: "79566136-d25b-475e-80ba-e3202dbd538c" -->
## 🚀 Quick Start

<!-- section_id: "c4e6f494-57b9-40d4-9690-f49c7e8e29fb" -->
### 1. Set up your API Key

Before using Codex CLI, you need to set up your OpenAI API key:

1. Get your API key from: https://platform.openai.com/settings/organization/api-keys
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

<!-- section_id: "279460ec-9c9c-49f9-9246-f7649ee430c4" -->
### 2. Load the Codex Environment

To use Codex CLI in any terminal session, run:

```bash
source .codex_alias
```

This will:
- Load Node.js v22.19.0
- Make the `codex` command available
- Show version information

<!-- section_id: "0e5c3d3d-abd5-493b-9d3d-19634b70ec03" -->
### 3. Using Codex CLI

Once the environment is loaded and API key is set:

```bash
# Get help
codex --help

# Example usage (replace with actual commands from the help)
codex generate "function to sort an array"
```

<!-- section_id: "adf29102-9f3d-48c3-887c-98c78a4d06d1" -->
## 📁 Files Created

- `setup_codex.sh` - Setup script to verify installation
- `.codex_alias` - Environment setup for shell sessions
- `CODEX_SETUP_README.md` - This documentation

<!-- section_id: "2cf82a23-76b9-4d8b-8c01-88bf42ba127c" -->
## 🔧 Technical Details

- **Node.js Version**: v22.19.0 (installed via nvm)
- **npm Version**: v10.9.3
- **Codex CLI Version**: 0.30.0
- **Installation Method**: nvm + npm global install

<!-- section_id: "eba6b83e-0e9a-424a-b774-0d1a5823306d" -->
## 🛠️ Troubleshooting

1. **Command not found**: Run `source .codex_alias` first
2. **API key errors**: Ensure `OPENAI_API_KEY` is set correctly
3. **Permission errors**: The setup script should handle permissions automatically

<!-- section_id: "adea2de6-8bad-4fa6-89bb-8a5a9d9dae27" -->
## 💡 Tips

- Add `source /home/runner/workspace/.codex_alias` to your `~/.bashrc` for automatic loading
- The Codex CLI will check for your API key automatically when running commands
