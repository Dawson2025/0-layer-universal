---
resource_id: "0f883a6a-4514-4a23-984e-6f398b17c418"
resource_type: "document"
resource_name: "bash-wrapper-setup"
---
# Claude Code Bash Wrapper Setup Guide
*Advanced Configuration: Conditional Bypass Permissions via Shell Wrapper*

<!-- section_id: "f82bc443-c80f-42f5-85dc-cf517f1f1df1" -->
## Overview

This guide documents how to create a bash wrapper function that conditionally enables bypass permissions based on your current directory or environment variables. This approach provides more flexibility than configuration files alone.

<!-- section_id: "f0782cbb-a0c2-48c4-88ed-9e9bca4ac1c2" -->
## Why Use a Bash Wrapper?

<!-- section_id: "52efe12f-aaa3-4f5f-8f99-0bfc49035844" -->
### Advantages

✅ **Context-Aware Bypass**
- Enable bypass only in specific directories
- Control via environment variables
- Different behavior per project

✅ **No Configuration File Changes**
- Works without modifying `.claude/settings.json`
- Doesn't affect version-controlled settings
- Easy to enable/disable globally

✅ **Granular Control**
- Per-directory automation
- Per-session control via environment variables
- Preserves help/version commands

<!-- section_id: "7f53a0a4-3f3f-455b-92db-3ca555b8586e" -->
### Disadvantages

❌ **Shell-Specific**
- Only works in bash/zsh
- Doesn't affect Claude Code launched from GUI
- Must configure each shell environment

❌ **Less Discoverable**
- Hidden in shell config files
- Team members won't automatically get it
- Harder to audit than configuration files

<!-- section_id: "62de2a66-6d3a-40c4-93d1-391cef9899fe" -->
## Implementation

<!-- section_id: "3adefaed-591b-4ab6-8de4-3ed0f868096d" -->
### Method 1: Project Directory-Based Bypass

This wrapper enables bypass permissions automatically when you're in a specific project directory.

#### Step 1: Find Claude Binary Path

```bash
which claude
# Output example: /home/username/.nvm/versions/node/v22.20.0/bin/claude
```

Store this path - you'll need it for the wrapper.

#### Step 2: Add Wrapper to ~/.bashrc

Open your `~/.bashrc` (or `~/.zshrc` for zsh):

```bash
nano ~/.bashrc
```

