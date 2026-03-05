---
resource_id: "738fc975-5c5b-4783-bfa2-122ff0756fa1"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "3feb5754-0396-476b-8982-fdcba1f62064" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "f293842c-fc03-4768-bdd5-e9e18f0865db" -->
## 🚀 Quick Start

<!-- section_id: "7f4ba488-b8e0-4539-bc16-9bdb05eb0293" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "0fb35f45-c8a4-410f-b429-e91dc1bc0fc9" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "151c039c-778d-4098-80a4-dfa7b49c6c19" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "b1ebc777-f974-4754-825e-917037f46de7" -->
## 💡 Example Usage

<!-- section_id: "2d429f3c-0faa-45f6-ad48-cc45b083094c" -->
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

<!-- section_id: "f8640c28-e4f0-48c5-ab9d-11ea4d6e268c" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "97100793-3804-4482-b6b2-28d02041077f" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "6a4b623e-a3a1-4382-bf42-37fd8ab5ceea" -->
## 🔧 Environment Setup

<!-- section_id: "6ea95aa3-804f-4427-9fdb-083189b4fee3" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "5c848c34-0f66-4b73-bf49-a34fad4ac734" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "f195e625-7daf-464e-bb20-4294d667a6b7" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "f0b9f87c-f1b2-4d55-a301-f205ec08940f" -->
## 🛠️ Troubleshooting

<!-- section_id: "24a2a6f8-c788-4462-8ee9-1f3255eb96c7" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "bfde19f4-bc9a-4661-9891-a68b40d7e6b2" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "853263a3-43d7-4daf-8362-3ccfd8f7e2e2" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "07c81110-4440-47fd-9110-76970a42fb7a" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
