# Specification: Fix Linux Login Loop via Cloud Server SSH

**Layer**: 0 (Universal)
**Stage**: 0.01 Instructions
**Created**: 2026-01-17
**Related Request**: `REQUEST_fix_linux_login_loop_via_cloud_ssh.md`

---

## Technical Specification

### System Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   Phone     │────▶│ Cloud Server │────▶│ Linux Ubuntu │
│  (User)     │ SSH │  (Syncthing) │ SSH │  (Login Loop)│
└─────────────┘     └──────────────┘     └──────────────┘
                           │
                    ┌──────┴──────┐
                    │  AI CLIs    │
                    │ - Gemini    │
                    │ - Claude    │
                    │ - Codex     │
                    └─────────────┘
```

---

## Component Specifications

### 1. Cloud Server AI CLI Setup

#### 1.1 Gemini CLI
- **Package**: `@google/gemini-cli`
- **Environment Variable**: `GOOGLE_API_KEY`
- **API Key**: `AIzaSyCoGDYmISEIK4PI-mQno4EhShL0Jp6RY2I`
- **Usage**: `gemini "prompt"`

#### 1.2 Claude Code CLI
- **Package**: `@anthropic-ai/claude-code`
- **Authentication**: Browser login OR `ANTHROPIC_API_KEY`
- **Usage**: `claude` (interactive) or `claude "prompt"`

#### 1.3 Codex CLI
- **Package**: `@openai/codex`
- **Environment Variable**: `OPENAI_API_KEY`
- **Usage**: `codex "prompt"`

### 2. Linux Login Loop Fix

#### 2.1 Common Causes & Fixes

| Cause | Diagnostic | Fix Command |
|-------|------------|-------------|
| Corrupt .Xauthority | `ls -la ~/.Xauthority` | `rm ~/.Xauthority` |
| Corrupt .ICEauthority | `ls -la ~/.ICEauthority` | `rm ~/.ICEauthority` |
| Wrong permissions | `ls -la ~` | `chown -R user:user ~` |
| Full disk | `df -h` | Clear space in `/` or `/home` |
| Broken display manager | `systemctl status gdm3` | `apt install --reinstall gdm3` |
| GPU driver issue | `nvidia-smi` fails | Reinstall or remove nvidia drivers |
| Bad .bashrc/.profile | Errors on source | Fix or rename the file |

#### 2.2 Fix Script Location
```
/home/dawson/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/
  └── 0.02_sub_layers/sub_layer_0.05-0.014_setup/0.01_universal_setup_file_tree_0/
      └── 0.02_operating_systems/linux_ubuntu/setup/trickle_down_0.5_setup/
          └── 0_instruction_docs/setup/
              ├── fix_linux_login_loop.sh
              └── cloud_server_ai_cli_master_setup.sh
```

---

## SSH Connection Specification

### Prerequisites
- SSH server running on Linux: `systemctl status sshd`
- Network connectivity between cloud server and Linux machine
- Known IP address or hostname of Linux machine
- SSH key or password authentication configured

### Connection Command
```bash
ssh dawson@<linux-ip-address>
```

### If SSH Not Set Up
From Linux TTY (Ctrl+Alt+F2):
```bash
# Install SSH server if not installed
sudo apt install openssh-server

# Start SSH service
sudo systemctl start sshd
sudo systemctl enable sshd

# Get IP address
ip addr | grep "inet "
```

---

## File Paths Reference

### On Windows
```
C:\Users\Dawson\dawson-workspace\code\0_ai_context\...
```

### On Linux
```
/home/dawson/dawson-workspace/code/0_ai_context/...
```

### On Cloud Server (if synced to home)
```
~/dawson-workspace/code/0_ai_context/...
```

---

## Error Handling

### If Gemini API Key Invalid
1. Verify key is correct
2. Check for copy/paste errors (hidden characters)
3. Try without quotes: `export GOOGLE_API_KEY=key`
4. Regenerate key at https://aistudio.google.com/apikey

### If SSH Connection Refused
1. Check if sshd is running on Linux
2. Check firewall: `sudo ufw status`
3. Check if port 22 is open: `ss -tlnp | grep 22`

### If Scripts Not Synced
1. Check Syncthing status on cloud server
2. Wait for sync to complete
3. Manually copy script content if urgent
