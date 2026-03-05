---
resource_id: "e9f18d40-5327-40e5-af2b-55d7299b5fc3"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "26e1cfb4-38a2-46e4-a4e6-aee1edc6aabc" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "9fabcaf1-5f94-4043-8498-35f8622b3c3e" -->
## 🚀 Quick Start

<!-- section_id: "c9e97eb7-941e-415e-b02c-66627830f66f" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "ca467649-ba0c-47d0-8178-e99606488988" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "1ec3d912-b37a-446d-844e-e11e28f66331" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "39793156-1e0b-4d7d-9bb6-14ede8e4d679" -->
## 💡 Example Usage

<!-- section_id: "9b4197c8-34a7-451d-a85e-4c0c06ed1493" -->
### Interactive Mode
```bash
# Start interactive session
claude

# Then you can ask things like:
> refactor this function to use async/await
> add error handling to my API calls
> explain what this code does
> help me debug this issue
```

<!-- section_id: "ef846746-43ee-4029-bc4c-77e24d838681" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "23421535-eb63-4d76-8128-9bb0233dc883" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "d318f21f-e39d-435e-baa4-ede164799179" -->
## 🔧 Environment Setup

<!-- section_id: "f3d78778-4f43-408b-9c1f-ef1b863598b7" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "624b5c8d-4026-4f92-a532-4eac9dabf5c3" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "c604da4d-7fa3-47f9-a2ba-6e9ce72acd0b" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "1bcf783e-3c31-4cf3-83a7-9443719472ad" -->
## 🛠️ Troubleshooting

<!-- section_id: "e18c11b9-9f6a-4139-8897-e63c6deaad4d" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "768ce961-1326-43f7-91be-a4c7afa08af8" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "d73bd312-dbfe-4a4c-8576-1590376c1211" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "8f59061b-1b71-424b-9b05-b43aead7872c" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
