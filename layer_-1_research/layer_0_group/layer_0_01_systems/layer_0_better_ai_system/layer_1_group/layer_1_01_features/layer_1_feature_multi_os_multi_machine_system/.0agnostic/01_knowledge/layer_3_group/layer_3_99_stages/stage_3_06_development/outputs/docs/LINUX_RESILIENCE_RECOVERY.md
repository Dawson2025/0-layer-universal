---
resource_id: "a08196be-ab3f-4222-a81e-b127e7bf9235"
resource_type: "knowledge"
resource_name: "LINUX_RESILIENCE_RECOVERY"
---
# Linux Resilience & Remote Recovery System

**Created**: 2026-01-21
**Status**: Implemented (2026-01-21)
**OS**: Ubuntu 24.04.3 LTS

---

<!-- section_id: "9ddaaeb2-815c-4e90-b0a6-7c302865bd86" -->
## Overview

This document describes a Murphy's Law resilient recovery system for the Linux laptop. The goal is to ensure that **no matter what breaks**, you can always SSH into the system from the VPS and fix it using Claude Code.

---

<!-- section_id: "44a697df-60df-4c7b-9731-eb176ba75cfc" -->
## System Configuration

| Setting | Value |
|---------|-------|
| OS | Ubuntu 24.04.3 LTS |
| Encryption | None (no LUKS) |
| Network Manager | NetworkManager |
| Tailscale IP | 100.73.84.89 |
| Local IP | 10.200.164.45 (may change) |

---

<!-- section_id: "86e06dde-6fad-4625-804f-1428b3133902" -->
## Failure Modes & Solutions

<!-- section_id: "475a8cd3-9152-41ac-b845-091013ad497b" -->
### Layer 1: Service Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Tailscale crashes | Auto-restart via systemd | [x] Done |
| SSH crashes | Auto-restart via systemd | [x] Done |
| NetworkManager crashes | Auto-restart via systemd | [x] Done |
| SSH socket activation delays | Disable socket activation | [x] Done |

<!-- section_id: "f73dfd26-dbd7-42e0-b2bc-e9a52213e612" -->
### Layer 2: Boot Failures

| Failure | Solution | Status |
|---------|----------|--------|
| GUI login loop | SSH still works via Tailscale | [x] Already works |
| Network not starting in rescue | Custom rescue-with-net.target | [x] Done |
| Kernel panic | Auto-reboot after 20s + watchdog | [x] Done |
| Bad kernel update | Keep multiple kernels in GRUB | [x] Done (2 kernels) |

<!-- section_id: "d0866053-6874-4db6-adfc-514b00f997df" -->
### Layer 3: Filesystem/Config Corruption

| Failure | Solution | Status |
|---------|----------|--------|
| SSH keys deleted | Fallback to password auth | [x] Done |
| /etc corrupted | Regular backups | [ ] Manual |
| Root filesystem errors | Auto-fsck on boot | [x] Default |

<!-- section_id: "43cd65f6-4063-4264-be87-d08a3dd769a4" -->
### Layer 4: Hardware Level

| Failure | Solution | Status |
|---------|----------|--------|
| System hangs | Software watchdog auto-reboot | [x] Done |
| Complete unresponsiveness | Watchdog + GRUB recovery | [x] Done |

---

<!-- section_id: "cc807f0f-0d6a-4783-bf13-67181b615f1e" -->
## Implementation Details

<!-- section_id: "6e6b8511-ab63-4a60-b5e6-33382370fc77" -->
### 1. Tailscale Auto-Restart & Readiness

File: `/etc/systemd/system/tailscaled.service.d/override.conf`

```ini
[Service]
Restart=on-failure
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5
TimeoutStopSec=15
ExecStartPost=timeout 60s bash -c 'until tailscale status --peers=false; do sleep 1; done'
```

<!-- section_id: "7cff89d0-4789-4bed-8e66-871d5764c556" -->
### 2. SSH Always-On (Disable Socket Activation)

```bash
sudo systemctl disable --now ssh.socket
sudo systemctl enable ssh.service
```

File: `/etc/systemd/system/ssh.service.d/override.conf`

