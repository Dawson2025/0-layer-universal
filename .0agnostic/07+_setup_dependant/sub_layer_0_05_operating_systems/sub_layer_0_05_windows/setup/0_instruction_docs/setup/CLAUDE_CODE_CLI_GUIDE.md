---
resource_id: "a12334c8-67f2-4010-88c1-51b62de670f3"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "d54ac4fa-25f4-4b02-93e3-ff9c6207b0a9" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "19d6fe65-9881-4fe5-9157-3a323d4cee4a" -->
## 🚀 Quick Start

<!-- section_id: "300991de-148b-415b-ab05-66d2dbdf46d1" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "48ecfc70-0e8e-41d6-b7c7-2a7230130b0b" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "8afbf0cd-0d41-4af8-8bf5-b71f8f7213f5" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "f3cb5f08-36cc-4ab1-8ad3-9e286a6983f2" -->
## 💡 Example Usage

<!-- section_id: "5bb7dc3e-c0f9-4df1-893a-704789509962" -->
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

<!-- section_id: "145277d5-f4c2-4fdb-878b-2a753237d300" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "1bf4f3d7-8aa6-4021-9fb9-2f96974a52c1" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "ad2f01d3-c886-4e9c-a2b3-dac687cad71c" -->
## 🔧 Environment Setup

<!-- section_id: "c7b46e46-b775-4719-a780-55451188bd1a" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "61f149f8-1c25-4805-a070-a6dec171ef2b" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "9f7bf013-45dd-488d-85bb-a4d2d19f993c" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "b3bbcb9f-bbc0-4663-ad61-7dac2de19747" -->
## 🛠️ Troubleshooting

<!-- section_id: "a7a6e8d4-9298-4a6e-b263-ba763567a933" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "a7c60833-ceb4-4e7c-988d-7519e36d6366" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "76ced327-3452-4bc7-9309-dacaff0082d1" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "e86e1ab4-5e13-4ee0-8a45-0849c3d16b78" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
