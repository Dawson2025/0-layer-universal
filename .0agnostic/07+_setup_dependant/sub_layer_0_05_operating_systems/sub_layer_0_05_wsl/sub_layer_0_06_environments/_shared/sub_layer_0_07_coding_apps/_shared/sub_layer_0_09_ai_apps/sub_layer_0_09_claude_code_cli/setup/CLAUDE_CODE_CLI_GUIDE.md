---
resource_id: "2c2df2de-f220-492f-849d-44b8612e02f3"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "8e528ea2-5005-4e17-91f1-a322e4dded39" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "fb9698f8-f5bc-43b3-81a6-0165b973ebe2" -->
## 🚀 Quick Start

<!-- section_id: "b58992f7-62ec-48c3-8447-3ec152aa3a28" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "85bf0c97-81a4-44fc-83c1-1f9ea3d1a61a" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "418def3b-309a-40dd-9158-e6ef6f0ec209" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "d89eaa1f-b485-46f1-baf8-84e11ac8ece8" -->
## 💡 Example Usage

<!-- section_id: "84476e0c-a698-4830-be9c-c8b3965119e0" -->
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

<!-- section_id: "948382ee-0a87-4634-a7be-15a11e3a3496" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "6464bf86-b095-48a9-a4e5-403bf1bbc92b" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "ce73c599-cc19-4ca0-ae1e-de006932dcfa" -->
## 🔧 Environment Setup

<!-- section_id: "34e94b05-ae45-4ed9-bf08-709269a1359a" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "81279fd3-7ba6-444c-8620-65a4aa4453eb" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "c45dae17-9d4b-4ebb-b80a-7676f95d9667" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "6822eeba-a4ee-47f0-9846-02208a1da390" -->
## 🛠️ Troubleshooting

<!-- section_id: "272dac1f-c057-4319-82ba-e44d4812d26c" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "4109fa45-bfbd-453e-be52-a16a03d52d96" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "470a0d25-9bed-4aa8-b6d6-307a89279fe1" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "25f56ab5-37f7-4a5a-b02e-058fe17764fd" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
