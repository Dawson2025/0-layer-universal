---
resource_id: "e7f7eeef-63af-4053-bc8e-051bc4a36939"
resource_type: "document"
resource_name: "CODEX_SETUP_README"
---
# OpenAI Codex CLI Setup Guide

<!-- section_id: "ec3a8872-bc12-465e-86a7-fd62d9e96397" -->
## ✅ Installation Complete!

The OpenAI Codex CLI has been successfully installed in your Cursor environment.

<!-- section_id: "2a25c12a-7d73-4ed3-9718-d78e54ec4ab6" -->
## 🚀 Quick Start

<!-- section_id: "609efa22-0334-447f-b118-d1b7ed6cebdb" -->
### 1. Set up your API Key

Before using Codex CLI, you need to set up your OpenAI API key:

1. Get your API key from: https://platform.openai.com/settings/organization/api-keys
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

<!-- section_id: "f7a2e643-6e48-418b-b938-7c5abf24dd27" -->
### 2. Load the Codex Environment

To use Codex CLI in any terminal session, run:

```bash
source .codex_alias
```

This will:
- Load Node.js v22.19.0
- Make the `codex` command available
- Show version information

<!-- section_id: "fd139cd4-cb65-4743-8691-1dab16acf07a" -->
### 3. Using Codex CLI

Once the environment is loaded and API key is set:

```bash
# Get help
codex --help

# Example usage (replace with actual commands from the help)
codex generate "function to sort an array"
```

<!-- section_id: "9c18b9a9-48ad-4f77-9ee3-78c0d3a43b55" -->
## 📁 Files Created

- `setup_codex.sh` - Setup script to verify installation
- `.codex_alias` - Environment setup for shell sessions
- `CODEX_SETUP_README.md` - This documentation

<!-- section_id: "8a165dbb-1b7a-4a09-b0a8-323b05016188" -->
## 🔧 Technical Details

- **Node.js Version**: v22.19.0 (installed via nvm)
- **npm Version**: v10.9.3
- **Codex CLI Version**: 0.30.0
- **Installation Method**: nvm + npm global install

<!-- section_id: "6e6b69ff-ab8b-4dd1-b262-c1f0887eb5dc" -->
## 🛠️ Troubleshooting

1. **Command not found**: Run `source .codex_alias` first
2. **API key errors**: Ensure `OPENAI_API_KEY` is set correctly
3. **Permission errors**: The setup script should handle permissions automatically

<!-- section_id: "0d53c1bb-8818-4471-b680-fc4ef8142fbb" -->
## 💡 Tips

- Add `source /home/runner/workspace/.codex_alias` to your `~/.bashrc` for automatic loading
- The Codex CLI will check for your API key automatically when running commands
