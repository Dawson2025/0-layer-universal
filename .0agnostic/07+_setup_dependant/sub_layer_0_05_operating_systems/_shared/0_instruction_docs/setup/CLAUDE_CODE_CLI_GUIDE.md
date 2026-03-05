---
resource_id: "ce5c107f-1574-483b-a5ac-5395ed27996f"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "32280e5d-1814-4caa-8d32-c07320188988" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "a79c3ae1-c1a2-4cfb-8123-8a7fcf26fcea" -->
## 🚀 Quick Start

<!-- section_id: "ced83f47-1aa1-47a9-949f-634ccc64209c" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "84f3a6b6-99c5-4776-b5f9-695605d715df" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "c3b1f44b-cbd4-4731-85b2-116a80995b85" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "7b23226e-9227-40b4-abfb-c652cefd28a6" -->
## 💡 Example Usage

<!-- section_id: "0d1d22e9-7965-4e05-8c3d-a64f57c378d0" -->
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

<!-- section_id: "db464653-3997-473b-9ae0-ee60ea82a2aa" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "3be3fb27-99ff-471d-84dc-fdabfbb7a35d" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "2aa18112-41f0-464f-bba1-9fae171acba6" -->
## 🔧 Environment Setup

<!-- section_id: "e84abf9e-9487-482c-909a-9aea5b42e959" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "f281abf2-c0c1-4212-9d4f-a066c8940de4" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "394ae185-96f1-420e-bb54-19d07baf1403" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "c0cd6e38-00b6-4336-850d-99c1b782e593" -->
## 🛠️ Troubleshooting

<!-- section_id: "64d78d85-6a48-4182-a76c-288ffb82ef54" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "845c3009-68a0-4f20-99dd-77562f73b2c3" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "7173e8be-a530-40a2-ab70-dd5350dc85c4" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "8d46a7af-df01-462e-853a-9b509d40eb1b" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