```ini
[Service]
Restart=on-failure
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5

[Unit]
After=tailscaled.service
Wants=tailscaled.service
```

<!-- section_id: "cb1f1d32-c04f-476c-9172-b1784c354353" -->
### 3. NetworkManager Auto-Restart

File: `/etc/systemd/system/NetworkManager.service.d/override.conf`

```ini
[Service]
Restart=on-failure
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5
```

<!-- section_id: "22cb4383-c1e3-4b9a-bc66-c09036ff6d89" -->
### 4. Custom Rescue Target with Networking

File: `/etc/systemd/system/rescue-with-net.target`

```ini
[Unit]
Description=Rescue Mode with Networking
Documentation=man:systemd.special(7)
Requires=rescue.target
Wants=NetworkManager.service NetworkManager-wait-online.service tailscaled.service ssh.service
After=rescue.target NetworkManager.service NetworkManager-wait-online.service tailscaled.service
AllowIsolate=yes

[Install]
WantedBy=rescue.target
```

<!-- section_id: "627a8533-d7b9-4709-b2f0-e926b8f8e835" -->
### 5. SSH Fallback to Password Auth

File: `/etc/ssh/sshd_config.d/99-fallback.conf`

```
# Enable both key-based and password authentication for recovery
PubkeyAuthentication yes
PasswordAuthentication yes
PermitRootLogin yes
```

<!-- section_id: "2e934b1a-6842-4f1f-a8cf-4baf75e198fb" -->
### 6. Hardware Watchdog

File: `/etc/systemd/system.conf` (add to [Manager] section)

```ini
[Manager]
RuntimeWatchdogSec=30s
ShutdownWatchdogSec=30s
```

<!-- section_id: "9952bcf1-e4bc-455a-8662-fd664aadee4e" -->
### 7. GRUB Configuration

File: `/etc/default/grub`

```bash
GRUB_DEFAULT=0
GRUB_TIMEOUT=5
GRUB_TIMEOUT_STYLE=menu
GRUB_CMDLINE_LINUX="panic=20"
```

<!-- section_id: "f54a79e7-1cce-4e8c-beab-db35aaa15df3" -->
### 8. Kernel Panic Auto-Reboot

The `panic=20` kernel parameter makes the system automatically reboot 20 seconds after a kernel panic.

---

<!-- section_id: "e2bab355-5106-4c0a-8ce4-c2b8d1310a97" -->
## Health Check Scripts

<!-- section_id: "d02ca395-6642-41e6-847e-a19536aa8c29" -->
### Tailscale Health Check

File: `/usr/local/bin/tailscale-health-check.sh`

```bash
#!/bin/bash
if ! tailscale status --peers=false &>/dev/null; then
    echo "Tailscale unresponsive, restarting..."
    sudo systemctl restart tailscaled
fi
```

Cron: `/etc/cron.d/tailscale-monitor`
```
*/5 * * * * root /usr/local/bin/tailscale-health-check.sh
```

<!-- section_id: "aaa23b96-6a05-4ad0-a28c-c9594822537e" -->
### SSH Key Permission Monitor

File: `/usr/local/bin/ssh-key-monitor.sh`

```bash
#!/bin/bash
for dir in /root/.ssh /home/*/.ssh; do
    if [ -d "$dir" ]; then
        chmod 700 "$dir" 2>/dev/null
        chmod 600 "$dir/authorized_keys" 2>/dev/null
    fi
done
```

---

<!-- section_id: "01d2cefb-5472-4390-8715-45c2bc146ba8" -->
## AI CLI Tools (System-Wide)

All AI coding assistants are installed system-wide for access by any user including root and rescue mode.

| Tool | Command | Version | Location |
|------|---------|---------|----------|
| Claude Code | `claude` | 2.1.14 | /usr/bin/claude |
| Gemini CLI | `gemini` | 0.25.0 | /usr/bin/gemini |
| OpenAI Codex | `codex` | 0.87.0 | /usr/bin/codex |
| OpenCode | `opencode` | latest | /usr/bin/opencode |

