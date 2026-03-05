---
resource_id: "70ce3fbe-e47e-4002-b767-0ab9893fa384"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "80219df1-ea1e-4ed8-93ca-73b395c33178" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "040b125d-c2dc-4847-9252-8fd3cc51a260" -->
## 🚀 Quick Start

<!-- section_id: "253381a2-8418-4beb-b2da-df27c8b95443" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "174ffab4-07ab-4016-8949-d7fbe799759b" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "3d61f256-d158-4054-8ba4-bf754dde66b8" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "99012f4b-8950-42ba-a4fa-b78e430da2f1" -->
## 💡 Example Usage

<!-- section_id: "9e051210-a709-47be-8824-cef292bfa20c" -->
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

<!-- section_id: "deb76c42-5d10-4b3a-b87c-13bfb14dc050" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "026728c1-875c-4491-bef8-0708e8759d01" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "6193e6a3-bb90-40a7-82bf-d9169dc58b41" -->
## 🔧 Environment Setup

<!-- section_id: "f07bb397-6ad1-4d91-be25-283a40ea1c27" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "928b18b7-3b91-4f5f-ba07-d2ce9058a7e2" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "c55b6ab4-dbd1-4e12-a350-dfdaddc052f2" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "87d09557-344f-4f03-873b-74a9daea054c" -->
## 🛠️ Troubleshooting

<!-- section_id: "ade94328-26ff-471b-b9bd-5928ef07a55d" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "a6399e9b-71e4-4f1e-b98d-94e553e22c7f" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "4fa00bc7-fd87-4809-bffb-cdee15f2eab5" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "c1c0f979-5f8a-4602-a2b2-bb5c602ac817" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
