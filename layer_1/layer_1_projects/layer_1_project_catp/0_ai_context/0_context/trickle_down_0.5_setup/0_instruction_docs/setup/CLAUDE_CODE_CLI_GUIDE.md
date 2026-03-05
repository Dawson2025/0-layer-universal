---
resource_id: "0e22e349-ebbc-4d14-8075-8482af50f965"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "b6f76cea-a64e-4ffa-acbe-158b26780e7d" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "6783fbc7-f2da-4cac-a4fb-41c1b9e7dd6f" -->
## 🚀 Quick Start

<!-- section_id: "e2b0e7d7-aa4b-49d1-afdd-ac32ffc39a9c" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "8e2b5a0e-9e82-4df8-a3da-4055d4ced0a7" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "414bc0b2-3877-493e-85d4-895534dd120c" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "820b69ab-4465-4112-923e-19fac8ecb647" -->
## 💡 Example Usage

<!-- section_id: "ae517468-cc3d-4135-8042-6e89812c9839" -->
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

<!-- section_id: "062312f1-7367-40b4-9c40-6ed899534fe2" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "ff83d44c-a781-42d6-a26a-4716cb2a747d" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "ab075cd3-634f-4731-97ad-c5199c5dee21" -->
## 🔧 Environment Setup

<!-- section_id: "2c21018e-efa0-4261-bc6f-761679889db9" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "c3ebe0b7-846b-4622-bb18-36ca2a88bf59" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "c384106a-e43a-4647-9faa-3db3c7558d4d" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "b15b3a9e-adc7-4f8b-ba86-1de9c8e32423" -->
## 🛠️ Troubleshooting

<!-- section_id: "f87e663c-3ceb-4494-b424-ef837968b8a8" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "67c8695b-242d-4cb1-9dff-10ae2b67563a" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "24b28221-f0ad-4682-8d79-17627fc87544" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "e400d726-a32a-4032-879f-6a30022ac6c8" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