Add this function at the end:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when in project directory
    if [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Important**: Replace:
- `/home/username/.nvm/versions/node/v22.20.0/bin/claude` with your actual path from step 1
- `/home/username/code/my-project` with your project path

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Wrapper

```bash
# Check the wrapper function exists
typeset -f claude

# Test inside your project directory
cd /home/username/code/my-project
claude -p "echo 'testing bypass'"
# Should run without permission prompts

# Test outside your project directory
cd /tmp
claude -p "echo 'testing normal'"
# Should run with normal permission behavior
```

<!-- section_id: "09b76e88-277d-490f-a680-f68ad11cd582" -->
### Method 2: Environment Variable-Based Bypass

Enable bypass permissions on-demand with an environment variable.

```bash
# >>> CLAUDE_WRAPPER_ENV_VAR_START
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_ENV_VAR_END
```

**Usage:**

```bash
# Normal mode (with permissions)
claude

# Bypass mode (for this session)
CLAUDE_UNSAFE=1 claude

# Or set for entire session
export CLAUDE_UNSAFE=1
claude
# ... work without prompts ...
unset CLAUDE_UNSAFE  # Back to normal
```

<!-- section_id: "b45380f2-39ed-4281-b5bf-b0c7009b726f" -->
### Method 3: Combined Approach (Recommended)

Combine both methods for maximum flexibility:

```bash
# >>> CLAUDE_WRAPPER_COMBINED_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 OR in project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_COMBINED_END
```

**Behavior:**
- Inside `/home/username/code/my-project`: Bypass enabled automatically
- Outside that directory: Normal permissions
- Anywhere with `CLAUDE_UNSAFE=1`: Bypass enabled
- `--help` and `--version`: Always work normally

<!-- section_id: "d8197388-c6ae-4986-ab4b-67295d69561a" -->
## Real-World Example

Here's the exact wrapper from the Lang-Trak project:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/dawson/.nvm/versions/node/v22.20.0/bin/claude"
if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 or when in the project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/dawson/code/lang-trak-in-progress"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Testing Results:**
```bash
# Inside project
$ cd /home/dawson/code/lang-trak-in-progress
$ claude -p "echo hello"
hello  # No permission prompt

# Outside project
$ cd /tmp
$ claude -p "echo hello"
# Permission prompt appears (normal behavior)

# Override from outside project
$ cd /tmp
$ CLAUDE_UNSAFE=1 claude -p "echo hello"
hello  # No permission prompt
```

<!-- section_id: "4751af7f-c4da-4025-a290-36761d3ace9c" -->
## Advanced Configurations

<!-- section_id: "39a32556-6221-45c9-be2e-ad6b74c5484d" -->
### Multiple Project Directories

Enable bypass for multiple projects:

```bash
claude() {
  # ... help/version handling ...

  # List of trusted project directories
  local trusted_dirs=(
    "/home/username/code/personal-project"
    "/home/username/code/side-project"
    "/home/username/experiments"
  )

  # Check if current directory starts with any trusted path
  local bypass=0
  for dir in "${trusted_dirs[@]}"; do
    if [[ "$PWD" == "$dir"* ]]; then
      bypass=1
      break
    fi
  done

  # Enable bypass if in trusted directory or CLAUDE_UNSAFE=1
  if [ "$bypass" = "1" ] || [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "b68f6d38-6d56-4edf-925a-6c3487410eef" -->
### Time-Based Bypass

Automatically disable bypass during certain hours (e.g., working hours for client projects):

```bash
claude() {
  # ... help/version handling ...

  # Get current hour (0-23)
  local hour=$(date +%H)

  # Disable bypass during working hours (9 AM - 5 PM)
  if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then
    # Normal mode during work hours
    command "$_claude_real" "$@"
  else
    # Bypass enabled outside work hours
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/personal"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  fi
}
```

<!-- section_id: "83739af0-fe13-402b-b701-ddc4655cd26d" -->
### Git Repository Detection

Enable bypass only in git repositories you own:

```bash
claude() {
  # ... help/version handling ...

  # Check if in a git repo
  if git rev-parse --git-dir > /dev/null 2>&1; then
    # Get git user email
    local git_email=$(git config user.email)

    # Enable bypass if it's your personal email
    if [[ "$git_email" == "personal@example.com" ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  else
    # Not in a git repo - normal mode
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "46f93362-ee52-49d3-bf26-6e22136ac9c0" -->
## Debugging

<!-- section_id: "9552dde8-a513-407d-9621-d2f9fb0dec21" -->
### Check if Wrapper is Active

```bash
# View the current wrapper function
typeset -f claude

# Check which claude command is being used
type claude
# Should output: claude is a function
```

<!-- section_id: "aa708344-e586-4024-a31e-6999f7e7ad00" -->
### Test Without Wrapper

To temporarily bypass the wrapper and use the real binary:

```bash
# Use full path
/home/username/.nvm/versions/node/v22.20.0/bin/claude

# Or use command builtin
command /path/to/real/claude
```

<!-- section_id: "3eb68022-2b2d-4a32-849d-9fb988522075" -->
### Enable Debug Output

Add debugging to your wrapper:

```bash
claude() {
  # Debug mode
  if [ "${CLAUDE_DEBUG:-0}" = "1" ]; then
    echo "[DEBUG] PWD: $PWD"
    echo "[DEBUG] CLAUDE_UNSAFE: ${CLAUDE_UNSAFE:-0}"
    echo "[DEBUG] Will use bypass: $([ condition ] && echo yes || echo no)"
  fi

  # ... rest of wrapper ...
}
```

Usage:
```bash
CLAUDE_DEBUG=1 claude -p "echo test"
```

<!-- section_id: "28bab428-6c3b-413d-8307-429fa96e97ec" -->
## Removing the Wrapper

<!-- section_id: "47359c56-cc54-44c7-b996-6d4faddcd21a" -->
### Temporary Removal (Current Session)

```bash
unset -f claude
```

<!-- section_id: "9e86a39d-f40e-461e-b195-24e06fe8c25c" -->
### Permanent Removal

1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```

2. Remove the wrapper block (between the comment markers)

3. Reload shell:
   ```bash
   source ~/.bashrc
   ```

4. Verify:
   ```bash
   type claude
   # Should output the path to the binary, not "claude is a function"
   ```

<!-- section_id: "d1927fc1-74ba-42bc-a092-f481edc3c43a" -->
## Security Considerations

<!-- section_id: "fc14c27c-58b6-4a2c-b01a-a34f7c0760eb" -->
### Risks

⚠️ **Directory-Based Bypass**
- Anyone with access to the directory gets bypass mode
- Symbolic links could potentially exploit path matching
- Subdirectories inherit bypass behavior

⚠️ **Environment Variable Bypass**
- Environment variables can be set by scripts
- Child processes inherit `CLAUDE_UNSAFE=1`
- Easy to forget it's enabled

⚠️ **Shell Configuration Files**
- `~/.bashrc` is executable code
- Errors can break your shell
- Hard for others to discover the bypass is active

<!-- section_id: "6be70e26-8458-4a00-9444-90c95dac9ac8" -->
### Mitigations

✅ **Add Visual Indicators**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "⚠️  BYPASS MODE ACTIVE" >&2
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Log Bypass Usage**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "$(date): Bypass enabled in $PWD" >> ~/.claude/bypass.log
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Restrict by Ownership**

```bash
claude() {
  # Only enable bypass if you own the directory
  if [ -O "$PWD" ] && [[ "$PWD" == "/home/username/code"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "e39b8ca3-79fc-43af-a654-1e909fa0ba4d" -->
## Integration with Configuration Files

The bash wrapper approach **works alongside** `.claude/settings.json` configurations:

<!-- section_id: "53b12cfe-ec24-4349-a12c-d87d043a2f49" -->
### Precedence

1. **Bash Wrapper** (highest)
   - If wrapper adds `--dangerously-skip-permissions`, that takes effect

2. **Command-Line Flags**
   - Flags passed to the wrapper are forwarded

3. **Configuration Files**
   - `.claude/settings.json` and `.claude/settings.local.json`
   - Still respected when wrapper doesn't add bypass flag

<!-- section_id: "9c27e33b-b4f3-4da9-a52d-104b283d4fa6" -->
### Example: Hybrid Approach

```bash
# ~/.bashrc - Project directory gets wrapper bypass
claude() {
  if [[ "$PWD" == "/home/username/code/personal"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

```json
// /home/username/code/work-project/.claude/settings.local.json
// Work project uses fine-grained permissions
{
  "permissions": {
    "allow": [
      "Read(src/**)",
      "Edit(src/**)",
      "Bash(npm test)"
    ]
  }
}
```

**Result:**
- Personal projects: Full bypass via wrapper
- Work projects: Fine-grained permissions via config files
- Other directories: Default Claude Code behavior

<!-- section_id: "7e012d54-38a4-4814-a8c5-aa5938e82455" -->
## Frequently Asked Questions

<!-- section_id: "365ae38d-a436-4e8c-8dac-b26be7f2e5ee" -->
### Q: Does this work with VS Code?

**A**: Only if you launch Claude Code from the terminal. If you launch VS Code from a GUI, it won't inherit your shell configuration.

**Workaround**: Set environment variables in VS Code settings:
```json
{
  "terminal.integrated.env.linux": {
    "CLAUDE_UNSAFE": "1"
  }
}
```

<!-- section_id: "0547df9f-5c6a-49b3-a739-d25a1ae399b4" -->
### Q: Can I use this with zsh?

**A**: Yes, the syntax is compatible. Just add the wrapper to `~/.zshrc` instead of `~/.bashrc`.

<!-- section_id: "b7f15732-4021-4e7e-9344-599993d2eda3" -->
### Q: What about fish shell?

**A**: Fish uses different syntax. Here's the equivalent:

```fish
# ~/.config/fish/functions/claude.fish
function claude
    set -l claude_real /home/username/.nvm/versions/node/v22.20.0/bin/claude

    # Check for help/version
    for arg in $argv
        switch $arg
            case --help -h --version -v
                command $claude_real $argv
                return
        end
    end

    # Enable bypass in project directory
    if string match -q "/home/username/code/my-project*" $PWD
        command $claude_real --dangerously-skip-permissions $argv
    else
        command $claude_real $argv
    end
end
```

<!-- section_id: "2ec005aa-11b3-4a92-be31-214cf292f6f1" -->
### Q: Can I check if bypass is active before running a command?

**A**: Yes, add a helper function:

```bash
claude-bypass-check() {
  if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/trusted"* ]]; then
    echo "✅ Bypass ACTIVE"
  else
    echo "❌ Bypass INACTIVE (normal permissions)"
  fi
}
```

Usage:
```bash
$ claude-bypass-check
✅ Bypass ACTIVE
```

<!-- section_id: "7d00a464-3931-45c3-89ca-7152fca05ac8" -->
### Q: How do I share this with my team?

**A**: Document it in your project's README and provide a setup script:

```bash
#!/bin/bash
# scripts/setup-claude-wrapper.sh

CLAUDE_PATH=$(which claude)
PROJECT_PATH=$(pwd)

cat >> ~/.bashrc << EOF

# Auto-generated Claude wrapper for $(basename "$PROJECT_PATH")
_claude_real="$CLAUDE_PATH"
if [ -x "\$_claude_real" ]; then
  claude() {
    for arg in "\$@"; do
      case "\$arg" in
        --help|-h|--version|-v)
          command "\$_claude_real" "\$@"
          return \$?
          ;;
      esac
    done

    if [[ "\$PWD" == "$PROJECT_PATH"* ]]; then
      command "\$_claude_real" --dangerously-skip-permissions "\$@"
    else
      command "\$_claude_real" "\$@"
    fi
  }
fi
EOF

echo "✅ Claude wrapper added to ~/.bashrc"
echo "Run: source ~/.bashrc"
```

<!-- section_id: "bed61383-05f4-4efd-b067-1312ab0d32eb" -->
## Related Documentation

- [Bypass Permissions Setup](./bypass-permissions-setup.md) - Configuration file approach
- [Fine-Grained Permissions](./fine-grained-permissions.md) - Alternative to bypass mode
- [Settings Hierarchy](./settings-hierarchy.md) - How settings interact

<!-- section_id: "bacb5e6f-3d3c-450d-a9ed-c8c03661a45d" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides advanced implementation patterns for Claude Code bypass permissions.*
