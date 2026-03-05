---
resource_id: "c179cf93-9df2-47b9-970b-c2d6d23ab4bb"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "6496c1b5-1a70-44c8-98fd-d4a1b9a54772" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "ab95ede3-9707-4a4f-8e79-f9d262c99e0a" -->
## 🚀 Quick Start

<!-- section_id: "78284dd1-2012-4e28-8724-f17a9e31a9c2" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "c58b1c58-cc46-4b86-a515-ccc414f5939f" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "3356ecc7-500b-4539-be4d-965fb8d45c73" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "94d4738d-5892-4c2d-bd29-20c463dc6fde" -->
## 💡 Example Usage

<!-- section_id: "a576a4cf-d085-4a71-bb4a-3242ba361104" -->
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

<!-- section_id: "1c79bca4-774a-4a7b-a9cc-156aafe970a3" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "b62b40e8-9f7e-4521-a000-515f43ba9ebd" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "c8f35870-4606-46b4-8fc1-49bad4c4da25" -->
## 🔧 Environment Setup

<!-- section_id: "60cc68f6-1cb6-41a2-a946-d9664e6a61b0" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "66dd03ec-efc0-49f1-84c6-e45fa003b566" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "9b4cf777-954b-4d9d-bee4-a132c66d0a14" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "6c4cbc55-5dad-4947-91f2-3e0d59782b4f" -->
## 🛠️ Troubleshooting

<!-- section_id: "9ab7539e-496e-480a-9a16-718eca0e97ce" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "fbe6aae5-b4af-48c2-aef8-e776f2d9d431" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "5c40a87c-5a36-46a3-af9c-b532a488fd7d" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "301edf51-5cec-43e4-b4d1-a2e0059f83e9" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
