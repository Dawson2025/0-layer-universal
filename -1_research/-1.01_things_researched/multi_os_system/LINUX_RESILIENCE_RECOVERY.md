# Linux Resilience & Remote Recovery System

**Created**: 2026-01-21
**Status**: Implemented (2026-01-21)
**OS**: Ubuntu 24.04.3 LTS

---

## Overview

This document describes a Murphy's Law resilient recovery system for the Linux laptop. The goal is to ensure that **no matter what breaks**, you can always SSH into the system from the VPS and fix it using Claude Code.

---

## System Configuration

| Setting | Value |
|---------|-------|
| OS | Ubuntu 24.04.3 LTS |
| Encryption | None (no LUKS) |
| Network Manager | NetworkManager |
| Tailscale IP | 100.73.84.89 |
| Local IP | 10.200.164.45 (may change) |

---

## Failure Modes & Solutions

### Layer 1: Service Failures

| Failure | Solution | Status |
|---------|----------|--------|
| Tailscale crashes | Auto-restart via systemd | [x] Done |
| SSH crashes | Auto-restart via systemd | [x] Done |
| NetworkManager crashes | Auto-restart via systemd | [x] Done |
| SSH socket activation delays | Disable socket activation | [x] Done |

### Layer 2: Boot Failures

| Failure | Solution | Status |
|---------|----------|--------|
| GUI login loop | SSH still works via Tailscale | [x] Already works |
| Network not starting in rescue | Custom rescue-with-net.target | [x] Done |
| Kernel panic | Auto-reboot after 20s + watchdog | [x] Done |
| Bad kernel update | Keep multiple kernels in GRUB | [x] Done (2 kernels) |

### Layer 3: Filesystem/Config Corruption

| Failure | Solution | Status |
|---------|----------|--------|
| SSH keys deleted | Fallback to password auth | [x] Done |
| /etc corrupted | Regular backups | [ ] Manual |
| Root filesystem errors | Auto-fsck on boot | [x] Default |

### Layer 4: Hardware Level

| Failure | Solution | Status |
|---------|----------|--------|
| System hangs | Software watchdog auto-reboot | [x] Done |
| Complete unresponsiveness | Watchdog + GRUB recovery | [x] Done |

---

## Implementation Details

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

### 3. NetworkManager Auto-Restart

File: `/etc/systemd/system/NetworkManager.service.d/override.conf`

```ini
[Service]
Restart=on-failure
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5
```

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

### 5. SSH Fallback to Password Auth

File: `/etc/ssh/sshd_config.d/99-fallback.conf`

```
# Enable both key-based and password authentication for recovery
PubkeyAuthentication yes
PasswordAuthentication yes
PermitRootLogin yes
```

### 6. Hardware Watchdog

File: `/etc/systemd/system.conf` (add to [Manager] section)

```ini
[Manager]
RuntimeWatchdogSec=30s
ShutdownWatchdogSec=30s
```

### 7. GRUB Configuration

File: `/etc/default/grub`

```bash
GRUB_DEFAULT=0
GRUB_TIMEOUT=5
GRUB_TIMEOUT_STYLE=menu
GRUB_CMDLINE_LINUX="panic=20"
```

### 8. Kernel Panic Auto-Reboot

The `panic=20` kernel parameter makes the system automatically reboot 20 seconds after a kernel panic.

---

## Health Check Scripts

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

## Emergency Recovery Procedure

### When GUI Breaks (Login Loop, etc.)

1. **From iPhone**: Open Termius
2. **Connect to VPS**: Use `tailscale_for_iphone_to_vps`
3. **On VPS**: Run `ssh dawson@100.73.84.89` (Linux laptop Tailscale IP)
4. **On Linux**: Start Claude Code with `claude`
5. **Use Claude**: To diagnose and fix the issue

### When SSH via Tailscale Fails

1. Boot into rescue mode: Add `systemd.unit=rescue-with-net.target` to GRUB
2. If on same network: Try local IP (10.200.164.x)
3. If all else fails: Use recovery USB

### When Everything Fails

1. Boot from Ubuntu Live USB
2. Mount root filesystem: `sudo mount /dev/sdaX /mnt`
3. Chroot: `sudo chroot /mnt`
4. Repair GRUB: `grub-install /dev/sda && update-grub`
5. Check/repair filesystem: `fsck -y /dev/sdaX`

---

## Backup Strategy

### Critical Files to Backup

- `/root/.ssh/` - SSH keys
- `/home/dawson/.ssh/` - User SSH keys
- `/etc/ssh/` - SSH server config
- `/etc/systemd/system/` - Custom systemd units
- `/etc/netplan/` - Network configuration

### Backup Location

Store encrypted backups on VPS:
```bash
tar czf - /root/.ssh /home/dawson/.ssh /etc/ssh | \
  gpg --symmetric --cipher-algo AES256 | \
  ssh dawson@100.93.148.5 "cat > /home/dawson/backups/linux-laptop-ssh-$(date +%Y%m%d).tar.gz.gpg"
```

---

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

## Related Files

- `TERMIUS_SSH_ARCHITECTURE.md` - SSH connection setup
- `STATUS.md` - Multi-OS workspace status
- `DEVICE_IDS.md` - Device identifiers and IPs
