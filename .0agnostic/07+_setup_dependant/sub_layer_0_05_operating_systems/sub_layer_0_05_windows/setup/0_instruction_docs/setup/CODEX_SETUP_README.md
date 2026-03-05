---
resource_id: "cd127b31-02cb-432c-a4b9-ed986f5d9523"
resource_type: "document"
resource_name: "CODEX_SETUP_README"
---
# OpenAI Codex CLI Setup Guide

<!-- section_id: "87370820-6eee-4746-b6b3-797ab2e12867" -->
## ✅ Installation Complete!

The OpenAI Codex CLI has been successfully installed in your Cursor environment.

<!-- section_id: "c759af71-3e97-4b96-8af1-9e309e0db450" -->
## 🚀 Quick Start

<!-- section_id: "42a6dc0a-10fa-4697-a47d-4c11fe9f1d19" -->
### 1. Set up your API Key

Before using Codex CLI, you need to set up your OpenAI API key:

1. Get your API key from: https://platform.openai.com/settings/organization/api-keys
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

<!-- section_id: "805a5796-0cfe-458c-b69d-7a1ab5266e8c" -->
### 2. Load the Codex Environment

To use Codex CLI in any terminal session, run:

```bash
source .codex_alias
```

This will:
- Load Node.js v22.19.0
- Make the `codex` command available
- Show version information

<!-- section_id: "6cfb55e0-de8a-4b9b-84cd-e2062cbd889c" -->
### 3. Using Codex CLI

Once the environment is loaded and API key is set:

```bash
# Get help
codex --help

# Example usage (replace with actual commands from the help)
codex generate "function to sort an array"
```

<!-- section_id: "852f8c8f-6072-42b5-bde1-b902dba4b727" -->
## 📁 Files Created

- `setup_codex.sh` - Setup script to verify installation
- `.codex_alias` - Environment setup for shell sessions
- `CODEX_SETUP_README.md` - This documentation

<!-- section_id: "fe7ed9eb-cd28-4386-8ed4-b7a281843b75" -->
## 🔧 Technical Details

- **Node.js Version**: v22.19.0 (installed via nvm)
- **npm Version**: v10.9.3
- **Codex CLI Version**: 0.30.0
- **Installation Method**: nvm + npm global install

<!-- section_id: "1cdf5f75-d507-4244-9fbd-e418ca6ff292" -->
## 🛠️ Troubleshooting

1. **Command not found**: Run `source .codex_alias` first
2. **API key errors**: Ensure `OPENAI_API_KEY` is set correctly
3. **Permission errors**: The setup script should handle permissions automatically

<!-- section_id: "c04b1215-717e-403f-98ae-cb831fe8fa1b" -->
## 💡 Tips

- Add `source /home/runner/workspace/.codex_alias` to your `~/.bashrc` for automatic loading
- The Codex CLI will check for your API key automatically when running commands
