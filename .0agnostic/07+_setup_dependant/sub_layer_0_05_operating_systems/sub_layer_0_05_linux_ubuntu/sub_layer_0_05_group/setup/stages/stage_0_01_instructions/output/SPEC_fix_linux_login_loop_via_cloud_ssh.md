---
resource_id: "67ca0abc-b52a-40ab-aabf-aaf69ab0b6e7"
resource_type: "document"
resource_name: "SPEC_fix_linux_login_loop_via_cloud_ssh"
---
# Specification: Fix Linux Login Loop via Cloud Server SSH

**Layer**: 0 (Universal)
**Stage**: 0.01 Instructions
**Created**: 2026-01-17
**Related Request**: `REQUEST_fix_linux_login_loop_via_cloud_ssh.md`

---

<!-- section_id: "8be46072-ec0e-4713-a849-b2558e321f2b" -->
## Technical Specification

<!-- section_id: "abaac125-a927-4e92-b232-c1435caf951e" -->
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

<!-- section_id: "c0298181-d192-4ec3-abd5-7d02f29c46b5" -->
## Component Specifications

<!-- section_id: "b4edf373-b9ac-4b94-bb16-90712e03332b" -->
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

<!-- section_id: "a983a0a6-2e95-4f76-b756-37f46fbcd45f" -->
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
  └── 0.02_sub_layers/sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/
      └── 0.02_operating_systems/linux_ubuntu/setup/trickle_down_0.5_setup/
          └── 0_instruction_docs/setup/
              ├── fix_linux_login_loop.sh
              └── cloud_server_ai_cli_master_setup.sh
```

---

<!-- section_id: "352a734c-c0f2-4c23-af86-17c25f3a3779" -->
## SSH Connection Specification

<!-- section_id: "ea902321-1a4d-405f-9b31-a54d3674a53f" -->
### Prerequisites
- SSH server running on Linux: `systemctl status sshd`
- Network connectivity between cloud server and Linux machine
- Known IP address or hostname of Linux machine
- SSH key or password authentication configured

<!-- section_id: "4d379a71-74f7-48b8-b8a1-8ca95350acda" -->
### Connection Command
```bash
ssh dawson@<linux-ip-address>
```

<!-- section_id: "5ffcd830-986a-4ea1-bdc9-ec938e00bf95" -->
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

<!-- section_id: "d7046836-e334-4f80-bef1-83bdd5c4acc3" -->
## File Paths Reference

<!-- section_id: "31bedbc4-a86c-40d7-8e9e-a789bd99c6f8" -->
### On Windows
```
C:\Users\Dawson\dawson-workspace\code\0_ai_context\...
```

<!-- section_id: "9fdc6292-4a4a-4808-ad37-ed90a9943d7c" -->
### On Linux
```
/home/dawson/dawson-workspace/code/0_ai_context/...
```

<!-- section_id: "a150cd4c-0f4d-473f-95d2-23a9195c19ed" -->
### On Cloud Server (if synced to home)
```
~/dawson-workspace/code/0_ai_context/...
```

---

<!-- section_id: "caf3c71c-9d89-4175-b79f-f92dc7b3839c" -->
## Error Handling

<!-- section_id: "1bbc7484-5fcc-4c68-8669-9c1906a2c322" -->
### If Gemini API Key Invalid
1. Verify key is correct
2. Check for copy/paste errors (hidden characters)
3. Try without quotes: `export GOOGLE_API_KEY=key`
4. Regenerate key at https://aistudio.google.com/apikey

<!-- section_id: "2a337f13-2e28-4cd0-916e-98a79aeb6a92" -->
### If SSH Connection Refused
1. Check if sshd is running on Linux
2. Check firewall: `sudo ufw status`
3. Check if port 22 is open: `ss -tlnp | grep 22`

<!-- section_id: "8170fb6f-1dc4-483d-9490-709b9e993b8d" -->
### If Scripts Not Synced
1. Check Syncthing status on cloud server
2. Wait for sync to complete
3. Manually copy script content if urgent
