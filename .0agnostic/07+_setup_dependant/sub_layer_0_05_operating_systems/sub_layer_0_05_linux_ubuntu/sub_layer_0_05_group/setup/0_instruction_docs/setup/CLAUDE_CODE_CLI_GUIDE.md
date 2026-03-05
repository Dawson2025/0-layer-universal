---
resource_id: "1931d07b-31a2-4ca9-a1bf-0c799a32482e"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "a212d1f9-5f9d-46ef-82f5-03fcb422cf9c" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "540efa37-ccc3-4c72-a148-a5f0f673fae7" -->
## 🚀 Quick Start

<!-- section_id: "f3198bc5-4024-45f1-a76e-ac8b64f566d5" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "622c6503-b473-41ea-8d7a-49a9b62f8959" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "d091eef1-132a-479e-9215-3ccd97966505" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "061f71b1-bc8a-4376-995b-248626f17c0b" -->
## 💡 Example Usage

<!-- section_id: "71fa8bd5-238b-4e19-8005-286f03639337" -->
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

<!-- section_id: "ba437480-2797-4fa5-88fb-9c227cf798eb" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "ef8ba369-debe-46fc-a6e7-b89d65263594" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "5ea407cc-b2f2-4b2f-b859-19c29cdb06a1" -->
## 🔧 Environment Setup

<!-- section_id: "5f3e0e6c-3b46-454c-b6af-98cf91295188" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "96bc7b24-8cac-4a01-813f-abcda95d5832" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "cdca6ca4-766e-49d7-93d0-986b1a5fa012" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "de034acf-48fb-4638-8ac4-a410d9953b3c" -->
## 🛠️ Troubleshooting

<!-- section_id: "c8778185-4ca7-4e58-8849-87eaf8fd1505" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "aa0842e0-523c-4e4b-9666-c84dc40bd8d7" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "13cb6b47-4495-4699-a485-c4fac7a716ca" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "a5f7b610-9b76-4465-bd05-358e59b4889e" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
