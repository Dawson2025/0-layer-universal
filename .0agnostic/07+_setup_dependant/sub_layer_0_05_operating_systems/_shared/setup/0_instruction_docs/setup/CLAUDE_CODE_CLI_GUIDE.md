---
resource_id: "e9f18d40-5327-40e5-af2b-55d7299b5fc3"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

## 🚀 Quick Start

### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

## 💡 Example Usage

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

### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

## 🔧 Environment Setup

### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

## 🛠️ Troubleshooting

### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
