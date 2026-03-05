---
resource_id: "77311a20-0aa3-4260-8ea7-b2f0eb0ff4f6"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "06559fb2-d91a-40d2-a619-2403ea3c4121" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "a99f7b98-16d5-47b1-a7ea-3c4cda48df6e" -->
## 🚀 Quick Start

<!-- section_id: "6ed6f939-d1c0-4f5f-bd44-e1d1eeecc263" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "10694ceb-70a9-45cd-8e0f-6a646a04d2f9" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "2030b7f0-55ef-4fcf-a2ff-907123b1f4eb" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "0daa48e6-0ae2-40c2-834b-1e24c3aca125" -->
## 💡 Example Usage

<!-- section_id: "2e701197-55ff-405c-a855-183f6c050fab" -->
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

<!-- section_id: "c948a8f6-e903-4902-bffc-c6f4dcea84a9" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "4c9c0dec-9d0e-4353-8b3d-5448b79c7d19" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "40e98b52-988f-4d86-8cb3-d1a560642b16" -->
## 🔧 Environment Setup

<!-- section_id: "7643ad1b-8623-4eec-8da1-29f66d3f3b58" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "fb24377a-478c-4f18-9c9b-19bbdd3a6ab3" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "3fbb38dd-585e-4196-a9f6-52c2799fe021" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "30ab60f7-31e5-48ec-864c-52e0f9c4c0b3" -->
## 🛠️ Troubleshooting

<!-- section_id: "6aa5a39f-4be5-4e70-9bfe-d18fde6c4448" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "ed4c0aab-4644-49d1-ba37-e99b2be45f32" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "ff18bd56-5e27-414e-be8e-0a6631a485ad" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "8386a345-8c03-4d5d-b9e3-3d5b2c297572" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
