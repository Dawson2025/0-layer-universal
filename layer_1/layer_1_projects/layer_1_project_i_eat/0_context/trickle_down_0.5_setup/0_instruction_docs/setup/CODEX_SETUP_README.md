---
resource_id: "bf5d4745-fae6-4434-b88b-e7fa0faf9c3b"
resource_type: "document"
resource_name: "CODEX_SETUP_README"
---
# OpenAI Codex CLI Setup Guide

<!-- section_id: "46d6e1c9-2586-4baf-b5f6-4fc09abcb897" -->
## ✅ Installation Complete!

The OpenAI Codex CLI has been successfully installed in your Cursor environment.

<!-- section_id: "98785b91-3d05-405c-8ed0-4dd76d9a46e5" -->
## 🚀 Quick Start

<!-- section_id: "ca823969-33f7-4999-999d-4c7f69efedb2" -->
### 1. Set up your API Key

Before using Codex CLI, you need to set up your OpenAI API key:

1. Get your API key from: https://platform.openai.com/settings/organization/api-keys
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

<!-- section_id: "204fc46d-4fd1-40ac-8bae-9d791800004e" -->
### 2. Load the Codex Environment

To use Codex CLI in any terminal session, run:

```bash
source .codex_alias
```

This will:
- Load Node.js v22.19.0
- Make the `codex` command available
- Show version information

<!-- section_id: "48b6cc20-f78a-4c05-95d0-d52c228bd048" -->
### 3. Using Codex CLI

Once the environment is loaded and API key is set:

```bash
# Get help
codex --help

# Example usage (replace with actual commands from the help)
codex generate "function to sort an array"
```

<!-- section_id: "a730c426-080f-4052-870a-35523e4c8801" -->
## 📁 Files Created

- `setup_codex.sh` - Setup script to verify installation
- `.codex_alias` - Environment setup for shell sessions
- `CODEX_SETUP_README.md` - This documentation

<!-- section_id: "d5bf014b-6abc-4456-b52f-47ae747a88fa" -->
## 🔧 Technical Details

- **Node.js Version**: v22.19.0 (installed via nvm)
- **npm Version**: v10.9.3
- **Codex CLI Version**: 0.30.0
- **Installation Method**: nvm + npm global install

<!-- section_id: "f72a301c-40bd-41d7-a131-13ca7f252e56" -->
## 🛠️ Troubleshooting

1. **Command not found**: Run `source .codex_alias` first
2. **API key errors**: Ensure `OPENAI_API_KEY` is set correctly
3. **Permission errors**: The setup script should handle permissions automatically

<!-- section_id: "76637315-af3d-4f78-983c-bc220e37d120" -->
## 💡 Tips

- Add `source /home/runner/workspace/.codex_alias` to your `~/.bashrc` for automatic loading
- The Codex CLI will check for your API key automatically when running commands