<!-- section_id: "c349d034-3a89-4b22-bdf0-3f6ba3816e70" -->
### Root Access Configuration

- Auth configs copied to `/root/.claude/`, `/root/.codex/`, `/root/.gemini/`
- API keys in `/root/.bashrc`
- System profile at `/etc/profile.d/ai-cli-tools.sh`

<!-- section_id: "3bb8b543-e468-4016-a29d-deb25297b0a7" -->
### Quick Aliases

```bash
ai-claude    # Claude Code
ai-gemini    # Gemini CLI
ai-codex     # OpenAI Codex
ai-opencode  # OpenCode
```

---

<!-- section_id: "4140622d-2590-4d71-b752-414fd1922d14" -->
## Emergency Recovery Procedure

<!-- section_id: "aa55fb56-eee1-4d2a-b0d5-f0a4418ca4d1" -->
### When GUI Breaks (Login Loop, etc.)

1. **From iPhone**: Open Termius
2. **Connect to VPS**: Use `tailscale_for_iphone_to_vps`
3. **On VPS**: Run `ssh dawson@100.73.84.89` (Linux laptop Tailscale IP)
4. **On Linux**: Start any AI assistant:
   - `claude` - Claude Code (recommended)
   - `gemini` - Gemini CLI
   - `codex` - OpenAI Codex
   - `opencode` - OpenCode (multi-provider)
5. **Use AI**: To diagnose and fix the issue

<!-- section_id: "acafaa2a-554d-4dcf-bf16-ce11caddacfa" -->
### When SSH via Tailscale Fails

1. Boot into rescue mode: Add `systemd.unit=rescue-with-net.target` to GRUB
2. If on same network: Try local IP (10.200.164.x)
3. If all else fails: Use recovery USB

<!-- section_id: "16d19e42-39a8-4bd1-a56d-aa2208f67ae1" -->
### When Everything Fails

1. Boot from Ubuntu Live USB
2. Mount root filesystem: `sudo mount /dev/sdaX /mnt`
3. Chroot: `sudo chroot /mnt`
4. Repair GRUB: `grub-install /dev/sda && update-grub`
5. Check/repair filesystem: `fsck -y /dev/sdaX`

---

<!-- section_id: "3329d327-528e-4d6f-9922-fe92c0200bfd" -->
## Backup Strategy

<!-- section_id: "eef1615d-871b-4149-9169-89282429b1fc" -->
### Critical Files to Backup

- `/root/.ssh/` - SSH keys
- `/home/dawson/.ssh/` - User SSH keys
- `/etc/ssh/` - SSH server config
- `/etc/systemd/system/` - Custom systemd units
- `/etc/netplan/` - Network configuration

<!-- section_id: "05ad332d-a882-4702-848d-557344a21412" -->
### Backup Location

Store encrypted backups on VPS:
```bash
tar czf - /root/.ssh /home/dawson/.ssh /etc/ssh | \
  gpg --symmetric --cipher-algo AES256 | \
  ssh dawson@100.93.148.5 "cat > /home/dawson/backups/linux-laptop-ssh-$(date +%Y%m%d).tar.gz.gpg"
```

---

<!-- section_id: "9403b316-1251-44f1-b082-841b5011873d" -->
## Testing Checklist

- [ ] Kill tailscaled, verify it auto-restarts within 5s
- [ ] Kill sshd, verify it auto-restarts within 5s
- [ ] Kill NetworkManager, verify it auto-restarts within 5s
- [ ] Boot to rescue-with-net.target, verify network and SSH work
- [ ] Delete SSH keys, verify password auth works as fallback
- [ ] Verify watchdog device exists: `sudo wdctl`
- [ ] Test SSH from VPS to Linux via Tailscale
- [ ] Test SSH from VPS to Linux via local IP (when on same network)

---

<!-- section_id: "05214c95-c955-4d9c-b579-2891b91a27d8" -->
## Related Files

- `TERMIUS_SSH_ARCHITECTURE.md` - SSH connection setup
- `STATUS.md` - Multi-OS workspace status
- `DEVICE_IDS.md` - Device identifiers and IPs
