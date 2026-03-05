---
resource_id: "ff780486-49c9-4154-a581-13c76ccb552a"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "8dc87e9e-11f5-4cb0-8909-315bf5ab6564" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "f70fb7f6-bae4-4780-8e5d-525773898f99" -->
## 🚀 Quick Start

<!-- section_id: "f2a4ec45-5d05-4751-be10-8f21cd61fb0d" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "d201b38d-6df1-4b75-82bd-6b5bead674a1" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "975234fa-dd34-4b77-a3c5-5619a4f4fedf" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "44f74454-51dc-4626-bae9-ab5730c5f2ec" -->
## 💡 Example Usage

<!-- section_id: "ea72c371-0e7b-422b-a52d-a9ad493ef22c" -->
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

<!-- section_id: "a2ce6f8c-6f52-4e6c-8f65-ba09ea1f300f" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "72f92fb8-4871-48f7-9ee5-4b132c32c37c" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "a4fe5075-0faf-4277-b037-e8bb5d242030" -->
## 🔧 Environment Setup

<!-- section_id: "503bf9f9-c920-49c1-ab4b-8259282f534a" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "aba3e554-72fd-4343-8a33-6bebd38d2dee" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "197b4468-212f-4946-8980-006d275220e2" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "57bc55a8-8317-4d2c-bb75-5f8d445c4c8d" -->
## 🛠️ Troubleshooting

<!-- section_id: "10251561-de85-45dc-8a3b-ac0c6888058b" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "3b6174f6-d4a4-4c12-84c2-b1dbff6ad84b" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "f5babebf-3b9a-48f0-8c68-1d2aa00dffeb" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "7bd405bc-f6d2-4680-97e0-105c88864678" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
