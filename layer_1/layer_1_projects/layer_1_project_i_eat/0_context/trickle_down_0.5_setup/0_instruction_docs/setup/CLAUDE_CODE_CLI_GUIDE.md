---
resource_id: "940a7e31-5d1b-424b-b15b-e37ff43c10fa"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "292cf850-2bca-4932-bef8-449a815eb50b" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "cb2c547b-3b52-44ec-b151-11ecb7907d64" -->
## 🚀 Quick Start

<!-- section_id: "45d09c80-388e-4e45-9642-a014dd476f33" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "f6748aab-329b-4820-af2d-ba06b6e171f9" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "b336d08a-16ed-410b-800b-31db0d1f2e44" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "b6022dfa-3053-48ae-99f6-7226400d1a21" -->
## 💡 Example Usage

<!-- section_id: "a813c6ec-3586-4538-b866-aae7411be885" -->
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

<!-- section_id: "8548ec35-2965-46c9-8553-844884b505db" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "27aa8ec5-bd6a-484d-a6d0-eedc08f73a9a" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "10434c08-956b-436b-8dc8-385d735eca68" -->
## 🔧 Environment Setup

<!-- section_id: "9299553a-00a3-4a70-b3a6-f697f1afe4ca" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "09e7fd7d-fac8-4bdc-a210-6034c6dd5499" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "89f317c7-2f35-46e8-b6a3-a96e3b12566d" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "615240b5-67b7-40f9-b034-81b8828d845f" -->
## 🛠️ Troubleshooting

<!-- section_id: "bfbbefa6-064d-43c9-a206-668c316ef9ed" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "a37f9007-99df-49ae-87e0-825876040e53" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "b5b5aca3-7131-46a6-a474-28c94177c6fb" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "74235230-2f9c-4db4-9952-afa03aea5875" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
